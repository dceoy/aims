r"""Validate an AIMS evidence bundle JSON file against the expected schema.

Usage:
    uv run .agents/skills/qualitative-analysis/scripts/validate_evidence.py \
        --input data/evidence/2026-07-04.json
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Final

from aims.evidence import (
    EVIDENCE_VERSION,
    SNIPPET_MAX_CHARS,
    TITLE_MAX_CHARS,
)

_REQUIRED_TOP: Final[tuple[str, ...]] = ("version", "metadata", "items")
_REQUIRED_META: Final[tuple[str, ...]] = (
    "generated_at",
    "analysis_date",
    "interval",
    "retrieved_at",
    "git_commit",
    "lookback_days",
    "coverage",
)
_REQUIRED_COVERAGE: Final[tuple[str, ...]] = (
    "sources",
    "instrument_count",
    "instruments_with_direct_news",
    "asset_classes",
)
_REQUIRED_ITEM: Final[tuple[str, ...]] = (
    "id",
    "title",
    "source",
    "url",
    "published_at",
    "snippet",
    "category",
    "canonical_ids",
    "asset_classes",
)
_CATEGORIES: Final[frozenset[str]] = frozenset({"instrument_news", "macro"})
_ID_RE: Final[re.Pattern[str]] = re.compile(r"^ev-[0-9a-f]{16}$")
_DATE_RE: Final[re.Pattern[str]] = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def _validate_item(idx: int, item: Any) -> list[str]:
    if not isinstance(item, dict):
        return [f"items[{idx}] must be a JSON object"]
    errors = [
        f"items[{idx}] missing required key: {key!r}"
        for key in _REQUIRED_ITEM
        if key not in item
    ]
    if errors:
        return errors
    if not _ID_RE.match(str(item["id"])):
        errors.append(f"items[{idx}]: id {item['id']!r} is not a valid evidence ID")
    if not item["title"] or len(str(item["title"])) > TITLE_MAX_CHARS:
        errors.append(f"items[{idx}]: title must be 1..{TITLE_MAX_CHARS} characters")
    if len(str(item["snippet"])) > SNIPPET_MAX_CHARS:
        errors.append(f"items[{idx}]: snippet exceeds {SNIPPET_MAX_CHARS} characters")
    if not str(item["url"]).startswith(("http://", "https://")):
        errors.append(f"items[{idx}]: url {item['url']!r} is not an HTTP(S) URL")
    if item["category"] not in _CATEGORIES:
        errors.append(f"items[{idx}]: category {item['category']!r} is not valid")
    for field in ("canonical_ids", "asset_classes"):
        value = item[field]
        if not isinstance(value, list) or any(
            not isinstance(entry, str) for entry in value
        ):
            errors.append(f"items[{idx}]: {field} must be a list of strings")
    return errors


def validate_bundle(data: dict[str, Any]) -> list[str]:
    errors = [
        f"missing required key: {key!r}" for key in _REQUIRED_TOP if key not in data
    ]
    if errors:
        return errors

    if data["version"] != EVIDENCE_VERSION:
        errors.append(
            f"unsupported version {data['version']!r} (expected {EVIDENCE_VERSION!r})"
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
        analysis_date = metadata.get("analysis_date")
        if isinstance(analysis_date, str) and not _DATE_RE.match(analysis_date):
            errors.append(
                f"metadata.analysis_date {analysis_date!r} is not a YYYY-MM-DD date"
            )
        coverage = metadata.get("coverage")
        if isinstance(coverage, dict):
            errors.extend(
                f"metadata.coverage missing required key: {key!r}"
                for key in _REQUIRED_COVERAGE
                if key not in coverage
            )
            sources = coverage.get("sources")
            if isinstance(sources, dict):
                for key, entry in sources.items():
                    if not isinstance(entry, dict) or entry.get("status") not in {
                        "success",
                        "failed",
                    }:
                        errors.append(
                            f"metadata.coverage.sources[{key!r}] must record"
                            " status 'success' or 'failed'"
                        )
            elif "sources" in coverage:
                errors.append("metadata.coverage.sources must be a JSON object")
        elif "coverage" in metadata:
            errors.append("metadata.coverage must be a JSON object")

    items = data["items"]
    if not isinstance(items, list):
        errors.append("'items' must be a JSON array")
        return errors
    seen: set[str] = set()
    for idx, item in enumerate(items):
        errors.extend(_validate_item(idx, item))
        if isinstance(item, dict):
            item_id = str(item.get("id", ""))
            if item_id in seen:
                errors.append(f"items[{idx}]: duplicate evidence ID {item_id!r}")
            seen.add(item_id)
    return errors


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help="Path to evidence bundle JSON file",
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
    errors = validate_bundle(data)
    if errors:
        for error in errors:
            print(error)
        return 1
    print(f"validated {args.input}: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
