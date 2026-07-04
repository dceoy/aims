"""Tests for the calendar-event and AI-commentary additions to notify_slack."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from aims import notifications
from aims.calendars import CalendarEvent, load_calendar_events, upcoming_events

FIXTURES = Path(__file__).resolve().parent / "fixtures"
ANALYSIS = FIXTURES / "analysis_2024-01-01_mapped.json"
CALENDAR = FIXTURES / "calendar_2024.json"
QUALITATIVE = FIXTURES / "qualitative_2024-01-01.json"
QUALITATIVE_WITHHELD = FIXTURES / "qualitative_2024-01-01_withheld.json"


def _load(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as fh:
        value: dict[str, Any] = json.load(fh)
    return value


@pytest.fixture
def analysis() -> dict[str, Any]:
    return _load(ANALYSIS)


@pytest.fixture
def qualitative() -> dict[str, Any]:
    return _load(QUALITATIVE)


def _field_texts(payload: dict[str, Any]) -> list[str]:
    fields = payload["blocks"][1]["fields"]
    return [f["text"] for f in fields]


# ── event lines ──────────────────────────────────────────────────────────────


def test_event_lines_reports_matches_and_caps_at_max(
    analysis: dict[str, Any],
) -> None:
    windowed = upcoming_events(
        load_calendar_events([CALENDAR]), "2024-01-01", window_days=7
    )
    lines = notifications._event_lines(analysis, windowed)
    # ^SPX matches the FOMC event (asset_class); ^DJI matches both the FOMC
    # event (asset_class) and its own earnings event (canonical_id) — three
    # matches total, exactly at the _MAX_EVENT_LINES cap.
    assert lines == [
        "^SPX: FOMC minutes release (2024-01-03)",
        "^DJI: FOMC minutes release (2024-01-03)",
        "^DJI: Dow component earnings (2024-01-05)",
    ]
    assert len(lines) == notifications._MAX_EVENT_LINES


def test_event_lines_empty_without_matches(analysis: dict[str, Any]) -> None:
    assert notifications._event_lines(analysis, []) == []


def test_build_success_payload_no_events_field_when_events_match_nothing(
    analysis: dict[str, Any],
) -> None:
    unmatched = [
        CalendarEvent("2024-01-03", "Unrelated", "earnings", ("uncovered",), (), "s")
    ]
    payload = notifications.build_success_payload(analysis, events=unmatched)
    texts = _field_texts(payload)
    assert not any("📅 Events" in t for t in texts)


def test_build_success_payload_includes_events_field(
    analysis: dict[str, Any],
) -> None:
    events = load_calendar_events([CALENDAR])
    payload = notifications.build_success_payload(analysis, events=events)
    texts = _field_texts(payload)
    assert any("📅 Events" in t for t in texts)
    assert any("FOMC minutes release" in t for t in texts)


def test_build_success_payload_no_events_field_when_no_matches(
    analysis: dict[str, Any],
) -> None:
    payload = notifications.build_success_payload(analysis, events=[])
    texts = _field_texts(payload)
    assert not any("📅 Events" in t for t in texts)


# ── qualitative summary ──────────────────────────────────────────────────────


def test_qualitative_summary_counts_stances(qualitative: dict[str, Any]) -> None:
    summary = notifications._qualitative_summary(qualitative)
    assert "supportive" in summary
    assert "neutral" in summary
    assert "conflicting" in summary


def test_qualitative_summary_reports_gated_count(qualitative: dict[str, Any]) -> None:
    qualitative["instruments"][0]["qualitative_gates"] = ["direction_inconsistent"]
    summary = notifications._qualitative_summary(qualitative)
    assert "1 gated" in summary


def test_qualitative_summary_ignores_unknown_ungated_stance() -> None:
    artifact = {
        "instruments": [{"stance": "unknown", "qualitative_gates": []}],
    }
    summary = notifications._qualitative_summary(artifact)
    assert summary == "0 supportive / 0 neutral / 0 conflicting"


def test_qualitative_summary_withheld() -> None:
    withheld = _load(QUALITATIVE_WITHHELD)
    summary = notifications._qualitative_summary(withheld)
    assert summary.startswith("withheld by gates (")
    assert "numeric_claim_mismatch" in summary


def test_build_success_payload_includes_qualitative_summary(
    analysis: dict[str, Any], qualitative: dict[str, Any]
) -> None:
    payload = notifications.build_success_payload(analysis, qualitative=qualitative)
    texts = _field_texts(payload)
    assert any("AI commentary" in t and "supportive" in t for t in texts)


def test_build_success_payload_includes_qualitative_failure_warning(
    analysis: dict[str, Any],
) -> None:
    payload = notifications.build_success_payload(analysis, qualitative_failed=True)
    texts = _field_texts(payload)
    assert any("step failed" in t for t in texts)


def test_build_success_payload_no_qualitative_fields_by_default(
    analysis: dict[str, Any],
) -> None:
    payload = notifications.build_success_payload(analysis)
    texts = _field_texts(payload)
    assert not any("AI commentary" in t for t in texts)


# ── CLI ──────────────────────────────────────────────────────────────────────


def test_main_success_with_calendar_and_qualitative(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("SLACK_WEBHOOK_URL", "https://hooks.slack.com/x")
    sent: dict[str, Any] = {}

    def fake_send(url: str, payload: dict[str, Any]) -> None:
        sent["url"] = url
        sent["payload"] = payload

    monkeypatch.setattr(notifications, "send_notification", fake_send)
    rc = notifications.main([
        "--artifact",
        str(ANALYSIS),
        "--calendar",
        str(CALENDAR),
        "--qualitative",
        str(QUALITATIVE),
    ])
    assert rc == 0
    texts = _field_texts(sent["payload"])
    assert any("📅 Events" in t for t in texts)
    assert any("AI commentary" in t for t in texts)


def test_main_success_with_qualitative_failed_flag(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("SLACK_WEBHOOK_URL", "https://hooks.slack.com/x")
    sent: dict[str, Any] = {}
    monkeypatch.setattr(
        notifications,
        "send_notification",
        lambda _url, payload: sent.update(payload=payload),
    )
    rc = notifications.main([
        "--artifact",
        str(ANALYSIS),
        "--qualitative-failed",
    ])
    assert rc == 0
    texts = _field_texts(sent["payload"])
    assert any("step failed" in t for t in texts)


def test_main_invalid_calendar_input(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setenv("SLACK_WEBHOOK_URL", "https://hooks.slack.com/x")
    bad_calendar = tmp_path / "bad.json"
    bad_calendar.write_text("{not json", encoding="utf-8")
    rc = notifications.main([
        "--artifact",
        str(ANALYSIS),
        "--calendar",
        str(bad_calendar),
    ])
    assert rc == 1
    assert "invalid calendar input" in capsys.readouterr().out


def test_main_missing_qualitative_file(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setenv("SLACK_WEBHOOK_URL", "https://hooks.slack.com/x")
    rc = notifications.main([
        "--artifact",
        str(ANALYSIS),
        "--qualitative",
        str(tmp_path / "missing.json"),
    ])
    assert rc == 1
    assert "invalid qualitative artifact" in capsys.readouterr().out
