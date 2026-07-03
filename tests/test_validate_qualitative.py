from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

import aims.validate_qualitative as vq

if TYPE_CHECKING:
    import pytest

_A = "a" * 16
_B = "b" * 16
_C = "c" * 16


def make_analysis() -> dict[str, Any]:
    return {
        "version": "1.0.0",
        "metadata": {
            "generated_at": "2024-01-01T01:00:00+00:00",
            "config": {"interval": "d"},
        },
        "instruments": [
            {
                "canonical_id": "spx",
                "symbol": "^SPX",
                "display_name": "S&P 500",
                "asset_class": "equity_index",
                "rank": 1,
                "score": 72.5,
                "is_reliable": True,
                "risk_gates": [],
                "features": {
                    "ret_1d": 0.012,
                    "ret_5d": 0.031,
                    "ret_20d": 0.053,
                    "ret_60d": 0.089,
                    "ma20_dist": 0.021,
                    "ma50_dist": 0.018,
                    "vol_20d": 0.127,
                    "mdd_60d": 0.031,
                    "rsi_14": 62.0,
                    "zscore_20d": 1.2,
                },
            },
            {
                "canonical_id": "dji",
                "symbol": "^DJI",
                "display_name": "Dow Jones Industrial Average",
                "asset_class": "equity_index",
                "rank": 2,
                "score": 41.0,
                "is_reliable": True,
                "risk_gates": [],
                "features": {
                    "ret_1d": -0.002,
                    "ret_5d": -0.015,
                    "ret_20d": -0.021,
                    "ret_60d": 0.010,
                    "ma20_dist": -0.008,
                    "ma50_dist": 0.002,
                    "vol_20d": 0.09,
                    "mdd_60d": 0.04,
                    "rsi_14": 44.0,
                    "zscore_20d": -0.5,
                },
            },
            {"symbol": "^NDX", "rank": 3, "score": 30.0, "is_reliable": False},
        ],
    }


def make_evidence() -> dict[str, Any]:
    return {
        "version": "1.0.0",
        "metadata": {
            "generated_at": "2024-01-01T09:00:00+00:00",
            "analysis_date": "2024-01-01",
            "max_age_days": 7,
            "coverage": {"sources": {}, "item_count": 3},
        },
        "items": [
            {
                "id": _A,
                "source": "yfinance:^SPX",
                "category": "instrument_news",
                "title": "S&P 500 posts weekly gain of 3.1%",
                "url": "https://news.example/spx",
                "published_at": "2023-12-31T12:00:00+00:00",
                "retrieved_at": "2024-01-01T09:00:00+00:00",
                "instruments": ["spx"],
                "summary": "The index rose 3.1% over five sessions.",
            },
            {
                "id": _B,
                "source": "feed:federal_reserve_press",
                "category": "macro",
                "title": "Federal Reserve holds policy rate",
                "url": "https://example.gov/press/1",
                "published_at": "2024-01-01T08:00:00+00:00",
                "retrieved_at": "2024-01-01T09:00:00+00:00",
                "instruments": [],
                "summary": "The committee held the target range unchanged.",
            },
            {
                "id": _C,
                "source": "yfinance:^DJI",
                "category": "instrument_news",
                "title": "Dow outlook piece",
                "url": "https://news.example/dji",
                "published_at": "2023-11-01T12:00:00+00:00",
                "retrieved_at": "2024-01-01T09:00:00+00:00",
                "instruments": ["dji"],
                "summary": "An older feature story.",
            },
        ],
    }


def _citation_entry(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "title": item["title"],
        "url": item["url"],
        "source": item["source"],
        "published_at": item["published_at"],
        "summary": item["summary"],
    }


