r"""Validate an AIMS stance-evaluation performance artifact.

Hand-rolled validator following the ``validate_analysis.py`` pattern (no
``jsonschema`` dependency). The format reference is
``data/schema/performance.schema.json``; artifacts are produced by
``aims.performance`` under ``data/performance/``.

Usage:
    uv run .agents/skills/qualitative-analysis/scripts/validate_performance.py \
        --input data/performance/2026-07-04.json
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Final

from aims.performance import CONFIDENCES, PERFORMANCE_VERSION, STANCES

_REQUIRED_TOP: Final[tuple[str, ...]] = (
    "version",
    "metadata",
    "stance_evaluation",
    "warnings",
)
_REQUIRED_META: Final[tuple[str, ...]] = (
    "generated_at",
    "analysis_date",
    "interval",
    "git_commit",
    "config",
    "inputs",
    "disclaimer",
)
_REQUIRED_EVALUATION: Final[tuple[str, ...]] = (
    "instruments_evaluated",
    "excluded_gated",
    "unmatched",
    "horizons",
)
_REQUIRED_HORIZON: Final[tuple[str, ...]] = (
    "observations",
    "pending",
    "broken_chain",
    "stances",
    "confidence_calibration",
)
_DATE_RE: Final[re.Pattern[str]] = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def _is_count(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


def _is_rate(value: Any) -> bool:
    if value is None:
        return True
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and 0.0 <= float(value) <= 1.0
    )


def _validate_bucket(where: str, bucket: Any, *, with_average: bool) -> list[str]:
    if not isinstance(bucket, dict):
        return [f"{where} must be a JSON object"]
    errors: list[str] = []
    if not _is_count(bucket.get("count")):
        errors.append(f"{where}.count must be a non-negative integer")
    if not _is_rate(bucket.get("hit_rate")):
        errors.append(f"{where}.hit_rate must be null or a number in [0, 1]")
    if with_average:
        average = bucket.get("average_return")
        if average is not None and (
            not isinstance(average, (int, float)) or isinstance(average, bool)
        ):
            errors.append(f"{where}.average_return must be null or a number")
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
    errors.extend(
        f"{where}.{key} must be a non-negative integer"
        for key in ("observations", "pending", "broken_chain")
        if not _is_count(horizon[key])
    )
    stances = horizon["stances"]
    if not isinstance(stances, dict) or sorted(stances) != sorted(STANCES):
        errors.append(f"{where}.stances must map exactly the stances {list(STANCES)}")
    else:
        for stance in STANCES:
            errors.extend(
                _validate_bucket(
                    f"{where}.stances.{stance}", stances[stance], with_average=True
                )
            )
    calibration = horizon["confidence_calibration"]
    if not isinstance(calibration, dict) or sorted(calibration) != sorted(CONFIDENCES):
        errors.append(
            f"{where}.confidence_calibration must map exactly the confidence"
            f" levels {list(CONFIDENCES)}"
        )
    else:
        for confidence in CONFIDENCES:
            errors.extend(
                _validate_bucket(
                    f"{where}.confidence_calibration.{confidence}",
                    calibration[confidence],
                    with_average=False,
                )
            )
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
        for key in ("analysis_dates", "qualitative_dates"):
            dates = inputs.get(key)
            if not isinstance(dates, list) or any(
                not isinstance(d, str) or not _DATE_RE.match(d) for d in dates
            ):
                errors.append(
                    f"metadata.inputs.{key} must be a list of YYYY-MM-DD dates"
                )
            elif dates != sorted(dates):
                errors.append(f"metadata.inputs.{key} must be sorted")
    elif "inputs" in metadata:
        errors.append("metadata.inputs must be a JSON object")
    date = metadata.get("analysis_date")
    if isinstance(date, str) and not _DATE_RE.match(date):
        errors.append(f"metadata.analysis_date {date!r} is not a YYYY-MM-DD date")
    return errors, horizons


def validate_artifact(data: dict[str, Any]) -> list[str]:
    """Validate shape, enums, and value ranges of a performance artifact."""
    errors = [
        f"missing required key: {key!r}" for key in _REQUIRED_TOP if key not in data
    ]
    if errors:
        return errors
    if data["version"] != PERFORMANCE_VERSION:
        errors.append(
            f"unsupported version {data['version']!r}"
            f" (expected {PERFORMANCE_VERSION!r})"
        )
    meta_errors, horizons = _validate_metadata(data["metadata"])
    errors.extend(meta_errors)

    evaluation = data["stance_evaluation"]
    if not isinstance(evaluation, dict):
        errors.append("'stance_evaluation' must be a JSON object")
    else:
        errors.extend(
            f"stance_evaluation missing required key: {key!r}"
            for key in _REQUIRED_EVALUATION
            if key not in evaluation
        )
        errors.extend(
            f"stance_evaluation.{key} must be a non-negative integer"
            for key in ("instruments_evaluated", "excluded_gated", "unmatched")
            if key in evaluation and not _is_count(evaluation[key])
        )
        horizon_map = evaluation.get("horizons")
        if not isinstance(horizon_map, dict):
            if "horizons" in evaluation:
                errors.append("stance_evaluation.horizons must be a JSON object")
        else:
            if horizons and sorted(horizon_map) != sorted(f"{h}d" for h in horizons):
                errors.append(
                    "stance_evaluation.horizons keys do not match"
                    " metadata.config.horizons"
                )
            for name in sorted(horizon_map):
                errors.extend(
                    _validate_horizon(
                        f"stance_evaluation.horizons.{name}", horizon_map[name]
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
        help="Path to stance-evaluation performance artifact JSON file",
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
