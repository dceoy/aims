#!/usr/bin/env python3
"""Thin wrapper: market data fetch, scoring, and analysis artifact generation."""

from __future__ import annotations

import sys

from aims.market_analysis import main

if __name__ == "__main__":
    sys.exit(main())
