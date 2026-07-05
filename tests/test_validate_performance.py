"""Tests for the stance-evaluation performance artifact validator."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from aims.validate_performance import main, validate_artifact

REPO_ROOT = Path(__file__).resolve().parent.parent
COMMITTED = REPO_ROOT / "data/performance/2026-07-04.json"


@pytest.fixture
def artifact() -> dict[str, Any]:
    with COMMITTED.open(encoding="utf-8") as stream:
        value: dict[str, Any] = json.load(stream)
    return value


def test_committed_artifact_is_valid(artifact: dict[str, Any]) -> None:
    assert validate_artifact(artifact) == []


def test_missing_top_key_short_circuits(artifact: dict[str, Any]) -> None:
    del artifact["warnings"]
    assert validate_artifact(artifact) == ["missing required key: 'warnings'"]


def test_wrong_version(artifact: dict[str, Any]) -> None:
    artifact["version"] = "9.9.9"
    assert any("unsupported version" in e for e in validate_artifact(artifact))


def test_metadata_must_be_object(artifact: dict[str, Any]) -> None:
    artifact["metadata"] = []
    assert "'metadata' must be a JSON object" in validate_artifact(artifact)


def test_metadata_missing_key(artifact: dict[str, Any]) -> None:
    del artifact["metadata"]["disclaimer"]
    assert "metadata missing required key: 'disclaimer'" in validate_artifact(artifact)


@pytest.mark.parametrize(
    "horizons",
    [[], [0], [1, 1], ["1"], [True], "1,5,20"],
)
def test_bad_config_horizons(artifact: dict[str, Any], horizons: Any) -> None:
    artifact["metadata"]["config"]["horizons"] = horizons
    assert (
        "metadata.config.horizons must be unique positive integers"
        in validate_artifact(artifact)
    )


def test_config_must_be_object(artifact: dict[str, Any]) -> None:
    artifact["metadata"]["config"] = "x"
    assert "metadata.config must be a JSON object" in validate_artifact(artifact)


def test_config_requires_return_consistency_tolerance(
    artifact: dict[str, Any],
) -> None:
    del artifact["metadata"]["config"]["return_consistency_tolerance"]
    assert (
        "metadata.config.return_consistency_tolerance must be a non-negative"
        " number" in validate_artifact(artifact)
    )


@pytest.mark.parametrize("tolerance", [-0.001, "0.001", True])
def test_config_rejects_bad_return_consistency_tolerance(
    artifact: dict[str, Any], tolerance: Any
) -> None:
    artifact["metadata"]["config"]["return_consistency_tolerance"] = tolerance
    assert (
        "metadata.config.return_consistency_tolerance must be a non-negative"
        " number" in validate_artifact(artifact)
    )


def test_config_accepts_zero_tolerance(artifact: dict[str, Any]) -> None:
    artifact["metadata"]["config"]["return_consistency_tolerance"] = 0
    assert (
        "metadata.config.return_consistency_tolerance must be a non-negative"
        " number" not in validate_artifact(artifact)
    )


def test_inputs_must_be_object(artifact: dict[str, Any]) -> None:
    artifact["metadata"]["inputs"] = "x"
    assert "metadata.inputs must be a JSON object" in validate_artifact(artifact)


def test_inputs_dates_must_be_valid(artifact: dict[str, Any]) -> None:
    artifact["metadata"]["inputs"]["analysis_dates"] = ["2026-07-04", "bad"]
    errors = validate_artifact(artifact)
    assert "metadata.inputs.analysis_dates must be a list of YYYY-MM-DD dates" in errors


def test_inputs_dates_must_be_sorted(artifact: dict[str, Any]) -> None:
    artifact["metadata"]["inputs"]["qualitative_dates"] = [
        "2026-07-04",
        "2026-07-01",
    ]
    assert "metadata.inputs.qualitative_dates must be sorted" in validate_artifact(
        artifact
    )


def test_bad_analysis_date(artifact: dict[str, Any]) -> None:
    artifact["metadata"]["analysis_date"] = "July 4"
    assert any("analysis_date" in e for e in validate_artifact(artifact))


def test_stance_evaluation_must_be_object(artifact: dict[str, Any]) -> None:
    artifact["stance_evaluation"] = 3
    assert "'stance_evaluation' must be a JSON object" in validate_artifact(artifact)


def test_stance_evaluation_missing_key(artifact: dict[str, Any]) -> None:
    del artifact["stance_evaluation"]["unmatched"]
    assert "stance_evaluation missing required key: 'unmatched'" in validate_artifact(
        artifact
    )


def test_stance_evaluation_counts_must_be_counts(artifact: dict[str, Any]) -> None:
    artifact["stance_evaluation"]["excluded_gated"] = -1
    assert (
        "stance_evaluation.excluded_gated must be a non-negative integer"
        in validate_artifact(artifact)
    )


def test_horizons_must_be_object(artifact: dict[str, Any]) -> None:
    artifact["stance_evaluation"]["horizons"] = []
    assert "stance_evaluation.horizons must be a JSON object" in validate_artifact(
        artifact
    )


def test_horizon_keys_must_match_config(artifact: dict[str, Any]) -> None:
    del artifact["stance_evaluation"]["horizons"]["20d"]
    assert (
        "stance_evaluation.horizons keys do not match metadata.config.horizons"
        in validate_artifact(artifact)
    )


def test_horizon_must_be_object(artifact: dict[str, Any]) -> None:
    artifact["stance_evaluation"]["horizons"]["1d"] = 4
    assert "stance_evaluation.horizons.1d must be a JSON object" in validate_artifact(
        artifact
    )


def test_horizon_missing_key(artifact: dict[str, Any]) -> None:
    del artifact["stance_evaluation"]["horizons"]["1d"]["pending"]
    assert (
        "stance_evaluation.horizons.1d missing required key: 'pending'"
        in validate_artifact(artifact)
    )


def test_horizon_counts_must_be_counts(artifact: dict[str, Any]) -> None:
    artifact["stance_evaluation"]["horizons"]["1d"]["observations"] = True
    assert (
        "stance_evaluation.horizons.1d.observations must be a non-negative integer"
        in validate_artifact(artifact)
    )


def test_stances_must_map_exact_enum(artifact: dict[str, Any]) -> None:
    del artifact["stance_evaluation"]["horizons"]["1d"]["stances"]["neutral"]
    assert any("must map exactly the stances" in e for e in validate_artifact(artifact))


def test_stance_bucket_must_be_object(artifact: dict[str, Any]) -> None:
    artifact["stance_evaluation"]["horizons"]["1d"]["stances"]["neutral"] = 1
    assert (
        "stance_evaluation.horizons.1d.stances.neutral must be a JSON object"
        in validate_artifact(artifact)
    )


def test_stance_bucket_count_and_rate(artifact: dict[str, Any]) -> None:
    bucket = artifact["stance_evaluation"]["horizons"]["1d"]["stances"]["supportive"]
    bucket["count"] = "3"
    bucket["hit_rate"] = 1.5
    bucket["average_return"] = "x"
    errors = validate_artifact(artifact)
    where = "stance_evaluation.horizons.1d.stances.supportive"
    assert f"{where}.count must be a non-negative integer" in errors
    assert f"{where}.hit_rate must be null or a number in [0, 1]" in errors
    assert f"{where}.average_return must be null or a number" in errors


def test_boolean_rate_is_rejected(artifact: dict[str, Any]) -> None:
    bucket = artifact["stance_evaluation"]["horizons"]["1d"]["stances"]["supportive"]
    bucket["hit_rate"] = True
    assert any("hit_rate" in e for e in validate_artifact(artifact))


def test_calibration_must_map_exact_enum(artifact: dict[str, Any]) -> None:
    calibration = artifact["stance_evaluation"]["horizons"]["1d"][
        "confidence_calibration"
    ]
    calibration["extreme"] = calibration.pop("high")
    assert any(
        "must map exactly the confidence levels" in e
        for e in validate_artifact(artifact)
    )


def test_absent_config_inputs_and_horizons_only_report_missing_keys(
    artifact: dict[str, Any],
) -> None:
    del artifact["metadata"]["config"]
    del artifact["metadata"]["inputs"]
    del artifact["stance_evaluation"]["horizons"]
    errors = validate_artifact(artifact)
    assert "metadata missing required key: 'config'" in errors
    assert "metadata missing required key: 'inputs'" in errors
    assert "stance_evaluation missing required key: 'horizons'" in errors


def test_warnings_must_be_strings(artifact: dict[str, Any]) -> None:
    artifact["warnings"] = [1]
    assert "'warnings' must be a list of strings" in validate_artifact(artifact)


# ── CLI ──────────────────────────────────────────────────────────────────────


def test_main_validates_committed_artifact(capsys: Any) -> None:
    assert main(["--input", str(COMMITTED)]) == 0
    assert "OK" in capsys.readouterr().out


def test_main_reports_errors(tmp_path: Path, capsys: Any) -> None:
    bad = tmp_path / "bad.json"
    bad.write_text('{"version": "1.0.0"}', encoding="utf-8")
    assert main(["--input", str(bad)]) == 1
    assert "missing required key" in capsys.readouterr().out


def test_main_missing_and_invalid_files(tmp_path: Path, capsys: Any) -> None:
    assert main(["--input", str(tmp_path / "absent.json")]) == 1
    assert "file not found" in capsys.readouterr().out
    broken = tmp_path / "broken.json"
    broken.write_text("{", encoding="utf-8")
    assert main(["--input", str(broken)]) == 1
    assert "invalid JSON" in capsys.readouterr().out
