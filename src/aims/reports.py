r"""Generate a Hugo Markdown report from an AIMS analysis artifact.

Usage:
    uv run .agents/skills/market-analysis/scripts/generate_report.py \
        --input data/analysis/2024-01-01.json \
        --output content/results/
"""

from __future__ import annotations

import argparse
import json
from operator import itemgetter
from pathlib import Path
from typing import Any, Final, Literal

from aims.calendars import (
    DEFAULT_WINDOW_DAYS,
    CalendarEvent,
    events_for_instrument,
    load_calendar_events,
    upcoming_events,
)
from aims.market_analysis import artifact_interval_suffix

MarkdownAlignment = Literal["left", "right", "center"]

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


def _format_vol(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value * 100:.1f}%"


_BULLISH_BREADTH: Final[float] = 0.65
_BEARISH_BREADTH: Final[float] = 0.35


def _regime_breadth(reliable: list[dict[str, Any]]) -> tuple[int, int]:
    """Return (above_ma20, with_ma20_data) counts for reliable instruments."""
    above = 0
    valid = 0
    for inst in reliable:
        features = inst.get("features") or {}
        dist = features.get("ma20_dist")
        if isinstance(dist, (int, float)):
            valid += 1
            if dist > 0:
                above += 1
    return above, valid


def market_regime(reliable: list[dict[str, Any]]) -> str:
    """Label the market regime from MA20 breadth of reliable instruments.

    Percentile-based composite scores are relative by construction, so their
    median stays near 50 regardless of market direction. Breadth — the share
    of reliable instruments trading above their 20-day moving average — is an
    absolute measure that distinguishes broad rallies from broad declines.
    """
    above, valid = _regime_breadth(reliable)
    if not valid:
        return "Unavailable"
    breadth = above / valid
    if breadth >= _BULLISH_BREADTH:
        return "Bullish"
    if breadth <= _BEARISH_BREADTH:
        return "Bearish"
    return "Neutral"


def _build_front_matter(
    artifact: dict[str, Any],
    date_str: str,
    history: dict[str, Any] | None = None,
    *,
    ai_commentary: bool = False,
) -> str:
    meta = artifact.get("metadata", {})
    generated_at = meta.get("generated_at", "1970-01-01T00:00:00+00:00")
    if not isinstance(generated_at, str):
        generated_at = "1970-01-01T00:00:00+00:00"

    data_source = str(meta.get("data_source", ""))
    scoring_version = str(meta.get("scoring_version", ""))
    git_commit = str(meta.get("git_commit", ""))

    instruments = artifact.get("instruments", [])
    reliable = [i for i in instruments if i.get("is_reliable")]
    regime = market_regime(reliable)
    n_reliable = len(reliable)

    all_symbols = sorted(str(i.get("symbol", "")) for i in instruments)
    symbols_toml = ", ".join(f'"{_toml_escape(s)}"' for s in all_symbols)

    stem = f"{date_str}{artifact_interval_suffix(artifact)}"
    source_files = [f"data/analysis/{stem}.json"]
    if history is not None:
        source_files.append(f"data/history/{stem}.json")
    if ai_commentary:
        source_files.extend([
            f"data/evidence/{stem}.json",
            f"data/qualitative/{stem}.json",
        ])
    sources_toml = ", ".join(f'"{_toml_escape(path)}"' for path in source_files)

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
        f"source_files = [{sources_toml}]",
        f'market_regime = "{_toml_escape(regime)}"',
        f'data_source = "{_toml_escape(data_source)}"',
        f'scoring_version = "{_toml_escape(scoring_version)}"',
        f'git_commit = "{_toml_escape(git_commit)}"',
    ]
    if ai_commentary:
        lines.append("ai_commentary = true")
    lines.append("+++")
    return "\n".join(lines)


