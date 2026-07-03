r"""Evaluate published AI qualitative stances against realized forward returns.

Joins per-instrument stances from qualitative artifacts with realized forward
returns computed from saved daily prices, entirely deterministically. Stances
are directional relative to the cross-sectional median: an ungated
"supportive" stance counts as a hit when the instrument's forward return is
at or above the median forward return of the evaluated entries for that date;
"conflicting" counts as a hit below the median; "neutral" entries are
excluded. Gated entries were never rendered, so they are excluded too.

This measures informational association, not an executable track record.

Usage:
    uv run .agents/skills/qualitative-analysis/scripts/evaluate_qualitative.py \
        evaluate --qualitative-dir data/qualitative --prices-dir data/prices \
        --output data/performance/qualitative_evaluation.json

    uv run .agents/skills/qualitative-analysis/scripts/evaluate_qualitative.py \
        check-links --evidence-dir data/evidence --sample 10
"""

from __future__ import annotations

import argparse
import json
import urllib.request
from bisect import bisect_right
from pathlib import Path
from typing import Any, Final

from aims.market_analysis import load_ohlcv

EVALUATION_VERSION: Final[str] = "1.0.0"
DEFAULT_HORIZONS: Final[tuple[int, ...]] = (1, 5, 20)
DEFAULT_OUTPUT: Final[Path] = Path("data/performance/qualitative_evaluation.json")
DEFAULT_LINK_SAMPLE: Final[int] = 10

_TIMEOUT: Final[int] = 15
_DIRECTIONAL_STANCES: Final[tuple[str, ...]] = ("supportive", "conflicting")
_CONFIDENCES: Final[tuple[str, ...]] = ("low", "medium", "high")
_REQUIRED_TOP: Final[tuple[str, ...]] = ("version", "metadata", "metrics")


def _median(values: list[float]) -> float:
    ordered = sorted(values)
    mid = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2.0


def _forward_return(
    closes_by_date: tuple[list[str], list[float]],
    analysis_date: str,
    horizon: int,
) -> float | None:
    dates, closes = closes_by_date
    idx = bisect_right(dates, analysis_date) - 1
    if idx < 0 or idx + horizon >= len(closes):
        return None
    return closes[idx + horizon] / closes[idx] - 1.0


def _load_series(
    symbol: str, interval: str, prices_dir: Path
) -> tuple[list[str], list[float]] | None:
    try:
        bars = load_ohlcv(symbol, interval, prices_dir)
    except FileNotFoundError:
        return None
    bars.sort(key=lambda b: b.timestamp)
    return (
        [b.timestamp.date().isoformat() for b in bars],
        [b.close for b in bars],
    )


def evaluate_stances(
    artifacts: list[dict[str, Any]],
    *,
    prices_dir: Path,
    interval: str = "d",
    horizons: tuple[int, ...] = DEFAULT_HORIZONS,
) -> dict[str, Any]:
    """Aggregate stance hit rates and excess returns across artifacts."""
    series_cache: dict[str, tuple[list[str], list[float]] | None] = {}
    samples: list[dict[str, Any]] = []
    evaluated_dates: list[str] = []

    for artifact in sorted(
        artifacts, key=lambda a: str(a.get("metadata", {}).get("analysis_date", ""))
    ):
        analysis_date = str(artifact.get("metadata", {}).get("analysis_date", ""))
        entries = [
            entry
            for entry in artifact.get("instruments") or []
            if isinstance(entry, dict) and not (entry.get("gates") or [])
        ]
        if not analysis_date or not entries:
            continue
        date_used = False
        for horizon in horizons:
            returns: dict[str, float] = {}
            for entry in entries:
                symbol = str(entry.get("symbol", ""))
                if symbol not in series_cache:
                    series_cache[symbol] = _load_series(symbol, interval, prices_dir)
                series = series_cache[symbol]
                if series is None:
                    continue
                forward = _forward_return(series, analysis_date, horizon)
                if forward is not None:
                    returns[symbol] = forward
            if len(returns) < 2:
                continue
            median = _median(list(returns.values()))
            for entry in entries:
                symbol = str(entry.get("symbol", ""))
                stance = str(entry.get("stance", ""))
                if symbol not in returns or stance not in _DIRECTIONAL_STANCES:
                    continue
                excess = returns[symbol] - median
                hit = excess >= 0 if stance == "supportive" else excess < 0
                samples.append({
                    "horizon": horizon,
                    "stance": stance,
                    "confidence": str(entry.get("confidence", "")),
                    "excess_return": excess,
                    "hit": hit,
                })
                date_used = True
        if date_used:
            evaluated_dates.append(analysis_date)

    metrics: dict[str, Any] = {}
    for horizon in horizons:
        horizon_samples = [s for s in samples if s["horizon"] == horizon]
        stance_metrics: dict[str, Any] = {}
        for stance in _DIRECTIONAL_STANCES:
            rows = [s for s in horizon_samples if s["stance"] == stance]
            stance_metrics[stance] = {
                "count": len(rows),
                "hit_rate": (
                    round(sum(1 for s in rows if s["hit"]) / len(rows), 4)
                    if rows
                    else None
                ),
                "mean_excess_return": (
                    round(sum(s["excess_return"] for s in rows) / len(rows), 6)
                    if rows
                    else None
                ),
            }
        by_confidence: dict[str, Any] = {}
        for confidence in _CONFIDENCES:
            rows = [s for s in horizon_samples if s["confidence"] == confidence]
            by_confidence[confidence] = {
                "count": len(rows),
                "hit_rate": (
                    round(sum(1 for s in rows if s["hit"]) / len(rows), 4)
                    if rows
                    else None
                ),
            }
        stance_metrics["by_confidence"] = by_confidence
        metrics[f"{horizon}d"] = stance_metrics

    return {
        "version": EVALUATION_VERSION,
        "metadata": {
            "generated_at": evaluated_dates[-1] if evaluated_dates else None,
            "interval": interval,
            "horizons": list(horizons),
            "artifact_count": len(artifacts),
            "evaluated_dates": evaluated_dates,
            "benchmark": (
                "cross-sectional median forward return of the evaluated"
                " (ungated) qualitative entries per date"
            ),
        },
        "metrics": metrics,
    }


