r"""Maintain and query scheduled-event calendars (earnings and macro events).

Calendar files under data/calendars/ hold known-in-advance events: the curated
macro schedule (macro_events.json, maintained from officially published
schedules) and the generated earnings calendar (earnings.json, fetched via
yfinance for equity mapping rows). Both share data/schema/calendar.schema.json.

Usage:
    uv run .agents/skills/qualitative-analysis/scripts/update_calendars.py \
        fetch-earnings --mapping data/mappings/canonical_instrument_mappings.csv \
        --provider yfinance --interval d --output data/calendars/earnings.json

    uv run .agents/skills/qualitative-analysis/scripts/update_calendars.py \
        validate --input data/calendars/macro_events.json
"""

from __future__ import annotations

import argparse
import json
from datetime import UTC, date, datetime, timedelta
from pathlib import Path
from typing import Any, Final

import yfinance as yf

from aims.market_analysis import instrument_display_map, load_instrument_mappings

CALENDAR_VERSION: Final[str] = "1.0.0"
DEFAULT_CALENDAR_DIR: Final[Path] = Path("data/calendars")
DEFAULT_WINDOW_DAYS: Final[int] = 7
DEFAULT_EARNINGS_HORIZON_DAYS: Final[int] = 120

_CATEGORIES: Final[tuple[str, ...]] = ("macro", "earnings")
_REQUIRED_TOP: Final[tuple[str, ...]] = ("version", "metadata", "events")
_REQUIRED_META: Final[tuple[str, ...]] = ("generated_at", "source")
_REQUIRED_EVENT: Final[tuple[str, ...]] = (
    "date",
    "name",
    "category",
    "canonical_ids",
    "asset_classes",
    "source_url",
)
_DATE_LEN: Final[int] = 10


def _is_iso_date(value: Any) -> bool:
    if not isinstance(value, str) or len(value) != _DATE_LEN:
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def validate_calendar(data: dict[str, Any]) -> list[str]:
    """Return a list of schema errors for a calendar file (empty when valid)."""
    errors = [
        f"missing required key: {key!r}" for key in _REQUIRED_TOP if key not in data
    ]
    if errors:
        return errors
    if data["version"] != CALENDAR_VERSION:
        errors.append(
            f"unsupported version {data['version']!r} (expected {CALENDAR_VERSION!r})"
        )
    metadata = data["metadata"]
    if not isinstance(metadata, dict):
        errors.append("'metadata' must be a JSON object")
    else:
        errors.extend(
            f"metadata missing required key: {key!r}"
            for key in _REQUIRED_META
            if key not in metadata
        )
    events = data["events"]
    if not isinstance(events, list):
        errors.append("'events' must be a JSON array")
        return errors
    for idx, event in enumerate(events):
        if not isinstance(event, dict):
            errors.append(f"event[{idx}] must be a JSON object")
            continue
        errors.extend(
            f"event[{idx}] missing required key: {key!r}"
            for key in _REQUIRED_EVENT
            if key not in event
        )
        if "date" in event and not _is_iso_date(event.get("date")):
            errors.append(
                f"event[{idx}]: date {event.get('date')!r} is not a YYYY-MM-DD date"
            )
        if "category" in event and event.get("category") not in _CATEGORIES:
            errors.append(
                f"event[{idx}]: category {event.get('category')!r} not in {_CATEGORIES}"
            )
        for key in ("canonical_ids", "asset_classes"):
            value = event.get(key)
            if key in event and (
                not isinstance(value, list)
                or any(not isinstance(v, str) for v in value)
            ):
                errors.append(f"event[{idx}]: {key} must be an array of strings")
    return errors


def load_calendar_events(calendar_dir: Path) -> list[dict[str, Any]]:
    """Load and merge events from every calendar JSON file in *calendar_dir*.

    Raises ValueError when any file fails schema validation.
    """
    events: list[dict[str, Any]] = []
    for path in sorted(calendar_dir.glob("*.json")):
        with path.open(encoding="utf-8") as fh:
            data = json.load(fh)
        errors = validate_calendar(data)
        if errors:
            msg = f"invalid calendar file {path}: {errors[0]}"
            raise ValueError(msg)
        events.extend(data["events"])
    events.sort(key=lambda e: (str(e["date"]), str(e["name"])))
    return events