def make_artifact(**overrides: Any) -> dict[str, Any]:
    evidence = make_evidence()
    items = {item["id"]: item for item in evidence["items"]}
    artifact: dict[str, Any] = {
        "version": "1.0.0",
        "metadata": {
            "generated_at": "2024-01-01T02:00:00+00:00",
            "analysis_date": "2024-01-01",
            "model": "claude-test",
            "prompt_version": "1.0.0",
            "input_hashes": {"analysis": "x", "evidence": "y"},
            "gates": {"gated_instruments": [], "narrative_gates": []},
        },
        "market_narrative": {
            "text": "Large caps gained 3.1% into year-end while the Fed held.",
            "citations": [_A, _B],
            "gates": [],
        },
        "themes": [
            {
                "title": "Rate pause",
                "text": "The Fed held rates, supporting risk assets.",
                "citations": [_B],
                "gates": [],
            }
        ],
        "instruments": [
            {
                "canonical_id": "spx",
                "symbol": "^SPX",
                "stance": "supportive",
                "confidence": "high",
                "drivers": [
                    {
                        "text": "A weekly gain of 3.1% aligns with the signal.",
                        "citations": [_A],
                    }
                ],
                "gates": [],
            }
        ],
        "citations": {cid: _citation_entry(items[cid]) for cid in (_A, _B)},
    }
    artifact.update(overrides)
    return artifact


# ── validate_artifact: structural ──────────────────────────────────────────────


def test_validate_artifact_valid() -> None:
    errors = vq.validate_artifact(
        make_artifact(), evidence=make_evidence(), analysis=make_analysis()
    )
    assert errors == []


def test_validate_artifact_valid_without_context() -> None:
    assert vq.validate_artifact(make_artifact()) == []


def test_validate_artifact_missing_top_key() -> None:
    errors = vq.validate_artifact({"version": "1.0.0"})
    assert any("citations" in e for e in errors)


def test_validate_artifact_wrong_version() -> None:
    errors = vq.validate_artifact(make_artifact(version="9.9.9"))
    assert any("unsupported version" in e for e in errors)


def test_validate_artifact_metadata_not_dict() -> None:
    errors = vq.validate_artifact(make_artifact(metadata="bad"))
    assert any("'metadata'" in e for e in errors)


def test_validate_artifact_metadata_missing_key() -> None:
    artifact = make_artifact()
    del artifact["metadata"]["model"]
    errors = vq.validate_artifact(artifact)
    assert any("'model'" in e for e in errors)


def test_validate_artifact_metadata_gates_not_dict() -> None:
    artifact = make_artifact()
    artifact["metadata"]["gates"] = []
    errors = vq.validate_artifact(artifact)
    assert any("metadata.gates" in e for e in errors)


def test_validate_artifact_citations_not_dict() -> None:
    errors = vq.validate_artifact(make_artifact(citations=[]))
    assert any("'citations'" in e for e in errors)


def test_validate_artifact_citation_entry_not_dict() -> None:
    artifact = make_artifact()
    artifact["citations"][_A] = "bad"
    errors = vq.validate_artifact(artifact)
    assert any("must be a JSON object" in e for e in errors)


def test_validate_artifact_citation_entry_missing_key() -> None:
    artifact = make_artifact()
    del artifact["citations"][_A]["url"]
    errors = vq.validate_artifact(artifact)
    assert any("'url'" in e for e in errors)


def test_validate_artifact_citation_not_in_evidence() -> None:
    artifact = make_artifact()
    artifact["citations"]["d" * 16] = artifact["citations"][_A]
    errors = vq.validate_artifact(artifact, evidence=make_evidence())
    assert any("not present in the evidence bundle" in e for e in errors)


def test_validate_artifact_narrative_not_dict() -> None:
    errors = vq.validate_artifact(make_artifact(market_narrative="bad"))
    assert any("'market_narrative'" in e for e in errors)


def test_validate_artifact_narrative_text_bad() -> None:
    artifact = make_artifact()
    artifact["market_narrative"]["text"] = ""
    errors = vq.validate_artifact(artifact)
    assert any("non-empty string" in e for e in errors)
    artifact["market_narrative"]["text"] = "x" * 1201
    errors = vq.validate_artifact(artifact)
    assert any("exceeds 1200" in e for e in errors)


