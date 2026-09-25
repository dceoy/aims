"""Tests for deterministic central-bank schedule ingestion."""
# ruff: noqa: E501

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from lxml import html

from aims import macro_calendar
from aims.macro_calendar import (
    BOJ_URL,
    ECB_URL,
    FED_URL,
    build_macro_calendar,
    main,
    parse_boj,
    parse_ecb,
    parse_fed,
)

if TYPE_CHECKING:
    from pathlib import Path

    from pytest_mock import MockerFixture


FED = html.fromstring("""<html><h2>2027 FOMC Meetings</h2><table>
<tr><th>January</th><td>26-27</td></tr><tr><th>March</th><td>16-17*</td></tr>
<tr><th>April</th><td>27-28</td></tr><tr><th>June</th><td>8-9*</td></tr>
<tr><th>July</th><td>27-28</td></tr><tr><th>September</th><td>14-15*</td></tr>
<tr><th>October</th><td>26-27</td></tr><tr><th>December</th><td>7-8*</td></tr>
</table></html>""")
ECB = html.fromstring("""<html><ul>
<li>Governing Council of the ECB: monetary policy meeting in Frankfurt (Day 2), followed by press conference 04/02/2027</li>
<li>Governing Council of the ECB: monetary policy meeting in Frankfurt (Day 2), followed by press conference 18/03/2027</li>
<li>Governing Council of the ECB: monetary policy meeting in Frankfurt (Day 2), followed by press conference 29/04/2027</li>
<li>Governing Council of the ECB: monetary policy meeting in Frankfurt (Day 2), followed by press conference 10/06/2027</li>
<li>Governing Council of the ECB: monetary policy meeting in Frankfurt (Day 2), followed by press conference 22/07/2027</li>
<li>Governing Council of the ECB: monetary policy meeting in Frankfurt (Day 2), followed by press conference 09/09/2027</li>
<li>Governing Council of the ECB: monetary policy meeting in Frankfurt (Day 2), followed by press conference 28/10/2027</li>
<li>Governing Council of the ECB: monetary policy meeting in Frankfurt (Day 2), followed by press conference 16/12/2027</li>
</ul></html>""")
BOJ = html.fromstring("""<html><h2>2027</h2><table>
<tr><th>Date of MPM</th></tr><tr><td>Jan. 21 (Thurs.), 22 (Fri.)</td></tr>
<tr><td>Mar. 17 (Wed.), 18 (Thurs.)</td></tr><tr><td>Apr. 27 (Tues.), 28 (Wed.)</td></tr>
<tr><td>June 10 (Thurs.), 11 (Fri.)</td></tr><tr><td>July 21 (Wed.), 22 (Thurs.)</td></tr>
<tr><td>Sept. 21 (Tues.), 22 (Wed.)</td></tr><tr><td>Oct. 28 (Thurs.), 29 (Fri.)</td></tr>
<tr><td>Dec. 16 (Thurs.), 17 (Fri.)</td></tr></table></html>""")
BOJ_FIVE = html.fromstring("""<html><h2>2026</h2><table>
<tr><td>May 27 (Wed.), 28 (Thurs.)</td></tr>
<tr><td>June 15 (Mon.), 16 (Tues.)</td></tr>
<tr><td>July 30 (Thurs.), 31 (Fri.)</td></tr>
<tr><td>Sept. 17 (Thurs.), 18 (Fri.)</td></tr>
<tr><td>Oct. 29 (Thurs.), 30 (Fri.)</td></tr></table></html>""")


def test_parse_fed_handles_cross_month_labels_and_year_rollover() -> None:
    root = html.fromstring(
        """<html><h2>2027 FOMC Meetings</h2><table>
        <tr><th>Apr/May</th><td>30-1</td></tr>
        <tr><th>Jan/Feb</th><td>31-1</td></tr>
        <tr><th>Dec/Jan</th><td>31-1</td></tr>
        <tr><th>February</th><td>30-31</td></tr>
        </table></html>"""
    )
    assert [event["date"] for event in parse_fed(root)] == [
        "2027-05-01",
        "2027-02-01",
        "2028-01-01",
    ]


def test_parse_fed_uses_final_day_and_tags_assets() -> None:
    events = parse_fed(FED)
    assert len(events) == 8
    assert events[0]["date"] == "2027-01-27"
    assert events[0]["asset_classes"] == ["equity_index", "equity", "commodity"]
    assert events[0]["source"] == FED_URL
    assert (
        parse_fed(
            html.fromstring("<h4>2027 FOMC Meetings</h4><p>January</p><p>TBD</p>")
        )
        == []
    )
    intro = html.fromstring(
        "<p>January</p><p>26-27</p><h4>2027 FOMC Meetings</h4>"
        "<p>January</p><p>26-27</p>"
    )
    assert [event["date"] for event in parse_fed(intro)] == ["2027-01-27"]


def test_parse_ecb_uses_day_two_and_ignores_nondecision_days() -> None:
    root = ECB
    assert len(parse_ecb(root)) == 8
    assert parse_ecb(root)[0]["date"] == "2027-02-04"
    assert parse_ecb(html.fromstring("<p>non-monetary event</p>")) == []
    assert (
        parse_ecb(
            html.fromstring(
                "<li>Day 2 press conference 31/02/2027 monetary policy meeting</li>"
            )
        )
        == []
    )
    assert parse_ecb(
        html.fromstring(
            "<li>Day 2 press conference 10/06/2027 monetary policy meeting</li>"
        )
    )[0]["canonical_ids"] == ["cac", "dax", "stoxx50"]
    assert parse_ecb(root)[0]["source"] == ECB_URL
    duplicate = html.fromstring(
        "<div>10/06/2027</div><p>Governing Council monetary policy meeting "
        "(Day 2), followed by press conference</p><p>10/06/2027 "
        "monetary policy meeting (Day 2), followed by press conference</p>"
    )
    assert len(parse_ecb(duplicate)) == 1
    multiple_dates = html.fromstring(
        "<p>10/06/2027 22/07/2027 monetary policy meeting (Day 2), "
        "followed by press conference</p>"
    )
    assert parse_ecb(multiple_dates) == []


