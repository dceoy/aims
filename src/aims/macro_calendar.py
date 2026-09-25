"""Refresh central-bank calendars from official Fed, ECB, and BOJ pages."""

from __future__ import annotations

import argparse
import json
import re
import urllib.request
from datetime import UTC, date, datetime
from operator import itemgetter
from pathlib import Path
from typing import Any, Final

from lxml import html

from aims.calendars import CALENDAR_VERSION

FED_URL: Final = "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"
ECB_URL: Final = "https://www.ecb.europa.eu/press/calendars/mgcgc/html/index.en.html"
BOJ_URL: Final = "https://www.boj.or.jp/en/mopo/mpmsche_minu/index.htm"
DEFAULT_OUTPUT: Final = Path("data/calendars/macro_events.json")
_MONTHS: Final = {
    name.lower(): number
    for number, name in enumerate(
        (
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ),
        1,
    )
}
_MONTH_ABBR: Final = {name[:3].lower(): num for name, num in _MONTHS.items()}
_BOJ_MONTH_PATTERN: Final = (
    r"Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|"
    r"Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|"
    r"Nov(?:ember)?|Dec(?:ember)?"
)
_FED_MONTH_LABEL_PATTERN: Final = re.compile(
    rf"^\s*({_BOJ_MONTH_PATTERN})(?:\s*/\s*({_BOJ_MONTH_PATTERN}))?\s*$",
    re.IGNORECASE,
)
_FED_NEXT_MEETING_PATTERN: Final = re.compile(
    rf"\btwo-day meeting is scheduled for\s+"
    rf"({_BOJ_MONTH_PATTERN})\.?\s+(\d{{1,2}})\s*[-–—]\s*"
    rf"(\d{{1,2}}),\s*(20\d{{2}})\b",
    re.IGNORECASE,
)
_ASSET_CLASSES: Final[list[str]] = ["equity_index", "equity", "commodity"]
_ECB_IDS: Final[list[str]] = ["cac", "dax", "stoxx50"]
_BOJ_IDS: Final[list[str]] = ["mufg", "nkx", "sony", "toyota"]


