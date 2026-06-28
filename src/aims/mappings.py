"""Validate data/mappings/canonical_instrument_mappings.csv.

Usage:
    uv run .agents/skills/market-analysis/scripts/validate_instrument_mappings.py \
        --input data/mappings/canonical_instrument_mappings.csv \
        --cfd-instruments data/cfd_instruments.csv
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path
from typing import Final

DEFAULT_MAPPING = Path("data/mappings/canonical_instrument_mappings.csv")
DEFAULT_CFD = Path("data/cfd_instruments.csv")

_REQUIRED_COLUMNS: Final[tuple[str, ...]] = (
    "canonical_id",
    "display_name",
    "asset_class",
    "broker",
    "broker_instrument_name",
    "broker_ticker_symbol",
    "provider",
    "provider_symbol",
    "provider_interval",
    "tradable",
)

_REQUIRED_NON_EMPTY: Final[frozenset[str]] = frozenset({
    "canonical_id",
    "display_name",
    "provider",
    "provider_symbol",
    "provider_interval",
})

_KNOWN_PROVIDERS: Final[frozenset[str]] = frozenset({"stooq", "csv", "yfinance"})

_PROVIDER_INTERVALS: Final[dict[str, frozenset[str]]] = {
    "stooq": frozenset({"d", "w", "m"}),
    "csv": frozenset({"d", "w", "m"}),
    "yfinance": frozenset({"d", "w", "m"}),
}


def _load_cfd_instruments(path: Path) -> set[tuple[str, str]]:
    """Return set of (broker, instrument_name) from cfd_instruments.csv."""
    instruments: set[tuple[str, str]] = set()
    with path.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            broker = row.get("broker", "").strip()
            name = row.get("instrument_name", "").strip()
            if broker and name:
                instruments.add((broker, name))
    return instruments


def validate_mappings(
    mapping_path: Path,
    cfd_path: Path | None = None,
) -> tuple[list[str], list[str]]:
    """Validate canonical_instrument_mappings.csv.

    Returns (errors, warnings). Errors are hard failures; warnings are
    informational notices about unmapped tradable CFD instruments.
    """
    errors: list[str] = []
    warnings: list[str] = []

    with mapping_path.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        actual_columns = list(reader.fieldnames or [])
        missing_cols = [c for c in _REQUIRED_COLUMNS if c not in actual_columns]
        if missing_cols:
            errors.extend(f"missing required column: {col!r}" for col in missing_cols)
            return errors, warnings

        rows = list(reader)

    if not rows:
        errors.append("mapping file has no data rows")
        return errors, warnings

    cfd_instruments: set[tuple[str, str]] = set()
    if cfd_path is not None and cfd_path.exists():
        cfd_instruments = _load_cfd_instruments(cfd_path)

    # canonical_id -> set of (provider, provider_symbol, provider_interval)
    canonical_provider_keys: dict[str, set[tuple[str, str, str]]] = {}
    # (provider, provider_symbol, provider_interval) -> canonical_id
    provider_key_to_canonical: dict[tuple[str, str, str], str] = {}

    for row_num, row in enumerate(rows, start=2):
        canonical_id = row.get("canonical_id", "").strip()
        provider = row.get("provider", "").strip()
        provider_symbol = row.get("provider_symbol", "").strip()
        provider_interval = row.get("provider_interval", "").strip()
        broker = row.get("broker", "").strip()
        broker_instrument_name = row.get("broker_instrument_name", "").strip()

        errors.extend(
            f"row {row_num}: required field {field!r} is empty"
            for field in _REQUIRED_NON_EMPTY
            if not row.get(field, "").strip()
        )

        if (
            not canonical_id
            or not provider
            or not provider_symbol
            or not provider_interval
        ):
            continue

        if provider not in _KNOWN_PROVIDERS:
            known = ", ".join(sorted(_KNOWN_PROVIDERS))
            errors.append(
                f"row {row_num}: unknown provider {provider!r}; known: {known}"
            )

        elif provider_interval not in _PROVIDER_INTERVALS.get(provider, frozenset()):
            supported = ", ".join(
                sorted(_PROVIDER_INTERVALS.get(provider, frozenset()))
            )
            errors.append(
                f"row {row_num}: provider {provider!r} does not support"
                f" interval {provider_interval!r}; supported: {supported}"
            )

        provider_key = (provider, provider_symbol, provider_interval)
        existing_canonical = provider_key_to_canonical.get(provider_key)
        if existing_canonical is not None and existing_canonical != canonical_id:
            errors.append(
                f"row {row_num}: duplicate provider mapping"
                f" ({provider}, {provider_symbol}, {provider_interval})"
                f" already mapped to canonical_id {existing_canonical!r},"
                f" cannot also map to {canonical_id!r}"
            )
        else:
            provider_key_to_canonical[provider_key] = canonical_id

        if canonical_id not in canonical_provider_keys:
            canonical_provider_keys[canonical_id] = set()
        canonical_provider_keys[canonical_id].add(provider_key)

        if (
            broker
            and broker_instrument_name
            and (
                cfd_instruments
                and (broker, broker_instrument_name) not in cfd_instruments
            )
        ):
            errors.append(
                f"row {row_num}: broker instrument"
                f" ({broker!r}, {broker_instrument_name!r})"
                f" not found in cfd_instruments.csv"
            )

    if cfd_instruments:
        mapped_broker_instruments: set[tuple[str, str]] = set()
        with mapping_path.open(encoding="utf-8", newline="") as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                b = row.get("broker", "").strip()
                n = row.get("broker_instrument_name", "").strip()
                t = row.get("tradable", "").strip().lower()
                if b and n:
                    mapped_broker_instruments.add((b, n))
                _ = t
        unmapped = cfd_instruments - mapped_broker_instruments
        for broker, name in sorted(unmapped):
            warnings.append(
                f"WARNING: CFD instrument ({broker!r}, {name!r})"
                f" has no canonical mapping entry"
            )

    return errors, warnings


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_MAPPING,
        help="Path to canonical_instrument_mappings.csv",
    )
    parser.add_argument(
        "--cfd-instruments",
        type=Path,
        default=DEFAULT_CFD,
        dest="cfd_instruments",
        help="Path to cfd_instruments.csv for broker reference checks",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        errors, warnings = validate_mappings(args.input, args.cfd_instruments)
    except FileNotFoundError as exc:
        print(f"ERROR: file not found: {exc}")
        return 1
    except (OSError, csv.Error) as exc:
        print(f"ERROR: failed to read mapping file: {exc}")
        return 1
    for w in warnings:
        print(w)
    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        return 1
    print(f"validated {args.input}: OK ({len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