def test_validate_artifact_citation_block_errors() -> None:
    artifact = make_artifact()
    artifact["market_narrative"]["citations"] = "bad"
    errors = vq.validate_artifact(artifact)
    assert any("array of strings" in e for e in errors)
    artifact = make_artifact()
    artifact["market_narrative"]["citations"] = [1]
    errors = vq.validate_artifact(artifact)
    assert any("array of strings" in e for e in errors)
    artifact = make_artifact()
    artifact["market_narrative"]["citations"] = [_A] * 9
    errors = vq.validate_artifact(artifact)
    assert any("more than 8 citations" in e for e in errors)
    artifact = make_artifact()
    artifact["market_narrative"]["citations"] = ["f" * 16]
    errors = vq.validate_artifact(artifact)
    assert any("not present in the citations map" in e for e in errors)


def test_validate_artifact_themes_errors() -> None:
    errors = vq.validate_artifact(make_artifact(themes="bad"))
    assert any("'themes'" in e for e in errors)
    theme = make_artifact()["themes"][0]
    errors = vq.validate_artifact(make_artifact(themes=[theme] * 6))
    assert any("more than 5 themes" in e for e in errors)
    errors = vq.validate_artifact(make_artifact(themes=["bad"]))
    assert any("theme[0] must be" in e for e in errors)
    bad_theme = dict(theme, title="x" * 81)
    errors = vq.validate_artifact(make_artifact(themes=[bad_theme]))
    assert any("title exceeds 80" in e for e in errors)


# ── validate_artifact: instruments ─────────────────────────────────────────────


def _artifact_with_instrument(**overrides: Any) -> dict[str, Any]:
    artifact = make_artifact()
    artifact["instruments"][0].update(overrides)
    return artifact


def test_validate_artifact_instruments_not_list() -> None:
    errors = vq.validate_artifact(make_artifact(instruments="bad"))
    assert any("'instruments'" in e for e in errors)


def test_validate_artifact_instrument_not_dict() -> None:
    errors = vq.validate_artifact(make_artifact(instruments=["bad"]))
    assert any("instrument[0] must be" in e for e in errors)


def test_validate_artifact_instrument_missing_key() -> None:
    artifact = make_artifact()
    del artifact["instruments"][0]["stance"]
    errors = vq.validate_artifact(artifact)
    assert any("missing required key: 'stance'" in e for e in errors)


def test_validate_artifact_bad_stance_and_confidence() -> None:
    errors = vq.validate_artifact(_artifact_with_instrument(stance="bullish"))
    assert any("stance" in e for e in errors)
    errors = vq.validate_artifact(_artifact_with_instrument(confidence="sure"))
    assert any("confidence" in e for e in errors)


def test_validate_artifact_bad_gates() -> None:
    errors = vq.validate_artifact(_artifact_with_instrument(gates="bad"))
    assert any("known gate names" in e for e in errors)
    errors = vq.validate_artifact(_artifact_with_instrument(gates=["novel"]))
    assert any("known gate names" in e for e in errors)


def test_validate_artifact_driver_errors() -> None:
    errors = vq.validate_artifact(_artifact_with_instrument(drivers=[]))
    assert any("non-empty array" in e for e in errors)
    errors = vq.validate_artifact(_artifact_with_instrument(drivers="bad"))
    assert any("non-empty array" in e for e in errors)
    driver = {"text": "t", "citations": [_A]}
    errors = vq.validate_artifact(_artifact_with_instrument(drivers=[driver] * 4))
    assert any("more than 3 drivers" in e for e in errors)
    errors = vq.validate_artifact(_artifact_with_instrument(drivers=["bad"]))
    assert any("driver[0] must be" in e for e in errors)
    long_driver = {"text": "x" * 301, "citations": [_A]}
    errors = vq.validate_artifact(_artifact_with_instrument(drivers=[long_driver]))
    assert any("exceeds 300" in e for e in errors)


def test_validate_artifact_unknown_canonical_id() -> None:
    artifact = _artifact_with_instrument(canonical_id="unknown")
    errors = vq.validate_artifact(artifact, analysis=make_analysis())
    assert any("not present in the analysis artifact" in e for e in errors)


