r"""Build deterministic per-instrument evidence bundles for AIMS.

Fetches per-symbol news via yfinance and curated macro RSS/Atom feeds
(stdlib XML parsing only), normalizes them into a schema-validated
``data/evidence/<stem>.json`` bundle with per-source and per-asset-class
coverage accounting. Fetched text is untrusted data: markup is stripped,
lengths are capped, and content is never interpreted as instructions.

Usage:
    uv run .agents/skills/qualitative-analysis/scripts/fetch_evidence.py \
        --mapping data/mappings/canonical_instrument_mappings.csv \
        --sources data/mappings/evidence_sources.csv \
        --analysis-date 2026-07-04 \
        --output data/evidence/
"""

from __future__ import annotations

import argparse
import csv
import email.utils
import hashlib
import html
import json
import re
import subprocess
import urllib.request

# Bundles fetch only curated feeds and provider news; entities/DTDs are not
# resolved by ElementTree.fromstring, and all text is length-capped after.
import xml.etree.ElementTree as ET  # noqa: S405
from collections.abc import Callable
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from operator import itemgetter
from pathlib import Path
from typing import TYPE_CHECKING, Any, Final

import yfinance as yf

if TYPE_CHECKING:
    from aims.market_analysis import InstrumentMappingRow

EVIDENCE_VERSION: Final[str] = "1.0.0"

DEFAULT_LOOKBACK_DAYS: Final[int] = 7
MAX_ITEMS_PER_INSTRUMENT: Final[int] = 5
MAX_ITEMS_PER_SOURCE: Final[int] = 10
TITLE_MAX_CHARS: Final[int] = 300
SNIPPET_MAX_CHARS: Final[int] = 500

CATEGORY_INSTRUMENT_NEWS: Final[str] = "instrument_news"
CATEGORY_MACRO: Final[str] = "macro"

_DEFAULT_OUTPUT_DIR: Final[Path] = Path("data/evidence")
_FETCH_TIMEOUT: Final[int] = 20
_NEWS_FETCH_COUNT: Final[int] = 8
_USER_AGENT: Final[str] = "Mozilla/5.0 (compatible; aims-evidence/1.0)"
_TAG_RE: Final[re.Pattern[str]] = re.compile(r"<[^>]+>")
_WS_RE: Final[re.Pattern[str]] = re.compile(r"\s+")

FetchUrl = Callable[[str], str]
FetchNews = Callable[[str], list[dict[str, Any]]]


@dataclass(frozen=True)
class EvidenceSource:
    """One curated macro feed from evidence_sources.csv."""

    source_id: str
    name: str
    url: str
    category: str
    asset_classes: tuple[str, ...]


@dataclass(frozen=True)
class EvidenceInstrument:
    """One canonical instrument the bundle covers."""

    canonical_id: str
    symbol: str
    asset_class: str


