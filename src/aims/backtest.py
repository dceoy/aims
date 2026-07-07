"""Run deterministic walk-forward tests against saved daily OHLCV data."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from dataclasses import fields
from pathlib import Path
from typing import Any, Final

from aims.market_analysis import (
    SCORING_VERSION,
    InstrumentFeatures,
    OhlcvBar,
    load_ohlcv,
    score_instruments,
)

DEFAULT_HORIZONS: Final[tuple[int, ...]] = (1, 5, 20, 60)
BACKTEST_VERSION: Final[str] = "1.1.0"

_FEATURES: Final[tuple[str, ...]] = tuple(f.name for f in fields(InstrumentFeatures))


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
        date_observed = False
        top_k_observed = False
        for horizon in horizons:
            horizon_returns = []
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
                for feat in _FEATURES:
                    value = getattr(score.features, feat)
                    if value is not None:
                        horizon_feature_pairs[feat].append((value, forward))
                if score in selected:
                    top_returns[horizon].append(forward)
                    top_hits[horizon].append(forward > 0)
                    horizon_returns.append(forward)
            for feat, pairs in horizon_feature_pairs.items():
                if len(pairs) < 2:
                    continue
                rho = _spearman([p[0] for p in pairs], [p[1] for p in pairs])
                if rho is not None:
                    feature_ic[horizon][feat].append(rho)
            if horizon == 1 and horizon_returns:
                daily_top_returns.append(sum(horizon_returns) / len(horizon_returns))
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
