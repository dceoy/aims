r"""Track realized forward returns of published top-5 quantitative signals.

Deterministic accountability loop for the quantitative pipeline (#82): each
committed ``data/analysis/`` artifact's top-5 reliable, tradable instruments
are joined with realized forward returns reconstructed purely from committed
analysis artifacts — no live price fetches — against an equal-weight
benchmark over the same artifact's reliable universe. This measures whether
the published top-5 outperformed a naive equal-weight basket, not an
investable or executable track record.

Reuses the bar-chaining and forward-return machinery from ``aims.performance``
(#97's stance-evaluation loop): per-symbol ``ret_1d`` values are chained
across artifacts, self-checked against ``ret_5d`` where available, and a
mismatch invalidates the affected links instead of producing wrong returns.

The artifact is a single cumulative file (``data/performance/signals.json``),
rebuilt in full from every committed daily analysis artifact on each run —
unlike the dated stance-evaluation artifacts, there is one growing record.

Usage:
    uv run .agents/skills/market-analysis/scripts/track_signal_performance.py \
        --analysis-dir data/analysis \
        --output data/performance/signals.json \
        --page-output content/performance/_index.md
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Final, NamedTuple

from aims.evidence import git_commit
from aims.performance import (
    RETURN_CONSISTENCY_TOLERANCE,
    Bar,
    build_bar_series,
    chain_breaks,
    forward_return,
)
from aims.reports import MarkdownAlignment, format_markdown_table

SIGNAL_PERFORMANCE_VERSION: Final[str] = "1.0.0"
DEFAULT_HORIZONS: Final[tuple[int, ...]] = (1, 5, 20)
TOP_K: Final[int] = 5
_ROUND_DIGITS: Final[int] = 6
_MAX_PAGE_WARNINGS: Final[int] = 20

_DEFAULT_ANALYSIS_DIR: Final[Path] = Path("data/analysis")
_DEFAULT_OUTPUT: Final[Path] = Path("data/performance/signals.json")

DISCLAIMER: Final[str] = (
    "Informational association only. These figures measure whether the"
    " published top-5 quantitative signals outperformed a naive equal-weight"
    " basket of the same day's reliable universe in committed data; they are"
    " not an investable or executable track record, exclude fees, slippage,"
    " financing, and order timing, rest on small overlapping samples, and are"
    " not investment advice."
)


class _SlotObservation(NamedTuple):
    """One realized top-5 slot: its return, that date's benchmark, and tags."""

    realized: float
    benchmark: float
    asset_class: str
    regime: str


def _artifact_date(artifact: dict[str, Any]) -> str:
    generated_at = artifact.get("metadata", {}).get("generated_at")
    if not isinstance(generated_at, str) or len(generated_at) < 10:
        msg = "analysis artifact has no valid metadata.generated_at"
        raise ValueError(msg)
    return generated_at[:10]


def _analysis_interval(artifact: dict[str, Any]) -> str:
    return str(artifact.get("metadata", {}).get("config", {}).get("interval", ""))


def _mean(values: list[float]) -> float | None:
    return sum(values) / len(values) if values else None


def _round_or_none(value: float | None) -> float | None:
    return None if value is None else round(value, _ROUND_DIGITS)


def _resolve_return(
    symbol: str,
    freshness: dict[str, Any],
    series: dict[str, list[Bar]],
    broken: dict[str, set[int]],
    index_of: dict[str, dict[str, int]],
    horizon: int,
) -> tuple[float | None, str]:
    """Resolve *symbol*'s realized forward return, or the reason it can't yet.

    Status is one of "ok", "unmatched" (no chained bar for this artifact's
    bar date), "pending" (not enough future bars chained yet), or "broken"
    (a bar is missing inside the forward window).
    """
    bar_date = freshness.get(symbol)
    if not isinstance(bar_date, str):
        return None, "unmatched"
    index = index_of.get(symbol, {}).get(bar_date)
    if index is None:
        return None, "unmatched"
    bars = series[symbol]
    if index + horizon >= len(bars):
        return None, "pending"
    realized = forward_return(bars, broken[symbol], index, horizon)
    if realized is None:
        return None, "broken"
    return realized, "ok"


