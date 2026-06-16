---
name: aims-okf-curator
description: Maintain OKF indexes, logs, tags, cross-links, duplicate consolidation, and stale concept cleanup.
disable-model-invocation: false
---

# AIMS OKF curation

Keep tags lowercase kebab-case. Ensure `okf/index.md` links durable concepts and `okf/logs/log.md` records meaningful curation changes. Run the adapter with `--check` to catch broken links and drift.

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
