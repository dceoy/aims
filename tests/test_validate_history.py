from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from pathlib import Path
    from types import ModuleType

import aims.validate_history as _aims_vh


@pytest.fixture(scope="module")
def vh() -> ModuleType:
    return _aims_vh


def _valid() -> dict[str, object]:
    return {
        "version": "1.0.0",
        "analysis_date": "2024-01-02",
        "previous_analysis_date": "2024-01-01",
        "top_k": 5,
        "instruments": [],
        "dropped_from_top_k": [],
    }


def _valid_row() -> dict[str, object]:
    return {
        "symbol": "A",
        "current_rank": 1,
        "previous_rank": None,
        "rank_delta": None,
        "current_score": 80.0,
        "previous_score": None,
        "score_delta": None,
        "is_reliable": True,
        "new_top_k": False,
        "consecutive_reliable_reports": 1,
        "consecutive_top_k_reports": 1,
        "risk_gates_added": [],
        "risk_gates_removed": [],
    }


def test_validate_valid_and_null_previous(vh: ModuleType) -> None:
    assert vh.validate(_valid()) == []
    artifact = _valid()
    artifact["previous_analysis_date"] = None
    artifact["instruments"] = [_valid_row()]
    assert vh.validate(artifact) == []


def test_validate_errors(vh: ModuleType) -> None:
    errors = vh.validate({
        "version": "2",
        "analysis_date": 1,
        "previous_analysis_date": 2,
        "top_k": True,
        "instruments": {},
        "dropped_from_top_k": {},
    })
    assert len(errors) == 6


def test_validate_malformed_rows(vh: ModuleType) -> None:
    artifact = _valid()
    malformed = dict.fromkeys(_valid_row(), True)
    malformed["risk_gates_added"] = [1]
    malformed["risk_gates_removed"] = "gate"
    artifact["instruments"] = ["bad", {}, malformed]
    artifact["dropped_from_top_k"] = [1]
    errors = vh.validate(artifact)
    assert "instruments[0] must be an object" in errors
    assert any("instruments[1] missing keys" in error for error in errors)
    assert any(".symbol must be a string" in error for error in errors)
    assert any(".current_rank must be a positive integer" in error for error in errors)
    assert any(".previous_rank must be an integer or null" in error for error in errors)
    assert any(".current_score must be a number" in error for error in errors)
    assert any(".previous_score must be a number or null" in error for error in errors)
    assert any(".is_reliable must be a boolean" in error for error in errors)
    assert any(
        ".risk_gates_added must be an array of strings" in error for error in errors
    )
    assert "dropped_from_top_k must be an array" in errors


def test_main(vh: ModuleType, tmp_path: Path) -> None:
    valid = tmp_path / "valid.json"
    valid.write_text(json.dumps(_valid()))
    invalid = tmp_path / "invalid.json"
    invalid.write_text("{")
    structurally_invalid = tmp_path / "structurally-invalid.json"
    structurally_invalid.write_text("{}")
    assert vh.main(["--input", str(valid)]) == 0
    assert vh.main(["--input", str(invalid)]) == 1
    assert vh.main(["--input", str(structurally_invalid)]) == 1
    assert vh.main(["--input", str(tmp_path / "missing.json")]) == 1