def evaluate_signals(
    analyses: list[dict[str, Any]],
    horizons: tuple[int, ...] = DEFAULT_HORIZONS,
) -> tuple[dict[str, Any], list[str]]:
    """Join each artifact's top-5 with realized forward returns and a benchmark.

    Each of a date's top-5 instruments becomes one "slot observation" tagged
    with its asset class and that date's market regime label, paired with the
    equal-weight benchmark return over the full reliable universe that date.
    Grouping the flat pool of slot observations by tag yields the
    per-asset-class and per-regime breakdowns without needing a date-level
    top-5 average to already be complete in every asset class or regime.
    """
    if (
        not horizons
        or any(h < 1 for h in horizons)
        or len(set(horizons)) != len(horizons)
    ):
        msg = "horizons must be unique positive integers"
        raise ValueError(msg)
    series, warnings = build_bar_series(analyses)
    broken = {symbol: chain_breaks(bars) for symbol, bars in series.items()}
    index_of = {
        symbol: {bar.date: i for i, bar in enumerate(bars)}
        for symbol, bars in series.items()
    }

    slots: dict[int, list[_SlotObservation]] = {h: [] for h in horizons}
    pending = dict.fromkeys(horizons, 0)
    incomplete = dict.fromkeys(horizons, 0)
    dates_evaluated = 0

    for analysis in sorted(analyses, key=_artifact_date):
        date = _artifact_date(analysis)
        freshness = analysis.get("metadata", {}).get("data_freshness", {})
        instruments = analysis.get("instruments", [])
        reliable = [
            inst
            for inst in instruments
            if inst.get("is_reliable") and inst.get("tradable") is not False
        ]
        if not reliable:
            continue
        top5 = sorted(
            reliable, key=lambda inst: float(inst.get("score", 0)), reverse=True
        )[:TOP_K]
        regime = str(
            (analysis.get("metadata", {}).get("market_regime") or {}).get("label")
            or "Unavailable"
        )
        dates_evaluated += 1
        for horizon in horizons:
            benchmark_values: list[float] = []
            for inst in reliable:
                realized, status = _resolve_return(
                    str(inst.get("symbol", "")),
                    freshness,
                    series,
                    broken,
                    index_of,
                    horizon,
                )
                if status == "ok" and realized is not None:
                    benchmark_values.append(realized)
            benchmark_avg = _mean(benchmark_values)
            for inst in top5:
                symbol = str(inst.get("symbol", ""))
                realized, status = _resolve_return(
                    symbol, freshness, series, broken, index_of, horizon
                )
                if status == "pending":
                    pending[horizon] += 1
                    continue
                if status != "ok" or realized is None or benchmark_avg is None:
                    incomplete[horizon] += 1
                    if status == "broken":
                        warnings.append(
                            f"{date}: {symbol}: broken bar chain within"
                            f" {horizon}d forward window"
                        )
                    continue
                slots[horizon].append(
                    _SlotObservation(
                        realized,
                        benchmark_avg,
                        str(inst.get("asset_class") or "unknown"),
                        regime,
                    )
                )

    def _bucket_summary(observations: list[_SlotObservation]) -> dict[str, Any]:
        top5_avg = _mean([o.realized for o in observations])
        benchmark_avg = _mean([o.benchmark for o in observations])
        excess = (
            None
            if top5_avg is None or benchmark_avg is None
            else top5_avg - benchmark_avg
        )
        hits = [o.realized > o.benchmark for o in observations]
        return {
            "count": len(observations),
            "top5_average_return": _round_or_none(top5_avg),
            "benchmark_average_return": _round_or_none(benchmark_avg),
            "excess_return": _round_or_none(excess),
            "hit_rate": _round_or_none(
                _mean([float(h) for h in hits]) if hits else None
            ),
        }

    horizons_out: dict[str, Any] = {}
    for horizon in horizons:
        observations = slots[horizon]
        by_asset_class: dict[str, list[_SlotObservation]] = defaultdict(list)
        by_regime: dict[str, list[_SlotObservation]] = defaultdict(list)
        for obs in observations:
            by_asset_class[obs.asset_class].append(obs)
            by_regime[obs.regime].append(obs)
        summary = _bucket_summary(observations)
        summary["pending"] = pending[horizon]
        summary["incomplete"] = incomplete[horizon]
        summary["by_asset_class"] = {
            key: _bucket_summary(values)
            for key, values in sorted(by_asset_class.items())
        }
        summary["by_regime"] = {
            key: _bucket_summary(values) for key, values in sorted(by_regime.items())
        }
        horizons_out[f"{horizon}d"] = summary

    return {
        "dates_evaluated": dates_evaluated,
        "horizons": horizons_out,
    }, sorted(set(warnings))


def build_artifact(
    analyses: list[dict[str, Any]],
    *,
    as_of: str,
    horizons: tuple[int, ...] = DEFAULT_HORIZONS,
) -> dict[str, Any]:
    """Assemble the versioned, schema-validated signal-performance artifact."""
    signal_evaluation, warnings = evaluate_signals(analyses, horizons)
    return {
        "version": SIGNAL_PERFORMANCE_VERSION,
        "metadata": {
            "generated_at": f"{as_of}T00:00:00+00:00",
            "as_of": as_of,
            "git_commit": git_commit(),
            "config": {
                "top_k": TOP_K,
                "horizons": list(horizons),
                "return_consistency_tolerance": RETURN_CONSISTENCY_TOLERANCE,
            },
            "inputs": {"analysis_dates": sorted(_artifact_date(a) for a in analyses)},
            "disclaimer": DISCLAIMER,
        },
        "signal_evaluation": signal_evaluation,
        "warnings": warnings,
    }


def _pct(value: float | None, *, signed: bool = False) -> str:
    if value is None:
        return "n/a"
    if signed:
        return f"{value * 100:+.2f}%"
    return f"{value * 100:.0f}%"


def _horizon_names(horizons: dict[str, Any]) -> list[str]:
    return sorted(horizons, key=lambda name: int(name.removesuffix("d")))


