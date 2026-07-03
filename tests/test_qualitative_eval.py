from __future__ import annotations

import json
from datetime import UTC, datetime, timedelta
from typing import TYPE_CHECKING, Any

import pytest

import aims.qualitative_eval as qe
from aims.market_analysis import OhlcvBar, save_ohlcv

if TYPE_CHECKING:
    from pathlib import Path

    from pytest_mock import MockerFixture


def _write_prices(prices_dir: Path, symbol: str, closes: list[float]) -> None:
    start = datetime(2024, 1, 1, tzinfo=UTC)
    bars = [
        OhlcvBar(
            symbol=symbol,
            timestamp=start + timedelta(days=i),
            open=c,
            high=c,
            low=c,
            close=c,
            volume=1000.0,
            source="csv",
            interval="d",
        )
        for i, c in enumerate(closes)
    ]
    save_ohlcv(bars, prices_dir)


def _entry(
    symbol: str,
    stance: str,
    confidence: str = "medium",
    gates: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "canonical_id": symbol.strip("^").lower(),
        "symbol": symbol,
        "stance": stance,
        "confidence": confidence,
        "drivers": [],
        "gates": gates or [],
    }


def _artifact(analysis_date: str, entries: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "version": "1.0.0",
        "metadata": {"analysis_date": analysis_date},
        "instruments": entries,
    }


@pytest.fixture
def prices_dir(tmp_path: Path) -> Path:
    directory = tmp_path / "prices"
    _write_prices(directory, "^SPX", [100, 102, 104, 106, 108, 110])
    _write_prices(directory, "^DJI", [100, 99, 98, 97, 96, 95])
    return directory


def test_evaluate_stances_hits(prices_dir: Path) -> None:
    artifact = _artifact(
        "2024-01-01",
        [
            _entry("^SPX", "supportive", "high"),
            _entry("^DJI", "conflicting", "low"),
            _entry("^NDX", "neutral"),
            _entry("^SPX", "conflicting", gates=["stale_evidence"]),
            _entry("^MISSING", "supportive"),
        ],
    )
    result = qe.evaluate_stances([artifact], prices_dir=prices_dir, horizons=(1, 2))
    assert result["version"] == qe.EVALUATION_VERSION
    assert result["metadata"]["evaluated_dates"] == ["2024-01-01"]
    assert result["metadata"]["generated_at"] == "2024-01-01"
    for horizon in ("1d", "2d"):
        metrics = result["metrics"][horizon]
        assert metrics["supportive"] == {
            "count": 1,
            "hit_rate": 1.0,
            "mean_excess_return": metrics["supportive"]["mean_excess_return"],
        }
        assert metrics["supportive"]["mean_excess_return"] > 0
        assert metrics["conflicting"]["hit_rate"] == 1.0
        assert metrics["by_confidence"]["high"]["count"] == 1
        assert metrics["by_confidence"]["medium"]["count"] == 0
        assert metrics["by_confidence"]["medium"]["hit_rate"] is None
    assert qe.validate_evaluation(result) == []


def test_evaluate_stances_misses(prices_dir: Path) -> None:
    artifact = _artifact(
        "2024-01-01",
        [
            _entry("^SPX", "conflicting"),
            _entry("^DJI", "supportive"),
        ],
    )
    result = qe.evaluate_stances([artifact], prices_dir=prices_dir, horizons=(1,))
    metrics = result["metrics"]["1d"]
    assert metrics["supportive"]["hit_rate"] == 0.0
    assert metrics["conflicting"]["hit_rate"] == 0.0


def test_evaluate_stances_horizon_beyond_data(prices_dir: Path) -> None:
    artifact = _artifact(
        "2024-01-01",
        [_entry("^SPX", "supportive"), _entry("^DJI", "conflicting")],
    )
    result = qe.evaluate_stances([artifact], prices_dir=prices_dir, horizons=(20,))
    assert result["metrics"]["20d"]["supportive"]["count"] == 0
    assert result["metrics"]["20d"]["supportive"]["hit_rate"] is None
    assert result["metadata"]["evaluated_dates"] == []
    assert result["metadata"]["generated_at"] is None


def test_evaluate_stances_needs_two_series(tmp_path: Path) -> None:
    directory = tmp_path / "prices"
    _write_prices(directory, "^SPX", [100, 101, 102])
    artifact = _artifact(
        "2024-01-01",
        [_entry("^SPX", "supportive"), _entry("^GONE", "conflicting")],
    )
    result = qe.evaluate_stances([artifact], prices_dir=directory, horizons=(1,))
    assert result["metrics"]["1d"]["supportive"]["count"] == 0


def test_evaluate_stances_skips_empty_artifacts(prices_dir: Path) -> None:
    no_date = {
        "version": "1.0.0",
        "metadata": {},
        "instruments": [_entry("^SPX", "supportive")],
    }
    all_gated = _artifact(
        "2024-01-01", [_entry("^SPX", "supportive", gates=["uncited_claims"])]
    )
    result = qe.evaluate_stances(
        [no_date, all_gated], prices_dir=prices_dir, horizons=(1,)
    )
    assert result["metadata"]["evaluated_dates"] == []


