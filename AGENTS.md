# Repository Guidelines

## Project Structure & Module Organization

This repository combines Python automation scripts with a Hugo static site. Core scripts live under `.agents/skills/`, especially `market-analysis/scripts/` and `update-cfd-instruments/scripts/`. Tests and fixtures are in `tests/`, with golden report output in `tests/golden/`. Data files and JSON schemas are in `data/` and `data/schema/`. Hugo content, archetypes, and configuration live in `content/`, `archetypes/`, and `config/_default/`; the generated site is written to the ignored `site/` directory.

## Build, Test, and Development Commands

- `uv sync --group dev`: install Python development tools from `uv.lock`.
- `uv run pytest`: run the Python test suite with branch coverage.
- `uv run ruff format .`: format Python files.
- `uv run ruff check --fix .`: lint and apply safe Ruff fixes.
- `uv run pyright .`: run strict type checks for skill scripts.
- `hugo --gc --minify`: build the static site.
- `hugo server --buildDrafts`: preview the site locally, including draft posts.
- `.agents/skills/local-qa/scripts/qa.sh`: run the full local QA workflow used by contributors.

## Coding Style & Naming Conventions

Python targets 3.11 through 3.13. Ruff enforces 88-character lines, Google-style docstrings, import sorting, and strict lint rules. Prefer typed functions and `pathlib` over string path manipulation. Apply KISS, DRY, and YAGNI: keep implementations simple, reuse existing helpers and patterns, and avoid abstractions or features before they are needed. Test files use `test_*.py`, and test names should describe behavior. Keep generated Hugo reports named like `YYYY-MM-DD-market-analysis.md` under `content/results/`.

## Market Knowledge Wiki

`knowledge/` is an internal, Markdown-only research memory derived from daily market analysis artifacts. Before editing wiki pages, agents must read `knowledge/index.md`, `knowledge/log.md`, the relevant `knowledge/sources/*.md` rendered source, and the corresponding `data/analysis/*.json` artifact.

`data/analysis/*.json` remains the immutable source of truth. `knowledge/sources/*.md` files are deterministic renderings for agent ingestion and should be regenerated with `render_wiki_source.py`, not manually summarized. `knowledge/wiki/**/*.md`, `knowledge/index.md`, and `knowledge/log.md` are derived memory maintained by agents.

Daily analysis can update the wiki with:

```bash
uv run python .agents/skills/market-wiki/scripts/render_wiki_source.py --input data/analysis/${DATE}.json --output knowledge/sources/${DATE}-market-analysis.md
uv run python .agents/skills/market-wiki/scripts/update_wiki.py --source knowledge/sources/${DATE}-market-analysis.md --analysis data/analysis/${DATE}.json --wiki-root knowledge
uv run python .agents/skills/market-wiki/scripts/lint_wiki.py --wiki-root knowledge
```

Generated analysis PRs should include `knowledge/` changes alongside `data/analysis/` and `content/results/` when wiki updates are enabled.

## Testing Guidelines

Pytest is configured in `pyproject.toml` and requires 100% branch coverage for the script directories under `.agents/skills/`. Add or update fixtures in `tests/fixtures/` and golden output in `tests/golden/` when changing report generation or parser behavior. Validate CFD data with:

```bash
uv run python .agents/skills/update-cfd-instruments/scripts/validate_cfd_instruments.py --input data/cfd_instruments.csv --schema data/schema/cfd_instruments.schema.json
```

## Commit & Pull Request Guidelines

Recent history uses concise Conventional Commit-style subjects such as `feat: ...`, `fix: ...`, and scoped variants like `feat(data): ...`. Keep commits focused and include issue or PR references when relevant. Pull requests should explain the change, list validation commands run, link related issues, and include screenshots or generated report paths when the Hugo output changes.

## Security & Configuration Tips

Do not commit secrets or local environment files. Operational details, scheduled workflows, Slack notifications, and required repository secrets are documented in `OPERATIONS.md`. GitHub Actions live in `.github/workflows/`; run the full QA script after workflow edits because it applies `zizmor`, `actionlint`, `yamllint`, and `checkov`.
