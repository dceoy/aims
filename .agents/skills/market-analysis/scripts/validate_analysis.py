#!/usr/bin/env python3
"""Thin wrapper: validate an AIMS analysis artifact JSON file."""

from __future__ import annotations

from aims.validate_analysis import main, validate_artifact

__all__ = ["main", "validate_artifact"]

if __name__ == "__main__":
    main()
