from __future__ import annotations

import json
from dataclasses import replace
from datetime import UTC, datetime, timedelta
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from pathlib import Path
    from types import ModuleType

import aims.backtest as _aims_bt
import aims.market_analysis as _aims_ma
from aims.validate_backtest import validate_artifact


@pytest.fixture(scope="module")
def modules() -> tuple[ModuleType, ModuleType]:
    return _aims_ma, _aims_bt


def _bars(ma: ModuleType, symbol: str, slope: float, count: int = 70) -> list[object]:
    start = datetime(2024, 1, 1, tzinfo=UTC)
    return [
        ma.OhlcvBar(
            symbol,
            start + timedelta(days=index),
            100 + slope * index,
            100 + slope * index,
            100 + slope * index,
            100 + slope * index,
            1_000,
            "test",
            "d",
        )
        for index in range(count)
    ]


def test_helpers_and_validation(modules: tuple[ModuleType, ModuleType]) -> None:
    _, backtest = modules
    assert backtest._mean([]) is None
    assert backtest._mean([1.0, 3.0]) == 2.0
    assert backtest._drawdown([]) is None
    assert backtest._drawdown([0.1, -0.2]) == pytest.approx(0.2)
    assert backtest._parse_positive_csv("1,5") == (1, 5)
    with pytest.raises(Exception, match="positive"):
        backtest._parse_positive_csv("0")
    for kwargs in (
        {"top_k": 0},
        {"buckets": 0},
        {"min_history": 0},
        {"horizons": ()},
        {"horizons": (0,)},
        {"horizons": (-1,)},
    ):
        with pytest.raises(ValueError, match="positive"):
            backtest.run_backtest({}, **kwargs)
    with pytest.raises(ValueError, match="unique"):
        backtest.run_backtest({}, horizons=(1, 1))


# ── Spearman rank correlation helpers ───────────────────────────────────────────


def test_ranks_handles_ties_by_averaging(
    modules: tuple[ModuleType, ModuleType],
) -> None:
    _, backtest = modules
    assert backtest._ranks([10.0, 20.0, 20.0, 30.0]) == [1.0, 2.5, 2.5, 4.0]


def test_spearman_perfect_positive_and_negative_correlation(
    modules: tuple[ModuleType, ModuleType],
) -> None:
    _, backtest = modules
    assert backtest._spearman([1.0, 2.0, 3.0], [10.0, 20.0, 30.0]) == pytest.approx(1.0)
    assert backtest._spearman([1.0, 2.0, 3.0], [30.0, 20.0, 10.0]) == pytest.approx(
        -1.0
    )


def test_spearman_requires_at_least_two_pairs(
    modules: tuple[ModuleType, ModuleType],
) -> None:
    _, backtest = modules
    assert backtest._spearman([], []) is None
    assert backtest._spearman([1.0], [2.0]) is None


def test_spearman_none_when_no_variance(
    modules: tuple[ModuleType, ModuleType],
) -> None:
    _, backtest = modules
    assert backtest._spearman([1.0, 1.0], [1.0, 2.0]) is None
    assert backtest._spearman([1.0, 2.0], [1.0, 1.0]) is None


def test_corr_key_is_order_independent(
    modules: tuple[ModuleType, ModuleType],
) -> None:
    _, backtest = modules
    assert backtest._corr_key("ret_1d", "ret_5d") == backtest._corr_key(
        "ret_5d", "ret_1d"
    )


# ── cost model ───────────────────────────────────────────────────────────────────


def test_load_instrument_costs(
    modules: tuple[ModuleType, ModuleType], tmp_path: Path
) -> None:
    _, backtest = modules
    path = tmp_path / "costs.csv"
    path.write_text(
        "symbol,spread_bps,financing_rate_annual\nAAPL,5,0.03\n", encoding="utf-8"
    )
    costs = backtest.load_instrument_costs(path)
    assert costs == {"AAPL": backtest.InstrumentCost(5.0, 0.03)}


def test_round_trip_cost(modules: tuple[ModuleType, ModuleType]) -> None:
    _, backtest = modules
    cost = backtest.InstrumentCost(spread_bps=10.0, financing_rate_annual=0.1)
    # 2 * 10bps + 0.1 * (10/365)
    assert backtest._round_trip_cost(cost, 10) == pytest.approx(
        0.002 + 0.1 * (10 / 365)
    )


# ── moving-block bootstrap ───────────────────────────────────────────────────────


def test_moving_block_bootstrap_ci_requires_two_values(
    modules: tuple[ModuleType, ModuleType],
) -> None:
    _, backtest = modules
    assert (
        backtest._moving_block_bootstrap_ci([], block_size=5, iterations=100, seed=0)
        is None
    )
    assert (
        backtest._moving_block_bootstrap_ci([0.1], block_size=5, iterations=100, seed=0)
        is None
    )


