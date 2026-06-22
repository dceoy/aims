#!/usr/bin/env python3
"""Thin wrapper: create or update the CFD instruments CSV."""

from __future__ import annotations

from aims.update_cfd_instruments import build_rows, main

__all__ = ["build_rows", "main"]

if __name__ == "__main__":
    main()
