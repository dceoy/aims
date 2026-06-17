#!/usr/bin/env python3
r"""Validate an AIMS analysis artifact JSON file against the expected schema.

Usage:
    uv run .agents/skills/market-analysis/scripts/validate_analysis.py \
        --input data/analysis/2024-01-01.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Final

ARTIFACT_VERSION: Final[str] = "1.0.0"
DEFAULT_INPUT: Final[Path] = Path("data/analysis")

_REQUIRED_TOP: Final[tuple[str, ...]] = ("version", "metadata", "instruments")
_REQUIRED_META: Final[tuple[str, ...]] = (
    "generated_at",
    "git_commit",
    "data_source",
    "data_freshness",
    "scoring_version",
    "config",
    "coverage",
)
_REQUIRED_CONFIG: Final[tuple[str, ...]] = (
    "interval",
    "stale_days",
    "max_gap_days",
    "min_history",
    "coverage_policy",
)
_REQUIRED_COVERAGE: Final[tuple[str, ...]] = (
    "attempted_count",
    "fetched_count",
    "missing_symbols",
    "success_ratio",
    "passed",
    "violations",
)
_FRESHNESS_SENTINEL: Final[str] = "n/a"
_DATE_LEN: Final[int] = 10
_REQUIRED_INST: Final[tuple[str, ...]] = (
    "symbol",
    "rank",
    "score",
    "is_reliable",
    "risk_gates",
    "explanation",
    "features",
)


def validate_artifact(data: dict[str, Any]) -> list[str]:
    errors = [
        f"missing required key: {key!r}" for key in _REQUIRED_TOP if key not in data
    ]
    if errors:
        return errors

    if data["version"] != ARTIFACT_VERSION:
        errors.append(
            f"unsupported version {data['version']!r} (expected {ARTIFACT_VERSION!r})"
        )

    metadata = data["metadata"]
    if not isinstance(metadata, dict):
        errors.append("'metadata' must be a JSON object")
    else:
        errors.extend(
            f"metadata missing required key: {key!r}"
            for key in _REQUIRED_META
            if key not in metadata
        )
        freshness = metadata.get("data_freshness")
        if freshness is not None:
            if not isinstance(freshness, dict):
                errors.append("metadata.data_freshness must be a JSON object")
            else:
                for sym, val in freshness.items():
                    if not isinstance(val, str):
                        errors.append(
                            f"metadata.data_freshness[{sym!r}] must be a string"
                        )
                    elif val != _FRESHNESS_SENTINEL and (
                        len(val) != _DATE_LEN or val[4] != "-" or val[7] != "-"
                    ):
                        errors.append(
                            f"metadata.data_freshness[{sym!r}]: {val!r} is not"
                            f" a YYYY-MM-DD date or {_FRESHNESS_SENTINEL!r}"
                        )

        config = metadata.get("config")
        if config is None:
            errors.append("metadata.config must not be null")
        elif not isinstance(config, dict):
            errors.append("metadata.config must be a JSON object")
        else:
            errors.extend(
                f"metadata.config missing required key: {key!r}"
                for key in _REQUIRED_CONFIG
                if key not in config
            )
            coverage_policy = config.get("coverage_policy")
            if coverage_policy is not None and not isinstance(coverage_policy, dict):
                errors.append("metadata.config.coverage_policy must be a JSON object")

        coverage = metadata.get("coverage")
        if coverage is None:
            errors.append("metadata.coverage must not be null")
        elif not isinstance(coverage, dict):
            errors.append("metadata.coverage must be a JSON object")
        else:
            errors.extend(
                f"metadata.coverage missing required key: {key!r}"
                for key in _REQUIRED_COVERAGE
                if key not in coverage
            )
            passed = coverage.get("passed")
            if passed is not None and not isinstance(passed, bool):
                errors.append("metadata.coverage.passed must be a boolean")

    instruments = data["instruments"]
    if not isinstance(instruments, list):
        errors.append("'instruments' must be a JSON array")
    else:
        for idx, inst in enumerate(instruments):
            if not isinstance(inst, dict):
                errors.append(f"instrument[{idx}] must be a JSON object")
                continue
            errors.extend(
                f"instrument[{idx}] missing required key: {key!r}"
                for key in _REQUIRED_INST
                if key not in inst
            )
            score = inst.get("score")
            if not isinstance(score, (int, float)):
                errors.append(f"instrument[{idx}]: score must be a number")
            elif not 0.0 <= float(score) <= 100.0:
                errors.append(f"instrument[{idx}]: score {score!r} outside [0, 100]")
            rank = inst.get("rank")
            if not isinstance(rank, int) or isinstance(rank, bool):
                errors.append(f"instrument[{idx}]: rank must be an integer")
            elif rank < 1:
                errors.append(f"instrument[{idx}]: rank {rank} must be >= 1")

    return errors


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help="Path to analysis artifact JSON file",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    try:
        with args.input.open() as fh:
            data = json.load(fh)
    except FileNotFoundError:
        print(f"ERROR: file not found: {args.input}")
        raise SystemExit(1) from None
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON in {args.input}: {exc}")
        raise SystemExit(1) from exc
    errors = validate_artifact(data)
    if errors:
        for error in errors:
            print(error)
        raise SystemExit(1)
    print(f"validated {args.input}: OK")


if __name__ == "__main__":
    main()
