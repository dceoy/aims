#!/usr/bin/env python3
"""Thin wrapper: validate qualitative artifacts and inspect grounding gates."""

from __future__ import annotations

import sys

from aims.validate_qualitative import apply_gates, main, validate_artifact

__all__ = ["apply_gates", "main", "validate_artifact"]

if __name__ == "__main__":
    sys.exit(main())
