"""Tests for tracking realized forward returns of published top-5 signals."""

from __future__ import annotations

import argparse
import json
from datetime import date, timedelta
from typing import TYPE_CHECKING, Any

import pytest

if TYPE_CHECKING:
    from pathlib import Path

from aims import signal_performance as sp

_UNIVERSE: dict[str, dict[str, Any]] = {
    "A": {"score": 90.0, "ret_1d": 0.05, "asset_class": "equity"},
    "B": {"score": 80.0, "ret_1d": 0.04, "asset_class": "equity"},
    "C": {"score": 70.0, "ret_1d": 0.03, "asset_class": "commodity"},
    "D": {"score": 60.0, "ret_1d": 0.02, "asset_class": "commodity"},
    "E": {"score": 50.0, "ret_1d": 0.01, "asset_class": "equity_index"},
    "F": {"score": 40.0, "ret_1d": -0.01, "asset_class": "equity_index"},
}


def _dates(n: int, start: str = "2024-01-01") -> list[str]:
    first = date.fromisoformat(start)
    return [(first + timedelta(days=i)).isoformat() for i in range(n)]


def _inst(
    symbol: str,
    *,
    is_reliable: bool = True,
    tradable: bool | None = None,
    ret_1d: float | None = None,
) -> dict[str, Any]:
    spec = _UNIVERSE[symbol]
    inst: dict[str, Any] = {
        "symbol": symbol,
        "rank": 1,
        "score": spec["score"],
        "is_reliable": is_reliable,
        "risk_gates": [] if is_reliable else ["stale_data"],
        "explanation": "x",
        "asset_class": spec["asset_class"],
        "features": {"ret_1d": ret_1d if ret_1d is not None else spec["ret_1d"]},
    }
    if tradable is not None:
        inst["tradable"] = tradable
    return inst


def _analysis(
    when: str,
    symbols: list[str],
    *,
    regime: str | None = None,
    overrides: dict[str, dict[str, Any]] | None = None,
) -> dict[str, Any]:
    overrides = overrides or {}
    instruments = [_inst(s, **overrides.get(s, {})) for s in symbols]
    meta: dict[str, Any] = {
        "generated_at": f"{when}T00:00:00+00:00",
        "config": {"interval": "d"},
        "data_freshness": dict.fromkeys(symbols, when),
    }
    if regime is not None:
        meta["market_regime"] = {"label": regime}
    return {"metadata": meta, "instruments": instruments}


def _chain(
    symbols: list[str],
    n: int,
    *,
    regimes: list[str] | None = None,
    start: str = "2024-01-01",
) -> list[dict[str, Any]]:
    dates = _dates(n, start)
    return [
        _analysis(when, symbols, regime=(regimes[i] if regimes else None))
        for i, when in enumerate(dates)
    ]


# ── _resolve_return ──────────────────────────────────────────────────────────────


def test_resolve_return_unmatched_without_bar_date() -> None:
    realized, status = sp._resolve_return("A", {}, {}, {}, {}, 1)
    assert (realized, status) == (None, "unmatched")


def test_resolve_return_unmatched_without_chained_index() -> None:
    realized, status = sp._resolve_return(
        "A", {"A": "2024-01-01"}, {}, {}, {"A": {}}, 1
    )
    assert (realized, status) == (None, "unmatched")


def test_resolve_return_pending_at_chain_end() -> None:
    bars = {"A": [sp.Bar("2024-01-01", 0.01, None)]}
    realized, status = sp._resolve_return(
        "A", {"A": "2024-01-01"}, bars, {"A": set()}, {"A": {"2024-01-01": 0}}, 1
    )
    assert (realized, status) == (None, "pending")


def test_resolve_return_ok() -> None:
    bars = {"A": [sp.Bar("2024-01-01", 0.01, None), sp.Bar("2024-01-02", 0.02, None)]}
    realized, status = sp._resolve_return(
        "A", {"A": "2024-01-01"}, bars, {"A": set()}, {"A": {"2024-01-01": 0}}, 1
    )
    assert status == "ok"
    assert realized == pytest.approx(0.02)


def test_resolve_return_broken() -> None:
    bars = {"A": [sp.Bar("2024-01-01", 0.01, None), sp.Bar("2024-01-02", 0.02, None)]}
    realized, status = sp._resolve_return(
        "A", {"A": "2024-01-01"}, bars, {"A": {1}}, {"A": {"2024-01-01": 0}}, 1
    )
    assert (realized, status) == (None, "broken")