def _overview_table(horizons: dict[str, Any]) -> str:
    rows = [
        [
            name,
            str(horizons[name]["count"]),
            _pct(horizons[name]["top5_average_return"], signed=True),
            _pct(horizons[name]["benchmark_average_return"], signed=True),
            _pct(horizons[name]["excess_return"], signed=True),
            _pct(horizons[name]["hit_rate"]),
        ]
        for name in _horizon_names(horizons)
    ]
    alignments: list[MarkdownAlignment] = [
        "left",
        "right",
        "right",
        "right",
        "right",
        "right",
    ]
    return format_markdown_table(
        ["Horizon", "Count", "Top-5", "Benchmark", "Excess", "Hit rate"],
        rows,
        alignments,
    )


def _breakdown_section(title: str, key: str, horizons: dict[str, Any]) -> str:
    rows = [
        [
            f"{name} / {label}",
            str(bucket["count"]),
            _pct(bucket["excess_return"], signed=True),
            _pct(bucket["hit_rate"]),
        ]
        for name in _horizon_names(horizons)
        for label, bucket in sorted(horizons[name][key].items())
    ]
    if not rows:
        return f"### {title}\n\n_No matured observations yet._"
    alignments: list[MarkdownAlignment] = ["left", "right", "right", "right"]
    table = format_markdown_table(
        ["Horizon / Group", "Count", "Excess", "Hit rate"], rows, alignments
    )
    return f"### {title}\n\n{table}"


def render_page(artifact: dict[str, Any]) -> str:
    """Render the deterministic Hugo signal-performance page from the artifact."""
    meta = artifact["metadata"]
    as_of = str(meta["as_of"])
    evaluation = artifact["signal_evaluation"]
    horizons = evaluation["horizons"]
    warnings = artifact["warnings"]

    front_matter = "\n".join([
        "+++",
        'title = "Signal Performance"',
        f'date = "{meta["generated_at"]}"',
        "draft = false",
        (
            f'summary = "Realized forward returns of the published top-{TOP_K}'
            ' signals vs. an equal-weight benchmark."'
        ),
        'source_files = ["data/performance/signals.json"]',
        "+++",
    ])

    intro = (
        f"As of **{as_of}**, {evaluation['dates_evaluated']} daily analysis"
        f" artifact(s) evaluated.\n\n> {artifact['metadata']['disclaimer']}"
    )

    sections = [
        front_matter,
        "## Signal Performance",
        intro,
        "## Cumulative Overview",
        _overview_table(horizons),
        _breakdown_section("By Asset Class", "by_asset_class", horizons),
        _breakdown_section("By Market Regime", "by_regime", horizons),
    ]

    if warnings:
        shown = warnings[:_MAX_PAGE_WARNINGS]
        lines = "\n".join(f"- {w}" for w in shown)
        more = len(warnings) - len(shown)
        if more > 0:
            lines += f"\n- … and {more} more"
        sections.append(f"## Warnings ({len(warnings)})\n\n{lines}")

    return "\n\n".join(sections) + "\n"


def _load(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        value: dict[str, Any] = json.load(stream)
    return value


def generate(
    analysis_dir: Path,
    output: Path,
    *,
    horizons: tuple[int, ...] = DEFAULT_HORIZONS,
    page_output: Path | None = None,
) -> Path:
    """Build, write, and optionally render the signal-performance artifact."""
    analyses = [
        artifact
        for path in sorted(analysis_dir.glob("*.json"))
        if _analysis_interval(artifact := _load(path)) == "d"
    ]
    if not analyses:
        msg = f"no daily analysis artifacts found under {analysis_dir}"
        raise ValueError(msg)
    as_of = max(_artifact_date(a) for a in analyses)
    artifact = build_artifact(analyses, as_of=as_of, horizons=horizons)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(artifact, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"Signal performance written to {output}")
    if page_output is not None:
        page_output.parent.mkdir(parents=True, exist_ok=True)
        page_output.write_text(render_page(artifact), encoding="utf-8")
        print(f"Signal performance page written to {page_output}")
    return output


def _parse_horizons(value: str) -> tuple[int, ...]:
    try:
        horizons = tuple(int(item) for item in value.split(","))
    except ValueError as exc:
        msg = "horizons must be comma-separated positive integers"
        raise argparse.ArgumentTypeError(msg) from exc
    if not horizons or any(h < 1 for h in horizons):
        msg = "horizons must be comma-separated positive integers"
        raise argparse.ArgumentTypeError(msg)
    return horizons


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--analysis-dir", default=_DEFAULT_ANALYSIS_DIR, type=Path)
    parser.add_argument("--output", default=_DEFAULT_OUTPUT, type=Path)
    parser.add_argument("--horizons", default=DEFAULT_HORIZONS, type=_parse_horizons)
    parser.add_argument(
        "--page-output",
        default=None,
        type=Path,
        help="Optional Hugo page path (e.g. content/performance/_index.md)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        generate(
            args.analysis_dir,
            args.output,
            horizons=tuple(args.horizons),
            page_output=args.page_output,
        )
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as exc:
        print(f"ERROR: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
