from __future__ import annotations

import json
import urllib.error
from typing import TYPE_CHECKING, Any

import pytest

import aims.qualitative as q
import aims.validate_qualitative as vq
from tests.test_validate_qualitative import make_analysis, make_evidence

if TYPE_CHECKING:
    from pathlib import Path

    from pytest_mock import MockerFixture

_A = "a" * 16
_B = "b" * 16

_GENERATED_AT = "2024-01-01T02:00:00+00:00"


def make_output() -> dict[str, Any]:
    return {
        "market_narrative": {
            "text": "Large caps gained 3.1% into year-end while the Fed held.",
            "citations": [_A, _B],
        },
        "themes": [
            {
                "title": "Rate pause",
                "text": "The Fed held rates, supporting risk assets.",
                "citations": [_B],
            }
        ],
        "instruments": [
            {
                "canonical_id": "spx",
                "stance": "supportive",
                "confidence": "high",
                "drivers": [
                    {
                        "text": "A weekly gain of 3.1% aligns with the signal.",
                        "citations": [_A],
                    }
                ],
            }
        ],
    }


def _assemble(output: dict[str, Any]) -> dict[str, Any]:
    return q.assemble_artifact(
        output,
        analysis=make_analysis(),
        evidence=make_evidence(),
        generated_at=_GENERATED_AT,
        model="claude-test",
        input_hashes={"analysis": "x", "evidence": "y"},
    )


# ── prompt building ─────────────────────────────────────────────────────────────


def test_build_prompt_structure() -> None:
    system, user = q.build_prompt(
        make_analysis(),
        make_evidence(),
        [
            {
                "date": "2024-01-03",
                "name": "FOMC rate decision",
                "category": "macro",
                "canonical_ids": [],
                "asset_classes": ["equity_index"],
                "source_url": "https://example.gov",
            }
        ],
    )
    assert "untrusted" in system
    assert "record_qualitative_analysis" in system
    assert "<analysis>" in user
    assert "<evidence>" in user
    assert "<upcoming_events>" in user
    assert '"spx"' in user
    assert '"dji"' in user
    assert "^NDX" not in user  # no canonical_id -> excluded from the prompt
    assert _A in user
    assert "FOMC rate decision" in user


def test_prompt_instrument_rounds_percentages() -> None:
    inst = make_analysis()["instruments"][0]
    block = q._prompt_instrument(inst)
    assert block["features_pct"]["ret_5d"] == 3.1
    assert block["rsi_14"] == 62.0


def test_prompt_instrument_handles_missing_features() -> None:
    block = q._prompt_instrument({"canonical_id": "x", "features": None})
    assert block["features_pct"]["ret_1d"] is None
    assert block["rsi_14"] is None


def test_round_pct_rejects_bool() -> None:
    assert q._round_pct(True) is None  # noqa: FBT003
    assert q._round_pct(0.0312) == 3.1
    assert q._round_pct(None) is None


def test_build_tool_schema_enums() -> None:
    schema = q.build_tool_schema()
    stances = schema["properties"]["instruments"]["items"]["properties"]["stance"]
    assert stances == {"enum": ["supportive", "neutral", "conflicting"]}
    assert schema["required"] == ["market_narrative", "themes", "instruments"]


# ── call_model ──────────────────────────────────────────────────────────────────


def _mock_response(mocker: MockerFixture, body: dict[str, Any]) -> Any:
    response = mocker.MagicMock()
    response.read.return_value = json.dumps(body).encode()
    response.__enter__.return_value = response
    return mocker.patch.object(q.urllib.request, "urlopen", return_value=response)


