"""Tests for the prompt-regression history validator."""

from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any

import pytest

from aims.validate_prompt_regression import main, validate_history

REPO_ROOT = Path(__file__).resolve().parent.parent
COMMITTED = REPO_ROOT / "data/performance/prompt_regressions.json"


@pytest.fixture
def history() -> dict[str, Any]:
    with COMMITTED.open(encoding="utf-8") as stream:
        value: dict[str, Any] = json.load(stream)
    return copy.deepcopy(value)


def test_committed_history_is_valid(history: dict[str, Any]) -> None:
    assert validate_history(history) == []


def test_missing_top_key_short_circuits() -> None:
    assert validate_history({"version": "1.0.0"}) == ["missing required key: 'entries'"]


def test_wrong_version(history: dict[str, Any]) -> None:
    history["version"] = "0.0.1"
    assert any("unsupported version" in e for e in validate_history(history))


def test_entries_must_be_array(history: dict[str, Any]) -> None:
    history["entries"] = {}
    assert validate_history(history) == ["'entries' must be a JSON array"]


def test_entry_must_be_object(history: dict[str, Any]) -> None:
    history["entries"] = [3]
    assert validate_history(history) == ["entries[0] must be a JSON object"]


def test_entry_missing_key(history: dict[str, Any]) -> None:
    del history["entries"][0]["metrics"]
    assert validate_history(history) == ["entries[0] missing required key: 'metrics'"]


def test_entry_field_errors(history: dict[str, Any]) -> None:
    entry = history["entries"][0]
    entry["analysis_date"] = "someday"
    entry["artifact"] = ""
    entry["prompt_sha256"] = "xyz"
    entry["artifact_provenance"] = "x"
    entry["metrics"] = []
    entry["checks"] = {"a": "yes"}
    entry["passed"] = "true"
    errors = validate_history(history)
    assert "entries[0].analysis_date 'someday' is not a YYYY-MM-DD date" in errors
    assert "entries[0].artifact must be a non-empty string" in errors
    assert "entries[0].prompt_sha256 'xyz' is not a SHA-256 hex digest" in errors
    assert "entries[0].artifact_provenance must be a JSON object" in errors
    assert "entries[0].metrics must be a JSON object" in errors
    assert "entries[0].checks must map check names to booleans" in errors
    assert "entries[0].passed must be a boolean" in errors


def test_entry_provenance_missing_key(history: dict[str, Any]) -> None:
    del history["entries"][0]["artifact_provenance"]["model_id"]
    assert (
        "entries[0].artifact_provenance missing required key: 'model_id'"
        in validate_history(history)
    )


def test_passed_must_match_checks(history: dict[str, Any]) -> None:
    history["entries"][0]["passed"] = False
    assert "entries[0].passed does not match the recorded checks" in validate_history(
        history
    )


def test_main_validates_committed_history(capsys: Any) -> None:
    assert main(["--input", str(COMMITTED)]) == 0
    assert "OK" in capsys.readouterr().out


def test_main_reports_errors(tmp_path: Path, capsys: Any) -> None:
    bad = tmp_path / "bad.json"
    bad.write_text("{}", encoding="utf-8")
    assert main(["--input", str(bad)]) == 1
    assert "missing required key" in capsys.readouterr().out


def test_main_missing_and_invalid_files(tmp_path: Path, capsys: Any) -> None:
    assert main(["--input", str(tmp_path / "absent.json")]) == 1
    assert "file not found" in capsys.readouterr().out
    broken = tmp_path / "broken.json"
    broken.write_text("{", encoding="utf-8")
    assert main(["--input", str(broken)]) == 1
    assert "invalid JSON" in capsys.readouterr().out
