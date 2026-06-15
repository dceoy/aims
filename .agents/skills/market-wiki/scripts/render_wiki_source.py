#!/usr/bin/env python3
r"""Render deterministic Markdown source from an AIMS analysis artifact."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Final

_SCHEMA_VERSION: Final[str] = "1"
_DATE_LEN: Final[int] = 10
_TOP_LIMIT: Final[int] = 10


def _analysis_date(artifact: dict[str, Any]) -> str:
    generated_at = str(artifact.get("metadata", {}).get("generated_at", ""))
    return generated_at[:_DATE_LEN] if len(generated_at) >= _DATE_LEN else "unknown"


def _fmt(value: object) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        return f"{value:.6g}"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, list):
        return ", ".join(str(v) for v in value) if value else "none"
    return str(value)


def _risk_gate_counts(instruments: list[dict[str, Any]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for instrument in instruments:
        for gate in instrument.get("risk_gates", []):
            counts[str(gate)] = counts.get(str(gate), 0) + 1
    return dict(sorted(counts.items()))


def render_source(artifact: dict[str, Any], source_path: Path | None = None) -> str:
    """Render an artifact as compact deterministic Markdown."""
    metadata = artifact.get("metadata", {})
    instruments = sorted(
        artifact.get("instruments", []),
        key=lambda i: (
            i.get("rank") is None,
            i.get("rank", 999999),
            i.get("symbol", ""),
        ),
    )
    date = _analysis_date(artifact)
    reliable = [i for i in instruments if i.get("is_reliable") is True]
    unreliable = [i for i in instruments if i.get("is_reliable") is not True]
    fingerprint = hashlib.sha256(
        json.dumps(artifact, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

    lines = [
        "<!-- generated-by: market-wiki/render_wiki_source.py -->",
        f"<!-- source-sha256: {fingerprint} -->",
        "",
        f"# Market Analysis Source: {date}",
        "",
        "## Metadata",
        "",
        f"- Analysis date: {date}",
        f"- Generated at: {_fmt(metadata.get('generated_at'))}",
        f"- Artifact version: {_fmt(artifact.get('version'))}",
        f"- Data source: {_fmt(metadata.get('data_source'))}",
        f"- Scoring version: {_fmt(metadata.get('scoring_version'))}",
        f"- Git commit: {_fmt(metadata.get('git_commit'))}",
        f"- Source artifact: {_fmt(source_path) if source_path else 'unknown'}",
        f"- Renderer schema: {_SCHEMA_VERSION}",
        "",
        "## Market snapshot",
        "",
        f"- Instruments analyzed: {len(instruments)}",
        f"- Reliable instruments: {len(reliable)}",
        f"- Unreliable instruments: {len(unreliable)}",
        "",
        "## Top-ranked instruments",
        "",
        "<!-- prettier-ignore-start -->",
        "| Rank | Symbol | Score | Reliable | Risk gates | Explanation |",
        "| ---: | --- | ---: | --- | --- | --- |",
    ]
    row_template = (
        "| {rank} | {symbol} | {score} | {reliable} | {gates} | {explanation} |"
    )
    lines.extend(
        row_template.format(
            rank=_fmt(instrument.get("rank")),
            symbol=_fmt(instrument.get("symbol")),
            score=_fmt(instrument.get("score")),
            reliable=_fmt(instrument.get("is_reliable")),
            gates=_fmt(instrument.get("risk_gates", [])),
            explanation=str(instrument.get("explanation", "n/a")).replace("|", "\\|"),
        )
        for instrument in instruments[:_TOP_LIMIT]
    )

    lines.extend(["<!-- prettier-ignore-end -->", "", "## Unreliable instruments", ""])
    if unreliable:
        lines.extend(
            f"- {_fmt(instrument.get('symbol'))}: "
            f"{_fmt(instrument.get('risk_gates', []))}"
            for instrument in unreliable
        )
    else:
        lines.append("- none")

    lines.extend(["", "## Risk gates", ""])
    counts = _risk_gate_counts(instruments)
    if counts:
        for gate, count in counts.items():
            lines.append(f"- {gate}: {count}")
    else:
        lines.append("- none")

    lines.extend(["", "## Notable feature values", ""])
    for instrument in instruments[:_TOP_LIMIT]:
        features = instrument.get("features", {})
        feature_text = ", ".join(f"{k}={_fmt(v)}" for k, v in sorted(features.items()))
        lines.append(f"- {_fmt(instrument.get('symbol'))}: {feature_text or 'n/a'}")

    freshness = metadata.get("data_freshness", {})
    lines.extend(["", "## Data freshness", ""])
    if isinstance(freshness, dict) and freshness:
        for symbol, value in sorted(freshness.items()):
            lines.append(f"- {symbol}: {_fmt(value)}")
    else:
        lines.append("- n/a")
    return "\n".join(lines) + "\n"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="Analysis JSON path")
    parser.add_argument(
        "--output", required=True, type=Path, help="Markdown output path"
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    artifact = json.loads(args.input.read_text(encoding="utf-8"))
    output = render_source(artifact, args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
