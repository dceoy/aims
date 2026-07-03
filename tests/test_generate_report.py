from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING, Any

import pytest

if TYPE_CHECKING:
    from types import ModuleType

import aims.reports as _aims_reports
from aims.calendars import upcoming_events

FIXTURE_PATH = Path(__file__).resolve().parent / "fixtures" / "analysis_2024-01-01.json"
GOLDEN_PATH = (
    Path(__file__).resolve().parent / "golden" / "2024-01-01-market-analysis.md"
)


@pytest.fixture(scope="module")
def gr() -> ModuleType:
    return _aims_reports


@pytest.fixture(scope="module")
def fixture_artifact() -> dict[str, Any]:
    with FIXTURE_PATH.open() as fh:
        return json.load(fh)


# ── Golden file test ────────────────────────────────────────────────────────────


def test_generate_report_golden(
    gr: ModuleType, fixture_artifact: dict[str, Any]
) -> None:
    actual = gr.generate_report(fixture_artifact)
    expected = GOLDEN_PATH.read_text()
    assert actual == expected


def test_generate_report_with_history(
    gr: ModuleType, fixture_artifact: dict[str, Any]
) -> None:
    history = {
        "previous_analysis_date": "2023-12-30",
        "top_k": 2,
        "instruments": [
            {
                "symbol": "^SPX",
                "new_top_k": True,
                "consecutive_top_k_reports": 2,
                "risk_gates_added": [],
                "risk_gates_removed": ["stale_data"],
            },
            {
                "symbol": "^NDX",
                "new_top_k": False,
                "consecutive_top_k_reports": 1,
                "risk_gates_added": [],
                "risk_gates_removed": [],
            },
        ],
        "dropped_from_top_k": ["^DJI"],
    }
    result = gr.generate_report(fixture_artifact, history)
    assert "data/history/2024-01-01.json" in result
    assert "New top-2:** ^SPX" in result
    assert "Persistent top signals:** ^SPX (2 reports)" in result
    assert "Dropped from top-2:** ^DJI" in result
    assert "removed stale_data" in result


def test_generate_report_history_without_previous(
    gr: ModuleType, fixture_artifact: dict[str, Any]
) -> None:
    result = gr.generate_report(fixture_artifact, {"previous_analysis_date": None})
    assert "No previous analysis artifact" in result


def test_generate_report_history_universe_change(
    gr: ModuleType, fixture_artifact: dict[str, Any]
) -> None:
    history = {
        "previous_analysis_date": "2023-12-30",
        "top_k": 5,
        "universe_size": 20,
        "previous_universe_size": 5,
        "instruments": [],
        "dropped_from_top_k": [],
    }
    result = gr.generate_report(fixture_artifact, history)
    assert "**Universe change:** 5 → 20 instruments" in result
    assert "not directly comparable" in result
    history["previous_universe_size"] = 20
    result = gr.generate_report(fixture_artifact, history)
    assert "Universe change" not in result


def test_instrument_scores_grouped_by_asset_class(gr: ModuleType) -> None:
    artifact: dict[str, Any] = {
        "version": "1.0.0",
        "metadata": {
            "generated_at": "2024-06-01T00:00:00+00:00",
            "git_commit": "deadbeef",
            "data_source": "yfinance",
            "data_freshness": {},
            "scoring_version": "1.0.0",
            "config": {},
        },
        "instruments": [
            {
                "symbol": "^GSPC",
                "rank": 1,
                "score": 70.0,
                "is_reliable": True,
                "risk_gates": [],
                "explanation": "e",
                "features": {},
                "asset_class": "equity_index",
            },
            {
                "symbol": "GC=F",
                "rank": 2,
                "score": 60.0,
                "is_reliable": True,
                "risk_gates": [],
                "explanation": "e",
                "features": {},
                "asset_class": "commodity",
            },
            {
                "symbol": "UNKNOWN",
                "rank": 3,
                "score": 50.0,
                "is_reliable": True,
                "risk_gates": [],
                "explanation": "e",
                "features": {},
            },
        ],
    }
    result = gr.generate_report(artifact)
    assert "### Equity Index" in result
    assert "### Commodity" in result
    assert "### Other" in result
    assert result.index("### Commodity") < result.index("### Equity Index")
    assert result.index("### Equity Index") < result.index("### Other")


# ── Edge-case artifact tests ────────────────────────────────────────────────────