def test_parse_boj_uses_last_day_and_skips_headers() -> None:
    events = parse_boj(BOJ)
    assert len(events) == 8
    assert events[0]["date"] == "2027-01-22"
    assert events[0]["canonical_ids"] == ["mufg", "nkx", "sony", "toyota"]
    assert events[0]["source"] == BOJ_URL
    assert (
        parse_boj(
            html.fromstring("<h2>2027</h2><table><tr><th>header</th></tr></table>")
        )
        == []
    )
    invalid = html.fromstring(
        "<h2>2027</h2><table><tr><td>Feb. 30 (Wed.), 31 (Thurs.)</td></tr>"
        "<tr><td></td></tr><tr><td>Jan. 21 (Thurs.), 22 (Fri.)</td></tr></table>"
    )
    assert parse_boj(invalid) == []
    assert parse_boj(html.fromstring("<h2>not a year</h2>")) == []
    assert parse_boj(html.fromstring("<h2>2027</h2><p>no schedule published</p>")) == []
    empty_row = html.fromstring(
        "<h2>2027</h2><table><tr></tr><tr><td>bad date</td></tr></table>"
    )
    assert parse_boj(empty_row) == []


def test_build_macro_calendar_filters_past_and_guards_empty_source() -> None:
    calendar = build_macro_calendar(
        FED, ECB, BOJ, updated_at="2026-09-24", start_date="2026-09-24"
    )
    assert len(calendar["events"]) == 24
    assert calendar["events"][0]["date"] == "2027-01-22"
    assert calendar["metadata"]["updated_at"] == "2026-09-24"
    with pytest.raises(ValueError, match="fed returned"):
        build_macro_calendar(
            html.fromstring("<html></html>"),
            ECB,
            BOJ,
            updated_at="2026-09-24",
            start_date="2026-09-24",
        )


def test_build_macro_calendar_preserves_future_macro_releases() -> None:
    future_release = {
        "date": "2027-03-01",
        "title": "US CPI release",
        "category": "macro_release",
        "canonical_ids": ["spy"],
        "asset_classes": ["equity"],
        "source": "https://example.test/cpi",
    }
    past_release = {
        **future_release,
        "date": "2026-09-23",
        "title": "Past CPI release",
    }
    calendar = build_macro_calendar(
        FED,
        ECB,
        BOJ,
        updated_at="2026-09-24",
        start_date="2026-09-24",
        previous={"events": [future_release, past_release]},
    )
    assert future_release in calendar["events"]
    assert past_release not in calendar["events"]


def test_build_macro_calendar_protects_against_anomalous_drop() -> None:
    previous = {
        "events": [
            {"date": f"2027-{month:02d}-01", "source": FED_URL}
            for month in range(1, 13)
        ]
        * 2
    }
    with pytest.raises(ValueError, match="fed returned"):
        build_macro_calendar(
            FED,
            ECB,
            BOJ,
            updated_at="2026-09-24",
            start_date="2026-09-24",
            previous=previous,
        )


def test_build_macro_calendar_allows_small_schedule_from_prior_count() -> None:
    previous = {
        "events": [
            {"date": f"2026-{month:02d}-15", "source": BOJ_URL}
            for month in (5, 6, 7, 9, 10)
        ]
    }
    calendar = build_macro_calendar(
        FED,
        ECB,
        BOJ_FIVE,
        updated_at="2026-04-20",
        start_date="2026-04-20",
        previous=previous,
    )
    assert sum(event["source"] == BOJ_URL for event in calendar["events"]) == 5


def test_main_keeps_output_when_source_fetch_fails(
    tmp_path: Path, mocker: MockerFixture, capsys: pytest.CaptureFixture[str]
) -> None:
    output = tmp_path / "macro.json"
    output.write_text('{"events": []}', encoding="utf-8")
    mocker.patch("aims.macro_calendar._page", side_effect=OSError("offline"))
    assert main(["--output", str(output)]) == 1
    assert "leaving" in capsys.readouterr().out
    assert output.read_text(encoding="utf-8") == '{"events": []}'


def test_main_refreshes_calendar(
    tmp_path: Path, mocker: MockerFixture, capsys: pytest.CaptureFixture[str]
) -> None:
    output = tmp_path / "macro.json"
    mocker.patch("aims.macro_calendar._page", side_effect=[FED, ECB, BOJ])
    assert (
        main([
            "--output",
            str(output),
            "--updated-at",
            "2026-09-24",
            "--start-date",
            "2026-09-24",
        ])
        == 0
    )
    assert len(__import__("json").loads(output.read_text())["events"]) == 24
    assert "24 events" in capsys.readouterr().out


def test_main_uses_current_dates_by_default(
    tmp_path: Path, mocker: MockerFixture
) -> None:
    output = tmp_path / "macro.json"
    mocker.patch("aims.macro_calendar._page", side_effect=[FED, ECB, BOJ])
    assert main(["--output", str(output)]) == 0


def test_page_downloads_and_parses_html(mocker: MockerFixture) -> None:
    response = mocker.MagicMock()
    response.__enter__.return_value.read.return_value = (
        b"<html><body>page</body></html>"
    )
    opener = mocker.patch(
        "aims.macro_calendar.urllib.request.urlopen", return_value=response
    )
    root = macro_calendar._page("https://example.test")
    assert root.tag == "html"
    opener.assert_called_once()
