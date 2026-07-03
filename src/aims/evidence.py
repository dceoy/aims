r"""Fetch and validate per-instrument news and macro evidence bundles.

Evidence bundles are committed, validated artifacts that the AI qualitative
analysis step may cite from — and nothing else. All fetched text is untrusted
data: it is stored (markup-stripped and length-capped), never interpreted as
instructions.

Usage:
    uv run .agents/skills/qualitative-analysis/scripts/fetch_evidence.py \
        fetch --mapping data/mappings/canonical_instrument_mappings.csv \
        --provider yfinance --interval d \
        --sources data/mappings/evidence_sources.csv \
        --analysis-date 2026-07-02 --output data/evidence/

    uv run .agents/skills/qualitative-analysis/scripts/fetch_evidence.py \
        validate --input data/evidence/2026-07-02.json
"""

from __future__ import annotations

import argparse
import csv
import email.utils
import hashlib
import html
import json
import re
import urllib.request
import xml.etree.ElementTree as ET  # noqa: S405
from dataclasses import dataclass
from datetime import UTC, date, datetime, timedelta
from pathlib import Path
from typing import Any, Final

import yfinance as yf

from aims.market_analysis import instrument_display_map, load_instrument_mappings

EVIDENCE_VERSION: Final[str] = "1.0.0"
DEFAULT_MAX_AGE_DAYS: Final[int] = 7
DEFAULT_OUTPUT_DIR: Final[Path] = Path("data/evidence")

_CATEGORIES: Final[tuple[str, ...]] = ("instrument_news", "macro")
_TITLE_LIMIT: Final[int] = 300
_SUMMARY_LIMIT: Final[int] = 500
_MAX_ITEMS_PER_SYMBOL: Final[int] = 10
_MAX_ITEMS_PER_FEED: Final[int] = 20
_MAX_FEED_BYTES: Final[int] = 1_048_576
_TIMEOUT: Final[int] = 30
_ID_LENGTH: Final[int] = 16
_ID_RE: Final[re.Pattern[str]] = re.compile(r"^[0-9a-f]{16}$")
_TAG_RE: Final[re.Pattern[str]] = re.compile(r"<[^>]+>")
_ATOM: Final[str] = "{http://www.w3.org/2005/Atom}"
_USER_AGENT: Final[str] = "aims-evidence/1.0 (+https://github.com/dceoy/aims)"


@dataclass(frozen=True)
class EvidenceSource:
    """One curated feed row from evidence_sources.csv."""

    name: str
    url: str
    category: str


def load_evidence_sources(path: Path) -> list[EvidenceSource]:
    """Load and parse the curated feed list CSV."""
    with path.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        return [
            EvidenceSource(
                name=row.get("name", ""),
                url=row.get("url", ""),
                category=row.get("category", ""),
            )
            for row in reader
            if row.get("name") and row.get("url")
        ]


def evidence_id(url: str, published_at: str) -> str:
    """Return the stable 16-hex-character identifier for an evidence item."""
    digest = hashlib.sha256(f"{url}|{published_at}".encode()).hexdigest()
    return digest[:_ID_LENGTH]


def _plain_text(value: str, limit: int) -> str:
    text = html.unescape(_TAG_RE.sub(" ", value))
    return " ".join(text.split())[:limit]


def _format_timestamp(value: Any) -> str | None:
    """Normalize a unix/ISO/RFC-822 timestamp to a UTC ISO string, or None."""
    parsed: datetime | None = None
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        try:
            parsed = datetime.fromtimestamp(float(value), tz=UTC)
        except (OverflowError, OSError, ValueError):
            return None
    elif isinstance(value, str) and value.strip():
        text = value.strip().replace("Z", "+00:00")
        try:
            parsed = datetime.fromisoformat(text)
        except ValueError:
            try:
                parsed = email.utils.parsedate_to_datetime(text)
            except ValueError:
                return None
    if parsed is None:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=UTC)
    return parsed.astimezone(UTC).isoformat()


