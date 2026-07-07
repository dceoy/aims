"""Run deterministic walk-forward tests against saved daily OHLCV data."""

from __future__ import annotations

import argparse
import csv
import json
import random
from collections import defaultdict
from dataclasses import dataclass, fields
from pathlib import Path
from typing import Any, Final

from aims.market_analysis import (
    SCORING_VERSION,
    InstrumentFeatures,
    OhlcvBar,
    load_ohlcv,
    market_regime_metadata,
    score_instruments,
)

DEFAULT_HORIZONS: Final[tuple[int, ...]] = (1, 5, 20, 60)
BACKTEST_VERSION: Final[str] = "1.2.0"

_FEATURES: Final[tuple[str, ...]] = tuple(f.name for f in fields(InstrumentFeatures))

# Conservative placeholders used for any symbol absent from a cost mapping;
# real per-instrument costs should come from broker spread/financing data
# once available (data/cfd_instruments.csv already records 金利調整 flags).
DEFAULT_SPREAD_BPS: Final[float] = 10.0
DEFAULT_FINANCING_RATE_ANNUAL: Final[float] = 0.05


@dataclass(frozen=True)
class InstrumentCost:
    """Per-instrument trading cost inputs for net-of-cost backtest metrics."""

    spread_bps: float
    financing_rate_annual: float


DEFAULT_COST: Final[InstrumentCost] = InstrumentCost(
    DEFAULT_SPREAD_BPS, DEFAULT_FINANCING_RATE_ANNUAL
)


