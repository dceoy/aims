#!/usr/bin/env python3
"""Thin wrapper: propose OKF theme promotions from qualitative artifacts."""

from __future__ import annotations

from aims.okf_curation import cluster_themes, main, promotion_candidates

__all__ = ["cluster_themes", "main", "promotion_candidates"]

if __name__ == "__main__":
    raise SystemExit(main())
