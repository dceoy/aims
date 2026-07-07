r"""Earnings and macro-event calendars for AIMS reports and notifications.

Calendars are versioned, schema-validated JSON files under ``data/calendars/``:
``macro_events.json`` is maintained by hand from officially published yearly
schedules (see OPERATIONS.md), while ``earnings.json`` is refreshed from
yfinance earnings dates by the updater CLI in this module.

Usage:
    uv run .agents/skills/qualitative-analysis/scripts/update_calendars.py \
        --mapping data/mappings/canonical_instrument_mappings.csv \
        --output data/calendars/earnings.json
"""

from __future__ import annotations

import argparse
import csv
import json
from collections.abc import Callable
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from operator import itemgetter
from pathlib import Path
from typing import TYPE_CHECKING, Any, Final

if TYPE_CHECKING:
    from aims.market_analysis import InstrumentMappingRow

CALENDAR_VERSION: Final[str] = "1.0.0"
DEFAULT_WINDOW_DAYS: Final[int] = 7
DEFAULT_EARNINGS_HORIZON_DAYS: Final[int] = 120

CATEGORY_EARNINGS: Final[str] = "earnings"
EVENT_CATEGORIES: Final[frozenset[str]] = frozenset({
    "central_bank",
    "macro_release",
    "earnings",
})

_DEFAULT_EARNINGS_OUTPUT: Final[Path] = Path("data/calendars/earnings.json")
_EARNINGS_FETCH_LIMIT: Final[int] = 12

FetchEarnings = Callable[[str], list[str]]


@dataclass(frozen=True)
class CalendarEvent:
    """One scheduled event tagged to instruments or asset classes."""

    date: str
    title: str
    category: str
    canonical_ids: tuple[str, ...]
    asset_classes: tuple[str, ...]
    source: str


def _event_from_dict(raw: dict[str, Any]) -> CalendarEvent:
    return CalendarEvent(
        date=str(raw.get("date", "")),
        title=str(raw.get("title", "")),
        category=str(raw.get("category", "")),
        canonical_ids=tuple(str(c) for c in raw.get("canonical_ids", [])),
        asset_classes=tuple(str(a) for a in raw.get("asset_classes", [])),
        source=str(raw.get("source", "")),
    )


def load_calendar_events(paths: list[Path]) -> list[CalendarEvent]:
    """Load and merge events from calendar JSON files, sorted by date."""
    events: list[CalendarEvent] = []
    for path in paths:
        with path.open(encoding="utf-8") as fh:
            data: dict[str, Any] = json.load(fh)
        events.extend(_event_from_dict(raw) for raw in data.get("events", []))
    return sorted(events, key=lambda e: (e.date, e.title, e.canonical_ids))


def upcoming_events(
    events: list[CalendarEvent],
    analysis_date: str,
    window_days: int = DEFAULT_WINDOW_DAYS,
) -> list[CalendarEvent]:
    """Return events strictly after *analysis_date* within *window_days*."""
    start = datetime.fromisoformat(f"{analysis_date}T00:00:00+00:00")
    end = start + timedelta(days=window_days)
    return [
        event
        for event in events
        if start < datetime.fromisoformat(f"{event.date}T00:00:00+00:00") <= end
    ]


def events_for_instrument(
    events: list[CalendarEvent],
    canonical_id: str,
    asset_class: str,
) -> list[CalendarEvent]:
    """Return events tagged to *canonical_id* or its *asset_class*."""
    return [
        event
        for event in events
        if canonical_id in event.canonical_ids or asset_class in event.asset_classes
    ]


def fetch_earnings_dates(symbol: str) -> list[str]:
    """Fetch upcoming/recent earnings dates via yfinance (network boundary)."""
    # Imported lazily so report generation, which imports this module for
    # calendar rendering, does not pay the yfinance import.
    import yfinance as yf  # noqa: PLC0415

    frame = yf.Ticker(symbol).get_earnings_dates(limit=_EARNINGS_FETCH_LIMIT)
    if frame is None:
        return []
    return sorted({ts.date().isoformat() for ts in frame.index})


