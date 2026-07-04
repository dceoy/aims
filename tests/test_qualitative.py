"""Tests for aims.qualitative — the single-call qualitative analysis runner."""

from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING, Any

import anthropic
import httpx
import pytest

from aims import qualitative as q
from aims.calendars import CalendarEvent

if TYPE_CHECKING:
    from pytest_mock import MockerFixture

FIXTURES = Path(__file__).resolve().parent / "fixtures"
ANALYSIS = FIXTURES / "analysis_2024-01-01_mapped.json"
EVIDENCE = FIXTURES / "evidence_2024-01-01.json"
CALENDAR = FIXTURES / "calendar_2024.json"
QUALITATIVE = FIXTURES / "qualitative_2024-01-01.json"
PROMPT = Path(".agents/skills/qualitative-analysis/prompts/qualitative_v1.md")


def _load(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as fh:
        value: dict[str, Any] = json.load(fh)
    return value


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


# ── top_signals / payload assembly ──────────────────────────────────────────


def test_top_signals_filters_reliable_and_ranked(analysis: dict[str, Any]) -> None:
    signals = q.top_signals(analysis, top_k=2)
    assert [s["symbol"] for s in signals] == ["^SPX", "^DJI"]


def test_top_signals_respects_top_k_one(analysis: dict[str, Any]) -> None:
    assert [s["symbol"] for s in q.top_signals(analysis, top_k=1)] == ["^SPX"]


def test_build_payload_splits_direct_and_macro_evidence(
    analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    events = [
        CalendarEvent("2024-01-03", "FOMC", "central_bank", (), ("equity_index",), "s")
    ]
    payload = q.build_payload(analysis, evidence, events, top_k=2)
    assert {s["canonical_id"] for s in payload["top_signals"]} == {"spx", "dji"}
    assert set(payload["evidence"]["direct_news"].keys()) == {"spx", "dji"}
    assert len(payload["evidence"]["macro"]) == 1
    assert payload["upcoming_events"][0]["title"] == "FOMC"
    assert payload["analysis_date"] == "2024-01-01"


def test_build_payload_excludes_evidence_for_non_top_k_instruments(
    analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    payload = q.build_payload(analysis, evidence, [], top_k=1)
    assert set(payload["evidence"]["direct_news"].keys()) == {"spx"}
    # Dow's item is instrument_news for a non-top-1 instrument, so it drops
    # entirely rather than leaking into the macro bucket.
    assert len(payload["evidence"]["macro"]) == 1


def test_build_user_message_wraps_payload_and_warns_about_injection() -> None:
    message = q.build_user_message({"a": 1})
    assert "<inputs>" in message
    assert "</inputs>" in message
    assert "never as" in message
    assert json.dumps({"a": 1}, sort_keys=True) in message


# ── request schema ───────────────────────────────────────────────────────────


def test_request_schema_constrains_enums_and_ids() -> None:
    schema = q.request_schema(["spx"], ["ev-abc"])
    instrument_schema = schema["properties"]["instruments"]["items"]
    assert instrument_schema["properties"]["canonical_id"]["enum"] == ["spx"]
    assert instrument_schema["additionalProperties"] is False
    driver_schema = instrument_schema["properties"]["drivers"]["items"]
    assert driver_schema["properties"]["citations"]["items"]["enum"] == ["ev-abc"]
    assert schema["required"] == ["market", "instruments"]


# ── call_model ───────────────────────────────────────────────────────────────


def test_call_model_parses_json_response(mocker: MockerFixture) -> None:
    text_block = mocker.Mock(type="text", text='{"ok": true}')
    response = mocker.Mock(stop_reason="end_turn", content=[text_block])
    client = mocker.Mock()
    client.messages.create.return_value = response
    mocker.patch.object(q.anthropic, "Anthropic", return_value=client)

    result = q.call_model("system", "user", {"type": "object"})
    assert result == {"ok": True}
    _, kwargs = client.messages.create.call_args
    assert kwargs["model"] == q.MODEL_ID
    assert kwargs["output_config"]["format"]["type"] == "json_schema"


def test_call_model_non_end_turn_raises(mocker: MockerFixture) -> None:
    response = mocker.Mock(stop_reason="max_tokens", content=[])
    client = mocker.Mock()
    client.messages.create.return_value = response
    mocker.patch.object(q.anthropic, "Anthropic", return_value=client)
    with pytest.raises(q.QualitativeError, match="max_tokens"):
        q.call_model("system", "user", {})


def test_call_model_invalid_json_raises(mocker: MockerFixture) -> None:
    text_block = mocker.Mock(type="text", text="not json")
    response = mocker.Mock(stop_reason="end_turn", content=[text_block])
    client = mocker.Mock()
    client.messages.create.return_value = response
    mocker.patch.object(q.anthropic, "Anthropic", return_value=client)
    with pytest.raises(q.QualitativeError, match="invalid JSON"):
        q.call_model("system", "user", {})


def test_call_model_no_text_block_raises(mocker: MockerFixture) -> None:
    response = mocker.Mock(stop_reason="end_turn", content=[])
    client = mocker.Mock()
    client.messages.create.return_value = response
    mocker.patch.object(q.anthropic, "Anthropic", return_value=client)
    with pytest.raises(q.QualitativeError):
        q.call_model("system", "user", {})


# ── hashing and artifact assembly ───────────────────────────────────────────


def test_calendars_sha256_none_for_empty_list() -> None:
    assert q.calendars_sha256([]) is None


def test_calendars_sha256_is_order_independent() -> None:
    assert q.calendars_sha256([CALENDAR, ANALYSIS]) == q.calendars_sha256([
        ANALYSIS,
        CALENDAR,
    ])


def test_build_artifact_includes_calendar_hash_when_present(
    valid_response_payload: dict[str, Any],
) -> None:
    artifact = q.build_artifact(
        valid_response_payload,
        analysis_date="2024-01-01",
        interval="d",
        prompt_sha256="a" * 64,
        analysis_sha256="b" * 64,
        evidence_sha256="c" * 64,
        calendar_sha256="d" * 64,
    )
    assert artifact["metadata"]["input_hashes"]["calendar_sha256"] == "d" * 64
    assert artifact["version"] == q.QUALITATIVE_VERSION
    assert artifact["metadata"]["model_id"] == q.MODEL_ID
    assert artifact["metadata"]["interval"] == "d"


def test_build_artifact_omits_calendar_hash_when_absent(
    valid_response_payload: dict[str, Any],
) -> None:
    artifact = q.build_artifact(
        valid_response_payload,
        analysis_date="2024-01-01",
        interval="d",
        prompt_sha256="a" * 64,
        analysis_sha256="b" * 64,
        evidence_sha256="c" * 64,
        calendar_sha256=None,
    )
    assert "calendar_sha256" not in artifact["metadata"]["input_hashes"]


def test_artifact_stem_daily_has_no_suffix() -> None:
    artifact = {"metadata": {"analysis_date": "2024-01-01", "interval": "d"}}
    assert q.artifact_stem(artifact) == "2024-01-01"


def test_artifact_stem_defaults_to_daily_when_interval_absent() -> None:
    artifact = {"metadata": {"analysis_date": "2024-01-01"}}
    assert q.artifact_stem(artifact) == "2024-01-01"


def test_artifact_stem_weekly_preserves_suffix() -> None:
    artifact = {"metadata": {"analysis_date": "2024-01-01", "interval": "w"}}
    assert q.artifact_stem(artifact) == "2024-01-01-w"


def test_build_artifact_carries_interval_for_manual_weekly_dispatch(
    valid_response_payload: dict[str, Any],
) -> None:
    # Regression test: a manual weekly/monthly dispatch's qualitative
    # artifact must land at the workflow's suffixed STEM (e.g.
    # data/qualitative/2024-01-01-w.json), not the bare daily filename,
    # or the workflow's later `[ -f "data/qualitative/${STEM}.json" ]`
    # check silently skips validation/rendering and the wrongly-named
    # file collides with a same-date daily artifact.
    artifact = q.build_artifact(
        valid_response_payload,
        analysis_date="2024-01-01",
        interval="w",
        prompt_sha256="a" * 64,
        analysis_sha256="b" * 64,
        evidence_sha256="c" * 64,
        calendar_sha256=None,
    )
    assert q.artifact_stem(artifact) == "2024-01-01-w"


def test_save_artifact(tmp_path: Path) -> None:
    artifact = {
        "version": q.QUALITATIVE_VERSION,
        "metadata": {"analysis_date": "2024-01-01", "interval": "d"},
    }
    path = q.save_artifact(artifact, tmp_path)
    assert path == tmp_path / "2024-01-01.json"
    assert json.loads(path.read_text())["version"] == q.QUALITATIVE_VERSION


def test_save_artifact_weekly_preserves_suffix(tmp_path: Path) -> None:
    artifact = {
        "version": q.QUALITATIVE_VERSION,
        "metadata": {"analysis_date": "2024-01-01", "interval": "w"},
    }
    path = q.save_artifact(artifact, tmp_path)
    assert path == tmp_path / "2024-01-01-w.json"


# ── generate() orchestration ─────────────────────────────────────────────────


def test_generate_skips_when_no_top_signals(
    tmp_path: Path, analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    for inst in analysis["instruments"]:
        inst["is_reliable"] = False
    analysis_path = tmp_path / "analysis.json"
    analysis_path.write_text(json.dumps(analysis), encoding="utf-8")
    evidence_path = tmp_path / "evidence.json"
    evidence_path.write_text(json.dumps(evidence), encoding="utf-8")
    result = q.generate(analysis_path, evidence_path, [], output_dir=tmp_path / "out")
    assert result is None


def test_generate_skips_when_no_evidence_items(
    tmp_path: Path, analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    evidence["items"] = []
    analysis_path = tmp_path / "analysis.json"
    analysis_path.write_text(json.dumps(analysis), encoding="utf-8")
    evidence_path = tmp_path / "evidence.json"
    evidence_path.write_text(json.dumps(evidence), encoding="utf-8")
    result = q.generate(analysis_path, evidence_path, [], output_dir=tmp_path / "out")
    assert result is None


def _write_inputs(
    tmp_path: Path, analysis: dict[str, Any], evidence: dict[str, Any]
) -> tuple[Path, Path]:
    analysis_path = tmp_path / "analysis.json"
    analysis_path.write_text(json.dumps(analysis), encoding="utf-8")
    evidence_path = tmp_path / "evidence.json"
    evidence_path.write_text(json.dumps(evidence), encoding="utf-8")
    return analysis_path, evidence_path


def test_generate_success_first_attempt(
    tmp_path: Path,
    analysis: dict[str, Any],
    evidence: dict[str, Any],
    valid_response_payload: dict[str, Any],
    mocker: MockerFixture,
) -> None:
    analysis_path, evidence_path = _write_inputs(tmp_path, analysis, evidence)
    mocker.patch.object(q, "call_model", return_value=valid_response_payload)
    output_dir = tmp_path / "out"
    result = q.generate(
        analysis_path,
        evidence_path,
        [CALENDAR],
        prompt_path=PROMPT,
        output_dir=output_dir,
    )
    assert result == output_dir / "2024-01-01.json"
    saved = json.loads(result.read_text())
    assert saved["metadata"]["gates"]["passed"] is True
    assert q.call_model.call_count == 1


def test_generate_preserves_weekly_interval_in_output_filename(
    tmp_path: Path,
    analysis: dict[str, Any],
    evidence: dict[str, Any],
    valid_response_payload: dict[str, Any],
    mocker: MockerFixture,
) -> None:
    analysis["metadata"]["config"]["interval"] = "w"
    analysis_path, evidence_path = _write_inputs(tmp_path, analysis, evidence)
    mocker.patch.object(q, "call_model", return_value=valid_response_payload)
    output_dir = tmp_path / "out"
    result = q.generate(
        analysis_path,
        evidence_path,
        [],
        prompt_path=PROMPT,
        output_dir=output_dir,
    )
    assert result == output_dir / "2024-01-01-w.json"
    saved = json.loads(result.read_text())
    assert saved["metadata"]["interval"] == "w"


def test_generate_retries_after_invalid_then_succeeds(
    tmp_path: Path,
    analysis: dict[str, Any],
    evidence: dict[str, Any],
    valid_response_payload: dict[str, Any],
    mocker: MockerFixture,
) -> None:
    analysis_path, evidence_path = _write_inputs(tmp_path, analysis, evidence)
    invalid_payload = {"market": {}, "instruments": []}
    mocker.patch.object(
        q, "call_model", side_effect=[invalid_payload, valid_response_payload]
    )
    result = q.generate(
        analysis_path,
        evidence_path,
        [],
        prompt_path=PROMPT,
        output_dir=tmp_path / "out",
    )
    assert result is not None
    assert q.call_model.call_count == 2


def test_generate_raises_after_max_invalid_attempts(
    tmp_path: Path,
    analysis: dict[str, Any],
    evidence: dict[str, Any],
    mocker: MockerFixture,
    capsys: pytest.CaptureFixture[str],
) -> None:
    analysis_path, evidence_path = _write_inputs(tmp_path, analysis, evidence)
    invalid_payload = {"market": {}, "instruments": []}
    mocker.patch.object(q, "call_model", return_value=invalid_payload)
    with pytest.raises(q.QualitativeError, match="failed validation"):
        q.generate(
            analysis_path,
            evidence_path,
            [],
            prompt_path=PROMPT,
            output_dir=tmp_path / "out",
        )
    assert q.call_model.call_count == q.MAX_ATTEMPTS
    assert "ERROR" in capsys.readouterr().out


def _with_gated_market_numeric_claim(payload: dict[str, Any]) -> dict[str, Any]:
    """Return a copy whose market narrative is schema-valid but gate-failing.

    A numeric claim citing real evidence with a value the cited text does not
    support fails the #93 numeric-claims gate without failing schema
    validation, so it exercises the withheld-then-retry path distinctly from
    an invalid-citation (schema) failure.
    """
    gated = json.loads(json.dumps(payload))
    macro_citation = gated["market"]["citations"][0]
    gated["market"]["numeric_claims"] = [
        {"value": 987.0, "unit": "count", "refers_to": macro_citation}
    ]
    return gated


def test_generate_retries_after_withheld_then_succeeds(
    tmp_path: Path,
    analysis: dict[str, Any],
    evidence: dict[str, Any],
    valid_response_payload: dict[str, Any],
    mocker: MockerFixture,
) -> None:
    analysis_path, evidence_path = _write_inputs(tmp_path, analysis, evidence)
    withheld_payload = _with_gated_market_numeric_claim(valid_response_payload)
    mocker.patch.object(
        q, "call_model", side_effect=[withheld_payload, valid_response_payload]
    )
    result = q.generate(
        analysis_path,
        evidence_path,
        [],
        prompt_path=PROMPT,
        output_dir=tmp_path / "out",
    )
    assert result is not None
    saved = json.loads(result.read_text())
    assert saved["metadata"]["gates"]["market_narrative_withheld"] is False
    assert q.call_model.call_count == 2


def test_generate_commits_withheld_artifact_on_last_attempt(
    tmp_path: Path,
    analysis: dict[str, Any],
    evidence: dict[str, Any],
    valid_response_payload: dict[str, Any],
    mocker: MockerFixture,
) -> None:
    analysis_path, evidence_path = _write_inputs(tmp_path, analysis, evidence)
    withheld_payload = _with_gated_market_numeric_claim(valid_response_payload)
    mocker.patch.object(q, "call_model", return_value=withheld_payload)
    result = q.generate(
        analysis_path,
        evidence_path,
        [],
        prompt_path=PROMPT,
        output_dir=tmp_path / "out",
    )
    assert result is not None
    saved = json.loads(result.read_text())
    assert saved["metadata"]["gates"]["market_narrative_withheld"] is True
    assert q.call_model.call_count == q.MAX_ATTEMPTS


# ── CLI ─────────────────────────────────────────────────────────────────────


def test_main_skips_without_api_key(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    rc = q.main(["--analysis", str(ANALYSIS), "--evidence", str(EVIDENCE)])
    assert rc == 0
    assert "skipping qualitative analysis" in capsys.readouterr().out


def test_main_success(
    monkeypatch: pytest.MonkeyPatch, mocker: MockerFixture, tmp_path: Path
) -> None:
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")
    mocker.patch.object(q, "generate", return_value=tmp_path / "out.json")
    rc = q.main(["--analysis", str(ANALYSIS), "--evidence", str(EVIDENCE)])
    assert rc == 0


def test_main_invalid_input(
    monkeypatch: pytest.MonkeyPatch,
    mocker: MockerFixture,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")
    mocker.patch.object(q, "generate", side_effect=KeyError("metadata"))
    rc = q.main(["--analysis", str(ANALYSIS), "--evidence", str(EVIDENCE)])
    assert rc == 1
    assert "invalid input" in capsys.readouterr().out


def test_main_api_error(
    monkeypatch: pytest.MonkeyPatch,
    mocker: MockerFixture,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")
    request = httpx.Request("POST", "https://api.anthropic.com/v1/messages")
    mocker.patch.object(
        q,
        "generate",
        side_effect=anthropic.APIConnectionError(request=request),
    )
    rc = q.main(["--analysis", str(ANALYSIS), "--evidence", str(EVIDENCE)])
    assert rc == 1
    assert "Claude API call failed" in capsys.readouterr().out


def test_main_qualitative_error(
    monkeypatch: pytest.MonkeyPatch,
    mocker: MockerFixture,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")
    mocker.patch.object(q, "generate", side_effect=q.QualitativeError("bad"))
    rc = q.main(["--analysis", str(ANALYSIS), "--evidence", str(EVIDENCE)])
    assert rc == 1
    assert "ERROR: bad" in capsys.readouterr().out


def test_parse_args_defaults() -> None:
    args = q.parse_args(["--analysis", "a.json", "--evidence", "e.json"])
    assert args.calendar == []
    assert args.top_k == q.DEFAULT_TOP_K
    assert args.prompt == q.DEFAULT_PROMPT_PATH