def test_call_model_returns_tool_input(mocker: MockerFixture) -> None:
    urlopen = _mock_response(
        mocker,
        {
            "content": [
                {"type": "text", "text": "thinking"},
                {"type": "tool_use", "name": "t", "input": {"themes": []}},
            ]
        },
    )
    result = q.call_model("key", model="claude-test", system="s", user="u")
    assert result == {"themes": []}
    request = urlopen.call_args[0][0]
    assert request.get_header("X-api-key") == "key"
    payload = json.loads(request.data.decode())
    assert payload["temperature"] == 0
    assert payload["tool_choice"] == {
        "type": "tool",
        "name": "record_qualitative_analysis",
    }


def test_call_model_no_tool_use(mocker: MockerFixture) -> None:
    _mock_response(mocker, {"content": [{"type": "text", "text": "hi"}]})
    with pytest.raises(q.QualitativeGenerationError, match="no tool_use"):
        q.call_model("key", model="claude-test", system="s", user="u")


def test_call_model_tool_use_input_not_dict(mocker: MockerFixture) -> None:
    _mock_response(mocker, {"content": [{"type": "tool_use", "input": "bad"}, "junk"]})
    with pytest.raises(q.QualitativeGenerationError):
        q.call_model("key", model="claude-test", system="s", user="u")


# ── content_hash / _clean_citations ────────────────────────────────────────────


def test_content_hash_is_canonical() -> None:
    assert q.content_hash({"a": 1, "b": 2}) == q.content_hash({"b": 2, "a": 1})
    assert q.content_hash({"a": 1}) != q.content_hash({"a": 2})


def test_clean_citations() -> None:
    known = {_A, _B}
    assert q._clean_citations("bad", known) == []
    assert q._clean_citations([_A, _A, "f" * 16, 3, _B], known) == [_A, _B]
    assert q._clean_citations([_A] * 20, known) == [_A]


# ── assemble_artifact ───────────────────────────────────────────────────────────


def test_assemble_artifact_valid_output() -> None:
    artifact = _assemble(make_output())
    assert artifact["version"] == "1.0.0"
    assert artifact["metadata"]["model"] == "claude-test"
    assert artifact["metadata"]["input_hashes"] == {"analysis": "x", "evidence": "y"}
    assert artifact["instruments"][0]["symbol"] == "^SPX"
    assert sorted(artifact["citations"]) == [_A, _B]
    assert artifact["citations"][_A]["summary"].startswith("The index rose")
    assert (
        vq.validate_artifact(
            artifact, evidence=make_evidence(), analysis=make_analysis()
        )
        == []
    )


def test_assemble_artifact_drops_fabricated_citations() -> None:
    output = make_output()
    output["instruments"][0]["drivers"][0]["citations"] = ["f" * 16]
    artifact = _assemble(output)
    assert artifact["instruments"][0]["drivers"][0]["citations"] == []


def test_assemble_artifact_drops_unknown_instrument(
    capsys: pytest.CaptureFixture[str],
) -> None:
    output = make_output()
    output["instruments"].append({
        "canonical_id": "ghost",
        "stance": "neutral",
        "confidence": "low",
        "drivers": [{"text": "x", "citations": []}],
    })
    artifact = _assemble(output)
    assert [i["canonical_id"] for i in artifact["instruments"]] == ["spx"]
    assert "unknown instrument" in capsys.readouterr().out


def test_assemble_artifact_dedupes_and_sorts_instruments() -> None:
    output = make_output()
    dji_entry = {
        "canonical_id": "dji",
        "stance": "neutral",
        "confidence": "low",
        "drivers": [{"text": "x", "citations": [_B]}],
    }
    output["instruments"] = [
        dict(output["instruments"][0]),
        dji_entry,
        dict(output["instruments"][0]),
    ]
    artifact = _assemble(output)
    assert [i["canonical_id"] for i in artifact["instruments"]] == ["dji", "spx"]


def test_assemble_artifact_malformed_shapes() -> None:
    artifact = _assemble({
        "market_narrative": "bad",
        "themes": "bad",
        "instruments": "bad",
    })
    assert artifact["market_narrative"]["text"] == ""
    assert artifact["themes"] == []
    assert artifact["instruments"] == []
    assert artifact["citations"] == {}