def test_moving_block_bootstrap_ci_deterministic_and_brackets_mean(
    modules: tuple[ModuleType, ModuleType],
) -> None:
    _, backtest = modules
    values = [0.01, 0.02, -0.01, 0.015, 0.005, 0.0, 0.03, -0.005, 0.01, 0.02]
    ci_a = backtest._moving_block_bootstrap_ci(
        values, block_size=3, iterations=200, seed=42
    )
    ci_b = backtest._moving_block_bootstrap_ci(
        values, block_size=3, iterations=200, seed=42
    )
    assert ci_a == ci_b
    assert ci_a is not None
    assert ci_a["low"] <= ci_a["high"]


def test_moving_block_bootstrap_ci_block_size_capped_at_n(
    modules: tuple[ModuleType, ModuleType],
) -> None:
    _, backtest = modules
    ci = backtest._moving_block_bootstrap_ci(
        [0.1, 0.2], block_size=100, iterations=50, seed=0
    )
    assert ci is not None


# ── run_backtest metrics ─────────────────────────────────────────────────────────


def test_run_backtest_metrics(modules: tuple[ModuleType, ModuleType]) -> None:
    ma, backtest = modules
    data = {"UP": _bars(ma, "UP", 2.0), "DOWN": _bars(ma, "DOWN", -0.5)}
    result = backtest.run_backtest(
        data, horizons=(1, 5), top_k=1, buckets=2, min_history=60
    )
    assert result["observations"] == 10
    assert result["metrics"]["1d"]["top_k"]["count"] == 10
    assert result["metrics"]["1d"]["top_k"]["hit_rate"] == 1.0
    assert result["metrics"]["5d"]["score_buckets"]["1"]["count"] == 6
    assert result["turnover"] == 0.0
    assert result["max_drawdown"] == 0.0
    empty = backtest.run_backtest({}, horizons=(1,))
    assert empty["observations"] == 0
    assert empty["date_range"] == {"start": None, "end": None}
    assert empty["metrics"]["1d"]["top_k"]["average_return"] is None
    empty_diagnostics = empty["feature_diagnostics"]
    assert empty_diagnostics["features"] == list(backtest._FEATURES)
    assert empty_diagnostics["information_coefficient"]["1d"]["ret_1d"] == {
        "mean": None,
        "n": 0,
    }
    assert empty_diagnostics["feature_correlation"]["ret_1d"]["ret_1d"] == 1.0
    assert empty_diagnostics["feature_correlation"]["ret_1d"]["ret_5d"] is None


# ── net-of-cost, benchmark, significance, regime breakdown ─────────────────────


def test_run_backtest_benchmark_and_net_of_cost(
    modules: tuple[ModuleType, ModuleType],
) -> None:
    ma, backtest = modules
    data = {"UP": _bars(ma, "UP", 2.0), "DOWN": _bars(ma, "DOWN", -0.5)}
    cost = backtest.InstrumentCost(spread_bps=10.0, financing_rate_annual=0.05)
    result = backtest.run_backtest(
        data,
        horizons=(1,),
        top_k=1,
        min_history=60,
        costs={"UP": cost, "DOWN": cost},
    )
    top_k = result["metrics"]["1d"]["top_k"]
    benchmark = result["metrics"]["1d"]["benchmark"]
    # UP is always selected (top_k=1); benchmark averages UP and DOWN.
    assert benchmark["count"] == top_k["count"] * 2
    assert top_k["average_return"] > benchmark["average_return"]
    assert top_k["excess_return"] == pytest.approx(
        top_k["average_return"] - benchmark["average_return"]
    )
    expected_cost = backtest._round_trip_cost(cost, 1)
    assert top_k["net_average_return"] == pytest.approx(
        top_k["average_return"] - expected_cost
    )
    assert top_k["net_excess_return"] == pytest.approx(
        top_k["net_average_return"] - benchmark["average_return"]
    )


def test_run_backtest_uses_default_cost_when_unmapped(
    modules: tuple[ModuleType, ModuleType],
) -> None:
    ma, backtest = modules
    data = {"UP": _bars(ma, "UP", 2.0), "DOWN": _bars(ma, "DOWN", -0.5)}
    result = backtest.run_backtest(data, horizons=(1,), top_k=1, min_history=60)
    top_k = result["metrics"]["1d"]["top_k"]
    default_cost_amount = backtest._round_trip_cost(backtest.DEFAULT_COST, 1)
    assert top_k["net_average_return"] == pytest.approx(
        top_k["average_return"] - default_cost_amount
    )


