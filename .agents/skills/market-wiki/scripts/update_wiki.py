#!/usr/bin/env python3
r"""Orchestrate baseline Market Knowledge Wiki updates for one source."""

from __future__ import annotations

import argparse
import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Final

_DATE_LEN: Final[int] = 10

INDEX_TEMPLATE = """# Market Knowledge Wiki

The Market Knowledge Wiki is an internal, Git-managed research memory.
It is derived from AIMS daily market analysis artifacts.

## Core pages

- [Overview](wiki/overview.md)

## Market regimes

- [Bullish](wiki/market-regimes/bullish.md)
- [Neutral](wiki/market-regimes/neutral.md)
- [Bearish](wiki/market-regimes/bearish.md)

## Themes

- [AI Infrastructure](wiki/themes/ai-infrastructure.md)
- [Japan Equities](wiki/themes/japan-equities.md)
- [Commodity Cycle](wiki/themes/commodity-cycle.md)

## Methods

- [Scoring Methodology](wiki/methods/scoring-methodology.md)
- [Risk Gates](wiki/methods/risk-gates.md)
- [Data Quality](wiki/methods/data-quality.md)

## Watchlists

- [High Momentum](wiki/watchlists/high-momentum.md)
- [High Risk](wiki/watchlists/high-risk.md)
- [Stale or Unreliable](wiki/watchlists/stale-or-unreliable.md)
{instruments}{sources}"""

_BASELINE_PAGES: Final[dict[str, str]] = {
    "wiki/market-regimes/bullish.md": "# Bullish Market Regime\n\nDated bullish observations.\n",
    "wiki/market-regimes/neutral.md": "# Neutral Market Regime\n\nDated neutral observations.\n",
    "wiki/market-regimes/bearish.md": "# Bearish Market Regime\n\nDated bearish observations.\n",
    "wiki/themes/ai-infrastructure.md": "# AI Infrastructure Theme\n\nDated source-backed observations.\n",
    "wiki/themes/japan-equities.md": "# Japan Equities Theme\n\nDated source-backed observations.\n",
    "wiki/themes/commodity-cycle.md": "# Commodity Cycle Theme\n\nDated source-backed observations.\n",
    "wiki/methods/scoring-methodology.md": "# Scoring Methodology\n\nScoring behavior notes.\n",
    "wiki/methods/risk-gates.md": "# Risk Gates\n\nDated risk-gate observations.\n",
    "wiki/methods/data-quality.md": "# Data Quality\n\nData-quality patterns.\n",
    "wiki/watchlists/high-momentum.md": "# High Momentum Watchlist\n\nSource-backed instruments.\n",
    "wiki/watchlists/high-risk.md": "# High Risk Watchlist\n\nSource-backed instruments.\n",
    "wiki/watchlists/stale-or-unreliable.md": "# Stale or Unreliable Watchlist\n\nUnreliable instruments.\n",
}


def _title(symbol: str) -> str:
    clean = symbol.strip("^").replace(".", " ").replace("_", "-")
    return clean.upper() if clean else "UNKNOWN"


def _slug(symbol: str) -> str:
    return symbol.lower().strip("^").replace(".", "-").replace("_", "-") or "unknown"


def _ensure(path: Path, content: str) -> None:
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def _analysis_date(artifact: dict[str, object]) -> str:
    metadata = artifact.get("metadata")
    if isinstance(metadata, dict):
        generated_at = str(metadata.get("generated_at", ""))
        if len(generated_at) >= _DATE_LEN:
            return generated_at[:_DATE_LEN]
    return "unknown"


def refresh_index(wiki_root: Path) -> None:
    """Refresh the content navigation index from current wiki pages."""
    instrument_pages = sorted((wiki_root / "wiki" / "instruments").glob("*.md"))
    source_pages = sorted((wiki_root / "sources").glob("*.md"))
    instruments = ""
    if instrument_pages:
        instruments = "\n## Instruments\n\n" + "".join(
            f"- [{page.stem.upper()}]({page.relative_to(wiki_root).as_posix()})\n"
            for page in instrument_pages
        )
    sources = ""
    if source_pages:
        sources = "\n## Rendered sources\n\n" + "".join(
            f"- [{page.stem}]({page.relative_to(wiki_root).as_posix()})\n"
            for page in source_pages
        )
    (wiki_root / "index.md").write_text(
        INDEX_TEMPLATE.format(instruments=instruments, sources=sources),
        encoding="utf-8",
    )


def update_wiki(source: Path, analysis: Path, wiki_root: Path) -> None:
    """Ensure baseline wiki pages and append an ingest log entry."""
    artifact = json.loads(analysis.read_text(encoding="utf-8"))
    wiki_root.mkdir(parents=True, exist_ok=True)
    _ensure(wiki_root / "log.md", "# Market Knowledge Wiki Log\n\n")
    _ensure(
        wiki_root / "wiki" / "overview.md",
        (
            "# Market Knowledge Wiki Overview\n\n"
            "Internal research memory for AIMS market analysis.\n"
        ),
    )
    for rel_path, content in _BASELINE_PAGES.items():
        _ensure(wiki_root / rel_path, content)
    for instrument in artifact.get("instruments", []):
        if not isinstance(instrument, dict):
            continue
        symbol = str(instrument.get("symbol", "unknown"))
        _ensure(
            wiki_root / "wiki" / "instruments" / f"{_slug(symbol)}.md",
            f"# {_title(symbol)}\n\nDated observations for `{symbol}`.\n",
        )
    refresh_index(wiki_root)
    rel_source = source.relative_to(wiki_root).as_posix()
    rel_analysis = analysis.as_posix()
    date = _analysis_date(artifact)
    stamp = datetime.now(UTC).replace(microsecond=0).isoformat()
    entry = (
        f"\n## {stamp} — ingest {date}\n\n"
        f"- Source: [{rel_source}]({rel_source})\n"
        f"- Analysis artifact: `{rel_analysis}`\n"
        "- Action: refreshed index and baseline instrument pages.\n"
    )
    log = wiki_root / "log.md"
    if rel_source not in log.read_text(encoding="utf-8"):
        log.write_text(
            log.read_text(encoding="utf-8").rstrip() + "\n" + entry, encoding="utf-8"
        )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--analysis", required=True, type=Path)
    parser.add_argument("--wiki-root", default=Path("knowledge"), type=Path)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    update_wiki(args.source, args.analysis, args.wiki_root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
