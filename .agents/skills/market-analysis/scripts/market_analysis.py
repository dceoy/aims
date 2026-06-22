#!/usr/bin/env python3
"""Thin wrapper: market data fetch, scoring, and analysis artifact generation."""

from __future__ import annotations

import sys

from aims.market_analysis import (
    OhlcvBar,
    StooqProvider,
    generate_artifact,
    main,
    score_instruments,
)

__all__ = [
    "OhlcvBar",
    "StooqProvider",
    "generate_artifact",
    "main",
    "score_instruments",
]

if __name__ == "__main__":
    sys.exit(main())
