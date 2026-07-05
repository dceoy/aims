"""Tests for the deterministic stance-vs-forward-return evaluation (#97)."""

from __future__ import annotations

import argparse
import json
from datetime import date, timedelta
from pathlib import Path
from typing import Any

import pytest

from aims import performance, validate_performance

GOLDEN = Path(__file__).resolve().parent / "golden"
REPO_ROOT = Path(__file__).resolve().parent.parent


def _dates(n: int, start: str = "2024-01-01") -> list[str]:
    first = date.fromisoformat(start)
    return [(first + timedelta(days=i)).isoformat() for i in range(n)]


def _analysis(
    when: str,
    bars: dict[str, tuple[Any, Any, Any]],
    interval: str = "d",
) -> dict[str, Any]:
    # Analysis artifact stub: symbol -> (bar_date, ret_1d, ret_5d).
    return {
        "metadata": {
            "generated_at": f"{when}T00:00:00+00:00",
            "config": {"interval": interval},
            "data_freshness": {sym: bar[0] for sym, bar in bars.items()},
        },
        "instruments": [
            {
                "symbol": sym,
                "features": {"ret_1d": bar[1], "ret_5d": bar[2]},
            }
            for sym, bar in bars.items()
        ],
    }


def _chain(
    returns: dict[str, float], n: int, start: str = "2024-01-01"
) -> list[dict[str, Any]]:
    # One analysis per day, each advancing every symbol by one bar.
    return [
        _analysis(when, {sym: (when, ret, None) for sym, ret in returns.items()})
        for when in _dates(n, start)
    ]


def _qualitative(
    when: str,
    entries: list[tuple[str, str, str, list[str]]],
    interval: str = "d",
) -> dict[str, Any]:
    # Qualitative stub: entries of (symbol, stance, confidence, gates).
    return {
        "metadata": {"analysis_date": when, "interval": interval},
        "instruments": [
            {
                "symbol": sym,
                "stance": stance,
                "confidence": confidence,
                "qualitative_gates": gates,
            }
            for sym, stance, confidence, gates in entries
        ],
    }


# ── bar-series construction ──────────────────────────────────────────────────


def test_build_bar_series_chains_and_dedupes_repeated_bars() -> None:
    analyses = [
        _analysis("2024-01-01", {"AAA": ("2024-01-01", 0.01, None)}),
        _analysis("2024-01-02", {"AAA": ("2024-01-02", 0.02, 0.05)}),
        # weekend artifact repeating the same bar collapses into one entry
        _analysis("2024-01-03", {"AAA": ("2024-01-02", 0.02, 0.05)}),
    ]
    series, warnings = performance.build_bar_series(analyses)
    assert warnings == []
    assert series == {
        "AAA": [
            performance.Bar("2024-01-01", 0.01, None),
            performance.Bar("2024-01-02", 0.02, 0.05),
        ]
    }


def test_build_bar_series_warns_on_conflicting_revisions_and_keeps_latest() -> None:
    analyses = [
        _analysis("2024-01-01", {"AAA": ("2024-01-01", 0.01, None)}),
        _analysis("2024-01-02", {"AAA": ("2024-01-01", 0.05, None)}),
    ]
    series, warnings = performance.build_bar_series(analyses)
    assert series["AAA"] == [performance.Bar("2024-01-01", 0.05, None)]
    assert warnings == [
        (
            "AAA: conflicting ret_1d for bar 2024-01-01 across analysis"
            " artifacts; keeping the latest value"
        )
    ]


def test_build_bar_series_skips_rows_without_usable_bar_or_return() -> None:
    artifact = {
        "metadata": {
            "generated_at": "2024-01-01T00:00:00+00:00",
            "config": {"interval": "d"},
            "data_freshness": {"AAA": "n/a", "BBB": "2024-01-01"},
        },
        "instruments": [
            {"symbol": "AAA", "features": {"ret_1d": 0.01}},
            {"symbol": "BBB", "features": {"ret_1d": None, "ret_5d": "x"}},
            {"symbol": "", "features": {"ret_1d": 0.01}},
            {"symbol": "CCC", "features": None},
        ],
    }
    series, warnings = performance.build_bar_series([artifact])
    assert series == {}
    assert warnings == []


