#!/usr/bin/env python3
"""Thin wrapper: validate the AIMS prompt-regression history file."""

from __future__ import annotations

from aims.validate_prompt_regression import main, validate_history

__all__ = ["main", "validate_history"]

if __name__ == "__main__":
    raise SystemExit(main())