def _page(url: str) -> Any:
    request = urllib.request.Request(
        url, headers={"User-Agent": "AIMS calendar updater"}
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return html.fromstring(response.read())


def _text(node: Any) -> str:
    return " ".join(" ".join(node.itertext()).split())


def _year_tables(tree: Any) -> dict[int, list[Any]]:
    result: dict[int, list[Any]] = {}
    for heading in tree.xpath("//h1|//h2|//h3|//caption"):
        match = re.search(r"\b(20\d{2})\b", _text(heading))
        if match:
            year = int(match.group(1))
            following = heading.xpath("following::table[1]")
            if following:
                result[year] = following[0].xpath(".//tr")
    return result


def parse_fed(root: Any) -> list[dict[str, Any]]:
    """Extract the final day of each published FOMC meeting."""
    events = []
    year = None
    months: tuple[int, int | None] | None = None
    for fragment in root.itertext():
        label = " ".join(fragment.split())
        next_meeting_match = _FED_NEXT_MEETING_PATTERN.search(label)
        if next_meeting_match:
            event_month = _MONTH_ABBR[next_meeting_match.group(1)[:3].lower()]
            event_year = int(next_meeting_match.group(4))
            try:
                start_date = date(
                    event_year, event_month, int(next_meeting_match.group(2))
                )
                event_date = date(
                    event_year, event_month, int(next_meeting_match.group(3))
                )
            except ValueError:
                continue
            if event_date <= start_date:
                continue
            events.append(
                _event(
                    event_date,
                    "FOMC rate decision",
                    FED_URL,
                    asset_classes=_ASSET_CLASSES,
                )
            )
            continue
        year_match = re.search(r"(20\d{2})\s+FOMC Meetings", label)
        if year_match:
            year = int(year_match.group(1))
            months = None
            continue
        if year is None:
            continue
        month_match = _FED_MONTH_LABEL_PATTERN.fullmatch(label)
        if month_match:
            start_month = _MONTH_ABBR[month_match.group(1)[:3].lower()]
            end_month = (
                _MONTH_ABBR[month_match.group(2)[:3].lower()]
                if month_match.group(2)
                else None
            )
            months = (start_month, end_month)
            continue
        date_match = re.fullmatch(r"\s*(\d{1,2})\s*[-–—]\s*(\d{1,2})\s*\*?\s*", label)
        if months and date_match:
            start_month, end_month = months
            start_day, end_day = map(int, date_match.groups())
            event_month = start_month
            if end_day < start_day:
                event_month = end_month or (start_month % 12) + 1
            event_year = year + int(event_month < start_month)
            try:
                event_date = date(event_year, event_month, end_day)
            except ValueError:
                continue
            events.append(
                _event(
                    event_date,
                    "FOMC rate decision",
                    FED_URL,
                    asset_classes=_ASSET_CLASSES,
                )
            )
    return _unique(events)


def parse_ecb(root: Any) -> list[dict[str, Any]]:
    """Extract monetary policy meeting Day 2, followed by the press conference."""
    events = []
    latest_date = None
    for fragment in root.itertext():
        label = " ".join(fragment.split())
        dates = re.findall(r"(\d{2})/(\d{2})/(20\d{2})", label)
        if len(dates) == 1:
            day, month, year = map(int, dates[0])
            try:
                latest_date = date(year, month, day)
            except ValueError:
                latest_date = None
        if (
            latest_date
            and "monetary policy meeting" in label
            and "Day 2" in label
            and "press conference" in label
        ):
            events.append(
                _event(
                    latest_date,
                    "ECB monetary policy decision",
                    ECB_URL,
                    canonical_ids=_ECB_IDS,
                )
            )
    return _unique(events)


def parse_boj(root: Any) -> list[dict[str, Any]]:
    """Extract final meeting dates from the BOJ's year tables."""
    events = []
    for year, rows in sorted(_year_tables(root).items()):
        previous_month = None
        for row in rows:
            cells = row.xpath("./th|./td")
            if not cells:
                continue
            label = _text(cells[0])
            match = re.search(
                rf"\b({_BOJ_MONTH_PATTERN})\.?\s*(\d{{1,2}})[^,]*,\s*(?:({_BOJ_MONTH_PATTERN})\.?\s*)?(\d{{1,2}})\b",
                label,
            )
            if not match:
                continue
            month = _MONTH_ABBR[match.group(1)[:3].lower()]
            end_month = _MONTH_ABBR[(match.group(3) or match.group(1))[:3].lower()]
            if previous_month is not None and month < previous_month:
                continue
            previous_month = month
            try:
                event_date = date(year, end_month, int(match.group(4)))
            except ValueError:
                continue
            events.append(
                _event(
                    event_date,
                    "BOJ monetary policy decision",
                    BOJ_URL,
                    canonical_ids=_BOJ_IDS,
                )
            )
    return _unique(events)


def _event(
    event_date: date,
    title: str,
    source: str,
    *,
    canonical_ids: list[str] | None = None,
    asset_classes: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "date": event_date.isoformat(),
        "title": title,
        "category": "central_bank",
        "canonical_ids": canonical_ids or [],
        "asset_classes": asset_classes or [],
        "source": source,
    }


def _unique(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return list({(e["date"], e["title"]): e for e in events}.values())


def build_macro_calendar(
    fed_html: Any,
    ecb_html: Any,
    boj_html: Any,
    *,
    updated_at: str,
    start_date: str,
    previous: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Parse, sanity-check, and build a future-only macro calendar."""
    parsed = {
        "fed": parse_fed(fed_html),
        "ecb": parse_ecb(ecb_html),
        "boj": parse_boj(boj_html),
    }
    start = date.fromisoformat(start_date)
    for source, events in parsed.items():
        events[:] = [e for e in events if e["date"] > start.isoformat()]
        old_count = sum(
            1
            for e in (previous or {}).get("events", [])
            if e.get("source")
            == {"fed": FED_URL, "ecb": ECB_URL, "boj": BOJ_URL}[source]
            and e.get("date", "") > start.isoformat()
        )
        minimum = max(1, (old_count + 1) // 2)
        if not events or (old_count and len(events) < minimum):
            message = (
                f"{source} returned {len(events)} future events; "
                f"expected at least {minimum} based on the previous schedule"
            )
            raise ValueError(message)
    preserved_events = [
        event
        for event in (previous or {}).get("events", [])
        if event.get("category") == "macro_release"
        and event.get("date", "") > start.isoformat()
    ]
    events = sorted(
        [event for group in parsed.values() for event in group] + preserved_events,
        key=itemgetter("date", "title"),
    )
    return {
        "version": CALENDAR_VERSION,
        "metadata": {
            "calendar_id": "macro_events",
            "updated_at": updated_at,
            "source": "Official Fed, ECB, and BOJ schedules; see OPERATIONS.md",
        },
        "events": events,
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--updated-at", default=None)
    parser.add_argument("--start-date", default=None)
    parser.add_argument("--fed-url", default=FED_URL)
    parser.add_argument("--ecb-url", default=ECB_URL)
    parser.add_argument("--boj-url", default=BOJ_URL)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        old = (
            json.loads(args.output.read_text(encoding="utf-8"))
            if args.output.exists()
            else None
        )
        calendar = build_macro_calendar(
            _page(args.fed_url),
            _page(args.ecb_url),
            _page(args.boj_url),
            updated_at=args.updated_at or datetime.now(tz=UTC).date().isoformat(),
            start_date=args.start_date or datetime.now(tz=UTC).date().isoformat(),
            previous=old,
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        message = (
            f"ERROR: macro calendar refresh failed; leaving {args.output} "
            f"untouched: {exc}"
        )
        print(message)
        return 1
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(calendar, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"Macro calendar written to {args.output} ({len(calendar['events'])} events)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