def test_validate_artifact_symbol_mismatch() -> None:
    artifact = _artifact_with_instrument(symbol="^WRONG")
    errors = vq.validate_artifact(artifact, analysis=make_analysis())
    assert any("does not match" in e for e in errors)


def test_validate_artifact_non_string_canonical_id_skips_analysis_check() -> None:
    artifact = _artifact_with_instrument(canonical_id=42)
    errors = vq.validate_artifact(artifact, analysis=make_analysis())
    assert not any("not present in the analysis artifact" in e for e in errors)


# ── numeric/direction helpers ──────────────────────────────────────────────────


def test_claimed_percentages_tolerances() -> None:
    claims = vq._claimed_percentages("up 3.1% then about 2% and -0.25 %")
    assert claims == [(3.1, 0.05), (2.0, 0.5), (-0.25, 0.005)]


def test_numeric_mismatch() -> None:
    assert not vq._numeric_mismatch("gained 3.1%", [3.13])
    assert not vq._numeric_mismatch("fell 3.1%", [-3.13])
    assert vq._numeric_mismatch("gained 9.9%", [3.13])
    assert not vq._numeric_mismatch("no numbers here", [])


def test_feature_percentages_skips_non_numeric() -> None:
    values = vq._feature_percentages({
        "ret_1d": 0.01,
        "ret_5d": None,
        "ret_20d": True,
        "rsi_14": 62.0,
    })
    assert values == [1.0]


def test_direction_conflict() -> None:
    down_features = {"ret_5d": -0.02, "ret_20d": -0.03}
    up_features = {"ret_5d": 0.02, "ret_20d": 0.03}
    assert vq._direction_conflict("The index rallied strongly", down_features)
    assert not vq._direction_conflict("The index rallied strongly", up_features)
    assert vq._direction_conflict("Shares dropped sharply", up_features)
    assert not vq._direction_conflict("Shares dropped sharply", down_features)
    assert not vq._direction_conflict("Flat and quiet", down_features)
    assert not vq._direction_conflict("rallied", {"ret_5d": None})


# ── apply_gates ─────────────────────────────────────────────────────────────────


def test_apply_gates_clean_artifact() -> None:
    gated = vq.apply_gates(make_artifact(), analysis=make_analysis())
    assert gated["instruments"][0]["gates"] == []
    assert gated["market_narrative"]["gates"] == []
    assert gated["themes"][0]["gates"] == []
    assert gated["metadata"]["gates"] == {
        "gated_instruments": [],
        "narrative_gates": [],
    }


def test_apply_gates_uncited_claims() -> None:
    artifact = _artifact_with_instrument(
        drivers=[{"text": "No sources for this.", "citations": []}]
    )
    gated = vq.apply_gates(artifact, analysis=make_analysis())
    assert "uncited_claims" in gated["instruments"][0]["gates"]
    assert gated["metadata"]["gates"]["gated_instruments"] == ["spx"]


def test_apply_gates_stale_evidence() -> None:
    artifact = make_artifact()
    artifact["citations"][_C] = _citation_entry(make_evidence()["items"][2])
    artifact["instruments"][0]["drivers"] = [
        {"text": "Based on an old story.", "citations": [_C]}
    ]
    gated = vq.apply_gates(artifact, analysis=make_analysis())
    assert "stale_evidence" in gated["instruments"][0]["gates"]


def test_apply_gates_numeric_claim_mismatch() -> None:
    artifact = _artifact_with_instrument(
        drivers=[{"text": "The index soared 42.0% last week.", "citations": [_A]}]
    )
    gated = vq.apply_gates(artifact, analysis=make_analysis())
    assert "numeric_claim_mismatch" in gated["instruments"][0]["gates"]


def test_apply_gates_numeric_claim_matches_evidence_text() -> None:
    artifact = _artifact_with_instrument(
        drivers=[{"text": "A gain of 3.1% was reported.", "citations": [_A]}]
    )
    gated = vq.apply_gates(artifact, analysis=make_analysis())
    assert "numeric_claim_mismatch" not in gated["instruments"][0]["gates"]


