"""Backwards-compatible re-export of data quality policy from aims.policy."""

from __future__ import annotations

from aims.policy import (
    DEFAULT_COVERAGE_POLICY,
    CoveragePolicy,
    CoverageResult,
    DataQualityPolicy,
    Interval,
    IntervalQualityThresholds,
    build_config_dict,
    build_coverage_metadata,
    evaluate_coverage,
    get_data_quality_policy,
    get_interval_thresholds,
)

__all__ = [
    "DEFAULT_COVERAGE_POLICY",
    "CoveragePolicy",
    "CoverageResult",
    "DataQualityPolicy",
    "Interval",
    "IntervalQualityThresholds",
    "build_config_dict",
    "build_coverage_metadata",
    "evaluate_coverage",
    "get_data_quality_policy",
    "get_interval_thresholds",
]
