#!/usr/bin/env python3
"""Validate data/cfd_instruments.csv against its JSON schema."""

from __future__ import annotations

import argparse
import csv
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

DEFAULT_INPUT = Path("data/cfd_instruments.csv")
DEFAULT_SCHEMA = Path("data/schema/cfd_instruments.schema.json")


def load_schema(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)  # type: ignore[no-any-return]


@dataclass
class _SchemaConfig:
    required_columns: list[str]
    required_non_empty: set[str]
    uniqueness_key: list[str]
    allowed_brokers: list[str]
    allowed_categories_by_broker: dict[str, list[str]]
    ticker_pattern: re.Pattern[str]


def _parse_schema(schema: dict[str, Any]) -> _SchemaConfig:
    props = schema["properties"]
    return _SchemaConfig(
        required_columns=schema["columns"],
        required_non_empty=set(schema["required_non_empty"]),
        uniqueness_key=schema["uniqueness_key"],
        allowed_brokers=props["broker"]["enum"],
        allowed_categories_by_broker=props["category"]["allowed_categories_by_broker"],
        ticker_pattern=re.compile(props["ticker_symbol"]["pattern"]),
    )


def validate_csv(csv_path: Path, schema_path: Path) -> list[str]:
    cfg = _parse_schema(load_schema(schema_path))
    errors: list[str] = []

    with csv_path.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        actual_columns: list[str] = list(reader.fieldnames or [])

        missing_columns = [c for c in cfg.required_columns if c not in actual_columns]
        if missing_columns:
            errors.extend(
                f"Missing required column: {col!r}" for col in missing_columns
            )
            return errors

        seen_keys: set[tuple[str, ...]] = set()
        row_count = 0
        for row_num, row in enumerate(reader, start=2):
            row_count += 1
            errors.extend(
                f"Row {row_num}: blank required field {fn!r}"
                for fn in cfg.required_non_empty
                if not row.get(fn, "").strip()
            )

            broker = row.get("broker", "")
            if broker not in cfg.allowed_brokers:
                errors.append(f"Row {row_num}: unsupported broker {broker!r}")
            else:
                category = row.get("category", "")
                allowed_cats = cfg.allowed_categories_by_broker.get(broker, [])
                if category and category not in allowed_cats:
                    errors.append(
                        f"Row {row_num}: unsupported category {category!r}"
                        f" for broker {broker!r}"
                    )

            ticker = row.get("ticker_symbol", "")
            if ticker and not cfg.ticker_pattern.fullmatch(ticker):
                errors.append(f"Row {row_num}: invalid ticker_symbol {ticker!r}")

            key = tuple(row.get(k, "") for k in cfg.uniqueness_key)
            if key in seen_keys:
                dup = dict(zip(cfg.uniqueness_key, key, strict=True))
                errors.append(f"Row {row_num}: duplicate {dup}")
            else:
                seen_keys.add(key)

    if not row_count:
        errors.append("No data rows found")
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
