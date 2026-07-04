#!/usr/bin/env python3
"""Thin wrapper: generate the AI qualitative analysis artifact."""

from __future__ import annotations

from aims.qualitative import generate, main

__all__ = ["generate", "main"]

if __name__ == "__main__":
    raise SystemExit(main())
