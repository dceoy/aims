#!/usr/bin/env python3
"""Thin wrapper: run the qualitative prompt/model regression harness."""

from __future__ import annotations

from aims.prompt_regression import compute_metrics, main, run_checks

__all__ = ["compute_metrics", "main", "run_checks"]

if __name__ == "__main__":
    raise SystemExit(main())