def _build_item(
    *,
    title: Any,
    url: Any,
    published: Any,
    summary: Any,
    source: str,
    category: str,
    instruments: list[str],
    retrieved_at: str,
) -> dict[str, Any] | None:
    published_at = _format_timestamp(published)
    if (
        not isinstance(title, str)
        or not title.strip()
        or not isinstance(url, str)
        or not url.strip()
        or published_at is None
    ):
        return None
    url_text = url.strip()
    summary_text = (
        _plain_text(summary, _SUMMARY_LIMIT) if isinstance(summary, str) else ""
    )
    return {
        "id": evidence_id(url_text, published_at),
        "source": source,
        "category": category,
        "title": _plain_text(title, _TITLE_LIMIT),
        "url": url_text,
        "published_at": published_at,
        "retrieved_at": retrieved_at,
        "instruments": instruments,
        "summary": summary_text,
    }


def normalize_news_item(
    raw: dict[str, Any],
    *,
    symbol: str,
    canonical_id: str,
    retrieved_at: str,
) -> dict[str, Any] | None:
    """Normalize one yfinance news entry (old or new API shape), or None."""
    content_raw = raw.get("content")
    content = content_raw if isinstance(content_raw, dict) else raw
    canonical_url = content.get("canonicalUrl")
    url = (
        canonical_url.get("url")
        if isinstance(canonical_url, dict)
        else content.get("link")
    )
    return _build_item(
        title=content.get("title"),
        url=url,
        published=content.get("pubDate") or content.get("providerPublishTime"),
        summary=content.get("summary"),
        source=f"yfinance:{symbol}",
        category="instrument_news",
        instruments=[canonical_id],
        retrieved_at=retrieved_at,
    )


def _feed_entries(root: ET.Element) -> list[tuple[Any, Any, Any, Any]]:
    """Yield (title, url, published, summary) tuples from RSS 2.0 or Atom XML."""
    entries: list[tuple[Any, Any, Any, Any]] = []
    if root.tag == f"{_ATOM}feed":
        for entry in root.findall(f"{_ATOM}entry"):
            link_el = entry.find(f"{_ATOM}link")
            entries.append((
                entry.findtext(f"{_ATOM}title"),
                link_el.get("href") if link_el is not None else None,
                entry.findtext(f"{_ATOM}published")
                or entry.findtext(f"{_ATOM}updated"),
                entry.findtext(f"{_ATOM}summary") or "",
            ))
    else:
        entries.extend(
            (
                item.findtext("title"),
                item.findtext("link"),
                item.findtext("pubDate"),
                item.findtext("description") or "",
            )
            for item in root.iter("item")
        )
    return entries


def parse_feed(
    xml_text: str,
    *,
    source_name: str,
    retrieved_at: str,
    max_items: int = _MAX_ITEMS_PER_FEED,
) -> list[dict[str, Any]]:
    """Parse an RSS 2.0 or Atom feed document into normalized evidence items.

    Raises xml.etree.ElementTree.ParseError on malformed XML.
    """
    # Curated allowlisted institutional feeds, fetched size-capped; see
    # OPERATIONS.md for the trust boundary of the source list.
    root = ET.fromstring(xml_text)  # noqa: S314
    items: list[dict[str, Any]] = []
    for title, url, published, summary in _feed_entries(root):
        item = _build_item(
            title=title,
            url=url,
            published=published,
            summary=summary,
            source=f"feed:{source_name}",
            category="macro",
            instruments=[],
            retrieved_at=retrieved_at,
        )
        if item is not None:
            items.append(item)
        if len(items) >= max_items:
            break
    return items


def _http_get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": _USER_AGENT})
    with urllib.request.urlopen(req, timeout=_TIMEOUT) as resp:
        return resp.read(_MAX_FEED_BYTES).decode("utf-8", errors="replace")