# ── evaluate_signals ──────────────────────────────────────────────────────────────


def test_evaluate_signals_rejects_invalid_horizons() -> None:
    with pytest.raises(ValueError, match="unique"):
        sp.evaluate_signals([], horizons=(1, 1))
    with pytest.raises(ValueError, match="positive"):
        sp.evaluate_signals([], horizons=())
    with pytest.raises(ValueError, match="positive"):
        sp.evaluate_signals([], horizons=(0,))


def test_evaluate_signals_empty_analyses() -> None:
    result, warnings = sp.evaluate_signals([], horizons=(1,))
    assert result["dates_evaluated"] == 0
    assert result["horizons"]["1d"]["count"] == 0
    assert result["horizons"]["1d"]["top5_average_return"] is None
    assert result["horizons"]["1d"]["by_asset_class"] == {}
    assert result["horizons"]["1d"]["by_regime"] == {}
    assert warnings == []


def test_evaluate_signals_top5_excludes_lowest_scorer_and_computes_benchmark() -> None:
    symbols = list(_UNIVERSE)
    analyses = _chain(symbols, 3, regimes=["Bullish", "Bearish", "Bullish"])
    result, warnings = sp.evaluate_signals(analyses, horizons=(1,))
    assert warnings == []
    assert result["dates_evaluated"] == 3
    horizon = result["horizons"]["1d"]
    # 2 fully resolved days x 5 top-5 slots; the 3rd (last) day is pending.
    assert horizon["count"] == 10
    assert horizon["pending"] == 5
    assert horizon["incomplete"] == 0
    assert horizon["top5_average_return"] == pytest.approx(0.03, abs=1e-5)
    assert horizon["benchmark_average_return"] == pytest.approx(0.14 / 6, abs=1e-5)
    assert horizon["excess_return"] == pytest.approx(0.03 - 0.14 / 6, abs=1e-5)
    assert horizon["hit_rate"] == pytest.approx(0.6)


def test_evaluate_signals_by_asset_class_breakdown() -> None:
    symbols = list(_UNIVERSE)
    analyses = _chain(symbols, 3)
    result, _ = sp.evaluate_signals(analyses, horizons=(1,))
    by_asset_class = result["horizons"]["1d"]["by_asset_class"]
    assert sorted(by_asset_class) == ["commodity", "equity", "equity_index"]
    assert by_asset_class["equity"]["count"] == 4
    assert by_asset_class["equity"]["top5_average_return"] == pytest.approx(0.045)
    assert by_asset_class["commodity"]["count"] == 4
    assert by_asset_class["commodity"]["top5_average_return"] == pytest.approx(0.025)
    # F (equity_index) is excluded from top-5, so only E contributes.
    assert by_asset_class["equity_index"]["count"] == 2
    assert by_asset_class["equity_index"]["top5_average_return"] == pytest.approx(0.01)


def test_evaluate_signals_by_regime_breakdown() -> None:
    symbols = list(_UNIVERSE)
    analyses = _chain(symbols, 3, regimes=["Bullish", "Bearish", "Bullish"])
    result, _ = sp.evaluate_signals(analyses, horizons=(1,))
    by_regime = result["horizons"]["1d"]["by_regime"]
    assert by_regime["Bullish"]["count"] == 5
    assert by_regime["Bearish"]["count"] == 5
    assert by_regime["Bullish"]["top5_average_return"] == pytest.approx(0.03)


def test_evaluate_signals_defaults_regime_to_unavailable() -> None:
    symbols = list(_UNIVERSE)
    analyses = _chain(symbols, 2)  # no regime label set
    result, _ = sp.evaluate_signals(analyses, horizons=(1,))
    by_regime = result["horizons"]["1d"]["by_regime"]
    assert list(by_regime) == ["Unavailable"]


def test_evaluate_signals_excludes_non_tradable_from_top5() -> None:
    symbols = list(_UNIVERSE)
    # Make A (the top scorer) non-tradable; it must not occupy a top-5 slot
    # even though it would otherwise rank first, but it still counts toward
    # the benchmark.
    analyses = _chain(symbols, 3)
    for artifact in analyses:
        for inst in artifact["instruments"]:
            if inst["symbol"] == "A":
                inst["tradable"] = False
    result, _ = sp.evaluate_signals(analyses, horizons=(1,))
    horizon = result["horizons"]["1d"]
    # Top-5 now B..F's top 5 minus benchmark-only exclusion: B,C,D,E,F.
    assert horizon["count"] == 10
    assert horizon["by_asset_class"]["equity_index"]["count"] == 4  # E and F now