def _section_market_regime(
    regime: str,
    above: int,
    valid: int,
    total: int,
) -> str:
    return (
        f"## Market Regime\n\n**{regime}** — {above} of {valid} reliable"
        f" instrument(s) with MA20 data trade above their 20-day moving"
        f" average ({total} instruments in universe)."
    )


def _instrument_label(inst: dict[str, Any]) -> str:
    """Return 'Display Name / symbol' when display_name is available, else symbol."""
    symbol = str(inst.get("symbol", ""))
    display_name = inst.get("display_name")
    if display_name and str(display_name) != symbol:
        return f"{display_name} / {symbol}"
    return symbol


def _instrument_events(
    inst: dict[str, Any], events: list[CalendarEvent]
) -> list[CalendarEvent]:
    return events_for_instrument(
        events,
        str(inst.get("canonical_id") or ""),
        str(inst.get("asset_class") or ""),
    )


def _section_top_opportunities(
    reliable: list[dict[str, Any]],
    events: list[CalendarEvent] | None = None,
) -> str:
    header = "## Top Opportunities"
    top5 = sorted(reliable, key=lambda i: float(i.get("score", 0)), reverse=True)[:5]
    if not top5:
        return f"{header}\n\n_No reliable instruments available._"
    lines = []
    for inst in top5:
        label = _instrument_label(inst)
        score = float(inst.get("score", 0))
        features = inst.get("features") or {}
        ret_20d = features.get("ret_20d")
        rsi_raw = features.get("rsi_14")
        rsi_str = f"{rsi_raw:.0f}" if isinstance(rsi_raw, (int, float)) else "n/a"
        explanation = str(inst.get("explanation", ""))
        line = (
            f"- **{label}** — score {score:.1f},"
            f" 20d return {_format_pct(ret_20d)},"
            f" RSI14={rsi_str}. {explanation}"
        )
        matched = _instrument_events(inst, events) if events else []
        if matched:
            flagged = "; ".join(f"{e.title} ({e.date})" for e in matched)
            line += f" ⚠️ Upcoming: {flagged}"
        lines.append(line)
    return f"{header}\n\n" + "\n".join(lines)


def _event_scope(event: CalendarEvent, instruments: list[dict[str, Any]]) -> str:
    symbol_by_cid = {
        str(inst.get("canonical_id")): str(inst.get("symbol", ""))
        for inst in instruments
        if inst.get("canonical_id")
    }
    symbols = sorted(
        symbol_by_cid[cid] for cid in event.canonical_ids if cid in symbol_by_cid
    )
    classes = sorted(_asset_class_label(ac) for ac in event.asset_classes)
    return ", ".join(symbols + classes)


def _section_upcoming_events(
    instruments: list[dict[str, Any]],
    events: list[CalendarEvent],
    window_days: int,
) -> str:
    header = "## Upcoming Events"
    rows: list[list[str]] = []
    for event in events:
        scope = _event_scope(event, instruments)
        if scope:
            rows.append([event.date, event.title, scope])
    if not rows:
        return (
            f"{header}\n\n_No scheduled events for covered instruments in the"
            f" next {window_days} days._"
        )
    table = format_markdown_table(
        ["Date", "Event", "Applies To"], rows, ["left", "left", "left"]
    )
    preamble = (
        f"Scheduled events within the next {window_days} days for covered"
        " instruments (from `data/calendars/`)."
    )
    return f"{header}\n\n{preamble}\n\n{table}"


def _section_instruments_to_avoid(unreliable: list[dict[str, Any]]) -> str:
    header = "## Instruments to Avoid"
    if not unreliable:
        return f"{header}\n\n_All instruments passed quality checks._"
    preamble = (
        "These instruments have quality or risk issues and are excluded from ranking:"
    )
    lines = []
    for inst in unreliable:
        label = _instrument_label(inst)
        gates = inst.get("risk_gates") or []
        gates_str = ", ".join(str(g) for g in gates)
        lines.append(f"- **{label}** — {gates_str}")
    return f"{header}\n\n{preamble}\n\n" + "\n".join(lines)


