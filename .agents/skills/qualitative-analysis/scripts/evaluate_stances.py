#!/usr/bin/env python3
"""Thin wrapper: evaluate AI qualitative stances against realized returns."""

from __future__ import annotations

from aims.performance import build_artifact, evaluate_stances, main, render_page

__all__ = ["build_artifact", "evaluate_stances", "main", "render_page"]

if __name__ == "__main__":
    raise SystemExit(main())
