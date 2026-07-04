"""Tests for aims.validate_qualitative — schema, enums, and grounding rules."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from typing import Any

import pytest

from aims import validate_qualitative as vq

FIXTURES = Path(__file__).resolve().parent / "fixtures"
QUALITATIVE = FIXTURES / "qualitative_2024-01-01.json"
ANALYSIS = FIXTURES / "analysis_2024-01-01_mapped.json"
EVIDENCE = FIXTURES / "evidence_2024-01-01.json"


def _load(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as fh:
        value: dict[str, Any] = json.load(fh)
    return value


@pytest.fixture
def artifact() -> dict[str, Any]:
    return _load(QUALITATIVE)


@pytest.fixture
def analysis() -> dict[str, Any]:
    return _load(ANALYSIS)


@pytest.fixture
def evidence() -> dict[str, Any]:
    return _load(EVIDENCE)


def _evidence_id(evidence: dict[str, Any], idx: int = 0) -> str:
    return str(evidence["items"][idx]["id"])


# ── fixture sanity ───────────────────────────────────────────────────────────


def test_fixture_valid_without_cross_checks(artifact: dict[str, Any]) -> None:
    assert vq.validate_artifact(artifact) == []


def test_fixture_valid_with_cross_checks(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    assert vq.validate_artifact(artifact, analysis=analysis, evidence=evidence) == []


# ── top-level shape ──────────────────────────────────────────────────────────


def test_missing_top_keys() -> None:
    errors = vq.validate_artifact({})
    assert any("version" in e for e in errors)
    assert any("metadata" in e for e in errors)
    assert any("market" in e for e in errors)
    assert any("instruments" in e for e in errors)


def test_wrong_version(artifact: dict[str, Any]) -> None:
    artifact["version"] = "9.9.9"
    assert any("unsupported version" in e for e in vq.validate_artifact(artifact))


def test_metadata_not_object(artifact: dict[str, Any]) -> None:
    artifact["metadata"] = "nope"
    assert any("metadata" in e for e in vq.validate_artifact(artifact))


def test_metadata_missing_keys(artifact: dict[str, Any]) -> None:
    del artifact["metadata"]["model_id"]
    assert any("model_id" in e for e in vq.validate_artifact(artifact))


def test_input_hashes_missing_keys(artifact: dict[str, Any]) -> None:
    del artifact["metadata"]["input_hashes"]["evidence_sha256"]
    assert any(
        "input_hashes missing required key: 'evidence_sha256'" in e
        for e in vq.validate_artifact(artifact)
    )


def test_metadata_missing_input_hashes_entirely(artifact: dict[str, Any]) -> None:
    del artifact["metadata"]["input_hashes"]
    errors = vq.validate_artifact(artifact)
    assert any("missing required key: 'input_hashes'" in e for e in errors)
    assert not any("input_hashes must be a JSON object" in e for e in errors)


def test_input_hashes_not_object(artifact: dict[str, Any]) -> None:
    artifact["metadata"]["input_hashes"] = "nope"
    assert any(
        "input_hashes must be a JSON object" in e
        for e in vq.validate_artifact(artifact)
    )


def test_input_hashes_bad_format(artifact: dict[str, Any]) -> None:
    artifact["metadata"]["input_hashes"]["analysis_sha256"] = "not-hex"
    assert any("not a SHA-256 hex digest" in e for e in vq.validate_artifact(artifact))


def test_prompt_sha256_bad_format(artifact: dict[str, Any]) -> None:
    artifact["metadata"]["prompt_sha256"] = "short"
    assert any(
        "prompt_sha256" in e and "not a SHA-256 hex digest" in e
        for e in vq.validate_artifact(artifact)
    )


def test_analysis_date_mismatch(
    artifact: dict[str, Any], analysis: dict[str, Any]
) -> None:
    artifact["metadata"]["analysis_date"] = "2024-02-02"
    errors = vq.validate_artifact(artifact, analysis=analysis)
    assert any("does not match the analysis artifact date" in e for e in errors)


# ── market ───────────────────────────────────────────────────────────────────


def test_market_not_object(artifact: dict[str, Any]) -> None:
    artifact["market"] = "nope"
    assert vq.validate_artifact(artifact) == ["'market' must be a JSON object"]


def test_market_missing_keys(artifact: dict[str, Any]) -> None:
    del artifact["market"]["themes"]
    assert any(
        "market missing required key: 'themes'" in e
        for e in vq.validate_artifact(artifact)
    )


def test_market_narrative_empty(artifact: dict[str, Any]) -> None:
    artifact["market"]["narrative"] = "   "
    assert any(
        "narrative must be a non-empty string" in e
        for e in vq.validate_artifact(artifact)
    )


def test_market_narrative_too_long(artifact: dict[str, Any]) -> None:
    artifact["market"]["narrative"] = "x" * (vq.NARRATIVE_MAX_CHARS + 1)
    assert any("narrative exceeds" in e for e in vq.validate_artifact(artifact))


def test_market_citations_empty(artifact: dict[str, Any]) -> None:
    artifact["market"]["citations"] = []
    assert any(
        "citations must be a non-empty list" in e
        for e in vq.validate_artifact(artifact)
    )


def test_market_citation_not_in_bundle(
    artifact: dict[str, Any], evidence: dict[str, Any]
) -> None:
    artifact["market"]["citations"] = ["ev-deadbeefdeadbeef"]
    errors = vq.validate_artifact(artifact, evidence=evidence)
    assert any("is not in the evidence bundle" in e for e in errors)


def test_market_numeric_claims_invalid_entries(artifact: dict[str, Any]) -> None:
    artifact["market"]["numeric_claims"] = [
        {"value": "not-a-number", "unit": "percent", "refers_to": "x"},
        {"value": 1, "unit": "bogus", "refers_to": "x"},
        {"value": 1, "unit": "percent", "refers_to": ""},
    ]
    errors = vq.validate_artifact(artifact)
    assert any("'value' must be a number" in e for e in errors)
    assert any("unit" in e and "is not valid" in e for e in errors)
    assert any("'refers_to' must be a non-empty string" in e for e in errors)


def test_market_numeric_claims_non_dict_entry(artifact: dict[str, Any]) -> None:
    artifact["market"]["numeric_claims"] = ["not-a-dict"]
    errors = vq.validate_artifact(artifact)
    assert any("numeric_claims[0] must be a JSON object" in e for e in errors)


def test_market_numeric_claims_not_list(artifact: dict[str, Any]) -> None:
    artifact["market"]["numeric_claims"] = "nope"
    assert any(
        "numeric_claims must be a JSON array" in e
        for e in vq.validate_artifact(artifact)
    )


def test_market_free_text_undeclared_number(artifact: dict[str, Any]) -> None:
    artifact["market"]["narrative"] += " Sales grew 42 percent."
    errors = vq.validate_artifact(artifact)
    assert any("numeric token '42'" in e for e in errors)


def test_themes_not_list(artifact: dict[str, Any]) -> None:
    artifact["market"]["themes"] = "nope"
    assert "market.themes must be a JSON array" in vq.validate_artifact(artifact)


def test_themes_too_many(artifact: dict[str, Any], evidence: dict[str, Any]) -> None:
    cid = _evidence_id(evidence)
    artifact["market"]["themes"] = [
        {"title": f"Theme {i}", "citations": [cid]} for i in range(vq.MAX_THEMES + 1)
    ]
    assert any("more than" in e for e in vq.validate_artifact(artifact))


def test_theme_not_object(artifact: dict[str, Any]) -> None:
    artifact["market"]["themes"] = ["nope"]
    assert "market.themes[0] must be a JSON object" in vq.validate_artifact(artifact)


def test_theme_title_empty_and_too_long(
    artifact: dict[str, Any], evidence: dict[str, Any]
) -> None:
    cid = _evidence_id(evidence)
    artifact["market"]["themes"] = [
        {"title": "", "citations": [cid]},
        {"title": "x" * (vq.THEME_TITLE_MAX_CHARS + 1), "citations": [cid]},
    ]
    errors = vq.validate_artifact(artifact)
    assert any("title' must be a non-empty string" in e for e in errors)
    assert any("title exceeds" in e for e in errors)


def test_theme_numeric_claims_validated(
    artifact: dict[str, Any], evidence: dict[str, Any]
) -> None:
    cid = _evidence_id(evidence)
    artifact["market"]["themes"] = [
        {
            "title": "Rates steady",
            "citations": [cid],
            "numeric_claims": [{"value": "bad", "unit": "percent", "refers_to": "x"}],
        }
    ]
    assert any("'value' must be a number" in e for e in vq.validate_artifact(artifact))


# ── instruments ──────────────────────────────────────────────────────────────


def test_instruments_not_list(artifact: dict[str, Any]) -> None:
    artifact["instruments"] = "nope"
    assert "'instruments' must be a JSON array" in vq.validate_artifact(artifact)


def test_instruments_more_than_top_k(
    artifact: dict[str, Any], evidence: dict[str, Any]
) -> None:
    cid = _evidence_id(evidence)
    extra = copy.deepcopy(artifact["instruments"][0])
    for i in range(vq.DEFAULT_TOP_K):
        entry = copy.deepcopy(extra)
        entry["canonical_id"] = f"extra{i}"
        entry["drivers"][0]["citations"] = [cid]
        artifact["instruments"].append(entry)
    assert any(
        f"more than top-K={vq.DEFAULT_TOP_K}" in e
        for e in vq.validate_artifact(artifact)
    )


def test_instrument_not_object(artifact: dict[str, Any]) -> None:
    artifact["instruments"] = ["nope"]
    assert "instruments[0] must be a JSON object" in vq.validate_artifact(artifact)


def test_instrument_missing_keys(artifact: dict[str, Any]) -> None:
    del artifact["instruments"][0]["stance"]
    assert any(
        "missing required key: 'stance'" in e for e in vq.validate_artifact(artifact)
    )


def test_duplicate_canonical_id(artifact: dict[str, Any]) -> None:
    artifact["instruments"].append(copy.deepcopy(artifact["instruments"][0]))
    assert any("duplicate canonical_id" in e for e in vq.validate_artifact(artifact))


def test_instrument_not_in_top_k(
    artifact: dict[str, Any], analysis: dict[str, Any]
) -> None:
    artifact["instruments"][0]["canonical_id"] = "ndx"
    errors = vq.validate_artifact(artifact, analysis=analysis)
    assert any("is not a top-5 reliable signal" in e for e in errors)


def test_instrument_symbol_mismatch(
    artifact: dict[str, Any], analysis: dict[str, Any]
) -> None:
    artifact["instruments"][0]["symbol"] = "^WRONG"
    errors = vq.validate_artifact(artifact, analysis=analysis)
    assert any("does not match the analysis symbol" in e for e in errors)


def test_instrument_bad_stance_and_confidence(artifact: dict[str, Any]) -> None:
    artifact["instruments"][0]["stance"] = "bullish"
    artifact["instruments"][0]["confidence"] = "certain"
    errors = vq.validate_artifact(artifact)
    assert any("stance" in e and "is not valid" in e for e in errors)
    assert any("confidence" in e and "is not valid" in e for e in errors)


def test_instrument_drivers_not_list_or_empty(artifact: dict[str, Any]) -> None:
    artifact["instruments"][0]["drivers"] = []
    assert any(
        "drivers must be a non-empty JSON array" in e
        for e in vq.validate_artifact(artifact)
    )


def test_instrument_too_many_drivers(
    artifact: dict[str, Any], evidence: dict[str, Any]
) -> None:
    cid = _evidence_id(evidence)
    driver = {"text": "Filler.", "citations": [cid]}
    artifact["instruments"][0]["drivers"] = [
        driver for _ in range(vq.MAX_DRIVERS_PER_INSTRUMENT + 1)
    ]
    assert any("more than" in e for e in vq.validate_artifact(artifact))


# ── drivers ──────────────────────────────────────────────────────────────────


def test_driver_not_object(artifact: dict[str, Any]) -> None:
    artifact["instruments"][0]["drivers"] = ["nope"]
    errors = vq.validate_artifact(artifact)
    assert any("must be a JSON object" in e for e in errors)


def test_driver_missing_text_and_citations(artifact: dict[str, Any]) -> None:
    artifact["instruments"][0]["drivers"][0] = {}
    errors = vq.validate_artifact(artifact)
    assert any("'text' must be a non-empty string" in e for e in errors)
    assert any("citations must be a non-empty list" in e for e in errors)


def test_driver_text_empty_and_too_long(
    artifact: dict[str, Any], evidence: dict[str, Any]
) -> None:
    cid = _evidence_id(evidence)
    artifact["instruments"][0]["drivers"][0]["text"] = "   "
    errors = vq.validate_artifact(artifact)
    assert any("'text' must be a non-empty string" in e for e in errors)
    artifact["instruments"][0]["drivers"][0]["text"] = "x" * (
        vq.DRIVER_TEXT_MAX_CHARS + 1
    )
    artifact["instruments"][0]["drivers"][0]["citations"] = [cid]
    errors = vq.validate_artifact(artifact)
    assert any("text exceeds" in e for e in errors)


def test_driver_too_many_citations(
    artifact: dict[str, Any], evidence: dict[str, Any]
) -> None:
    cid = _evidence_id(evidence)
    artifact["instruments"][0]["drivers"][0]["citations"] = [cid] * (
        vq.MAX_CITATIONS_PER_DRIVER + 1
    )
    assert any("more than" in e for e in vq.validate_artifact(artifact))


def test_driver_citation_not_in_bundle(
    artifact: dict[str, Any], evidence: dict[str, Any]
) -> None:
    artifact["instruments"][0]["drivers"][0]["citations"] = ["ev-0000000000000000"]
    errors = vq.validate_artifact(artifact, evidence=evidence)
    assert any("is not in the evidence bundle" in e for e in errors)


def test_direction_claim_invalid(artifact: dict[str, Any]) -> None:
    artifact["instruments"][0]["drivers"][0]["direction_claim"] = {
        "direction": "sideways",
        "window": "3d",
    }
    errors = vq.validate_artifact(artifact)
    assert any("direction" in e and "up/down/none" in e for e in errors)
    assert any("window" in e and "is not valid" in e for e in errors)


def test_direction_claim_not_object(artifact: dict[str, Any]) -> None:
    artifact["instruments"][0]["drivers"][0]["direction_claim"] = "up"
    errors = vq.validate_artifact(artifact)
    assert any("direction_claim must be a JSON object" in e for e in errors)


def test_driver_numeric_claims_validated(artifact: dict[str, Any]) -> None:
    artifact["instruments"][0]["drivers"][0]["numeric_claims"] = [
        {"value": None, "unit": "percent", "refers_to": "ret_20d"}
    ]
    errors = vq.validate_artifact(artifact)
    assert any("'value' must be a number" in e for e in errors)


def test_driver_free_text_undeclared_number(artifact: dict[str, Any]) -> None:
    artifact["instruments"][0]["drivers"][0]["text"] += " up 17 points"
    errors = vq.validate_artifact(artifact)
    assert any("numeric token '17'" in e for e in errors)


# ── free-text whitelist ──────────────────────────────────────────────────────


@pytest.mark.parametrize(
    "text",
    [
        "As of 2024-01-01 the trend held.",
        "Over the past 20-day window momentum improved.",
        "RSI14 stayed elevated and MA20 support held.",
        "Q1 guidance was reaffirmed.",
        "The 2024 outlook is stable.",
        "ret_20d and ma50_dist both improved.",
    ],
)
def test_undeclared_numbers_whitelist(text: str) -> None:
    assert vq.undeclared_numbers(text, []) == []


def test_undeclared_numbers_flags_bare_number() -> None:
    assert vq.undeclared_numbers("Revenue rose 12.5 percent.", []) == ["12.5"]


def test_undeclared_numbers_matches_declared_value_within_tolerance() -> None:
    claims = [{"value": 12.5, "unit": "percent", "refers_to": "ret_20d"}]
    assert vq.undeclared_numbers("Revenue rose 12.5 percent.", claims) == []


def test_undeclared_numbers_ignores_non_numeric_claims() -> None:
    claims = ["not-a-dict", {"value": "nan", "unit": "percent", "refers_to": "x"}]
    assert vq.undeclared_numbers("It moved 3 points.", claims) == ["3"]


def test_undeclared_numbers_whitelisted_number_is_exempt() -> None:
    assert vq.undeclared_numbers("The S&P 500 led gains.", [], frozenset({"500"})) == []


def test_undeclared_numbers_whitelist_does_not_mask_other_numbers() -> None:
    tokens = vq.undeclared_numbers(
        "The S&P 500 rose 12.5 percent.", [], frozenset({"500"})
    )
    assert tokens == ["12.5"]


# ── instrument_name_numbers ──────────────────────────────────────────────────


def test_instrument_name_numbers_none_analysis() -> None:
    assert vq.instrument_name_numbers(None) == frozenset()


def test_instrument_name_numbers_extracts_digits_from_display_names() -> None:
    analysis = {
        "instruments": [
            {"display_name": "S&P 500"},
            {"display_name": "NASDAQ 100"},
            {"display_name": "Dow Jones Industrial Average"},
            {"display_name": None},
            {},
        ]
    }
    assert vq.instrument_name_numbers(analysis) == frozenset({"500", "100"})


def test_market_narrative_mentions_instrument_name_with_analysis(
    artifact: dict[str, Any], analysis: dict[str, Any]
) -> None:
    # Regression test for a Codex finding: a covered instrument's own name
    # ("S&P 500", the analysis fixture's spx display_name) must not be
    # rejected as an undeclared numeric claim when the analysis artifact is
    # supplied for cross-checking.
    artifact["market"]["narrative"] += " The S&P 500 led the rally."
    errors = vq.validate_artifact(artifact, analysis=analysis)
    assert not any("numeric token '500'" in e for e in errors)


def test_market_narrative_instrument_name_number_still_flagged_without_analysis(
    artifact: dict[str, Any],
) -> None:
    artifact["market"]["narrative"] += " The S&P 500 led the rally."
    errors = vq.validate_artifact(artifact)
    assert any("numeric token '500'" in e for e in errors)


# ── sha256_file ──────────────────────────────────────────────────────────────


def test_sha256_file_matches_hashlib(tmp_path: Path) -> None:
    path = tmp_path / "f.txt"
    path.write_bytes(b"hello world")
    assert vq.sha256_file(path) == hashlib.sha256(b"hello world").hexdigest()


# ── CLI ─────────────────────────────────────────────────────────────────────


def test_main_ok(capsys: pytest.CaptureFixture[str]) -> None:
    rc = vq.main([
        "--input",
        str(QUALITATIVE),
        "--analysis",
        str(ANALYSIS),
        "--evidence",
        str(EVIDENCE),
    ])
    assert rc == 0
    assert "OK" in capsys.readouterr().out


def test_main_ok_without_cross_checks() -> None:
    rc = vq.main(["--input", str(QUALITATIVE)])
    assert rc == 0


def test_main_missing_file(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    rc = vq.main(["--input", str(tmp_path / "missing.json")])
    assert rc == 1
    assert "file not found" in capsys.readouterr().out


def test_main_invalid_json(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    path = tmp_path / "bad.json"
    path.write_text("{not json", encoding="utf-8")
    rc = vq.main(["--input", str(path)])
    assert rc == 1
    assert "invalid JSON" in capsys.readouterr().out


def test_main_validation_failure(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    path = tmp_path / "bad.json"
    path.write_text("{}", encoding="utf-8")
    rc = vq.main(["--input", str(path)])
    assert rc == 1
    assert "missing required key" in capsys.readouterr().out


def test_main_hash_mismatch_detected(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    tampered_analysis = tmp_path / "analysis.json"
    tampered_analysis.write_text(
        json.dumps({**_load(ANALYSIS), "extra": "field"}), encoding="utf-8"
    )
    rc = vq.main([
        "--input",
        str(QUALITATIVE),
        "--analysis",
        str(tampered_analysis),
        "--evidence",
        str(EVIDENCE),
    ])
    out = capsys.readouterr().out
    assert rc == 1
    assert "analysis_sha256 does not match" in out


def test_main_evidence_hash_mismatch_detected(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    tampered_evidence = tmp_path / "evidence.json"
    tampered_evidence.write_text(
        json.dumps({**_load(EVIDENCE), "extra": "field"}), encoding="utf-8"
    )
    rc = vq.main([
        "--input",
        str(QUALITATIVE),
        "--evidence",
        str(tampered_evidence),
    ])
    out = capsys.readouterr().out
    assert rc == 1
    assert "evidence_sha256 does not match" in out
