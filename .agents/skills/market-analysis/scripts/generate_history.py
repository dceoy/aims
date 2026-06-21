#!/usr/bin/env python3
"""Generate deterministic score-history artifacts from saved analyses."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Final

HISTORY_VERSION: Final[str] = "1.0.0"
DEFAULT_TOP_K: Final[int] = 5


def _load(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        value: dict[str, Any] = json.load(stream)
    return value


def _date(artifact: dict[str, Any]) -> str:
    generated_at = artifact.get("metadata", {}).get("generated_at")
    if not isinstance(generated_at, str) or len(generated_at) < 10:
        msg = "analysis artifact has no valid metadata.generated_at"
        raise TypeError(msg)
    return generated_at[:10]


def _interval(artifact: dict[str, Any]) -> str:
    interval = artifact.get("metadata", {}).get("config", {}).get("interval")
    if interval not in {"d", "w", "m"}:
        msg = "analysis artifact has no valid metadata.config.interval"
        raise ValueError(msg)
    return str(interval)


def _by_symbol(artifact: dict[str, Any]) -> dict[str, dict[str, Any]]:
    instruments = artifact.get("instruments")
    if not isinstance(instruments, list):
        msg = "analysis artifact has no valid instruments list"
        raise TypeError(msg)
    return {str(item["symbol"]): item for item in instruments}


def _top_symbols(artifact: dict[str, Any], top_k: int) -> set[str]:
    return {
        str(item["symbol"])
        for item in artifact["instruments"]
        if item.get("is_reliable") and int(item["rank"]) <= top_k
    }


def build_history(
    artifacts: list[dict[str, Any]], top_k: int = DEFAULT_TOP_K
) -> dict[str, Any]:
    if top_k < 1:
        msg = "top_k must be at least 1"
        raise ValueError(msg)
    if not artifacts:
        msg = "at least one analysis artifact is required"
        raise ValueError(msg)
    ordered = sorted(artifacts, key=_date)
    intervals = {_interval(artifact) for artifact in ordered}
    if len(intervals) != 1:
        msg = "analysis artifacts must use the same interval"
        raise ValueError(msg)
    dates = [_date(item) for item in ordered]
    if len(set(dates)) != len(dates):
        msg = "analysis dates must be unique"
        raise ValueError(msg)
    current = ordered[-1]
    previous = ordered[-2] if len(ordered) > 1 else None
    current_items = _by_symbol(current)
    previous_items = _by_symbol(previous) if previous else {}
    current_top = _top_symbols(current, top_k)
    previous_top = _top_symbols(previous, top_k) if previous else set()

    rows: list[dict[str, Any]] = []
    for symbol, item in sorted(
        current_items.items(), key=lambda pair: (int(pair[1]["rank"]), pair[0])
    ):
        old = previous_items.get(symbol)
        current_gates = sorted(str(gate) for gate in item.get("risk_gates", []))
        old_gates = (
            sorted(str(gate) for gate in old.get("risk_gates", [])) if old else []
        )
        reliable_days = 0
        top_days = 0
        for artifact in reversed(ordered):
            historical = _by_symbol(artifact).get(symbol)
            if historical is None or not historical.get("is_reliable"):
                break
            reliable_days += 1
        for artifact in reversed(ordered):
            if symbol not in _top_symbols(artifact, top_k):
                break
            top_days += 1
        old_rank = int(old["rank"]) if old else None
        old_score = float(old["score"]) if old else None
        score = float(item["score"])
        rank = int(item["rank"])
        rows.append({
            "symbol": symbol,
            "current_rank": rank,
            "previous_rank": old_rank,
            "rank_delta": old_rank - rank if old_rank is not None else None,
            "current_score": score,
            "previous_score": old_score,
            "score_delta": round(score - old_score, 6)
            if old_score is not None
            else None,
            "is_reliable": bool(item.get("is_reliable")),
            "new_top_k": previous is not None and symbol in current_top - previous_top,
            "consecutive_reliable_reports": reliable_days,
            "consecutive_top_k_reports": top_days,
            "risk_gates_added": sorted(set(current_gates) - set(old_gates)),
            "risk_gates_removed": sorted(set(old_gates) - set(current_gates)),
        })
    dropped = sorted(previous_top - current_top) if previous else []
    return {
        "version": HISTORY_VERSION,
        "analysis_date": dates[-1],
        "previous_analysis_date": dates[-2] if previous else None,
        "top_k": top_k,
        "instruments": rows,
        "dropped_from_top_k": dropped,
    }


def generate_history(
    current_path: Path, analysis_dir: Path, output_dir: Path, top_k: int
) -> Path:
    current = _load(current_path)
    current_date = _date(current)
    current_interval = _interval(current)
    paths = sorted(
        path
        for path in analysis_dir.glob("*.json")
        if path.stem <= current_date and path.resolve() != current_path.resolve()
    )
    artifacts = [
        artifact
        for path in paths
        if _interval(artifact := _load(path)) == current_interval
    ]
    artifacts.append(current)
    history = build_history(artifacts, top_k)
    output_dir.mkdir(parents=True, exist_ok=True)
    output = output_dir / f"{current_date}.json"
    output.write_text(
        json.dumps(history, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"History written to {output}")
    return output


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--analysis-dir", default=Path("data/analysis"), type=Path)
    parser.add_argument("--output", default=Path("data/history"), type=Path)
    parser.add_argument("--top-k", default=DEFAULT_TOP_K, type=int)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        generate_history(args.input, args.analysis_dir, args.output, args.top_k)
    except (
        FileNotFoundError,
        json.JSONDecodeError,
        KeyError,
        TypeError,
        ValueError,
    ) as exc:
        print(f"ERROR: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
