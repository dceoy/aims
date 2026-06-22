#!/usr/bin/env python3
"""Thin wrapper: generate deterministic score-history artifacts."""

from __future__ import annotations

import sys

from aims.history import build_history, main

__all__ = ["build_history", "main"]

if __name__ == "__main__":
    sys.exit(main())
