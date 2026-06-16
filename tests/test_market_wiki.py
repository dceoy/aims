import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = ROOT / ".agents" / "skills" / "market-wiki" / "scripts"
FIXTURE = Path("tests/fixtures/analysis_2024-01-01.json")
GOLDEN = Path("tests/golden/2024-01-01-wiki-source.md")


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPT_DIR / f"{name}.py")
    if spec is None or spec.loader is None:
        pytest.fail(f"Failed to load {name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_render_wiki_source_matches_golden():
    mod = _load("render_wiki_source")
    artifact = json.loads(FIXTURE.read_text())

    assert mod.render_source(artifact, FIXTURE) == GOLDEN.read_text()


def test_render_wiki_source_cli_writes_output(tmp_path):
    mod = _load("render_wiki_source")
    output = tmp_path / "source.md"

    assert mod.main(["--input", str(FIXTURE), "--output", str(output)]) == 0
    assert output.read_text() == GOLDEN.read_text()


def test_update_wiki_creates_instrument_pages_and_log(tmp_path):
    render = _load("render_wiki_source")
    update = _load("update_wiki")
    wiki_root = tmp_path / "knowledge"
    source = wiki_root / "sources" / "2024-01-01-market-analysis.md"
    source.parent.mkdir(parents=True)
    source.write_text(render.render_source(json.loads(FIXTURE.read_text()), FIXTURE))

    assert (
        update.main([
            "--source",
            str(source),
            "--analysis",
            str(FIXTURE),
            "--wiki-root",
            str(wiki_root),
        ])
        == 0
    )

    assert (wiki_root / "wiki" / "instruments" / "spx.md").exists()
    assert (
        "sources/2024-01-01-market-analysis.md" in (wiki_root / "index.md").read_text()
    )
    assert "sources/2024-01-01-market-analysis.md" in (wiki_root / "log.md").read_text()


def test_lint_wiki_passes_and_reports_errors(tmp_path):
    render = _load("render_wiki_source")
    update = _load("update_wiki")
    lint = _load("lint_wiki")
    wiki_root = tmp_path / "knowledge"
    source = wiki_root / "sources" / "2024-01-01-market-analysis.md"
    source.parent.mkdir(parents=True)
    source.write_text(render.render_source(json.loads(FIXTURE.read_text()), FIXTURE))
    update.update_wiki(source, FIXTURE, wiki_root)

    assert lint.lint_wiki(wiki_root) == []
    (wiki_root / "wiki" / "overview.md").write_text("[broken](missing.md)\n")
    assert "broken link in wiki/overview.md: missing.md" in lint.lint_wiki(wiki_root)


def test_lint_wiki_cli_fails_for_missing_required_file(tmp_path, capsys):
    lint = _load("lint_wiki")
    wiki_root = tmp_path / "knowledge"
    wiki_root.mkdir()

    assert lint.main(["--wiki-root", str(wiki_root)]) == 1
    assert "missing required file: index.md" in capsys.readouterr().out


def test_render_wiki_source_handles_empty_reliable_artifact():
    mod = _load("render_wiki_source")
    artifact = {
        "version": "1.0.0",
        "metadata": {"generated_at": "bad", "data_source": "stooq"},
        "instruments": [
            {
                "symbol": "TEST.US",
                "rank": 1,
                "score": 1.0,
                "is_reliable": True,
                "risk_gates": [],
                "explanation": "ok|escaped",
                "features": {},
            }
        ],
    }

    rendered = mod.render_source(artifact)

    assert "# Market Analysis Source: unknown" in rendered
    assert "## Unreliable instruments\n\n- none" in rendered
    assert "## Risk gates\n\n- none" in rendered
    assert "## Data freshness\n\n- n/a" in rendered
    assert "ok\\|escaped" in rendered
    assert "- Source artifact: unknown" in rendered


def test_update_wiki_handles_existing_files_unknown_dates_and_non_dicts(tmp_path):
    update = _load("update_wiki")
    wiki_root = tmp_path / "knowledge"
    source = wiki_root / "sources" / "unknown-market-analysis.md"
    analysis = tmp_path / "analysis.json"
    artifact = {
        "metadata": {"generated_at": "bad"},
        "instruments": ["skip-me", {"symbol": ""}],
    }
    source.parent.mkdir(parents=True)
    source.write_text("source")
    analysis.write_text(json.dumps(artifact))

    update.update_wiki(source, analysis, wiki_root)
    first_log = (wiki_root / "log.md").read_text()
    update.update_wiki(source, analysis, wiki_root)

    assert (wiki_root / "wiki" / "instruments" / "unknown.md").exists()
    assert "ingest unknown" in first_log
    assert (wiki_root / "log.md").read_text() == first_log


def test_update_wiki_refresh_index_without_optional_sections(tmp_path):
    update = _load("update_wiki")
    wiki_root = tmp_path / "knowledge"
    wiki_root.mkdir()

    update.refresh_index(wiki_root)

    index = (wiki_root / "index.md").read_text()
    assert "## Instruments" not in index
    assert "## Rendered sources" not in index


def test_lint_wiki_reports_structural_source_and_log_errors(tmp_path):
    lint = _load("lint_wiki")
    wiki_root = tmp_path / "knowledge"
    wiki = wiki_root / "wiki"
    source_dir = wiki_root / "sources"
    wiki.mkdir(parents=True)
    source_dir.mkdir()
    (wiki_root / "index.md").write_text(
        "# Index\n\n[external](https://example.com) [anchor](#top) [empty](#)\n"
    )
    (wiki_root / "log.md").write_text("# Log\n")
    (wiki / "overview.md").write_text("# Overview\n")
    (wiki / "orphan.md").write_text("# Orphan\n")
    (wiki / "empty.md").write_text("\n")
    (source_dir / "2024-01-02-market-analysis.md").write_text("# Bad source\n")

    errors = lint.lint_wiki(wiki_root)

    assert "empty markdown page: wiki/empty.md" in errors
    assert "wiki page not reachable from index.md: wiki/orphan.md" in errors
    assert (
        "source missing generated marker: sources/2024-01-02-market-analysis.md"
        in errors
    )
    assert (
        "source missing artifact fingerprint: sources/2024-01-02-market-analysis.md"
        in errors
    )
    assert (
        "log missing latest source entry: sources/2024-01-02-market-analysis.md"
        in errors
    )
    assert not any("https://example.com" in error for error in errors)


def test_lint_wiki_cli_passes_for_existing_scaffold(capsys):
    lint = _load("lint_wiki")

    assert lint.main(["--wiki-root", "knowledge"]) == 0
    assert "Wiki lint passed: knowledge" in capsys.readouterr().out


def test_update_wiki_handles_missing_metadata_date(tmp_path):
    update = _load("update_wiki")
    wiki_root = tmp_path / "knowledge"
    source = wiki_root / "sources" / "missing-date.md"
    analysis = tmp_path / "analysis.json"
    source.parent.mkdir(parents=True)
    source.write_text("source")
    analysis.write_text(json.dumps({"instruments": []}))

    update.update_wiki(source, analysis, wiki_root)

    assert "ingest unknown" in (wiki_root / "log.md").read_text()
