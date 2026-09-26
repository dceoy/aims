#!/usr/bin/env python3
"""Thin wrapper: refresh central-bank schedules from official web pages."""

from __future__ import annotations

from aims.macro_calendar import (
    build_macro_calendar,
    main,
    parse_boj,
    parse_ecb,
    parse_fed,
)

__all__ = ["build_macro_calendar", "main", "parse_boj", "parse_ecb", "parse_fed"]

if __name__ == "__main__":
    raise SystemExit(main())
