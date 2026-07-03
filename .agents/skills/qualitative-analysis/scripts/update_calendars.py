#!/usr/bin/env python3
"""Thin wrapper: fetch earnings dates and validate calendar files."""

from __future__ import annotations

import sys

from aims.calendars import fetch_earnings_calendar, main, validate_calendar

__all__ = ["fetch_earnings_calendar", "main", "validate_calendar"]

if __name__ == "__main__":
    sys.exit(main())