def test_build_bar_series_rejects_artifact_without_generated_at() -> None:
    with pytest.raises(ValueError, match="generated_at"):
        performance.build_bar_series([{"metadata": {}}])


# ── chain integrity ──────────────────────────────────────────────────────────


def test_chain_breaks_accepts_consistent_ret_5d() -> None:
    bars = [performance.Bar(when, 0.01, None) for when in _dates(5)]
    compounded = 1.01**5 - 1
    bars.append(performance.Bar("2024-01-06", 0.01, compounded))
    assert performance.chain_breaks(bars) == set()


def test_chain_breaks_marks_window_when_a_bar_is_missing() -> None:
    bars = [performance.Bar(when, 0.01, None) for when in _dates(5)]
    # ret_5d implies a much larger move than the chained bars: a bar is missing
    bars.append(performance.Bar("2024-01-06", 0.01, 0.20))
    assert performance.chain_breaks(bars) == {1, 2, 3, 4, 5}


def test_forward_return_compounds_and_respects_broken_links() -> None:
    bars = [performance.Bar(when, 0.01, None) for when in _dates(4)]
    realized = performance.forward_return(bars, set(), 0, 3)
    assert realized == pytest.approx(1.01**3 - 1)
    assert performance.forward_return(bars, {2}, 0, 3) is None


# ── stance evaluation ────────────────────────────────────────────────────────


def test_evaluate_stances_rejects_bad_horizons() -> None:
    with pytest.raises(ValueError, match="horizons"):
        performance.evaluate_stances([], [], ())
    with pytest.raises(ValueError, match="horizons"):
        performance.evaluate_stances([], [], (0,))
    with pytest.raises(ValueError, match="horizons"):
        performance.evaluate_stances([], [], (1, 1))


def test_evaluate_stances_empty_state_is_safe() -> None:
    result, warnings = performance.evaluate_stances([], [], (1,))
    assert result["instruments_evaluated"] == 0
    assert result["horizons"]["1d"]["observations"] == 0
    assert warnings == ["no qualitative artifacts found; stance evaluation is empty"]


def test_evaluate_stances_scores_hits_by_stance_and_confidence() -> None:
    analyses = _chain({"AAA": 0.01, "BBB": -0.005, "CCC": 0.002}, 4)
    qualitative = [
        _qualitative(
            "2024-01-01",
            [
                ("AAA", "supportive", "high", []),
                ("BBB", "conflicting", "medium", []),
                ("CCC", "neutral", "low", []),
            ],
        )
    ]
    result, warnings = performance.evaluate_stances(qualitative, analyses, (1, 2))
    assert warnings == []
    assert result["instruments_evaluated"] == 3
    one_day = result["horizons"]["1d"]
    assert one_day["observations"] == 3
    assert one_day["stances"]["supportive"] == {
        "count": 1,
        "hit_rate": 1.0,
        "average_return": 0.01,
    }
    assert one_day["stances"]["conflicting"]["hit_rate"] == 1.0
    assert one_day["stances"]["neutral"]["hit_rate"] is None
    assert one_day["stances"]["neutral"]["count"] == 1
    assert one_day["confidence_calibration"]["high"] == {
        "count": 1,
        "hit_rate": 1.0,
    }
    assert one_day["confidence_calibration"]["low"] == {
        "count": 0,
        "hit_rate": None,
    }
    two_day = result["horizons"]["2d"]
    assert two_day["stances"]["supportive"]["average_return"] == pytest.approx(
        round(1.01**2 - 1, 6)
    )