def test_apply_gates_direction_conflict() -> None:
    artifact = make_artifact()
    artifact["instruments"].append({
        "canonical_id": "dji",
        "symbol": "^DJI",
        "stance": "supportive",
        "confidence": "medium",
        "drivers": [{"text": "The Dow rallied this month.", "citations": [_B]}],
        "gates": [],
    })
    gated = vq.apply_gates(artifact, analysis=make_analysis())
    assert "direction_conflict" in gated["instruments"][1]["gates"]
    assert gated["metadata"]["gates"]["gated_instruments"] == ["dji"]


def test_apply_gates_narrative_and_theme() -> None:
    artifact = make_artifact()
    artifact["market_narrative"] = {
        "text": "Markets moved 77.7% in a day.",
        "citations": [],
        "gates": [],
    }
    artifact["themes"][0]["citations"] = []
    gated = vq.apply_gates(artifact, analysis=make_analysis())
    assert gated["market_narrative"]["gates"] == [
        "numeric_claim_mismatch",
        "uncited_claims",
    ]
    assert gated["metadata"]["gates"]["narrative_gates"] == [
        "numeric_claim_mismatch",
        "uncited_claims",
    ]
    assert gated["themes"][0]["gates"] == ["uncited_claims"]


def test_apply_gates_narrative_matches_any_instrument_feature() -> None:
    artifact = make_artifact()
    artifact["market_narrative"]["text"] = (
        "Leadership was narrow, with a 5.3% one-month move at the top."
    )
    gated = vq.apply_gates(artifact, analysis=make_analysis())
    assert "numeric_claim_mismatch" not in gated["market_narrative"]["gates"]


def test_apply_gates_unknown_instrument_features_default_empty() -> None:
    artifact = _artifact_with_instrument(canonical_id="ghost")
    gated = vq.apply_gates(artifact, analysis=make_analysis())
    assert "direction_conflict" not in gated["instruments"][0]["gates"]


def test_citation_texts_skips_missing_entries() -> None:
    assert vq._citation_texts(["missing"], {}) == []
    assert vq._citation_texts([_A], {_A: {"title": "t", "summary": "s"}}) == ["t s"]


def test_all_stale_missing_citation_entry_counts_stale() -> None:
    assert vq._all_stale(["missing"], {}, "2023-12-27")
    assert not vq._all_stale([], {}, "2023-12-27")


# ── CLI ─────────────────────────────────────────────────────────────────────────


def test_main_ok(tmp_path: Any) -> None:
    artifact_path = tmp_path / "qual.json"
    artifact_path.write_text(json.dumps(make_artifact()))
    evidence_path = tmp_path / "evidence.json"
    evidence_path.write_text(json.dumps(make_evidence()))
    analysis_path = tmp_path / "analysis.json"
    analysis_path.write_text(json.dumps(make_analysis()))
    result = vq.main([
        "--input",
        str(artifact_path),
        "--evidence",
        str(evidence_path),
        "--analysis",
        str(analysis_path),
    ])
    assert result == 0


def test_main_ok_without_context(tmp_path: Any) -> None:
    artifact_path = tmp_path / "qual.json"
    artifact_path.write_text(json.dumps(make_artifact()))
    assert vq.main(["--input", str(artifact_path)]) == 0


def test_main_errors(tmp_path: Any, capsys: pytest.CaptureFixture[str]) -> None:
    artifact_path = tmp_path / "qual.json"
    artifact_path.write_text(json.dumps({"version": "1.0.0"}))
    assert vq.main(["--input", str(artifact_path)]) == 1
    assert "missing required key" in capsys.readouterr().out


def test_main_missing_file(tmp_path: Any) -> None:
    assert vq.main(["--input", str(tmp_path / "nope.json")]) == 1


def test_main_bad_json(tmp_path: Any) -> None:
    path = tmp_path / "bad.json"
    path.write_text("{")
    assert vq.main(["--input", str(path)]) == 1
