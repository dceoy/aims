# aims

AI Market Strategist

[![CI](https://github.com/dceoy/aims/actions/workflows/ci.yml/badge.svg)](https://github.com/dceoy/aims/actions/workflows/ci.yml)

## Static analysis site

Analysis results are saved as Hugo content under `content/results/` and rendered to the ignored `site/` directory.
The site uses the Congo Hugo theme via Hugo Modules, so local Hugo builds require a Go toolchain in addition to Hugo Extended.

Create a new result:

```bash
hugo new results/YYYY-MM-DD-market-analysis.md
```

Set `draft = false` in the generated front matter when the result is ready to publish, then build the static site:

```bash
hugo --gc --minify
```

Preview drafts locally with:

```bash
hugo server --buildDrafts
```

## Automated analysis pipeline

Daily market analysis runs automatically via `.github/workflows/daily-market-analysis.yml`. It fetches market data, scores instruments, generates JSON artifacts and Hugo Markdown reports, builds the site, and creates a pull request with the results for review and merging.

See [OPERATIONS.md](OPERATIONS.md) for data sources, scoring methodology, required secrets, and operational runbooks.

## OKF knowledge layer

AIMS uses an OKF-first knowledge layer for durable repository knowledge. AIMS targets OKF v0.1 Draft as described in the [OKF v0.1 draft specification](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) and the [Google Cloud OKF announcement](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing):

- `okf/` is the canonical source for stable concepts about architecture, data sources, scoring methodology, operations, and Agent Skills.
- `data/analysis/*.json` remains authoritative for numeric market facts, scores, ranks, dates, risk gates, and data availability.
- `content/results/` remains the public daily market-analysis report output.
- `content/knowledge/` is generated Hugo shadow content derived from `okf/` and must not be hand-edited.
- Repository-local Agent Skills under `.agents/skills/` guide OKF authoring, curation, Hugo generation, and PR review.

After editing `okf/`, regenerate and validate the Hugo shadow content, then build the site:

```bash
uv run python tools/okf_hugo_adapter.py --src okf --dst content/knowledge --clean
uv run python tools/okf_hugo_adapter.py --src okf --dst content/knowledge --check
hugo --gc --minify
```

Do not hand-edit `content/knowledge/`. If Markdown formatting or other tooling changes the generated files, fix drift by regenerating from `okf/` with the adapter rather than editing the shadow content directly.

The adapter deterministically maps OKF reserved `index.md` files to Hugo `_index.md` files, accepts OKF v0.1 reserved files without concept front matter, and moves non-reserved OKF front matter `type` into `params.okf_type` so Hugo can use a stable `type: knowledge` presentation type.
