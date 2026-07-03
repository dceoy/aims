#!/usr/bin/env python3
"""Thin wrapper: fetch and validate news/disclosure evidence bundles."""

from __future__ import annotations

import sys

from aims.evidence import fetch_bundle, main, parse_feed, validate_bundle

__all__ = ["fetch_bundle", "main", "parse_feed", "validate_bundle"]

if __name__ == "__main__":
    sys.exit(main())
