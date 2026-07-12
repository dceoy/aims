r"""Validate an AIMS qualitative analysis artifact against the #89 contract.

Hand-rolled validator following the ``validate_analysis.py`` pattern (no
``jsonschema`` dependency). The format reference is
``data/schema/qualitative.schema.json``. Beyond shape and enums, this module
enforces the grounding rules: citations must exist in the evidence bundle,
instrument entries must stay within the analysis top-K, and free text may not
contain numeric tokens undeclared in ``numeric_claims``.

Usage:
    uv run .agents/skills/qualitative-analysis/scripts/validate_qualitative.py \
        --input data/qualitative/2026-07-04.json \
        --analysis data/analysis/2026-07-04.json \
        --evidence data/evidence/2026-07-04.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Final

QUALITATIVE_VERSION: Final[str] = "1.0.0"

NARRATIVE_MAX_CHARS: Final[int] = 1200
DRIVER_TEXT_MAX_CHARS: Final[int] = 300
THEME_TITLE_MAX_CHARS: Final[int] = 120
MAX_THEMES: Final[int] = 5
MAX_DRIVERS_PER_INSTRUMENT: Final[int] = 4
MAX_CITATIONS_PER_DRIVER: Final[int] = 6
DEFAULT_TOP_K: Final[int] = 5

STANCES: Final[frozenset[str]] = frozenset({"supportive", "neutral", "conflicting"})
CONFIDENCES: Final[frozenset[str]] = frozenset({"low", "medium", "high"})
DIRECTIONS: Final[frozenset[str]] = frozenset({"up", "down", "none"})
WINDOWS: Final[frozenset[str]] = frozenset({"1d", "5d", "20d", "60d"})
UNITS: Final[frozenset[str]] = frozenset({"percent", "price", "count", "other"})

FEATURE_NAMES: Final[frozenset[str]] = frozenset({
    "ret_1d",
    "ret_5d",
    "ret_20d",
    "ret_60d",
    "ma20_dist",
    "ma50_dist",
    "vol_20d",
    "mdd_60d",
    "rsi_14",
    "zscore_20d",
})

_REQUIRED_TOP: Final[tuple[str, ...]] = ("version", "metadata", "market", "instruments")
_REQUIRED_META: Final[tuple[str, ...]] = (
    "generated_at",
    "analysis_date",
    "interval",
    "git_commit",
    "model_id",
    "prompt_version",
    "prompt_sha256",
    "execution_type",
    "action_revision",
    "input_hashes",
)
_REQUIRED_HASHES: Final[tuple[str, ...]] = ("analysis_sha256", "evidence_sha256")
_REQUIRED_MARKET: Final[tuple[str, ...]] = ("narrative", "citations", "themes")
_REQUIRED_INSTRUMENT: Final[tuple[str, ...]] = (
    "canonical_id",
    "symbol",
    "stance",
    "confidence",
    "drivers",
)

# Numeric tokens matching these patterns are display conventions, not claims:
# ISO dates, bare years, window phrases like "20-day", indicator names like
# "MA20"/"RSI14", quarter labels, and the quantitative feature names.
_WHITELIST_PATTERNS: Final[tuple[str, ...]] = (
    r"\d{4}-\d{2}-\d{2}",
    r"\b\d+(?:\.\d+)?-(?:day|week|month|year)\b",
    (
        r"\b(?:ret_1d|ret_5d|ret_20d|ret_60d|ma20_dist|ma50_dist"
        r"|vol_20d|mdd_60d|rsi_14|zscore_20d)\b"
    ),
    r"\b(?:MA|RSI|EMA)\s?\d+\b",
    r"\bQ[1-4]\b",
    r"\b(?:19|20)\d{2}\b",
)
_WHITELIST_RE: Final[re.Pattern[str]] = re.compile(
    "|".join(_WHITELIST_PATTERNS), re.IGNORECASE
)
_NUM_RE: Final[re.Pattern[str]] = re.compile(r"[-+]?\d+(?:\.\d+)?")
_SHA256_RE: Final[re.Pattern[str]] = re.compile(r"^[0-9a-f]{64}$")
_MATCH_TOLERANCE: Final[float] = 1e-6


def sha256_file(path: Path) -> str:
    """Return the SHA-256 hex digest of *path*'s bytes."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _declared_values(claims: list[Any]) -> list[float]:
    return [
        float(claim["value"])
        for claim in claims
        if isinstance(claim, dict) and isinstance(claim.get("value"), (int, float))
    ]


