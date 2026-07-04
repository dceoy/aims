#!/usr/bin/env python3
"""Thin wrapper: validate an AIMS qualitative analysis artifact."""

from __future__ import annotations

from aims.validate_qualitative import main, validate_artifact

__all__ = ["main", "validate_artifact"]

if __name__ == "__main__":
    raise SystemExit(main())