def _qualitative_withheld(qualitative: dict[str, Any]) -> bool:
    gates = qualitative.get("metadata", {}).get("gates", {})
    return bool(gates.get("market_narrative_withheld"))


def _citation_refs(citations: list[Any], numbers: dict[str, int]) -> str:
    refs = ""
    for cid in citations:
        key = str(cid)
        if key not in numbers:
            numbers[key] = len(numbers) + 1
        refs += f"[{numbers[key]}]"
    return refs


def _section_ai_commentary(
    qualitative: dict[str, Any],
    evidence: dict[str, Any] | None,
    instruments: list[dict[str, Any]],
) -> str:
    meta = qualitative.get("metadata", {})
    market = qualitative.get("market", {})
    numbers: dict[str, int] = {}

    label_by_cid = {
        str(inst.get("canonical_id")): _instrument_label(inst)
        for inst in instruments
        if inst.get("canonical_id")
    }
    banner = (
        "> **AI-generated section.** Produced by"
        f" `{meta.get('model_id', 'unknown')}` (prompt"
        f" v{meta.get('prompt_version', 'unknown')}) from the committed"
        " evidence bundle and quantitative artifact, after schema validation"
        " and deterministic consistency gates. It does not modify the scores,"
        " ranks, risk gates, or market regime above, and it is not investment"
        " advice — see the Disclaimer section below."
    )
    parts = ["## AI Market Commentary", banner]

    narrative = str(market.get("narrative", ""))
    refs = _citation_refs(market.get("citations", []), numbers)
    parts.append(f"{narrative} {refs}".rstrip())

    themes = market.get("themes", [])
    if themes:
        theme_lines = [
            f"- {theme.get('title', '')}"
            f" {_citation_refs(theme.get('citations', []), numbers)}".rstrip()
            for theme in themes
        ]
        parts.append("**Recurring themes:**\n\n" + "\n".join(theme_lines))

    withheld_notes: list[str] = []
    for entry in qualitative.get("instruments", []):
        cid = str(entry.get("canonical_id", ""))
        label = label_by_cid.get(cid, str(entry.get("symbol", cid)))
        gates = entry.get("qualitative_gates") or []
        if gates:
            gates_str = ", ".join(str(g) for g in gates)
            withheld_notes.append(
                f"_Commentary for **{label}** withheld by consistency gates:"
                f" {gates_str}._"
            )
            continue
        driver_lines = [
            f"- {driver.get('text', '')}"
            f" {_citation_refs(driver.get('citations', []), numbers)}".rstrip()
            for driver in entry.get("drivers", [])
        ]
        parts.append(
            f"### {label} — {entry.get('stance', '')}"
            f" (confidence: {entry.get('confidence', '')})\n\n"
            + "\n".join(driver_lines)
        )
    parts.extend(withheld_notes)

    if numbers:
        items_by_id = {
            str(item.get("id")): item for item in (evidence or {}).get("items", [])
        }
        source_lines = []
        for cid, number in sorted(numbers.items(), key=itemgetter(1)):
            item = items_by_id.get(cid)
            if item is None:
                source_lines.append(f"{number}. {cid}")
            else:
                source_lines.append(
                    f"{number}. [{item.get('title', '')}]({item.get('url', '')})"
                    f" — {item.get('source', '')}, {item.get('published_at', '')[:10]}"
                )
        parts.append("### Sources\n\n" + "\n".join(source_lines))

    return "\n\n".join(parts)


