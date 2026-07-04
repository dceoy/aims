"""Tests for aims.qualitative_gates — deterministic grounding gates."""

from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any

import pytest

from aims import qualitative_gates as qg

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def _load(name: str) -> dict[str, Any]:
    with (FIXTURES / name).open() as fh:
        value: dict[str, Any] = json.load(fh)
    return value


@pytest.fixture
def analysis() -> dict[str, Any]:
    return _load("analysis_2024-01-01_mapped.json")


@pytest.fixture
def evidence() -> dict[str, Any]:
    return _load("evidence_2024-01-01.json")


@pytest.fixture
def artifact() -> dict[str, Any]:
    return _load("qualitative_2024-01-01.json")


def _evidence_id(evidence: dict[str, Any], canonical_id: str | None = None) -> str:
    for item in evidence["items"]:
        if canonical_id is None or canonical_id in item.get("canonical_ids", []):
            return str(item["id"])
    msg = f"no evidence item for {canonical_id!r}"
    raise AssertionError(msg)


def _macro_evidence_id(evidence: dict[str, Any]) -> str:
    for item in evidence["items"]:
        if item["category"] == "macro":
            return str(item["id"])
    msg = "no macro item in fixture"
    raise AssertionError(msg)


# ── fixture sanity ───────────────────────────────────────────────────────────


