---
name: aims-okf-site
description: Generate Hugo shadow content from OKF and troubleshoot Hugo publication.
disable-model-invocation: false
---

# AIMS OKF site generation

Run `uv run python tools/okf_hugo_adapter.py --src okf --dst content/knowledge --clean`, then `hugo --gc --minify`. Keep `content/results/` and `content/knowledge/` separate in URLs and navigation.

## AIMS paths and commands

- Canonical OKF source: `okf/`
- Generated Hugo shadow content: `content/knowledge/`
- Daily report output: `content/results/`
- Numeric analysis artifacts: `data/analysis/*.json`
- Generate: `uv run python tools/okf_hugo_adapter.py --src okf --dst content/knowledge --clean`
- Check: `uv run python tools/okf_hugo_adapter.py --src okf --dst content/knowledge --check`
- Build: `hugo --gc --minify`

## Guardrails

- Do not let LLM-authored OKF prose become the source of truth for scores, ranks, dates, prices, risk gates, or data availability.
- Do not hand-edit `content/knowledge/`; regenerate it from `okf/`.
- Keep custom code small and deterministic.

## OKF primary references

- Google Cloud announcement: https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing
- OKF v0.1 draft specification: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