def test_run_backtest_significance_and_regime_breakdown(
    modules: tuple[ModuleType, ModuleType],
) -> None:
    ma, backtest = modules
    data = {"UP": _bars(ma, "UP", 2.0), "DOWN": _bars(ma, "DOWN", -0.5)}
    result = backtest.run_backtest(
        data,
        horizons=(1, 5),
        top_k=1,
        min_history=60,
        bootstrap_iterations=200,
        bootstrap_seed=7,
    )
    significance = result["significance"]
    assert significance["horizon"] == 1
    assert significance["n"] == result["observations"]
    assert significance["iterations"] == 200
    assert significance["seed"] == 7
    assert significance["confidence_interval"] is not None
    assert (
        significance["confidence_interval"]["low"]
        <= significance["confidence_interval"]["high"]
    )

    regime_breakdown = result["regime_breakdown"]
    assert regime_breakdown["horizon"] == 1
    regimes = regime_breakdown["regimes"]
    assert regimes
    total_count = sum(r["count"] for r in regimes.values())
    assert total_count == result["observations"]


def test_run_backtest_significance_none_without_enough_observations(
    modules: tuple[ModuleType, ModuleType],
) -> None:
    _, backtest = modules
    empty = backtest.run_backtest({}, horizons=(1,))
    assert empty["significance"]["confidence_interval"] is None
    assert empty["significance"]["n"] == 0
    assert empty["regime_breakdown"]["regimes"] == {}


# ── feature_diagnostics ──────────────────────────────────────────────────────────


def test_run_backtest_feature_diagnostics_ic_sign(
    modules: tuple[ModuleType, ModuleType],
) -> None:
    ma, backtest = modules
    # UP always leads DOWN on both short-term momentum and forward returns,
    # so the cross-sectional Spearman correlation is +1 every observed date.
    data = {"UP": _bars(ma, "UP", 2.0), "DOWN": _bars(ma, "DOWN", -0.5)}
    result = backtest.run_backtest(data, horizons=(1,), top_k=1, min_history=60)
    ic = result["feature_diagnostics"]["information_coefficient"]["1d"]["ret_1d"]
    assert ic["mean"] == pytest.approx(1.0)
    assert ic["n"] == result["observations"]
    corr = result["feature_diagnostics"]["feature_correlation"]
    assert corr["ret_1d"]["ret_5d"] == pytest.approx(1.0)
    assert corr["ret_5d"]["ret_1d"] == pytest.approx(1.0)


def test_run_backtest_feature_diagnostics_three_symbols(
    modules: tuple[ModuleType, ModuleType],
) -> None:
    ma, backtest = modules
    # Three distinct slopes give non-degenerate rank variance every date,
    # exercising the >2-point Spearman path (not just a +-1 coin flip).
    data = {
        "HIGH": _bars(ma, "HIGH", 3.0),
        "MID": _bars(ma, "MID", 1.0),
        "LOW": _bars(ma, "LOW", -1.0),
    }
    result = backtest.run_backtest(data, horizons=(1,), min_history=60)
    ic = result["feature_diagnostics"]["information_coefficient"]["1d"]["ret_1d"]
    assert ic["mean"] == pytest.approx(1.0)
    assert ic["n"] == result["observations"]
    no_daily = backtest.run_backtest(data, horizons=(5,), min_history=60)
    assert no_daily["max_drawdown"] is None


def test_short_history_symbol_does_not_suppress_mature_symbols(
    modules: tuple[ModuleType, ModuleType],
) -> None:
    ma, backtest = modules
    data = {
        "MATURE": _bars(ma, "MATURE", 1.0),
        "NEW": _bars(ma, "NEW", 2.0, count=10),
    }
    result = backtest.run_backtest(data, horizons=(1,), min_history=60)
    assert result["observations"] == 10
    assert result["metrics"]["1d"]["top_k"]["count"] == 10
    assert result["date_range"]["end"] == "2024-03-09"
    gapped = _bars(ma, "GAPPED", 1.0, count=3)
    gapped = [
        replace(bar, timestamp=bar.timestamp + timedelta(days=10 * index))
        for index, bar in enumerate(gapped)
    ]
    unreliable = backtest.run_backtest({"GAPPED": gapped}, horizons=(1,), min_history=2)
    assert unreliable["observations"] == 0


