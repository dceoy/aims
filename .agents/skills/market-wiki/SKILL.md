# market-wiki

Maintain the internal AIMS Market Knowledge Wiki: a Markdown-only, Git-managed research memory derived from immutable daily market analysis artifacts.

## Hard rules

1. Treat `data/analysis/*.json` as immutable source-of-truth inputs.
2. Do not invent numeric values, dates, ranks, instruments, risk gates, or data-quality facts.
3. Use `unknown` or `n/a` when the source does not contain a fact.
4. Preserve dated claims and distinguish historical observations from current observations.
5. On contradiction, update the relevant page and record the change in `knowledge/log.md`.
6. Update `knowledge/index.md` on every ingest.
7. Append to `knowledge/log.md` on every ingest, query-derived page update, or lint-driven maintenance pass.
8. Prefer small, focused wiki pages over one large monolithic report.
9. Cross-link related instruments, themes, regimes, and methodology pages.
10. Keep public Hugo content separate from the internal research wiki unless a later issue explicitly introduces public wiki publishing.

## Required reading before edits

Before editing `knowledge/wiki/**/*.md`, read:

- `knowledge/index.md`
- `knowledge/log.md`
- the relevant rendered source under `knowledge/sources/`
- the relevant source artifact under `data/analysis/`

## Scripts

### Render a deterministic source

```bash
uv run python .agents/skills/market-wiki/scripts/render_wiki_source.py \
  --input data/analysis/${DATE}.json \
  --output knowledge/sources/${DATE}-market-analysis.md
```

This script renders compact Markdown from a daily JSON artifact for agent ingestion. It performs no LLM summarization.

### Update wiki bookkeeping

```bash
uv run python .agents/skills/market-wiki/scripts/update_wiki.py \
  --source knowledge/sources/${DATE}-market-analysis.md \
  --analysis data/analysis/${DATE}.json \
  --wiki-root knowledge
```

This thin orchestration wrapper ensures baseline pages exist, refreshes `knowledge/index.md`, and appends an ingest entry to `knowledge/log.md`. Agents remain responsible for focused semantic page updates.

### Lint wiki structure

```bash
uv run python .agents/skills/market-wiki/scripts/lint_wiki.py --wiki-root knowledge
```

The lint checks required files, empty pages, reachable wiki pages, broken relative links, generated source fingerprints, and a log entry for the latest source.
