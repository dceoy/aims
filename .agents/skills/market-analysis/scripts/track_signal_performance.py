#!/usr/bin/env python3
"""Thin wrapper: track realized forward returns of published top-5 signals."""

from __future__ import annotations

from aims.signal_performance import build_artifact, evaluate_signals, main, render_page

__all__ = ["build_artifact", "evaluate_signals", "main", "render_page"]

if __name__ == "__main__":
    raise SystemExit(main())
