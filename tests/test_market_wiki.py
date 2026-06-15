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
