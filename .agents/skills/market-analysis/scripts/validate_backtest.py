#!/usr/bin/env python3
"""Thin wrapper: validate an AIMS walk-forward backtest artifact."""

from __future__ import annotations

import sys

from aims.validate_backtest import main, validate_artifact

__all__ = ["main", "validate_artifact"]

if __name__ == "__main__":
    sys.exit(main())
