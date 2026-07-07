"""Tests for the cumulative signal-performance artifact validator."""

from __future__ import annotations

import copy
import json
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pathlib import Path

    import pytest

from aims import signal_performance as sp
from aims.validate_signal_performance import main, validate_artifact


def _valid_artifact() -> dict[str, Any]:
    analyses = [
        {
            "metadata": {
                "generated_at": "2024-01-01T00:00:00+00:00",
                "config": {"interval": "d"},
                "data_freshness": {"A": "2024-01-01", "B": "2024-01-01"},
                "market_regime": {"label": "Bullish"},
            },
            "instruments": [
                {
                    "symbol": "A",
                    "rank": 1,
                    "score": 90.0,
                    "is_reliable": True,
                    "risk_gates": [],
                    "explanation": "x",
                    "asset_class": "equity",
                    "features": {"ret_1d": 0.02},
                },
                {
                    "symbol": "B",
                    "rank": 2,
                    "score": 80.0,
                    "is_reliable": True,
                    "risk_gates": [],
                    "explanation": "x",
                    "asset_class": "commodity",
                    "features": {"ret_1d": 0.01},
                },
            ],
        },
        {
            "metadata": {
                "generated_at": "2024-01-02T00:00:00+00:00",
                "config": {"interval": "d"},
                "data_freshness": {"A": "2024-01-02", "B": "2024-01-02"},
                "market_regime": {"label": "Bullish"},
            },
            "instruments": [
                {
                    "symbol": "A",
                    "rank": 1,
                    "score": 90.0,
                    "is_reliable": True,
                    "risk_gates": [],
                    "explanation": "x",
                    "asset_class": "equity",
                    "features": {"ret_1d": 0.02},
                },
                {
                    "symbol": "B",
                    "rank": 2,
                    "score": 80.0,
                    "is_reliable": True,
                    "risk_gates": [],
                    "explanation": "x",
                    "asset_class": "commodity",
                    "features": {"ret_1d": 0.01},
                },
            ],
        },
    ]
    return sp.build_artifact(analyses, as_of="2024-01-02", horizons=(1,))


def test_validate_valid_artifact() -> None:
    assert validate_artifact(_valid_artifact()) == []


def test_validate_missing_top_key() -> None:
    artifact = _valid_artifact()
    del artifact["warnings"]
    assert validate_artifact(artifact) == ["missing required key: 'warnings'"]


def test_validate_wrong_version() -> None:
    artifact = _valid_artifact()
    artifact["version"] = "9.9.9"
    assert any("unsupported version" in e for e in validate_artifact(artifact))


def test_validate_metadata_must_be_object() -> None:
    artifact = _valid_artifact()
    artifact["metadata"] = []
    assert "'metadata' must be a JSON object" in validate_artifact(artifact)


def test_validate_metadata_missing_key() -> None:
    artifact = _valid_artifact()
    del artifact["metadata"]["disclaimer"]
    errors = validate_artifact(artifact)
    assert any("metadata missing required key: 'disclaimer'" in e for e in errors)


def test_validate_config_top_k_must_be_positive_int() -> None:
    artifact = _valid_artifact()
    artifact["metadata"]["config"]["top_k"] = 0
    errors = validate_artifact(artifact)
    assert any("top_k must be a positive integer" in e for e in errors)
    artifact["metadata"]["config"]["top_k"] = "5"
    errors = validate_artifact(artifact)
    assert any("top_k must be a positive integer" in e for e in errors)


def test_validate_config_horizons_must_be_unique_positive() -> None:
    artifact = _valid_artifact()
    artifact["metadata"]["config"]["horizons"] = [1, 1]
    errors = validate_artifact(artifact)
    assert any("horizons must be unique positive integers" in e for e in errors)


def test_validate_config_tolerance_must_be_non_negative() -> None:
    artifact = _valid_artifact()
    artifact["metadata"]["config"]["return_consistency_tolerance"] = -1
    errors = validate_artifact(artifact)
    assert any("return_consistency_tolerance" in e for e in errors)


def test_validate_config_must_be_object_when_present() -> None:
    artifact = _valid_artifact()
    artifact["metadata"]["config"] = "bad"
    errors = validate_artifact(artifact)
    assert any("metadata.config must be a JSON object" in e for e in errors)


