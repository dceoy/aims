from __future__ import annotations

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
    / "market-analysis"
    / "scripts"
    / "validate_instrument_mappings.py"
)


@pytest.fixture(scope="module")
def vim() -> ModuleType:
    spec = importlib.util.spec_from_file_location(
        "validate_instrument_mappings", SCRIPT_PATH
    )
    if spec is None or spec.loader is None:
        pytest.fail("Failed to load validate_instrument_mappings.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


_HEADERS = (
    "canonical_id,display_name,asset_class,broker,broker_instrument_name,"
    "broker_ticker_symbol,provider,provider_symbol,provider_interval,tradable"
)

_VALID_ROW = "spx,S&P 500,equity_index,TestBroker,US500,ES,stooq,^SPX,d,true"


def _write_mapping(tmp_path: Path, rows: list[str]) -> Path:
    p = tmp_path / "mappings.csv"
    p.write_text(_HEADERS + "\n" + "\n".join(rows), encoding="utf-8")
    return p


def _write_cfd(tmp_path: Path, rows: list[str]) -> Path:
    p = tmp_path / "cfd.csv"
    p.write_text("broker,instrument_name\n" + "\n".join(rows), encoding="utf-8")
    return p


def test_valid_mapping_no_errors(vim: ModuleType, tmp_path: Path) -> None:
    p = _write_mapping(tmp_path, [_VALID_ROW])
    errors, _warnings = vim.validate_mappings(p)
    assert errors == []


def test_missing_required_column(vim: ModuleType, tmp_path: Path) -> None:
    p = tmp_path / "bad.csv"
    p.write_text("canonical_id,display_name\nspx,S&P 500\n", encoding="utf-8")
    errors, _ = vim.validate_mappings(p)
    assert any("missing required column" in e for e in errors)


def test_empty_required_field_canonical_id(vim: ModuleType, tmp_path: Path) -> None:
    row = ",S&P 500,equity_index,TestBroker,US500,ES,stooq,^SPX,d,true"
    p = _write_mapping(tmp_path, [row])
    errors, _ = vim.validate_mappings(p)
    assert any("canonical_id" in e for e in errors)


def test_empty_required_field_provider(vim: ModuleType, tmp_path: Path) -> None:
    row = "spx,S&P 500,equity_index,TestBroker,US500,ES,,^SPX,d,true"
    p = _write_mapping(tmp_path, [row])
    errors, _ = vim.validate_mappings(p)
    assert any("provider" in e for e in errors)


def test_unknown_provider(vim: ModuleType, tmp_path: Path) -> None:
    row = "spx,S&P 500,equity_index,TestBroker,US500,ES,bloomberg,^SPX,d,true"
    p = _write_mapping(tmp_path, [row])
    errors, _ = vim.validate_mappings(p)
    assert any("unknown provider" in e for e in errors)


def test_unsupported_interval(vim: ModuleType, tmp_path: Path) -> None:
    row = "spx,S&P 500,equity_index,TestBroker,US500,ES,stooq,^SPX,1h,true"
    p = _write_mapping(tmp_path, [row])
    errors, _ = vim.validate_mappings(p)
    assert any("does not support interval" in e for e in errors)


def test_duplicate_provider_mapping_different_canonical(
    vim: ModuleType, tmp_path: Path
) -> None:
    rows = [
        "spx,S&P 500,equity_index,A,US500,ES,stooq,^SPX,d,true",
        "sp500alt,S&P Alt,equity_index,B,US500,ES,stooq,^SPX,d,true",
    ]
    p = _write_mapping(tmp_path, rows)
    errors, _ = vim.validate_mappings(p)
    assert any("duplicate provider mapping" in e for e in errors)


def test_same_canonical_same_provider_key_ok(vim: ModuleType, tmp_path: Path) -> None:
    rows = [
        "spx,S&P 500,equity_index,BrokerA,US500,ES,stooq,^SPX,d,true",
        "spx,S&P 500,equity_index,BrokerA,US500,ES,stooq,^SPX,d,true",
    ]
    p = _write_mapping(tmp_path, rows)
    errors, _ = vim.validate_mappings(p)
    assert not any("duplicate provider mapping" in e for e in errors)


def test_broker_instrument_not_in_cfd(vim: ModuleType, tmp_path: Path) -> None:
    mapping_path = _write_mapping(tmp_path, [_VALID_ROW])
    cfd_path = _write_cfd(tmp_path, ["OtherBroker,US500"])
    errors, _ = vim.validate_mappings(mapping_path, cfd_path)
    assert any("not found in cfd_instruments.csv" in e for e in errors)


def test_broker_instrument_found_in_cfd_no_error(
    vim: ModuleType, tmp_path: Path
) -> None:
    mapping_path = _write_mapping(tmp_path, [_VALID_ROW])
    cfd_path = _write_cfd(tmp_path, ["TestBroker,US500"])
    errors, _ = vim.validate_mappings(mapping_path, cfd_path)
    assert errors == []


def test_cfd_row_with_empty_broker_skipped(vim: ModuleType, tmp_path: Path) -> None:
    # CFD file rows with empty broker or instrument_name must be skipped gracefully
    mapping_path = _write_mapping(tmp_path, [_VALID_ROW])
    cfd_path = tmp_path / "cfd_empty.csv"
    cfd_path.write_text(
        "broker,instrument_name\nTestBroker,US500\n,EmptyBroker\nTestBroker,\n",
        encoding="utf-8",
    )
    errors, _ = vim.validate_mappings(mapping_path, cfd_path)
    assert errors == []


def test_warns_unmapped_tradable_cfd(vim: ModuleType, tmp_path: Path) -> None:
    mapping_path = _write_mapping(tmp_path, [_VALID_ROW])
    cfd_path = _write_cfd(tmp_path, ["TestBroker,US500", "TestBroker,US30"])
    _, warnings = vim.validate_mappings(mapping_path, cfd_path)
    assert any("US30" in w for w in warnings)


def test_no_data_rows(vim: ModuleType, tmp_path: Path) -> None:
    p = tmp_path / "empty.csv"
    p.write_text(_HEADERS + "\n", encoding="utf-8")
    errors, _ = vim.validate_mappings(p)
    assert any("no data rows" in e for e in errors)


def test_cfd_path_not_exists_skips_broker_check(
    vim: ModuleType, tmp_path: Path
) -> None:
    mapping_path = _write_mapping(tmp_path, [_VALID_ROW])
    errors, _ = vim.validate_mappings(mapping_path, tmp_path / "nonexistent.csv")
    assert errors == []


def test_row_with_empty_broker_skips_cfd_check(vim: ModuleType, tmp_path: Path) -> None:
    row = "spx,S&P 500,equity_index,,,,stooq,^SPX,d,true"
    mapping_path = _write_mapping(tmp_path, [row])
    cfd_path = _write_cfd(tmp_path, ["TestBroker,US500"])
    errors, _ = vim.validate_mappings(mapping_path, cfd_path)
    assert not any("not found in cfd_instruments.csv" in e for e in errors)


def test_main_returns_0_on_valid(vim: ModuleType, tmp_path: Path) -> None:
    p = _write_mapping(tmp_path, [_VALID_ROW])
    # Use a non-existent CFD path to skip broker reference checks
    result = vim.main([
        "--input",
        str(p),
        "--cfd-instruments",
        str(tmp_path / "no_cfd.csv"),
    ])
    assert result == 0


def test_main_prints_warnings_and_returns_0(
    vim: ModuleType,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    # TestBroker/US500 is mapped; TestBroker/US30 is in CFD but not mapped → warning
    mapping_path = _write_mapping(tmp_path, [_VALID_ROW])
    cfd_path = _write_cfd(tmp_path, ["TestBroker,US500", "TestBroker,US30"])
    result = vim.main([
        "--input",
        str(mapping_path),
        "--cfd-instruments",
        str(cfd_path),
    ])
    assert result == 0
    out = capsys.readouterr().out
    assert "WARNING" in out


def test_main_returns_1_on_error(vim: ModuleType, tmp_path: Path) -> None:
    p = tmp_path / "bad.csv"
    p.write_text("canonical_id,display_name\nspx,S&P 500\n", encoding="utf-8")
    assert vim.main(["--input", str(p)]) == 1


def test_main_returns_1_file_not_found(vim: ModuleType) -> None:
    assert vim.main(["--input", "nonexistent_file.csv"]) == 1


def test_main_returns_1_on_os_error(
    vim: ModuleType, tmp_path: Path, mocker: MockerFixture
) -> None:
    p = _write_mapping(tmp_path, [_VALID_ROW])
    mocker.patch.object(vim, "validate_mappings", side_effect=OSError("io"))
    assert vim.main(["--input", str(p)]) == 1


def test_real_mapping_validates_ok(vim: ModuleType) -> None:
    mapping_path = Path("data/mappings/canonical_instrument_mappings.csv")
    cfd_path = Path("data/cfd_instruments.csv")
    errors, _ = vim.validate_mappings(mapping_path, cfd_path)
    assert errors == [], f"real mapping failed validation: {errors}"
