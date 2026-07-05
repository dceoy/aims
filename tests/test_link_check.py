"""Tests for the citation link-rot sampling check (warning only, never a gate)."""

from __future__ import annotations

import json
import urllib.error
from typing import TYPE_CHECKING, Any

import pytest

from aims import link_check

if TYPE_CHECKING:
    from pathlib import Path


def _bundle(when: str, items: list[dict[str, Any]]) -> dict[str, Any]:
    return {"metadata": {"analysis_date": when}, "items": items}


def _item(item_id: str, url: str) -> dict[str, Any]:
    return {"id": item_id, "url": url}


# ── sampling ─────────────────────────────────────────────────────────────────


def test_sample_items_windows_dedupes_sorts_and_caps() -> None:
    bundles = [
        _bundle("2024-01-01", [_item("ev-old", "https://a.example/old")]),
        _bundle(
            "2024-01-20",
            [
                _item("ev-b", "https://a.example/dup"),
                _item("ev-a", "https://a.example/dup"),
                _item("ev-c", "https://a.example/c"),
            ],
        ),
        _bundle("2024-01-21", [_item("ev-d", "https://a.example/d")]),
    ]
    sampled = link_check.sample_items(bundles, days=7, limit=10)
    assert [item["id"] for item in sampled] == ["ev-a", "ev-c", "ev-d"]
    assert link_check.sample_items(bundles, days=7, limit=2) == sampled[:2]
    # a wide window brings the old bundle back in
    wide = link_check.sample_items(bundles, days=30, limit=10)
    assert next(item["id"] for item in wide) == "ev-a"
    assert any(item["id"] == "ev-old" for item in wide)


def test_sample_items_skips_undated_bundles_and_bad_items() -> None:
    assert link_check.sample_items([], days=7, limit=5) == []
    bundles = [
        {"metadata": {}, "items": [_item("ev-a", "https://a.example/a")]},
        _bundle("2024-01-01", [{"id": "ev-b"}, "not-a-dict"]),
    ]
    assert link_check.sample_items(bundles, days=7, limit=5) == []


# ── URL probing ──────────────────────────────────────────────────────────────


def test_check_url_rejects_non_http() -> None:
    assert link_check.check_url("ftp://example.com/x") == "not an HTTP(S) URL"


def test_check_url_ok(mocker: Any) -> None:
    mocker.patch("urllib.request.urlopen", return_value=mocker.MagicMock())
    assert link_check.check_url("https://example.com/ok") is None


def test_check_url_head_fails_get_succeeds(mocker: Any) -> None:
    error = urllib.error.HTTPError(
        "https://example.com/x", 405, "Method Not Allowed", None, None
    )
    mocked = mocker.patch(
        "urllib.request.urlopen", side_effect=[error, mocker.MagicMock()]
    )
    assert link_check.check_url("https://example.com/x") is None
    assert mocked.call_count == 2


def test_check_url_reports_http_error_after_get_retry(mocker: Any) -> None:
    error = urllib.error.HTTPError(
        "https://example.com/x", 404, "Not Found", None, None
    )
    mocker.patch("urllib.request.urlopen", side_effect=[error, error])
    assert link_check.check_url("https://example.com/x") == "HTTP 404"


def test_check_url_reports_unreachable_and_timeout(mocker: Any) -> None:
    mocker.patch(
        "urllib.request.urlopen",
        side_effect=urllib.error.URLError("no route"),
    )
    assert link_check.check_url("https://example.com/x") == "unreachable: no route"
    mocker.patch("urllib.request.urlopen", side_effect=TimeoutError)
    assert link_check.check_url("https://example.com/x") == "timed out"


# ── CLI ──────────────────────────────────────────────────────────────────────


def test_main_skips_missing_directory(tmp_path: Path, capsys: Any) -> None:
    assert link_check.main(["--evidence-dir", str(tmp_path / "absent")]) == 0
    assert "skipping link check" in capsys.readouterr().out


def test_main_skips_when_nothing_to_sample(tmp_path: Path, capsys: Any) -> None:
    (tmp_path / "broken.json").write_text("{", encoding="utf-8")
    assert link_check.main(["--evidence-dir", str(tmp_path)]) == 0
    out = capsys.readouterr().out
    assert "skipping unreadable evidence bundle" in out
    assert "No recent evidence citations to sample" in out


def test_main_warns_on_rot_and_still_exits_zero(
    tmp_path: Path, capsys: Any, mocker: Any
) -> None:
    bundle = _bundle(
        "2024-01-01",
        [
            _item("ev-bad", "https://a.example/bad"),
            _item("ev-good", "https://a.example/good"),
        ],
    )
    (tmp_path / "2024-01-01.json").write_text(json.dumps(bundle), encoding="utf-8")
    mocker.patch(
        "aims.link_check.check_url",
        side_effect=lambda url, _timeout: "HTTP 404" if "bad" in url else None,
    )
    assert link_check.main(["--evidence-dir", str(tmp_path)]) == 0
    out = capsys.readouterr().out
    assert "WARNING: citation link rot: ev-bad https://a.example/bad (HTTP 404)" in out
    assert "Link check: 1/2 sampled citation URL(s) unreachable" in out


@pytest.mark.parametrize("flag", ["--days", "--limit"])
def test_main_accepts_tuning_flags(tmp_path: Path, flag: str) -> None:
    bundle = _bundle("2024-01-01", [])
    (tmp_path / "2024-01-01.json").write_text(json.dumps(bundle), encoding="utf-8")
    assert link_check.main(["--evidence-dir", str(tmp_path), flag, "1"]) == 0
