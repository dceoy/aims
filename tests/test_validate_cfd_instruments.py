from __future__ import annotations

import csv
import importlib.util
import sys
from pathlib import Path
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from types import ModuleType

    from pytest_mock import MockerFixture

SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / ".agents"
    / "skills"
    / "update-cfd-instruments"
    / "scripts"
    / "validate_cfd_instruments.py"
)
SCHEMA_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "schema"
    / "cfd_instruments.schema.json"
)

VALID_ROW = {
    "source_accessed_at": "2026-01-01T00:00:00+09:00",
    "broker": "楽天証券",
    "source_url": "https://example.com/",
    "category": "指数CFD",
    "section": "株価指数",
    "sector": "",
    "instrument_name": "米国500",
    "ticker_symbol": "ES",
    "underlying_asset_exchange": "CME",
    "currency": "USD",
    "tick_size": "0.1",
    "price_display_example": "",
    "minimum_trade_unit": "1",
    "contract_value_per_lot": "",
    "trade_unit": "",
    "trading_hours": "",
    "margin_rate_leverage": "10倍",
    "max_order_quantity": "",
    "instrument_position_limit": "",
    "account_position_limit": "",
    "price_adjustment": "",
    "interest_adjustment": "",
    "rights_adjustment": "",
    "instrument_position_limit_note": "",
    "minimum_trade_quantity": "",
    "withholding_tax_note": "",
}

ALL_FIELDS = list(VALID_ROW.keys())


@pytest.fixture(scope="module")
def validator() -> ModuleType:
    spec = importlib.util.spec_from_file_location(
        "validate_cfd_instruments", SCRIPT_PATH
    )
    if spec is None or spec.loader is None:
        pytest.fail("Failed to load validate_cfd_instruments.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def write_csv(
    tmp_path: Path, rows: list[dict[str, str]], fields: list[str] | None = None
) -> Path:
    fields = fields or ALL_FIELDS
    path = tmp_path / "test.csv"
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    return path


def test_validate_csv_valid(validator: ModuleType, tmp_path: Path) -> None:
    csv_path = write_csv(tmp_path, [VALID_ROW])
    errors = validator.validate_csv(csv_path, SCHEMA_PATH)
    assert errors == []


def test_validate_csv_missing_required_column(
    validator: ModuleType, tmp_path: Path
) -> None:
    fields_without_broker = [f for f in ALL_FIELDS if f != "broker"]
    csv_path = write_csv(tmp_path, [VALID_ROW], fields=fields_without_broker)
    errors = validator.validate_csv(csv_path, SCHEMA_PATH)
    assert any("broker" in e for e in errors)
    assert len(errors) == 1


def test_validate_csv_blank_required_field(
    validator: ModuleType, tmp_path: Path
) -> None:
    row = {**VALID_ROW, "category": ""}
    csv_path = write_csv(tmp_path, [row])
    errors = validator.validate_csv(csv_path, SCHEMA_PATH)
    assert any("category" in e for e in errors)


def test_validate_csv_unsupported_category(
    validator: ModuleType, tmp_path: Path
) -> None:
    row = {**VALID_ROW, "category": "未知カテゴリ"}
    csv_path = write_csv(tmp_path, [row])
    errors = validator.validate_csv(csv_path, SCHEMA_PATH)
    assert any("category" in e for e in errors)


def test_validate_csv_unsupported_broker(validator: ModuleType, tmp_path: Path) -> None:
    row = {**VALID_ROW, "broker": "UnknownBroker"}
    csv_path = write_csv(tmp_path, [row])
    errors = validator.validate_csv(csv_path, SCHEMA_PATH)
    assert any("UnknownBroker" in e for e in errors)


def test_validate_csv_invalid_ticker_symbol(
    validator: ModuleType, tmp_path: Path
) -> None:
    row = {**VALID_ROW, "ticker_symbol": "lowercase"}
    csv_path = write_csv(tmp_path, [row])
    errors = validator.validate_csv(csv_path, SCHEMA_PATH)
    assert any("ticker_symbol" in e for e in errors)


def test_validate_csv_no_data_rows(validator: ModuleType, tmp_path: Path) -> None:
    csv_path = write_csv(tmp_path, [])
    errors = validator.validate_csv(csv_path, SCHEMA_PATH)
    assert any("No data rows" in e for e in errors)


def test_validate_csv_duplicate_row(validator: ModuleType, tmp_path: Path) -> None:
    csv_path = write_csv(tmp_path, [VALID_ROW, VALID_ROW])
    errors = validator.validate_csv(csv_path, SCHEMA_PATH)
    assert any("duplicate" in e for e in errors)


def test_main_exits_zero_on_valid_csv(
    validator: ModuleType,
    mocker: MockerFixture,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    csv_path = write_csv(tmp_path, [VALID_ROW])
    mocker.patch.object(
        sys,
        "argv",
        [
            "validate_cfd_instruments.py",
            "--input",
            str(csv_path),
            "--schema",
            str(SCHEMA_PATH),
        ],
    )
    validator.main()
    assert "OK" in capsys.readouterr().out


def test_main_exits_nonzero_on_invalid_csv(
    validator: ModuleType,
    mocker: MockerFixture,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    row = {**VALID_ROW, "broker": "Bad"}
    csv_path = write_csv(tmp_path, [row])
    mocker.patch.object(
        sys,
        "argv",
        [
            "validate_cfd_instruments.py",
            "--input",
            str(csv_path),
            "--schema",
            str(SCHEMA_PATH),
        ],
    )
    with pytest.raises(SystemExit) as exc_info:
        validator.main()
    assert exc_info.value.code == 1
    assert capsys.readouterr().out.strip()


def test_parse_args_defaults(validator: ModuleType, mocker: MockerFixture) -> None:
    mocker.patch.object(sys, "argv", ["validate_cfd_instruments.py"])
    args = validator.parse_args()
    assert args.input == validator.DEFAULT_INPUT
    assert args.schema == validator.DEFAULT_SCHEMA


def test_parse_args_custom(validator: ModuleType, mocker: MockerFixture) -> None:
    mocker.patch.object(
        sys,
        "argv",
        [
            "validate_cfd_instruments.py",
            "--input",
            "custom.csv",
            "--schema",
            "custom.schema.json",
        ],
    )
    args = validator.parse_args()
    assert args.input == Path("custom.csv")
    assert args.schema == Path("custom.schema.json")
