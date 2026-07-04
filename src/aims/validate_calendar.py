r"""Validate an AIMS calendar JSON file against the expected schema.

Usage:
    uv run .agents/skills/qualitative-analysis/scripts/validate_calendar.py \
        --input data/calendars/macro_events.json
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Final

from aims.calendars import CALENDAR_VERSION, EVENT_CATEGORIES

_REQUIRED_TOP: Final[tuple[str, ...]] = ("version", "metadata", "events")
_REQUIRED_META: Final[tuple[str, ...]] = ("calendar_id", "updated_at", "source")
_REQUIRED_EVENT: Final[tuple[str, ...]] = (
    "date",
    "title",
    "category",
    "canonical_ids",
    "asset_classes",
    "source",
)
_DATE_RE: Final[re.Pattern[str]] = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def _validate_event(idx: int, event: Any) -> list[str]:
    if not isinstance(event, dict):
        return [f"events[{idx}] must be a JSON object"]
    errors = [
        f"events[{idx}] missing required key: {key!r}"
        for key in _REQUIRED_EVENT
        if key not in event
    ]
    if errors:
        return errors
    if not _DATE_RE.match(str(event["date"])):
        errors.append(f"events[{idx}]: date {event['date']!r} is not a YYYY-MM-DD date")
    if not str(event["title"]).strip():
        errors.append(f"events[{idx}]: title must be a non-empty string")
    if event["category"] not in EVENT_CATEGORIES:
        allowed = ", ".join(sorted(EVENT_CATEGORIES))
        errors.append(
            f"events[{idx}]: category {event['category']!r} is not one of {allowed}"
        )
    for field in ("canonical_ids", "asset_classes"):
        value = event[field]
        if not isinstance(value, list) or any(
            not isinstance(entry, str) for entry in value
        ):
            errors.append(f"events[{idx}]: {field} must be a list of strings")
    if not event["canonical_ids"] and not event["asset_classes"]:
        errors.append(
            f"events[{idx}]: event must tag at least one canonical_id or asset_class"
        )
    return errors


def validate_calendar(data: dict[str, Any]) -> list[str]:
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
        updated_at = metadata.get("updated_at")
        if isinstance(updated_at, str) and not _DATE_RE.match(updated_at):
            errors.append(
                f"metadata.updated_at {updated_at!r} is not a YYYY-MM-DD date"
            )
    events = data["events"]
    if not isinstance(events, list):
        errors.append("'events' must be a JSON array")
        return errors
    for idx, event in enumerate(events):
        errors.extend(_validate_event(idx, event))
    return errors


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help="Path to calendar JSON file",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
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