def test_median_even_and_odd() -> None:
    assert qe._median([3.0, 1.0, 2.0]) == 2.0
    assert qe._median([1.0, 2.0, 3.0, 4.0]) == 2.5


def test_forward_return_bounds() -> None:
    series = (["2024-01-02", "2024-01-03"], [100.0, 110.0])
    assert qe._forward_return(series, "2024-01-01", 1) is None
    assert qe._forward_return(series, "2024-01-02", 1) == pytest.approx(0.1)
    assert qe._forward_return(series, "2024-01-03", 1) is None


# ── validate_evaluation ─────────────────────────────────────────────────────────


def test_validate_evaluation_errors() -> None:
    assert qe.validate_evaluation({}) != []
    assert any(
        "unsupported version" in e
        for e in qe.validate_evaluation({
            "version": "0.1",
            "metadata": {},
            "metrics": {},
        })
    )
    errors = qe.validate_evaluation({
        "version": qe.EVALUATION_VERSION,
        "metadata": [],
        "metrics": "bad",
    })
    assert any("'metadata'" in e for e in errors)
    assert any("'metrics'" in e for e in errors)


# ── check_links ─────────────────────────────────────────────────────────────────


def _evidence_dir(tmp_path: Path, urls: list[str]) -> Path:
    directory = tmp_path / "evidence"
    directory.mkdir()
    bundle = {
        "version": "1.0.0",
        "metadata": {},
        "items": [{"id": f"{i:016x}", "url": url} for i, url in enumerate(urls)],
    }
    (directory / "2024-01-01.json").write_text(json.dumps(bundle))
    return directory


def test_check_links_no_bundles(tmp_path: Path) -> None:
    empty = tmp_path / "evidence"
    empty.mkdir()
    assert qe.check_links(empty) == ["no evidence bundles found"]


def test_check_links_reachable(tmp_path: Path, mocker: MockerFixture) -> None:
    directory = _evidence_dir(tmp_path, ["https://ok.example/a"])
    response = mocker.MagicMock()
    response.__enter__.return_value = response
    mocker.patch.object(qe.urllib.request, "urlopen", return_value=response)
    assert qe.check_links(directory) == []


def test_check_links_unreachable(tmp_path: Path, mocker: MockerFixture) -> None:
    directory = _evidence_dir(
        tmp_path, ["https://dead.example/a", "https://dead.example/b"]
    )
    mocker.patch.object(qe.urllib.request, "urlopen", side_effect=OSError("gone"))
    warnings = qe.check_links(directory, sample=1)
    assert len(warnings) == 1
    assert "unreachable" in warnings[0]


# ── main ────────────────────────────────────────────────────────────────────────


def test_main_evaluate(tmp_path: Path, prices_dir: Path) -> None:
    qual_dir = tmp_path / "qualitative"
    qual_dir.mkdir()
    artifact = _artifact(
        "2024-01-01",
        [_entry("^SPX", "supportive"), _entry("^DJI", "conflicting")],
    )
    (qual_dir / "2024-01-01.json").write_text(json.dumps(artifact))
    output = tmp_path / "performance" / "eval.json"
    result = qe.main([
        "evaluate",
        "--qualitative-dir",
        str(qual_dir),
        "--prices-dir",
        str(prices_dir),
        "--horizons",
        "1,2",
        "--output",
        str(output),
    ])
    assert result == 0
    written = json.loads(output.read_text())
    assert qe.validate_evaluation(written) == []


def test_main_evaluate_bad_horizons(tmp_path: Path) -> None:
    result = qe.main([
        "evaluate",
        "--qualitative-dir",
        str(tmp_path),
        "--horizons",
        "1,x",
    ])
    assert result == 1
    result = qe.main([
        "evaluate",
        "--qualitative-dir",
        str(tmp_path),
        "--horizons",
        "0",
    ])
    assert result == 1


def test_main_evaluate_no_artifacts(tmp_path: Path) -> None:
    empty = tmp_path / "qualitative"
    empty.mkdir()
    result = qe.main(["evaluate", "--qualitative-dir", str(empty)])
    assert result == 1


def test_main_check_links(
    tmp_path: Path, mocker: MockerFixture, capsys: pytest.CaptureFixture[str]
) -> None:
    directory = _evidence_dir(tmp_path, ["https://ok.example/a"])
    response = mocker.MagicMock()
    response.__enter__.return_value = response
    mocker.patch.object(qe.urllib.request, "urlopen", return_value=response)
    assert qe.main(["check-links", "--evidence-dir", str(directory)]) == 0
    assert "all sampled" in capsys.readouterr().out


def test_main_check_links_warnings(
    tmp_path: Path, mocker: MockerFixture, capsys: pytest.CaptureFixture[str]
) -> None:
    directory = _evidence_dir(tmp_path, ["https://dead.example/a"])
    mocker.patch.object(qe.urllib.request, "urlopen", side_effect=OSError("gone"))
    assert qe.main(["check-links", "--evidence-dir", str(directory)]) == 0
    assert "WARNING: unreachable" in capsys.readouterr().out