def test_generate_report_no_instruments(gr: ModuleType) -> None:
    artifact: dict[str, Any] = {
        "version": "1.0.0",
        "metadata": {
            "generated_at": "2024-06-01T00:00:00+00:00",
            "git_commit": "deadbeef",
            "data_source": "stooq",
            "data_freshness": {},
            "scoring_version": "1.0.0",
            "config": {},
        },
        "instruments": [],
    }
    result = gr.generate_report(artifact)
    assert "No reliable instruments" in result
    assert "No risk gates triggered" in result
    assert "All instruments passed quality checks" in result


def test_generate_report_all_reliable(gr: ModuleType) -> None:
    artifact: dict[str, Any] = {
        "version": "1.0.0",
        "metadata": {
            "generated_at": "2024-06-01T00:00:00+00:00",
            "git_commit": "deadbeef",
            "data_source": "stooq",
            "data_freshness": {"AAPL": "2024-06-01"},
            "scoring_version": "1.0.0",
            "config": {},
        },
        "instruments": [
            {
                "symbol": "AAPL",
                "rank": 1,
                "score": 70.0,
                "is_reliable": True,
                "risk_gates": [],
                "explanation": "Strong",
                "features": {
                    "ret_1d": 0.01,
                    "ret_5d": 0.02,
                    "ret_20d": 0.05,
                    "ret_60d": 0.10,
                    "ma20_dist": 0.02,
                    "ma50_dist": 0.01,
                    "vol_20d": 0.10,
                    "mdd_60d": 0.02,
                    "rsi_14": 60.0,
                    "zscore_20d": 1.0,
                },
            }
        ],
    }
    result = gr.generate_report(artifact)
    assert "All instruments passed quality checks." in result


def test_generate_report_no_reliable(gr: ModuleType) -> None:
    artifact: dict[str, Any] = {
        "version": "1.0.0",
        "metadata": {
            "generated_at": "2024-06-01T00:00:00+00:00",
            "git_commit": "deadbeef",
            "data_source": "stooq",
            "data_freshness": {},
            "scoring_version": "1.0.0",
            "config": {},
        },
        "instruments": [
            {
                "symbol": "BAD",
                "rank": 1,
                "score": 20.0,
                "is_reliable": False,
                "risk_gates": ["stale_data"],
                "explanation": "Suppressed",
                "features": {
                    "ret_1d": None,
                    "ret_5d": None,
                    "ret_20d": None,
                    "ret_60d": None,
                    "ma20_dist": None,
                    "ma50_dist": None,
                    "vol_20d": None,
                    "mdd_60d": None,
                    "rsi_14": None,
                    "zscore_20d": None,
                },
            }
        ],
    }
    result = gr.generate_report(artifact)
    assert "Unavailable" in result
    assert "No reliable instruments." in result


def test_generate_report_missing_generated_at(gr: ModuleType) -> None:
    artifact: dict[str, Any] = {
        "version": "1.0.0",
        "metadata": {
            "git_commit": "abc",
            "data_source": "stooq",
            "data_freshness": {},
            "scoring_version": "1.0.0",
            "config": {},
        },
        "instruments": [],
    }
    result = gr.generate_report(artifact)
    assert "1970-01-01" in result


def test_generate_report_non_string_generated_at(gr: ModuleType) -> None:
    artifact: dict[str, Any] = {
        "version": "1.0.0",
        "metadata": {
            "generated_at": 12345,
            "git_commit": "abc",
            "data_source": "stooq",
            "data_freshness": {},
            "scoring_version": "1.0.0",
            "config": {},
        },
        "instruments": [],
    }
    result = gr.generate_report(artifact)
    assert "1970-01-01" in result


def test_generate_report_no_stale_warning(gr: ModuleType) -> None:
    artifact: dict[str, Any] = {
        "version": "1.0.0",
        "metadata": {
            "generated_at": "2024-06-01T00:00:00+00:00",
            "git_commit": "abc",
            "data_source": "stooq",
            "data_freshness": {"AAPL": "2024-06-01"},
            "scoring_version": "1.0.0",
            "config": {},
        },
        "instruments": [],
    }
    result = gr.generate_report(artifact)
    assert "Warning" not in result


# ── report_filename tests ───────────────────────────────────────────────────────