def test_assemble_artifact_skips_non_dict_entries() -> None:
    output = make_output()
    output["themes"] = ["bad", output["themes"][0]]
    output["instruments"] = [
        "bad",
        {"canonical_id": 7},
        output["instruments"][0],
    ]
    artifact = _assemble(output)
    assert len(artifact["themes"]) == 1
    assert len(artifact["instruments"]) == 1


def test_assemble_artifact_caps_lists() -> None:
    output = make_output()
    output["themes"] = [output["themes"][0]] * 9
    output["instruments"][0]["drivers"] = [
        {"text": f"driver {i}", "citations": [_A]} for i in range(6)
    ]
    output["instruments"][0]["drivers"].append("bad")
    artifact = _assemble(output)
    assert len(artifact["themes"]) == 5
    assert len(artifact["instruments"][0]["drivers"]) == 3


# ── generate ────────────────────────────────────────────────────────────────────


def test_generate_success(mocker: MockerFixture) -> None:
    mocker.patch.object(q, "call_model", return_value=make_output())
    artifact = q.generate(
        analysis=make_analysis(),
        evidence=make_evidence(),
        events=[],
        api_key="key",
    )
    assert artifact["metadata"]["prompt_version"] == q.PROMPT_VERSION
    assert artifact["metadata"]["gates"] == {
        "gated_instruments": [],
        "narrative_gates": [],
    }
    hashes = artifact["metadata"]["input_hashes"]
    assert hashes["analysis"] == q.content_hash(make_analysis())
    assert hashes["evidence"] == q.content_hash(make_evidence())


def test_generate_retries_then_succeeds(
    mocker: MockerFixture, capsys: pytest.CaptureFixture[str]
) -> None:
    bad = {
        "market_narrative": {"text": "", "citations": []},
        "themes": [],
        "instruments": [],
    }
    mocker.patch.object(q, "call_model", side_effect=[bad, make_output()])
    artifact = q.generate(
        analysis=make_analysis(),
        evidence=make_evidence(),
        events=[],
        api_key="key",
    )
    assert artifact["instruments"]
    out = capsys.readouterr().out
    assert "contract violation" in out
    assert "retrying model call" in out


def test_generate_exhausts_retries(mocker: MockerFixture) -> None:
    bad = {
        "market_narrative": {"text": "", "citations": []},
        "themes": [],
        "instruments": [],
    }
    mocker.patch.object(q, "call_model", return_value=bad)
    with pytest.raises(q.QualitativeGenerationError, match="failed contract"):
        q.generate(
            analysis=make_analysis(),
            evidence=make_evidence(),
            events=[],
            api_key="key",
            max_retries=1,
        )


# ── main ────────────────────────────────────────────────────────────────────────


def _write_inputs(tmp_path: Path) -> tuple[Path, Path]:
    analysis_path = tmp_path / "analysis.json"
    analysis_path.write_text(json.dumps(make_analysis()))
    evidence_path = tmp_path / "evidence.json"
    evidence_path.write_text(json.dumps(make_evidence()))
    return analysis_path, evidence_path


def _calendar_dir(tmp_path: Path) -> Path:
    calendar_dir = tmp_path / "calendars"
    calendar_dir.mkdir()
    (calendar_dir / "macro.json").write_text(
        json.dumps({
            "version": "1.0.0",
            "metadata": {
                "generated_at": "2024-01-01T00:00:00+00:00",
                "source": "curated",
            },
            "events": [
                {
                    "date": "2024-01-03",
                    "name": "FOMC rate decision",
                    "category": "macro",
                    "canonical_ids": [],
                    "asset_classes": ["equity_index"],
                    "source_url": "https://example.gov",
                }
            ],
        })
    )
    return calendar_dir


