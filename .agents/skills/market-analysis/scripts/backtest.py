#!/usr/bin/env python3
"""Thin wrapper: run deterministic walk-forward scoring backtest."""

from __future__ import annotations

import sys

from aims.backtest import main

if __name__ == "__main__":
    sys.exit(main())
