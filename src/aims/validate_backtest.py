"""Validate an AIMS walk-forward backtest artifact."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Final

from aims.backtest import BACKTEST_VERSION

_REQUIRED_TOP: Final[tuple[str, ...]] = (
    "schema_version",
    "scoring_version",
    "config",
    "observations",
    "date_range",
    "metrics",
    "turnover",
    "max_drawdown",
    "feature_diagnostics",
    "significance",
    "regime_breakdown",
)
_REQUIRED_CONFIG: Final[tuple[str, ...]] = (
    "symbols",
    "interval",
    "forward_horizons",
    "top_k",
    "buckets",
    "min_history",
)


def _is_number(value: object) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _validate_metrics(metrics: object) -> list[str]:
    if not isinstance(metrics, dict):
        return ["metrics must be an object"]
    errors: list[str] = []
    for horizon_key, horizon_metrics in metrics.items():
        prefix = f"metrics[{horizon_key!r}]"
        if not isinstance(horizon_metrics, dict):
            errors.append(f"{prefix} must be an object")
            continue
        buckets = horizon_metrics.get("score_buckets")
        if not isinstance(buckets, dict):
            errors.append(f"{prefix}.score_buckets must be an object")
        else:
            for bucket_key, bucket in buckets.items():
                bucket_prefix = f"{prefix}.score_buckets[{bucket_key!r}]"
                if not isinstance(bucket, dict):
                    errors.append(f"{bucket_prefix} must be an object")
                    continue
                if not isinstance(bucket.get("count"), int) or isinstance(
                    bucket.get("count"), bool
                ):
                    errors.append(f"{bucket_prefix}.count must be an integer")
                avg = bucket.get("average_return")
                if avg is not None and not _is_number(avg):
                    errors.append(
                        f"{bucket_prefix}.average_return must be a number or null"
                    )
        benchmark = horizon_metrics.get("benchmark")
        if not isinstance(benchmark, dict):
            errors.append(f"{prefix}.benchmark must be an object")
        else:
            if not isinstance(benchmark.get("count"), int) or isinstance(
                benchmark.get("count"), bool
            ):
                errors.append(f"{prefix}.benchmark.count must be an integer")
            avg = benchmark.get("average_return")
            if avg is not None and not _is_number(avg):
                errors.append(
                    f"{prefix}.benchmark.average_return must be a number or null"
                )
        top_k = horizon_metrics.get("top_k")
        if not isinstance(top_k, dict):
            errors.append(f"{prefix}.top_k must be an object")
        else:
            if not isinstance(top_k.get("count"), int) or isinstance(
                top_k.get("count"), bool
            ):
                errors.append(f"{prefix}.top_k.count must be an integer")
            for field in (
                "average_return",
                "net_average_return",
                "hit_rate",
                "excess_return",
                "net_excess_return",
            ):
                value = top_k.get(field)
                if value is not None and not _is_number(value):
                    errors.append(f"{prefix}.top_k.{field} must be a number or null")
    return errors


def _validate_significance(significance: object) -> list[str]:
    if not isinstance(significance, dict):
        return ["significance must be an object"]
    errors: list[str] = []
    for field in ("horizon", "iterations", "block_size", "seed", "n"):
        value = significance.get(field)
        if not isinstance(value, int) or isinstance(value, bool):
            errors.append(f"significance.{field} must be an integer")
    mean = significance.get("mean_net_excess_return")
    if mean is not None and not _is_number(mean):
        errors.append("significance.mean_net_excess_return must be a number or null")
    confidence = significance.get("confidence")
    if not _is_number(confidence):
        errors.append("significance.confidence must be a number")
    ci = significance.get("confidence_interval")
    if ci is not None:
        if not isinstance(ci, dict) or not {"low", "high"} <= ci.keys():
            errors.append(
                "significance.confidence_interval must be an object with"
                " 'low' and 'high', or null"
            )
        else:
            errors.extend(
                f"significance.confidence_interval.{bound} must be a number"
                for bound in ("low", "high")
                if not _is_number(ci.get(bound))
            )
    return errors


def _validate_regime_breakdown(regime_breakdown: object) -> list[str]:
    if not isinstance(regime_breakdown, dict):
        return ["regime_breakdown must be an object"]
    errors: list[str] = []
    horizon = regime_breakdown.get("horizon")
    if not isinstance(horizon, int) or isinstance(horizon, bool):
        errors.append("regime_breakdown.horizon must be an integer")
    regimes = regime_breakdown.get("regimes")
    if not isinstance(regimes, dict):
        errors.append("regime_breakdown.regimes must be an object")
    else:
        for label, stats in regimes.items():
            prefix = f"regime_breakdown.regimes[{label!r}]"
            if not isinstance(stats, dict):
                errors.append(f"{prefix} must be an object")
                continue
            if not isinstance(stats.get("count"), int) or isinstance(
                stats.get("count"), bool
            ):
                errors.append(f"{prefix}.count must be an integer")
            for field in (
                "top_k_net_average_return",
                "benchmark_average_return",
                "excess_return",
            ):
                value = stats.get(field)
                if value is not None and not _is_number(value):
                    errors.append(f"{prefix}.{field} must be a number or null")
    return errors


def _validate_feature_diagnostics(diagnostics: object) -> list[str]:
    if not isinstance(diagnostics, dict):
        return ["feature_diagnostics must be an object"]
    errors: list[str] = []
    features = diagnostics.get("features")
    if not isinstance(features, list) or not all(
        isinstance(item, str) for item in features
    ):
        errors.append("feature_diagnostics.features must be an array of strings")
        features = []

    ic = diagnostics.get("information_coefficient")
    if not isinstance(ic, dict):
        errors.append("feature_diagnostics.information_coefficient must be an object")
    else:
        for horizon_key, per_feature in ic.items():
            prefix = f"feature_diagnostics.information_coefficient[{horizon_key!r}]"
            if not isinstance(per_feature, dict):
                errors.append(f"{prefix} must be an object")
                continue
            for feat, stats in per_feature.items():
                stat_prefix = f"{prefix}[{feat!r}]"
                if not isinstance(stats, dict):
                    errors.append(f"{stat_prefix} must be an object")
                    continue
                mean = stats.get("mean")
                if mean is not None and not _is_number(mean):
                    errors.append(f"{stat_prefix}.mean must be a number or null")
                if not isinstance(stats.get("n"), int) or isinstance(
                    stats.get("n"), bool
                ):
                    errors.append(f"{stat_prefix}.n must be an integer")

    correlation = diagnostics.get("feature_correlation")
    if not isinstance(correlation, dict):
        errors.append("feature_diagnostics.feature_correlation must be an object")
    else:
        for feat_a, row in correlation.items():
            prefix = f"feature_diagnostics.feature_correlation[{feat_a!r}]"
            if not isinstance(row, dict):
                errors.append(f"{prefix} must be an object")
                continue
            for feat_b, value in row.items():
                if value is not None and not _is_number(value):
                    errors.append(f"{prefix}[{feat_b!r}] must be a number or null")
    return errors


def validate_artifact(data: dict[str, Any]) -> list[str]:
    errors = [
        f"missing required key: {key!r}" for key in _REQUIRED_TOP if key not in data
    ]
    if errors:
        return errors

    if data["schema_version"] != BACKTEST_VERSION:
        errors.append(
            f"unsupported schema_version {data['schema_version']!r}"
            f" (expected {BACKTEST_VERSION!r})"
        )

    config = data["config"]
    if not isinstance(config, dict):
        errors.append("config must be an object")
    else:
        errors.extend(
            f"config missing required key: {key!r}"
            for key in _REQUIRED_CONFIG
            if key not in config
        )

    date_range = data["date_range"]
    if not isinstance(date_range, dict) or not {"start", "end"} <= date_range.keys():
        errors.append("date_range must be an object with 'start' and 'end'")
    else:
        for field in ("start", "end"):
            value = date_range.get(field)
            if value is not None and not isinstance(value, str):
                errors.append(f"date_range.{field} must be a string or null")

    if not isinstance(data["observations"], int) or isinstance(
        data["observations"], bool
    ):
        errors.append("observations must be an integer")

    for field in ("turnover", "max_drawdown"):
        value = data[field]
        if value is not None and not _is_number(value):
            errors.append(f"{field} must be a number or null")

    errors.extend(_validate_metrics(data["metrics"]))
    errors.extend(_validate_feature_diagnostics(data["feature_diagnostics"]))
    errors.extend(_validate_significance(data["significance"]))
    errors.extend(_validate_regime_breakdown(data["regime_breakdown"]))
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        with args.input.open(encoding="utf-8") as stream:
            data: dict[str, Any] = json.load(stream)
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1
    errors = validate_artifact(data)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"validated {args.input}: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