def test_report_filename(gr: ModuleType, fixture_artifact: dict[str, Any]) -> None:
    assert gr.report_filename(fixture_artifact) == "2024-01-01-market-analysis.md"


def test_report_filename_missing_generated_at(gr: ModuleType) -> None:
    artifact: dict[str, Any] = {"metadata": {}}
    assert gr.report_filename(artifact) == "1970-01-01-market-analysis.md"


def test_report_filename_non_string_generated_at(gr: ModuleType) -> None:
    artifact: dict[str, Any] = {"metadata": {"generated_at": 999}}
    assert gr.report_filename(artifact) == "1970-01-01-market-analysis.md"


# ── generate_and_save tests ─────────────────────────────────────────────────────


def test_generate_and_save(gr: ModuleType, tmp_path: Path) -> None:
    # Copy fixture to tmp_path
    artifact_path = tmp_path / "analysis_2024-01-01.json"
    artifact_path.write_text(FIXTURE_PATH.read_text())
    output_dir = tmp_path / "results"
    result_path = gr.generate_and_save(artifact_path, output_dir)
    assert result_path.exists()
    assert result_path.name == "2024-01-01-market-analysis.md"


def test_generate_and_save_with_history(gr: ModuleType, tmp_path: Path) -> None:
    artifact_path = tmp_path / "analysis.json"
    artifact_path.write_text(FIXTURE_PATH.read_text())
    history_path = tmp_path / "history.json"
    history_path.write_text(json.dumps({"previous_analysis_date": None}))
    result_path = gr.generate_and_save(
        artifact_path, tmp_path / "results", history_path
    )
    assert "data/history/2024-01-01.json" in result_path.read_text()


def test_generate_and_save_file_not_found(gr: ModuleType, tmp_path: Path) -> None:
    missing = tmp_path / "nonexistent.json"
    with pytest.raises(FileNotFoundError):
        gr.generate_and_save(missing, tmp_path)


def test_generate_and_save_missing_generated_at(gr: ModuleType, tmp_path: Path) -> None:
    artifact: dict[str, Any] = {
        "version": "1.0.0",
        "metadata": {
            "git_commit": "abc",
            "data_source": "stooq",
            "data_freshness": {},
            "scoring_version": "1.0.0",
            "config": {},
        },
        "instruments": [],
    }
    artifact_path = tmp_path / "artifact.json"
    artifact_path.write_text(json.dumps(artifact))
    output_dir = tmp_path / "results"
    with pytest.raises(ValueError, match="generated_at"):
        gr.generate_and_save(artifact_path, output_dir)


# ── main() tests ────────────────────────────────────────────────────────────────


def test_main_success(gr: ModuleType, tmp_path: Path) -> None:
    artifact_path = tmp_path / "analysis_2024-01-01.json"
    artifact_path.write_text(FIXTURE_PATH.read_text())
    output_dir = tmp_path / "results"
    result = gr.main(["--input", str(artifact_path), "--output", str(output_dir)])
    assert result == 0


def test_main_file_not_found(gr: ModuleType, tmp_path: Path) -> None:
    missing = tmp_path / "nonexistent.json"
    result = gr.main(["--input", str(missing), "--output", str(tmp_path)])
    assert result == 1


def test_main_bad_json(gr: ModuleType, tmp_path: Path) -> None:
    bad_file = tmp_path / "bad.json"
    bad_file.write_text("this is not json {{{{")
    result = gr.main(["--input", str(bad_file), "--output", str(tmp_path)])
    assert result == 1


# ── market_regime tests ─────────────────────────────────────────────────────────


def _reliable_inst(ma20_dist: float | None) -> dict[str, Any]:
    return {"is_reliable": True, "features": {"ma20_dist": ma20_dist}}


def test_market_regime_bullish(gr: ModuleType) -> None:
    insts = [_reliable_inst(0.02), _reliable_inst(0.01), _reliable_inst(0.03)]
    assert gr.market_regime(insts) == "Bullish"


def test_market_regime_neutral(gr: ModuleType) -> None:
    insts = [_reliable_inst(0.02), _reliable_inst(-0.01)]
    assert gr.market_regime(insts) == "Neutral"


def test_market_regime_bearish(gr: ModuleType) -> None:
    insts = [_reliable_inst(-0.02), _reliable_inst(-0.01), _reliable_inst(-0.03)]
    assert gr.market_regime(insts) == "Bearish"


