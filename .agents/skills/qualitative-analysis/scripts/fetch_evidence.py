#!/usr/bin/env python3
"""Thin wrapper: build a deterministic evidence bundle for AIMS."""

from __future__ import annotations

from aims.evidence import build_bundle, main, save_bundle

__all__ = ["build_bundle", "main", "save_bundle"]

if __name__ == "__main__":
    raise SystemExit(main())
