#!/usr/bin/env python3
"""Thin wrapper: validate an AIMS evidence bundle JSON file."""

from __future__ import annotations

from aims.validate_evidence import main, validate_bundle

__all__ = ["main", "validate_bundle"]

if __name__ == "__main__":
    raise SystemExit(main())