def test_evaluate_stances_counts_pending_gated_and_unmatched() -> None:
    analyses = _chain({"AAA": 0.01}, 2)
    qualitative = [
        _qualitative(
            "2024-01-02",
            [
                ("AAA", "supportive", "high", []),
                ("BBB", "supportive", "high", []),
                ("CCC", "neutral", "low", ["citation_coverage"]),
            ],
        )
    ]
    result, warnings = performance.evaluate_stances(qualitative, analyses, (1,))
    assert result["instruments_evaluated"] == 1
    assert result["excluded_gated"] == 1
    assert result["unmatched"] == 1
    assert result["horizons"]["1d"]["pending"] == 1
    assert warnings == ["2024-01-02: BBB: no chained bar for the stance"]


def test_evaluate_stances_flags_missing_analysis_and_bad_enum() -> None:
    analyses = _chain({"AAA": 0.01}, 2)
    qualitative = [
        _qualitative("2024-01-05", [("AAA", "supportive", "high", [])]),
        _qualitative("2024-01-01", [("AAA", "bullish", "high", [])]),
    ]
    result, warnings = performance.evaluate_stances(qualitative, analyses, (1,))
    assert result["instruments_evaluated"] == 0
    assert warnings == [
        "2024-01-01: AAA: invalid stance or confidence",
        "2024-01-05: no analysis artifact for qualitative artifact",
    ]


def test_evaluate_stances_skips_windows_with_broken_chain() -> None:
    dates = _dates(7)
    analyses = []
    for i, when in enumerate(dates):
        # the last bar carries a ret_5d that contradicts the chained ret_1d
        ret_5d = 0.5 if i == 6 else None
        analyses.append(_analysis(when, {"AAA": (when, 0.01, ret_5d)}))
    qualitative = [_qualitative(dates[2], [("AAA", "supportive", "high", [])])]
    result, warnings = performance.evaluate_stances(qualitative, analyses, (1,))
    assert result["horizons"]["1d"]["broken_chain"] == 1
    assert result["horizons"]["1d"]["observations"] == 0
    assert "2024-01-03: AAA: broken bar chain within 1d forward window" in warnings


def test_evaluate_stances_rejects_qualitative_without_date() -> None:
    with pytest.raises(ValueError, match="analysis_date"):
        performance.evaluate_stances([{"metadata": {}}], [], (1,))


# ── artifact and page ────────────────────────────────────────────────────────


def _populated_artifact() -> dict[str, Any]:
    analyses = _chain({"AAA": 0.01, "BBB": -0.005, "CCC": 0.002}, 25)
    qualitative = [
        _qualitative(
            "2024-01-01",
            [
                ("AAA", "supportive", "high", []),
                ("BBB", "conflicting", "medium", []),
                ("CCC", "neutral", "low", []),
            ],
        ),
        _qualitative("2024-01-21", [("AAA", "supportive", "high", [])]),
    ]
    return performance.build_artifact(
        qualitative, analyses, as_of="2024-01-25", interval="d"
    )


def test_build_artifact_carries_provenance_and_disclaimer() -> None:
    artifact = _populated_artifact()
    meta = artifact["metadata"]
    assert artifact["version"] == performance.PERFORMANCE_VERSION
    assert meta["generated_at"] == "2024-01-25T00:00:00+00:00"
    assert meta["config"]["horizons"] == [1, 5, 20]
    assert meta["inputs"]["qualitative_dates"] == ["2024-01-01", "2024-01-21"]
    assert meta["disclaimer"] == performance.DISCLAIMER
    assert meta["git_commit"]


def test_render_page_matches_golden() -> None:
    artifact = _populated_artifact()
    rendered = performance.render_page(artifact)
    assert rendered == (GOLDEN / "stance-evaluation.md").read_text()


def test_render_page_is_stable_across_json_round_trip() -> None:
    artifact = _populated_artifact()
    round_tripped = json.loads(json.dumps(artifact, sort_keys=True))
    assert performance.render_page(round_tripped) == performance.render_page(artifact)


