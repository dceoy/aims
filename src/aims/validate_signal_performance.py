r"""Validate an AIMS cumulative signal-performance artifact.

Hand-rolled validator following the ``validate_analysis.py`` pattern (no
``jsonschema`` dependency). The format reference is
``data/schema/signal_performance.schema.json``; the artifact is produced by
``aims.signal_performance`` at ``data/performance/signals.json``.

Usage:
    uv run .agents/skills/market-analysis/scripts/validate_signal_performance.py \
        --input data/performance/signals.json
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Final

from aims.signal_performance import SIGNAL_PERFORMANCE_VERSION

_REQUIRED_TOP: Final[tuple[str, ...]] = (
    "version",
    "metadata",
    "signal_evaluation",
    "warnings",
)
_REQUIRED_META: Final[tuple[str, ...]] = (
    "generated_at",
    "as_of",
    "git_commit",
    "config",
    "inputs",
    "disclaimer",
)
_REQUIRED_EVALUATION: Final[tuple[str, ...]] = ("dates_evaluated", "horizons")
_REQUIRED_HORIZON: Final[tuple[str, ...]] = (
    "count",
    "top5_average_return",
    "benchmark_average_return",
    "excess_return",
    "hit_rate",
    "pending",
    "incomplete",
    "by_asset_class",
    "by_regime",
)
_REQUIRED_BUCKET: Final[tuple[str, ...]] = (
    "count",
    "top5_average_return",
    "benchmark_average_return",
    "excess_return",
    "hit_rate",
)
_DATE_RE: Final[re.Pattern[str]] = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def _is_count(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


def _is_number_or_null(value: Any) -> bool:
    return value is None or (
        isinstance(value, (int, float)) and not isinstance(value, bool)
    )


def _is_rate_or_null(value: Any) -> bool:
    if value is None:
        return True
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and 0.0 <= float(value) <= 1.0
    )


def _validate_bucket(where: str, bucket: Any) -> list[str]:
    if not isinstance(bucket, dict):
        return [f"{where} must be a JSON object"]
    errors = [
        f"{where} missing required key: {key!r}"
        for key in _REQUIRED_BUCKET
        if key not in bucket
    ]
    if errors:
        return errors
    if not _is_count(bucket["count"]):
        errors.append(f"{where}.count must be a non-negative integer")
    errors.extend(
        f"{where}.{key} must be null or a number"
        for key in ("top5_average_return", "benchmark_average_return", "excess_return")
        if not _is_number_or_null(bucket[key])
    )
    if not _is_rate_or_null(bucket["hit_rate"]):
        errors.append(f"{where}.hit_rate must be null or a number in [0, 1]")
    return errors


def _validate_horizon(where: str, horizon: Any) -> list[str]:
    if not isinstance(horizon, dict):
        return [f"{where} must be a JSON object"]
    errors = [
        f"{where} missing required key: {key!r}"
        for key in _REQUIRED_HORIZON
        if key not in horizon
    ]
    if errors:
        return errors
    errors.extend(_validate_bucket(where, horizon))
    errors.extend(
        f"{where}.{key} must be a non-negative integer"
        for key in ("pending", "incomplete")
        if not _is_count(horizon[key])
    )
    for key in ("by_asset_class", "by_regime"):
        buckets = horizon[key]
        if not isinstance(buckets, dict):
            errors.append(f"{where}.{key} must be a JSON object")
            continue
        for label, bucket in buckets.items():
            errors.extend(_validate_bucket(f"{where}.{key}.{label}", bucket))
    return errors


def _validate_metadata(metadata: Any) -> tuple[list[str], list[int]]:
    if not isinstance(metadata, dict):
        return ["'metadata' must be a JSON object"], []
    errors = [
        f"metadata missing required key: {key!r}"
        for key in _REQUIRED_META
        if key not in metadata
    ]
    horizons: list[int] = []
    config = metadata.get("config")
    if isinstance(config, dict):
        top_k = config.get("top_k")
        if not _is_count(top_k) or not isinstance(top_k, int) or top_k < 1:
            errors.append("metadata.config.top_k must be a positive integer")
        raw = config.get("horizons")
        if (
            not isinstance(raw, list)
            or not raw
            or any(not _is_count(h) or h < 1 for h in raw)
            or len(set(raw)) != len(raw)
        ):
            errors.append("metadata.config.horizons must be unique positive integers")
        else:
            horizons = [int(h) for h in raw]
        tolerance = config.get("return_consistency_tolerance")
        if (
            not isinstance(tolerance, (int, float))
            or isinstance(tolerance, bool)
            or tolerance < 0
        ):
            errors.append(
                "metadata.config.return_consistency_tolerance must be a"
                " non-negative number"
            )
    elif "config" in metadata:
        errors.append("metadata.config must be a JSON object")
    inputs = metadata.get("inputs")
    if isinstance(inputs, dict):
        dates = inputs.get("analysis_dates")
        if not isinstance(dates, list) or any(
            not isinstance(d, str) or not _DATE_RE.match(d) for d in dates
        ):
            errors.append(
                "metadata.inputs.analysis_dates must be a list of YYYY-MM-DD dates"
            )
        elif dates != sorted(dates):
            errors.append("metadata.inputs.analysis_dates must be sorted")
    elif "inputs" in metadata:
        errors.append("metadata.inputs must be a JSON object")
    as_of = metadata.get("as_of")
    if isinstance(as_of, str) and not _DATE_RE.match(as_of):
        errors.append(f"metadata.as_of {as_of!r} is not a YYYY-MM-DD date")
    return errors, horizons


def validate_artifact(data: dict[str, Any]) -> list[str]:
    """Validate shape, enums, and value ranges of a signal-performance artifact."""
    errors = [
        f"missing required key: {key!r}" for key in _REQUIRED_TOP if key not in data
    ]
    if errors:
        return errors
    if data["version"] != SIGNAL_PERFORMANCE_VERSION:
        errors.append(
            f"unsupported version {data['version']!r}"
            f" (expected {SIGNAL_PERFORMANCE_VERSION!r})"
        )
    meta_errors, horizons = _validate_metadata(data["metadata"])
    errors.extend(meta_errors)

    evaluation = data["signal_evaluation"]
    if not isinstance(evaluation, dict):
        errors.append("'signal_evaluation' must be a JSON object")
    else:
        errors.extend(
            f"signal_evaluation missing required key: {key!r}"
            for key in _REQUIRED_EVALUATION
            if key not in evaluation
        )
        if "dates_evaluated" in evaluation and not _is_count(
            evaluation["dates_evaluated"]
        ):
            errors.append(
                "signal_evaluation.dates_evaluated must be a non-negative integer"
            )
        horizon_map = evaluation.get("horizons")
        if not isinstance(horizon_map, dict):
            if "horizons" in evaluation:
                errors.append("signal_evaluation.horizons must be a JSON object")
        else:
            if horizons and sorted(horizon_map) != sorted(f"{h}d" for h in horizons):
                errors.append(
                    "signal_evaluation.horizons keys do not match"
                    " metadata.config.horizons"
                )
            for name in sorted(horizon_map):
                errors.extend(
                    _validate_horizon(
                        f"signal_evaluation.horizons.{name}", horizon_map[name]
                    )
                )

    warnings = data["warnings"]
    if not isinstance(warnings, list) or any(not isinstance(w, str) for w in warnings):
        errors.append("'warnings' must be a list of strings")
    return errors


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help="Path to signal-performance artifact JSON file",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        with args.input.open(encoding="utf-8") as stream:
            data: dict[str, Any] = json.load(stream)
    except FileNotFoundError as exc:
        print(f"ERROR: file not found: {exc.filename}")
        return 1
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON: {exc}")
        return 1
    errors = validate_artifact(data)
    if errors:
        for error in errors:
            print(error)
        return 1
    print(f"validated {args.input}: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