def test_market_regime_empty(gr: ModuleType) -> None:
    assert gr.market_regime([]) == "Unavailable"


def test_market_regime_no_ma20_data(gr: ModuleType) -> None:
    assert gr.market_regime([_reliable_inst(None)]) == "Unavailable"


def test_market_regime_missing_features(gr: ModuleType) -> None:
    assert gr.market_regime([{"is_reliable": True, "features": None}]) == "Unavailable"


def test_market_regime_ignores_none_ma20(gr: ModuleType) -> None:
    # None values are excluded from the breadth denominator.
    assert gr.market_regime([_reliable_inst(None), _reliable_inst(0.01)]) == "Bullish"


def test_market_regime_boundary_bullish(gr: ModuleType) -> None:
    # exactly 65% above MA20 is Bullish (>=0.65)
    insts = [_reliable_inst(0.01)] * 13 + [_reliable_inst(-0.01)] * 7
    assert gr.market_regime(insts) == "Bullish"


def test_market_regime_boundary_bearish(gr: ModuleType) -> None:
    # exactly 35% above MA20 is Bearish (<=0.35)
    insts = [_reliable_inst(0.01)] * 7 + [_reliable_inst(-0.01)] * 13
    assert gr.market_regime(insts) == "Bearish"


def test_market_regime_zero_ma20_dist_not_above(gr: ModuleType) -> None:
    # sitting exactly on the MA20 does not count as above it
    assert gr.market_regime([_reliable_inst(0.0)]) == "Bearish"


# ── _format_pct tests ───────────────────────────────────────────────────────────


def test_format_pct_none(gr: ModuleType) -> None:
    assert gr._format_pct(None) == "n/a"


def test_format_pct_positive(gr: ModuleType) -> None:
    assert gr._format_pct(0.053) == "+5.3%"


def test_format_pct_negative(gr: ModuleType) -> None:
    assert gr._format_pct(-0.042) == "-4.2%"


def test_format_pct_zero(gr: ModuleType) -> None:
    assert gr._format_pct(0.0) == "+0.0%"


# ── _instrument_table edge cases ────────────────────────────────────────────────


def test_instrument_table_empty(gr: ModuleType) -> None:
    result = gr._section_instrument_scores([])
    assert (
        "| Rank | Instrument | Score | Reliable | Risk Gates | Explanation |" in result
    )
    assert (
        "| ---: | ---------- | ----: | :------: | ---------- | ----------- |" in result
    )


def test_instrument_label_symbol_only(gr: ModuleType) -> None:
    label = gr._instrument_label({"symbol": "^SPX"})
    assert label == "^SPX"


def test_instrument_label_with_display_name(gr: ModuleType) -> None:
    label = gr._instrument_label({"symbol": "^SPX", "display_name": "S&P 500"})
    assert label == "S&P 500 / ^SPX"


def test_instrument_label_display_name_same_as_symbol(gr: ModuleType) -> None:
    label = gr._instrument_label({"symbol": "^SPX", "display_name": "^SPX"})
    assert label == "^SPX"


# ── _freshness_table edge cases ─────────────────────────────────────────────────


def test_freshness_table_empty(gr: ModuleType) -> None:
    result = gr._section_data_freshness("stooq", {})
    assert "_No freshness data available._" in result


# ── _toml_escape tests ──────────────────────────────────────────────────────────


def test_toml_escape_backslash(gr: ModuleType) -> None:
    assert gr._toml_escape("a\\b") == "a\\\\b"


def test_toml_escape_quote(gr: ModuleType) -> None:
    assert gr._toml_escape('a"b') == 'a\\"b'


def test_toml_escape_both(gr: ModuleType) -> None:
    assert gr._toml_escape('a\\"b') == 'a\\\\\\"b'


# ── Section edge case tests ─────────────────────────────────────────────────────


def test_section_top_opportunities_unknown_gate(gr: ModuleType) -> None:
    result = gr._section_key_risks([
        {
            "symbol": "X",
            "risk_gates": ["custom_gate"],
            "is_reliable": False,
        }
    ])
    assert "custom_gate" in result


def test_section_key_risks_none_gates(gr: ModuleType) -> None:
    result = gr._section_key_risks([{"symbol": "X", "risk_gates": None}])
    assert "_No risk gates triggered._" in result


