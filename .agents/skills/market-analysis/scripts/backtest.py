#!/usr/bin/env python3
"""Run deterministic walk-forward tests against saved daily OHLCV data."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Final

from market_analysis import SCORING_VERSION, OhlcvBar, load_ohlcv, score_instruments

DEFAULT_HORIZONS: Final[tuple[int, ...]] = (1, 5, 20, 60)


def _mean(values: list[float]) -> float | None:
    return sum(values) / len(values) if values else None


def _drawdown(returns: list[float]) -> float | None:
    if not returns:
        return None
    wealth = peak = 1.0
    maximum = 0.0
    for value in returns:
        wealth *= 1.0 + value
        peak = max(peak, wealth)
        maximum = max(maximum, 1.0 - wealth / peak)
    return maximum


def run_backtest(
    data: dict[str, list[OhlcvBar]],
    *,
    horizons: tuple[int, ...] = DEFAULT_HORIZONS,
    top_k: int = 3,
    buckets: int = 4,
    min_history: int = 60,
) -> dict[str, Any]:
    """Score each available date without look-ahead and aggregate forward returns."""
    if top_k < 1 or buckets < 1 or min_history < 1 or not horizons:
        msg = "top-k, buckets, min-history, and horizons must be positive"
        raise ValueError(msg)
    dates = sorted({bar.timestamp for bars in data.values() for bar in bars})
    positions = {
        symbol: {bar.timestamp: i for i, bar in enumerate(bars)}
        for symbol, bars in data.items()
    }
    bucket_returns: dict[int, dict[int, list[float]]] = defaultdict(
        lambda: defaultdict(list)
    )
    top_returns: dict[int, list[float]] = defaultdict(list)
    top_hits: dict[int, list[bool]] = defaultdict(list)
    daily_top_returns: list[float] = []
    turnovers: list[float] = []
    previous: set[str] | None = None
    observations = 0

    for date in dates:
        window = {
            symbol: bars[: positions[symbol][date] + 1]
            for symbol, bars in data.items()
            if date in positions[symbol] and positions[symbol][date] + 1 >= min_history
        }
        if not window:
            continue
        scores = [
            s
            for s in score_instruments(
                window, reference_time=date, min_history=min_history
            )
            if s.is_reliable
        ]
        if not scores:
            continue
        selected = scores[:top_k]
        selected_symbols = {s.symbol for s in selected}
        if previous is not None:
            turnovers.append(
                1.0
                - len(previous & selected_symbols)
                / max(len(previous), len(selected_symbols))
            )
        previous = selected_symbols
        date_observed = False
        for horizon in horizons:
            eligible = [
                score
                for score in scores
                if positions[score.symbol][date] + horizon < len(data[score.symbol])
            ]
            if not eligible:
                continue
            date_observed = True
            horizon_selected = eligible[:top_k]
            horizon_returns = []
            for rank_index, score in enumerate(eligible):
                bucket = min(buckets, rank_index * buckets // len(eligible) + 1)
                index = positions[score.symbol][date]
                close = data[score.symbol][index].close
                forward = data[score.symbol][index + horizon].close / close - 1.0
                bucket_returns[horizon][bucket].append(forward)
                if score in horizon_selected:
                    top_returns[horizon].append(forward)
                    top_hits[horizon].append(forward > 0)
                    horizon_returns.append(forward)
            if horizon == 1:
                daily_top_returns.append(sum(horizon_returns) / len(horizon_returns))
        observations += date_observed

    metrics = {}
    for horizon in horizons:
        metrics[f"{horizon}d"] = {
            "score_buckets": {
                str(bucket): {
                    "count": len(values),
                    "average_return": _mean(values),
                }
                for bucket, values in sorted(bucket_returns[horizon].items())
            },
            "top_k": {
                "count": len(top_returns[horizon]),
                "average_return": _mean(top_returns[horizon]),
                "hit_rate": _mean([float(hit) for hit in top_hits[horizon]]),
            },
        }
    return {
        "observations": observations,
        "metrics": metrics,
        "turnover": _mean(turnovers),
        "max_drawdown": _drawdown(daily_top_returns),
    }


def _parse_positive_csv(value: str) -> tuple[int, ...]:
    values = tuple(int(item) for item in value.split(","))
    if not values or any(item < 1 for item in values):
        msg = "horizons must be comma-separated positive integers"
        raise argparse.ArgumentTypeError(msg)
    return values


def main(argv: list[str] | None = None) -> int:
    """Load saved prices, run the backtest, and write one JSON artifact."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--symbols", required=True, help="Comma-separated symbols")
    parser.add_argument("--data-dir", type=Path, default=Path("data/prices"))
    parser.add_argument("--output-dir", type=Path, default=Path("data/backtests"))
    parser.add_argument("--interval", default="d", choices=("d",))
    parser.add_argument(
        "--horizons", type=_parse_positive_csv, default=DEFAULT_HORIZONS
    )
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--buckets", type=int, default=4)
    parser.add_argument("--min-history", type=int, default=60)
    args = parser.parse_args(argv)
    symbols = tuple(item.strip() for item in args.symbols.split(",") if item.strip())
    if not symbols:
        parser.error("at least one symbol is required")
    try:
        data = {
            symbol: load_ohlcv(symbol, args.interval, args.data_dir)
            for symbol in symbols
        }
        result = run_backtest(
            data,
            horizons=args.horizons,
            top_k=args.top_k,
            buckets=args.buckets,
            min_history=args.min_history,
        )
    except (FileNotFoundError, ValueError) as exc:
        parser.error(str(exc))
    start = max(bars[0].timestamp for bars in data.values()).date().isoformat()
    end = min(bars[-1].timestamp for bars in data.values()).date().isoformat()
    artifact = {
        "schema_version": "1.0.0",
        "scoring_version": SCORING_VERSION,
        "generated_at": datetime.now(UTC).isoformat(),
        "date_range": {"start": start, "end": end},
        "config": {
            "symbols": list(symbols),
            "interval": args.interval,
            "forward_horizons": list(args.horizons),
            "top_k": args.top_k,
            "buckets": args.buckets,
            "min_history": args.min_history,
        },
        **result,
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    path = args.output_dir / f"{start}_{end}_{args.interval}.json"
    path.write_text(json.dumps(artifact, indent=2, sort_keys=True) + "\n")
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