def instrument_name_numbers(analysis: dict[str, Any] | None) -> frozenset[str]:
    """Return numeric tokens embedded in the universe's instrument names.

    Many canonical display names carry a number that is part of the proper
    name, not a market claim (e.g. "S&P 500", "NASDAQ 100", "Nikkei 225",
    "Euro Stoxx 50", "FTSE 100", "CAC 40", "Russell 2000"). Free text that
    mentions one of these instruments must not be rejected as an undeclared
    numeric claim for reciting the name.
    """
    if analysis is None:
        return frozenset()
    numbers: set[str] = set()
    for inst in analysis.get("instruments", []):
        display_name = inst.get("display_name")
        if isinstance(display_name, str):
            numbers.update(_NUM_RE.findall(display_name))
    return frozenset(numbers)


def undeclared_numbers(
    text: str,
    claims: list[Any],
    whitelisted_numbers: frozenset[str] = frozenset(),
) -> list[str]:
    """Return numeric tokens in *text* not declared in *claims*.

    Whitelisted display conventions (dates, years, window phrases,
    indicator/feature names) are stripped before scanning; numbers
    matching *whitelisted_numbers* (e.g. instrument-name numerals from
    ``instrument_name_numbers``) are also exempt.
    """
    declared = _declared_values(claims)
    whitelisted = {float(n) for n in whitelisted_numbers}
    cleaned = _WHITELIST_RE.sub(" ", text)
    return [
        token
        for token in _NUM_RE.findall(cleaned)
        if float(token) not in whitelisted
        and not any(abs(float(token) - value) <= _MATCH_TOLERANCE for value in declared)
    ]


def _validate_numeric_claims(where: str, claims: Any) -> list[str]:
    if not isinstance(claims, list):
        return [f"{where}: numeric_claims must be a JSON array"]
    errors: list[str] = []
    for idx, claim in enumerate(claims):
        label = f"{where}.numeric_claims[{idx}]"
        if not isinstance(claim, dict):
            errors.append(f"{label} must be a JSON object")
            continue
        if not isinstance(claim.get("value"), (int, float)) or isinstance(
            claim.get("value"), bool
        ):
            errors.append(f"{label}: 'value' must be a number")
        if claim.get("unit") not in UNITS:
            errors.append(f"{label}: unit {claim.get('unit')!r} is not valid")
        refers_to = claim.get("refers_to")
        if not isinstance(refers_to, str) or not refers_to:
            errors.append(f"{label}: 'refers_to' must be a non-empty string")
    return errors


def _validate_citations(
    where: str,
    citations: Any,
    evidence_ids: frozenset[str] | None,
    max_citations: int | None = None,
) -> list[str]:
    if (
        not isinstance(citations, list)
        or not citations
        or any(not isinstance(entry, str) for entry in citations)
    ):
        return [f"{where}: citations must be a non-empty list of evidence IDs"]
    errors: list[str] = []
    if max_citations is not None and len(citations) > max_citations:
        errors.append(f"{where}: more than {max_citations} citations")
    if evidence_ids is not None:
        errors.extend(
            f"{where}: citation {cid!r} is not in the evidence bundle"
            for cid in citations
            if cid not in evidence_ids
        )
    return errors


def _validate_free_text(
    where: str,
    text: str,
    claims: Any,
    whitelisted_numbers: frozenset[str],
) -> list[str]:
    claim_list = claims if isinstance(claims, list) else []
    return [
        f"{where}: numeric token {token!r} in free text is not declared"
        " in numeric_claims"
        for token in undeclared_numbers(text, claim_list, whitelisted_numbers)
    ]


def _validate_direction_claim(where: str, claim: Any) -> list[str]:
    if not isinstance(claim, dict):
        return [f"{where}: direction_claim must be a JSON object"]
    errors: list[str] = []
    if claim.get("direction") not in DIRECTIONS:
        errors.append(
            f"{where}: direction {claim.get('direction')!r} is not one of up/down/none"
        )
    if claim.get("window") not in WINDOWS:
        errors.append(f"{where}: window {claim.get('window')!r} is not valid")
    return errors


def _validate_driver(
    where: str,
    driver: Any,
    evidence_ids: frozenset[str] | None,
    whitelisted_numbers: frozenset[str],
) -> list[str]:
    if not isinstance(driver, dict):
        return [f"{where} must be a JSON object"]
    errors: list[str] = []
    text = driver.get("text")
    if not isinstance(text, str) or not text.strip():
        errors.append(f"{where}: 'text' must be a non-empty string")
        text = ""
    elif len(text) > DRIVER_TEXT_MAX_CHARS:
        errors.append(f"{where}: text exceeds {DRIVER_TEXT_MAX_CHARS} characters")
    errors.extend(
        _validate_citations(
            where, driver.get("citations"), evidence_ids, MAX_CITATIONS_PER_DRIVER
        )
    )
    if "direction_claim" in driver:
        errors.extend(_validate_direction_claim(where, driver["direction_claim"]))
    if "numeric_claims" in driver:
        errors.extend(_validate_numeric_claims(where, driver["numeric_claims"]))
    errors.extend(
        _validate_free_text(
            where, text, driver.get("numeric_claims", []), whitelisted_numbers
        )
    )
    return errors


