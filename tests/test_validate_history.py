from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from types import ModuleType

SCRIPTS = Path(__file__).parents[1] / ".agents/skills/market-analysis/scripts"


@pytest.fixture(scope="module")
def vh() -> ModuleType:
    sys.path.insert(0, str(SCRIPTS))
    spec = importlib.util.spec_from_file_location(
        "validate_history", SCRIPTS / "validate_history.py"
    )
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _valid() -> dict[str, object]:
    return {
        "version": "1.0.0",
        "analysis_date": "2024-01-02",
        "previous_analysis_date": "2024-01-01",
        "top_k": 5,
        "instruments": [],
        "dropped_from_top_k": [],
    }


def test_validate_valid_and_null_previous(vh: ModuleType) -> None:
    assert vh.validate(_valid()) == []
    artifact = _valid()
    artifact["previous_analysis_date"] = None
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
