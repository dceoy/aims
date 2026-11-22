# aims

AI Market Strategist

[![CI](https://github.com/dceoy/aims/actions/workflows/ci.yml/badge.svg)](https://github.com/dceoy/aims/actions/workflows/ci.yml)

## Automated data maintenance

AIMS maintains structured research data through independent GitHub Actions workflows:

- **Daily market analysis:** `.github/workflows/daily-market-analysis.yml` runs on weekdays, creates and validates machine-readable analysis, history, and performance JSON artifacts, and merges a data-only pull request. It does not generate articles or Hugo pages.
- **Event calendars:** `.github/workflows/update-calendars.yml` refreshes the earnings and central-bank event calendars every Monday (05:30 UTC).
- **CFD instruments:** `.github/workflows/update-cfd-instruments.yml` refreshes `data/cfd_instruments.csv` every Monday (05:00 UTC).

Scheduled Markdown report generation and GitHub Pages deployment have been retired. Existing reports under `content/results/` are historical snapshots, not new scheduled publications. The Hugo source and OKF adapter remain available for local/manual use; there is no automated website deployment.

See [OPERATIONS.md](OPERATIONS.md) for data sources, scoring methodology, and manual recovery procedures.

## OKF knowledge layer

AIMS uses an OKF-first knowledge layer for durable repository knowledge. AIMS targets OKF v0.2 as described in the [OKF v0.2 specification](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) and the [Google Cloud OKF announcement](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing):

- `okf/` is the canonical source for stable concepts about architecture, data sources, scoring methodology, operations, and Agent Skills.
- `data/analysis/*.json` remains authoritative for numeric market facts, scores, ranks, dates, risk gates, and data availability.
- `content/results/` preserves historical report output; automated publication is disabled.
- `content/knowledge/` is generated Hugo shadow content derived from `okf/` and must not be hand-edited.
- Repository-local Agent Skills under `.agents/skills/` guide OKF authoring, curation, Hugo generation, and PR review.

For optional local preview after editing `okf/`, regenerate and validate the Hugo shadow content, then build the site locally:

```bash
uv run python tools/okf_hugo_adapter.py --src okf --dst content/knowledge --clean
uv run python tools/okf_hugo_adapter.py --src okf --dst content/knowledge --check
hugo --gc --minify
```

Do not hand-edit `content/knowledge/`. If Markdown formatting or other tooling changes the generated files, fix drift by regenerating from `okf/` with the adapter rather than editing the shadow content directly.

The adapter deterministically maps OKF reserved `index.md` files to Hugo `_index.md` files, accepts OKF v0.2 reserved files without concept front matter, and moves non-reserved OKF front matter `type` into `params.okf_type` so Hugo can use a stable `type: knowledge` presentation type. Provenance, trust, lifecycle, freshness, attested-computation, and AIMS extension fields are preserved as structured `params.okf_metadata`.
