r"""Structural regression harness for qualitative prompt and model changes.

A prompt edit or model swap can silently change output quality with no code
diff to review. Before adopting one, run candidate qualitative artifacts
(generated with the candidate prompt/model from committed inputs, or the
committed fixtures) through this harness: it recomputes the validator and the
deterministic #93 gates and asserts **structural and gate metrics** —
citation coverage, gate pass rates, stance-distribution sanity — never exact
prose. Results are recorded in ``data/performance/prompt_regressions.json``
keyed by the prompt file's SHA-256 and the pinned model ID, so the prompt
version history lives alongside its measured results and CI can verify that
the committed prompt has a recorded passing run.

There is no automatic prompt tuning here: the harness only measures and
records; adopting a change stays a reviewed human decision.

Usage:
    uv run .agents/skills/qualitative-analysis/scripts/prompt_regression.py \
        --artifact tests/fixtures/qualitative_2024-01-01.json \
        --analysis tests/fixtures/analysis_2024-01-01_mapped.json \
        --evidence tests/fixtures/evidence_2024-01-01.json \
        --record data/performance/prompt_regressions.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Final

from aims.qualitative import DEFAULT_PROMPT_PATH, MODEL_ID, PROMPT_VERSION
from aims.qualitative_gates import apply_gates
from aims.validate_qualitative import sha256_file, validate_artifact

PROMPT_REGRESSION_VERSION: Final[str] = "1.0.0"
DEFAULT_RECORD_PATH: Final[Path] = Path("data/performance/prompt_regressions.json")
DEFAULT_MIN_GATE_PASS_RATE: Final[float] = 0.6
DEFAULT_MIN_CITATION_COVERAGE: Final[float] = 1.0

_STANCES: Final[tuple[str, ...]] = ("supportive", "neutral", "conflicting")
_CONFIDENCES: Final[tuple[str, ...]] = ("low", "medium", "high")
_ROUND_DIGITS: Final[int] = 6


def _citation_scopes(artifact: dict[str, Any]) -> list[list[str]]:
    """Citation lists of every scope that must resolve: narrative, themes, drivers."""
    market = artifact.get("market", {})
    scopes = [market, *market.get("themes", [])]
    scopes.extend(
        driver
        for entry in artifact.get("instruments", [])
        for driver in entry.get("drivers", [])
    )
    return [
        [str(cid) for cid in scope.get("citations", [])]
        for scope in scopes
        if isinstance(scope, dict)
    ]


def compute_metrics(
    artifact: dict[str, Any],
    analysis: dict[str, Any],
    evidence: dict[str, Any],
) -> dict[str, Any]:
    """Recompute validator and gate outcomes into structural metrics."""
    errors = validate_artifact(artifact, analysis=analysis, evidence=evidence)
    gated = apply_gates(artifact, analysis, evidence)
    instruments = gated.get("instruments", [])
    total = len(instruments)
    gated_count = sum(1 for entry in instruments if entry.get("qualitative_gates"))
    stance_counts = {
        stance: sum(1 for e in instruments if e.get("stance") == stance)
        for stance in _STANCES
    }
    confidence_counts = {
        confidence: sum(1 for e in instruments if e.get("confidence") == confidence)
        for confidence in _CONFIDENCES
    }
    item_ids = {str(item.get("id")) for item in evidence.get("items", [])}
    scopes = _citation_scopes(gated)
    covered = sum(1 for cites in scopes if any(cid in item_ids for cid in cites))
    cited = {cid for cites in scopes for cid in cites if cid in item_ids}
    gates = gated["metadata"]["gates"]
    return {
        "validation_errors": len(errors),
        "instruments": total,
        "instruments_gated": gated_count,
        "instrument_gate_pass_rate": round((total - gated_count) / total, _ROUND_DIGITS)
        if total
        else None,
        "market_narrative_withheld": bool(gates["market_narrative_withheld"]),
        "market_gates": [str(g) for g in gates["market_gates"]],
        "stance_distribution": stance_counts,
        "confidence_distribution": confidence_counts,
        "themes": len(artifact.get("market", {}).get("themes", [])),
        "drivers": sum(len(e.get("drivers", [])) for e in instruments),
        "citation_coverage": round(covered / len(scopes), _ROUND_DIGITS)
        if scopes
        else None,
        "distinct_evidence_cited": len(cited),
        "evidence_items": len(item_ids),
        "narrative_chars": len(str(artifact.get("market", {}).get("narrative", ""))),
    }


def run_checks(
    metrics: dict[str, Any],
    *,
    min_gate_pass_rate: float = DEFAULT_MIN_GATE_PASS_RATE,
    min_citation_coverage: float = DEFAULT_MIN_CITATION_COVERAGE,
) -> dict[str, bool]:
    """Assert structural and gate thresholds; never exact prose."""
    pass_rate = metrics["instrument_gate_pass_rate"]
    coverage = metrics["citation_coverage"]
    stance_counts: dict[str, int] = metrics["stance_distribution"]
    total = metrics["instruments"]
    return {
        "validation_clean": metrics["validation_errors"] == 0,
        "market_narrative_rendered": not metrics["market_narrative_withheld"],
        "instrument_gate_pass_rate": pass_rate is not None
        and pass_rate >= min_gate_pass_rate,
        "citation_coverage": coverage is not None and coverage >= min_citation_coverage,
        "stance_distribution_sane": total < 3 or max(stance_counts.values()) < total,
    }


def build_entry(
    artifact: dict[str, Any],
    artifact_path: Path,
    metrics: dict[str, Any],
    checks: dict[str, bool],
    prompt_sha256: str,
) -> dict[str, Any]:
    """One recorded harness run for the currently configured prompt and model."""
    meta = artifact.get("metadata", {})
    return {
        "analysis_date": str(meta.get("analysis_date", "")),
        "artifact": artifact_path.as_posix(),
        "artifact_provenance": {
            "model_id": str(meta.get("model_id", "")),
            "prompt_version": str(meta.get("prompt_version", "")),
            "prompt_sha256": str(meta.get("prompt_sha256", "")),
        },
        "model_id": MODEL_ID,
        "prompt_version": PROMPT_VERSION,
        "prompt_sha256": prompt_sha256,
        "metrics": metrics,
        "checks": checks,
        "passed": all(checks.values()),
    }


def _entry_key(entry: dict[str, Any]) -> tuple[str, str, str, str, str]:
    return (
        str(entry.get("prompt_version", "")),
        str(entry.get("prompt_sha256", "")),
        str(entry.get("model_id", "")),
        str(entry.get("analysis_date", "")),
        str(entry.get("artifact", "")),
    )


def record_entry(entry: dict[str, Any], record_path: Path) -> None:
    """Insert or replace the entry in the version-history file, sorted."""
    if record_path.exists():
        with record_path.open(encoding="utf-8") as stream:
            history: dict[str, Any] = json.load(stream)
        entries = history.get("entries")
        if history.get("version") != PROMPT_REGRESSION_VERSION or not isinstance(
            entries, list
        ):
            msg = f"{record_path} is not a valid prompt-regression history file"
            raise ValueError(msg)
    else:
        history = {"version": PROMPT_REGRESSION_VERSION, "entries": []}
        entries = history["entries"]
    kept = [e for e in entries if _entry_key(e) != _entry_key(entry)]
    kept.append(entry)
    history["entries"] = sorted(kept, key=_entry_key)
    record_path.parent.mkdir(parents=True, exist_ok=True)
    record_path.write_text(
        json.dumps(history, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifact", type=Path, required=True)
    parser.add_argument("--analysis", type=Path, required=True)
    parser.add_argument("--evidence", type=Path, required=True)
    parser.add_argument(
        "--prompt",
        type=Path,
        default=DEFAULT_PROMPT_PATH,
        help="Committed prompt file whose SHA-256 keys the recorded entry",
    )
    parser.add_argument(
        "--record",
        type=Path,
        default=None,
        help=f"History file to record into (e.g. {DEFAULT_RECORD_PATH})",
    )
    parser.add_argument(
        "--min-gate-pass-rate", type=float, default=DEFAULT_MIN_GATE_PASS_RATE
    )
    parser.add_argument(
        "--min-citation-coverage", type=float, default=DEFAULT_MIN_CITATION_COVERAGE
    )
    return parser.parse_args(argv)


def _load(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        value: dict[str, Any] = json.load(stream)
    return value


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        artifact = _load(args.artifact)
        analysis = _load(args.analysis)
        evidence = _load(args.evidence)
        prompt_sha256 = sha256_file(args.prompt)
    except FileNotFoundError as exc:
        print(f"ERROR: file not found: {exc.filename}")
        return 1
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON: {exc}")
        return 1
    metrics = compute_metrics(artifact, analysis, evidence)
    checks = run_checks(
        metrics,
        min_gate_pass_rate=args.min_gate_pass_rate,
        min_citation_coverage=args.min_citation_coverage,
    )
    print(json.dumps(metrics, indent=2, sort_keys=True))
    for name in sorted(checks):
        print(f"{'PASS' if checks[name] else 'FAIL'}: {name}")
    entry = build_entry(artifact, args.artifact, metrics, checks, prompt_sha256)
    if args.record is not None:
        try:
            record_entry(entry, args.record)
        except (json.JSONDecodeError, ValueError) as exc:
            print(f"ERROR: {exc}")
            return 1
        print(f"Recorded prompt-regression entry in {args.record}")
    return 0 if entry["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