def test_evaluate_signals_skips_dates_without_reliable_instruments() -> None:
    analysis = _analysis("2024-01-01", ["A"], overrides={"A": {"is_reliable": False}})
    result, _ = sp.evaluate_signals([analysis], horizons=(1,))
    assert result["dates_evaluated"] == 0


def test_evaluate_signals_broken_chain_recorded_as_incomplete_with_warning() -> None:
    # ret_5d that cannot be reproduced by the chained ret_1d values marks the
    # link broken; build 6 days so day0's 5-day forward window is affected.
    dates = _dates(7)
    analyses = []
    for i, when in enumerate(dates):
        instruments = []
        for symbol in _UNIVERSE:
            inst = _inst(symbol)
            if symbol == "A" and i == 5:
                # Any ret_5d inconsistent with the chained ret_1d values
                # breaks the preceding 5 links for A.
                inst["features"]["ret_5d"] = 999.0
            instruments.append(inst)
        analyses.append({
            "metadata": {
                "generated_at": f"{when}T00:00:00+00:00",
                "config": {"interval": "d"},
                "data_freshness": dict.fromkeys(_UNIVERSE, when),
            },
            "instruments": instruments,
        })
    result, warnings = sp.evaluate_signals(analyses, horizons=(1,))
    assert result["horizons"]["1d"]["incomplete"] > 0
    assert any("broken bar chain" in w for w in warnings)


def test_evaluate_signals_top5_symbol_unmatched_is_incomplete_without_warning() -> None:
    when = "2024-01-01"
    analysis = _analysis(when, list(_UNIVERSE))
    del analysis["metadata"]["data_freshness"]["A"]
    result, warnings = sp.evaluate_signals([analysis], horizons=(1,))
    assert result["horizons"]["1d"]["incomplete"] >= 1
    assert warnings == []


def test_evaluate_signals_deduplicates_conflicting_ret_1d_warnings() -> None:
    when = "2024-01-01"
    analyses = [
        _analysis(when, ["A"]),
        {
            **_analysis(when, ["A"]),
            "instruments": [_inst("A", ret_1d=0.5)],
        },
        {
            **_analysis(when, ["A"]),
            "instruments": [_inst("A", ret_1d=0.9)],
        },
    ]
    _, warnings = sp.evaluate_signals(analyses, horizons=(1,))
    conflict = [w for w in warnings if "conflicting ret_1d" in w]
    assert len(conflict) == 1


# ── build_artifact ────────────────────────────────────────────────────────────────


def test_build_artifact_shape() -> None:
    symbols = list(_UNIVERSE)
    analyses = _chain(symbols, 3)
    artifact = sp.build_artifact(analyses, as_of="2024-01-03", horizons=(1,))
    assert artifact["version"] == sp.SIGNAL_PERFORMANCE_VERSION
    assert artifact["metadata"]["as_of"] == "2024-01-03"
    assert artifact["metadata"]["config"]["top_k"] == sp.TOP_K
    assert artifact["metadata"]["inputs"]["analysis_dates"] == _dates(3)
    assert artifact["metadata"]["disclaimer"] == sp.DISCLAIMER
    assert "1d" in artifact["signal_evaluation"]["horizons"]


def test_build_artifact_is_stable_across_json_round_trip() -> None:
    symbols = list(_UNIVERSE)
    analyses = _chain(symbols, 3)
    artifact = sp.build_artifact(analyses, as_of="2024-01-03")
    round_tripped = json.loads(json.dumps(artifact, sort_keys=True))
    assert round_tripped["signal_evaluation"] == artifact["signal_evaluation"]


# ── render_page ───────────────────────────────────────────────────────────────────


def test_render_page_overview_and_breakdowns() -> None:
    symbols = list(_UNIVERSE)
    analyses = _chain(symbols, 3, regimes=["Bullish", "Bearish", "Bullish"])
    artifact = sp.build_artifact(analyses, as_of="2024-01-03", horizons=(1,))
    page = sp.render_page(artifact)
    assert 'title = "Signal Performance"' in page
    assert "## Cumulative Overview" in page
    assert "### By Asset Class" in page
    assert "### By Market Regime" in page
    assert "equity" in page
    assert "Bullish" in page
    assert sp.DISCLAIMER in page