def test_validate_config_absent_skips_config_checks() -> None:
    artifact = _valid_artifact()
    del artifact["metadata"]["config"]
    errors = validate_artifact(artifact)
    assert any("metadata missing required key: 'config'" in e for e in errors)
    assert not any("metadata.config must be" in e for e in errors)


def test_validate_inputs_dates_must_be_sorted_iso_dates() -> None:
    artifact = _valid_artifact()
    artifact["metadata"]["inputs"]["analysis_dates"] = ["2024-01-02", "2024-01-01"]
    errors = validate_artifact(artifact)
    assert any("analysis_dates must be sorted" in e for e in errors)
    artifact["metadata"]["inputs"]["analysis_dates"] = ["bad-date"]
    errors = validate_artifact(artifact)
    assert any("YYYY-MM-DD" in e for e in errors)


def test_validate_inputs_must_be_object_when_present() -> None:
    artifact = _valid_artifact()
    artifact["metadata"]["inputs"] = "bad"
    errors = validate_artifact(artifact)
    assert any("metadata.inputs must be a JSON object" in e for e in errors)


def test_validate_inputs_absent_skips_inputs_checks() -> None:
    artifact = _valid_artifact()
    del artifact["metadata"]["inputs"]
    errors = validate_artifact(artifact)
    assert any("metadata missing required key: 'inputs'" in e for e in errors)
    assert not any("metadata.inputs must be" in e for e in errors)


def test_validate_as_of_must_be_iso_date() -> None:
    artifact = _valid_artifact()
    artifact["metadata"]["as_of"] = "not-a-date"
    errors = validate_artifact(artifact)
    assert any("is not a YYYY-MM-DD date" in e for e in errors)


def test_validate_signal_evaluation_must_be_object() -> None:
    artifact = _valid_artifact()
    artifact["signal_evaluation"] = []
    errors = validate_artifact(artifact)
    assert "'signal_evaluation' must be a JSON object" in errors


def test_validate_dates_evaluated_must_be_non_negative_int() -> None:
    artifact = _valid_artifact()
    artifact["signal_evaluation"]["dates_evaluated"] = -1
    errors = validate_artifact(artifact)
    assert any("dates_evaluated must be a non-negative integer" in e for e in errors)


def test_validate_horizons_must_be_object() -> None:
    artifact = _valid_artifact()
    artifact["signal_evaluation"]["horizons"] = "bad"
    errors = validate_artifact(artifact)
    assert any("signal_evaluation.horizons must be a JSON object" in e for e in errors)


def test_validate_horizons_absent_skips_horizons_object_check() -> None:
    artifact = _valid_artifact()
    del artifact["signal_evaluation"]["horizons"]
    errors = validate_artifact(artifact)
    assert any(
        "signal_evaluation missing required key: 'horizons'" in e for e in errors
    )
    assert not any("horizons must be a JSON object" in e for e in errors)


def test_validate_horizons_keys_must_match_config() -> None:
    artifact = _valid_artifact()
    artifact["signal_evaluation"]["horizons"]["5d"] = artifact["signal_evaluation"][
        "horizons"
    ].pop("1d")
    errors = validate_artifact(artifact)
    assert any("horizons keys do not match" in e for e in errors)


def test_validate_horizon_missing_key() -> None:
    artifact = _valid_artifact()
    del artifact["signal_evaluation"]["horizons"]["1d"]["count"]
    errors = validate_artifact(artifact)
    assert any(
        "signal_evaluation.horizons.1d missing required key: 'count'" in e
        for e in errors
    )


def test_validate_horizon_must_be_object() -> None:
    artifact = _valid_artifact()
    artifact["signal_evaluation"]["horizons"]["1d"] = "bad"
    errors = validate_artifact(artifact)
    assert any(
        "signal_evaluation.horizons.1d must be a JSON object" in e for e in errors
    )


def test_validate_horizon_pending_incomplete_must_be_non_negative() -> None:
    artifact = _valid_artifact()
    artifact["signal_evaluation"]["horizons"]["1d"]["pending"] = -1
    errors = validate_artifact(artifact)
    assert any(
        "signal_evaluation.horizons.1d.pending must be a non-negative integer" in e
        for e in errors
    )


