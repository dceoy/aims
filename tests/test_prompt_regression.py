"""Tests for the prompt/model structural regression harness (#97)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from aims import prompt_regression
from aims.qualitative import DEFAULT_PROMPT_PATH, MODEL_ID, PROMPT_VERSION
from aims.validate_prompt_regression import validate_history
from aims.validate_qualitative import sha256_file

FIXTURES = Path(__file__).resolve().parent / "fixtures"
REPO_ROOT = Path(__file__).resolve().parent.parent
ARTIFACT = FIXTURES / "qualitative_2024-01-01.json"
GATED_ARTIFACT = FIXTURES / "qualitative_2024-01-01_gated.json"
ANALYSIS = FIXTURES / "analysis_2024-01-01_mapped.json"
EVIDENCE = FIXTURES / "evidence_2024-01-01.json"
RECORD = REPO_ROOT / "data/performance/prompt_regressions.json"


def _load(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        value: dict[str, Any] = json.load(stream)
    return value


@pytest.fixture
def metrics() -> dict[str, Any]:
    return prompt_regression.compute_metrics(
        _load(ARTIFACT), _load(ANALYSIS), _load(EVIDENCE)
    )


# ── metrics and checks ───────────────────────────────────────────────────────


def test_compute_metrics_on_clean_fixture(metrics: dict[str, Any]) -> None:
    assert metrics["validation_errors"] == 0
    assert metrics["instruments"] == 2
    assert metrics["instruments_gated"] == 0
    assert metrics["instrument_gate_pass_rate"] == 1.0
    assert metrics["market_narrative_withheld"] is False
    assert metrics["citation_coverage"] == 1.0
    assert metrics["stance_distribution"] == {
        "supportive": 1,
        "neutral": 1,
        "conflicting": 0,
    }
    assert metrics["distinct_evidence_cited"] == 3
    assert metrics["themes"] == 1


def test_compute_metrics_counts_gated_instruments() -> None:
    metrics = prompt_regression.compute_metrics(
        _load(GATED_ARTIFACT), _load(ANALYSIS), _load(EVIDENCE)
    )
    assert metrics["instruments_gated"] == 1
    assert metrics["instrument_gate_pass_rate"] == 0.5


def test_compute_metrics_handles_empty_artifact() -> None:
    artifact = {
        "metadata": {"analysis_date": "2024-01-01"},
        "market": {"narrative": "", "citations": [], "themes": []},
        "instruments": [],
    }
    metrics = prompt_regression.compute_metrics(artifact, {}, {})
    assert metrics["instrument_gate_pass_rate"] is None
    assert metrics["citation_coverage"] == 0.0


def test_run_checks_passes_clean_metrics(metrics: dict[str, Any]) -> None:
    checks = prompt_regression.run_checks(metrics)
    assert checks == {
        "validation_clean": True,
        "market_narrative_rendered": True,
        "instrument_gate_pass_rate": True,
        "citation_coverage": True,
        "stance_distribution_sane": True,
    }


def test_run_checks_flags_threshold_violations(metrics: dict[str, Any]) -> None:
    metrics["validation_errors"] = 2
    metrics["market_narrative_withheld"] = True
    metrics["instrument_gate_pass_rate"] = 0.4
    metrics["citation_coverage"] = 0.9
    metrics["instruments"] = 5
    metrics["stance_distribution"] = {"supportive": 5, "neutral": 0, "conflicting": 0}
    checks = prompt_regression.run_checks(metrics)
    assert not any(checks.values())


def test_run_checks_handles_missing_rates(metrics: dict[str, Any]) -> None:
    metrics["instrument_gate_pass_rate"] = None
    metrics["citation_coverage"] = None
    checks = prompt_regression.run_checks(metrics)
    assert checks["instrument_gate_pass_rate"] is False
    assert checks["citation_coverage"] is False


# ── recording ────────────────────────────────────────────────────────────────


def _entry(metrics: dict[str, Any]) -> dict[str, Any]:
    checks = prompt_regression.run_checks(metrics)
    return prompt_regression.build_entry(
        _load(ARTIFACT), ARTIFACT, metrics, checks, "ab" * 32
    )


def test_record_entry_creates_and_replaces(
    tmp_path: Path, metrics: dict[str, Any]
) -> None:
    record = tmp_path / "history.json"
    entry = _entry(metrics)
    prompt_regression.record_entry(entry, record)
    prompt_regression.record_entry(entry, record)
    history = _load(record)
    assert history["version"] == prompt_regression.PROMPT_REGRESSION_VERSION
    assert len(history["entries"]) == 1
    other = dict(entry, analysis_date="2024-02-02")
    prompt_regression.record_entry(other, record)
    assert len(_load(record)["entries"]) == 2


def test_record_entry_rejects_foreign_file(
    tmp_path: Path, metrics: dict[str, Any]
) -> None:
    record = tmp_path / "history.json"
    record.write_text('{"version": "0.0.1"}', encoding="utf-8")
    with pytest.raises(ValueError, match="not a valid prompt-regression"):
        prompt_regression.record_entry(_entry(metrics), record)


# ── CI guard: committed prompt/model must have a recorded passing run ────────


def test_committed_prompt_and_model_have_a_recorded_passing_entry() -> None:
    # Changing the prompt file, PROMPT_VERSION, or MODEL_ID without running the
    # regression harness and committing its record must fail CI.
    history = _load(RECORD)
    assert validate_history(history) == []
    prompt_sha = sha256_file(REPO_ROOT / DEFAULT_PROMPT_PATH)
    matching = [
        entry
        for entry in history["entries"]
        if entry["prompt_sha256"] == prompt_sha
        and entry["model_id"] == MODEL_ID
        and entry["prompt_version"] == PROMPT_VERSION
        and entry["passed"]
    ]
    assert matching, (
        "No passing prompt-regression entry recorded for the committed prompt"
        f" (sha256 {prompt_sha}) and model {MODEL_ID!r}. Run"
        " .agents/skills/qualitative-analysis/scripts/prompt_regression.py"
        " with --record data/performance/prompt_regressions.json and commit"
        " the result."
    )


# ── CLI ──────────────────────────────────────────────────────────────────────


def _cli_args(record: Path | None = None) -> list[str]:
    args = [
        "--artifact",
        str(ARTIFACT),
        "--analysis",
        str(ANALYSIS),
        "--evidence",
        str(EVIDENCE),
        "--prompt",
        str(REPO_ROOT / DEFAULT_PROMPT_PATH),
    ]
    if record is not None:
        args += ["--record", str(record)]
    return args


def test_main_passes_and_records(tmp_path: Path, capsys: Any) -> None:
    record = tmp_path / "history.json"
    assert prompt_regression.main(_cli_args(record)) == 0
    out = capsys.readouterr().out
    assert "PASS: validation_clean" in out
    assert "Recorded prompt-regression entry" in out
    history = _load(record)
    assert validate_history(history) == []
    entry = history["entries"][0]
    assert entry["passed"] is True
    assert entry["prompt_sha256"] == sha256_file(REPO_ROOT / DEFAULT_PROMPT_PATH)
    assert entry["artifact_provenance"]["prompt_sha256"] == "ab" * 32


def test_main_fails_on_threshold_and_still_records(tmp_path: Path, capsys: Any) -> None:
    record = tmp_path / "history.json"
    args = [
        "--artifact",
        str(GATED_ARTIFACT),
        "--analysis",
        str(ANALYSIS),
        "--evidence",
        str(EVIDENCE),
        "--prompt",
        str(REPO_ROOT / DEFAULT_PROMPT_PATH),
        "--record",
        str(record),
    ]
    assert prompt_regression.main(args) == 1
    assert "FAIL: instrument_gate_pass_rate" in capsys.readouterr().out
    assert _load(record)["entries"][0]["passed"] is False


def test_main_without_record_is_dry_run(capsys: Any) -> None:
    assert prompt_regression.main(_cli_args()) == 0
    assert "Recorded" not in capsys.readouterr().out


def test_main_reports_bad_record_file(tmp_path: Path, capsys: Any) -> None:
    record = tmp_path / "history.json"
    record.write_text('{"version": "0.0.1"}', encoding="utf-8")
    assert prompt_regression.main(_cli_args(record)) == 1
    assert "ERROR" in capsys.readouterr().out


def test_main_missing_and_invalid_inputs(tmp_path: Path, capsys: Any) -> None:
    args = _cli_args()
    args[1] = str(tmp_path / "absent.json")
    assert prompt_regression.main(args) == 1
    assert "file not found" in capsys.readouterr().out
    broken = tmp_path / "broken.json"
    broken.write_text("{", encoding="utf-8")
    args[1] = str(broken)
    assert prompt_regression.main(args) == 1
    assert "invalid JSON" in capsys.readouterr().out
