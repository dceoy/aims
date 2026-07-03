#!/usr/bin/env python3
"""Thin wrapper: generate a grounded AI qualitative analysis artifact."""

from __future__ import annotations

import sys

from aims.qualitative import build_prompt, generate, main

__all__ = ["build_prompt", "generate", "main"]

if __name__ == "__main__":
    sys.exit(main())
