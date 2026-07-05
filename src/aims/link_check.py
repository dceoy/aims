r"""Sample recent evidence citation URLs and warn about link rot.

Citation-validity sampling for the qualitative layer (#97): a bounded,
deterministic sample of citation URLs from recent committed evidence bundles
is probed over HTTP so rotting sources surface in workflow logs. This is a
**warning, not a gate** — the exit code is always 0 once arguments parse, no
artifact is written (network results are not deterministic and stay out of
committed data), and nothing downstream consumes the outcome.

Sampling is deterministic: bundles within the lookback window of the newest
bundle contribute their items, sorted by evidence ID, de-duplicated by URL,
and capped. Only the network responses vary run to run.

Usage:
    uv run .agents/skills/qualitative-analysis/scripts/check_citation_links.py \
        --evidence-dir data/evidence --days 14 --limit 20
"""

from __future__ import annotations

import argparse
import json
import re
import urllib.error
import urllib.request
from datetime import date, timedelta
from pathlib import Path
from typing import Any, Final

DEFAULT_DAYS: Final[int] = 14
DEFAULT_LIMIT: Final[int] = 20
DEFAULT_TIMEOUT: Final[float] = 10.0
_USER_AGENT: Final[str] = "aims-link-check/1.0"
_DATE_RE: Final[re.Pattern[str]] = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def sample_items(
    bundles: list[dict[str, Any]], days: int, limit: int
) -> list[dict[str, Any]]:
    """Deterministically sample citation items from recent bundles.

    Bundles dated within *days* of the newest bundle contribute their items;
    the pool is sorted by evidence ID, de-duplicated by URL (first wins), and
    capped at *limit*.
    """
    dated = [
        (str(bundle.get("metadata", {}).get("analysis_date", "")), bundle)
        for bundle in bundles
    ]
    dated = [(when, bundle) for when, bundle in dated if _DATE_RE.match(when)]
    if not dated:
        return []
    latest = max(when for when, _ in dated)
    cutoff = (date.fromisoformat(latest) - timedelta(days=days)).isoformat()
    pool = [
        item
        for when, bundle in dated
        if when >= cutoff
        for item in bundle.get("items", [])
        if isinstance(item, dict) and item.get("url")
    ]
    seen: set[str] = set()
    sampled: list[dict[str, Any]] = []
    for item in sorted(pool, key=lambda item: (str(item.get("id")), str(item["url"]))):
        url = str(item["url"])
        if url in seen:
            continue
        seen.add(url)
        sampled.append(item)
        if len(sampled) >= limit:
            break
    return sampled


def check_url(url: str, timeout: float = DEFAULT_TIMEOUT) -> str | None:
    """Probe a URL; return a warning reason, or None when it responds OK.

    Tries HEAD first and falls back to GET on an HTTP error, since some
    servers reject HEAD from non-browser clients.
    """
    if not url.startswith(("http://", "https://")):
        return "not an HTTP(S) URL"
    reason: str | None = None
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(
            url, method=method, headers={"User-Agent": _USER_AGENT}
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout):
                return None
        except urllib.error.HTTPError as exc:
            reason = f"HTTP {exc.code}"
        except urllib.error.URLError as exc:
            return f"unreachable: {exc.reason}"
        except TimeoutError:
            return "timed out"
    return reason


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence-dir", type=Path, default=Path("data/evidence"))
    parser.add_argument("--days", type=int, default=DEFAULT_DAYS)
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    parser.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if not args.evidence_dir.is_dir():
        print(f"No evidence bundles at {args.evidence_dir}; skipping link check.")
        return 0
    bundles: list[dict[str, Any]] = []
    for path in sorted(args.evidence_dir.glob("*.json")):
        try:
            with path.open(encoding="utf-8") as stream:
                bundles.append(json.load(stream))
        except json.JSONDecodeError as exc:
            print(f"WARNING: skipping unreadable evidence bundle {path}: {exc}")
    sampled = sample_items(bundles, args.days, args.limit)
    if not sampled:
        print("No recent evidence citations to sample; skipping link check.")
        return 0
    rotten = 0
    for item in sampled:
        reason = check_url(str(item["url"]), args.timeout)
        if reason is not None:
            rotten += 1
            print(
                f"WARNING: citation link rot: {item.get('id')} {item['url']} ({reason})"
            )
    print(
        f"Link check: {rotten}/{len(sampled)} sampled citation URL(s)"
        " unreachable (warning only, never a gate)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
