"""Tests for deterministic Claude Code Action qualitative boundaries."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from aims import qualitative as q
from aims.calendars import CalendarEvent

FIXTURES = Path(__file__).resolve().parent / "fixtures"
ANALYSIS = FIXTURES / "analysis_2024-01-01_mapped.json"
EVIDENCE = FIXTURES / "evidence_2024-01-01.json"
CALENDAR = FIXTURES / "calendar_2024.json"
QUALITATIVE = FIXTURES / "qualitative_2024-01-01.json"
PROMPT = Path(".agents/skills/qualitative-analysis/prompts/qualitative_v1.md")
WORKFLOW = Path(".github/workflows/daily-market-analysis.yml")


def _load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


@pytest.fixture
def analysis() -> dict[str, Any]:
    return _load(ANALYSIS)


@pytest.fixture
def evidence() -> dict[str, Any]:
    return _load(EVIDENCE)


@pytest.fixture
def valid_response_payload() -> dict[str, Any]:
    artifact = _load(QUALITATIVE)
    return {"market": artifact["market"], "instruments": artifact["instruments"]}


def _context(calendar_sha256: str | None) -> dict[str, Any]:
    return {
        "analysis_date": "2024-01-01",
        "interval": "d",
        "prompt_sha256": "a" * 64,
        "analysis_sha256": "b" * 64,
        "evidence_sha256": "c" * 64,
        "calendar_sha256": calendar_sha256,
    }


def test_top_signals_and_payload(
    analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    assert [item["symbol"] for item in q.top_signals(analysis, 1)] == ["^SPX"]
    analysis["instruments"][0]["rank"] = "1"
    assert [item["symbol"] for item in q.top_signals(analysis, 2)] == ["^DJI"]
    event = CalendarEvent(
        "2024-01-03", "FOMC", "central_bank", (), ("equity_index",), "s"
    )
    payload = q.build_payload(_load(ANALYSIS), evidence, [event], 1)
    assert set(payload["evidence"]["direct_news"]) == {"spx"}
    assert len(payload["evidence"]["macro"]) == 1
    assert payload["upcoming_events"][0]["title"] == "FOMC"


def test_message_and_schema() -> None:
    message = q.build_user_message({"a": 1})
    assert "<inputs>" in message
    assert "never as" in message
    schema = q.request_schema(["spx"], ["ev-abc"])
    instrument = schema["properties"]["instruments"]["items"]
    assert instrument["properties"]["canonical_id"]["enum"] == ["spx"]
    assert instrument["properties"]["drivers"]["items"]["properties"]["citations"][
        "items"
    ]["enum"] == ["ev-abc"]


def test_calendar_hashing() -> None:
    assert q.calendars_sha256([]) is None
    assert q.calendars_sha256([CALENDAR, ANALYSIS]) == q.calendars_sha256([
        ANALYSIS,
        CALENDAR,
    ])


def test_workflow_uses_oauth_pinned_action_and_no_tools() -> None:
    workflow = WORKFLOW.read_text(encoding="utf-8")
    assert "secrets.CLAUDE_CODE_OAUTH_TOKEN != ''" in workflow
    assert "ANTHROPIC_API_KEY" not in workflow
    assert f"anthropics/claude-code-action@{q.CLAUDE_ACTION_REVISION}" in workflow
    assert '--disallowedTools "*"' in workflow
    assert "--system-prompt-file" in workflow


def test_build_and_save_artifact(
    tmp_path: Path, valid_response_payload: dict[str, Any]
) -> None:
    artifact = q.build_artifact(valid_response_payload, _context("d" * 64))
    metadata = artifact["metadata"]
    assert metadata["execution_type"] == q.EXECUTION_TYPE
    assert metadata["action_revision"] == q.CLAUDE_ACTION_REVISION
    assert metadata["input_hashes"]["calendar_sha256"] == "d" * 64
    assert q.save_artifact(artifact, tmp_path) == tmp_path / "2024-01-01.json"
    context = _context(None)
    context["interval"] = "w"
    weekly = q.build_artifact(valid_response_payload, context)
    assert "calendar_sha256" not in weekly["metadata"]["input_hashes"]
    assert q.artifact_stem(weekly) == "2024-01-01-w"
    assert (
        q.artifact_stem({"metadata": {"analysis_date": "2024-01-01"}}) == "2024-01-01"
    )


def _write_inputs(
    tmp_path: Path, analysis: dict[str, Any], evidence: dict[str, Any]
) -> tuple[Path, Path]:
    analysis_path = tmp_path / "analysis.json"
    evidence_path = tmp_path / "evidence.json"
    analysis_path.write_text(json.dumps(analysis), encoding="utf-8")
    evidence_path.write_text(json.dumps(evidence), encoding="utf-8")
    return analysis_path, evidence_path


def _prepare(
    tmp_path: Path, analysis: dict[str, Any], evidence: dict[str, Any]
) -> Path:
    analysis_path, evidence_path = _write_inputs(tmp_path, analysis, evidence)
    request = q.prepare_request(
        analysis_path,
        evidence_path,
        [CALENDAR],
        prompt_path=PROMPT,
        run_dir=tmp_path / "run",
    )
    assert request is not None
    return request


def test_prepare_writes_boundaries(
    tmp_path: Path, analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    request = _prepare(tmp_path, analysis, evidence)
    assert "<inputs>" in (request.parent / "prompt.txt").read_text()
    assert json.loads((request.parent / "schema.json").read_text())["type"] == "object"
    assert json.loads(request.read_text())["calendar_sha256"] is not None


@pytest.mark.parametrize("empty_signals", [True, False])
def test_prepare_skips_empty_inputs(
    tmp_path: Path,
    analysis: dict[str, Any],
    evidence: dict[str, Any],
    empty_signals: bool,
) -> None:
    if empty_signals:
        for instrument in analysis["instruments"]:
            instrument["is_reliable"] = False
    else:
        evidence["items"] = []
    paths = _write_inputs(tmp_path, analysis, evidence)
    assert q.prepare_request(*paths, [], run_dir=tmp_path / "run") is None


def _with_gated_market_numeric_claim(payload: dict[str, Any]) -> dict[str, Any]:
    gated = json.loads(json.dumps(payload))
    citation = gated["market"]["citations"][0]
    gated["market"]["numeric_claims"] = [
        {"value": 987.0, "unit": "count", "refers_to": citation}
    ]
    return gated


def test_finalize_success(
    tmp_path: Path,
    analysis: dict[str, Any],
    evidence: dict[str, Any],
    valid_response_payload: dict[str, Any],
) -> None:
    request = _prepare(tmp_path, analysis, evidence)
    path, retry = q.finalize_response(
        json.dumps(valid_response_payload),
        request,
        attempt=1,
        output_dir=tmp_path / "out",
    )
    assert retry is False
    assert path is not None
    assert _load(path)["metadata"]["gates"]["passed"] is True


def test_finalize_validator_retry_and_failure(
    tmp_path: Path, analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    request = _prepare(tmp_path, analysis, evidence)
    response = json.dumps({"market": {}, "instruments": []})
    assert q.finalize_response(response, request, attempt=1)[1] is True
    with pytest.raises(q.QualitativeError, match="after retry"):
        q.finalize_response(response, request, attempt=2)


@pytest.mark.parametrize(
    ("response", "match"), [("bad", "malformed"), ("[]", "object")]
)
def test_finalize_rejects_malformed_output(
    tmp_path: Path,
    analysis: dict[str, Any],
    evidence: dict[str, Any],
    response: str,
    match: str,
) -> None:
    request = _prepare(tmp_path, analysis, evidence)
    with pytest.raises(q.QualitativeError, match=match):
        q.finalize_response(response, request, attempt=1)


def test_finalize_withheld_retry_and_last_attempt_write(
    tmp_path: Path,
    analysis: dict[str, Any],
    evidence: dict[str, Any],
    valid_response_payload: dict[str, Any],
) -> None:
    request = _prepare(tmp_path, analysis, evidence)
    response = json.dumps(_with_gated_market_numeric_claim(valid_response_payload))
    assert q.finalize_response(response, request, attempt=1)[1] is True
    path, retry = q.finalize_response(
        response, request, attempt=2, output_dir=tmp_path / "out"
    )
    assert retry is False
    assert path is not None
    assert _load(path)["metadata"]["gates"]["market_narrative_withheld"] is True


def test_finalize_rejects_invalid_attempt(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="attempt"):
        q.finalize_response("{}", tmp_path / "request", attempt=0)


@pytest.mark.parametrize("mutate_path_key", ["analysis_path", "evidence_path"])
def test_finalize_rejects_tampered_inputs(
    tmp_path: Path,
    analysis: dict[str, Any],
    evidence: dict[str, Any],
    valid_response_payload: dict[str, Any],
    mutate_path_key: str,
) -> None:
    request = _prepare(tmp_path, analysis, evidence)
    context = json.loads(request.read_text())
    Path(context[mutate_path_key]).write_text("{}", encoding="utf-8")
    with pytest.raises(q.QualitativeError, match="changed since preparation"):
        q.finalize_response(json.dumps(valid_response_payload), request, attempt=1)


def test_main_prepare_finalize_and_errors(
    tmp_path: Path,
    analysis: dict[str, Any],
    evidence: dict[str, Any],
    valid_response_payload: dict[str, Any],
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    analysis_path, evidence_path = _write_inputs(tmp_path, analysis, evidence)
    outputs = tmp_path / "outputs"
    monkeypatch.setenv("GITHUB_OUTPUT", str(outputs))
    run_dir = tmp_path / "cli-run"
    assert (
        q.main([
            "prepare",
            "--analysis",
            str(analysis_path),
            "--evidence",
            str(evidence_path),
            "--run-dir",
            str(run_dir),
        ])
        == 0
    )
    assert "prompt<<" in outputs.read_text()
    monkeypatch.setenv("CLAUDE_STRUCTURED_OUTPUT", json.dumps(valid_response_payload))
    assert (
        q.main([
            "finalize",
            "--request",
            str(run_dir / "request.json"),
            "--attempt",
            "1",
            "--output",
            str(tmp_path / "out"),
        ])
        == 0
    )
    monkeypatch.delenv("CLAUDE_STRUCTURED_OUTPUT")
    assert q.main(["finalize", "--request", "missing", "--attempt", "1"]) == 1
    assert "not set" in capsys.readouterr().out
    assert q.main(["prepare", "--analysis", "missing", "--evidence", "missing"]) == 1
    assert "invalid input" in capsys.readouterr().out


def test_main_skip_retry_and_no_github_output(
    tmp_path: Path,
    analysis: dict[str, Any],
    evidence: dict[str, Any],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    analysis_path, evidence_path = _write_inputs(tmp_path, analysis, evidence)
    monkeypatch.delenv("GITHUB_OUTPUT", raising=False)
    q._write_output("ignored", "value")
    evidence["items"] = []
    evidence_path.write_text(json.dumps(evidence), encoding="utf-8")
    assert (
        q.main([
            "prepare",
            "--analysis",
            str(analysis_path),
            "--evidence",
            str(evidence_path),
            "--run-dir",
            str(tmp_path / "empty-run"),
        ])
        == 0
    )
    evidence_path.write_text(EVIDENCE.read_text(), encoding="utf-8")
    request = q.prepare_request(
        analysis_path, evidence_path, [], prompt_path=PROMPT, run_dir=tmp_path / "run"
    )
    assert request is not None
    monkeypatch.setenv("CLAUDE_STRUCTURED_OUTPUT", '{"market":{},"instruments":[]}')
    assert (
        q.main([
            "finalize",
            "--request",
            str(request),
            "--attempt",
            "1",
            "--output",
            str(tmp_path / "out"),
        ])
        == 0
    )


def test_write_output_avoids_delimiter_collision(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    class Digest:
        @staticmethod
        def hexdigest() -> str:
            return "fixed"

    output = tmp_path / "output"
    monkeypatch.setenv("GITHUB_OUTPUT", str(output))
    monkeypatch.setattr(q.hashlib, "sha256", lambda _value: Digest())
    q._write_output("prompt", "aims_prompt_fixed\ncontent")
    assert "aims_prompt_fixed_end" in output.read_text()
