"""Tests for aims.calendars — earnings and macro-event calendars."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

from aims import calendars as cal
from aims.market_analysis import InstrumentMappingRow

if TYPE_CHECKING:
    from pathlib import Path

    import pytest
    from pytest_mock import MockerFixture


def _row(**overrides: str) -> InstrumentMappingRow:
    values = {
        "canonical_id": "aapl",
        "display_name": "Apple Inc.",
        "asset_class": "equity",
        "broker": "",
        "broker_instrument_name": "",
        "broker_ticker_symbol": "",
        "provider": "yfinance",
        "provider_symbol": "AAPL",
        "provider_interval": "d",
        "tradable": "true",
    }
    values.update(overrides)
    return InstrumentMappingRow(**values)


def _write_calendar(path: Path, events: list[dict[str, Any]]) -> None:
    path.write_text(
        json.dumps({
            "version": cal.CALENDAR_VERSION,
            "metadata": {
                "calendar_id": "test",
                "updated_at": "2024-01-01",
                "source": "unit-test",
            },
            "events": events,
        }),
        encoding="utf-8",
    )


# ── load / merge ─────────────────────────────────────────────────────────────


def test_load_calendar_events_merges_and_sorts(tmp_path: Path) -> None:
    a = tmp_path / "a.json"
    b = tmp_path / "b.json"
    _write_calendar(
        a,
        [
            {
                "date": "2024-01-05",
                "title": "Z event",
                "category": "macro_release",
                "canonical_ids": [],
                "asset_classes": ["equity"],
                "source": "s",
            }
        ],
    )
    _write_calendar(
        b,
        [
            {
                "date": "2024-01-02",
                "title": "A event",
                "category": "earnings",
                "canonical_ids": ["aapl"],
                "asset_classes": [],
                "source": "s",
            }
        ],
    )
    events = cal.load_calendar_events([a, b])
    assert [e.date for e in events] == ["2024-01-02", "2024-01-05"]
    assert events[0].canonical_ids == ("aapl",)


def test_event_from_dict_defaults() -> None:
    event = cal._event_from_dict({"date": "2024-01-01"})
    assert event.title == ""
    assert event.canonical_ids == ()
    assert event.asset_classes == ()


# ── windowing and matching ──────────────────────────────────────────────────


def _events() -> list[cal.CalendarEvent]:
    return [
        cal.CalendarEvent(
            "2023-12-31", "Yesterday", "macro_release", (), ("equity",), "s"
        ),
        cal.CalendarEvent("2024-01-01", "Same day", "macro_release", (), (), "s"),
        cal.CalendarEvent(
            "2024-01-03", "In window", "central_bank", (), ("equity_index",), "s"
        ),
        cal.CalendarEvent(
            "2024-01-08", "End of window", "earnings", ("aapl",), (), "s"
        ),
        cal.CalendarEvent("2024-01-09", "Past window", "earnings", ("aapl",), (), "s"),
    ]


def test_upcoming_events_window_is_exclusive_start_inclusive_end() -> None:
    events = cal.upcoming_events(_events(), "2024-01-01", window_days=7)
    assert [e.title for e in events] == ["In window", "End of window"]


def test_events_for_instrument_matches_canonical_id_or_asset_class() -> None:
    events = _events()
    matched = cal.events_for_instrument(events, "aapl", "equity")
    assert {e.title for e in matched} == {
        "Yesterday",
        "End of window",
        "Past window",
    }
    assert cal.events_for_instrument(events, "msft", "commodity") == []


# ── yfinance boundary and calendar building ─────────────────────────────────


def test_fetch_earnings_dates_deduplicates_and_sorts(mocker: MockerFixture) -> None:
    ts1 = mocker.Mock()
    ts1.date.return_value.isoformat.return_value = "2024-02-01"
    ts2 = mocker.Mock()
    ts2.date.return_value.isoformat.return_value = "2024-01-15"
    ts3 = mocker.Mock()
    ts3.date.return_value.isoformat.return_value = "2024-01-15"
    frame = mocker.Mock(index=[ts1, ts2, ts3])
    ticker = mocker.Mock()
    ticker.get_earnings_dates.return_value = frame
    mock_yf = mocker.Mock()
    mock_yf.Ticker.return_value = ticker
    mocker.patch.dict("sys.modules", {"yfinance": mock_yf})
    dates = cal.fetch_earnings_dates("AAPL")
    assert dates == ["2024-01-15", "2024-02-01"]
    ticker.get_earnings_dates.assert_called_once_with(limit=cal._EARNINGS_FETCH_LIMIT)


def test_fetch_earnings_dates_none_frame(mocker: MockerFixture) -> None:
    ticker = mocker.Mock()
    ticker.get_earnings_dates.return_value = None
    mock_yf = mocker.Mock()
    mock_yf.Ticker.return_value = ticker
    mocker.patch.dict("sys.modules", {"yfinance": mock_yf})
    assert cal.fetch_earnings_dates("AAPL") == []


def test_build_earnings_calendar_filters_horizon_and_records_failures() -> None:
    def fetch(symbol: str) -> list[str]:
        if symbol == "AAPL":
            return ["2023-12-31", "2024-01-15", "2024-06-01"]
        msg = "no data"
        raise ConnectionError(msg)

    calendar, failed = cal.build_earnings_calendar(
        [("aapl", "AAPL"), ("msft", "MSFT")],
        start_date="2024-01-01",
        horizon_days=120,
        updated_at="2024-01-01",
        fetch_fn=fetch,
    )
    assert failed == [("MSFT", "ConnectionError: no data")]
    assert [e["date"] for e in calendar["events"]] == ["2024-01-15"]
    assert calendar["events"][0]["canonical_ids"] == ["aapl"]
    assert calendar["metadata"]["updated_at"] == "2024-01-01"


def test_build_earnings_calendar_default_updated_at() -> None:
    calendar, failed = cal.build_earnings_calendar(
        [], start_date="2024-01-01", fetch_fn=lambda _symbol: []
    )
    assert failed == []
    assert calendar["metadata"]["updated_at"]


def test_equities_from_mappings_filters_and_dedupes() -> None:
    rows = [
        _row(),
        _row(provider_interval="w"),
        _row(asset_class="equity_index", canonical_id="spx", provider_symbol="^SPX"),
        _row(),
    ]
    assert cal.equities_from_mappings(rows, "yfinance", "d") == [("aapl", "AAPL")]


def test_save_calendar(tmp_path: Path) -> None:
    path = tmp_path / "nested" / "cal.json"
    calendar = {"version": cal.CALENDAR_VERSION, "events": []}
    result = cal.save_calendar(calendar, path)
    assert result == path
    assert json.loads(path.read_text())["version"] == cal.CALENDAR_VERSION


# ── CLI ─────────────────────────────────────────────────────────────────────


def test_main_missing_mapping(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    rc = cal.main(["--mapping", str(tmp_path / "missing.csv")])
    assert rc == 1
    assert "ERROR" in capsys.readouterr().out


def test_main_no_equities(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    mapping = tmp_path / "map.csv"
    mapping.write_text(
        "canonical_id,display_name,asset_class,broker,broker_instrument_name,"
        "broker_ticker_symbol,provider,provider_symbol,provider_interval,tradable\n"
        "spx,S&P 500,equity_index,,,,yfinance,^GSPC,d,true\n",
        encoding="utf-8",
    )
    rc = cal.main(["--mapping", str(mapping)])
    assert rc == 1
    assert "no equity instruments" in capsys.readouterr().out


def _write_mapping(tmp_path: Path, *symbols: str) -> Path:
    mapping = tmp_path / "map.csv"
    header = (
        "canonical_id,display_name,asset_class,broker,broker_instrument_name,"
        "broker_ticker_symbol,provider,provider_symbol,provider_interval,tradable\n"
    )
    rows = "".join(
        f"{symbol.lower()},{symbol},equity,,,,yfinance,{symbol},d,true\n"
        for symbol in symbols
    )
    mapping.write_text(header + rows, encoding="utf-8")
    return mapping


def _calendar_stub(events: list[dict[str, str]] | None = None) -> dict[str, object]:
    return {
        "version": cal.CALENDAR_VERSION,
        "metadata": {
            "calendar_id": "earnings",
            "updated_at": "2024-01-01",
            "source": "test",
        },
        "events": events or [],
    }


def test_main_success_with_partial_failure(
    tmp_path: Path, mocker: MockerFixture, capsys: pytest.CaptureFixture[str]
) -> None:
    mapping = _write_mapping(tmp_path, "AAPL", "MSFT")
    mocker.patch.object(
        cal,
        "build_earnings_calendar",
        return_value=(_calendar_stub(), [("AAPL", "ImportError: lxml missing")]),
    )
    rc = cal.main([
        "--mapping",
        str(mapping),
        "--start-date",
        "2024-01-01",
        "--output",
        str(tmp_path / "out.json"),
    ])
    out = capsys.readouterr().out
    assert rc == 0
    assert "WARNING: earnings fetch failed for AAPL: ImportError: lxml missing" in out
    assert (tmp_path / "out.json").exists()


def test_main_all_symbols_failed_exits_nonzero_without_writing(
    tmp_path: Path, mocker: MockerFixture, capsys: pytest.CaptureFixture[str]
) -> None:
    mapping = _write_mapping(tmp_path, "AAPL", "MSFT")
    mocker.patch.object(
        cal,
        "build_earnings_calendar",
        return_value=(
            _calendar_stub(),
            [
                ("AAPL", "ImportError: lxml missing"),
                ("MSFT", "ImportError: lxml missing"),
            ],
        ),
    )
    rc = cal.main([
        "--mapping",
        str(mapping),
        "--start-date",
        "2024-01-01",
        "--output",
        str(tmp_path / "out.json"),
    ])
    out = capsys.readouterr().out
    assert rc == 1
    assert "ERROR: all 2 earnings fetches failed" in out
    assert not (tmp_path / "out.json").exists()
