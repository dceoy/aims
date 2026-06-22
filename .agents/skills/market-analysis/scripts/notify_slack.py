#!/usr/bin/env python3
"""Thin wrapper: send Slack notifications for AIMS pipeline results."""

from __future__ import annotations

import sys

from aims.notifications import build_success_payload, main

__all__ = ["build_success_payload", "main"]

if __name__ == "__main__":
    sys.exit(main())
