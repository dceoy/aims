#!/usr/bin/env python3
"""Thin wrapper: validate an AIMS calendar JSON file."""

from __future__ import annotations

from aims.validate_calendar import main, validate_calendar

__all__ = ["main", "validate_calendar"]

if __name__ == "__main__":
    raise SystemExit(main())