def test_full_artifact_passes_all_gates(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    gated = qg.apply_gates(artifact, analysis, evidence)
    gates = gated["metadata"]["gates"]
    assert gates["passed"] is True
    assert gates["market_narrative_withheld"] is False
    assert gates["gated_instruments"] == {}
    for entry in gated["instruments"]:
        assert entry["qualitative_gates"] == []


def test_apply_gates_does_not_mutate_input(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    before = copy.deepcopy(artifact)
    qg.apply_gates(artifact, analysis, evidence)
    assert artifact == before


def test_apply_gates_does_not_modify_quantitative_artifact(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    before = copy.deepcopy(analysis)
    qg.apply_gates(artifact, analysis, evidence)
    assert analysis == before


# ── direction consistency ───────────────────────────────────────────────────


def test_direction_gate_fails_on_contradiction(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    artifact["instruments"][0]["drivers"][0]["direction_claim"]["direction"] = "down"
    gated = qg.apply_gates(artifact, analysis, evidence)
    spx = next(i for i in gated["instruments"] if i["canonical_id"] == "spx")
    assert qg.GATE_DIRECTION in spx["qualitative_gates"]


def test_direction_gate_passes_matching_direction(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    # ^SPX ret_20d is positive in the fixture; an "up" claim over 20d holds.
    gated = qg.apply_gates(artifact, analysis, evidence)
    spx = next(i for i in gated["instruments"] if i["canonical_id"] == "spx")
    assert qg.GATE_DIRECTION not in spx["qualitative_gates"]


def test_direction_gate_none_claim_within_tolerance(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    for inst in analysis["instruments"]:
        if inst["canonical_id"] == "spx":
            inst["features"]["ret_1d"] = 0.0
    artifact["instruments"][0]["drivers"][0]["direction_claim"] = {
        "direction": "none",
        "window": "1d",
    }
    gated = qg.apply_gates(artifact, analysis, evidence)
    spx = next(i for i in gated["instruments"] if i["canonical_id"] == "spx")
    assert qg.GATE_DIRECTION not in spx["qualitative_gates"]


def test_direction_gate_none_claim_outside_tolerance(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    artifact["instruments"][0]["drivers"][0]["direction_claim"] = {
        "direction": "none",
        "window": "20d",
    }
    gated = qg.apply_gates(artifact, analysis, evidence)
    spx = next(i for i in gated["instruments"] if i["canonical_id"] == "spx")
    assert qg.GATE_DIRECTION in spx["qualitative_gates"]


def test_direction_gate_fails_on_missing_feature(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    for inst in analysis["instruments"]:
        if inst["canonical_id"] == "spx":
            inst["features"]["ret_20d"] = None
    gated = qg.apply_gates(artifact, analysis, evidence)
    spx = next(i for i in gated["instruments"] if i["canonical_id"] == "spx")
    assert qg.GATE_DIRECTION in spx["qualitative_gates"]


def test_direction_gate_no_claim_never_gated(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    del artifact["instruments"][0]["drivers"][0]["direction_claim"]
    gated = qg.apply_gates(artifact, analysis, evidence)
    spx = next(i for i in gated["instruments"] if i["canonical_id"] == "spx")
    assert qg.GATE_DIRECTION not in spx["qualitative_gates"]


def test_conflicting_stance_never_gated_for_disagreement(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    artifact["instruments"][0]["stance"] = "conflicting"
    gated = qg.apply_gates(artifact, analysis, evidence)
    spx = next(i for i in gated["instruments"] if i["canonical_id"] == "spx")
    assert spx["qualitative_gates"] == []


# ── numeric claims ───────────────────────────────────────────────────────────


def test_numeric_gate_passes_percent_feature_within_tolerance(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    gated = qg.apply_gates(artifact, analysis, evidence)
    spx = next(i for i in gated["instruments"] if i["canonical_id"] == "spx")
    assert qg.GATE_NUMERIC not in spx["qualitative_gates"]


def test_numeric_gate_boundary_tolerance_passes_at_exact_edge(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    # ret_20d = 0.053 -> 5.3%; claiming 5.8% is exactly +0.5pp, the tolerance edge.
    artifact["instruments"][0]["drivers"][0]["numeric_claims"][0]["value"] = 5.8
    gated = qg.apply_gates(artifact, analysis, evidence)
    spx = next(i for i in gated["instruments"] if i["canonical_id"] == "spx")
    assert qg.GATE_NUMERIC not in spx["qualitative_gates"]


def test_numeric_gate_fails_just_past_boundary(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    artifact["instruments"][0]["drivers"][0]["numeric_claims"][0]["value"] = 5.9
    gated = qg.apply_gates(artifact, analysis, evidence)
    spx = next(i for i in gated["instruments"] if i["canonical_id"] == "spx")
    assert qg.GATE_NUMERIC in spx["qualitative_gates"]


def test_numeric_gate_fails_unresolvable_refers_to(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    artifact["instruments"][0]["drivers"][0]["numeric_claims"][0]["refers_to"] = (
        "not_a_feature_or_evidence_id"
    )
    gated = qg.apply_gates(artifact, analysis, evidence)
    spx = next(i for i in gated["instruments"] if i["canonical_id"] == "spx")
    assert qg.GATE_NUMERIC in spx["qualitative_gates"]


def test_numeric_gate_evidence_referenced_claim_requires_citation(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    dji_id = _evidence_id(evidence, "dji")
    driver = artifact["instruments"][1]["drivers"][0]
    driver["numeric_claims"][0]["refers_to"] = dji_id
    driver["citations"] = ["ev-not-cited-here"[:19]]
    gated = qg.apply_gates(artifact, analysis, evidence)
    dji = next(i for i in gated["instruments"] if i["canonical_id"] == "dji")
    assert qg.GATE_NUMERIC in dji["qualitative_gates"]


def test_numeric_gate_evidence_text_number_matches(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    dji_id = _evidence_id(evidence, "dji")
    artifact["instruments"][1]["drivers"][0]["numeric_claims"][0] = {
        "value": 2.1,
        "unit": "other",
        "refers_to": dji_id,
    }
    artifact["instruments"][1]["drivers"][0]["citations"] = [dji_id]
    gated = qg.apply_gates(artifact, analysis, evidence)
    dji = next(i for i in gated["instruments"] if i["canonical_id"] == "dji")
    assert qg.GATE_NUMERIC not in dji["qualitative_gates"]


def test_numeric_gate_non_numeric_value_fails(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    # Bypasses validate_qualitative on purpose: gates must not crash on a
    # malformed value and must gate it as unverifiable.
    artifact["instruments"][0]["drivers"][0]["numeric_claims"][0]["value"] = "5.3"
    gated = qg.apply_gates(artifact, analysis, evidence)
    spx = next(i for i in gated["instruments"] if i["canonical_id"] == "spx")
    assert qg.GATE_NUMERIC in spx["qualitative_gates"]


def test_numeric_gate_passes_feature_non_percent_unit(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    rsi = next(
        i["features"]["rsi_14"]
        for i in analysis["instruments"]
        if i["canonical_id"] == "spx"
    )
    artifact["instruments"][0]["drivers"][0]["numeric_claims"][0] = {
        "value": rsi,
        "unit": "other",
        "refers_to": "rsi_14",
    }
    gated = qg.apply_gates(artifact, analysis, evidence)
    spx = next(i for i in gated["instruments"] if i["canonical_id"] == "spx")
    assert qg.GATE_NUMERIC not in spx["qualitative_gates"]


def test_numeric_gate_evidence_text_number_mismatch(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    dji_id = _evidence_id(evidence, "dji")
    artifact["instruments"][1]["drivers"][0]["numeric_claims"][0] = {
        "value": 99.0,
        "unit": "other",
        "refers_to": dji_id,
    }
    artifact["instruments"][1]["drivers"][0]["citations"] = [dji_id]
    gated = qg.apply_gates(artifact, analysis, evidence)
    dji = next(i for i in gated["instruments"] if i["canonical_id"] == "dji")
    assert qg.GATE_NUMERIC in dji["qualitative_gates"]


# ── evidence recency ─────────────────────────────────────────────────────────


def test_stale_gate_fails_when_all_citations_old(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    for item in evidence["items"]:
        item["published_at"] = "2023-01-01T00:00:00+00:00"
    gated = qg.apply_gates(artifact, analysis, evidence)
    spx = next(i for i in gated["instruments"] if i["canonical_id"] == "spx")
    assert qg.GATE_STALE in spx["qualitative_gates"]


def test_stale_gate_passes_with_one_recent_citation(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    gated = qg.apply_gates(artifact, analysis, evidence)
    spx = next(i for i in gated["instruments"] if i["canonical_id"] == "spx")
    assert qg.GATE_STALE not in spx["qualitative_gates"]


def test_stale_gate_respects_configured_stale_days(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    analysis["metadata"]["config"]["stale_days"] = 0
    for item in evidence["items"]:
        item["published_at"] = "2023-12-31T23:59:00+00:00"
    gated = qg.apply_gates(artifact, analysis, evidence)
    spx = next(i for i in gated["instruments"] if i["canonical_id"] == "spx")
    assert qg.GATE_STALE in spx["qualitative_gates"]


def test_stale_gate_no_citations_resolves_as_stale(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    artifact["instruments"][0]["drivers"][0]["citations"] = ["ev-missing0000000"]
    gated = qg.apply_gates(artifact, analysis, evidence)
    spx = next(i for i in gated["instruments"] if i["canonical_id"] == "spx")
    assert qg.GATE_STALE in spx["qualitative_gates"]


# ── citation coverage ────────────────────────────────────────────────────────


def test_citation_coverage_gate_fails_when_driver_cites_nothing_resolvable(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    artifact["instruments"][0]["drivers"][0]["citations"] = ["ev-missing0000000"]
    gated = qg.apply_gates(artifact, analysis, evidence)
    spx = next(i for i in gated["instruments"] if i["canonical_id"] == "spx")
    assert qg.GATE_CITATION in spx["qualitative_gates"]


def test_citation_coverage_gate_passes_when_fully_covered(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    gated = qg.apply_gates(artifact, analysis, evidence)
    spx = next(i for i in gated["instruments"] if i["canonical_id"] == "spx")
    assert qg.GATE_CITATION not in spx["qualitative_gates"]


def test_citation_coverage_gate_partial_coverage_fails(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    spx_id = _evidence_id(evidence, "spx")
    extra_driver = {
        "text": "Additional context without resolvable citation.",
        "citations": ["ev-missing0000000"],
    }
    artifact["instruments"][0]["drivers"].append(extra_driver)
    artifact["instruments"][0]["drivers"][0]["citations"] = [spx_id]
    gated = qg.apply_gates(artifact, analysis, evidence)
    spx = next(i for i in gated["instruments"] if i["canonical_id"] == "spx")
    assert qg.GATE_CITATION in spx["qualitative_gates"]


# ── market-level gates and withholding ──────────────────────────────────────


def test_market_numeric_gate_withholds_narrative(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    fed_id = _macro_evidence_id(evidence)
    artifact["market"]["numeric_claims"] = [
        {"value": 99.9, "unit": "percent", "refers_to": fed_id}
    ]
    gated = qg.apply_gates(artifact, analysis, evidence)
    gates = gated["metadata"]["gates"]
    assert gates["market_narrative_withheld"] is True
    assert qg.GATE_NUMERIC in gates["market_gates"]
    assert gates["passed"] is False


def test_market_citation_gate_withholds_narrative(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    artifact["market"]["citations"] = ["ev-missing0000000"]
    gated = qg.apply_gates(artifact, analysis, evidence)
    assert gated["metadata"]["gates"]["market_narrative_withheld"] is True
    assert qg.GATE_CITATION in gated["metadata"]["gates"]["market_gates"]


def test_theme_citation_gate_withholds_narrative(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    artifact["market"]["themes"][0]["citations"] = ["ev-missing0000000"]
    gated = qg.apply_gates(artifact, analysis, evidence)
    assert gated["metadata"]["gates"]["market_narrative_withheld"] is True


def test_market_stale_gate_withholds_narrative(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    for item in evidence["items"]:
        item["published_at"] = "2023-01-01T00:00:00+00:00"
    gated = qg.apply_gates(artifact, analysis, evidence)
    assert gated["metadata"]["gates"]["market_narrative_withheld"] is True
    assert qg.GATE_STALE in gated["metadata"]["gates"]["market_gates"]


def test_theme_numeric_gate_withholds_narrative_independent_of_market(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    fed_id = _macro_evidence_id(evidence)
    artifact["market"]["themes"][0]["numeric_claims"] = [
        {"value": 12345.0, "unit": "count", "refers_to": fed_id}
    ]
    gated = qg.apply_gates(artifact, analysis, evidence)
    gates = gated["metadata"]["gates"]
    assert gates["market_narrative_withheld"] is True
    assert qg.GATE_NUMERIC in gates["market_gates"]


def test_market_passes_with_valid_theme_numeric_claim(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    fed_id = _macro_evidence_id(evidence)
    fed_item = next(i for i in evidence["items"] if i["id"] == fed_id)
    # snippet mentions no explicit number; add one and cite it accurately.
    fed_item["snippet"] += " The vote was 9 to 0."
    artifact["market"]["themes"][0]["numeric_claims"] = [
        {"value": 9, "unit": "count", "refers_to": fed_id}
    ]
    gated = qg.apply_gates(artifact, analysis, evidence)
    assert gated["metadata"]["gates"]["market_narrative_withheld"] is False


def test_instrument_gate_excludes_only_offending_entry(
    artifact: dict[str, Any], analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    artifact["instruments"][0]["drivers"][0]["direction_claim"]["direction"] = "down"
    gated = qg.apply_gates(artifact, analysis, evidence)
    spx = next(i for i in gated["instruments"] if i["canonical_id"] == "spx")
    dji = next(i for i in gated["instruments"] if i["canonical_id"] == "dji")
    assert spx["qualitative_gates"] != []
    assert dji["qualitative_gates"] == []
    assert gated["metadata"]["gates"]["gated_instruments"] == {
        "spx": [qg.GATE_DIRECTION]
    }
    assert gated["metadata"]["gates"]["market_narrative_withheld"] is False


# ── pre-built fixtures agree with apply_gates ───────────────────────────────


def test_gated_fixture_matches_recomputed_gates(
    analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    committed = _load("qualitative_2024-01-01_gated.json")
    source = copy.deepcopy(committed)
    for inst in source["instruments"]:
        inst.pop("qualitative_gates", None)
    source["metadata"].pop("gates", None)
    recomputed = qg.apply_gates(source, analysis, evidence)
    assert recomputed["metadata"]["gates"] == committed["metadata"]["gates"]


def test_withheld_fixture_matches_recomputed_gates(
    analysis: dict[str, Any], evidence: dict[str, Any]
) -> None:
    committed = _load("qualitative_2024-01-01_withheld.json")
    source = copy.deepcopy(committed)
    for inst in source["instruments"]:
        inst.pop("qualitative_gates", None)
    source["metadata"].pop("gates", None)
    recomputed = qg.apply_gates(source, analysis, evidence)
    assert recomputed["metadata"]["gates"] == committed["metadata"]["gates"]
