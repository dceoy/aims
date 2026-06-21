from __future__ import annotations

import importlib.util
import json
import sys
from dataclasses import replace
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from types import ModuleType

SCRIPTS = (
    Path(__file__).resolve().parents[1]
    / ".agents"
    / "skills"
    / "market-analysis"
    / "scripts"
)


@pytest.fixture(scope="module")
def modules() -> tuple[ModuleType, ModuleType]:
    sys.path.insert(0, str(SCRIPTS))
    loaded = []
    for name in ("market_analysis", "backtest"):
        spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
        assert spec is not None
        assert spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        loaded.append(module)
    return loaded[0], loaded[1]


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
    for kwargs in ({"top_k": 0}, {"buckets": 0}, {"min_history": 0}, {"horizons": ()}):
        with pytest.raises(ValueError, match="positive"):
            backtest.run_backtest({}, **kwargs)


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
    assert empty["metrics"]["1d"]["top_k"]["average_return"] is None
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
    gapped = _bars(ma, "GAPPED", 1.0, count=3)
    gapped = [
        replace(bar, timestamp=bar.timestamp + timedelta(days=10 * index))
        for index, bar in enumerate(gapped)
    ]
    unreliable = backtest.run_backtest({"GAPPED": gapped}, horizons=(1,), min_history=2)
    assert unreliable["observations"] == 0


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
    artifact = json.loads(next(output.glob("*.json")).read_text())
    assert artifact["scoring_version"] == ma.SCORING_VERSION
    assert artifact["config"]["forward_horizons"] == [1, 5]
    assert artifact["date_range"]["start"] == "2024-01-01"


def test_main_rejects_missing_inputs(
    modules: tuple[ModuleType, ModuleType], tmp_path: Path
) -> None:
    _, backtest = modules
    with pytest.raises(SystemExit):
        backtest.main(["--symbols", ","])
    with pytest.raises(SystemExit):
        backtest.main(["--symbols", "MISSING", "--data-dir", str(tmp_path)])