def test_section_top_opportunities_with_null_rsi(gr: ModuleType) -> None:
    reliable = [
        {
            "symbol": "AAPL",
            "rank": 1,
            "score": 70.0,
            "is_reliable": True,
            "risk_gates": [],
            "explanation": "Strong",
            "features": {
                "ret_1d": 0.01,
                "ret_5d": 0.02,
                "ret_20d": 0.05,
                "ret_60d": 0.10,
                "ma20_dist": 0.02,
                "ma50_dist": 0.01,
                "vol_20d": 0.10,
                "mdd_60d": 0.02,
                "rsi_14": None,
                "zscore_20d": 1.0,
            },
        }
    ]
    result = gr._section_top_opportunities(reliable)
    assert "RSI14=n/a" in result


def test_generate_report_returns_string(
    gr: ModuleType, fixture_artifact: dict[str, Any]
) -> None:
    result = gr.generate_report(fixture_artifact)
    assert isinstance(result, str)
    assert "Market Analysis 2024-01-01" in result


# ── _validate_for_report tests ──────────────────────────────────────────────────


def test_validate_for_report_valid(
    gr: ModuleType, fixture_artifact: dict[str, Any]
) -> None:
    gr._validate_for_report(fixture_artifact)  # must not raise


def test_validate_for_report_no_metadata(gr: ModuleType) -> None:
    with pytest.raises(ValueError, match="metadata"):
        gr._validate_for_report({"instruments": []})


def test_validate_for_report_metadata_not_dict(gr: ModuleType) -> None:
    with pytest.raises(ValueError, match="metadata"):
        gr._validate_for_report({"metadata": "bad", "instruments": []})


def test_validate_for_report_missing_generated_at(gr: ModuleType) -> None:
    with pytest.raises(ValueError, match="generated_at"):
        gr._validate_for_report({"metadata": {}, "instruments": []})


def test_validate_for_report_non_string_generated_at(gr: ModuleType) -> None:
    with pytest.raises(ValueError, match="generated_at"):
        gr._validate_for_report({
            "metadata": {"generated_at": 12345},
            "instruments": [],
        })


def test_validate_for_report_epoch_generated_at(gr: ModuleType) -> None:
    with pytest.raises(ValueError, match="epoch sentinel"):
        gr._validate_for_report({
            "metadata": {"generated_at": "1970-01-01T00:00:00+00:00"},
            "instruments": [],
        })


def test_validate_for_report_missing_instruments(gr: ModuleType) -> None:
    with pytest.raises(ValueError, match="instruments"):
        gr._validate_for_report({
            "metadata": {"generated_at": "2024-01-01T00:00:00+00:00"}
        })


def test_main_validation_error(gr: ModuleType, tmp_path: Path) -> None:
    artifact: dict[str, Any] = {
        "version": "1.0.0",
        "metadata": {},
        "instruments": [],
    }
    artifact_path = tmp_path / "artifact.json"
    artifact_path.write_text(json.dumps(artifact))
    result = gr.main(["--input", str(artifact_path), "--output", str(tmp_path)])
    assert result == 1


def test_generate_report_missing_data_gate(gr: ModuleType) -> None:
    artifact: dict[str, Any] = {
        "version": "1.0.0",
        "metadata": {
            "generated_at": "2024-06-01T00:00:00+00:00",
            "git_commit": "abc",
            "data_source": "stooq",
            "data_freshness": {"MISS": "n/a"},
            "scoring_version": "1.0.0",
            "config": {},
        },
        "instruments": [
            {
                "symbol": "MISS",
                "rank": 1,
                "score": 0.0,
                "is_reliable": False,
                "risk_gates": ["missing_data"],
                "explanation": "Suppressed: missing_data",
                "features": {
                    "ret_1d": None,
                    "ret_5d": None,
                    "ret_20d": None,
                    "ret_60d": None,
                    "ma20_dist": None,
                    "ma50_dist": None,
                    "vol_20d": None,
                    "mdd_60d": None,
                    "rsi_14": None,
                    "zscore_20d": None,
                },
            }
        ],
    }
    result = gr.generate_report(artifact)
    assert "Missing data" in result
    assert "MISS" in result


# ── _format_vol tests ───────────────────────────────────────────────────────────


def test_format_vol_none(gr: ModuleType) -> None:
    assert gr._format_vol(None) == "n/a"


def test_format_vol_positive(gr: ModuleType) -> None:
    assert gr._format_vol(0.127) == "12.7%"


