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

## Market-theme curation from qualitative artifacts

Periodically (weekly, or when asked) review recent `data/qualitative/*.json` artifacts and decide whether any _recurring_ theme deserves promotion into a durable OKF concept.

Promotion criteria — promote only themes that:

- recur across at least three dated qualitative artifacts (single-day observations are point-in-time, not durable knowledge);
- survived grounding gates in those artifacts (never promote gated content);
- describe drivers qualitatively (a rate cycle, a supply regime), not numeric market facts.

How to promote:

1. Author a concept under `okf/concepts/` (kebab-case id, tags including `market-theme`) describing the theme qualitatively.
2. Cite the dated qualitative artifacts (`data/qualitative/YYYY-MM-DD.json`) and the evidence source URLs the theme derives from in the Citations section.
3. Link the concept from `okf/index.md`, record the promotion in `okf/logs/log.md`, regenerate shadow content, and run the adapter `--check` plus `hugo --gc --minify`.
4. Open a pull request for human review. Market-theme concepts are never merged without review, and no automation may auto-merge OKF changes.

Retirement: when a promoted theme stops appearing in qualitative artifacts for roughly a month, or is contradicted by newer gated-free artifacts, mark it superseded in the log and remove it from `okf/index.md` (stale-concept cleanup above applies).

Guardrails (in addition to the ones above): scores, ranks, dates, prices, and data availability stay in `data/analysis/*.json`; a theme concept may point at those artifacts but never restate their numbers as durable truth.
