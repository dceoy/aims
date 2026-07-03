#!/usr/bin/env python3
"""Thin wrapper: evaluate qualitative stances against realized returns."""

from __future__ import annotations

import sys

from aims.qualitative_eval import check_links, evaluate_stances, main

__all__ = ["check_links", "evaluate_stances", "main"]

if __name__ == "__main__":
    sys.exit(main())
