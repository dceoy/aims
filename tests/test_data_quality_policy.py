from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from types import ModuleType

import aims.policy as _aims_policy


@pytest.fixture(scope="module")
def policy() -> ModuleType:
    return _aims_policy


def test_daily_thresholds(policy: ModuleType) -> None:
    thresholds = policy.get_interval_thresholds("d")
    assert thresholds.stale_days == 5
    assert thresholds.max_gap_days == 7
    assert thresholds.min_history == 60


def test_weekly_thresholds(policy: ModuleType) -> None:
    thresholds = policy.get_interval_thresholds("w")
    assert thresholds.stale_days == 21
    assert thresholds.max_gap_days == 21


def test_monthly_thresholds(policy: ModuleType) -> None:
    thresholds = policy.get_interval_thresholds("m")
    assert thresholds.stale_days == 62
    assert thresholds.max_gap_days == 62


def test_unsupported_interval(policy: ModuleType) -> None:
    with pytest.raises(ValueError, match="unsupported interval"):
        policy.get_interval_thresholds("h")


def test_fetch_window_days_daily(policy: ModuleType) -> None:
    assert policy.fetch_window_days("d") == 365


def test_fetch_window_days_weekly_clears_min_history(policy: ModuleType) -> None:
    thresholds = policy.get_interval_thresholds("w")
    window = policy.fetch_window_days("w")
    # ~7 calendar days per weekly bar; window must clear min_history bars.
    assert window / 7 > thresholds.min_history


def test_fetch_window_days_monthly_clears_min_history(policy: ModuleType) -> None:
    thresholds = policy.get_interval_thresholds("m")
    window = policy.fetch_window_days("m")
    # ~30 calendar days per monthly bar; window must clear min_history bars.
    assert window / 30 > thresholds.min_history


def test_fetch_window_days_unsupported_interval(policy: ModuleType) -> None:
    with pytest.raises(ValueError, match="unsupported interval"):
        policy.fetch_window_days("h")


def test_build_config_dict(policy: ModuleType) -> None:
    quality_policy = policy.get_data_quality_policy("d")
    config = policy.build_config_dict(quality_policy)
    assert config["interval"] == "d"
    assert config["stale_days"] == 5
    assert config["max_gap_days"] == 7
    assert config["coverage_policy"]["min_success_ratio"] == 0.8


def test_evaluate_coverage_all_available(policy: ModuleType) -> None:
    result = policy.evaluate_coverage(
        ["A", "B", "C", "D", "E"],
        ["A", "B", "C", "D", "E"],
        [],
        policy.DEFAULT_COVERAGE_POLICY,
    )
    assert result.passed is True
    assert result.success_ratio == 1.0


def test_evaluate_coverage_one_missing_within_policy(policy: ModuleType) -> None:
    result = policy.evaluate_coverage(
        ["A", "B", "C", "D", "E"],
        ["A", "B", "C", "D"],
        ["E"],
        policy.DEFAULT_COVERAGE_POLICY,
    )
    assert result.passed is True
    assert result.success_ratio == 0.8


def test_evaluate_coverage_too_many_missing(policy: ModuleType) -> None:
    result = policy.evaluate_coverage(
        ["A", "B", "C", "D", "E"],
        ["A", "B", "C"],
        ["D", "E"],
        policy.DEFAULT_COVERAGE_POLICY,
    )
    assert result.passed is False
    assert any("missing symbols" in v for v in result.violations)


def test_evaluate_coverage_success_ratio_below_threshold(policy: ModuleType) -> None:
    result = policy.evaluate_coverage(
        ["A", "B", "C"],
        ["A"],
        ["B", "C"],
        policy.DEFAULT_COVERAGE_POLICY,
    )
    assert result.passed is False
    assert any("success ratio" in v for v in result.violations)


def test_evaluate_coverage_empty_universe(policy: ModuleType) -> None:
    result = policy.evaluate_coverage([], [], [], policy.DEFAULT_COVERAGE_POLICY)
    assert result.passed is False
    assert result.violations == ("empty symbol universe",)


def test_evaluate_coverage_all_failed(policy: ModuleType) -> None:
    result = policy.evaluate_coverage(
        ["A", "B"],
        [],
        ["A", "B"],
        policy.DEFAULT_COVERAGE_POLICY,
    )
    assert result.passed is False
    assert any("all symbols failed" in v for v in result.violations)


def test_build_coverage_metadata(policy: ModuleType) -> None:
    result = policy.evaluate_coverage(
        ["A", "B", "C", "D", "E"],
        ["A", "B", "C", "D"],
        ["E"],
        policy.DEFAULT_COVERAGE_POLICY,
    )
    metadata = policy.build_coverage_metadata(result)
    assert metadata["attempted_count"] == 5
    assert metadata["fetched_count"] == 4
    assert metadata["missing_symbols"] == ["E"]
    assert metadata["passed"] is True