def _fetch_symbol_news(symbol: str) -> list[Any]:
    news: Any = yf.Ticker(symbol).news
    return news if isinstance(news, list) else []


def build_bundle(
    items: list[dict[str, Any]],
    *,
    analysis_date: str,
    max_age_days: int,
    coverage: dict[str, Any],
    generated_at: str,
) -> dict[str, Any]:
    """Deduplicate, recency-filter, sort, and wrap evidence items."""
    day = date.fromisoformat(analysis_date)
    earliest = (day - timedelta(days=max_age_days)).isoformat()
    latest = (day + timedelta(days=1)).isoformat()
    seen: set[str] = set()
    kept: list[dict[str, Any]] = []
    for item in items:
        published_day = str(item["published_at"])[:10]
        if item["id"] in seen or not earliest <= published_day <= latest:
            continue
        seen.add(item["id"])
        kept.append(item)
    kept.sort(key=lambda i: (str(i["published_at"]), str(i["id"])))
    coverage_out = dict(coverage)
    coverage_out["item_count"] = len(kept)
    return {
        "version": EVIDENCE_VERSION,
        "metadata": {
            "generated_at": generated_at,
            "analysis_date": analysis_date,
            "max_age_days": max_age_days,
            "coverage": coverage_out,
        },
        "items": kept,
    }


def fetch_bundle(
    *,
    mapping_path: Path,
    provider: str,
    interval: str,
    sources_path: Path,
    analysis_date: str,
    max_age_days: int = DEFAULT_MAX_AGE_DAYS,
    now: datetime | None = None,
) -> dict[str, Any]:
    """Fetch news for all mapped instruments plus curated feeds into a bundle."""
    retrieved = (now or datetime.now(tz=UTC)).astimezone(UTC).isoformat()
    display_map = instrument_display_map(
        load_instrument_mappings(mapping_path), provider, interval
    )
    items: list[dict[str, Any]] = []

    news_failed: list[str] = []
    for symbol in sorted(display_map):
        canonical_id = display_map[symbol]["canonical_id"]
        try:
            raw_items = _fetch_symbol_news(symbol)
        except Exception as exc:  # noqa: BLE001 - provider errors are non-fatal
            print(f"WARNING: news fetch failed for {symbol}: {exc}")
            news_failed.append(symbol)
            continue
        normalized = [
            item
            for raw in raw_items
            if isinstance(raw, dict)
            and (
                item := normalize_news_item(
                    raw,
                    symbol=symbol,
                    canonical_id=canonical_id,
                    retrieved_at=retrieved,
                )
            )
            is not None
        ]
        items.extend(normalized[:_MAX_ITEMS_PER_SYMBOL])

    sources = load_evidence_sources(sources_path)
    feeds_failed: list[str] = []
    for source in sources:
        try:
            xml_text = _http_get(source.url)
            items.extend(
                parse_feed(xml_text, source_name=source.name, retrieved_at=retrieved)
            )
        except Exception as exc:  # noqa: BLE001 - feed errors are non-fatal
            print(f"WARNING: feed fetch failed for {source.name}: {exc}")
            feeds_failed.append(source.name)

    coverage = {
        "sources": {
            "yfinance_news": {
                "attempted": len(display_map),
                "fetched": len(display_map) - len(news_failed),
                "failed": news_failed,
            },
            "feeds": {
                "attempted": len(sources),
                "fetched": len(sources) - len(feeds_failed),
                "failed": feeds_failed,
            },
        },
    }
    return build_bundle(
        items,
        analysis_date=analysis_date,
        max_age_days=max_age_days,
        coverage=coverage,
        generated_at=retrieved,
    )


_REQUIRED_TOP: Final[tuple[str, ...]] = ("version", "metadata", "items")
_REQUIRED_META: Final[tuple[str, ...]] = (
    "generated_at",
    "analysis_date",
    "max_age_days",
    "coverage",
)
_REQUIRED_ITEM: Final[tuple[str, ...]] = (
    "id",
    "source",
    "category",
    "title",
    "url",
    "published_at",
    "retrieved_at",
    "instruments",
    "summary",
)


