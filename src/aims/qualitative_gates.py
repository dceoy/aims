r"""Deterministic grounding and consistency gates for qualitative artifacts.

Schema validity is not truth: a qualitative artifact can be well-formed while
misstating realized price action or inventing a magnitude. This gate pass
cross-examines the structured claim fields (``direction_claim`` enums and
``numeric_claims`` objects — never prose) against the quantitative analysis
artifact and the cited evidence items, mirroring the ``risk_gates`` pattern.

A ``conflicting`` stance — the model disagreeing with the quantitative signal
on outlook — is legitimate output and is never gated for the disagreement
itself. Only factual misstatements are gated. Gate outcomes are recorded in
artifact metadata so the report and Slack can say why commentary is absent,
and so the shadow period can measure gate pass rates. Gates never modify
quantitative outputs; they only filter qualitative content.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timedelta
from typing import Any, Final

GATE_DIRECTION: Final[str] = "direction_inconsistent"
GATE_NUMERIC: Final[str] = "numeric_claim_mismatch"
GATE_STALE: Final[str] = "stale_evidence"
GATE_CITATION: Final[str] = "citation_coverage"

# An explicit "none" direction claim passes while |return| <= this band.
NONE_DIRECTION_TOLERANCE: Final[float] = 0.01
# percent-unit claims are compared on the fraction scale within 0.5pp.
PERCENT_ABS_TOLERANCE: Final[float] = 0.005
# other units: relative tolerance with a small absolute floor.
NUMERIC_REL_TOLERANCE: Final[float] = 0.05
NUMERIC_ABS_TOLERANCE: Final[float] = 0.01
# Every driver must carry at least one bundle-resolvable citation.
MIN_CITATION_COVERAGE: Final[float] = 1.0
_DEFAULT_STALE_DAYS: Final[int] = 5

_WINDOW_FEATURES: Final[dict[str, str]] = {
    "1d": "ret_1d",
    "5d": "ret_5d",
    "20d": "ret_20d",
    "60d": "ret_60d",
}
_NUM_RE: Final[re.Pattern[str]] = re.compile(r"[-+]?\d+(?:\.\d+)?")


def _features_by_canonical_id(analysis: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        str(inst["canonical_id"]): inst.get("features") or {}
        for inst in analysis.get("instruments", [])
        if inst.get("canonical_id")
    }


def _items_by_id(evidence: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        str(item["id"]): item
        for item in evidence.get("items", [])
        if isinstance(item, dict) and item.get("id")
    }


def _direction_consistent(claim: dict[str, Any], features: dict[str, Any]) -> bool:
    feature_name = _WINDOW_FEATURES[str(claim["window"])]
    value = features.get(feature_name)
    if not isinstance(value, (int, float)):
        return False
    direction = claim["direction"]
    if direction == "up":
        return value > 0
    if direction == "down":
        return value < 0
    return abs(value) <= NONE_DIRECTION_TOLERANCE


def _evidence_numbers(item: dict[str, Any]) -> list[float]:
    text = f"{item.get('title', '')} {item.get('snippet', '')}".replace(",", "")
    return [float(token) for token in _NUM_RE.findall(text)]


def _numeric_claim_holds(
    claim: dict[str, Any],
    features: dict[str, Any] | None,
    items: dict[str, dict[str, Any]],
    cited: frozenset[str],
) -> bool:
    value = claim.get("value")
    refers_to = str(claim.get("refers_to", ""))
    if not isinstance(value, (int, float)):
        return False
    if refers_to in items:
        if refers_to not in cited:
            return False
        tolerance = max(
            NUMERIC_ABS_TOLERANCE, NUMERIC_REL_TOLERANCE * abs(float(value))
        )
        return any(
            abs(number - float(value)) <= tolerance
            for number in _evidence_numbers(items[refers_to])
        )
    if features is not None and refers_to in features:
        expected = features.get(refers_to)
        if not isinstance(expected, (int, float)):
            return False
        if claim.get("unit") == "percent":
            return abs(float(value) / 100.0 - expected) <= PERCENT_ABS_TOLERANCE
        tolerance = max(NUMERIC_ABS_TOLERANCE, NUMERIC_REL_TOLERANCE * abs(expected))
        return abs(float(value) - expected) <= tolerance
    return False


def _citations_of(scope: dict[str, Any]) -> list[str]:
    citations = scope.get("citations")
    return [str(c) for c in citations] if isinstance(citations, list) else []


def _is_recent(
    citation_ids: list[str],
    items: dict[str, dict[str, Any]],
    analysis_date: str,
    stale_days: int,
) -> bool:
    """True when at least one cited item is newer than the staleness cutoff."""
    cutoff = datetime.fromisoformat(f"{analysis_date}T00:00:00+00:00") - timedelta(
        days=stale_days
    )
    for cid in citation_ids:
        item = items.get(cid)
        if item is None:
            continue
        if datetime.fromisoformat(str(item["published_at"])) >= cutoff:
            return True
    return False


def _coverage_ratio(drivers: list[Any], items: dict[str, dict[str, Any]]) -> float:
    covered = sum(
        1
        for driver in drivers
        if isinstance(driver, dict)
        and any(cid in items for cid in _citations_of(driver))
    )
    return covered / len(drivers) if drivers else 0.0


def _numeric_scope_gates(
    scope: dict[str, Any],
    features: dict[str, Any] | None,
    items: dict[str, dict[str, Any]],
) -> bool:
    """True when every numeric claim in *scope* verifies."""
    cited = frozenset(_citations_of(scope))
    return all(
        _numeric_claim_holds(claim, features, items, cited)
        for claim in scope.get("numeric_claims", [])
        if isinstance(claim, dict)
    )


def _instrument_gates(
    entry: dict[str, Any],
    features: dict[str, Any],
    items: dict[str, dict[str, Any]],
    analysis_date: str,
    stale_days: int,
) -> list[str]:
    gates: set[str] = set()
    drivers = [d for d in entry.get("drivers", []) if isinstance(d, dict)]
    for driver in drivers:
        claim = driver.get("direction_claim")
        if isinstance(claim, dict) and not _direction_consistent(claim, features):
            gates.add(GATE_DIRECTION)
        if not _numeric_scope_gates(driver, features, items):
            gates.add(GATE_NUMERIC)
    if _coverage_ratio(drivers, items) < MIN_CITATION_COVERAGE:
        gates.add(GATE_CITATION)
    cited = [cid for driver in drivers for cid in _citations_of(driver)]
    if not _is_recent(cited, items, analysis_date, stale_days):
        gates.add(GATE_STALE)
    return sorted(gates)


def _market_gates(
    market: dict[str, Any],
    items: dict[str, dict[str, Any]],
    analysis_date: str,
    stale_days: int,
) -> list[str]:
    gates: set[str] = set()
    themes = [t for t in market.get("themes", []) if isinstance(t, dict)]
    if not _numeric_scope_gates(market, None, items):
        gates.add(GATE_NUMERIC)
    for theme in themes:
        if not _numeric_scope_gates(theme, None, items):
            gates.add(GATE_NUMERIC)
    scopes = [market, *themes]
    if any(not any(cid in items for cid in _citations_of(scope)) for scope in scopes):
        gates.add(GATE_CITATION)
    cited = [cid for scope in scopes for cid in _citations_of(scope)]
    if not _is_recent(cited, items, analysis_date, stale_days):
        gates.add(GATE_STALE)
    return sorted(gates)


def apply_gates(
    artifact: dict[str, Any],
    analysis: dict[str, Any],
    evidence: dict[str, Any],
) -> dict[str, Any]:
    """Return a copy of *artifact* with gate outcomes recorded.

    Per-instrument entries gain a ``qualitative_gates`` list (non-empty means
    the entry is excluded from rendering); ``metadata.gates`` records the
    summary, including whether the market narrative — and with it the whole
    artifact — is withheld from rendering.
    """
    result: dict[str, Any] = json.loads(json.dumps(artifact))
    analysis_date = str(result["metadata"]["analysis_date"])
    stale_days = int(
        analysis
        .get("metadata", {})
        .get("config", {})
        .get("stale_days", _DEFAULT_STALE_DAYS)
    )
    features_map = _features_by_canonical_id(analysis)
    items = _items_by_id(evidence)

    gated_instruments: dict[str, list[str]] = {}
    for entry in result["instruments"]:
        features = features_map.get(str(entry["canonical_id"]), {})
        gates = _instrument_gates(entry, features, items, analysis_date, stale_days)
        entry["qualitative_gates"] = gates
        if gates:
            gated_instruments[str(entry["canonical_id"])] = gates

    market_gates = _market_gates(result["market"], items, analysis_date, stale_days)
    result["metadata"]["gates"] = {
        "passed": not market_gates and not gated_instruments,
        "market_narrative_withheld": bool(market_gates),
        "market_gates": market_gates,
        "gated_instruments": dict(sorted(gated_instruments.items())),
        "thresholds": {
            "stale_days": stale_days,
            "none_direction_tolerance": NONE_DIRECTION_TOLERANCE,
            "percent_abs_tolerance": PERCENT_ABS_TOLERANCE,
            "numeric_rel_tolerance": NUMERIC_REL_TOLERANCE,
            "numeric_abs_tolerance": NUMERIC_ABS_TOLERANCE,
            "min_citation_coverage": MIN_CITATION_COVERAGE,
        },
    }
    return result