def git_commit() -> str:
    """Return the short git commit for artifact provenance metadata."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError:
        return "unknown"
    return result.stdout.strip() if result.returncode == 0 else "unknown"


def load_evidence_sources(path: Path) -> list[EvidenceSource]:
    """Load and parse evidence_sources.csv, sorted by source_id."""
    with path.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    sources = [
        EvidenceSource(
            source_id=row.get("source_id", "").strip(),
            name=row.get("name", "").strip(),
            url=row.get("url", "").strip(),
            category=row.get("category", "").strip(),
            asset_classes=tuple(
                part for part in row.get("asset_classes", "").strip().split("|") if part
            ),
        )
        for row in rows
    ]
    return sorted(sources, key=lambda s: s.source_id)


def instruments_from_mappings(
    rows: list[InstrumentMappingRow],
    provider: str,
    interval: str,
) -> list[EvidenceInstrument]:
    """Return unique instruments for *provider*/*interval*, by canonical_id."""
    result: dict[str, EvidenceInstrument] = {}
    for row in rows:
        if (
            row.provider == provider
            and row.provider_interval == interval
            and row.canonical_id not in result
        ):
            result[row.canonical_id] = EvidenceInstrument(
                canonical_id=row.canonical_id,
                symbol=row.provider_symbol,
                asset_class=row.asset_class,
            )
    return [result[cid] for cid in sorted(result)]


def clean_text(value: str, limit: int) -> str:
    """Strip markup, unescape entities, collapse whitespace, cap length."""
    text = html.unescape(_TAG_RE.sub(" ", value))
    text = _WS_RE.sub(" ", text).strip()
    return text[:limit]


def evidence_id(url: str, published_at: str) -> str:
    """Stable evidence ID: hash of canonical URL + published timestamp."""
    digest = hashlib.sha256(f"{url}|{published_at}".encode()).hexdigest()
    return f"ev-{digest[:16]}"


def parse_timestamp(value: str) -> str | None:
    """Parse an RFC 822 or ISO 8601 timestamp into UTC ISO format."""
    text = value.strip()
    if not text:
        return None
    try:
        parsed = email.utils.parsedate_to_datetime(text)
    except (TypeError, ValueError):
        parsed = None
    if parsed is None:
        try:
            parsed = datetime.fromisoformat(text)
        except ValueError:
            return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=UTC)
    return parsed.astimezone(UTC).isoformat()


def fetch_url(url: str) -> str:
    """Fetch *url* and return its decoded body (network boundary)."""
    request = urllib.request.Request(url, headers={"User-Agent": _USER_AGENT})
    with urllib.request.urlopen(request, timeout=_FETCH_TIMEOUT) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        body: str = resp.read().decode(charset, errors="replace")
    return body


def fetch_symbol_news(symbol: str) -> list[dict[str, Any]]:
    """Fetch raw news items for *symbol* via yfinance (network boundary)."""
    news: list[dict[str, Any]] = yf.Ticker(symbol).get_news(count=_NEWS_FETCH_COUNT)
    return news


def _element_text(parent: ET.Element, tag: str) -> str:
    node = parent.find(tag)
    return (node.text or "") if node is not None else ""


def _atom_link(entry: ET.Element) -> str:
    node = entry.find("{http://www.w3.org/2005/Atom}link")
    return node.get("href", "") if node is not None else ""


def parse_feed(xml_text: str) -> list[dict[str, str]]:
    """Parse an RSS 2.0 or Atom feed into raw entry dicts via stdlib XML."""
    root = ET.fromstring(xml_text.lstrip("﻿"))  # noqa: S314
    atom = "{http://www.w3.org/2005/Atom}"
    entries: list[dict[str, str]] = [
        {
            "title": _element_text(item, "title"),
            "url": _element_text(item, "link").strip(),
            "published": _element_text(item, "pubDate"),
            "summary": _element_text(item, "description"),
        }
        for item in root.iter("item")
    ]
    entries.extend(
        {
            "title": _element_text(entry, f"{atom}title"),
            "url": _atom_link(entry),
            "published": _element_text(entry, f"{atom}published")
            or _element_text(entry, f"{atom}updated"),
            "summary": _element_text(entry, f"{atom}summary"),
        }
        for entry in root.iter(f"{atom}entry")
    )
    return entries


def normalize_news_item(raw: dict[str, Any]) -> dict[str, str] | None:
    """Normalize a yfinance news item into a raw entry dict."""
    content: dict[str, Any] = raw.get("content") or raw
    url = (
        (content.get("canonicalUrl") or {}).get("url")
        or (content.get("clickThroughUrl") or {}).get("url")
        or content.get("link")
        or ""
    )
    title = content.get("title") or ""
    published = str(content.get("pubDate") or content.get("displayTime") or "")
    if not url or not title:
        return None
    return {
        "title": str(title),
        "url": str(url),
        "published": published,
        "summary": str(content.get("summary") or content.get("description") or ""),
        "source": str(
            (content.get("provider") or {}).get("displayName") or "yahoo-finance"
        ),
    }


def _build_item(
    entry: dict[str, str],
    *,
    source: str,
    category: str,
    canonical_ids: list[str],
    asset_classes: list[str],
) -> dict[str, Any] | None:
    title = clean_text(entry.get("title", ""), TITLE_MAX_CHARS)
    url = entry.get("url", "")
    published_at = parse_timestamp(entry.get("published", ""))
    if not title or not url or published_at is None:
        return None
    return {
        "id": evidence_id(url, published_at),
        "title": title,
        "source": source,
        "url": url,
        "published_at": published_at,
        "snippet": clean_text(entry.get("summary", ""), SNIPPET_MAX_CHARS),
        "category": category,
        "canonical_ids": canonical_ids,
        "asset_classes": asset_classes,
    }


def _in_window(published_at: str, analysis_date: str, lookback_days: int) -> bool:
    published = datetime.fromisoformat(published_at)
    day = datetime.fromisoformat(f"{analysis_date}T00:00:00+00:00")
    return day - timedelta(days=lookback_days) <= published <= day + timedelta(days=1)


def _newest_first(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(items, key=itemgetter("published_at", "id"), reverse=True)


def build_bundle(
    instruments: list[EvidenceInstrument],
    sources: list[EvidenceSource],
    *,
    analysis_date: str,
    interval: str = "d",
    lookback_days: int = DEFAULT_LOOKBACK_DAYS,
    retrieved_at: str | None = None,
    fetch_url_fn: FetchUrl = fetch_url,
    fetch_news_fn: FetchNews = fetch_symbol_news,
) -> dict[str, Any]:
    """Build a schema-shaped evidence bundle for *analysis_date*."""
    source_status: dict[str, dict[str, Any]] = {}
    items_by_id: dict[str, dict[str, Any]] = {}
    instruments_with_news: set[str] = set()

    for inst in instruments:
        key = f"yfinance:{inst.symbol}"
        try:
            raw_items = fetch_news_fn(inst.symbol)
        except Exception as exc:  # noqa: BLE001 - per-source failures are non-fatal
            source_status[key] = {"status": "failed", "error": str(exc)[:200]}
            continue
        candidates: list[dict[str, Any]] = []
        for raw in raw_items:
            entry = normalize_news_item(raw)
            if entry is None:
                continue
            item = _build_item(
                entry,
                source=entry["source"],
                category=CATEGORY_INSTRUMENT_NEWS,
                canonical_ids=[inst.canonical_id],
                asset_classes=[inst.asset_class],
            )
            if item is not None and _in_window(
                item["published_at"], analysis_date, lookback_days
            ):
                candidates.append(item)
        kept = _newest_first(candidates)[:MAX_ITEMS_PER_INSTRUMENT]
        for item in kept:
            existing = items_by_id.get(item["id"])
            if existing is not None:
                merged = sorted({*existing["canonical_ids"], inst.canonical_id})
                existing["canonical_ids"] = merged
            else:
                items_by_id[item["id"]] = item
        if kept:
            instruments_with_news.add(inst.canonical_id)
        source_status[key] = {"status": "success", "item_count": len(kept)}

    for source in sources:
        key = f"feed:{source.source_id}"
        try:
            entries = parse_feed(fetch_url_fn(source.url))
        except Exception as exc:  # noqa: BLE001 - per-source failures are non-fatal
            source_status[key] = {"status": "failed", "error": str(exc)[:200]}
            continue
        candidates = []
        for entry in entries:
            item = _build_item(
                entry,
                source=source.name,
                category=CATEGORY_MACRO,
                canonical_ids=[],
                asset_classes=list(source.asset_classes),
            )
            if item is not None and _in_window(
                item["published_at"], analysis_date, lookback_days
            ):
                candidates.append(item)
        kept = _newest_first(candidates)[:MAX_ITEMS_PER_SOURCE]
        for item in kept:
            items_by_id.setdefault(item["id"], item)
        source_status[key] = {"status": "success", "item_count": len(kept)}

    asset_class_coverage: dict[str, dict[str, int]] = {}
    for inst in instruments:
        stats = asset_class_coverage.setdefault(
            inst.asset_class, {"instruments": 0, "with_direct_news": 0}
        )
        stats["instruments"] += 1
        stats["with_direct_news"] += int(inst.canonical_id in instruments_with_news)

    items = sorted(items_by_id.values(), key=itemgetter("published_at", "id"))
    now = retrieved_at or datetime.now(tz=UTC).isoformat()
    return {
        "version": EVIDENCE_VERSION,
        "metadata": {
            "generated_at": f"{analysis_date}T00:00:00+00:00",
            "analysis_date": analysis_date,
            "interval": interval,
            "retrieved_at": now,
            "git_commit": git_commit(),
            "lookback_days": lookback_days,
            "coverage": {
                "sources": dict(sorted(source_status.items())),
                "instrument_count": len(instruments),
                "instruments_with_direct_news": sorted(instruments_with_news),
                "asset_classes": dict(sorted(asset_class_coverage.items())),
            },
        },
        "items": items,
    }


def bundle_stem(bundle: dict[str, Any]) -> str:
    """Return the date[-interval] filename stem for *bundle*."""
    meta = bundle["metadata"]
    interval = meta.get("interval", "d")
    suffix = "" if interval == "d" else f"-{interval}"
    return f"{meta['analysis_date']}{suffix}"


def save_bundle(
    bundle: dict[str, Any],
    output_dir: Path = _DEFAULT_OUTPUT_DIR,
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"{bundle_stem(bundle)}.json"
    path.write_text(
        json.dumps(bundle, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return path


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mapping",
        type=Path,
        default=Path("data/mappings/canonical_instrument_mappings.csv"),
        help="Path to canonical_instrument_mappings.csv",
    )
    parser.add_argument(
        "--sources",
        type=Path,
        default=Path("data/mappings/evidence_sources.csv"),
        help="Path to evidence_sources.csv",
    )
    parser.add_argument(
        "--analysis-date",
        required=True,
        help="Analysis date (YYYY-MM-DD) the bundle belongs to",
    )
    parser.add_argument("--interval", default="d", choices=["d", "w", "m"])
    parser.add_argument("--provider", default="yfinance")
    parser.add_argument("--lookback-days", type=int, default=DEFAULT_LOOKBACK_DAYS)
    parser.add_argument(
        "--retrieved-at",
        default=None,
        help="Override the retrieved_at timestamp (for reproducible tests)",
    )
    parser.add_argument("--output", type=Path, default=_DEFAULT_OUTPUT_DIR)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    from aims.market_analysis import load_instrument_mappings  # noqa: PLC0415

    try:
        rows = load_instrument_mappings(args.mapping)
        sources = load_evidence_sources(args.sources)
    except (FileNotFoundError, csv.Error) as exc:
        print(f"ERROR: {exc}")
        return 1
    instruments = instruments_from_mappings(rows, args.provider, args.interval)
    if not instruments:
        print(
            f"ERROR: no instruments in {args.mapping} for"
            f" provider={args.provider} interval={args.interval}"
        )
        return 1
    bundle = build_bundle(
        instruments,
        sources,
        analysis_date=args.analysis_date,
        interval=args.interval,
        lookback_days=args.lookback_days,
        retrieved_at=args.retrieved_at,
    )
    path = save_bundle(bundle, args.output)
    coverage = bundle["metadata"]["coverage"]
    failed = sorted(
        key for key, entry in coverage["sources"].items() if entry["status"] == "failed"
    )
    for key in failed:
        print(f"WARNING: fetch failed for source {key}")
    print(
        f"Evidence bundle written to {path}"
        f" ({len(bundle['items'])} items,"
        f" {len(failed)} failed source(s))"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