def _section_signal_history(history: dict[str, Any] | None) -> str:
    header = "## Signal History"
    if history is None:
        return f"{header}\n\n_No previous analysis artifact available._"
    previous = history.get("previous_analysis_date")
    if previous is None:
        return f"{header}\n\n_No previous analysis artifact available._"
    rows = history.get("instruments", [])
    new_top = sorted(str(row["symbol"]) for row in rows if row.get("new_top_k"))
    persistent = sorted(
        (row for row in rows if int(row.get("consecutive_top_k_reports", 0)) >= 2),
        key=lambda row: (-int(row["consecutive_top_k_reports"]), str(row["symbol"])),
    )
    transitions = sorted(
        (
            row
            for row in rows
            if row.get("risk_gates_added") or row.get("risk_gates_removed")
        ),
        key=lambda row: str(row["symbol"]),
    )
    lines = [f"Compared with the previous available report (**{previous}**)."]
    current_size = history.get("universe_size")
    previous_size = history.get("previous_universe_size")
    if (
        isinstance(current_size, int)
        and isinstance(previous_size, int)
        and current_size != previous_size
    ):
        lines.append(
            f"- **Universe change:** {previous_size} → {current_size} instruments;"
            " percentile-based scores and deltas are not directly comparable"
            " across this change."
        )
    lines.append(
        f"- **New top-{history.get('top_k', 5)}:** {', '.join(new_top) or 'None'}"
    )
    persistent_text = ", ".join(
        f"{row['symbol']} ({row['consecutive_top_k_reports']} reports)"
        for row in persistent
    )
    lines.append(f"- **Persistent top signals:** {persistent_text or 'None'}")
    dropped = history.get("dropped_from_top_k", [])
    dropped_text = ", ".join(dropped) or "None"
    lines.append(f"- **Dropped from top-{history.get('top_k', 5)}:** {dropped_text}")
    for row in transitions:
        added = ", ".join(row.get("risk_gates_added", [])) or "none"
        removed = ", ".join(row.get("risk_gates_removed", [])) or "none"
        lines.append(
            f"- **{row['symbol']} risk gates:** added {added}; removed {removed}"
        )

    delta_rows = [
        row
        for row in rows
        if row.get("rank_delta") is not None or row.get("score_delta") is not None
    ]
    if delta_rows:
        table_rows: list[list[str]] = []
        for row in sorted(delta_rows, key=lambda r: str(r.get("symbol", ""))):
            sym = str(row.get("symbol", ""))
            rank_delta = row.get("rank_delta")
            score_delta = row.get("score_delta")
            rank_str = f"{rank_delta:+d}" if isinstance(rank_delta, int) else "n/a"
            score_str = (
                f"{score_delta:+.1f}"
                if isinstance(score_delta, (int, float))
                else "n/a"
            )
            table_rows.append([sym, rank_str, score_str])
        delta_table = format_markdown_table(
            ["Symbol", "Rank Δ", "Score Δ"],
            table_rows,
            ["left", "right", "right"],
        )
        lines.extend(("", delta_table))

    return f"{header}\n\n" + "\n".join(lines)


def format_markdown_table(
    headers: list[str],
    rows: list[list[str]],
    alignments: list[MarkdownAlignment],
) -> str:
    """Format a markdown table with column padding matching Prettier."""
    widths = [max(len(row[i]) for row in [headers, *rows]) for i in range(len(headers))]

    def _pad_cell(value: str, width: int, align: MarkdownAlignment) -> str:
        if align == "right":
            inner = value.rjust(width)
        elif align == "center":
            inner = value.center(width)
        else:
            inner = value.ljust(width)
        return f" {inner} "

    def _pad_sep(width: int, align: MarkdownAlignment) -> str:
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