def test_committed_evaluation_page_is_regenerated_from_artifact() -> None:
    committed = json.loads((REPO_ROOT / "data/performance/2026-07-04.json").read_text())
    expected = (REPO_ROOT / "content/evaluation/_index.md").read_text()
    assert performance.render_page(committed) == expected


def test_render_page_caps_warning_list() -> None:
    artifact = _populated_artifact()
    artifact["warnings"] = [f"warning {i:02d}" for i in range(25)]
    rendered = performance.render_page(artifact)
    assert "warning 19" in rendered
    assert "warning 20" not in rendered
    assert "… and 5 more" in rendered


def test_build_artifact_merges_and_sorts_extra_warnings() -> None:
    analyses = _chain({"AAA": 0.01}, 2)
    qualitative = [_qualitative("2024-01-01", [("AAA", "supportive", "high", [])])]
    artifact = performance.build_artifact(
        qualitative,
        analyses,
        as_of="2024-01-02",
        interval="d",
        extra_warnings=("zzz-extra", "aaa-extra"),
    )
    assert "zzz-extra" in artifact["warnings"]
    assert "aaa-extra" in artifact["warnings"]
    assert artifact["warnings"] == sorted(artifact["warnings"])


def test_build_artifact_default_extra_warnings_is_empty() -> None:
    analyses = _chain({"AAA": 0.01}, 2)
    qualitative = [_qualitative("2024-01-01", [("AAA", "supportive", "high", [])])]
    artifact = performance.build_artifact(
        qualitative, analyses, as_of="2024-01-02", interval="d"
    )
    assert artifact["warnings"] == sorted(artifact["warnings"])


# ── trust boundary: excluding a same-run qualitative artifact ───────────────


def _write(path: Path, data: dict[str, Any]) -> None:
    path.write_text(json.dumps(data, sort_keys=True) + "\n", encoding="utf-8")


def test_load_qualitative_artifacts_excludes_given_date_with_warning(
    tmp_path: Path,
) -> None:
    qdir = tmp_path / "qualitative"
    qdir.mkdir()
    _write(
        qdir / "2024-01-01.json",
        _qualitative("2024-01-01", [("AAA", "supportive", "high", [])]),
    )
    _write(
        qdir / "2024-01-05.json",
        _qualitative("2024-01-05", [("AAA", "supportive", "high", [])]),
    )
    artifacts, warnings = performance._load_qualitative_artifacts(
        qdir, "2024-01-05", frozenset({"2024-01-05"})
    )
    assert [a["metadata"]["analysis_date"] for a in artifacts] == ["2024-01-01"]
    assert warnings == [
        (
            "2024-01-05: excluded a same-run qualitative artifact because the"
            " qualitative-analysis step did not report success"
        )
    ]


def test_load_qualitative_artifacts_no_exclusions_by_default(tmp_path: Path) -> None:
    qdir = tmp_path / "qualitative"
    qdir.mkdir()
    _write(
        qdir / "2024-01-01.json",
        _qualitative("2024-01-01", [("AAA", "supportive", "high", [])]),
    )
    artifacts, warnings = performance._load_qualitative_artifacts(
        qdir, "2024-01-01", frozenset()
    )
    assert len(artifacts) == 1
    assert warnings == []


def test_load_qualitative_artifacts_missing_dir(tmp_path: Path) -> None:
    artifacts, warnings = performance._load_qualitative_artifacts(
        tmp_path / "absent", "2024-01-01", frozenset()
    )
    assert artifacts == []
    assert warnings == []


