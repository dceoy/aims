#!/usr/bin/env python3
"""Thin wrapper: sample recent evidence citation URLs and warn on link rot."""

from __future__ import annotations

from aims.link_check import check_url, main, sample_items

__all__ = ["check_url", "main", "sample_items"]

if __name__ == "__main__":
    raise SystemExit(main())
