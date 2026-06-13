#!/usr/bin/env python3
"""Validate data/cfd_instruments.csv against its JSON schema."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from typing import Any

DEFAULT_INPUT = Path("data/cfd_instruments.csv")
DEFAULT_SCHEMA = Path("data/schema/cfd_instruments.schema.json")


def load_schema(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)  # type: ignore[no-any-return]


def validate_csv(csv_path: Path, schema_path: Path) -> list[str]:
    schema = load_schema(schema_path)
    errors: list[str] = []

    required_columns: list[str] = schema["columns"]
    required_non_empty: set[str] = set(schema["required_non_empty"])
    uniqueness_key: list[str] = schema["uniqueness_key"]
    allowed_brokers: list[str] = schema["properties"]["broker"]["enum"]
    ticker_pattern = re.compile(schema["properties"]["ticker_symbol"]["pattern"])

    with csv_path.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        actual_columns: list[str] = list(reader.fieldnames or [])

        missing_columns = [c for c in required_columns if c not in actual_columns]
        if missing_columns:
            errors.extend(
                f"Missing required column: {col!r}" for col in missing_columns
            )
            return errors

        seen_keys: set[tuple[str, ...]] = set()
        for row_num, row in enumerate(reader, start=2):
            errors.extend(
                f"Row {row_num}: blank required field {fn!r}"
                for fn in required_non_empty
                if not row.get(fn, "").strip()
            )

            broker = row.get("broker", "")
            if broker not in allowed_brokers:
                errors.append(f"Row {row_num}: unsupported broker {broker!r}")

            ticker = row.get("ticker_symbol", "")
            if ticker and not ticker_pattern.fullmatch(ticker):
                errors.append(f"Row {row_num}: invalid ticker_symbol {ticker!r}")

            key = tuple(row.get(k, "") for k in uniqueness_key)
            if key in seen_keys:
                dup = dict(zip(uniqueness_key, key, strict=True))
                errors.append(f"Row {row_num}: duplicate {dup}")
            else:
                seen_keys.add(key)

    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input", type=Path, default=DEFAULT_INPUT, help="CSV path to validate"
    )
    parser.add_argument(
        "--schema", type=Path, default=DEFAULT_SCHEMA, help="Schema JSON path"
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    errors = validate_csv(args.input, args.schema)
    if errors:
        for error in errors:
            print(error)
        raise SystemExit(1)
    print(f"validated {args.input}: OK")


if __name__ == "__main__":
    main()
