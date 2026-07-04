"""Tests for aims.validate_evidence."""

from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING, Any

from aims import validate_evidence as ve

if TYPE_CHECKING:
    import pytest

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "evidence_2024-01-01.json"


def _load() -> dict[str, Any]:
    with FIXTURE.open() as fh:
        value: dict[str, Any] = json.load(fh)
    return value


def test_fixture_is_valid() -> None:
    assert ve.validate_bundle(_load()) == []


def test_missing_top_keys() -> None:
    errors = ve.validate_bundle({})
    assert any("version" in e for e in errors)
    assert any("metadata" in e for e in errors)
    assert any("items" in e for e in errors)


def test_wrong_version() -> None:
    data = _load()
    data["version"] = "9.9.9"
    errors = ve.validate_bundle(data)
    assert any("unsupported version" in e for e in errors)


def test_metadata_not_object() -> None:
    data = _load()
    data["metadata"] = "nope"
    assert any("metadata" in e for e in ve.validate_bundle(data))


def test_metadata_missing_keys() -> None:
    data = _load()
    del data["metadata"]["lookback_days"]
    assert any("lookback_days" in e for e in ve.validate_bundle(data))


def test_bad_analysis_date() -> None:
    data = _load()
    data["metadata"]["analysis_date"] = "01-01-2024"
    assert any("analysis_date" in e for e in ve.validate_bundle(data))


def test_coverage_missing_keys() -> None:
    data = _load()
    del data["metadata"]["coverage"]["asset_classes"]
    assert any(
        "coverage missing required key: 'asset_classes'" in e
        for e in ve.validate_bundle(data)
    )


def test_coverage_not_object() -> None:
    data = _load()
    data["metadata"]["coverage"] = []
    assert any("coverage must be a JSON object" in e for e in ve.validate_bundle(data))


def test_coverage_sources_bad_status() -> None:
    data = _load()
    data["metadata"]["coverage"]["sources"]["bad"] = {"status": "maybe"}
    assert any("status 'success' or 'failed'" in e for e in ve.validate_bundle(data))


def test_coverage_missing_sources_key_is_fine_when_absent() -> None:
    data = _load()
    del data["metadata"]["coverage"]["sources"]
    errors = ve.validate_bundle(data)
    assert any("coverage missing required key: 'sources'" in e for e in errors)
    assert not any("must record status" in e for e in errors)


def test_metadata_missing_coverage_entirely() -> None:
    data = _load()
    del data["metadata"]["coverage"]
    errors = ve.validate_bundle(data)
    assert any("missing required key: 'coverage'" in e for e in errors)
    assert not any("coverage must be a JSON object" in e for e in errors)


def test_coverage_sources_not_object() -> None:
    data = _load()
    data["metadata"]["coverage"]["sources"] = []
    assert any("sources must be a JSON object" in e for e in ve.validate_bundle(data))


def test_items_not_array() -> None:
    data = _load()
    data["items"] = {}
    assert ve.validate_bundle(data) == ["'items' must be a JSON array"]


def test_item_not_object() -> None:
    data = _load()
    data["items"] = ["nope"]
    assert ve.validate_bundle(data) == ["items[0] must be a JSON object"]


def test_item_missing_keys() -> None:
    data = _load()
    del data["items"][0]["title"]
    assert any("missing required key: 'title'" in e for e in ve.validate_bundle(data))


def test_item_bad_id() -> None:
    data = _load()
    data["items"][0]["id"] = "not-an-id"
    assert any("not a valid evidence ID" in e for e in ve.validate_bundle(data))


def test_item_empty_or_long_title() -> None:
    data = _load()
    data["items"][0]["title"] = ""
    assert any("title must be" in e for e in ve.validate_bundle(data))
    data["items"][0]["title"] = "x" * (ve.TITLE_MAX_CHARS + 1)
    assert any("title must be" in e for e in ve.validate_bundle(data))


def test_item_long_snippet() -> None:
    data = _load()
    data["items"][0]["snippet"] = "x" * (ve.SNIPPET_MAX_CHARS + 1)
    assert any("exceeds" in e for e in ve.validate_bundle(data))


def test_item_bad_url() -> None:
    data = _load()
    data["items"][0]["url"] = "ftp://example.org"
    assert any("not an HTTP(S) URL" in e for e in ve.validate_bundle(data))


def test_item_bad_category() -> None:
    data = _load()
    data["items"][0]["category"] = "rumor"
    assert any("is not valid" in e for e in ve.validate_bundle(data))


def test_item_bad_list_fields() -> None:
    data = _load()
    data["items"][0]["canonical_ids"] = "spx"
    data["items"][0]["asset_classes"] = [1]
    errors = ve.validate_bundle(data)
    assert any("canonical_ids must be a list of strings" in e for e in errors)
    assert any("asset_classes must be a list of strings" in e for e in errors)


def test_duplicate_ids() -> None:
    data = _load()
    data["items"].append(dict(data["items"][0]))
    assert any("duplicate evidence ID" in e for e in ve.validate_bundle(data))


# ── CLI ─────────────────────────────────────────────────────────────────────


def test_main_ok(capsys: pytest.CaptureFixture[str]) -> None:
    rc = ve.main(["--input", str(FIXTURE)])
    assert rc == 0
    assert "OK" in capsys.readouterr().out


def test_main_missing_file(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    rc = ve.main(["--input", str(tmp_path / "missing.json")])
    assert rc == 1
    assert "file not found" in capsys.readouterr().out


def test_main_invalid_json(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    path = tmp_path / "bad.json"
    path.write_text("{not json", encoding="utf-8")
    rc = ve.main(["--input", str(path)])
    assert rc == 1
    assert "invalid JSON" in capsys.readouterr().out


def test_main_validation_failure(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    path = tmp_path / "bad.json"
    path.write_text("{}", encoding="utf-8")
    rc = ve.main(["--input", str(path)])
    assert rc == 1
    assert "missing required key" in capsys.readouterr().out
