#!/usr/bin/env python3
"""Thin wrapper: validate an AIMS score-history artifact."""

from __future__ import annotations

import sys

from aims.validate_history import main, validate

__all__ = ["main", "validate"]

if __name__ == "__main__":
    sys.exit(main())
