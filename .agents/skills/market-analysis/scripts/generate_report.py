#!/usr/bin/env python3
r"""Generate a Hugo Markdown report from an AIMS analysis artifact.

Usage:
    uv run .agents/skills/market-analysis/scripts/generate_report.py \
        --input data/analysis/2024-01-01.json \
        --output content/results/
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Final, Literal

_Alignment = Literal["left", "right", "center"]

_DEFAULT_OUTPUT_DIR: Final[Path] = Path("content/results")

_DISCLAIMER: Final[str] = (
    "This report is generated automatically from publicly available market data"
    " for informational purposes only. It does not constitute investment advice,"
    " a solicitation, or a recommendation to buy or sell any financial instrument."
    " Past performance is not indicative of future results. Always consult a"
    " qualified financial adviser before making investment decisions."
)

_GATE_DESCRIPTIONS: Final[dict[str, str]] = {
    "stale_data": (
        "Stale data: one or more instruments have data older than the threshold."
    ),
    "insufficient_history": (
        "Insufficient history: some instruments lack enough historical data for"
        " reliable scoring."
    ),
    "missing_bars": "Missing bars: data gaps detected in price history.",
    "malformed_input": "Malformed input: price data quality issues detected.",
    "high_volatility": (
        "High volatility: one or more instruments show extreme volatility."
    ),
    "missing_data": "Missing data: no price history available for this instrument.",
}


def _toml_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def _format_pct(value: float | None) -> str:
    if value is None:
        return "n/a"
    sign = "+" if value >= 0 else ""
    return f"{sign}{value * 100:.1f}%"


def _market_regime(scores: list[float]) -> str:
    if not scores:
        return "Unavailable"
    s = sorted(scores)
    n = len(s)
    median = s[n // 2] if n % 2 == 1 else (s[n // 2 - 1] + s[n // 2]) / 2
    if median >= 65.0:
        return "Bullish"
    if median <= 40.0:
        return "Bearish"
    return "Neutral"


def _build_front_matter(artifact: dict[str, Any], date_str: str) -> str:
    meta = artifact.get("metadata", {})
    generated_at = meta.get("generated_at", "1970-01-01T00:00:00+00:00")
    if not isinstance(generated_at, str):
        generated_at = "1970-01-01T00:00:00+00:00"

    data_source = str(meta.get("data_source", ""))
    scoring_version = str(meta.get("scoring_version", ""))
    git_commit = str(meta.get("git_commit", ""))

    instruments = artifact.get("instruments", [])
    reliable = [i for i in instruments if i.get("is_reliable")]
    reliable_scores = [float(i["score"]) for i in reliable if "score" in i]
    regime = _market_regime(reliable_scores)
    n_reliable = len(reliable)
    total = len(instruments)

    all_symbols = sorted(str(i.get("symbol", "")) for i in instruments)
    symbols_toml = ", ".join(f'"{_toml_escape(s)}"' for s in all_symbols)

    source_file = f"data/analysis/{date_str}.json"

    if reliable:
        top = max(reliable, key=lambda i: float(i.get("score", 0)))
        top_symbol = _toml_escape(str(top.get("symbol", "")))
        top_score = float(top.get("score", 0))
        summary = (
            f"{regime} market: {n_reliable} reliable instruments."
            f" Top signal: {top_symbol} (score {top_score:.1f})."
        )
    else:
        summary = "No reliable instruments."

    lines = [
        "+++",
        f'title = "Market Analysis {date_str}"',
        f'date = "{_toml_escape(generated_at)}"',
        "draft = false",
        f'summary = "{_toml_escape(summary)}"',
        f"ticker_symbols = [{symbols_toml}]",
        f'source_files = ["{_toml_escape(source_file)}"]',
        f'market_regime = "{_toml_escape(regime)}"',
        f'data_source = "{_toml_escape(data_source)}"',
        f'scoring_version = "{_toml_escape(scoring_version)}"',
        f'git_commit = "{_toml_escape(git_commit)}"',
        "+++",
    ]
    _ = total  # referenced in body, not front matter
    return "\n".join(lines)


def _section_market_regime(
    regime: str,
    n_reliable: int,
    total: int,
) -> str:
    return (
        f"## Market Regime\n\n**{regime}** — based on cross-sectional momentum"
        f" scores of {n_reliable} reliable instrument(s) out of {total} total."
    )


def _section_top_opportunities(reliable: list[dict[str, Any]]) -> str:
    header = "## Top Opportunities"
    top5 = sorted(reliable, key=lambda i: float(i.get("score", 0)), reverse=True)[:5]
    if not top5:
        return f"{header}\n\n_No reliable instruments available._"
    lines = []
    for inst in top5:
        symbol = str(inst.get("symbol", ""))
        score = float(inst.get("score", 0))
        features = inst.get("features") or {}
        ret_20d = features.get("ret_20d")
        rsi_raw = features.get("rsi_14")
        rsi_str = f"{rsi_raw:.0f}" if isinstance(rsi_raw, (int, float)) else "n/a"
        explanation = str(inst.get("explanation", ""))
        lines.append(
            f"- **{symbol}** — score {score:.1f},"
            f" 20d return {_format_pct(ret_20d)},"
            f" RSI14={rsi_str}. {explanation}"
        )
    return f"{header}\n\n" + "\n".join(lines)


def _section_instruments_to_avoid(unreliable: list[dict[str, Any]]) -> str:
    header = "## Instruments to Avoid"
    if not unreliable:
        return f"{header}\n\n_All instruments passed quality checks._"
    preamble = (
        "These instruments have quality or risk issues and are excluded from ranking:"
    )
    lines = []
    for inst in unreliable:
        symbol = str(inst.get("symbol", ""))
        gates = inst.get("risk_gates") or []
        gates_str = ", ".join(str(g) for g in gates)
        lines.append(f"- **{symbol}** — {gates_str}")
    return f"{header}\n\n{preamble}\n\n" + "\n".join(lines)


def _format_markdown_table(
    headers: list[str],
    rows: list[list[str]],
    alignments: list[_Alignment],
) -> str:
    """Format a markdown table with column padding matching Prettier."""
    widths = [max(len(row[i]) for row in [headers, *rows]) for i in range(len(headers))]

    def _pad_cell(value: str, width: int, align: _Alignment) -> str:
        if align == "right":
            inner = value.rjust(width)
        elif align == "center":
            inner = value.center(width)
        else:
            inner = value.ljust(width)
        return f" {inner} "

    def _pad_sep(width: int, align: _Alignment) -> str:
        if align == "right":
            inner = "-" * (width - 1) + ":" if width > 1 else ":"
        elif align == "center":
            inner = ":" + "-" * max(width - 2, 1) + ":"
        else:
            inner = "-" * width
        return f" {inner} "

    lines = [
        "|"
        + "|".join(
            _pad_cell(h, widths[i], alignments[i]) for i, h in enumerate(headers)
        )
        + "|",
        "|"
        + "|".join(_pad_sep(widths[i], alignments[i]) for i in range(len(headers)))
        + "|",
    ]
    lines.extend(
        "|"
        + "|".join(
            _pad_cell(row[i], widths[i], alignments[i]) for i in range(len(headers))
        )
        + "|"
        for row in rows
    )
    return "\n".join(lines)


def _section_key_risks(instruments: list[dict[str, Any]]) -> str:
    header = "## Key Risks"
    gate_counts: dict[str, int] = {}
    for inst in instruments:
        for gate in inst.get("risk_gates") or []:
            gate_str = str(gate)
            gate_counts[gate_str] = gate_counts.get(gate_str, 0) + 1
    if not gate_counts:
        return f"{header}\n\n_No risk gates triggered._"
    lines = []
    for gate in sorted(gate_counts):
        count = gate_counts[gate]
        desc = _GATE_DESCRIPTIONS.get(gate, gate)
        lines.append(f"- **{gate}** ({count} instrument(s)): {desc}")
    return f"{header}\n\n" + "\n".join(lines)


def _section_instrument_scores(instruments: list[dict[str, Any]]) -> str:
    header = "## Instrument Scores"
    table_headers = [
        "Rank",
        "Symbol",
        "Score",
        "Reliable",
        "Risk Gates",
        "Explanation",
    ]
    alignments: list[_Alignment] = [
        "right",
        "left",
        "right",
        "center",
        "left",
        "left",
    ]
    rows: list[list[str]] = []
    for inst in instruments:
        rank = inst.get("rank", "")
        symbol = str(inst.get("symbol", ""))
        score = float(inst.get("score", 0))
        reliable = "Yes" if inst.get("is_reliable") else "No"
        gates = inst.get("risk_gates") or []
        gates_str = ", ".join(str(g) for g in gates) if gates else "—"
        explanation = str(inst.get("explanation", ""))
        rows.append([
            str(rank),
            symbol,
            f"{score:.1f}",
            reliable,
            gates_str,
            explanation,
        ])
    table = _format_markdown_table(table_headers, rows, alignments)
    return f"{header}\n\n{table}"


def _section_data_freshness(
    data_source: str,
    freshness: dict[str, str],
) -> str:
    header = "## Data Freshness"
    parts: list[str] = [f"Data source: **{data_source}**"]

    if freshness:
        table_headers = ["Symbol", "Latest Bar"]
        alignments: list[_Alignment] = ["left", "left"]
        table_rows = [[sym, freshness[sym]] for sym in sorted(freshness)]
        stale_symbols = []
        for sym, val in table_rows:
            if val == "n/a":
                stale_symbols.append(sym)
        parts.append(_format_markdown_table(table_headers, table_rows, alignments))
        if stale_symbols:
            stale_joined = ", ".join(sorted(stale_symbols))
            n = len(stale_symbols)
            parts.append(
                f"> **Warning:** {n} instrument(s) have no data: {stale_joined}."
            )
    else:
        parts.append("_No freshness data available._")

    return f"{header}\n\n" + "\n\n".join(parts)


def _section_methodology(scoring_version: str, git_commit: str) -> str:
    header = "## Methodology"
    feature_list = (
        "Instruments are scored and ranked cross-sectionally using the following"
        " features:\n\n"
        "- **Momentum**: 1-day, 5-day, 20-day, and 60-day returns\n"
        "- **Trend**: Distance from 20-day and 50-day moving averages\n"
        "- **Volatility**: 20-day realized annualized volatility (lower is better)\n"
        "- **Drawdown**: Maximum drawdown over 60 days (lower is better)\n"
        "- **RSI**: 14-day Relative Strength Index\n"
        "- **Z-score**: Price z-score relative to 20-day mean"
    )
    percentile_note = (
        "Each feature is converted to a cross-sectional percentile rank."
        " The composite score is the mean percentile across all features (0–100)."  # noqa: RUF001
    )
    version_line = (
        f"Scoring engine version: **{scoring_version}** | Git commit: **{git_commit}**"
    )
    ops_ref = "For methodology details, see OPERATIONS.md in the repository root."
    content = f"{feature_list}\n\n{percentile_note}\n\n{version_line}\n\n{ops_ref}"
    return f"{header}\n\n{content}"


def _section_disclaimer() -> str:
    return f"## Disclaimer\n\n> {_DISCLAIMER}"


def _validate_for_report(artifact: dict[str, Any]) -> None:
    meta = artifact.get("metadata")
    if not isinstance(meta, dict):
        msg = "artifact is missing a valid 'metadata' section"
        raise ValueError(msg)  # noqa: TRY004
    generated_at = meta.get("generated_at")
    if not isinstance(generated_at, str) or not generated_at:
        msg = "artifact 'generated_at' is missing or not a string"
        raise ValueError(msg)
    if generated_at.startswith("1970-01-01"):
        msg = (
            f"'generated_at' is the epoch sentinel;"
            f" artifact is not publishable: {generated_at!r}"
        )
        raise ValueError(msg)
    if "instruments" not in artifact:
        msg = "artifact is missing the 'instruments' key"
        raise ValueError(msg)


def generate_report(artifact: dict[str, Any]) -> str:
    meta = artifact.get("metadata", {})
    generated_at = meta.get("generated_at", "")
    if not isinstance(generated_at, str) or not generated_at:
        generated_at = "1970-01-01T00:00:00+00:00"
    date_str = generated_at[:10]

    data_source = str(meta.get("data_source", ""))
    scoring_version = str(meta.get("scoring_version", ""))
    git_commit = str(meta.get("git_commit", ""))
    freshness_raw = meta.get("data_freshness", {})
    freshness: dict[str, str] = (
        {str(k): str(v) for k, v in freshness_raw.items()}
        if isinstance(freshness_raw, dict)
        else {}
    )

    instruments = artifact.get("instruments", [])
    reliable = [i for i in instruments if i.get("is_reliable")]
    unreliable = [i for i in instruments if not i.get("is_reliable")]
    reliable_scores = [float(i["score"]) for i in reliable if "score" in i]
    regime = _market_regime(reliable_scores)
    n_reliable = len(reliable)
    total = len(instruments)

    front_matter = _build_front_matter(artifact, date_str)

    sections = [
        _section_market_regime(regime, n_reliable, total),
        _section_top_opportunities(reliable),
        _section_instruments_to_avoid(unreliable),
        _section_key_risks(instruments),
        _section_instrument_scores(instruments),
        _section_data_freshness(data_source, freshness),
        _section_methodology(scoring_version, git_commit),
        _section_disclaimer(),
    ]
    body = "\n\n".join(sections)
    return f"{front_matter}\n\n{body}\n"


def report_filename(artifact: dict[str, Any]) -> str:
    meta = artifact.get("metadata", {})
    generated_at = meta.get("generated_at", "")
    if not isinstance(generated_at, str) or not generated_at:
        date_str = "1970-01-01"
    else:
        date_str = generated_at[:10]
    return f"{date_str}-market-analysis.md"


def generate_and_save(
    artifact_path: Path,
    output_dir: Path = _DEFAULT_OUTPUT_DIR,
) -> Path:
    with artifact_path.open(encoding="utf-8") as fh:
        artifact: dict[str, Any] = json.load(fh)
    _validate_for_report(artifact)
    content = generate_report(artifact)
    filename = report_filename(artifact)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / filename
    output_path.write_text(content, encoding="utf-8")
    print(f"Report written to {output_path}")
    return output_path


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help="Path to analysis artifact JSON file",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=_DEFAULT_OUTPUT_DIR,
        help=f"Output directory (default: {_DEFAULT_OUTPUT_DIR})",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        generate_and_save(args.input, args.output)
    except FileNotFoundError:
        print(f"ERROR: file not found: {args.input}")
        return 1
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON in {args.input}: {exc}")
        return 1
    except ValueError as exc:
        print(f"ERROR: artifact validation failed: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
