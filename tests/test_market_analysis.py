from __future__ import annotations

import importlib.util
import json
import math
import sys
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import TYPE_CHECKING
from urllib.error import URLError

import pytest

if TYPE_CHECKING:
    from types import ModuleType

    from pytest_mock import MockerFixture

SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / ".agents"
    / "skills"
    / "market-analysis"
    / "scripts"
    / "market_analysis.py"
)


@pytest.fixture(scope="module")
def ma() -> ModuleType:
    spec = importlib.util.spec_from_file_location("market_analysis", SCRIPT_PATH)
    if spec is None or spec.loader is None:
        pytest.fail("Failed to load market_analysis.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


# ── Helpers ────────────────────────────────────────────────────────────────────


def _bar(
    ma: ModuleType,
    symbol: str,
    close: float,
    ts: datetime,
    *,
    open_: float | None = None,
    high: float | None = None,
    low: float | None = None,
    interval: str = "d",
) -> object:
    o = open_ if open_ is not None else close
    h = high if high is not None else close
    lo = low if low is not None else close
    return ma.OhlcvBar(
        symbol=symbol,
        timestamp=ts,
        open=o,
        high=h,
        low=lo,
        close=close,
        volume=1000.0,
        source="test",
        interval=interval,
    )


def _make_bars(
    ma: ModuleType,
    symbol: str,
    closes: list[float],
    *,
    interval: str = "d",
    start: datetime | None = None,
) -> list[object]:
    base = start if start is not None else datetime(2023, 1, 2, tzinfo=UTC)
    bars = []
    for i, c in enumerate(closes):
        ts = base + timedelta(days=i)
        bars.append(_bar(ma, symbol, c, ts, interval=interval))
    return bars


# ── OhlcvBar ────────────────────────────────────────────────────────────────────


def test_ohlcvbar_is_frozen(ma: ModuleType) -> None:
    ts = datetime(2024, 1, 2, tzinfo=UTC)
    bar = ma.OhlcvBar("A", ts, 1.0, 2.0, 0.5, 1.5, 100.0, "test", "d")
    with pytest.raises(AttributeError):
        bar.close = 99.0  # type: ignore[misc]


def test_ohlcvbar_utc_timestamp(ma: ModuleType) -> None:
    ts = datetime(2024, 1, 2, tzinfo=UTC)
    bar = ma.OhlcvBar("X", ts, 1.0, 1.0, 1.0, 1.0, 0.0, "test", "d")
    assert bar.timestamp.tzinfo is not None


# ── StooqProvider._parse_csv ────────────────────────────────────────────────────


def test_parse_csv_valid(ma: ModuleType) -> None:
    provider = ma.StooqProvider()
    content = "Date,Open,High,Low,Close,Volume\n2024-01-02,100,110,90,105,1000\n"
    bars = provider._parse_csv(content, "AAPL.US", "d")
    assert len(bars) == 1
    assert bars[0].close == 105.0
    assert bars[0].timestamp == datetime(2024, 1, 2, tzinfo=UTC)


def test_parse_csv_skips_missing_date(ma: ModuleType) -> None:
    provider = ma.StooqProvider()
    content = "Date,Open,High,Low,Close,Volume\n,100,110,90,105,1000\n"
    bars = provider._parse_csv(content, "X", "d")
    assert bars == []


def test_parse_csv_skips_malformed_row(ma: ModuleType) -> None:
    provider = ma.StooqProvider()
    content = "Date,Open,High,Low,Close,Volume\n2024-01-02,bad,110,90,105,1000\n"
    bars = provider._parse_csv(content, "X", "d")
    assert bars == []


def test_parse_csv_sorted_ascending(ma: ModuleType) -> None:
    provider = ma.StooqProvider()
    content = (
        "Date,Open,High,Low,Close,Volume\n"
        "2024-01-03,103,113,93,108,1100\n"
        "2024-01-02,100,110,90,105,1000\n"
    )
    bars = provider._parse_csv(content, "X", "d")
    assert bars[0].timestamp < bars[1].timestamp


def test_stooq_provider_fetch_ohlcv(ma: ModuleType, mocker: MockerFixture) -> None:
    csv_content = "Date,Open,High,Low,Close,Volume\n2024-01-02,100,110,90,105,1000\n"
    mock_resp = mocker.MagicMock()
    mock_resp.read.return_value = csv_content.encode()
    mock_resp.__enter__ = mocker.MagicMock(return_value=mock_resp)
    mock_resp.__exit__ = mocker.MagicMock(return_value=False)
    mocker.patch("market_analysis.urlopen", return_value=mock_resp)
    provider = ma.StooqProvider()
    start = datetime(2024, 1, 1, tzinfo=UTC)
    end = datetime(2024, 1, 31, tzinfo=UTC)
    bars = provider.fetch_ohlcv("AAPL.US", start, end)
    assert len(bars) == 1
    assert bars[0].source == "stooq"


# ── CsvFileProvider ────────────────────────────────────────────────────────────


def test_csv_file_provider_filters_range(ma: ModuleType, tmp_path: Path) -> None:
    closes = [float(100 + i) for i in range(5)]
    bars = _make_bars(ma, "TEST", closes)
    ma.save_ohlcv(bars, tmp_path)
    provider = ma.CsvFileProvider(tmp_path)
    start = datetime(2023, 1, 3, tzinfo=UTC)
    end = datetime(2023, 1, 4, tzinfo=UTC)
    result = provider.fetch_ohlcv("TEST", start, end)
    assert len(result) == 2
    assert all(start <= b.timestamp <= end for b in result)


# ── ohlcv_csv_path ─────────────────────────────────────────────────────────────


def test_ohlcv_csv_path_slash(ma: ModuleType, tmp_path: Path) -> None:
    path = ma.ohlcv_csv_path("BTC/USD", "d", tmp_path)
    assert "BTC-USD" in path.name


def test_ohlcv_csv_path_caret(ma: ModuleType, tmp_path: Path) -> None:
    path = ma.ohlcv_csv_path("^SPX", "d", tmp_path)
    assert "_SPX" in path.name


# ── save_ohlcv / load_ohlcv ────────────────────────────────────────────────────


def test_save_ohlcv_roundtrip(ma: ModuleType, tmp_path: Path) -> None:
    bars = _make_bars(ma, "AAPL.US", [100.0, 101.0, 102.0])
    path = ma.save_ohlcv(bars, tmp_path)
    assert path.exists()
    loaded = ma.load_ohlcv("AAPL.US", "d", tmp_path)
    assert len(loaded) == 3
    assert loaded[0].close == 100.0
    assert loaded[0].timestamp.tzinfo is not None


def test_save_ohlcv_raises_on_empty(ma: ModuleType) -> None:
    with pytest.raises(ValueError, match="empty"):
        ma.save_ohlcv([])


def test_load_ohlcv_raises_file_not_found(ma: ModuleType, tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        ma.load_ohlcv("NOTEXIST", "d", tmp_path)


def test_load_ohlcv_naive_timestamp_gets_utc(ma: ModuleType, tmp_path: Path) -> None:
    # Write a CSV with a naive timestamp (no +00:00) to test the tzinfo fix
    path = tmp_path / "TEST_d.csv"
    path.write_text(
        "symbol,timestamp,open,high,low,close,volume,source,interval\n"
        "TEST,2024-01-02T00:00:00,100,100,100,100,0,test,d\n"
    )
    loaded = ma.load_ohlcv("TEST", "d", tmp_path)
    assert loaded[0].timestamp.tzinfo is not None


# ── check_data_quality ─────────────────────────────────────────────────────────


def test_quality_empty_bars(ma: ModuleType) -> None:
    report = ma.check_data_quality([])
    assert not report.is_valid
    assert any("empty" in i for i in report.issues)


def test_quality_stale_data(ma: ModuleType) -> None:
    bars = _make_bars(ma, "X", [100.0] * 70)
    ref = bars[-1].timestamp + timedelta(days=10)
    report = ma.check_data_quality(bars, stale_days=5, reference_time=ref)
    assert any("stale" in i for i in report.issues)


def test_quality_not_stale(ma: ModuleType) -> None:
    bars = _make_bars(ma, "X", [100.0] * 70)
    ref = bars[-1].timestamp + timedelta(days=2)
    report = ma.check_data_quality(bars, stale_days=5, reference_time=ref)
    assert not any("stale" in i for i in report.issues)


def test_quality_insufficient_history(ma: ModuleType) -> None:
    bars = _make_bars(ma, "X", [100.0] * 5)
    ref = bars[-1].timestamp + timedelta(days=1)
    report = ma.check_data_quality(bars, min_history=10, reference_time=ref)
    assert any("insufficient" in i for i in report.issues)


def test_quality_sufficient_history(ma: ModuleType) -> None:
    bars = _make_bars(ma, "X", [100.0] * 70)
    ref = bars[-1].timestamp + timedelta(days=1)
    report = ma.check_data_quality(bars, min_history=60, reference_time=ref)
    assert not any("insufficient" in i for i in report.issues)


def test_quality_malformed_nonpositive(ma: ModuleType) -> None:
    bars = _make_bars(ma, "X", [100.0] * 70)
    ref = bars[-1].timestamp + timedelta(days=1)
    bad_ts = bars[0].timestamp
    bad = ma.OhlcvBar("X", bad_ts, -1.0, 100.0, 0.5, 100.0, 0.0, "test", "d")
    report = ma.check_data_quality([bad, *bars[1:]], min_history=1, reference_time=ref)
    assert any("non-positive" in i for i in report.issues)


def test_quality_malformed_high_lt_low(ma: ModuleType) -> None:
    bars = _make_bars(ma, "X", [100.0] * 70)
    ref = bars[-1].timestamp + timedelta(days=1)
    bad_ts = bars[0].timestamp
    bad = ma.OhlcvBar("X", bad_ts, 100.0, 90.0, 110.0, 100.0, 0.0, "test", "d")
    report = ma.check_data_quality([bad, *bars[1:]], min_history=1, reference_time=ref)
    assert any("high < low" in i for i in report.issues)


def test_quality_malformed_open_outside_range(ma: ModuleType) -> None:
    bars = _make_bars(ma, "X", [100.0] * 70)
    ref = bars[-1].timestamp + timedelta(days=1)
    bad_ts = bars[0].timestamp
    bad = ma.OhlcvBar("X", bad_ts, 200.0, 110.0, 90.0, 100.0, 0.0, "test", "d")
    report = ma.check_data_quality([bad, *bars[1:]], min_history=1, reference_time=ref)
    assert any("open outside" in i for i in report.issues)


def test_quality_malformed_close_outside_range(ma: ModuleType) -> None:
    bars = _make_bars(ma, "X", [100.0] * 70)
    ref = bars[-1].timestamp + timedelta(days=1)
    bad_ts = bars[0].timestamp
    bad = ma.OhlcvBar("X", bad_ts, 100.0, 110.0, 90.0, 5.0, 0.0, "test", "d")
    report = ma.check_data_quality([bad, *bars[1:]], min_history=1, reference_time=ref)
    assert any("close outside" in i for i in report.issues)


def test_quality_all_clear(ma: ModuleType) -> None:
    bars = _make_bars(ma, "X", [100.0 + i for i in range(70)])
    ref = bars[-1].timestamp + timedelta(days=1)
    report = ma.check_data_quality(bars, min_history=60, reference_time=ref)
    assert report.is_valid


def test_quality_duplicate_timestamps(ma: ModuleType) -> None:
    ts = datetime(2024, 1, 2, tzinfo=UTC)
    bar = ma.OhlcvBar("X", ts, 100.0, 110.0, 90.0, 100.0, 0.0, "test", "d")
    report = ma.check_data_quality(
        [bar, bar], min_history=1, reference_time=ts + timedelta(days=1)
    )
    assert any("duplicate" in i for i in report.issues)


def test_quality_large_gap_detected(ma: ModuleType) -> None:
    ts1 = datetime(2024, 1, 2, tzinfo=UTC)
    ts2 = datetime(2024, 2, 2, tzinfo=UTC)
    bar1 = ma.OhlcvBar("X", ts1, 100.0, 100.0, 100.0, 100.0, 0.0, "test", "d")
    bar2 = ma.OhlcvBar("X", ts2, 100.0, 100.0, 100.0, 100.0, 0.0, "test", "d")
    ref = ts2 + timedelta(days=1)
    report = ma.check_data_quality([bar1, bar2], min_history=1, reference_time=ref)
    assert any("gap" in i or "missing" in i for i in report.issues)


def test_quality_no_gap_with_two_bars(ma: ModuleType) -> None:
    ts1 = datetime(2024, 1, 2, tzinfo=UTC)
    ts2 = datetime(2024, 1, 3, tzinfo=UTC)
    bar1 = ma.OhlcvBar("X", ts1, 100.0, 100.0, 100.0, 100.0, 0.0, "test", "d")
    bar2 = ma.OhlcvBar("X", ts2, 100.0, 100.0, 100.0, 100.0, 0.0, "test", "d")
    ref = ts2 + timedelta(days=1)
    report = ma.check_data_quality([bar1, bar2], min_history=1, reference_time=ref)
    assert not any("gap" in i or "missing" in i for i in report.issues)


def test_quality_single_bar_no_gap_check(ma: ModuleType) -> None:
    ts = datetime(2024, 1, 2, tzinfo=UTC)
    bar = ma.OhlcvBar("X", ts, 100.0, 100.0, 100.0, 100.0, 0.0, "test", "d")
    ref = ts + timedelta(days=1)
    report = ma.check_data_quality([bar], min_history=1, reference_time=ref)
    assert not any("gap" in i or "missing" in i for i in report.issues)


# ── Feature helpers ────────────────────────────────────────────────────────────


def test_compute_return_insufficient(ma: ModuleType) -> None:
    assert ma._compute_return([100.0], 1) is None


def test_compute_return_sufficient(ma: ModuleType) -> None:
    result = ma._compute_return([100.0, 110.0], 1)
    assert result is not None
    assert abs(result - 0.10) < 1e-9


def test_compute_ma_distance_insufficient(ma: ModuleType) -> None:
    assert ma._compute_ma_distance([100.0] * 19, 20) is None


def test_compute_ma_distance_sufficient(ma: ModuleType) -> None:
    closes = [100.0] * 19 + [120.0]
    result = ma._compute_ma_distance(closes, 20)
    assert result is not None
    assert result > 0


def test_compute_realized_vol_insufficient(ma: ModuleType) -> None:
    assert ma._compute_realized_vol([100.0] * 20, 20) is None


def test_compute_realized_vol_sufficient(ma: ModuleType) -> None:
    closes = [100.0 + i for i in range(22)]
    result = ma._compute_realized_vol(closes, 20)
    assert result is not None
    assert result >= 0


def test_compute_max_drawdown_empty(ma: ModuleType) -> None:
    assert ma._compute_max_drawdown([], 60) is None


def test_compute_max_drawdown_monotone_up(ma: ModuleType) -> None:
    closes = [float(100 + i) for i in range(10)]
    result = ma._compute_max_drawdown(closes, 60)
    assert result is not None
    assert result == pytest.approx(0.0)


def test_compute_max_drawdown_with_drop(ma: ModuleType) -> None:
    closes = [1.0, 3.0, 2.0]
    result = ma._compute_max_drawdown(closes, 60)
    assert result is not None
    assert result == pytest.approx(1.0 / 3.0)


def test_compute_rsi_insufficient(ma: ModuleType) -> None:
    assert ma._compute_rsi([100.0] * 14, 14) is None


def test_compute_rsi_all_gains(ma: ModuleType) -> None:
    closes = [float(100 + i) for i in range(16)]
    result = ma._compute_rsi(closes, 14)
    assert result == pytest.approx(100.0)


def test_compute_rsi_mixed(ma: ModuleType) -> None:
    closes = [
        100.0,
        110.0,
        105.0,
        108.0,
        103.0,
        107.0,
        102.0,
        106.0,
        101.0,
        105.0,
        100.0,
        104.0,
        99.0,
        103.0,
        98.0,
    ]
    result = ma._compute_rsi(closes, 14)
    assert result is not None
    assert 0.0 < result < 100.0


def test_compute_zscore_insufficient(ma: ModuleType) -> None:
    assert ma._compute_zscore([100.0] * 19, 20) is None


def test_compute_zscore_flat(ma: ModuleType) -> None:
    result = ma._compute_zscore([100.0] * 20, 20)
    assert result == pytest.approx(0.0)


def test_compute_zscore_varying(ma: ModuleType) -> None:
    closes = [float(100 + (i % 3)) for i in range(20)]
    result = ma._compute_zscore(closes, 20)
    assert result is not None


def test_compute_features_few_bars(ma: ModuleType) -> None:
    bars = _make_bars(ma, "X", [100.0, 101.0, 102.0])
    feats = ma.compute_features(bars)
    assert feats.ret_1d is not None
    assert feats.ret_60d is None
    assert feats.ma20_dist is None
    assert feats.rsi_14 is None


def test_compute_features_full(ma: ModuleType) -> None:
    closes = [float(100 + i) for i in range(80)]
    bars = _make_bars(ma, "X", closes)
    feats = ma.compute_features(bars)
    assert feats.ret_1d is not None
    assert feats.ret_60d is not None
    assert feats.ma20_dist is not None
    assert feats.ma50_dist is not None
    assert feats.rsi_14 is not None
    assert feats.zscore_20d is not None


# ── _percentile_rank ──────────────────────────────────────────────────────────


def test_percentile_rank_all_none(ma: ModuleType) -> None:
    assert ma._percentile_rank([None, None], 0) == pytest.approx(50.0)


def test_percentile_rank_this_none(ma: ModuleType) -> None:
    assert ma._percentile_rank([1.0, None, 2.0], 1) == pytest.approx(50.0)


def test_percentile_rank_lowest(ma: ModuleType) -> None:
    assert ma._percentile_rank([1.0, 2.0, 3.0], 0) == pytest.approx(0.0)


def test_percentile_rank_highest(ma: ModuleType) -> None:
    result = ma._percentile_rank([1.0, 2.0, 3.0], 2)
    assert result == pytest.approx(200.0 / 3.0)


# ── _collect_risk_gates ────────────────────────────────────────────────────────


def _empty_features(ma: ModuleType) -> object:
    return ma.InstrumentFeatures(
        ret_1d=None,
        ret_5d=None,
        ret_20d=None,
        ret_60d=None,
        ma20_dist=None,
        ma50_dist=None,
        vol_20d=None,
        mdd_60d=None,
        rsi_14=None,
        zscore_20d=None,
    )


def _report(ma: ModuleType, issues: list[str]) -> object:
    return ma.DataQualityReport(symbol="X", interval="d", bar_count=1, issues=issues)


def test_collect_gates_no_issues_no_vol(ma: ModuleType) -> None:
    gates = ma._collect_risk_gates(_report(ma, []), _empty_features(ma))
    assert gates == []


def test_collect_gates_stale(ma: ModuleType) -> None:
    gates = ma._collect_risk_gates(
        _report(ma, ["stale data: ..."]), _empty_features(ma)
    )
    assert ma.RISK_GATE_STALE in gates


def test_collect_gates_insufficient(ma: ModuleType) -> None:
    gates = ma._collect_risk_gates(
        _report(ma, ["insufficient history: 5 bars"]), _empty_features(ma)
    )
    assert ma.RISK_GATE_INSUFFICIENT in gates


def test_collect_gates_missing_bars(ma: ModuleType) -> None:
    gates = ma._collect_risk_gates(
        _report(ma, ["possible missing bars: 30-day gap"]), _empty_features(ma)
    )
    assert ma.RISK_GATE_MISSING_BARS in gates


def test_collect_gates_malformed(ma: ModuleType) -> None:
    gates = ma._collect_risk_gates(
        _report(ma, ["malformed OHLC at index 0"]), _empty_features(ma)
    )
    assert ma.RISK_GATE_MALFORMED in gates


def test_collect_gates_high_vol(ma: ModuleType) -> None:
    feats = ma.InstrumentFeatures(
        ret_1d=None,
        ret_5d=None,
        ret_20d=None,
        ret_60d=None,
        ma20_dist=None,
        ma50_dist=None,
        vol_20d=2.0,
        mdd_60d=None,
        rsi_14=None,
        zscore_20d=None,
    )
    gates = ma._collect_risk_gates(_report(ma, []), feats)
    assert ma.RISK_GATE_HIGH_VOL in gates


def test_collect_gates_low_vol_not_flagged(ma: ModuleType) -> None:
    feats = ma.InstrumentFeatures(
        ret_1d=None,
        ret_5d=None,
        ret_20d=None,
        ret_60d=None,
        ma20_dist=None,
        ma50_dist=None,
        vol_20d=0.3,
        mdd_60d=None,
        rsi_14=None,
        zscore_20d=None,
    )
    gates = ma._collect_risk_gates(_report(ma, []), feats)
    assert ma.RISK_GATE_HIGH_VOL not in gates


# ── _build_explanation ─────────────────────────────────────────────────────────


def _full_features(ma: ModuleType) -> object:
    return ma.InstrumentFeatures(
        ret_1d=0.01,
        ret_5d=0.02,
        ret_20d=0.05,
        ret_60d=0.10,
        ma20_dist=0.03,
        ma50_dist=0.02,
        vol_20d=0.20,
        mdd_60d=0.05,
        rsi_14=60.0,
        zscore_20d=0.5,
    )


def test_build_explanation_with_gates(ma: ModuleType) -> None:
    expl = ma._build_explanation("X", _empty_features(ma), ["stale_data"])
    assert "Suppressed" in expl
    assert "stale_data" in expl


def test_build_explanation_no_features(ma: ModuleType) -> None:
    expl = ma._build_explanation("X", _empty_features(ma), [])
    assert "insufficient" in expl


def test_build_explanation_full_features(ma: ModuleType) -> None:
    expl = ma._build_explanation("X", _full_features(ma), [])
    assert "20d" in expl
    assert "MA20" in expl
    assert "RSI14" in expl


# ── score_instruments ──────────────────────────────────────────────────────────


def test_score_instruments_empty(ma: ModuleType) -> None:
    assert ma.score_instruments({}) == []


def test_score_single_instrument(ma: ModuleType) -> None:
    bars = _make_bars(ma, "A", [float(100 + i) for i in range(80)])
    ref = bars[-1].timestamp + timedelta(days=1)
    results = ma.score_instruments({"A": bars}, reference_time=ref)
    assert len(results) == 1
    assert results[0].rank == 1


def test_score_multiple_instruments(ma: ModuleType) -> None:
    up = _make_bars(ma, "UP", [float(100 + i) for i in range(80)])
    down = _make_bars(ma, "DOWN", [float(100 - i * 0.5) for i in range(80)])
    ref = up[-1].timestamp + timedelta(days=1)
    results = ma.score_instruments({"UP": up, "DOWN": down}, reference_time=ref)
    assert len(results) == 2
    assert results[0].rank == 1
    assert results[1].rank == 2
    symbols = [r.symbol for r in results]
    assert symbols[0] == "UP"


def test_score_risk_gate_stale(ma: ModuleType) -> None:
    bars = _make_bars(ma, "X", [100.0] * 70)
    ref = bars[-1].timestamp + timedelta(days=30)
    results = ma.score_instruments({"X": bars}, reference_time=ref, stale_days=5)
    assert not results[0].is_reliable
    assert ma.RISK_GATE_STALE in results[0].risk_gates


def test_score_risk_gate_insufficient(ma: ModuleType) -> None:
    bars = _make_bars(ma, "X", [100.0] * 5)
    ref = bars[-1].timestamp + timedelta(days=1)
    results = ma.score_instruments({"X": bars}, reference_time=ref, min_history=60)
    assert not results[0].is_reliable
    assert ma.RISK_GATE_INSUFFICIENT in results[0].risk_gates


def test_score_risk_gate_high_vol(ma: ModuleType) -> None:
    factor = math.exp(0.1)
    closes = [100.0 * (factor if i % 2 == 0 else 1.0 / factor) for i in range(80)]
    bars = _make_bars(ma, "X", closes)
    ref = bars[-1].timestamp + timedelta(days=1)
    results = ma.score_instruments({"X": bars}, reference_time=ref)
    if results[0].features.vol_20d is not None and results[0].features.vol_20d > 1.0:
        assert ma.RISK_GATE_HIGH_VOL in results[0].risk_gates


def test_score_risk_gate_missing_bars(ma: ModuleType) -> None:
    ts1 = datetime(2023, 1, 2, tzinfo=UTC)
    ts2 = datetime(2023, 6, 1, tzinfo=UTC)
    bars = [
        ma.OhlcvBar("X", ts1, 100.0, 100.0, 100.0, 100.0, 0.0, "test", "d"),
        ma.OhlcvBar("X", ts2, 100.0, 100.0, 100.0, 100.0, 0.0, "test", "d"),
    ]
    ref = ts2 + timedelta(days=1)
    results = ma.score_instruments({"X": bars}, reference_time=ref, min_history=1)
    assert ma.RISK_GATE_MISSING_BARS in results[0].risk_gates


def test_score_risk_gate_malformed(ma: ModuleType) -> None:
    bars = _make_bars(ma, "X", [100.0] * 70)
    ref = bars[-1].timestamp + timedelta(days=1)
    bad_ts = bars[0].timestamp
    bad = ma.OhlcvBar("X", bad_ts, -1.0, 100.0, 100.0, 100.0, 0.0, "test", "d")
    mixed = [bad, *bars[1:]]
    results = ma.score_instruments({"X": mixed}, reference_time=ref)
    assert ma.RISK_GATE_MALFORMED in results[0].risk_gates


# ── _get_git_commit ─────────────────────────────────────────────────────────────


def test_get_git_commit_success(ma: ModuleType, mocker: MockerFixture) -> None:
    mock_result = mocker.MagicMock()
    mock_result.returncode = 0
    mock_result.stdout = "abc1234\n"
    mocker.patch("subprocess.run", return_value=mock_result)
    commit = ma._get_git_commit()
    assert commit == "abc1234"


def test_get_git_commit_nonzero(ma: ModuleType, mocker: MockerFixture) -> None:
    mock_result = mocker.MagicMock()
    mock_result.returncode = 1
    mock_result.stdout = ""
    mocker.patch("subprocess.run", return_value=mock_result)
    assert ma._get_git_commit() == "unknown"


def test_get_git_commit_oserror(ma: ModuleType, mocker: MockerFixture) -> None:
    mocker.patch("subprocess.run", side_effect=OSError("git not found"))
    assert ma._get_git_commit() == "unknown"


# ── generate_artifact / save_artifact ─────────────────────────────────────────


def test_generate_artifact_structure(ma: ModuleType, mocker: MockerFixture) -> None:
    mocker.patch.object(ma, "_get_git_commit", return_value="abc1234")
    bars = _make_bars(ma, "A", [float(100 + i) for i in range(80)])
    ref = bars[-1].timestamp + timedelta(days=1)
    scores = ma.score_instruments({"A": bars}, reference_time=ref)
    artifact = ma.generate_artifact(scores, {"A": bars}, {"stale_days": 5})
    assert artifact["version"] == "1.0.0"
    assert "metadata" in artifact
    assert "instruments" in artifact
    meta = artifact["metadata"]
    assert meta["git_commit"] == "abc1234"
    assert "generated_at" in meta
    assert meta["data_source"] == "test"


def test_generate_artifact_empty_data_source(
    ma: ModuleType, mocker: MockerFixture
) -> None:
    mocker.patch.object(ma, "_get_git_commit", return_value="unknown")
    artifact = ma.generate_artifact([], {}, {})
    assert artifact["metadata"]["data_source"] == "unknown"


def test_save_artifact_path_contains_date(
    ma: ModuleType, mocker: MockerFixture, tmp_path: Path
) -> None:
    mocker.patch.object(ma, "_get_git_commit", return_value="abc")
    bars = _make_bars(ma, "A", [float(100 + i) for i in range(80)])
    ref = bars[-1].timestamp + timedelta(days=1)
    scores = ma.score_instruments({"A": bars}, reference_time=ref)
    artifact = ma.generate_artifact(scores, {"A": bars}, {})
    path = ma.save_artifact(artifact, tmp_path)
    assert path.suffix == ".json"
    loaded = json.loads(path.read_text())
    assert loaded["version"] == "1.0.0"


def test_save_artifact_no_generated_at(ma: ModuleType, tmp_path: Path) -> None:
    artifact: dict = {"version": "1.0.0", "instruments": []}
    path = ma.save_artifact(artifact, tmp_path)
    assert path.exists()


# ── CLI: _cmd_fetch ───────────────────────────────────────────────────────────


def test_cmd_fetch_success(
    ma: ModuleType, mocker: MockerFixture, tmp_path: Path
) -> None:
    csv_content = "Date,Open,High,Low,Close,Volume\n2024-01-02,100,110,90,105,1000\n"
    mock_resp = mocker.MagicMock()
    mock_resp.read.return_value = csv_content.encode()
    mock_resp.__enter__ = mocker.MagicMock(return_value=mock_resp)
    mock_resp.__exit__ = mocker.MagicMock(return_value=False)
    mocker.patch("market_analysis.urlopen", return_value=mock_resp)
    mocker.patch.object(
        sys,
        "argv",
        [
            "market_analysis.py",
            "fetch",
            "--symbol",
            "AAPL.US",
            "--start",
            "2024-01-01",
            "--end",
            "2024-01-31",
            "--output",
            str(tmp_path),
        ],
    )
    result = ma.main()
    assert result == 0


def test_cmd_fetch_url_error(
    ma: ModuleType, mocker: MockerFixture, tmp_path: Path
) -> None:
    mocker.patch("market_analysis.urlopen", side_effect=URLError("network error"))
    mocker.patch.object(
        sys,
        "argv",
        [
            "market_analysis.py",
            "fetch",
            "--symbol",
            "AAPL.US",
            "--start",
            "2024-01-01",
            "--end",
            "2024-01-31",
            "--output",
            str(tmp_path),
        ],
    )
    result = ma.main()
    assert result == 1


def test_cmd_fetch_no_data(
    ma: ModuleType, mocker: MockerFixture, tmp_path: Path
) -> None:
    csv_content = "Date,Open,High,Low,Close,Volume\n"
    mock_resp = mocker.MagicMock()
    mock_resp.read.return_value = csv_content.encode()
    mock_resp.__enter__ = mocker.MagicMock(return_value=mock_resp)
    mock_resp.__exit__ = mocker.MagicMock(return_value=False)
    mocker.patch("market_analysis.urlopen", return_value=mock_resp)
    mocker.patch.object(
        sys,
        "argv",
        [
            "market_analysis.py",
            "fetch",
            "--symbol",
            "AAPL.US",
            "--start",
            "2024-01-01",
            "--end",
            "2024-01-31",
            "--output",
            str(tmp_path),
        ],
    )
    result = ma.main()
    assert result == 1


def test_cmd_fetch_no_validate_flag(
    ma: ModuleType, mocker: MockerFixture, tmp_path: Path
) -> None:
    csv_content = "Date,Open,High,Low,Close,Volume\n2024-01-02,100,110,90,105,1000\n"
    mock_resp = mocker.MagicMock()
    mock_resp.read.return_value = csv_content.encode()
    mock_resp.__enter__ = mocker.MagicMock(return_value=mock_resp)
    mock_resp.__exit__ = mocker.MagicMock(return_value=False)
    mocker.patch("market_analysis.urlopen", return_value=mock_resp)
    mocker.patch.object(
        sys,
        "argv",
        [
            "market_analysis.py",
            "fetch",
            "--symbol",
            "AAPL.US",
            "--start",
            "2024-01-01",
            "--end",
            "2024-01-31",
            "--output",
            str(tmp_path),
            "--no-validate",
        ],
    )
    result = ma.main()
    assert result == 0


def test_cmd_fetch_reports_quality_issues(
    ma: ModuleType,
    mocker: MockerFixture,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    csv_content = "Date,Open,High,Low,Close,Volume\n2020-01-02,100,110,90,105,1000\n"
    mock_resp = mocker.MagicMock()
    mock_resp.read.return_value = csv_content.encode()
    mock_resp.__enter__ = mocker.MagicMock(return_value=mock_resp)
    mock_resp.__exit__ = mocker.MagicMock(return_value=False)
    mocker.patch("market_analysis.urlopen", return_value=mock_resp)
    mocker.patch.object(
        sys,
        "argv",
        [
            "market_analysis.py",
            "fetch",
            "--symbol",
            "AAPL.US",
            "--start",
            "2020-01-01",
            "--end",
            "2020-01-31",
            "--output",
            str(tmp_path),
        ],
    )
    result = ma.main()
    assert result == 0
    output = capsys.readouterr().out
    assert "WARNING" in output


# ── CLI: _cmd_check ───────────────────────────────────────────────────────────


def test_cmd_check_valid(ma: ModuleType, mocker: MockerFixture, tmp_path: Path) -> None:
    bars = _make_bars(ma, "A", [float(100 + i) for i in range(70)])
    ma.save_ohlcv(bars, tmp_path)
    ref_ts = bars[-1].timestamp + timedelta(days=1)
    mocker.patch.object(
        ma,
        "check_data_quality",
        return_value=ma.DataQualityReport("A", "d", len(bars)),
    )
    mocker.patch.object(
        sys,
        "argv",
        [
            "market_analysis.py",
            "check",
            "--symbol",
            "A",
            "--data-dir",
            str(tmp_path),
        ],
    )
    _ = ref_ts
    result = ma.main()
    assert result == 0


def test_cmd_check_file_not_found(
    ma: ModuleType, mocker: MockerFixture, tmp_path: Path
) -> None:
    mocker.patch.object(
        sys,
        "argv",
        [
            "market_analysis.py",
            "check",
            "--symbol",
            "NOEXIST",
            "--data-dir",
            str(tmp_path),
        ],
    )
    result = ma.main()
    assert result == 1


# ── CLI: _cmd_check (direct) ──────────────────────────────────────────────────


def test_cmd_check_direct_valid(ma: ModuleType, tmp_path: Path) -> None:
    today = datetime.now(tz=UTC)
    bars = _make_bars(
        ma, "B", [float(100 + i) for i in range(70)], start=today - timedelta(days=69)
    )
    ma.save_ohlcv(bars, tmp_path)

    class Args:
        symbol = "B"
        interval = "d"
        data_dir = str(tmp_path)

    result = ma._cmd_check(Args())
    assert result == 0


def test_cmd_check_direct_invalid(ma: ModuleType, tmp_path: Path) -> None:
    bars = _make_bars(ma, "B", [100.0] * 3)
    ma.save_ohlcv(bars, tmp_path)

    class Args:
        symbol = "B"
        interval = "d"
        data_dir = str(tmp_path)

    result = ma._cmd_check(Args())
    assert result == 1


def test_cmd_check_direct_not_found(ma: ModuleType, tmp_path: Path) -> None:
    class Args:
        symbol = "NOFILE"
        interval = "d"
        data_dir = str(tmp_path)

    result = ma._cmd_check(Args())
    assert result == 1


# ── CLI: _cmd_score ───────────────────────────────────────────────────────────


def test_cmd_score_no_data(ma: ModuleType, tmp_path: Path) -> None:
    class Args:
        symbols = "NOEXIST"
        interval = "d"
        data_dir = str(tmp_path)

    result = ma._cmd_score(Args())
    assert result == 1


def test_cmd_score_success(ma: ModuleType, tmp_path: Path) -> None:
    bars = _make_bars(ma, "C", [float(100 + i) for i in range(70)])
    ma.save_ohlcv(bars, tmp_path)

    class Args:
        symbols = "C"
        interval = "d"
        data_dir = str(tmp_path)

    result = ma._cmd_score(Args())
    assert result == 0


def test_cmd_score_partial_missing(
    ma: ModuleType, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    bars = _make_bars(ma, "D", [float(100 + i) for i in range(70)])
    ma.save_ohlcv(bars, tmp_path)

    class Args:
        symbols = "D,MISSING"
        interval = "d"
        data_dir = str(tmp_path)

    result = ma._cmd_score(Args())
    assert result == 0
    assert "WARNING" in capsys.readouterr().out


# ── CLI: _cmd_generate ────────────────────────────────────────────────────────


def test_cmd_generate_no_data(ma: ModuleType, tmp_path: Path) -> None:
    class Args:
        symbols = "NOEXIST"
        interval = "d"
        data_dir = str(tmp_path)
        output = str(tmp_path / "analysis")

    result = ma._cmd_generate(Args())
    assert result == 1


def test_cmd_generate_success(
    ma: ModuleType, mocker: MockerFixture, tmp_path: Path
) -> None:
    mocker.patch.object(ma, "_get_git_commit", return_value="abc")
    bars = _make_bars(ma, "E", [float(100 + i) for i in range(70)])
    ma.save_ohlcv(bars, tmp_path)

    class Args:
        symbols = "E"
        interval = "d"
        data_dir = str(tmp_path)
        output = str(tmp_path / "analysis")

    result = ma._cmd_generate(Args())
    assert result == 0
    analysis_dir = tmp_path / "analysis"
    json_files = list(analysis_dir.glob("*.json"))
    assert len(json_files) == 1


# ── CLI: main routing ─────────────────────────────────────────────────────────


def test_main_routes_fetch(ma: ModuleType, mocker: MockerFixture) -> None:
    called = []
    mocker.patch.object(
        ma, "_cmd_fetch", side_effect=lambda _a: called.append("fetch") or 0
    )
    mocker.patch.object(
        sys,
        "argv",
        [
            "market_analysis.py",
            "fetch",
            "--symbol",
            "X",
            "--start",
            "2024-01-01",
            "--end",
            "2024-01-31",
        ],
    )
    ma.main()
    assert called == ["fetch"]


def test_main_routes_check(ma: ModuleType, mocker: MockerFixture) -> None:
    called = []
    mocker.patch.object(
        ma, "_cmd_check", side_effect=lambda _a: called.append("check") or 0
    )
    mocker.patch.object(
        sys,
        "argv",
        [
            "market_analysis.py",
            "check",
            "--symbol",
            "X",
        ],
    )
    ma.main()
    assert called == ["check"]


def test_main_routes_score(ma: ModuleType, mocker: MockerFixture) -> None:
    called = []
    mocker.patch.object(
        ma, "_cmd_score", side_effect=lambda _a: called.append("score") or 0
    )
    mocker.patch.object(
        sys,
        "argv",
        [
            "market_analysis.py",
            "score",
            "--symbols",
            "X",
        ],
    )
    ma.main()
    assert called == ["score"]


def test_main_routes_generate(ma: ModuleType, mocker: MockerFixture) -> None:
    called = []
    mocker.patch.object(
        ma, "_cmd_generate", side_effect=lambda _a: called.append("generate") or 0
    )
    mocker.patch.object(
        sys,
        "argv",
        [
            "market_analysis.py",
            "generate",
            "--symbols",
            "X",
        ],
    )
    ma.main()
    assert called == ["generate"]