def validate_bundle(data: dict[str, Any]) -> list[str]:
    """Return a list of schema errors for an evidence bundle (empty when valid)."""
    errors = [
        f"missing required key: {key!r}" for key in _REQUIRED_TOP if key not in data
    ]
    if errors:
        return errors
    if data["version"] != EVIDENCE_VERSION:
        errors.append(
            f"unsupported version {data['version']!r} (expected {EVIDENCE_VERSION!r})"
        )
    metadata = data["metadata"]
    if not isinstance(metadata, dict):
        errors.append("'metadata' must be a JSON object")
    else:
        errors.extend(
            f"metadata missing required key: {key!r}"
            for key in _REQUIRED_META
            if key not in metadata
        )
        coverage = metadata.get("coverage")
        if coverage is not None and not isinstance(coverage, dict):
            errors.append("metadata.coverage must be a JSON object")
    items = data["items"]
    if not isinstance(items, list):
        errors.append("'items' must be a JSON array")
        return errors
    seen_ids: set[str] = set()
    for idx, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(f"item[{idx}] must be a JSON object")
            continue
        errors.extend(
            f"item[{idx}] missing required key: {key!r}"
            for key in _REQUIRED_ITEM
            if key not in item
        )
        item_id = item.get("id")
        if isinstance(item_id, str):
            if not _ID_RE.match(item_id):
                errors.append(f"item[{idx}]: id {item_id!r} is not 16 hex characters")
            if item_id in seen_ids:
                errors.append(f"item[{idx}]: duplicate id {item_id!r}")
            seen_ids.add(item_id)
        if item.get("category") not in _CATEGORIES:
            errors.append(
                f"item[{idx}]: category {item.get('category')!r} not in {_CATEGORIES}"
            )
        instruments = item.get("instruments")
        if not isinstance(instruments, list) or any(
            not isinstance(i, str) for i in instruments
        ):
            errors.append(f"item[{idx}]: instruments must be an array of strings")
        summary = item.get("summary")
        if isinstance(summary, str) and len(summary) > _SUMMARY_LIMIT:
            errors.append(f"item[{idx}]: summary exceeds {_SUMMARY_LIMIT} characters")
    return errors


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    fetch = sub.add_parser("fetch", help="Fetch news and feeds into a bundle")
    fetch.add_argument("--mapping", type=Path, required=True)
    fetch.add_argument("--provider", default="yfinance")
    fetch.add_argument("--interval", default="d")
    fetch.add_argument("--sources", type=Path, required=True)
    fetch.add_argument("--analysis-date", required=True, help="YYYY-MM-DD")
    fetch.add_argument("--max-age-days", type=int, default=DEFAULT_MAX_AGE_DAYS)
    fetch.add_argument("--output", type=Path, default=DEFAULT_OUTPUT_DIR)

    validate = sub.add_parser("validate", help="Validate an evidence bundle")
    validate.add_argument("--input", type=Path, required=True)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.command == "fetch":
        bundle = fetch_bundle(
            mapping_path=args.mapping,
            provider=args.provider,
            interval=args.interval,
            sources_path=args.sources,
            analysis_date=args.analysis_date,
            max_age_days=args.max_age_days,
        )
        args.output.mkdir(parents=True, exist_ok=True)
        path = args.output / f"{args.analysis_date}.json"
        path.write_text(json.dumps(bundle, indent=2) + "\n", encoding="utf-8")
        print(f"Evidence bundle written to {path}")
        return 0
    try:
        with args.input.open(encoding="utf-8") as fh:
            data = json.load(fh)
    except FileNotFoundError:
        print(f"ERROR: file not found: {args.input}")
        return 1
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON in {args.input}: {exc}")
        return 1
    errors = validate_bundle(data)
    if errors:
        for error in errors:
            print(error)
        return 1
    print(f"validated {args.input}: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
