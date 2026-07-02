from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

import pytest

if TYPE_CHECKING:
    from pathlib import Path
    from types import ModuleType

import aims.history as _aims_history


@pytest.fixture(scope="module")
def gh() -> ModuleType:
    return _aims_history


def _artifact(date: str, rows: list[dict[str, Any]]) -> dict[str, Any]:
    instruments = []
    for rank, row in enumerate(rows, 1):
        instruments.append({
            "symbol": row["symbol"],
            "rank": row.get("rank", rank),
            "score": row.get("score", 100 - rank),
            "is_reliable": row.get("reliable", True),
            "risk_gates": row.get("gates", []),
        })
    return {
        "metadata": {
            "generated_at": f"{date}T00:00:00+00:00",
            "config": {"interval": "d"},
        },
        "instruments": instruments,
    }


def test_first_artifact(gh: ModuleType) -> None:
    result = gh.build_history([_artifact("2024-01-01", [{"symbol": "A"}])], 1)
    assert result["previous_analysis_date"] is None
    assert result["instruments"][0]["previous_rank"] is None
    assert result["instruments"][0]["new_top_k"] is False
    assert result["instruments"][0]["consecutive_reliable_reports"] == 1
    assert result["universe_size"] == 1
    assert result["previous_universe_size"] is None


def test_changes_persistence_and_missing_date(gh: ModuleType) -> None:
    old = _artifact(
        "2024-01-01",
        [
            {"symbol": "A", "score": 80, "gates": ["stale_data"]},
            {"symbol": "B", "score": 70},
            {"symbol": "C", "score": 60},
        ],
    )
    current = _artifact(
        "2024-01-03",
        [
            {"symbol": "B", "score": 85},
            {"symbol": "C", "score": 72},
            {"symbol": "A", "score": 65, "gates": ["high_volatility"]},
            {"symbol": "D", "score": 50},
        ],
    )
    result = gh.build_history([current, old], 2)
    rows = {row["symbol"]: row for row in result["instruments"]}
    assert result["previous_analysis_date"] == "2024-01-01"
    assert result["universe_size"] == 4
    assert result["previous_universe_size"] == 3
    assert rows["B"]["rank_delta"] == 1
    assert rows["B"]["score_delta"] == 15
    assert rows["B"]["consecutive_top_k_reports"] == 2
    assert rows["C"]["new_top_k"] is True
    assert rows["A"]["risk_gates_added"] == ["high_volatility"]
    assert rows["A"]["risk_gates_removed"] == ["stale_data"]
    assert rows["D"]["previous_score"] is None
    assert result["dropped_from_top_k"] == ["A"]


def test_unreliable_breaks_streak(gh: ModuleType) -> None:
    artifacts = [
        _artifact("2024-01-01", [{"symbol": "A"}]),
        _artifact("2024-01-02", [{"symbol": "A", "reliable": False}]),
        _artifact("2024-01-03", [{"symbol": "A"}]),
    ]
    row = gh.build_history(artifacts, 1)["instruments"][0]
    assert row["consecutive_reliable_reports"] == 1
    assert row["consecutive_top_k_reports"] == 1


@pytest.mark.parametrize(
    ("artifacts", "top_k", "message"),
    [([], 1, "at least one"), ([{}], 0, "top_k"), ([{}], 1, "generated_at")],
)
def test_invalid_input(
    gh: ModuleType,
    artifacts: list[dict[str, Any]],
    top_k: int,
    message: str,
) -> None:
    exception = TypeError if message == "generated_at" else ValueError
    with pytest.raises(exception, match=message):
        gh.build_history(artifacts, top_k)


def test_invalid_instruments_and_duplicate_dates(gh: ModuleType) -> None:
    bad = {
        "metadata": {
            "generated_at": "2024-01-01T00:00:00Z",
            "config": {"interval": "d"},
        }
    }
    with pytest.raises(TypeError, match="instruments"):
        gh.build_history([bad])
    artifact = _artifact("2024-01-01", [])
    with pytest.raises(ValueError, match="unique"):
        gh.build_history([artifact, artifact])


def test_invalid_or_mixed_intervals(gh: ModuleType) -> None:
    invalid = _artifact("2024-01-01", [])
    invalid["metadata"]["config"]["interval"] = "h"
    with pytest.raises(ValueError, match=r"config\.interval"):
        gh.build_history([invalid])
    daily = _artifact("2024-01-01", [])
    weekly = _artifact("2024-01-02", [])
    weekly["metadata"]["config"]["interval"] = "w"
    with pytest.raises(ValueError, match="same interval"):
        gh.build_history([daily, weekly])


def test_generate_history_and_main(gh: ModuleType, tmp_path: Path) -> None:
    analysis = tmp_path / "analysis"
    analysis.mkdir()
    old_path = analysis / "2024-01-01.json"
    current_path = analysis / "2024-01-03.json"
    future_path = analysis / "2024-01-04.json"
    weekly_path = analysis / "2024-01-02.json"
    old_path.write_text(json.dumps(_artifact("2024-01-01", [{"symbol": "A"}])))
    current_path.write_text(json.dumps(_artifact("2024-01-03", [{"symbol": "A"}])))
    future_path.write_text(json.dumps(_artifact("2024-01-04", [{"symbol": "A"}])))
    weekly = _artifact("2024-01-02", [{"symbol": "B"}])
    weekly["metadata"]["config"]["interval"] = "w"
    weekly_path.write_text(json.dumps(weekly))
    output = tmp_path / "history"
    result = gh.generate_history(current_path, analysis, output, 1)
    assert result == output / "2024-01-03.json"
    assert json.loads(result.read_text())["previous_analysis_date"] == "2024-01-01"
    assert (
        gh.main([
            "--input",
            str(current_path),
            "--analysis-dir",
            str(analysis),
            "--output",
            str(output),
        ])
        == 0
    )
    assert gh.main(["--input", str(tmp_path / "missing.json")]) == 1


def test_main_bad_json(gh: ModuleType, tmp_path: Path) -> None:
    bad = tmp_path / "bad.json"
    bad.write_text("{")
    assert gh.main(["--input", str(bad)]) == 1