def test_format_vol_zero(gr: ModuleType) -> None:
    assert gr._format_vol(0.0) == "0.0%"


# ── _fmt_feature tests ──────────────────────────────────────────────────────────


def test_fmt_feature_pct_keys(gr: ModuleType) -> None:
    for key in ("ret_1d", "ret_5d", "ret_20d", "ret_60d", "ma20_dist", "ma50_dist"):
        assert gr._fmt_feature(key, 0.05) == "+5.0%"
        assert gr._fmt_feature(key, None) == "n/a"


def test_fmt_feature_vol_keys(gr: ModuleType) -> None:
    for key in ("vol_20d", "mdd_60d"):
        assert gr._fmt_feature(key, 0.10) == "10.0%"
        assert gr._fmt_feature(key, None) == "n/a"


def test_fmt_feature_numeric_keys(gr: ModuleType) -> None:
    assert gr._fmt_feature("rsi_14", 62.0) == "62.0"
    assert gr._fmt_feature("zscore_20d", 1.2) == "1.2"


def test_fmt_feature_numeric_none(gr: ModuleType) -> None:
    assert gr._fmt_feature("rsi_14", None) == "n/a"


# ── _section_symbol_details tests ──────────────────────────────────────────────


def test_section_symbol_details_no_reliable(gr: ModuleType) -> None:
    result = gr._section_symbol_details([
        {
            "symbol": "BAD",
            "rank": 1,
            "score": 20.0,
            "is_reliable": False,
            "features": {},
        },
    ])
    assert "No reliable instruments" in result


def test_section_symbol_details_empty(gr: ModuleType) -> None:
    result = gr._section_symbol_details([])
    assert "No reliable instruments" in result


def test_section_symbol_details_reliable(gr: ModuleType) -> None:
    instruments = [
        {
            "symbol": "AAPL",
            "rank": 1,
            "score": 70.0,
            "is_reliable": True,
            "features": {
                "ret_1d": 0.01,
                "ret_5d": 0.02,
                "ret_20d": 0.05,
                "ret_60d": 0.10,
                "ma20_dist": 0.02,
                "ma50_dist": 0.01,
                "vol_20d": 0.10,
                "mdd_60d": 0.02,
                "rsi_14": 60.0,
                "zscore_20d": 1.0,
            },
        }
    ]
    result = gr._section_symbol_details(instruments)
    assert "### AAPL (score 70.0)" in result
    assert "ret_1d" in result
    assert "+1.0%" in result
    assert "10.0%" in result
    assert "60.0" in result


def test_section_symbol_details_sorted_by_rank(gr: ModuleType) -> None:
    instruments = [
        {
            "symbol": "B",
            "rank": 2,
            "score": 60.0,
            "is_reliable": True,
            "features": {},
        },
        {
            "symbol": "A",
            "rank": 1,
            "score": 70.0,
            "is_reliable": True,
            "features": {},
        },
    ]
    result = gr._section_symbol_details(instruments)
    assert result.index("### A") < result.index("### B")


def test_section_symbol_details_null_features(gr: ModuleType) -> None:
    instruments = [
        {
            "symbol": "X",
            "rank": 1,
            "score": 50.0,
            "is_reliable": True,
            "features": None,
        }
    ]
    result = gr._section_symbol_details(instruments)
    assert "n/a" in result


# ── delta table in _section_signal_history tests ────────────────────────────────


def test_section_signal_history_with_deltas(gr: ModuleType) -> None:
    history = {
        "previous_analysis_date": "2023-12-31",
        "top_k": 3,
        "instruments": [
            {
                "symbol": "^SPX",
                "new_top_k": False,
                "consecutive_top_k_reports": 1,
                "risk_gates_added": [],
                "risk_gates_removed": [],
                "rank_delta": -1,
                "score_delta": 3.5,
            }
        ],
        "dropped_from_top_k": [],
    }
    result = gr._section_signal_history(history)
    assert "^SPX" in result
    assert "-1" in result
    assert "+3.5" in result
    assert "Rank" in result
    assert "Score" in result


def test_section_signal_history_no_deltas(gr: ModuleType) -> None:
    history = {
        "previous_analysis_date": "2023-12-31",
        "top_k": 3,
        "instruments": [
            {
                "symbol": "^SPX",
                "new_top_k": False,
                "consecutive_top_k_reports": 1,
                "risk_gates_added": [],
                "risk_gates_removed": [],
            }
        ],
        "dropped_from_top_k": [],
    }
    result = gr._section_signal_history(history)
    assert "Rank" not in result or "Rank Δ" not in result


