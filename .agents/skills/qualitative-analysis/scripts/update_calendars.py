#!/usr/bin/env python3
"""Thin wrapper: refresh the AIMS earnings calendar from yfinance."""

from __future__ import annotations

from aims.calendars import build_earnings_calendar, main

__all__ = ["build_earnings_calendar", "main"]

if __name__ == "__main__":
    raise SystemExit(main())
