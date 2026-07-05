"""Tests for the deterministic OKF theme-curation proposal helper (#96)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from aims import okf_curation

GOLDEN = Path(__file__).resolve().parent / "golden"


def _qualitative(
    when: str,
    themes: list[tuple[str, list[str]]],
    instruments: list[tuple[str, str, str, list[str]]] | None = None,
    *,
    withheld: bool = False,
) -> dict[str, Any]:
    return {
        "metadata": {
            "analysis_date": when,
            "gates": {"market_narrative_withheld": withheld},
        },
        "market": {
            "themes": [{"title": title, "citations": cites} for title, cites in themes]
        },
        "instruments": [
            {
                "canonical_id": cid,
                "symbol": sym,
                "stance": stance,
                "qualitative_gates": gates,
            }
            for cid, sym, stance, gates in (instruments or [])
        ],
    }


def _tagged(when: str, themes: list[tuple[str, list[str]]]) -> list[tuple[str, dict]]:
    return [(f"data/qualitative/{when}.json", _qualitative(when, themes))]


# ── tokenization and clustering ──────────────────────────────────────────────


def test_theme_tokens_drops_stopwords_digits_and_short_words() -> None:
    tokens = okf_curation.theme_tokens("Year-end equity rally on rate-pause hopes 2024")
    assert tokens == frozenset({
        "year",
        "end",
        "equity",
        "rally",
        "rate",
        "pause",
        "hopes",
    })


def test_cluster_themes_groups_similar_titles() -> None:
    artifacts = [
        *_tagged("2024-01-01", [("Copper supply squeeze tightens", ["ev-a"])]),
        *_tagged("2024-01-10", [("Copper supply squeeze deepens", ["ev-b"])]),
        *_tagged("2024-01-20", [("Gold safe-haven demand rises", ["ev-c"])]),
    ]
    clusters, warnings = okf_curation.cluster_themes(artifacts)
    assert warnings == []
    sizes = sorted(len(c.occurrences) for c in clusters)
    assert sizes == [1, 2]


def test_cluster_themes_skips_withheld_and_empty_token_titles() -> None:
    artifacts = [
        (
            "data/qualitative/2024-01-01.json",
            _qualitative("2024-01-01", [("Copper squeeze", ["ev-a"])], withheld=True),
        ),
        (
            "data/qualitative/2024-01-02.json",
            _qualitative("2024-01-02", [("2024 500", ["ev-b"])]),
        ),
    ]
    clusters, warnings = okf_curation.cluster_themes(artifacts)
    assert clusters == []
    assert warnings == [
        "data/qualitative/2024-01-01.json: market narrative withheld by gates; skipped",
        "data/qualitative/2024-01-02.json: theme '2024 500' has no significant tokens",
    ]


def test_promotion_candidates_require_three_dates_and_span() -> None:
    # three occurrences but only 10 days apart → not promoted
    near = [
        *_tagged("2024-01-01", [("Copper supply squeeze", ["ev-a"])]),
        *_tagged("2024-01-05", [("Copper supply squeeze", ["ev-b"])]),
        *_tagged("2024-01-10", [("Copper supply squeeze", ["ev-c"])]),
    ]
    clusters, _ = okf_curation.cluster_themes(near)
    assert okf_curation.promotion_candidates(clusters) == []
    # spanning ≥14 days → promoted
    spanning = [
        *_tagged("2024-01-01", [("Copper supply squeeze", ["ev-a"])]),
        *_tagged("2024-01-10", [("Copper supply squeeze", ["ev-b"])]),
        *_tagged("2024-01-20", [("Copper supply squeeze", ["ev-c"])]),
    ]
    clusters, _ = okf_curation.cluster_themes(spanning)
    promoted = okf_curation.promotion_candidates(clusters)
    assert len(promoted) == 1
    assert promoted[0].span_days == 19


# ── stance streaks ───────────────────────────────────────────────────────────


def test_stance_streaks_finds_persistent_ungated_stances() -> None:
    artifacts = [
        (
            "s/2024-01-01.json",
            _qualitative("2024-01-01", [], [("cop", "HG=F", "conflicting", [])]),
        ),
        (
            "s/2024-01-10.json",
            _qualitative("2024-01-10", [], [("cop", "HG=F", "conflicting", [])]),
        ),
        (
            "s/2024-01-20.json",
            _qualitative(
                "2024-01-20", [], [("cop", "HG=F", "conflicting", ["stale_evidence"])]
            ),
        ),
        (
            "s/2024-01-21.json",
            _qualitative("2024-01-21", [], [("cop", "HG=F", "conflicting", [])]),
        ),
    ]
    streaks = okf_curation.stance_streaks(artifacts)
    assert streaks == [
        {
            "canonical_id": "cop",
            "symbol": "HG=F",
            "stance": "conflicting",
            "dates": ["2024-01-01", "2024-01-10", "2024-01-21"],
        }
    ]


def test_stance_streaks_ignores_short_runs() -> None:
    artifacts = [
        (
            "s/2024-01-01.json",
            _qualitative("2024-01-01", [], [("cop", "HG=F", "conflicting", [])]),
        ),
        (
            "s/2024-01-02.json",
            _qualitative("2024-01-02", [], [("cop", "HG=F", "conflicting", [])]),
        ),
    ]
    assert okf_curation.stance_streaks(artifacts) == []


# ── existing concepts and retirement ─────────────────────────────────────────


def _write_concept(
    path: Path, tags: list[str] | str, theme_tokens: list[str] | None
) -> None:
    lines = ["---", "title: A Theme", f"tags: {json.dumps(tags)}"]
    if theme_tokens is not None:
        lines.append(f"theme_tokens: {json.dumps(theme_tokens)}")
    lines += ["type: concept", "---", "", "# A Theme", ""]
    path.write_text("\n".join(lines), encoding="utf-8")


def test_load_theme_concepts_filters_and_warns(tmp_path: Path) -> None:
    concepts_dir = tmp_path / "concepts"
    concepts_dir.mkdir()
    _write_concept(
        concepts_dir / "theme-a.md", ["qualitative-theme"], ["copper", "squeeze"]
    )
    _write_concept(concepts_dir / "plain.md", ["architecture"], None)
    _write_concept(concepts_dir / "theme-missing.md", ["qualitative-theme"], None)
    (concepts_dir / "broken.md").write_text("---\ntags: [\n---\nx", encoding="utf-8")
    concepts, warnings = okf_curation.load_theme_concepts(concepts_dir)
    assert [c.title for c in concepts] == ["A Theme"]
    assert any("has no 'theme_tokens'" in w for w in warnings)
    assert any("unreadable front matter" in w for w in warnings)


def test_load_theme_concepts_missing_dir(tmp_path: Path) -> None:
    concepts, warnings = okf_curation.load_theme_concepts(tmp_path / "absent")
    assert concepts == []
    assert warnings == [f"{tmp_path / 'absent'}: concepts directory not found"]


def test_retirement_candidates_flags_stale_and_never_seen() -> None:
    concepts = [
        okf_curation.ThemeConcept(
            "okf/concepts/theme-copper.md",
            "Copper squeeze",
            frozenset({"copper", "squeeze"}),
        ),
        okf_curation.ThemeConcept(
            "okf/concepts/theme-ghost.md", "Ghost", frozenset({"ghost", "theme"})
        ),
    ]
    artifacts = _tagged("2024-01-01", [("Copper squeeze tightens", ["ev-a"])])
    clusters, _ = okf_curation.cluster_themes(artifacts)
    # copper last seen 2024-01-01; as-of 2024-04-01 is > 60 days → retire both
    retirements = okf_curation.retirement_candidates(concepts, clusters, "2024-04-01")
    paths = {item["path"] for item in retirements}
    assert paths == {"okf/concepts/theme-copper.md", "okf/concepts/theme-ghost.md"}
    # as-of just after last-seen → copper is fresh, only ghost retires
    fresh = okf_curation.retirement_candidates(concepts, clusters, "2024-01-15")
    assert [item["path"] for item in fresh] == ["okf/concepts/theme-ghost.md"]


def test_concept_skeleton_shape() -> None:
    artifacts = _tagged("2024-01-01", [("Copper Supply Squeeze", ["ev-a", "ev-b"])])
    clusters, _ = okf_curation.cluster_themes(artifacts)
    skeleton = okf_curation.concept_skeleton(clusters[0], "2024-02-01")
    assert "id: okf/concepts/theme-copper-supply-squeeze" in skeleton
    assert "tags: [qualitative-theme]" in skeleton
    assert "theme_tokens: [copper, squeeze, supply]" in skeleton
    assert "ev-a, ev-b" in skeleton


def test_slug_falls_back_when_empty() -> None:
    assert okf_curation._slug("!!!") == "theme"


def test_jaccard_zero_for_empty_sets() -> None:
    assert okf_curation._jaccard(frozenset(), frozenset({"a"})) == 0.0
    assert okf_curation._jaccard(frozenset({"a"}), frozenset()) == 0.0


# ── proposal rendering (goldens) ─────────────────────────────────────────────


def _promotable() -> list[tuple[str, dict[str, Any]]]:
    return [
        (
            "data/qualitative/2024-01-01.json",
            _qualitative(
                "2024-01-01",
                [("Copper supply squeeze tightens", ["ev-a"])],
                [("cop", "HG=F", "conflicting", [])],
            ),
        ),
        (
            "data/qualitative/2024-01-10.json",
            _qualitative(
                "2024-01-10",
                [("Copper supply squeeze persists", ["ev-b"])],
                [("cop", "HG=F", "conflicting", [])],
            ),
        ),
        (
            "data/qualitative/2024-01-20.json",
            _qualitative(
                "2024-01-20",
                [("Copper supply squeeze deepens", ["ev-c"])],
                [("cop", "HG=F", "conflicting", [])],
            ),
        ),
    ]


# Stable relative paths keep the goldens free of volatile tmp paths; tests run
# with the repository root as the working directory.
_FIXTURE_CONCEPTS = Path("tests/fixtures/okf_concepts")
_MISSING_CONCEPTS = Path("tests/fixtures/okf_concepts_missing")


def test_render_proposal_populated_matches_golden() -> None:
    rendered = okf_curation.render_proposal(
        _promotable(), _FIXTURE_CONCEPTS, "2024-06-01"
    )
    assert rendered == (GOLDEN / "okf-curation-proposal.md").read_text()


def test_render_proposal_empty_matches_golden() -> None:
    rendered = okf_curation.render_proposal([], _MISSING_CONCEPTS, None)
    assert rendered == (GOLDEN / "okf-curation-proposal-empty.md").read_text()


# ── loading and CLI ──────────────────────────────────────────────────────────


def test_load_artifacts_skips_bad_files(tmp_path: Path) -> None:
    qdir = tmp_path / "qualitative"
    qdir.mkdir()
    (qdir / "2024-01-01.json").write_text(
        json.dumps(_qualitative("2024-01-01", [("Copper", ["ev-a"])])),
        encoding="utf-8",
    )
    (qdir / "broken.json").write_text("{", encoding="utf-8")
    (qdir / "nodate.json").write_text(json.dumps({"metadata": {}}), encoding="utf-8")
    artifacts, warnings = okf_curation.load_artifacts(qdir)
    assert len(artifacts) == 1
    assert len(warnings) == 2


def test_load_artifacts_missing_dir(tmp_path: Path) -> None:
    artifacts, warnings = okf_curation.load_artifacts(tmp_path / "absent")
    assert artifacts == []
    assert warnings == []


def test_main_writes_output_file(tmp_path: Path, capsys: Any) -> None:
    qdir = tmp_path / "qualitative"
    qdir.mkdir()
    for source, artifact in _promotable():
        name = Path(source).name
        (qdir / name).write_text(json.dumps(artifact), encoding="utf-8")
    out = tmp_path / "proposal.md"
    code = okf_curation.main([
        "--qualitative-dir",
        str(qdir),
        "--concepts-dir",
        str(tmp_path / "concepts"),
        "--output",
        str(out),
    ])
    assert code == 0
    assert "Copper supply squeeze deepens" in out.read_text()
    assert "Curation proposal written" in capsys.readouterr().out


def test_main_prints_to_stdout(tmp_path: Path, capsys: Any) -> None:
    code = okf_curation.main([
        "--qualitative-dir",
        str(tmp_path / "absent"),
        "--concepts-dir",
        str(tmp_path / "concepts"),
    ])
    assert code == 0
    assert "OKF qualitative theme curation proposal" in capsys.readouterr().out


def test_main_rejects_bad_as_of(tmp_path: Path, capsys: Any) -> None:
    code = okf_curation.main([
        "--qualitative-dir",
        str(tmp_path),
        "--as-of",
        "nope",
    ])
    assert code == 1
    assert "not a YYYY-MM-DD" in capsys.readouterr().out


def test_main_warns_on_unreadable_artifacts(tmp_path: Path, capsys: Any) -> None:
    qdir = tmp_path / "qualitative"
    qdir.mkdir()
    (qdir / "broken.json").write_text("{", encoding="utf-8")
    code = okf_curation.main(["--qualitative-dir", str(qdir)])
    assert code == 0
    assert "WARNING" in capsys.readouterr().out