def test_render_page_no_observations_yet() -> None:
    artifact = sp.build_artifact([], as_of="2024-01-01", horizons=(1,))
    page = sp.render_page(artifact)
    assert "_No matured observations yet._" in page


def test_render_page_caps_warning_list() -> None:
    artifact = sp.build_artifact([], as_of="2024-01-01", horizons=(1,))
    artifact["warnings"] = [f"warning {i:02d}" for i in range(25)]
    page = sp.render_page(artifact)
    assert "warning 19" in page
    assert "warning 20" not in page
    assert "… and 5 more" in page


def test_render_page_no_warnings_section_when_empty() -> None:
    artifact = sp.build_artifact([], as_of="2024-01-01", horizons=(1,))
    page = sp.render_page(artifact)
    assert "Warnings" not in page


def test_render_page_warnings_under_cap_omits_more_suffix() -> None:
    artifact = sp.build_artifact([], as_of="2024-01-01", horizons=(1,))
    artifact["warnings"] = ["one", "two", "three"]
    page = sp.render_page(artifact)
    assert "Warnings (3)" in page
    assert "more" not in page


# ── generate / main ───────────────────────────────────────────────────────────────


def _write_analysis(path: Path, artifact: dict[str, Any]) -> None:
    path.write_text(json.dumps(artifact, sort_keys=True), encoding="utf-8")


def test_generate_writes_artifact_and_page(tmp_path: Path) -> None:
    analysis_dir = tmp_path / "analysis"
    analysis_dir.mkdir()
    symbols = list(_UNIVERSE)
    for artifact in _chain(symbols, 3):
        when = artifact["metadata"]["generated_at"][:10]
        _write_analysis(analysis_dir / f"{when}.json", artifact)
    output = tmp_path / "signals.json"
    page_output = tmp_path / "page.md"
    sp.generate(analysis_dir, output, horizons=(1,), page_output=page_output)
    written = json.loads(output.read_text())
    assert written["metadata"]["as_of"] == "2024-01-03"
    assert page_output.read_text().startswith("+++")


def test_generate_ignores_non_daily_artifacts(tmp_path: Path) -> None:
    analysis_dir = tmp_path / "analysis"
    analysis_dir.mkdir()
    daily = _analysis("2024-01-01", ["A"])
    weekly = _analysis("2024-01-01", ["A"])
    weekly["metadata"]["config"]["interval"] = "w"
    _write_analysis(analysis_dir / "2024-01-01.json", daily)
    _write_analysis(analysis_dir / "2024-01-01-w.json", weekly)
    output = tmp_path / "signals.json"
    sp.generate(analysis_dir, output, horizons=(1,))
    written = json.loads(output.read_text())
    assert written["metadata"]["inputs"]["analysis_dates"] == ["2024-01-01"]


def test_generate_raises_without_daily_artifacts(tmp_path: Path) -> None:
    analysis_dir = tmp_path / "analysis"
    analysis_dir.mkdir()
    with pytest.raises(ValueError, match="no daily analysis artifacts"):
        sp.generate(analysis_dir, tmp_path / "signals.json")


def test_main_success(tmp_path: Path) -> None:
    analysis_dir = tmp_path / "analysis"
    analysis_dir.mkdir()
    _write_analysis(analysis_dir / "2024-01-01.json", _analysis("2024-01-01", ["A"]))
    output = tmp_path / "signals.json"
    rc = sp.main([
        "--analysis-dir",
        str(analysis_dir),
        "--output",
        str(output),
        "--horizons",
        "1",
    ])
    assert rc == 0
    assert output.exists()


def test_main_error_returns_nonzero(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    analysis_dir = tmp_path / "empty"
    analysis_dir.mkdir()
    rc = sp.main([
        "--analysis-dir",
        str(analysis_dir),
        "--output",
        str(tmp_path / "out.json"),
    ])
    assert rc == 1
    assert "ERROR" in capsys.readouterr().out


def test_parse_horizons_rejects_invalid() -> None:
    with pytest.raises(argparse.ArgumentTypeError):
        sp._parse_horizons("0")
    with pytest.raises(argparse.ArgumentTypeError):
        sp._parse_horizons("a")
    assert sp._parse_horizons("1,5") == (1, 5)


def test_analysis_interval_defaults_to_empty_string() -> None:
    assert sp._analysis_interval({}) == ""


def test_artifact_date_requires_valid_generated_at() -> None:
    with pytest.raises(ValueError, match="generated_at"):
        sp._artifact_date({"metadata": {}})