def test_load_qualitative_artifacts_skips_future_and_non_daily(
    tmp_path: Path,
) -> None:
    qdir = tmp_path / "qualitative"
    qdir.mkdir()
    _write(
        qdir / "2024-01-01.json",
        _qualitative("2024-01-01", [("AAA", "supportive", "high", [])]),
    )
    _write(
        qdir / "2024-01-02-w.json",
        _qualitative("2024-01-02", [("AAA", "supportive", "high", [])], "w"),
    )
    _write(
        qdir / "2024-02-01.json",
        _qualitative("2024-02-01", [("AAA", "supportive", "high", [])]),
    )
    artifacts, warnings = performance._load_qualitative_artifacts(
        qdir, "2024-01-01", frozenset()
    )
    assert [a["metadata"]["analysis_date"] for a in artifacts] == ["2024-01-01"]
    assert warnings == []


# ── CLI ──────────────────────────────────────────────────────────────────────


def test_main_writes_artifact_and_page(tmp_path: Path) -> None:
    analysis_dir = tmp_path / "analysis"
    qualitative_dir = tmp_path / "qualitative"
    analysis_dir.mkdir()
    qualitative_dir.mkdir()
    for artifact in _chain({"AAA": 0.01}, 3):
        when = artifact["metadata"]["generated_at"][:10]
        _write(analysis_dir / f"{when}.json", artifact)
    # non-daily and future artifacts are excluded from the chain
    _write(
        analysis_dir / "2024-01-01-w.json",
        _analysis("2024-01-01", {"AAA": ("2024-01-01", 0.5, None)}, interval="w"),
    )
    _write(
        analysis_dir / "2024-02-01.json",
        _analysis("2024-02-01", {"AAA": ("2024-02-01", 0.5, None)}),
    )
    _write(
        qualitative_dir / "2024-01-01.json",
        _qualitative("2024-01-01", [("AAA", "supportive", "high", [])]),
    )
    _write(
        qualitative_dir / "2024-01-02-w.json",
        _qualitative("2024-01-02", [("AAA", "supportive", "high", [])], "w"),
    )
    page = tmp_path / "content" / "_index.md"
    exit_code = performance.main([
        "--input",
        str(analysis_dir / "2024-01-03.json"),
        "--analysis-dir",
        str(analysis_dir),
        "--qualitative-dir",
        str(qualitative_dir),
        "--output",
        str(tmp_path / "performance"),
        "--horizons",
        "1,2",
        "--page-output",
        str(page),
    ])
    assert exit_code == 0
    written = json.loads((tmp_path / "performance" / "2024-01-03.json").read_text())
    assert written["metadata"]["inputs"]["analysis_dates"] == [
        "2024-01-01",
        "2024-01-02",
        "2024-01-03",
    ]
    assert written["metadata"]["inputs"]["qualitative_dates"] == ["2024-01-01"]
    assert written["stance_evaluation"]["horizons"]["2d"]["observations"] == 1
    assert page.read_text() == performance.render_page(written)


def test_main_without_page_or_qualitative_dir(tmp_path: Path) -> None:
    analysis_dir = tmp_path / "analysis"
    analysis_dir.mkdir()
    _write(
        analysis_dir / "2024-01-01.json",
        _analysis("2024-01-01", {"AAA": ("2024-01-01", 0.01, None)}),
    )
    exit_code = performance.main([
        "--input",
        str(analysis_dir / "2024-01-01.json"),
        "--analysis-dir",
        str(analysis_dir),
        "--qualitative-dir",
        str(tmp_path / "missing"),
        "--output",
        str(tmp_path / "performance"),
    ])
    assert exit_code == 0
    written = json.loads((tmp_path / "performance" / "2024-01-01.json").read_text())
    assert written["metadata"]["inputs"]["qualitative_dates"] == []


def _setup_analysis_chain(tmp_path: Path) -> Path:
    analysis_dir = tmp_path / "analysis"
    analysis_dir.mkdir()
    for artifact in _chain({"AAA": 0.01}, 3):
        when = artifact["metadata"]["generated_at"][:10]
        _write(analysis_dir / f"{when}.json", artifact)
    return analysis_dir