def test_section_signal_history_delta_none_rank(gr: ModuleType) -> None:
    history = {
        "previous_analysis_date": "2023-12-31",
        "top_k": 3,
        "instruments": [
            {
                "symbol": "^SPX",
                "new_top_k": False,
                "consecutive_top_k_reports": 1,
                "risk_gates_added": [],
                "risk_gates_removed": [],
                "rank_delta": None,
                "score_delta": 2.0,
            }
        ],
        "dropped_from_top_k": [],
    }
    result = gr._section_signal_history(history)
    assert "n/a" in result
    assert "+2.0" in result


# ── Upcoming Events and AI Market Commentary tests ─────────────────────────────

QUAL_FIXTURE_PATH = (
    Path(__file__).resolve().parent / "fixtures" / "qualitative_2024-01-01.json"
)
CAL_FIXTURE_PATH = Path(__file__).resolve().parent / "fixtures" / "calendar_2024.json"
ENRICHED_GOLDEN_PATH = (
    Path(__file__).resolve().parent
    / "golden"
    / "2024-01-01-market-analysis-enriched.md"
)


@pytest.fixture(scope="module")
def fixture_qualitative() -> dict[str, Any]:
    with QUAL_FIXTURE_PATH.open() as fh:
        return json.load(fh)


@pytest.fixture(scope="module")
def fixture_events() -> list[dict[str, Any]]:
    with CAL_FIXTURE_PATH.open() as fh:
        calendar = json.load(fh)
    return upcoming_events(calendar["events"], "2024-01-01", 7)


def test_generate_report_enriched_golden(
    gr: ModuleType,
    fixture_artifact: dict[str, Any],
    fixture_qualitative: dict[str, Any],
    fixture_events: list[dict[str, Any]],
) -> None:
    actual = gr.generate_report(
        fixture_artifact,
        None,
        qualitative=fixture_qualitative,
        events=fixture_events,
        events_window=7,
    )
    assert actual == ENRICHED_GOLDEN_PATH.read_text()


def test_generate_report_without_inputs_is_byte_identical(
    gr: ModuleType, fixture_artifact: dict[str, Any]
) -> None:
    assert gr.generate_report(fixture_artifact) == GOLDEN_PATH.read_text()


def test_section_upcoming_events_empty(gr: ModuleType) -> None:
    result = gr._section_upcoming_events([], [], 7)
    assert "_No scheduled events within the next 7 days._" in result


def test_event_scope_label(gr: ModuleType) -> None:
    instruments = [{"canonical_id": "spx", "symbol": "^SPX", "display_name": "S&P 500"}]
    event = {"canonical_ids": ["spx", "ghost"], "asset_classes": ["commodity"]}
    label = gr._event_scope_label(event, instruments)
    assert label == "S&P 500 / ^SPX, ghost, Commodity"
    assert gr._event_scope_label({"canonical_ids": [], "asset_classes": []}, []) == "—"


def test_top_opportunities_without_matching_event(gr: ModuleType) -> None:
    reliable = [
        {
            "symbol": "GC=F",
            "canonical_id": "gold",
            "asset_class": "commodity",
            "score": 60.0,
            "is_reliable": True,
            "features": {},
            "explanation": "e",
        }
    ]
    events = [
        {
            "date": "2024-01-03",
            "name": "FOMC",
            "canonical_ids": [],
            "asset_classes": ["equity_index"],
        }
    ]
    result = gr._section_top_opportunities(reliable, events)
    assert "Scheduled event" not in result


def test_qualitative_has_content_variants(gr: ModuleType) -> None:
    base: dict[str, Any] = {
        "market_narrative": {"text": "", "citations": [], "gates": []},
        "themes": [],
        "instruments": [],
    }
    assert not gr._qualitative_has_content(base)
    narrative = dict(base, market_narrative={"text": "t", "gates": []})
    assert gr._qualitative_has_content(narrative)
    gated_narrative = dict(
        base, market_narrative={"text": "t", "gates": ["uncited_claims"]}
    )
    assert not gr._qualitative_has_content(gated_narrative)
    themes = dict(base, themes=[{"gates": []}])
    assert gr._qualitative_has_content(themes)
    instruments = dict(base, instruments=[{"gates": []}])
    assert gr._qualitative_has_content(instruments)