def _validate_market(
    market: Any,
    evidence_ids: frozenset[str] | None,
    whitelisted_numbers: frozenset[str],
) -> list[str]:
    if not isinstance(market, dict):
        return ["'market' must be a JSON object"]
    errors = [
        f"market missing required key: {key!r}"
        for key in _REQUIRED_MARKET
        if key not in market
    ]
    if errors:
        return errors
    narrative = market["narrative"]
    if not isinstance(narrative, str) or not narrative.strip():
        errors.append("market.narrative must be a non-empty string")
        narrative = ""
    elif len(narrative) > NARRATIVE_MAX_CHARS:
        errors.append(f"market.narrative exceeds {NARRATIVE_MAX_CHARS} characters")
    errors.extend(_validate_citations("market", market["citations"], evidence_ids))
    if "numeric_claims" in market:
        errors.extend(_validate_numeric_claims("market", market["numeric_claims"]))
    errors.extend(
        _validate_free_text(
            "market", narrative, market.get("numeric_claims", []), whitelisted_numbers
        )
    )

    themes = market["themes"]
    if not isinstance(themes, list):
        errors.append("market.themes must be a JSON array")
        return errors
    if len(themes) > MAX_THEMES:
        errors.append(f"market.themes has more than {MAX_THEMES} entries")
    for idx, theme in enumerate(themes):
        where = f"market.themes[{idx}]"
        if not isinstance(theme, dict):
            errors.append(f"{where} must be a JSON object")
            continue
        title = theme.get("title")
        if not isinstance(title, str) or not title.strip():
            errors.append(f"{where}: 'title' must be a non-empty string")
            title = ""
        elif len(title) > THEME_TITLE_MAX_CHARS:
            errors.append(f"{where}: title exceeds {THEME_TITLE_MAX_CHARS} characters")
        errors.extend(_validate_citations(where, theme.get("citations"), evidence_ids))
        if "numeric_claims" in theme:
            errors.extend(_validate_numeric_claims(where, theme["numeric_claims"]))
        errors.extend(
            _validate_free_text(
                where, title, theme.get("numeric_claims", []), whitelisted_numbers
            )
        )
    return errors


def _top_k_instruments(analysis: dict[str, Any], top_k: int) -> dict[str, str]:
    """Return {canonical_id: symbol} for reliable analysis rows in the top K."""
    result: dict[str, str] = {}
    for inst in analysis.get("instruments", []):
        if (
            inst.get("is_reliable")
            and isinstance(inst.get("rank"), int)
            and inst["rank"] <= top_k
            and inst.get("canonical_id")
        ):
            result[str(inst["canonical_id"])] = str(inst.get("symbol", ""))
    return result


def _validate_instruments(
    instruments: Any,
    evidence_ids: frozenset[str] | None,
    allowed: dict[str, str] | None,
    top_k: int,
    whitelisted_numbers: frozenset[str],
) -> list[str]:
    if not isinstance(instruments, list):
        return ["'instruments' must be a JSON array"]
    errors: list[str] = []
    if len(instruments) > top_k:
        errors.append(f"instruments has more than top-K={top_k} entries")
    seen: set[str] = set()
    for idx, inst in enumerate(instruments):
        where = f"instruments[{idx}]"
        if not isinstance(inst, dict):
            errors.append(f"{where} must be a JSON object")
            continue
        missing = [key for key in _REQUIRED_INSTRUMENT if key not in inst]
        if missing:
            errors.extend(f"{where} missing required key: {key!r}" for key in missing)
            continue
        canonical_id = str(inst["canonical_id"])
        if canonical_id in seen:
            errors.append(f"{where}: duplicate canonical_id {canonical_id!r}")
        seen.add(canonical_id)
        if allowed is not None:
            if canonical_id not in allowed:
                errors.append(
                    f"{where}: canonical_id {canonical_id!r} is not a top-{top_k}"
                    " reliable signal in the analysis artifact"
                )
            elif str(inst["symbol"]) != allowed[canonical_id]:
                errors.append(
                    f"{where}: symbol {inst['symbol']!r} does not match the"
                    f" analysis symbol {allowed[canonical_id]!r}"
                )
        if inst["stance"] not in STANCES:
            errors.append(f"{where}: stance {inst['stance']!r} is not valid")
        if inst["confidence"] not in CONFIDENCES:
            errors.append(f"{where}: confidence {inst['confidence']!r} is not valid")
        drivers = inst["drivers"]
        if not isinstance(drivers, list) or not drivers:
            errors.append(f"{where}: drivers must be a non-empty JSON array")
            continue
        if len(drivers) > MAX_DRIVERS_PER_INSTRUMENT:
            errors.append(f"{where}: more than {MAX_DRIVERS_PER_INSTRUMENT} drivers")
        for didx, driver in enumerate(drivers):
            errors.extend(
                _validate_driver(
                    f"{where}.drivers[{didx}]",
                    driver,
                    evidence_ids,
                    whitelisted_numbers,
                )
            )
    return errors


