"""Single source of truth for AIMS market-data quality and coverage policy."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Final, Literal

Interval = Literal["d", "w", "m"]

_SUPPORTED_INTERVALS: Final[tuple[str, ...]] = ("d", "w", "m")


@dataclass(frozen=True)
class IntervalQualityThresholds:
    """Freshness and gap thresholds for one bar interval."""

    stale_days: int
    max_gap_days: int
    min_history: int


@dataclass(frozen=True)
class CoveragePolicy:
    """Workflow fail gates for systemic data-source failures."""

    min_success_ratio: float
    max_missing_symbols: int


@dataclass(frozen=True)
class DataQualityPolicy:
    """Effective quality policy for a single analysis run."""

    interval: str
    thresholds: IntervalQualityThresholds
    coverage: CoveragePolicy


@dataclass(frozen=True)
class CoverageResult:
    """Observed symbol coverage for one analysis run."""

    attempted_symbols: tuple[str, ...]
    fetched_symbols: tuple[str, ...]
    missing_symbols: tuple[str, ...]
    success_ratio: float
    passed: bool
    violations: tuple[str, ...]


_INTERVAL_THRESHOLDS: Final[dict[str, IntervalQualityThresholds]] = {
    "d": IntervalQualityThresholds(stale_days=5, max_gap_days=7, min_history=60),
    "w": IntervalQualityThresholds(stale_days=21, max_gap_days=21, min_history=60),
    "m": IntervalQualityThresholds(stale_days=62, max_gap_days=62, min_history=60),
}

# Calendar-day fetch lookback per interval, chosen so each interval clears
# its min_history bar threshold above with a comfortable margin for
# holidays, provider gaps, and the longest feature lookback (60 bars).
_FETCH_WINDOW_DAYS: Final[dict[str, int]] = {
    "d": 365,  # ~250 trading days
    "w": 1460,  # ~4 years -> ~208 weekly bars
    "m": 3650,  # ~10 years -> ~120 monthly bars
}

_DEFAULT_COVERAGE: Final[CoveragePolicy] = CoveragePolicy(
    min_success_ratio=0.8,
    max_missing_symbols=1,
)
DEFAULT_COVERAGE_POLICY: Final[CoveragePolicy] = _DEFAULT_COVERAGE


def get_interval_thresholds(interval: str) -> IntervalQualityThresholds:
    """Return interval-specific freshness and missing-bar thresholds."""
    if interval not in _INTERVAL_THRESHOLDS:
        msg = (
            f"unsupported interval: {interval!r}"
            f" (expected one of {_SUPPORTED_INTERVALS})"
        )
        raise ValueError(msg)
    return _INTERVAL_THRESHOLDS[interval]


def fetch_window_days(interval: str) -> int:
    """Return the calendar-day fetch lookback window for *interval*.

    A fixed 365-day window (enough for ~250 daily bars) is far too short
    for weekly (~52 bars/year) or monthly (~12 bars/year) intervals to
    clear ``min_history=60``; this scales the window per interval instead.
    """
    if interval not in _FETCH_WINDOW_DAYS:
        msg = (
            f"unsupported interval: {interval!r}"
            f" (expected one of {_SUPPORTED_INTERVALS})"
        )
        raise ValueError(msg)
    return _FETCH_WINDOW_DAYS[interval]


def get_data_quality_policy(
    interval: str,
    *,
    coverage: CoveragePolicy | None = None,
) -> DataQualityPolicy:
    """Return the effective policy for *interval*."""
    return DataQualityPolicy(
        interval=interval,
        thresholds=get_interval_thresholds(interval),
        coverage=coverage or _DEFAULT_COVERAGE,
    )


def build_config_dict(policy: DataQualityPolicy) -> dict[str, Any]:
    """Serialize effective thresholds and coverage policy for artifact metadata."""
    thresholds = policy.thresholds
    coverage = policy.coverage
    return {
        "interval": policy.interval,
        "stale_days": thresholds.stale_days,
        "max_gap_days": thresholds.max_gap_days,
        "min_history": thresholds.min_history,
        "coverage_policy": {
            "min_success_ratio": coverage.min_success_ratio,
            "max_missing_symbols": coverage.max_missing_symbols,
        },
    }


def evaluate_coverage(
    attempted: list[str],
    fetched: list[str],
    missing: list[str],
    policy: CoveragePolicy,
) -> CoverageResult:
    """Evaluate whether observed symbol coverage satisfies workflow fail gates."""
    attempted_symbols = tuple(attempted)
    fetched_symbols = tuple(fetched)
    missing_symbols = tuple(missing)
    attempted_count = len(attempted_symbols)

    if attempted_count == 0:
        return CoverageResult(
            attempted_symbols=attempted_symbols,
            fetched_symbols=fetched_symbols,
            missing_symbols=missing_symbols,
            success_ratio=0.0,
            passed=False,
            violations=("empty symbol universe",),
        )

    success_ratio = len(fetched_symbols) / attempted_count
    violations: list[str] = []

    if not fetched_symbols:
        violations.append("all symbols failed to load")
    if len(missing_symbols) > policy.max_missing_symbols:
        violations.append(
            f"missing symbols ({len(missing_symbols)} > {policy.max_missing_symbols})"
        )
    if success_ratio < policy.min_success_ratio:
        violations.append(
            f"success ratio ({success_ratio:.2%} < {policy.min_success_ratio:.0%})"
        )

    return CoverageResult(
        attempted_symbols=attempted_symbols,
        fetched_symbols=fetched_symbols,
        missing_symbols=missing_symbols,
        success_ratio=success_ratio,
        passed=not violations,
        violations=tuple(violations),
    )


def build_coverage_metadata(result: CoverageResult) -> dict[str, Any]:
    """Serialize observed coverage statistics for artifact metadata."""
    return {
        "attempted_count": len(result.attempted_symbols),
        "fetched_count": len(result.fetched_symbols),
        "missing_symbols": list(result.missing_symbols),
        "success_ratio": round(result.success_ratio, 4),
        "passed": result.passed,
        "violations": list(result.violations),
    }