def test_front_matter_ai_commentary_false_when_all_gated(
    gr: ModuleType, fixture_artifact: dict[str, Any]
) -> None:
    qualitative: dict[str, Any] = {
        "metadata": {"model": "m", "prompt_version": "1.0.0", "gates": {}},
        "market_narrative": {
            "text": "t",
            "citations": [],
            "gates": ["uncited_claims"],
        },
        "themes": [],
        "instruments": [],
        "citations": {},
    }
    result = gr.generate_report(fixture_artifact, qualitative=qualitative)
    assert "ai_commentary = false" in result
    assert "_Market narrative withheld by grounding gates (uncited_claims)._" in result
    assert "### Sources" not in result


def test_ai_commentary_empty_narrative_without_gates(gr: ModuleType) -> None:
    qualitative: dict[str, Any] = {
        "metadata": {"model": "m", "prompt_version": "1.0.0"},
        "market_narrative": {"text": "", "citations": [], "gates": []},
        "themes": [],
        "instruments": [],
        "citations": {},
    }
    result = gr._section_ai_commentary(qualitative, [])
    assert "_Market narrative withheld by grounding gates._" in result


def test_ai_commentary_falls_back_to_symbol_label(gr: ModuleType) -> None:
    qualitative: dict[str, Any] = {
        "metadata": {"model": "m", "prompt_version": "1.0.0"},
        "market_narrative": {"text": "t", "citations": ["x" * 16], "gates": []},
        "themes": [],
        "instruments": [
            {
                "canonical_id": "gold",
                "symbol": "GC=F",
                "stance": "neutral",
                "confidence": "low",
                "drivers": [{"text": "d", "citations": []}],
                "gates": [],
            }
        ],
        "citations": {},
    }
    result = gr._section_ai_commentary(qualitative, [])
    assert "- **GC=F** — stance: neutral (confidence: low). d" in result
    # Cited id missing from the citations map falls back to the raw id.
    assert f"1. [{'x' * 16}]() — , " in result


def test_generate_and_save_enriched(gr: ModuleType, tmp_path: Path) -> None:
    artifact_path = tmp_path / "analysis.json"
    artifact_path.write_text(FIXTURE_PATH.read_text())
    qualitative_path = tmp_path / "qualitative.json"
    qualitative_path.write_text(QUAL_FIXTURE_PATH.read_text())
    calendar_dir = tmp_path / "calendars"
    calendar_dir.mkdir()
    (calendar_dir / "cal.json").write_text(CAL_FIXTURE_PATH.read_text())
    result_path = gr.generate_and_save(
        artifact_path,
        tmp_path / "results",
        qualitative_path=qualitative_path,
        calendar_dir=calendar_dir,
    )
    content = result_path.read_text()
    assert "ai_commentary = true" in content
    assert "## Upcoming Events" in content


def test_main_enriched(gr: ModuleType, tmp_path: Path) -> None:
    artifact_path = tmp_path / "analysis.json"
    artifact_path.write_text(FIXTURE_PATH.read_text())
    qualitative_path = tmp_path / "qualitative.json"
    qualitative_path.write_text(QUAL_FIXTURE_PATH.read_text())
    calendar_dir = tmp_path / "calendars"
    calendar_dir.mkdir()
    (calendar_dir / "cal.json").write_text(CAL_FIXTURE_PATH.read_text())
    result = gr.main([
        "--input",
        str(artifact_path),
        "--qualitative",
        str(qualitative_path),
        "--calendar-dir",
        str(calendar_dir),
        "--events-window",
        "7",
        "--output",
        str(tmp_path / "results"),
    ])
    assert result == 0


def test_main_invalid_calendar(gr: ModuleType, tmp_path: Path) -> None:
    artifact_path = tmp_path / "analysis.json"
    artifact_path.write_text(FIXTURE_PATH.read_text())
    calendar_dir = tmp_path / "calendars"
    calendar_dir.mkdir()
    (calendar_dir / "bad.json").write_text(json.dumps({"version": "1.0.0"}))
    result = gr.main([
        "--input",
        str(artifact_path),
        "--calendar-dir",
        str(calendar_dir),
        "--output",
        str(tmp_path / "results"),
    ])
    assert result == 1
