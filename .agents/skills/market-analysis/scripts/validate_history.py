#!/usr/bin/env python3
"""Validate an AIMS score-history artifact."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from generate_history import HISTORY_VERSION


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
    if not isinstance(history.get("instruments"), list):
        errors.append("instruments must be an array")
    if not isinstance(history.get("dropped_from_top_k"), list):
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
