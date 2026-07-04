"""Tests for aims.validate_calendar."""

from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING, Any

from aims import validate_calendar as vc

if TYPE_CHECKING:
    import pytest

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "calendar_2024.json"


def _load() -> dict[str, Any]:
    with FIXTURE.open() as fh:
        value: dict[str, Any] = json.load(fh)
    return value


def test_fixture_is_valid() -> None:
    assert vc.validate_calendar(_load()) == []


def test_missing_top_keys() -> None:
    errors = vc.validate_calendar({})
    assert any("version" in e for e in errors)
    assert any("metadata" in e for e in errors)
    assert any("events" in e for e in errors)


def test_wrong_version() -> None:
    data = _load()
    data["version"] = "9.9.9"
    assert any("unsupported version" in e for e in vc.validate_calendar(data))


def test_metadata_not_object() -> None:
    data = _load()
    data["metadata"] = "nope"
    assert any("metadata" in e for e in vc.validate_calendar(data))


def test_metadata_missing_keys() -> None:
    data = _load()
    del data["metadata"]["source"]
    assert any("source" in e for e in vc.validate_calendar(data))


def test_bad_updated_at() -> None:
    data = _load()
    data["metadata"]["updated_at"] = "01-01-2024"
    assert any("updated_at" in e for e in vc.validate_calendar(data))


def test_events_not_array() -> None:
    data = _load()
    data["events"] = {}
    assert vc.validate_calendar(data) == ["'events' must be a JSON array"]


def test_event_not_object() -> None:
    data = _load()
    data["events"] = ["nope"]
    assert vc.validate_calendar(data) == ["events[0] must be a JSON object"]


def test_event_missing_keys() -> None:
    data = _load()
    del data["events"][0]["title"]
    assert any("missing required key: 'title'" in e for e in vc.validate_calendar(data))


def test_event_bad_date() -> None:
    data = _load()
    data["events"][0]["date"] = "01-01-2024"
    assert any("not a YYYY-MM-DD date" in e for e in vc.validate_calendar(data))


def test_event_empty_title() -> None:
    data = _load()
    data["events"][0]["title"] = "   "
    assert any("non-empty string" in e for e in vc.validate_calendar(data))


def test_event_bad_category() -> None:
    data = _load()
    data["events"][0]["category"] = "rumor"
    assert any("is not one of" in e for e in vc.validate_calendar(data))


def test_event_bad_list_fields() -> None:
    data = _load()
    data["events"][0]["canonical_ids"] = "aapl"
    assert any(
        "canonical_ids must be a list of strings" in e
        for e in vc.validate_calendar(data)
    )


def test_event_untagged() -> None:
    data = _load()
    data["events"][0]["canonical_ids"] = []
    data["events"][0]["asset_classes"] = []
    assert any(
        "must tag at least one canonical_id" in e for e in vc.validate_calendar(data)
    )


# ── CLI ─────────────────────────────────────────────────────────────────────


def test_main_ok(capsys: pytest.CaptureFixture[str]) -> None:
    rc = vc.main(["--input", str(FIXTURE)])
    assert rc == 0
    assert "OK" in capsys.readouterr().out


def test_main_missing_file(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    rc = vc.main(["--input", str(tmp_path / "missing.json")])
    assert rc == 1
    assert "file not found" in capsys.readouterr().out


def test_main_invalid_json(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    path = tmp_path / "bad.json"
    path.write_text("{not json", encoding="utf-8")
    rc = vc.main(["--input", str(path)])
    assert rc == 1
    assert "invalid JSON" in capsys.readouterr().out


def test_main_validation_failure(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    path = tmp_path / "bad.json"
    path.write_text("{}", encoding="utf-8")
    rc = vc.main(["--input", str(path)])
    assert rc == 1
    assert "missing required key" in capsys.readouterr().out