def validate_artifact(
    data: dict[str, Any],
    *,
    analysis: dict[str, Any] | None = None,
    evidence: dict[str, Any] | None = None,
    top_k: int = DEFAULT_TOP_K,
) -> list[str]:
    """Validate shape, enums, caps, and grounding of a qualitative artifact.

    When *analysis* is provided, instrument entries are checked against the
    analysis top-K; when *evidence* is provided, every citation must exist in
    the bundle and the analysis dates must line up.
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

    metadata = data["metadata"]
    if not isinstance(metadata, dict):
        errors.append("'metadata' must be a JSON object")
    else:
        errors.extend(
            f"metadata missing required key: {key!r}"
            for key in _REQUIRED_META
            if key not in metadata
        )
        hashes = metadata.get("input_hashes")
        if isinstance(hashes, dict):
            errors.extend(
                f"metadata.input_hashes missing required key: {key!r}"
                for key in _REQUIRED_HASHES
                if key not in hashes
            )
            errors.extend(
                f"metadata.input_hashes.{key}: {hashes[key]!r} is not a"
                " SHA-256 hex digest"
                for key in _REQUIRED_HASHES
                if isinstance(hashes.get(key), str)
                and not _SHA256_RE.match(hashes[key])
            )
        elif "input_hashes" in metadata:
            errors.append("metadata.input_hashes must be a JSON object")
        prompt_sha = metadata.get("prompt_sha256")
        if isinstance(prompt_sha, str) and not _SHA256_RE.match(prompt_sha):
            errors.append(
                f"metadata.prompt_sha256 {prompt_sha!r} is not a SHA-256 hex digest"
            )
        if analysis is not None:
            analysis_gen = str(analysis.get("metadata", {}).get("generated_at", ""))[
                :10
            ]
            if metadata.get("analysis_date") != analysis_gen:
                errors.append(
                    f"metadata.analysis_date {metadata.get('analysis_date')!r} does"
                    f" not match the analysis artifact date {analysis_gen!r}"
                )

    evidence_ids: frozenset[str] | None = None
    if evidence is not None:
        evidence_ids = frozenset(
            str(item.get("id", "")) for item in evidence.get("items", [])
        )
    allowed = _top_k_instruments(analysis, top_k) if analysis is not None else None
    whitelisted_numbers = instrument_name_numbers(analysis)

    errors.extend(_validate_market(data["market"], evidence_ids, whitelisted_numbers))
    errors.extend(
        _validate_instruments(
            data["instruments"], evidence_ids, allowed, top_k, whitelisted_numbers
        )
    )
    return errors


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help="Path to qualitative artifact JSON file",
    )
    parser.add_argument(
        "--analysis",
        type=Path,
        default=None,
        help="Analysis artifact for top-K and input-hash cross-checks",
    )
    parser.add_argument(
        "--evidence",
        type=Path,
        default=None,
        help="Evidence bundle for citation and input-hash cross-checks",
    )
    parser.add_argument("--top-k", type=int, default=DEFAULT_TOP_K)
    return parser.parse_args(argv)


def _load(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as fh:
        value: dict[str, Any] = json.load(fh)
    return value


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        data = _load(args.input)
        analysis = _load(args.analysis) if args.analysis else None
        evidence = _load(args.evidence) if args.evidence else None
    except FileNotFoundError as exc:
        print(f"ERROR: file not found: {exc.filename}")
        return 1
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON: {exc}")
        return 1
    errors = validate_artifact(
        data, analysis=analysis, evidence=evidence, top_k=args.top_k
    )
    hashes = data.get("metadata", {}).get("input_hashes", {})
    if args.analysis and hashes.get("analysis_sha256") != sha256_file(args.analysis):
        errors.append(
            "metadata.input_hashes.analysis_sha256 does not match the"
            f" analysis artifact at {args.analysis}"
        )
    if args.evidence and hashes.get("evidence_sha256") != sha256_file(args.evidence):
        errors.append(
            "metadata.input_hashes.evidence_sha256 does not match the"
            f" evidence bundle at {args.evidence}"
        )
    if errors:
        for error in errors:
            print(error)
        return 1
    print(f"validated {args.input}: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
