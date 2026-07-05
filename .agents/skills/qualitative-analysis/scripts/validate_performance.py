#!/usr/bin/env python3
"""Thin wrapper: validate an AIMS stance-evaluation performance artifact."""

from __future__ import annotations

from aims.validate_performance import main, validate_artifact

__all__ = ["main", "validate_artifact"]

if __name__ == "__main__":
    raise SystemExit(main())