def load_instrument_costs(path: Path) -> dict[str, InstrumentCost]:
    """Load optional per-symbol cost overrides from a small CSV table.

    Columns: symbol, spread_bps, financing_rate_annual. Symbols absent from
    the table fall back to DEFAULT_COST in run_backtest.
    """
    costs: dict[str, InstrumentCost] = {}
    with path.open(encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            costs[row["symbol"]] = InstrumentCost(
                spread_bps=float(row["spread_bps"]),
                financing_rate_annual=float(row["financing_rate_annual"]),
            )
    return costs


def _round_trip_cost(cost: InstrumentCost, horizon: int) -> float:
    """Round-trip spread plus *horizon*-day holding financing, as a return fraction.

    Each forward-return observation is treated as an independent entry and
    exit (this backtest reports cross-sectional forward returns per date,
    not a single compounding equity curve), so the cost applies once per
    observation rather than accumulating with daily rebalance turnover.
    """
    return 2.0 * (cost.spread_bps / 10_000.0) + cost.financing_rate_annual * (
        horizon / 365.0
    )


def _moving_block_bootstrap_ci(
    values: list[float],
    *,
    block_size: int,
    iterations: int,
    seed: int,
    confidence: float = 0.95,
) -> dict[str, float] | None:
    """Deterministic moving-block bootstrap confidence interval on the mean.

    Resampling contiguous blocks (rather than i.i.d. points) preserves
    short-range autocorrelation in the daily excess-return series.
    """
    n = len(values)
    if n < 2:
        return None
    block_size = max(1, min(block_size, n))
    n_blocks = -(-n // block_size)  # ceil division
    rng = random.Random(seed)  # noqa: S311 - statistical resampling, not cryptographic
    means: list[float] = []
    for _ in range(iterations):
        sample: list[float] = []
        for _ in range(n_blocks):
            start = rng.randrange(0, n - block_size + 1)
            sample.extend(values[start : start + block_size])
        means.append(sum(sample[:n]) / n)
    means.sort()
    tail = (1.0 - confidence) / 2.0
    low_index = int(tail * iterations)
    high_index = min(iterations - 1, int((1.0 - tail) * iterations))
    return {"low": means[low_index], "high": means[high_index]}


def _mean(values: list[float]) -> float | None:
    return sum(values) / len(values) if values else None


def _ranks(values: list[float]) -> list[float]:
    """Return 1-indexed ranks, averaging ties."""
    order = sorted(range(len(values)), key=lambda i: values[i])
    ranks = [0.0] * len(values)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and values[order[j + 1]] == values[order[i]]:
            j += 1
        avg_rank = (i + j) / 2 + 1
        for k in range(i, j + 1):
            ranks[order[k]] = avg_rank
        i = j + 1
    return ranks


def _spearman(xs: list[float], ys: list[float]) -> float | None:
    """Spearman rank correlation (Pearson on ranks); None if degenerate."""
    n = len(xs)
    if n < 2:
        return None
    rx, ry = _ranks(xs), _ranks(ys)
    mean_rx, mean_ry = sum(rx) / n, sum(ry) / n
    cov = sum((a - mean_rx) * (b - mean_ry) for a, b in zip(rx, ry, strict=True)) / n
    var_x = sum((a - mean_rx) ** 2 for a in rx) / n
    var_y = sum((b - mean_ry) ** 2 for b in ry) / n
    if var_x == 0 or var_y == 0:
        return None
    return cov / (var_x * var_y) ** 0.5


def _corr_key(feat_a: str, feat_b: str) -> tuple[str, str]:
    ia, ib = _FEATURES.index(feat_a), _FEATURES.index(feat_b)
    return (feat_a, feat_b) if ia < ib else (feat_b, feat_a)


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
    costs: dict[str, InstrumentCost] | None = None,
    bootstrap_iterations: int = 1000,
    bootstrap_block_size: int = 5,
    bootstrap_seed: int = 0,
) -> dict[str, Any]:
    """Score each available date without look-ahead and aggregate forward returns."""
    if (
        top_k < 1
        or buckets < 1
        or min_history < 1
        or not horizons
        or any(horizon < 1 for horizon in horizons)
    ):
        msg = "top-k, buckets, min-history, and horizons must be positive"
        raise ValueError(msg)
    if len(horizons) != len(set(horizons)):
        msg = "forward horizons must be unique"
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
    top_net_returns: dict[int, list[float]] = defaultdict(list)
    top_hits: dict[int, list[bool]] = defaultdict(list)
    daily_top_returns: list[float] = []
    turnovers: list[float] = []
    previous: set[str] | None = None
    observations = 0
    observed_dates: list[str] = []
    feature_ic: dict[int, dict[str, list[float]]] = defaultdict(
        lambda: defaultdict(list)
    )
    feature_corr: dict[tuple[str, str], list[float]] = defaultdict(list)

    # Primary horizon for the significance test and regime breakdown: the
    # finest-grained horizon gives the most daily observations to resample.
    primary_horizon = min(horizons)
    daily_net_excess: list[float] = []
    regime_labels: list[str] = []
    regime_top_net: dict[str, list[float]] = defaultdict(list)
    regime_benchmark: dict[str, list[float]] = defaultdict(list)

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
        for i, feat_a in enumerate(_FEATURES):
            for feat_b in _FEATURES[i + 1 :]:
                pairs = [
                    (getattr(s.features, feat_a), getattr(s.features, feat_b))
                    for s in scores
                ]
                valid = [(a, b) for a, b in pairs if a is not None and b is not None]
                if len(valid) < 2:
                    continue
                rho = _spearman([a for a, _ in valid], [b for _, b in valid])
                if rho is not None:
                    feature_corr[feat_a, feat_b].append(rho)
        selected = scores[:top_k]
        selected_symbols = {s.symbol for s in selected}
        regime_label = market_regime_metadata(scores)["label"]
        date_observed = False
        top_k_observed = False
        for horizon in horizons:
            horizon_returns = []
            horizon_net_returns = []
            horizon_universe_returns: list[float] = []
            horizon_feature_pairs: dict[str, list[tuple[float, float]]] = defaultdict(
                list
            )
            for rank_index, score in enumerate(scores):
                index = positions[score.symbol][date]
                if index + horizon >= len(data[score.symbol]):
                    continue
                date_observed = True
                bucket = min(buckets, rank_index * buckets // len(scores) + 1)
                close = data[score.symbol][index].close
                forward = data[score.symbol][index + horizon].close / close - 1.0
                bucket_returns[horizon][bucket].append(forward)
                horizon_universe_returns.append(forward)
                for feat in _FEATURES:
                    value = getattr(score.features, feat)
                    if value is not None:
                        horizon_feature_pairs[feat].append((value, forward))
                if score in selected:
                    cost = (costs or {}).get(score.symbol, DEFAULT_COST)
                    net_forward = forward - _round_trip_cost(cost, horizon)
                    top_returns[horizon].append(forward)
                    top_net_returns[horizon].append(net_forward)
                    top_hits[horizon].append(forward > 0)
                    horizon_returns.append(forward)
                    horizon_net_returns.append(net_forward)
            for feat, pairs in horizon_feature_pairs.items():
                if len(pairs) < 2:
                    continue
                rho = _spearman([p[0] for p in pairs], [p[1] for p in pairs])
                if rho is not None:
                    feature_ic[horizon][feat].append(rho)
            if horizon == 1 and horizon_returns:
                daily_top_returns.append(sum(horizon_returns) / len(horizon_returns))
            if (
                horizon == primary_horizon
                and horizon_net_returns
                and horizon_universe_returns
            ):
                net_avg = sum(horizon_net_returns) / len(horizon_net_returns)
                benchmark_avg = sum(horizon_universe_returns) / len(
                    horizon_universe_returns
                )
                daily_net_excess.append(net_avg - benchmark_avg)
                regime_labels.append(regime_label)
                regime_top_net[regime_label].append(net_avg)
                regime_benchmark[regime_label].append(benchmark_avg)
            top_k_observed = top_k_observed or bool(horizon_returns)
        if date_observed:
            observations += 1
            observed_dates.append(date.date().isoformat())
        if top_k_observed:
            if previous is not None:
                turnovers.append(
                    1.0
                    - len(previous & selected_symbols)
                    / max(len(previous), len(selected_symbols))
                )
            previous = selected_symbols

    metrics = {}
    for horizon in horizons:
        universe_returns = [
            value for values in bucket_returns[horizon].values() for value in values
        ]
        benchmark_avg = _mean(universe_returns)
        top_k_avg = _mean(top_returns[horizon])
        top_k_net_avg = _mean(top_net_returns[horizon])
        metrics[f"{horizon}d"] = {
            "score_buckets": {
                str(bucket): {
                    "count": len(values),
                    "average_return": _mean(values),
                }
                for bucket, values in sorted(bucket_returns[horizon].items())
            },
            "benchmark": {
                "count": len(universe_returns),
                "average_return": benchmark_avg,
            },
            "top_k": {
                "count": len(top_returns[horizon]),
                "average_return": top_k_avg,
                "net_average_return": top_k_net_avg,
                "hit_rate": _mean([float(hit) for hit in top_hits[horizon]]),
                "excess_return": (
                    None
                    if top_k_avg is None or benchmark_avg is None
                    else top_k_avg - benchmark_avg
                ),
                "net_excess_return": (
                    None
                    if top_k_net_avg is None or benchmark_avg is None
                    else top_k_net_avg - benchmark_avg
                ),
            },
        }
    feature_diagnostics = {
        "features": list(_FEATURES),
        "information_coefficient": {
            f"{horizon}d": {
                feat: {
                    "mean": _mean(feature_ic[horizon][feat]),
                    "n": len(feature_ic[horizon][feat]),
                }
                for feat in _FEATURES
            }
            for horizon in horizons
        },
        "feature_correlation": {
            feat_a: {
                feat_b: (
                    1.0
                    if feat_a == feat_b
                    else _mean(feature_corr.get(_corr_key(feat_a, feat_b), []))
                )
                for feat_b in _FEATURES
            }
            for feat_a in _FEATURES
        },
    }
    ci = _moving_block_bootstrap_ci(
        daily_net_excess,
        block_size=bootstrap_block_size,
        iterations=bootstrap_iterations,
        seed=bootstrap_seed,
    )
    significance = {
        "horizon": primary_horizon,
        "mean_net_excess_return": _mean(daily_net_excess),
        "confidence": 0.95,
        "confidence_interval": ci,
        "block_size": bootstrap_block_size,
        "iterations": bootstrap_iterations,
        "seed": bootstrap_seed,
        "n": len(daily_net_excess),
    }

    def _regime_stats(label: str) -> dict[str, Any]:
        net_avg = _mean(regime_top_net[label])
        benchmark_avg = _mean(regime_benchmark[label])
        excess = (
            None
            if net_avg is None or benchmark_avg is None
            else net_avg - benchmark_avg
        )
        return {
            "count": len(regime_top_net[label]),
            "top_k_net_average_return": net_avg,
            "benchmark_average_return": benchmark_avg,
            "excess_return": excess,
        }

    regime_breakdown = {
        "horizon": primary_horizon,
        "regimes": {
            label: _regime_stats(label) for label in sorted(set(regime_labels))
        },
    }
    return {
        "observations": observations,
        "date_range": {
            "start": observed_dates[0] if observed_dates else None,
            "end": observed_dates[-1] if observed_dates else None,
        },
        "metrics": metrics,
        "turnover": _mean(turnovers),
        "max_drawdown": _drawdown(daily_top_returns),
        "feature_diagnostics": feature_diagnostics,
        "significance": significance,
        "regime_breakdown": regime_breakdown,
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
    parser.add_argument(
        "--cost-mapping",
        type=Path,
        default=None,
        help=(
            "Optional CSV (symbol, spread_bps, financing_rate_annual) of"
            " per-instrument cost overrides; unlisted symbols use"
            f" conservative defaults ({DEFAULT_SPREAD_BPS} bps,"
            f" {DEFAULT_FINANCING_RATE_ANNUAL:.0%} annual financing)"
        ),
    )
    parser.add_argument("--bootstrap-iterations", type=int, default=1000)
    parser.add_argument("--bootstrap-block-size", type=int, default=5)
    parser.add_argument("--bootstrap-seed", type=int, default=0)
    args = parser.parse_args(argv)
    symbols = tuple(item.strip() for item in args.symbols.split(",") if item.strip())
    if not symbols:
        parser.error("at least one symbol is required")
    try:
        data = {
            symbol: load_ohlcv(symbol, args.interval, args.data_dir)
            for symbol in symbols
        }
        costs = load_instrument_costs(args.cost_mapping) if args.cost_mapping else None
        result = run_backtest(
            data,
            horizons=args.horizons,
            top_k=args.top_k,
            buckets=args.buckets,
            min_history=args.min_history,
            costs=costs,
            bootstrap_iterations=args.bootstrap_iterations,
            bootstrap_block_size=args.bootstrap_block_size,
            bootstrap_seed=args.bootstrap_seed,
        )
    except (FileNotFoundError, ValueError) as exc:
        parser.error(str(exc))
    start = result["date_range"]["start"]
    end = result["date_range"]["end"]
    if start is None or end is None:
        parser.error("no backtest observations for the requested configuration")
    artifact = {
        "schema_version": BACKTEST_VERSION,
        "scoring_version": SCORING_VERSION,
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