def test_main_excludes_same_run_qualitative_date_but_keeps_historical(
    tmp_path: Path,
) -> None:
    # Mirrors the workflow's continue-on-error qualitative step: a same-run
    # file can exist on disk after a failed/unvalidated run, so it must be
    # excluded by date while historical, already-validated artifacts stay in.
    analysis_dir = _setup_analysis_chain(tmp_path)
    qualitative_dir = tmp_path / "qualitative"
    qualitative_dir.mkdir()
    _write(
        qualitative_dir / "2024-01-01.json",
        _qualitative("2024-01-01", [("AAA", "supportive", "high", [])]),
    )
    _write(
        qualitative_dir / "2024-01-03.json",
        _qualitative("2024-01-03", [("AAA", "conflicting", "low", [])]),
    )
    exit_code = performance.main([
        "--input",
        str(analysis_dir / "2024-01-03.json"),
        "--analysis-dir",
        str(analysis_dir),
        "--qualitative-dir",
        str(qualitative_dir),
        "--output",
        str(tmp_path / "performance"),
        "--exclude-qualitative-date",
        "2024-01-03",
    ])
    assert exit_code == 0
    written = json.loads((tmp_path / "performance" / "2024-01-03.json").read_text())
    assert written["metadata"]["inputs"]["qualitative_dates"] == ["2024-01-01"]
    assert any(
        "2024-01-03: excluded a same-run qualitative artifact" in warning
        for warning in written["warnings"]
    )
    assert validate_performance.validate_artifact(written) == []


def test_main_includes_same_run_qualitative_date_when_not_excluded(
    tmp_path: Path,
) -> None:
    # When the qualitative step succeeds, the workflow omits the exclusion
    # flag entirely, so today's own artifact is evaluated like any other.
    analysis_dir = _setup_analysis_chain(tmp_path)
    qualitative_dir = tmp_path / "qualitative"
    qualitative_dir.mkdir()
    _write(
        qualitative_dir / "2024-01-03.json",
        _qualitative("2024-01-03", [("AAA", "supportive", "high", [])]),
    )
    exit_code = performance.main([
        "--input",
        str(analysis_dir / "2024-01-03.json"),
        "--analysis-dir",
        str(analysis_dir),
        "--qualitative-dir",
        str(qualitative_dir),
        "--output",
        str(tmp_path / "performance"),
    ])
    assert exit_code == 0
    written = json.loads((tmp_path / "performance" / "2024-01-03.json").read_text())
    assert written["metadata"]["inputs"]["qualitative_dates"] == ["2024-01-03"]
    assert validate_performance.validate_artifact(written) == []


def test_main_rejects_non_daily_input(tmp_path: Path, capsys: Any) -> None:
    path = tmp_path / "2024-01-01-w.json"
    _write(path, _analysis("2024-01-01", {"AAA": ("2024-01-01", 0.01, None)}, "w"))
    exit_code = performance.main([
        "--input",
        str(path),
        "--analysis-dir",
        str(tmp_path),
        "--qualitative-dir",
        str(tmp_path / "missing"),
        "--output",
        str(tmp_path / "performance"),
    ])
    assert exit_code == 1
    assert "daily interval only" in capsys.readouterr().out


def test_main_reports_missing_and_invalid_input(tmp_path: Path, capsys: Any) -> None:
    assert performance.main(["--input", str(tmp_path / "absent.json")]) == 1
    assert "ERROR" in capsys.readouterr().out
    bad = tmp_path / "bad.json"
    bad.write_text("{", encoding="utf-8")
    assert performance.main(["--input", str(bad)]) == 1
    assert "ERROR" in capsys.readouterr().out


def test_parse_horizons_rejects_bad_values() -> None:
    with pytest.raises(argparse.ArgumentTypeError):
        performance._parse_horizons("1,x")
    with pytest.raises(argparse.ArgumentTypeError):
        performance._parse_horizons("0")
    assert performance._parse_horizons("1,5") == (1, 5)
