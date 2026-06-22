#!/usr/bin/env python3
"""Thin wrapper: generate a Hugo Markdown report from an AIMS analysis artifact."""

from __future__ import annotations

import sys

from aims.reports import generate_report, main, report_filename

__all__ = ["generate_report", "main", "report_filename"]

if __name__ == "__main__":
    sys.exit(main())
