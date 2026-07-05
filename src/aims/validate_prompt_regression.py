r"""Validate the AIMS prompt-regression history file.

Hand-rolled validator following the ``validate_analysis.py`` pattern (no
``jsonschema`` dependency). The format reference is
``data/schema/prompt_regression.schema.json``; the history is written by
``aims.prompt_regression`` to ``data/performance/prompt_regressions.json``.

Usage:
    uv run \
        .agents/skills/qualitative-analysis/scripts/validate_prompt_regression.py \
        --input data/performance/prompt_regressions.json
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Final

from aims.prompt_regression import PROMPT_REGRESSION_VERSION

_REQUIRED_ENTRY: Final[tuple[str, ...]] = (
    "analysis_date",
    "artifact",
    "artifact_provenance",
    "model_id",
    "prompt_version",
    "prompt_sha256",
    "metrics",
    "checks",
    "passed",
)
_REQUIRED_PROVENANCE: Final[tuple[str, ...]] = (
    "model_id",
    "prompt_version",
    "prompt_sha256",
)
_DATE_RE: Final[re.Pattern[str]] = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_SHA256_RE: Final[re.Pattern[str]] = re.compile(r"^[0-9a-f]{64}$")


def _validate_entry(where: str, entry: Any) -> list[str]:
    if not isinstance(entry, dict):
        return [f"{where} must be a JSON object"]
    errors = [
        f"{where} missing required key: {key!r}"
        for key in _REQUIRED_ENTRY
        if key not in entry
    ]
    if errors:
        return errors
    date = entry["analysis_date"]
    if not isinstance(date, str) or not _DATE_RE.match(date):
        errors.append(f"{where}.analysis_date {date!r} is not a YYYY-MM-DD date")
    errors.extend(
        f"{where}.{key} must be a non-empty string"
        for key in ("artifact", "model_id", "prompt_version")
        if not isinstance(entry[key], str) or not entry[key]
    )
    sha = entry["prompt_sha256"]
    if not isinstance(sha, str) or not _SHA256_RE.match(sha):
        errors.append(f"{where}.prompt_sha256 {sha!r} is not a SHA-256 hex digest")
    provenance = entry["artifact_provenance"]
    if not isinstance(provenance, dict):
        errors.append(f"{where}.artifact_provenance must be a JSON object")
    else:
        errors.extend(
            f"{where}.artifact_provenance missing required key: {key!r}"
            for key in _REQUIRED_PROVENANCE
            if key not in provenance
        )
    if not isinstance(entry["metrics"], dict):
        errors.append(f"{where}.metrics must be a JSON object")
    checks = entry["checks"]
    if not isinstance(checks, dict) or any(
        not isinstance(value, bool) for value in checks.values()
    ):
        errors.append(f"{where}.checks must map check names to booleans")
    elif entry["passed"] is not all(checks.values()):
        errors.append(f"{where}.passed does not match the recorded checks")
    if not isinstance(entry["passed"], bool):
        errors.append(f"{where}.passed must be a boolean")
    return errors


def validate_history(data: dict[str, Any]) -> list[str]:
    """Validate shape and consistency of a prompt-regression history file."""
    errors = [
        f"missing required key: {key!r}"
        for key in ("version", "entries")
        if key not in data
    ]
    if errors:
        return errors
    if data["version"] != PROMPT_REGRESSION_VERSION:
        errors.append(
            f"unsupported version {data['version']!r}"
            f" (expected {PROMPT_REGRESSION_VERSION!r})"
        )
    entries = data["entries"]
    if not isinstance(entries, list):
        errors.append("'entries' must be a JSON array")
        return errors
    for idx, entry in enumerate(entries):
        errors.extend(_validate_entry(f"entries[{idx}]", entry))
    return errors


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help="Path to the prompt-regression history JSON file",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        with args.input.open(encoding="utf-8") as stream:
            data: dict[str, Any] = json.load(stream)
    except FileNotFoundError as exc:
        print(f"ERROR: file not found: {exc.filename}")
        return 1
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON: {exc}")
        return 1
    errors = validate_history(data)
    if errors:
        for error in errors:
            print(error)
        return 1
    print(f"validated {args.input}: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
