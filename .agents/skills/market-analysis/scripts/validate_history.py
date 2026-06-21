#!/usr/bin/env python3
"""Validate an AIMS score-history artifact."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from generate_history import HISTORY_VERSION


def _is_number(value: object) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _validate_row(row: object, index: int) -> list[str]:
    prefix = f"instruments[{index}]"
    if not isinstance(row, dict):
        return [f"{prefix} must be an object"]
    errors: list[str] = []
    required = {
        "symbol",
        "current_rank",
        "previous_rank",
        "rank_delta",
        "current_score",
        "previous_score",
        "score_delta",
        "is_reliable",
        "new_top_k",
        "consecutive_reliable_reports",
        "consecutive_top_k_reports",
        "risk_gates_added",
        "risk_gates_removed",
    }
    missing = sorted(required - row.keys())
    if missing:
        errors.append(f"{prefix} missing keys: {', '.join(missing)}")
    if not isinstance(row.get("symbol"), str):
        errors.append(f"{prefix}.symbol must be a string")
    current_rank = row.get("current_rank")
    if (
        not isinstance(current_rank, int)
        or isinstance(current_rank, bool)
        or current_rank < 1
    ):
        errors.append(f"{prefix}.current_rank must be a positive integer")
    for field in ("consecutive_reliable_reports", "consecutive_top_k_reports"):
        value = row.get(field)
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            errors.append(f"{prefix}.{field} must be a non-negative integer")
    for field in ("previous_rank", "rank_delta"):
        value = row.get(field)
        if value is not None and (
            not isinstance(value, int) or isinstance(value, bool)
        ):
            errors.append(f"{prefix}.{field} must be an integer or null")
    for field in ("current_score", "previous_score", "score_delta"):
        value = row.get(field)
        if field == "current_score" and not _is_number(value):
            errors.append(f"{prefix}.{field} must be a number")
        elif field != "current_score" and value is not None and not _is_number(value):
            errors.append(f"{prefix}.{field} must be a number or null")
    errors.extend(
        f"{prefix}.{field} must be a boolean"
        for field in ("is_reliable", "new_top_k")
        if not isinstance(row.get(field), bool)
    )
    for field in ("risk_gates_added", "risk_gates_removed"):
        value = row.get(field)
        if not isinstance(value, list) or not all(
            isinstance(item, str) for item in value
        ):
            errors.append(f"{prefix}.{field} must be an array of strings")
    return errors


def validate(history: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = {
        "version",
        "analysis_date",
        "previous_analysis_date",
        "top_k",
        "instruments",
        "dropped_from_top_k",
    }
    missing = sorted(required - history.keys())
    if missing:
        errors.append(f"missing keys: {', '.join(missing)}")
    if history.get("version") != HISTORY_VERSION:
        errors.append(f"version must be {HISTORY_VERSION}")
    if not isinstance(history.get("analysis_date"), str):
        errors.append("analysis_date must be a string")
    previous = history.get("previous_analysis_date")
    if previous is not None and not isinstance(previous, str):
        errors.append("previous_analysis_date must be a string or null")
    top_k = history.get("top_k")
    if not isinstance(top_k, int) or isinstance(top_k, bool) or top_k < 1:
        errors.append("top_k must be a positive integer")
    instruments = history.get("instruments")
    if not isinstance(instruments, list):
        errors.append("instruments must be an array")
    else:
        for index, row in enumerate(instruments):
            errors.extend(_validate_row(row, index))
    dropped = history.get("dropped_from_top_k")
    if not isinstance(dropped, list) or not all(
        isinstance(symbol, str) for symbol in dropped
    ):
        errors.append("dropped_from_top_k must be an array")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        with args.input.open(encoding="utf-8") as stream:
            history: dict[str, Any] = json.load(stream)
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1
    errors = validate(history)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"validated {args.input}: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
