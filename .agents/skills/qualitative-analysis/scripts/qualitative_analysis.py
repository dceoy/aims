#!/usr/bin/env python3
"""Thin wrapper: prepare/finalize the AI qualitative analysis artifact."""

from __future__ import annotations

from aims.qualitative import finalize_response, main, prepare_request

__all__ = ["finalize_response", "main", "prepare_request"]

if __name__ == "__main__":
    raise SystemExit(main())
