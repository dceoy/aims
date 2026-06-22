#!/usr/bin/env python3
"""Thin wrapper: generate deterministic score-history artifacts."""

from __future__ import annotations

import sys

from aims.history import main

if __name__ == "__main__":
    sys.exit(main())
