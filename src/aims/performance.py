r"""Evaluate published AI qualitative stances against realized forward returns.

Deterministic accountability loop for the qualitative layer (#97, sharing the
``data/performance/`` home planned by #82): per-instrument stances from
committed ``data/qualitative/`` artifacts are joined with realized forward
returns derived purely from committed ``data/analysis/`` artifacts — no live
price fetches — so the same inputs always produce the same artifact.

Forward returns are reconstructed by chaining each symbol's trailing
``ret_1d`` feature across analysis artifacts, keyed by the per-symbol bar
date in ``metadata.data_freshness``. The chain is self-checked: wherever a
``ret_5d`` feature is available, the compounded product of the trailing five
chained ``ret_1d`` values must match it within tolerance, so a bar silently
missed between committed artifacts (e.g. a skipped scheduled run) invalidates
the affected links instead of producing wrong returns.

Results measure informational association only — never an investable or
executable track record. The disclaimer is embedded in every artifact and
rendered prominently on the evaluation page.

Trust boundary: the daily workflow's qualitative-analysis step is
``continue-on-error``, so a same-run ``data/qualitative/<stem>.json`` file
can exist on disk even after a failed or unvalidated run.
``--exclude-qualitative-date`` lets the caller exclude that date from
evaluation regardless of whether the file is present, mirroring the trust
boundary already used for report rendering and Slack notifications
(``steps.qualitative.outcome == 'success'``). Historical, already-validated
artifacts are never affected by this flag.

Usage:
    uv run .agents/skills/qualitative-analysis/scripts/evaluate_stances.py \
        --input data/analysis/2026-07-04.json \
        --analysis-dir data/analysis \
        --qualitative-dir data/qualitative \
        --output data/performance \
        --page-output content/evaluation/_index.md
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Final, NamedTuple

from aims.evidence import git_commit
from aims.reports import MarkdownAlignment, format_markdown_table

PERFORMANCE_VERSION: Final[str] = "1.0.0"
DEFAULT_HORIZONS: Final[tuple[int, ...]] = (1, 5, 20)
STANCES: Final[tuple[str, ...]] = ("supportive", "neutral", "conflicting")
CONFIDENCES: Final[tuple[str, ...]] = ("low", "medium", "high")
# Compounded chained ret_1d values must reproduce a later ret_5d within this
# absolute tolerance on the return scale; larger gaps mark the links broken.
RETURN_CONSISTENCY_TOLERANCE: Final[float] = 1e-3
_ROUND_DIGITS: Final[int] = 6
_MAX_PAGE_WARNINGS: Final[int] = 20

_DEFAULT_ANALYSIS_DIR: Final[Path] = Path("data/analysis")
_DEFAULT_QUALITATIVE_DIR: Final[Path] = Path("data/qualitative")
_DEFAULT_OUTPUT_DIR: Final[Path] = Path("data/performance")

_DATE_RE: Final[re.Pattern[str]] = re.compile(r"^\d{4}-\d{2}-\d{2}$")

DISCLAIMER: Final[str] = (
    "Informational association only. These figures measure whether published"
    " AI stances lined up with subsequent price moves in committed data; they"
    " are not an investable or executable track record, exclude fees,"
    " slippage, financing, and order timing, rest on small overlapping"
    " samples, and are not investment advice."
)


class Bar(NamedTuple):
    """One chained trading bar reconstructed from a committed analysis row."""

    date: str
    ret_1d: float
    ret_5d: float | None


def _artifact_date(artifact: dict[str, Any]) -> str:
    generated_at = artifact.get("metadata", {}).get("generated_at")
    if not isinstance(generated_at, str) or not _DATE_RE.match(generated_at[:10]):
        msg = "analysis artifact has no valid metadata.generated_at"
        raise ValueError(msg)
    return generated_at[:10]


def _analysis_interval(artifact: dict[str, Any]) -> str:
    return str(artifact.get("metadata", {}).get("config", {}).get("interval", ""))


def _qualitative_date(artifact: dict[str, Any]) -> str:
    date = artifact.get("metadata", {}).get("analysis_date")
    if not isinstance(date, str) or not _DATE_RE.match(date):
        msg = "qualitative artifact has no valid metadata.analysis_date"
        raise ValueError(msg)
    return date


def _qualitative_interval(artifact: dict[str, Any]) -> str:
    return str(artifact.get("metadata", {}).get("interval", ""))


def build_bar_series(
    analyses: list[dict[str, Any]],
) -> tuple[dict[str, list[Bar]], list[str]]:
    """Chain per-symbol bars from analysis artifacts, later artifacts winning.

    Bars are keyed by the per-symbol ``metadata.data_freshness`` date, so
    weekend or holiday artifacts that repeat the previous bar collapse into
    one entry. Conflicting ``ret_1d`` values for the same bar (provider
    revisions) keep the latest artifact's value and record a warning.
    """
    by_symbol: dict[str, dict[str, Bar]] = {}
    warnings: list[str] = []
    for analysis in sorted(analyses, key=_artifact_date):
        freshness = analysis.get("metadata", {}).get("data_freshness", {})
        for inst in analysis.get("instruments", []):
            symbol = str(inst.get("symbol", ""))
            bar_date = freshness.get(symbol) if isinstance(freshness, dict) else None
            features = inst.get("features") or {}
            ret_1d = features.get("ret_1d")
            if (
                not symbol
                or not isinstance(bar_date, str)
                or not _DATE_RE.match(bar_date)
                or not isinstance(ret_1d, (int, float))
            ):
                continue
            ret_5d_raw = features.get("ret_5d")
            ret_5d = float(ret_5d_raw) if isinstance(ret_5d_raw, (int, float)) else None
            bars = by_symbol.setdefault(symbol, {})
            existing = bars.get(bar_date)
            if (
                existing is not None
                and abs(existing.ret_1d - float(ret_1d)) > RETURN_CONSISTENCY_TOLERANCE
            ):
                warnings.append(
                    f"{symbol}: conflicting ret_1d for bar {bar_date} across"
                    " analysis artifacts; keeping the latest value"
                )
            bars[bar_date] = Bar(bar_date, float(ret_1d), ret_5d)
    series = {
        symbol: [bars[date] for date in sorted(bars)]
        for symbol, bars in by_symbol.items()
    }
    return series, warnings


def chain_breaks(bars: list[Bar]) -> set[int]:
    """Return untrusted link indices (link ``k`` connects bar k-1 to bar k).

    Wherever a bar carries ``ret_5d``, the compounded product of the trailing
    five chained ``ret_1d`` values must reproduce it; a mismatch means at
    least one real trading bar is missing from the chain inside that window,
    so all five links are marked broken.
    """
    broken: set[int] = set()
    for j in range(5, len(bars)):
        ret_5d = bars[j].ret_5d
        if ret_5d is None:
            continue
        product = 1.0
        for k in range(j - 4, j + 1):
            product *= 1.0 + bars[k].ret_1d
        if abs(product - 1.0 - ret_5d) > RETURN_CONSISTENCY_TOLERANCE:
            broken.update(range(j - 4, j + 1))
    return broken


def forward_return(
    bars: list[Bar], broken: set[int], index: int, horizon: int
) -> float | None:
    """Compound the next *horizon* chained bars; None on any broken link."""
    end = index + horizon
    if any(k in broken for k in range(index + 1, end + 1)):
        return None
    product = 1.0
    for k in range(index + 1, end + 1):
        product *= 1.0 + bars[k].ret_1d
    return product - 1.0


def _round_or_none(value: float | None) -> float | None:
    return None if value is None else round(value, _ROUND_DIGITS)


def _mean(values: list[float]) -> float | None:
    return sum(values) / len(values) if values else None


class _HorizonTally:
    """Mutable per-horizon accumulator for stance and confidence outcomes."""

    def __init__(self) -> None:
        self.pending = 0
        self.broken_chain = 0
        self.returns: dict[str, list[float]] = {stance: [] for stance in STANCES}
        self.hits: dict[str, list[bool]] = {stance: [] for stance in STANCES}
        self.confidence_hits: dict[str, list[bool]] = {
            confidence: [] for confidence in CONFIDENCES
        }

    def record(self, stance: str, confidence: str, realized: float) -> None:
        self.returns[stance].append(realized)
        if stance == "supportive":
            hit = realized > 0
        elif stance == "conflicting":
            hit = realized < 0
        else:
            return
        self.hits[stance].append(hit)
        self.confidence_hits[confidence].append(hit)

    def summary(self) -> dict[str, Any]:
        stances: dict[str, Any] = {}
        for stance in STANCES:
            returns = self.returns[stance]
            hits = self.hits[stance]
            stances[stance] = {
                "count": len(returns),
                "hit_rate": _round_or_none(
                    _mean([float(hit) for hit in hits]) if stance != "neutral" else None
                ),
                "average_return": _round_or_none(_mean(returns)),
            }
        calibration: dict[str, Any] = {}
        for confidence in CONFIDENCES:
            hits = self.confidence_hits[confidence]
            calibration[confidence] = {
                "count": len(hits),
                "hit_rate": _round_or_none(_mean([float(hit) for hit in hits])),
            }
        return {
            "observations": sum(len(values) for values in self.returns.values()),
            "pending": self.pending,
            "broken_chain": self.broken_chain,
            "stances": stances,
            "confidence_calibration": calibration,
        }


def evaluate_stances(
    qualitative_artifacts: list[dict[str, Any]],
    analyses: list[dict[str, Any]],
    horizons: tuple[int, ...] = DEFAULT_HORIZONS,
) -> tuple[dict[str, Any], list[str]]:
    """Join ungated stances with realized forward returns per horizon."""
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
    analyses_by_date = {_artifact_date(a): a for a in analyses}

    tallies = {horizon: _HorizonTally() for horizon in horizons}
    evaluated = 0
    excluded_gated = 0
    unmatched = 0
    if not qualitative_artifacts:
        warnings.append("no qualitative artifacts found; stance evaluation is empty")
    for artifact in sorted(qualitative_artifacts, key=_qualitative_date):
        date = _qualitative_date(artifact)
        analysis = analyses_by_date.get(date)
        if analysis is None:
            warnings.append(f"{date}: no analysis artifact for qualitative artifact")
            continue
        freshness = analysis.get("metadata", {}).get("data_freshness", {})
        for entry in artifact.get("instruments", []):
            symbol = str(entry.get("symbol", ""))
            if entry.get("qualitative_gates"):
                excluded_gated += 1
                continue
            stance = str(entry.get("stance", ""))
            confidence = str(entry.get("confidence", ""))
            if stance not in STANCES or confidence not in CONFIDENCES:
                warnings.append(f"{date}: {symbol}: invalid stance or confidence")
                continue
            bar_date = freshness.get(symbol)
            index = index_of.get(symbol, {}).get(str(bar_date))
            if index is None:
                unmatched += 1
                warnings.append(f"{date}: {symbol}: no chained bar for the stance")
                continue
            evaluated += 1
            bars = series[symbol]
            for horizon in horizons:
                tally = tallies[horizon]
                if index + horizon >= len(bars):
                    tally.pending += 1
                    continue
                realized = forward_return(bars, broken[symbol], index, horizon)
                if realized is None:
                    tally.broken_chain += 1
                    warnings.append(
                        f"{date}: {symbol}: broken bar chain within {horizon}d"
                        " forward window"
                    )
                    continue
                tally.record(stance, confidence, realized)

    return {
        "instruments_evaluated": evaluated,
        "excluded_gated": excluded_gated,
        "unmatched": unmatched,
        "horizons": {f"{horizon}d": tallies[horizon].summary() for horizon in horizons},
    }, sorted(warnings)


def build_artifact(
    qualitative_artifacts: list[dict[str, Any]],
    analyses: list[dict[str, Any]],
    *,
    as_of: str,
    interval: str,
    horizons: tuple[int, ...] = DEFAULT_HORIZONS,
    extra_warnings: tuple[str, ...] = (),
) -> dict[str, Any]:
    """Assemble the versioned, schema-validated stance-evaluation artifact.

    *extra_warnings* carries warnings from outside the join itself — e.g. a
    same-run qualitative artifact excluded by the caller's trust boundary —
    merged in deduplicated and sorted alongside the evaluation's own warnings.
    """
    stance_evaluation, warnings = evaluate_stances(
        qualitative_artifacts, analyses, horizons
    )
    all_warnings = sorted({*warnings, *extra_warnings})
    return {
        "version": PERFORMANCE_VERSION,
        "metadata": {
            "generated_at": f"{as_of}T00:00:00+00:00",
            "analysis_date": as_of,
            "interval": interval,
            "git_commit": git_commit(),
            "config": {
                "horizons": list(horizons),
                "return_consistency_tolerance": RETURN_CONSISTENCY_TOLERANCE,
            },
            "inputs": {
                "analysis_dates": sorted(_artifact_date(a) for a in analyses),
                "qualitative_dates": sorted(
                    _qualitative_date(q) for q in qualitative_artifacts
                ),
            },
            "disclaimer": DISCLAIMER,
        },
        "stance_evaluation": stance_evaluation,
        "warnings": all_warnings,
    }


def _pct(value: float | None, *, signed: bool = False) -> str:
    if value is None:
        return "n/a"
    if signed:
        return f"{value * 100:+.2f}%"
    return f"{value * 100:.0f}%"


def _date_range(dates: list[Any]) -> str:
    if not dates:
        return "none"
    return f"{len(dates)} ({dates[0]} to {dates[-1]})"


def _horizon_section(name: str, horizon: dict[str, Any]) -> str:
    stance_rows = [
        [
            stance,
            str(horizon["stances"][stance]["count"]),
            _pct(horizon["stances"][stance]["hit_rate"]),
            _pct(horizon["stances"][stance]["average_return"], signed=True),
        ]
        for stance in STANCES
    ]
    alignments: list[MarkdownAlignment] = ["left", "right", "right", "right"]
    table = format_markdown_table(
        ["Stance", "Count", "Hit rate", "Average return"], stance_rows, alignments
    )
    status = (
        f"{horizon['observations']} matured, {horizon['pending']} pending,"
        f" {horizon['broken_chain']} skipped (broken bar chain)."
    )
    return f"### {name} horizon\n\n{status}\n\n{table}"


def _horizon_names(horizons: dict[str, Any]) -> list[str]:
    """Horizon keys in numeric order, stable across JSON round-trips."""
    return sorted(horizons, key=lambda name: int(name.removesuffix("d")))


def _calibration_section(horizons: dict[str, Any]) -> str:
    rows = [
        [
            f"{name} / {confidence}",
            str(horizons[name]["confidence_calibration"][confidence]["count"]),
            _pct(horizons[name]["confidence_calibration"][confidence]["hit_rate"]),
        ]
        for name in _horizon_names(horizons)
        for confidence in CONFIDENCES
    ]
    alignments: list[MarkdownAlignment] = ["left", "right", "right"]
    table = format_markdown_table(
        ["Horizon / Confidence", "Count", "Hit rate"], rows, alignments
    )
    preamble = (
        "Directional stances (supportive and conflicting) grouped by the"
        " model's stated confidence; higher confidence should show a higher"
        " hit rate."
    )
    return f"## Confidence Calibration\n\n{preamble}\n\n{table}"


def render_page(artifact: dict[str, Any]) -> str:
    """Render the deterministic Hugo evaluation page from the artifact."""
    meta = artifact["metadata"]
    date = str(meta["analysis_date"])
    stance_evaluation = artifact["stance_evaluation"]
    horizons: dict[str, Any] = stance_evaluation["horizons"]
    matured = sum(int(h["observations"]) for h in horizons.values())
    inputs = meta["inputs"]

    if matured:
        summary = (
            f"AI stance evaluation as of {date}: {matured} matured stance observations."
        )
    else:
        summary = f"AI stance evaluation as of {date}: no matured observations yet."
    stem = date if meta["interval"] == "d" else f"{date}-{meta['interval']}"
    front_matter = "\n".join([
        "+++",
        'title = "AI Stance Evaluation"',
        f'date = "{meta["generated_at"]}"',
        "draft = false",
        f'summary = "{summary}"',
        f'source_files = ["data/performance/{stem}.json"]',
        "+++",
    ])

    intro = (
        "This page evaluates the AI qualitative layer's published"
        " per-instrument stances (supportive / neutral / conflicting) against"
        " realized forward returns reconstructed deterministically from"
        " committed analysis artifacts. A supportive stance counts as a hit"
        " when the instrument's forward return is positive; a conflicting"
        " stance counts as a hit when it is negative; neutral stances are"
        " tracked but not scored directionally."
    )
    disclaimer = f"> **{DISCLAIMER}**"

    parts = [front_matter, intro, disclaimer, "## Stance Hit Rates"]
    if matured:
        parts.extend(
            _horizon_section(name, horizons[name]) for name in _horizon_names(horizons)
        )
        parts.append(_calibration_section(horizons))
    else:
        parts.append(
            "_No matured stance observations yet. Stances need enough"
            " subsequent committed analysis artifacts to cover each forward"
            " horizon before they can be scored; this page fills in as"
            " qualitative artifacts and forward bars accumulate._"
        )

    status_lines = [
        f"- Analysis artifacts: {_date_range(inputs['analysis_dates'])}",
        f"- Qualitative artifacts: {_date_range(inputs['qualitative_dates'])}",
        (
            "- Stance entries evaluated:"
            f" {stance_evaluation['instruments_evaluated']}"
            f" (gate-excluded: {stance_evaluation['excluded_gated']},"
            f" unmatched: {stance_evaluation['unmatched']})"
        ),
    ]
    warnings = artifact["warnings"]
    if warnings:
        status_lines.append(f"- Warnings ({len(warnings)}):")
        status_lines.extend(
            f"  - {warning}" for warning in warnings[:_MAX_PAGE_WARNINGS]
        )
        if len(warnings) > _MAX_PAGE_WARNINGS:
            status_lines.append(f"  - … and {len(warnings) - _MAX_PAGE_WARNINGS} more")
    parts.append("## Data Status\n\n" + "\n".join(status_lines))

    methodology = (
        "## Methodology\n\n"
        "Forward returns are compounded from each symbol's trailing `ret_1d`"
        " feature chained across committed analysis artifacts, keyed by the"
        " per-symbol bar date in `data_freshness` — no live price fetches."
        " Wherever a later artifact carries `ret_5d`, the compounded chain"
        " must reproduce it within tolerance; windows failing that"
        " self-check are skipped as broken rather than scored. Stances"
        " withheld by the qualitative consistency gates are excluded."
        " Details: `data/schema/performance.schema.json` and OPERATIONS.md"
        " §12."
    )
    parts.append(methodology)
    return "\n\n".join(parts) + "\n"


def _load(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        value: dict[str, Any] = json.load(stream)
    return value


def _load_qualitative_artifacts(
    qualitative_dir: Path,
    as_of: str,
    exclude_dates: frozenset[str],
) -> tuple[list[dict[str, Any]], list[str]]:
    """Load committed daily qualitative artifacts up to *as_of*.

    Dates in *exclude_dates* are skipped even when a file is present on
    disk: the daily workflow's qualitative-analysis step is
    ``continue-on-error``, so a same-run file can exist after a failed or
    unvalidated run. Historical, already-validated artifacts are never
    affected by this trust boundary since only the caller-specified dates
    (in practice, at most today's) are ever excluded.
    """
    artifacts: list[dict[str, Any]] = []
    warnings: list[str] = []
    if not qualitative_dir.is_dir():
        return artifacts, warnings
    for path in sorted(qualitative_dir.glob("*.json")):
        artifact = _load(path)
        if _qualitative_interval(artifact) != "d":
            continue
        when = _qualitative_date(artifact)
        if when > as_of:
            continue
        if when in exclude_dates:
            warnings.append(
                f"{when}: excluded a same-run qualitative artifact because"
                " the qualitative-analysis step did not report success"
            )
            continue
        artifacts.append(artifact)
    return artifacts, warnings


def generate(
    input_path: Path,
    analysis_dir: Path,
    qualitative_dir: Path,
    output_dir: Path,
    *,
    horizons: tuple[int, ...] = DEFAULT_HORIZONS,
    page_output: Path | None = None,
    exclude_qualitative_dates: frozenset[str] = frozenset(),
) -> Path:
    """Build, write, and optionally render the stance-evaluation artifact."""
    current = _load(input_path)
    as_of = _artifact_date(current)
    if _analysis_interval(current) != "d":
        msg = "stance evaluation supports the daily interval only"
        raise ValueError(msg)
    analyses = [current]
    for path in sorted(analysis_dir.glob("*.json")):
        if path.resolve() == input_path.resolve():
            continue
        artifact = _load(path)
        if _analysis_interval(artifact) == "d" and _artifact_date(artifact) <= as_of:
            analyses.append(artifact)
    qualitative_artifacts, load_warnings = _load_qualitative_artifacts(
        qualitative_dir, as_of, exclude_qualitative_dates
    )

    artifact = build_artifact(
        qualitative_artifacts,
        analyses,
        as_of=as_of,
        interval="d",
        horizons=horizons,
        extra_warnings=tuple(load_warnings),
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    output = output_dir / f"{as_of}.json"
    output.write_text(
        json.dumps(artifact, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"Stance evaluation written to {output}")
    if page_output is not None:
        page_output.parent.mkdir(parents=True, exist_ok=True)
        page_output.write_text(render_page(artifact), encoding="utf-8")
        print(f"Evaluation page written to {page_output}")
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
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--analysis-dir", default=_DEFAULT_ANALYSIS_DIR, type=Path)
    parser.add_argument(
        "--qualitative-dir", default=_DEFAULT_QUALITATIVE_DIR, type=Path
    )
    parser.add_argument("--output", default=_DEFAULT_OUTPUT_DIR, type=Path)
    parser.add_argument("--horizons", default=DEFAULT_HORIZONS, type=_parse_horizons)
    parser.add_argument(
        "--page-output",
        default=None,
        type=Path,
        help="Optional Hugo page path (e.g. content/evaluation/_index.md)",
    )
    parser.add_argument(
        "--exclude-qualitative-date",
        dest="exclude_qualitative_dates",
        action="append",
        default=[],
        help=(
            "Qualitative artifact date (YYYY-MM-DD) to exclude even if present"
            " on disk, e.g. when the same-run qualitative-analysis step did not"
            " report success (repeatable)"
        ),
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        generate(
            args.input,
            args.analysis_dir,
            args.qualitative_dir,
            args.output,
            horizons=tuple(args.horizons),
            page_output=args.page_output,
            exclude_qualitative_dates=frozenset(args.exclude_qualitative_dates),
        )
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as exc:
        print(f"ERROR: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
