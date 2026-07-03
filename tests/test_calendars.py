from __future__ import annotations

import json
from datetime import UTC, date, datetime
from pathlib import Path
from typing import TYPE_CHECKING, Any

import pytest

import aims.calendars as cal

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


def _valid_event(**overrides: Any) -> dict[str, Any]:
    event = {
        "date": "2024-01-03",
        "name": "FOMC rate decision",
        "category": "macro",
        "canonical_ids": [],
        "asset_classes": ["equity_index"],
        "source_url": "https://example.gov/schedule",
    }
    event.update(overrides)
    return event


def _valid_calendar(events: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    return {
        "version": "1.0.0",
        "metadata": {
            "generated_at": "2024-01-01T00:00:00+00:00",
            "source": "curated",
        },
        "events": events if events is not None else [_valid_event()],
    }


# ── validate_calendar ───────────────────────────────────────────────────────────


def test_validate_calendar_valid() -> None:
    assert cal.validate_calendar(_valid_calendar()) == []


def test_validate_calendar_missing_top_key() -> None:
    errors = cal.validate_calendar({"version": "1.0.0"})
    assert any("metadata" in e for e in errors)


def test_validate_calendar_wrong_version() -> None:
    data = _valid_calendar()
    data["version"] = "0.0.1"
    assert any("unsupported version" in e for e in cal.validate_calendar(data))


def test_validate_calendar_metadata_not_dict() -> None:
    data = _valid_calendar()
    data["metadata"] = []
    assert any("'metadata'" in e for e in cal.validate_calendar(data))


def test_validate_calendar_metadata_missing_key() -> None:
    data = _valid_calendar()
    del data["metadata"]["source"]
    assert any("source" in e for e in cal.validate_calendar(data))


def test_validate_calendar_events_not_list() -> None:
    data = _valid_calendar()
    data["events"] = {}
    assert any("'events'" in e for e in cal.validate_calendar(data))


def test_validate_calendar_event_not_dict() -> None:
    data = _valid_calendar(events=["bad"])
    assert any("event[0]" in e for e in cal.validate_calendar(data))


def test_validate_calendar_event_missing_key() -> None:
    event = _valid_event()
    del event["date"]
    errors = cal.validate_calendar(_valid_calendar(events=[event]))
    assert any("missing required key: 'date'" in e for e in errors)


def test_validate_calendar_bad_date() -> None:
    data = _valid_calendar(events=[_valid_event(date="2024/01/03")])
    assert any("not a YYYY-MM-DD date" in e for e in cal.validate_calendar(data))
    data = _valid_calendar(events=[_valid_event(date="2024-13-99")])
    assert any("not a YYYY-MM-DD date" in e for e in cal.validate_calendar(data))
    data = _valid_calendar(events=[_valid_event(date=20240103)])
    assert any("not a YYYY-MM-DD date" in e for e in cal.validate_calendar(data))


def test_validate_calendar_bad_category() -> None:
    data = _valid_calendar(events=[_valid_event(category="party")])
    assert any("category" in e for e in cal.validate_calendar(data))


def test_validate_calendar_bad_id_lists() -> None:
    data = _valid_calendar(events=[_valid_event(canonical_ids="spx")])
    assert any("canonical_ids" in e for e in cal.validate_calendar(data))
    data = _valid_calendar(events=[_valid_event(asset_classes=[1])])
    assert any("asset_classes" in e for e in cal.validate_calendar(data))


# ── load_calendar_events / upcoming_events ─────────────────────────────────────


def test_load_calendar_events_merges_and_sorts(tmp_path: Path) -> None:
    first = _valid_calendar(events=[_valid_event(date="2024-01-05", name="B")])
    second = _valid_calendar(
        events=[
            _valid_event(date="2024-01-03", name="Z"),
            _valid_event(date="2024-01-03", name="A"),
        ]
    )
    (tmp_path / "b.json").write_text(json.dumps(first))
    (tmp_path / "a.json").write_text(json.dumps(second))
    events = cal.load_calendar_events(tmp_path)
    assert [(e["date"], e["name"]) for e in events] == [
        ("2024-01-03", "A"),
        ("2024-01-03", "Z"),
        ("2024-01-05", "B"),
    ]


def test_load_calendar_events_invalid_file(tmp_path: Path) -> None:
    (tmp_path / "bad.json").write_text(json.dumps({"version": "1.0.0"}))
    with pytest.raises(ValueError, match="invalid calendar file"):
        cal.load_calendar_events(tmp_path)


def test_upcoming_events_window() -> None:
    events = [
        _valid_event(date="2023-12-31", name="past"),
        _valid_event(date="2024-01-01", name="today"),
        _valid_event(date="2024-01-08", name="edge"),
        _valid_event(date="2024-01-09", name="beyond"),
    ]
    upcoming = cal.upcoming_events(events, "2024-01-01", window_days=7)
    assert [e["name"] for e in upcoming] == ["today", "edge"]


# ── event_applies ───────────────────────────────────────────────────────────────


def test_event_applies_by_canonical_id() -> None:
    event = _valid_event(canonical_ids=["spx"], asset_classes=[])
    assert cal.event_applies(event, {"canonical_id": "spx"})
    assert not cal.event_applies(event, {"canonical_id": "dji"})


def test_event_applies_by_asset_class() -> None:
    event = _valid_event(canonical_ids=[], asset_classes=["commodity"])
    assert cal.event_applies(event, {"asset_class": "commodity"})
    assert not cal.event_applies(event, {"asset_class": "equity"})


def test_event_applies_missing_fields() -> None:
    assert not cal.event_applies(_valid_event(), {})
    assert not cal.event_applies(
        {"date": "2024-01-01", "name": "x"}, {"canonical_id": "spx"}
    )


# ── earnings calendar fetch ─────────────────────────────────────────────────────


def _mapping_csv(tmp_path: Path) -> Path:
    path = tmp_path / "mappings.csv"
    path.write_text(
        "canonical_id,display_name,asset_class,broker,broker_instrument_name,"
        "broker_ticker_symbol,provider,provider_symbol,provider_interval,"
        "tradable,notes\n"
        "aapl,Apple Inc.,equity,,,,yfinance,AAPL,d,true,\n"
        "spx,S&P 500,equity_index,,,,yfinance,^SPX,d,true,\n"
        "msft,Microsoft,equity,,,,yfinance,MSFT,d,true,\n"
    )
    return path


_NOW = datetime(2024, 1, 1, tzinfo=UTC)


def test_fetch_earnings_calendar(tmp_path: Path, mocker: MockerFixture) -> None:
    mocker.patch.object(
        cal,
        "_earnings_dates",
        side_effect=[
            [
                date(2024, 1, 25),
                datetime(2024, 1, 25, 21, 0, tzinfo=UTC),
                "2024-09-01T00:00:00",
                "not a date",
                12345,
                date(2023, 12, 1),
            ],
            [date(2024, 2, 10)],
        ],
    )
    calendar = cal.fetch_earnings_calendar(
        mapping_path=_mapping_csv(tmp_path),
        provider="yfinance",
        interval="d",
        now=_NOW,
    )
    assert calendar["metadata"]["source"] == "yfinance"
    events = calendar["events"]
    assert [(e["date"], e["name"]) for e in events] == [
        ("2024-01-25", "Apple Inc. earnings"),
        ("2024-02-10", "Microsoft earnings"),
    ]
    assert events[0]["canonical_ids"] == ["aapl"]
    assert cal.validate_calendar(calendar) == []


def test_fetch_earnings_calendar_provider_error(
    tmp_path: Path, mocker: MockerFixture, capsys: pytest.CaptureFixture[str]
) -> None:
    mocker.patch.object(cal, "_earnings_dates", side_effect=RuntimeError("boom"))
    calendar = cal.fetch_earnings_calendar(
        mapping_path=_mapping_csv(tmp_path),
        provider="yfinance",
        interval="d",
        now=_NOW,
    )
    assert calendar["events"] == []
    assert "earnings fetch failed" in capsys.readouterr().out


def test_earnings_dates_shapes(mocker: MockerFixture) -> None:
    ticker = mocker.MagicMock()
    ticker.calendar = {"Earnings Date": [date(2024, 1, 25)]}
    mocker.patch.object(cal.yf, "Ticker", return_value=ticker)
    assert cal._earnings_dates("AAPL") == [date(2024, 1, 25)]
    ticker.calendar = {"Dividend Date": date(2024, 1, 25)}
    assert cal._earnings_dates("AAPL") == []
    ticker.calendar = None
    assert cal._earnings_dates("AAPL") == []


def test_to_iso_date() -> None:
    assert cal._to_iso_date(datetime(2024, 1, 2, 5, tzinfo=UTC)) == "2024-01-02"
    assert cal._to_iso_date(date(2024, 1, 2)) == "2024-01-02"
    assert cal._to_iso_date("2024-01-02T00:00:00") == "2024-01-02"
    assert cal._to_iso_date("bad") is None
    assert cal._to_iso_date(42) is None


# ── main ────────────────────────────────────────────────────────────────────────


def test_main_fetch_earnings(tmp_path: Path, mocker: MockerFixture) -> None:
    mocker.patch.object(
        cal, "fetch_earnings_calendar", return_value=_valid_calendar(events=[])
    )
    output = tmp_path / "calendars" / "earnings.json"
    result = cal.main([
        "fetch-earnings",
        "--mapping",
        str(tmp_path / "m.csv"),
        "--output",
        str(output),
    ])
    assert result == 0
    assert json.loads(output.read_text())["version"] == "1.0.0"


def test_main_validate_ok(tmp_path: Path) -> None:
    path = tmp_path / "cal.json"
    path.write_text(json.dumps(_valid_calendar()))
    assert cal.main(["validate", "--input", str(path)]) == 0


def test_main_validate_errors(tmp_path: Path) -> None:
    path = tmp_path / "cal.json"
    path.write_text(json.dumps({"version": "1.0.0"}))
    assert cal.main(["validate", "--input", str(path)]) == 1


def test_main_validate_missing_file(tmp_path: Path) -> None:
    assert cal.main(["validate", "--input", str(tmp_path / "nope.json")]) == 1


def test_main_validate_bad_json(tmp_path: Path) -> None:
    path = tmp_path / "bad.json"
    path.write_text("]")
    assert cal.main(["validate", "--input", str(path)]) == 1


def test_repo_macro_events_file_is_valid() -> None:
    repo_calendar = Path(__file__).resolve().parent.parent / "data" / "calendars"
    events = cal.load_calendar_events(repo_calendar)
    assert any(e["name"] == "FOMC rate decision" for e in events)