def test_validate_bucket_must_be_object() -> None:
    artifact = _valid_artifact()
    artifact["signal_evaluation"]["horizons"]["1d"]["count"] = "bad"
    errors = validate_artifact(artifact)
    assert any("count must be a non-negative integer" in e for e in errors)


def test_validate_bucket_missing_key() -> None:
    artifact = _valid_artifact()
    del artifact["signal_evaluation"]["horizons"]["1d"]["hit_rate"]
    errors = validate_artifact(artifact)
    assert any("missing required key: 'hit_rate'" in e for e in errors)


def test_validate_bucket_average_return_must_be_number_or_null() -> None:
    artifact = _valid_artifact()
    artifact["signal_evaluation"]["horizons"]["1d"]["top5_average_return"] = "bad"
    errors = validate_artifact(artifact)
    assert any("top5_average_return must be null or a number" in e for e in errors)


def test_validate_bucket_hit_rate_out_of_range() -> None:
    artifact = _valid_artifact()
    artifact["signal_evaluation"]["horizons"]["1d"]["hit_rate"] = 1.5
    errors = validate_artifact(artifact)
    assert any("hit_rate must be null or a number in [0, 1]" in e for e in errors)


def test_validate_by_asset_class_must_be_object() -> None:
    artifact = _valid_artifact()
    artifact["signal_evaluation"]["horizons"]["1d"]["by_asset_class"] = "bad"
    errors = validate_artifact(artifact)
    assert any("by_asset_class must be a JSON object" in e for e in errors)


def test_validate_by_asset_class_bucket_shape() -> None:
    artifact = _valid_artifact()
    by_asset_class = artifact["signal_evaluation"]["horizons"]["1d"]["by_asset_class"]
    bucket = next(iter(by_asset_class.values()))
    bucket["count"] = "bad"
    errors = validate_artifact(artifact)
    assert any("count must be a non-negative integer" in e for e in errors)


def test_validate_by_asset_class_bucket_must_be_object() -> None:
    artifact = _valid_artifact()
    by_asset_class = artifact["signal_evaluation"]["horizons"]["1d"]["by_asset_class"]
    label = next(iter(by_asset_class))
    by_asset_class[label] = []
    errors = validate_artifact(artifact)
    assert any(f"by_asset_class.{label} must be a JSON object" in e for e in errors)


def test_validate_by_asset_class_bucket_missing_key() -> None:
    artifact = _valid_artifact()
    by_asset_class = artifact["signal_evaluation"]["horizons"]["1d"]["by_asset_class"]
    label, bucket = next(iter(by_asset_class.items()))
    del bucket["hit_rate"]
    errors = validate_artifact(artifact)
    assert any(
        f"by_asset_class.{label} missing required key: 'hit_rate'" in e for e in errors
    )


def test_validate_bucket_hit_rate_null_is_valid() -> None:
    artifact = _valid_artifact()
    by_asset_class = artifact["signal_evaluation"]["horizons"]["1d"]["by_asset_class"]
    _, bucket = next(iter(by_asset_class.items()))
    bucket["hit_rate"] = None
    assert validate_artifact(artifact) == []


def test_validate_warnings_must_be_list_of_strings() -> None:
    artifact = _valid_artifact()
    artifact["warnings"] = "bad"
    errors = validate_artifact(artifact)
    assert "'warnings' must be a list of strings" in errors
    artifact["warnings"] = [1, 2]
    errors = validate_artifact(artifact)
    assert "'warnings' must be a list of strings" in errors


def test_main_valid_file(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    path = tmp_path / "signals.json"
    path.write_text(json.dumps(_valid_artifact()), encoding="utf-8")
    assert main(["--input", str(path)]) == 0
    assert "OK" in capsys.readouterr().out


def test_main_invalid_file(tmp_path: Path) -> None:
    artifact = copy.deepcopy(_valid_artifact())
    del artifact["warnings"]
    path = tmp_path / "signals.json"
    path.write_text(json.dumps(artifact), encoding="utf-8")
    assert main(["--input", str(path)]) == 1


def test_main_missing_file(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--input", str(tmp_path / "missing.json")]) == 1
    assert "ERROR" in capsys.readouterr().out


def test_main_invalid_json(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    path = tmp_path / "bad.json"
    path.write_text("{not json", encoding="utf-8")
    assert main(["--input", str(path)]) == 1
    assert "ERROR" in capsys.readouterr().out