def test_missing_forward_bar_does_not_promote_lower_rank(
    modules: tuple[ModuleType, ModuleType],
) -> None:
    ma, backtest = modules
    data = {
        "TOP": _bars(ma, "TOP", 2.0, count=70),
        "LOWER": _bars(ma, "LOWER", 1.0, count=75),
    }
    result = backtest.run_backtest(
        data, horizons=(1,), top_k=1, buckets=2, min_history=60
    )
    top = result["metrics"]["1d"]["top_k"]
    bucket_count = sum(
        bucket["count"] for bucket in result["metrics"]["1d"]["score_buckets"].values()
    )
    assert top["count"] == 14
    assert bucket_count == 25
    assert result["turnover"] == pytest.approx(1 / 13)


def test_turnover_excludes_dates_without_forward_observations(
    modules: tuple[ModuleType, ModuleType],
) -> None:
    ma, backtest = modules
    leader = _bars(ma, "LEADER", 1.0, count=65)
    late_leader = _bars(ma, "LATE", 0.0, count=65)
    late_leader[-1] = replace(
        late_leader[-1], open=1_000.0, high=1_000.0, low=1_000.0, close=1_000.0
    )
    result = backtest.run_backtest(
        {"LEADER": leader, "LATE": late_leader},
        horizons=(1,),
        top_k=1,
        min_history=60,
    )
    assert result["turnover"] == 0.0


def test_main_writes_artifact(
    modules: tuple[ModuleType, ModuleType], tmp_path: Path
) -> None:
    ma, backtest = modules
    prices = tmp_path / "prices"
    for symbol, slope in (("UP", 2.0), ("DOWN", -0.5)):
        ma.save_ohlcv(_bars(ma, symbol, slope), prices)
    output = tmp_path / "backtests"
    assert (
        backtest.main([
            "--symbols",
            "UP,DOWN",
            "--data-dir",
            str(prices),
            "--output-dir",
            str(output),
            "--horizons",
            "1,5",
            "--top-k",
            "1",
        ])
        == 0
    )
    path = next(output.glob("*.json"))
    content = path.read_text()
    artifact = json.loads(content)
    assert artifact["schema_version"] == backtest.BACKTEST_VERSION
    assert artifact["scoring_version"] == ma.SCORING_VERSION
    assert artifact["config"]["forward_horizons"] == [1, 5]
    assert artifact["date_range"] == {"start": "2024-02-29", "end": "2024-03-09"}
    assert "feature_diagnostics" in artifact
    assert validate_artifact(artifact) == []
    assert (
        backtest.main([
            "--symbols",
            "UP,DOWN",
            "--data-dir",
            str(prices),
            "--output-dir",
            str(output),
            "--horizons",
            "1,5",
            "--top-k",
            "1",
        ])
        == 0
    )
    assert path.read_text() == content


def test_main_with_cost_mapping_and_bootstrap_args(
    modules: tuple[ModuleType, ModuleType], tmp_path: Path
) -> None:
    ma, backtest = modules
    prices = tmp_path / "prices"
    for symbol, slope in (("UP", 2.0), ("DOWN", -0.5)):
        ma.save_ohlcv(_bars(ma, symbol, slope), prices)
    cost_mapping = tmp_path / "costs.csv"
    cost_mapping.write_text(
        "symbol,spread_bps,financing_rate_annual\nUP,5,0.03\n", encoding="utf-8"
    )
    output = tmp_path / "backtests"
    assert (
        backtest.main([
            "--symbols",
            "UP,DOWN",
            "--data-dir",
            str(prices),
            "--output-dir",
            str(output),
            "--horizons",
            "1",
            "--top-k",
            "1",
            "--cost-mapping",
            str(cost_mapping),
            "--bootstrap-iterations",
            "50",
            "--bootstrap-block-size",
            "3",
            "--bootstrap-seed",
            "1",
        ])
        == 0
    )
    artifact = json.loads(next(output.glob("*.json")).read_text())
    assert artifact["significance"]["iterations"] == 50
    assert artifact["significance"]["block_size"] == 3
    assert artifact["significance"]["seed"] == 1
    assert validate_artifact(artifact) == []


def test_main_rejects_no_observations(
    modules: tuple[ModuleType, ModuleType], tmp_path: Path
) -> None:
    ma, backtest = modules
    prices = tmp_path / "prices"
    ma.save_ohlcv(_bars(ma, "SHORT", 1.0, count=2), prices)
    with pytest.raises(SystemExit):
        backtest.main([
            "--symbols",
            "SHORT",
            "--data-dir",
            str(prices),
            "--min-history",
            "2",
        ])


def test_main_rejects_missing_inputs(
    modules: tuple[ModuleType, ModuleType], tmp_path: Path
) -> None:
    _, backtest = modules
    with pytest.raises(SystemExit):
        backtest.main(["--symbols", ","])
    with pytest.raises(SystemExit):
        backtest.main(["--symbols", "MISSING", "--data-dir", str(tmp_path)])