def upcoming_events(
    events: list[dict[str, Any]],
    analysis_date: str,
    window_days: int = DEFAULT_WINDOW_DAYS,
) -> list[dict[str, Any]]:
    """Return events dated within [analysis_date, analysis_date + window_days]."""
    start = date.fromisoformat(analysis_date)
    end = (start + timedelta(days=window_days)).isoformat()
    return [e for e in events if analysis_date <= str(e["date"]) <= end]


def event_applies(event: dict[str, Any], instrument: dict[str, Any]) -> bool:
    """Return True when *event* applies to an analysis artifact instrument."""
    canonical_id = instrument.get("canonical_id")
    asset_class = instrument.get("asset_class")
    canonical_ids = event.get("canonical_ids") or []
    asset_classes = event.get("asset_classes") or []
    return (canonical_id is not None and canonical_id in canonical_ids) or (
        asset_class is not None and asset_class in asset_classes
    )


def _earnings_dates(symbol: str) -> list[Any]:
    calendar: Any = yf.Ticker(symbol).calendar
    if not isinstance(calendar, dict):
        return []
    dates = calendar.get("Earnings Date")
    return dates if isinstance(dates, list) else []


def _to_iso_date(value: Any) -> str | None:
    if isinstance(value, datetime):
        return value.date().isoformat()
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, str) and _is_iso_date(value[:_DATE_LEN]):
        return value[:_DATE_LEN]
    return None


def fetch_earnings_calendar(
    *,
    mapping_path: Path,
    provider: str,
    interval: str,
    horizon_days: int = DEFAULT_EARNINGS_HORIZON_DAYS,
    now: datetime | None = None,
) -> dict[str, Any]:
    """Fetch upcoming earnings dates for equity mapping rows into a calendar."""
    current = (now or datetime.now(tz=UTC)).astimezone(UTC)
    today = current.date().isoformat()
    horizon = (current.date() + timedelta(days=horizon_days)).isoformat()
    display_map = instrument_display_map(
        load_instrument_mappings(mapping_path), provider, interval
    )
    events: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for symbol in sorted(display_map):
        entry = display_map[symbol]
        if entry.get("asset_class") != "equity":
            continue
        canonical_id = entry["canonical_id"]
        try:
            raw_dates = _earnings_dates(symbol)
        except Exception as exc:  # noqa: BLE001 - provider errors are non-fatal
            print(f"WARNING: earnings fetch failed for {symbol}: {exc}")
            continue
        for raw in raw_dates:
            event_date = _to_iso_date(raw)
            if (
                event_date is None
                or not today <= event_date <= horizon
                or (canonical_id, event_date) in seen
            ):
                continue
            seen.add((canonical_id, event_date))
            events.append({
                "date": event_date,
                "name": f"{entry['display_name']} earnings",
                "category": "earnings",
                "canonical_ids": [canonical_id],
                "asset_classes": [],
                "source_url": f"https://finance.yahoo.com/quote/{symbol}",
            })
    events.sort(key=lambda e: (str(e["date"]), str(e["name"])))
    return {
        "version": CALENDAR_VERSION,
        "metadata": {
            "generated_at": current.isoformat(),
            "source": "yfinance",
        },
        "events": events,
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    fetch = sub.add_parser(
        "fetch-earnings", help="Fetch upcoming earnings dates for equity rows"
    )
    fetch.add_argument("--mapping", type=Path, required=True)
    fetch.add_argument("--provider", default="yfinance")
    fetch.add_argument("--interval", default="d")
    fetch.add_argument(
        "--horizon-days", type=int, default=DEFAULT_EARNINGS_HORIZON_DAYS
    )
    fetch.add_argument(
        "--output", type=Path, default=DEFAULT_CALENDAR_DIR / "earnings.json"
    )

    validate = sub.add_parser("validate", help="Validate a calendar file")
    validate.add_argument("--input", type=Path, required=True)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.command == "fetch-earnings":
        calendar = fetch_earnings_calendar(
            mapping_path=args.mapping,
            provider=args.provider,
            interval=args.interval,
            horizon_days=args.horizon_days,
        )
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(calendar, indent=2) + "\n", encoding="utf-8")
        print(f"Earnings calendar written to {args.output}")
        return 0
    try:
        with args.input.open(encoding="utf-8") as fh:
            data = json.load(fh)
    except FileNotFoundError:
        print(f"ERROR: file not found: {args.input}")
        return 1
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON in {args.input}: {exc}")
        return 1
    errors = validate_calendar(data)
    if errors:
        for error in errors:
            print(error)
        return 1
    print(f"validated {args.input}: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