def _instrument_scores_table(instruments: list[dict[str, Any]]) -> str:
    table_headers = [
        "Rank",
        "Instrument",
        "Score",
        "Reliable",
        "Risk Gates",
        "Explanation",
    ]
    alignments: list[MarkdownAlignment] = [
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
        label = _instrument_label(inst)
        score = float(inst.get("score", 0))
        reliable = "Yes" if inst.get("is_reliable") else "No"
        gates = inst.get("risk_gates") or []
        gates_str = ", ".join(str(g) for g in gates) if gates else "—"
        explanation = str(inst.get("explanation", ""))
        rows.append([
            str(rank),
            label,
            f"{score:.1f}",
            reliable,
            gates_str,
            explanation,
        ])
    return format_markdown_table(table_headers, rows, alignments)


def _asset_class_label(asset_class: str) -> str:
    return asset_class.replace("_", " ").title()


def _section_instrument_scores(instruments: list[dict[str, Any]]) -> str:
    header = "## Instrument Scores"
    groups: dict[str, list[dict[str, Any]]] = {}
    for inst in instruments:
        groups.setdefault(str(inst.get("asset_class") or ""), []).append(inst)
    if len(groups) <= 1:
        return f"{header}\n\n{_instrument_scores_table(instruments)}"
    parts = [header]
    for asset_class in sorted(groups, key=lambda k: (not k, k)):
        label = _asset_class_label(asset_class) if asset_class else "Other"
        parts.extend((f"### {label}", _instrument_scores_table(groups[asset_class])))
    return "\n\n".join(parts)


def _section_data_freshness(
    data_source: str,
    freshness: dict[str, str],
) -> str:
    header = "## Data Freshness"
    parts: list[str] = [f"Data source: **{data_source}**"]

    if freshness:
        table_headers = ["Symbol", "Latest Bar"]
        alignments: list[MarkdownAlignment] = ["left", "left"]
        table_rows = [[sym, freshness[sym]] for sym in sorted(freshness)]
        stale_symbols = []
        for sym, val in table_rows:
            if val == "n/a":
                stale_symbols.append(sym)
        parts.append(format_markdown_table(table_headers, table_rows, alignments))
        if stale_symbols:
            stale_joined = ", ".join(sorted(stale_symbols))
            n = len(stale_symbols)
            parts.append(
                f"> **Warning:** {n} instrument(s) have no data: {stale_joined}."
            )
    else:
        parts.append("_No freshness data available._")

    return f"{header}\n\n" + "\n\n".join(parts)


def _fmt_feature(key: str, value: float | None) -> str:
    if key in {"ret_1d", "ret_5d", "ret_20d", "ret_60d", "ma20_dist", "ma50_dist"}:
        return _format_pct(value)
    if key in {"vol_20d", "mdd_60d"}:
        return _format_vol(value)
    if value is None:
        return "n/a"
    return f"{value:.1f}"


_FEATURE_KEYS: Final[tuple[str, ...]] = (
    "ret_1d",
    "ret_5d",
    "ret_20d",
    "ret_60d",
    "ma20_dist",
    "ma50_dist",
    "vol_20d",
    "mdd_60d",
    "rsi_14",
    "zscore_20d",
)


def _section_symbol_details(instruments: list[dict[str, Any]]) -> str:
    header = "## Symbol Details"
    reliable = sorted(
        [i for i in instruments if i.get("is_reliable")],
        key=lambda i: int(i.get("rank", 0)),
    )
    if not reliable:
        return f"{header}\n\n_No reliable instruments to display._"
    subsections: list[str] = []
    for inst in reliable:
        label = _instrument_label(inst)
        score = float(inst.get("score", 0))
        features = inst.get("features") or {}
        table_rows = [
            [key, _fmt_feature(key, features.get(key))] for key in _FEATURE_KEYS
        ]
        table = format_markdown_table(
            ["Feature", "Value"], table_rows, ["left", "right"]
        )
        subsections.append(f"### {label} (score {score:.1f})\n\n{table}")
    return f"{header}\n\n" + "\n\n".join(subsections)


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
        " The composite score is the mean percentile across all features (0–100)."
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


def generate_report(
    artifact: dict[str, Any],
    history: dict[str, Any] | None = None,
    *,
    calendar_events: list[CalendarEvent] | None = None,
    window_days: int = DEFAULT_WINDOW_DAYS,
    qualitative: dict[str, Any] | None = None,
    evidence: dict[str, Any] | None = None,
) -> str:
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
    regime = market_regime(reliable)
    above, valid = _regime_breadth(reliable)
    total = len(instruments)

    # A qualitative artifact whose market narrative was withheld by the #93
    # gates renders nothing: the report stays byte-identical to a run
    # without a qualitative artifact.
    if qualitative is not None and _qualitative_withheld(qualitative):
        qualitative = None

    events = (
        upcoming_events(calendar_events, date_str, window_days)
        if calendar_events is not None
        else None
    )

    front_matter = _build_front_matter(
        artifact, date_str, history, ai_commentary=qualitative is not None
    )

    sections = [
        _section_market_regime(regime, above, valid, total),
        _section_top_opportunities(reliable, events),
    ]
    if events is not None:
        sections.append(_section_upcoming_events(instruments, events, window_days))
    if qualitative is not None:
        sections.append(_section_ai_commentary(qualitative, evidence, instruments))
    sections.extend([
        _section_signal_history(history),
        _section_instruments_to_avoid(unreliable),
        _section_key_risks(instruments),
        _section_instrument_scores(instruments),
        _section_data_freshness(data_source, freshness),
        _section_symbol_details(instruments),
        _section_methodology(scoring_version, git_commit),
        _section_disclaimer(),
    ])
    body = "\n\n".join(sections)
    return f"{front_matter}\n\n{body}\n"


def report_filename(artifact: dict[str, Any]) -> str:
    meta = artifact.get("metadata", {})
    generated_at = meta.get("generated_at", "")
    if not isinstance(generated_at, str) or not generated_at:
        date_str = "1970-01-01"
    else:
        date_str = generated_at[:10]
    return f"{date_str}{artifact_interval_suffix(artifact)}-market-analysis.md"


def _load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as fh:
        value: dict[str, Any] = json.load(fh)
    return value


def generate_and_save(
    artifact_path: Path,
    output_dir: Path = _DEFAULT_OUTPUT_DIR,
    history_path: Path | None = None,
    *,
    calendar_paths: list[Path] | None = None,
    qualitative_path: Path | None = None,
    evidence_path: Path | None = None,
    window_days: int = DEFAULT_WINDOW_DAYS,
) -> Path:
    artifact = _load_json(artifact_path)
    _validate_for_report(artifact)
    history = _load_json(history_path) if history_path is not None else None
    calendar_events = load_calendar_events(calendar_paths) if calendar_paths else None
    qualitative = _load_json(qualitative_path) if qualitative_path is not None else None
    evidence = _load_json(evidence_path) if evidence_path is not None else None
    content = generate_report(
        artifact,
        history,
        calendar_events=calendar_events,
        window_days=window_days,
        qualitative=qualitative,
        evidence=evidence,
    )
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
    parser.add_argument("--history", type=Path, help="Path to score-history JSON")
    parser.add_argument(
        "--calendar",
        type=Path,
        action="append",
        default=None,
        help="Calendar JSON file for the Upcoming Events section (repeatable)",
    )
    parser.add_argument(
        "--events-window-days",
        type=int,
        default=DEFAULT_WINDOW_DAYS,
        help="Upcoming-events window in days after the analysis date",
    )
    parser.add_argument(
        "--qualitative",
        type=Path,
        default=None,
        help="Validated, gate-passed qualitative artifact to render",
    )
    parser.add_argument(
        "--evidence",
        type=Path,
        default=None,
        help="Evidence bundle for resolving qualitative citations",
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
    if args.qualitative is not None and args.evidence is None:
        print("ERROR: --qualitative requires --evidence for citation sources.")
        return 1
    try:
        generate_and_save(
            args.input,
            args.output,
            args.history,
            calendar_paths=args.calendar,
            qualitative_path=args.qualitative,
            evidence_path=args.evidence,
            window_days=args.events_window_days,
        )
    except FileNotFoundError as exc:
        print(f"ERROR: file not found: {exc.filename}")
        return 1
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON in input: {exc}")
        return 1
    except ValueError as exc:
        print(f"ERROR: artifact validation failed: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