def validate_evaluation(data: dict[str, Any]) -> list[str]:
    """Return schema errors for an evaluation artifact (empty when valid)."""
    errors = [
        f"missing required key: {key!r}" for key in _REQUIRED_TOP if key not in data
    ]
    if errors:
        return errors
    if data["version"] != EVALUATION_VERSION:
        errors.append(
            f"unsupported version {data['version']!r} (expected {EVALUATION_VERSION!r})"
        )
    if not isinstance(data["metadata"], dict):
        errors.append("'metadata' must be a JSON object")
    if not isinstance(data["metrics"], dict):
        errors.append("'metrics' must be a JSON object")
    return errors


def check_links(evidence_dir: Path, sample: int = DEFAULT_LINK_SAMPLE) -> list[str]:
    """HEAD-check a deterministic sample of cited URLs in the latest bundle.

    Returns warning strings for unreachable URLs; link rot is reported, never
    fatal.
    """
    bundles = sorted(evidence_dir.glob("*.json"))
    if not bundles:
        return ["no evidence bundles found"]
    with bundles[-1].open(encoding="utf-8") as fh:
        data = json.load(fh)
    urls = sorted({
        str(item["url"])
        for item in data.get("items", [])
        if isinstance(item, dict) and item.get("url")
    })[:sample]
    warnings: list[str] = []
    for url in urls:
        req = urllib.request.Request(url, method="HEAD")
        try:
            with urllib.request.urlopen(req, timeout=_TIMEOUT):
                pass
        except Exception as exc:  # noqa: BLE001 - any failure is just link rot
            warnings.append(f"unreachable evidence URL {url}: {exc}")
    return warnings


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    evaluate = sub.add_parser(
        "evaluate", help="Evaluate stances against realized forward returns"
    )
    evaluate.add_argument(
        "--qualitative-dir", type=Path, default=Path("data/qualitative")
    )
    evaluate.add_argument("--prices-dir", type=Path, default=Path("data/prices"))
    evaluate.add_argument("--interval", default="d", choices=("d",))
    evaluate.add_argument(
        "--horizons",
        default=",".join(str(h) for h in DEFAULT_HORIZONS),
        help="Comma-separated forward horizons in bars",
    )
    evaluate.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)

    links = sub.add_parser(
        "check-links", help="Warn about unreachable cited URLs (link rot)"
    )
    links.add_argument("--evidence-dir", type=Path, default=Path("data/evidence"))
    links.add_argument("--sample", type=int, default=DEFAULT_LINK_SAMPLE)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.command == "check-links":
        warnings = check_links(args.evidence_dir, args.sample)
        for warning in warnings:
            print(f"WARNING: {warning}")
        if not warnings:
            print("all sampled evidence URLs reachable")
        return 0
    try:
        horizons = tuple(int(h) for h in str(args.horizons).split(","))
    except ValueError:
        print(f"ERROR: invalid horizons: {args.horizons}")
        return 1
    if not horizons or any(h < 1 for h in horizons):
        print(f"ERROR: horizons must be positive integers: {args.horizons}")
        return 1
    artifacts: list[dict[str, Any]] = []
    for path in sorted(args.qualitative_dir.glob("*.json")):
        with path.open(encoding="utf-8") as fh:
            artifacts.append(json.load(fh))
    if not artifacts:
        print(f"ERROR: no qualitative artifacts in {args.qualitative_dir}")
        return 1
    result = evaluate_stances(
        artifacts,
        prices_dir=args.prices_dir,
        interval=args.interval,
        horizons=horizons,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Evaluation written to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