def build_earnings_calendar(
    equities: list[tuple[str, str]],
    *,
    start_date: str,
    horizon_days: int = DEFAULT_EARNINGS_HORIZON_DAYS,
    updated_at: str | None = None,
    fetch_fn: FetchEarnings = fetch_earnings_dates,
) -> tuple[dict[str, Any], list[tuple[str, str]]]:
    """Build the earnings calendar for (canonical_id, symbol) *equities*.

    Returns the calendar dict and a list of (symbol, error message) pairs
    for fetches that failed, so callers can surface the root cause.
    Only dates within (start_date, start_date + horizon_days] are kept —
    the calendar records known future events, not history.
    """
    start = datetime.fromisoformat(f"{start_date}T00:00:00+00:00")
    end = start + timedelta(days=horizon_days)
    events: list[dict[str, Any]] = []
    failed: list[tuple[str, str]] = []
    for canonical_id, symbol in sorted(equities):
        try:
            dates = fetch_fn(symbol)
        except Exception as exc:  # noqa: BLE001 - per-symbol failures are non-fatal
            failed.append((symbol, f"{type(exc).__name__}: {exc}"))
            continue
        events.extend(
            {
                "date": date_str,
                "title": f"{symbol} earnings release",
                "category": CATEGORY_EARNINGS,
                "canonical_ids": [canonical_id],
                "asset_classes": [],
                "source": "yfinance",
            }
            for date_str in dates
            if start < datetime.fromisoformat(f"{date_str}T00:00:00+00:00") <= end
        )
    events.sort(key=itemgetter("date", "title"))
    calendar = {
        "version": CALENDAR_VERSION,
        "metadata": {
            "calendar_id": "earnings",
            "updated_at": updated_at or datetime.now(tz=UTC).date().isoformat(),
            "source": "yfinance get_earnings_dates via update_calendars.py",
        },
        "events": events,
    }
    return calendar, failed


def equities_from_mappings(
    rows: list[InstrumentMappingRow],
    provider: str,
    interval: str,
) -> list[tuple[str, str]]:
    """Return (canonical_id, symbol) pairs for equity mapping rows."""
    result: dict[str, str] = {}
    for row in rows:
        if (
            row.provider == provider
            and row.provider_interval == interval
            and row.asset_class == "equity"
            and row.canonical_id not in result
        ):
            result[row.canonical_id] = row.provider_symbol
    return sorted(result.items())


def save_calendar(calendar: dict[str, Any], path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(calendar, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return path


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mapping",
        type=Path,
        default=Path("data/mappings/canonical_instrument_mappings.csv"),
        help="Path to canonical_instrument_mappings.csv",
    )
    parser.add_argument("--provider", default="yfinance")
    parser.add_argument("--interval", default="d", choices=["d", "w", "m"])
    parser.add_argument(
        "--start-date",
        default=None,
        help="Horizon start date (YYYY-MM-DD; default: today UTC)",
    )
    parser.add_argument(
        "--horizon-days", type=int, default=DEFAULT_EARNINGS_HORIZON_DAYS
    )
    parser.add_argument(
        "--updated-at",
        default=None,
        help="Override the updated_at date (for reproducible tests)",
    )
    parser.add_argument("--output", type=Path, default=_DEFAULT_EARNINGS_OUTPUT)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    from aims.market_analysis import load_instrument_mappings  # noqa: PLC0415

    try:
        rows = load_instrument_mappings(args.mapping)
    except (FileNotFoundError, csv.Error) as exc:
        print(f"ERROR: {exc}")
        return 1
    equities = equities_from_mappings(rows, args.provider, args.interval)
    if not equities:
        print(
            f"ERROR: no equity instruments in {args.mapping} for"
            f" provider={args.provider} interval={args.interval}"
        )
        return 1
    start_date = args.start_date or datetime.now(tz=UTC).date().isoformat()
    calendar, failed = build_earnings_calendar(
        equities,
        start_date=start_date,
        horizon_days=args.horizon_days,
        updated_at=args.updated_at,
    )
    for symbol, message in failed:
        print(f"WARNING: earnings fetch failed for {symbol}: {message}")
    if len(failed) == len(equities):
        # A calendar with zero fetched symbols means the fetch path itself is
        # broken (e.g. a missing dependency); keep the committed calendar
        # instead of silently overwriting it with an empty one.
        print(
            f"ERROR: all {len(equities)} earnings fetches failed;"
            f" leaving {args.output} untouched"
        )
        return 1
    path = save_calendar(calendar, args.output)
    print(
        f"Earnings calendar written to {path}"
        f" ({len(calendar['events'])} events, {len(failed)} failed symbol(s))"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
