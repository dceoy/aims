r"""Validate AIMS qualitative artifacts and apply deterministic grounding gates.

Schema validation enforces the artifact contract (shape, enums, length caps,
citation references). Grounding gates are deterministic cross-checks against
the quantitative artifact and cited evidence — schema validity is not truth.
Gated entries are excluded from report rendering; the artifact still publishes.

Usage:
    uv run .agents/skills/qualitative-analysis/scripts/validate_qualitative.py \
        --input data/qualitative/2026-07-02.json \
        --evidence data/evidence/2026-07-02.json \
        --analysis data/analysis/2026-07-02.json
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import date, timedelta
from pathlib import Path
from typing import Any, Final

QUALITATIVE_VERSION: Final[str] = "1.0.0"

STANCES: Final[tuple[str, ...]] = ("supportive", "neutral", "conflicting")
CONFIDENCES: Final[tuple[str, ...]] = ("low", "medium", "high")
GATES: Final[tuple[str, ...]] = (
    "direction_conflict",
    "numeric_claim_mismatch",
    "stale_evidence",
    "uncited_claims",
)

NARRATIVE_TEXT_LIMIT: Final[int] = 1200
THEME_TITLE_LIMIT: Final[int] = 80
THEME_TEXT_LIMIT: Final[int] = 400
DRIVER_TEXT_LIMIT: Final[int] = 300
MAX_THEMES: Final[int] = 5
MAX_DRIVERS: Final[int] = 3
MAX_CITATIONS: Final[int] = 8
EVIDENCE_STALE_DAYS: Final[int] = 5

_REQUIRED_TOP: Final[tuple[str, ...]] = (
    "version",
    "metadata",
    "market_narrative",
    "themes",
    "instruments",
    "citations",
)
_REQUIRED_META: Final[tuple[str, ...]] = (
    "generated_at",
    "analysis_date",
    "model",
    "prompt_version",
    "input_hashes",
    "gates",
)
_REQUIRED_INST: Final[tuple[str, ...]] = (
    "canonical_id",
    "symbol",
    "stance",
    "confidence",
    "drivers",
    "gates",
)

_PCT_RE: Final[re.Pattern[str]] = re.compile(r"([-+]?\d+(?:\.\d+)?)\s?%")
_UP_RE: Final[re.Pattern[str]] = re.compile(
    r"\b(?:rallied|rally|surged|surge|rose|risen|gained|jumped|climbed|advanced)\b",
    re.IGNORECASE,
)
_DOWN_RE: Final[re.Pattern[str]] = re.compile(
    r"\b(?:fell|dropped|declined|plunged|slumped|tumbled|sank|slid)\b",
    re.IGNORECASE,
)
_PCT_FEATURES: Final[tuple[str, ...]] = (
    "ret_1d",
    "ret_5d",
    "ret_20d",
    "ret_60d",
    "ma20_dist",
    "ma50_dist",
    "vol_20d",
    "mdd_60d",
)


def _check_citation_block(
    errors: list[str],
    obj: dict[str, Any],
    label: str,
    citation_ids: set[str],
) -> None:
    citations = obj.get("citations")
    if not isinstance(citations, list) or any(
        not isinstance(c, str) for c in citations
    ):
        errors.append(f"{label}: citations must be an array of strings")
        return
    if len(citations) > MAX_CITATIONS:
        errors.append(f"{label}: more than {MAX_CITATIONS} citations")
    errors.extend(
        f"{label}: citation {cid!r} not present in the citations map"
        for cid in citations
        if cid not in citation_ids
    )


def _check_text(
    errors: list[str], obj: dict[str, Any], label: str, key: str, limit: int
) -> None:
    value = obj.get(key)
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{label}: {key} must be a non-empty string")
    elif len(value) > limit:
        errors.append(f"{label}: {key} exceeds {limit} characters")


def _validate_metadata(errors: list[str], data: dict[str, Any]) -> None:
    metadata = data["metadata"]
    if not isinstance(metadata, dict):
        errors.append("'metadata' must be a JSON object")
        return
    errors.extend(
        f"metadata missing required key: {key!r}"
        for key in _REQUIRED_META
        if key not in metadata
    )
    gates_meta = metadata.get("gates")
    if gates_meta is not None and not isinstance(gates_meta, dict):
        errors.append("metadata.gates must be a JSON object")


def _validate_citations_map(
    errors: list[str],
    data: dict[str, Any],
    evidence: dict[str, Any] | None,
) -> set[str]:
    citations = data["citations"]
    if not isinstance(citations, dict):
        errors.append("'citations' must be a JSON object")
        return set()
    evidence_ids: set[str] | None = None
    if evidence is not None:
        evidence_ids = {
            str(item.get("id"))
            for item in evidence.get("items", [])
            if isinstance(item, dict)
        }
    for cid, entry in citations.items():
        if not isinstance(entry, dict):
            errors.append(f"citations[{cid!r}] must be a JSON object")
            continue
        errors.extend(
            f"citations[{cid!r}] missing required key: {key!r}"
            for key in ("title", "url", "source", "published_at")
            if key not in entry
        )
        if evidence_ids is not None and cid not in evidence_ids:
            errors.append(f"citations[{cid!r}]: id not present in the evidence bundle")
    return set(citations)


def _validate_instruments(
    errors: list[str],
    data: dict[str, Any],
    citation_ids: set[str],
    analysis: dict[str, Any] | None,
) -> None:
    instruments = data["instruments"]
    if not isinstance(instruments, list):
        errors.append("'instruments' must be a JSON array")
        return
    known: dict[str, str] | None = None
    if analysis is not None:
        known = {
            str(inst["canonical_id"]): str(inst.get("symbol", ""))
            for inst in analysis.get("instruments", [])
            if isinstance(inst, dict) and inst.get("canonical_id")
        }
    for idx, inst in enumerate(instruments):
        label = f"instrument[{idx}]"
        if not isinstance(inst, dict):
            errors.append(f"{label} must be a JSON object")
            continue
        errors.extend(
            f"{label} missing required key: {key!r}"
            for key in _REQUIRED_INST
            if key not in inst
        )
        if inst.get("stance") not in STANCES:
            errors.append(f"{label}: stance {inst.get('stance')!r} not in {STANCES}")
        if inst.get("confidence") not in CONFIDENCES:
            errors.append(
                f"{label}: confidence {inst.get('confidence')!r} not in {CONFIDENCES}"
            )
        gates = inst.get("gates")
        if not isinstance(gates, list) or any(g not in GATES for g in gates):
            errors.append(f"{label}: gates must be an array of known gate names")
        drivers = inst.get("drivers")
        if not isinstance(drivers, list) or not drivers:
            errors.append(f"{label}: drivers must be a non-empty array")
        elif len(drivers) > MAX_DRIVERS:
            errors.append(f"{label}: more than {MAX_DRIVERS} drivers")
        else:
            for didx, driver in enumerate(drivers):
                dlabel = f"{label}.driver[{didx}]"
                if not isinstance(driver, dict):
                    errors.append(f"{dlabel} must be a JSON object")
                    continue
                _check_text(errors, driver, dlabel, "text", DRIVER_TEXT_LIMIT)
                _check_citation_block(errors, driver, dlabel, citation_ids)
        canonical_id = inst.get("canonical_id")
        if known is not None and isinstance(canonical_id, str):
            if canonical_id not in known:
                errors.append(
                    f"{label}: canonical_id {canonical_id!r}"
                    " not present in the analysis artifact"
                )
            elif inst.get("symbol") != known[canonical_id]:
                errors.append(
                    f"{label}: symbol {inst.get('symbol')!r} does not match"
                    f" the analysis artifact ({known[canonical_id]!r})"
                )


def validate_artifact(
    data: dict[str, Any],
    *,
    evidence: dict[str, Any] | None = None,
    analysis: dict[str, Any] | None = None,
) -> list[str]:
    """Return schema/contract errors for a qualitative artifact (empty if valid).

    When *evidence* is given, every citation must reference a bundle item.
    When *analysis* is given, every instrument must exist in the quantitative
    artifact with a matching symbol.
    """
    errors = [
        f"missing required key: {key!r}" for key in _REQUIRED_TOP if key not in data
    ]
    if errors:
        return errors
    if data["version"] != QUALITATIVE_VERSION:
        errors.append(
            f"unsupported version {data['version']!r}"
            f" (expected {QUALITATIVE_VERSION!r})"
        )
    _validate_metadata(errors, data)
    citation_ids = _validate_citations_map(errors, data, evidence)

    narrative = data["market_narrative"]
    if not isinstance(narrative, dict):
        errors.append("'market_narrative' must be a JSON object")
    else:
        _check_text(errors, narrative, "market_narrative", "text", NARRATIVE_TEXT_LIMIT)
        _check_citation_block(errors, narrative, "market_narrative", citation_ids)

    themes = data["themes"]
    if not isinstance(themes, list):
        errors.append("'themes' must be a JSON array")
    elif len(themes) > MAX_THEMES:
        errors.append(f"more than {MAX_THEMES} themes")
    else:
        for idx, theme in enumerate(themes):
            label = f"theme[{idx}]"
            if not isinstance(theme, dict):
                errors.append(f"{label} must be a JSON object")
                continue
            _check_text(errors, theme, label, "title", THEME_TITLE_LIMIT)
            _check_text(errors, theme, label, "text", THEME_TEXT_LIMIT)
            _check_citation_block(errors, theme, label, citation_ids)

    _validate_instruments(errors, data, citation_ids, analysis)
    return errors


# ── Grounding gates ──────────────────────────────────────────────────────────


def _claimed_percentages(text: str) -> list[tuple[float, float]]:
    """Extract (value, tolerance) pairs for percentage claims in *text*."""
    claims: list[tuple[float, float]] = []
    for match in _PCT_RE.finditer(text):
        raw = match.group(1)
        decimals = len(raw.split(".")[1]) if "." in raw else 0
        claims.append((float(raw), 0.5 / (10**decimals)))
    return claims


def _feature_percentages(features: dict[str, Any]) -> list[float]:
    values: list[float] = []
    for key in _PCT_FEATURES:
        value = features.get(key)
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            values.append(float(value) * 100.0)
    return values


def _evidence_percentages(
    citation_texts: list[str],
) -> list[float]:
    values: list[float] = []
    for text in citation_texts:
        values.extend(claim for claim, _tol in _claimed_percentages(text))
    return values


def _numeric_mismatch(text: str, candidates: list[float]) -> bool:
    """Return True when a percentage claim in *text* matches no candidate."""
    for claim, tolerance in _claimed_percentages(text):
        matched = any(
            abs(claim - value) <= tolerance + 1e-9
            or abs(claim + value) <= tolerance + 1e-9
            for value in candidates
        )
        if not matched:
            return True
    return False


def _direction_conflict(text: str, features: dict[str, Any]) -> bool:
    ret_5d = features.get("ret_5d")
    ret_20d = features.get("ret_20d")
    if not isinstance(ret_5d, (int, float)) or not isinstance(ret_20d, (int, float)):
        return False
    if _UP_RE.search(text) and ret_5d < 0 and ret_20d < 0:
        return True
    return bool(_DOWN_RE.search(text) and ret_5d > 0 and ret_20d > 0)


def _citation_texts(citations: list[str], citations_map: dict[str, Any]) -> list[str]:
    texts: list[str] = []
    for cid in citations:
        entry = citations_map.get(cid)
        if isinstance(entry, dict):
            texts.append(f"{entry.get('title', '')} {entry.get('summary', '')}")
    return texts


def _all_stale(
    citations: list[str],
    citations_map: dict[str, Any],
    earliest_fresh: str,
) -> bool:
    if not citations:
        return False
    for cid in citations:
        entry = citations_map.get(cid)
        published = (
            str(entry.get("published_at", "")) if isinstance(entry, dict) else ""
        )
        if published[:10] >= earliest_fresh:
            return False
    return True


def _block_gates(
    *,
    texts_with_citations: list[tuple[str, list[str]]],
    citations_map: dict[str, Any],
    earliest_fresh: str,
    features: dict[str, Any] | None,
    extra_candidates: list[float],
) -> list[str]:
    """Compute gates for one narrative/theme/instrument block."""
    gates: list[str] = []
    all_citations = [c for _text, cits in texts_with_citations for c in cits]
    if any(not cits for _text, cits in texts_with_citations):
        gates.append("uncited_claims")
    if _all_stale(all_citations, citations_map, earliest_fresh) and all_citations:
        gates.append("stale_evidence")
    candidates = list(extra_candidates)
    if features is not None:
        candidates.extend(_feature_percentages(features))
    candidates.extend(
        _evidence_percentages(_citation_texts(all_citations, citations_map))
    )
    if any(_numeric_mismatch(text, candidates) for text, _cits in texts_with_citations):
        gates.append("numeric_claim_mismatch")
    if features is not None and any(
        _direction_conflict(text, features) for text, _cits in texts_with_citations
    ):
        gates.append("direction_conflict")
    return sorted(gates)


def apply_gates(
    data: dict[str, Any],
    *,
    analysis: dict[str, Any],
    stale_days: int = EVIDENCE_STALE_DAYS,
) -> dict[str, Any]:
    """Return a copy of *data* with deterministic grounding gates recorded."""
    result: dict[str, Any] = json.loads(json.dumps(data))
    citations_map = result.get("citations", {})
    analysis_date = str(result["metadata"]["analysis_date"])
    earliest_fresh = (
        date.fromisoformat(analysis_date) - timedelta(days=stale_days)
    ).isoformat()
    features_by_id: dict[str, dict[str, Any]] = {
        str(inst["canonical_id"]): inst.get("features") or {}
        for inst in analysis.get("instruments", [])
        if isinstance(inst, dict) and inst.get("canonical_id")
    }
    all_feature_pcts: list[float] = []
    for features in features_by_id.values():
        all_feature_pcts.extend(_feature_percentages(features))

    for inst in result["instruments"]:
        features = features_by_id.get(str(inst["canonical_id"]), {})
        inst["gates"] = _block_gates(
            texts_with_citations=[
                (str(d["text"]), list(d["citations"])) for d in inst["drivers"]
            ],
            citations_map=citations_map,
            earliest_fresh=earliest_fresh,
            features=features,
            extra_candidates=[],
        )

    narrative = result["market_narrative"]
    narrative["gates"] = _block_gates(
        texts_with_citations=[(str(narrative["text"]), list(narrative["citations"]))],
        citations_map=citations_map,
        earliest_fresh=earliest_fresh,
        features=None,
        extra_candidates=all_feature_pcts,
    )

    for theme in result["themes"]:
        theme["gates"] = _block_gates(
            texts_with_citations=[(str(theme["text"]), list(theme["citations"]))],
            citations_map=citations_map,
            earliest_fresh=earliest_fresh,
            features=None,
            extra_candidates=all_feature_pcts,
        )

    result["metadata"]["gates"] = {
        "gated_instruments": sorted(
            str(inst["canonical_id"]) for inst in result["instruments"] if inst["gates"]
        ),
        "narrative_gates": list(narrative["gates"]),
    }
    return result


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input", type=Path, required=True, help="Qualitative artifact JSON"
    )
    parser.add_argument(
        "--evidence", type=Path, default=None, help="Evidence bundle JSON"
    )
    parser.add_argument(
        "--analysis", type=Path, default=None, help="Analysis artifact JSON"
    )
    return parser.parse_args(argv)


def _load(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as fh:
        value: dict[str, Any] = json.load(fh)
    return value


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        data = _load(args.input)
        evidence = _load(args.evidence) if args.evidence else None
        analysis = _load(args.analysis) if args.analysis else None
    except FileNotFoundError as exc:
        print(f"ERROR: file not found: {exc.filename}")
        return 1
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON: {exc}")
        return 1
    errors = validate_artifact(data, evidence=evidence, analysis=analysis)
    if errors:
        for error in errors:
            print(error)
        return 1
    print(f"validated {args.input}: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
