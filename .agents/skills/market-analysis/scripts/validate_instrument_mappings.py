#!/usr/bin/env python3
"""Thin wrapper: validate canonical instrument mappings CSV."""

from __future__ import annotations

import sys

from aims.mappings import main

if __name__ == "__main__":
    sys.exit(main())