def test_main_requires_api_key(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    analysis_path, evidence_path = _write_inputs(tmp_path)
    result = q.main([
        "--analysis",
        str(analysis_path),
        "--evidence",
        str(evidence_path),
    ])
    assert result == 1


def test_main_success(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, mocker: MockerFixture
) -> None:
    monkeypatch.setenv("ANTHROPIC_API_KEY", "key")
    analysis_path, evidence_path = _write_inputs(tmp_path)
    calendar_dir = _calendar_dir(tmp_path)
    mocker.patch.object(q, "call_model", return_value=make_output())
    output_dir = tmp_path / "qualitative"
    result = q.main([
        "--analysis",
        str(analysis_path),
        "--evidence",
        str(evidence_path),
        "--calendar-dir",
        str(calendar_dir),
        "--output",
        str(output_dir),
    ])
    assert result == 0
    written = json.loads((output_dir / "2024-01-01.json").read_text())
    assert written["metadata"]["analysis_date"] == "2024-01-01"


def test_main_skips_missing_calendar_dir(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, mocker: MockerFixture
) -> None:
    monkeypatch.setenv("ANTHROPIC_API_KEY", "key")
    analysis_path, evidence_path = _write_inputs(tmp_path)
    mocker.patch.object(q, "call_model", return_value=make_output())
    result = q.main([
        "--analysis",
        str(analysis_path),
        "--evidence",
        str(evidence_path),
        "--calendar-dir",
        str(tmp_path / "missing"),
        "--output",
        str(tmp_path / "out"),
    ])
    assert result == 0


def test_main_warns_on_invalid_calendar(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    mocker: MockerFixture,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setenv("ANTHROPIC_API_KEY", "key")
    analysis_path, evidence_path = _write_inputs(tmp_path)
    calendar_dir = tmp_path / "calendars"
    calendar_dir.mkdir()
    (calendar_dir / "bad.json").write_text(json.dumps({"version": "1.0.0"}))
    mocker.patch.object(q, "call_model", return_value=make_output())
    result = q.main([
        "--analysis",
        str(analysis_path),
        "--evidence",
        str(evidence_path),
        "--calendar-dir",
        str(calendar_dir),
        "--output",
        str(tmp_path / "out"),
    ])
    assert result == 0
    assert "skipping calendars" in capsys.readouterr().out


def test_main_missing_input(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.setenv("ANTHROPIC_API_KEY", "key")
    result = q.main([
        "--analysis",
        str(tmp_path / "nope.json"),
        "--evidence",
        str(tmp_path / "nope2.json"),
    ])
    assert result == 1


def test_main_bad_json(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.setenv("ANTHROPIC_API_KEY", "key")
    analysis_path = tmp_path / "analysis.json"
    analysis_path.write_text("{{{")
    evidence_path = tmp_path / "evidence.json"
    evidence_path.write_text("{}")
    result = q.main([
        "--analysis",
        str(analysis_path),
        "--evidence",
        str(evidence_path),
    ])
    assert result == 1


def test_main_generation_error(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, mocker: MockerFixture
) -> None:
    monkeypatch.setenv("ANTHROPIC_API_KEY", "key")
    analysis_path, evidence_path = _write_inputs(tmp_path)
    mocker.patch.object(q, "generate", side_effect=q.QualitativeGenerationError("bad"))
    result = q.main([
        "--analysis",
        str(analysis_path),
        "--evidence",
        str(evidence_path),
        "--calendar-dir",
        str(tmp_path / "missing"),
    ])
    assert result == 1


def test_main_transport_error(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, mocker: MockerFixture
) -> None:
    monkeypatch.setenv("ANTHROPIC_API_KEY", "key")
    analysis_path, evidence_path = _write_inputs(tmp_path)
    mocker.patch.object(q, "generate", side_effect=urllib.error.URLError("down"))
    result = q.main([
        "--analysis",
        str(analysis_path),
        "--evidence",
        str(evidence_path),
        "--calendar-dir",
        str(tmp_path / "missing"),
    ])
    assert result == 1
