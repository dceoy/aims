"""Tests for the calendar (#91) and AI-commentary (#94) additions to reports."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from aims import reports
from aims.calendars import CalendarEvent, load_calendar_events

FIXTURES = Path(__file__).resolve().parent / "fixtures"
GOLDEN = Path(__file__).resolve().parent / "golden"
ANALYSIS = FIXTURES / "analysis_2024-01-01_mapped.json"
EVIDENCE = FIXTURES / "evidence_2024-01-01.json"
CALENDAR = FIXTURES / "calendar_2024.json"
QUALITATIVE = FIXTURES / "qualitative_2024-01-01.json"
QUALITATIVE_GATED = FIXTURES / "qualitative_2024-01-01_gated.json"
QUALITATIVE_WITHHELD = FIXTURES / "qualitative_2024-01-01_withheld.json"


def _load(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as fh:
        value: dict[str, Any] = json.load(fh)
    return value


@pytest.fixture
def analysis() -> dict[str, Any]:
    return _load(ANALYSIS)


@pytest.fixture
def evidence() -> dict[str, Any]:
    return _load(EVIDENCE)


@pytest.fixture
def qualitative() -> dict[str, Any]:
    return _load(QUALITATIVE)


@pytest.fixture
def calendar_events() -> list[Any]:
    return load_calendar_events([CALENDAR])


# ── golden: byte-identical / additive rendering ─────────────────────────────


def test_report_without_calendar_or_qualitative_is_unchanged() -> None:
    original = _load(FIXTURES / "analysis_2024-01-01.json")
    assert (
        reports.generate_report(original)
        == (GOLDEN / "2024-01-01-market-analysis.md").read_text()
    )


def test_report_with_events_matches_golden(
    analysis: dict[str, Any], calendar_events: list[Any]
) -> None:
    actual = reports.generate_report(analysis, calendar_events=calendar_events)
    expected = (GOLDEN / "2024-01-01-market-analysis-with-events.md").read_text()
    assert actual == expected


def test_report_with_qualitative_matches_golden(
    analysis: dict[str, Any],
    calendar_events: list[Any],
    qualitative: dict[str, Any],
    evidence: dict[str, Any],
) -> None:
    actual = reports.generate_report(
        analysis,
        calendar_events=calendar_events,
        qualitative=qualitative,
        evidence=evidence,
    )
    expected = (GOLDEN / "2024-01-01-market-analysis-with-qualitative.md").read_text()
    assert actual == expected


def test_report_partially_gated_matches_golden(
    analysis: dict[str, Any], calendar_events: list[Any], evidence: dict[str, Any]
) -> None:
    gated = _load(QUALITATIVE_GATED)
    actual = reports.generate_report(
        analysis, calendar_events=calendar_events, qualitative=gated, evidence=evidence
    )
    expected = (GOLDEN / "2024-01-01-market-analysis-partially-gated.md").read_text()
    assert actual == expected


def test_report_withheld_qualitative_is_byte_identical_to_no_qualitative(
    analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    withheld = _load(QUALITATIVE_WITHHELD)
    plain = reports.generate_report(analysis)
    with_withheld = reports.generate_report(
        analysis, qualitative=withheld, evidence=evidence
    )
    assert plain == with_withheld
    assert "ai_commentary = true" not in with_withheld


def test_report_with_qualitative_sets_front_matter_flag(
    analysis: dict[str, Any], qualitative: dict[str, Any], evidence: dict[str, Any]
) -> None:
    report = reports.generate_report(
        analysis, qualitative=qualitative, evidence=evidence
    )
    assert "ai_commentary = true" in report
    assert "data/qualitative/2024-01-01.json" in report
    assert "data/evidence/2024-01-01.json" in report


def test_report_without_qualitative_omits_front_matter_flag(
    analysis: dict[str, Any],
) -> None:
    report = reports.generate_report(analysis)
    assert "ai_commentary" not in report


# ── Upcoming Events section ─────────────────────────────────────────────────


def test_upcoming_events_section_lists_only_matched_events(
    analysis: dict[str, Any], calendar_events: list[Any]
) -> None:
    report = reports.generate_report(analysis, calendar_events=calendar_events)
    assert "## Upcoming Events" in report
    assert "FOMC minutes release" in report
    assert "Dow component earnings" in report
    assert "Far-future central bank meeting" not in report
    assert "Past macro release" not in report


def test_upcoming_events_section_empty_state(analysis: dict[str, Any]) -> None:
    report = reports.generate_report(analysis, calendar_events=[])
    assert "No scheduled events for covered instruments" in report


def test_top_opportunities_flags_upcoming_events(
    analysis: dict[str, Any], calendar_events: list[Any]
) -> None:
    report = reports.generate_report(analysis, calendar_events=calendar_events)
    top_section = report.split("## Upcoming Events")[0]
    assert "⚠️ Upcoming: FOMC minutes release (2024-01-03)" in top_section


def test_upcoming_events_section_skips_events_for_uncovered_instruments(
    analysis: dict[str, Any],
) -> None:
    # Tags a canonical_id absent from the current analysis universe and
    # carries no asset_classes, so it resolves to an empty scope and is
    # dropped from the rendered table entirely.
    unmatched = CalendarEvent(
        "2024-01-03", "Unrelated earnings", "earnings", ("uncovered",), (), "s"
    )
    matched = CalendarEvent(
        "2024-01-03", "FOMC minutes release", "central_bank", (), ("equity_index",), "s"
    )
    report = reports.generate_report(analysis, calendar_events=[unmatched, matched])
    assert "Unrelated earnings" not in report
    assert "FOMC minutes release" in report


def test_top_opportunities_without_events_arg_has_no_flags(
    analysis: dict[str, Any],
) -> None:
    report = reports.generate_report(analysis)
    assert "⚠️ Upcoming" not in report
    assert "## Upcoming Events" not in report


# ── AI Market Commentary section ────────────────────────────────────────────


def test_ai_commentary_section_present_and_labeled(
    analysis: dict[str, Any], qualitative: dict[str, Any], evidence: dict[str, Any]
) -> None:
    report = reports.generate_report(
        analysis, qualitative=qualitative, evidence=evidence
    )
    assert "## AI Market Commentary" in report
    assert "AI-generated section" in report
    assert "claude-opus-4-8" in report
    assert "prompt v1.0.0" in report


def test_ai_commentary_renders_citations_and_sources(
    analysis: dict[str, Any], qualitative: dict[str, Any], evidence: dict[str, Any]
) -> None:
    report = reports.generate_report(
        analysis, qualitative=qualitative, evidence=evidence
    )
    assert "[1]" in report
    assert "### Sources" in report
    assert "https://news.example.com/us-stocks-extend-rally" in report


def test_ai_commentary_without_evidence_falls_back_to_bare_ids(
    analysis: dict[str, Any], qualitative: dict[str, Any]
) -> None:
    report = reports.generate_report(analysis, qualitative=qualitative, evidence=None)
    assert "### Sources" in report
    # Falls back to the bare evidence ID when the source item can't be resolved.
    assert qualitative["market"]["citations"][0] in report


def test_ai_commentary_shows_gated_note_for_excluded_instrument(
    analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    gated = _load(QUALITATIVE_GATED)
    report = reports.generate_report(analysis, qualitative=gated, evidence=evidence)
    assert "withheld by consistency gates" in report
    assert "direction_inconsistent" in report


def test_ai_commentary_no_themes_omits_recurring_themes_block(
    analysis: dict[str, Any], qualitative: dict[str, Any], evidence: dict[str, Any]
) -> None:
    qualitative["market"]["themes"] = []
    report = reports.generate_report(
        analysis, qualitative=qualitative, evidence=evidence
    )
    assert "Recurring themes" not in report


def test_ai_commentary_no_citations_anywhere_omits_sources_section() -> None:
    minimal = {
        "metadata": {"model_id": "m", "prompt_version": "1"},
        "market": {"narrative": "No citations here.", "citations": [], "themes": []},
        "instruments": [],
    }
    section = reports._section_ai_commentary(minimal, None, [])
    assert "### Sources" not in section


def test_ai_commentary_omits_market_narrative_when_withheld(
    analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    withheld = _load(QUALITATIVE_WITHHELD)
    report = reports.generate_report(analysis, qualitative=withheld, evidence=evidence)
    assert "## AI Market Commentary" not in report


# ── generate_and_save wiring ─────────────────────────────────────────────────


def test_generate_and_save_renders_qualitative_and_events(tmp_path: Path) -> None:
    output_path = reports.generate_and_save(
        ANALYSIS,
        tmp_path,
        calendar_paths=[CALENDAR],
        qualitative_path=QUALITATIVE,
        evidence_path=EVIDENCE,
    )
    content = output_path.read_text()
    assert "## AI Market Commentary" in content
    assert "## Upcoming Events" in content


def test_generate_and_save_without_optional_inputs_matches_plain_report(
    tmp_path: Path,
) -> None:
    output_path = reports.generate_and_save(
        FIXTURES / "analysis_2024-01-01.json", tmp_path
    )
    assert (
        output_path.read_text()
        == (GOLDEN / "2024-01-01-market-analysis.md").read_text()
    )


# ── CLI ─────────────────────────────────────────────────────────────────────


def test_main_requires_evidence_with_qualitative(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    rc = reports.main([
        "--input",
        str(ANALYSIS),
        "--qualitative",
        str(QUALITATIVE),
        "--output",
        str(tmp_path),
    ])
    assert rc == 1
    assert "--qualitative requires --evidence" in capsys.readouterr().out


def test_main_with_qualitative_and_evidence(tmp_path: Path) -> None:
    rc = reports.main([
        "--input",
        str(ANALYSIS),
        "--qualitative",
        str(QUALITATIVE),
        "--evidence",
        str(EVIDENCE),
        "--calendar",
        str(CALENDAR),
        "--output",
        str(tmp_path),
    ])
    assert rc == 0
    output = tmp_path / "2024-01-01-market-analysis.md"
    assert "## AI Market Commentary" in output.read_text()


def test_main_file_not_found_reports_filename(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    rc = reports.main([
        "--input",
        str(tmp_path / "missing.json"),
        "--output",
        str(tmp_path),
    ])
    assert rc == 1
    assert "missing.json" in capsys.readouterr().out
