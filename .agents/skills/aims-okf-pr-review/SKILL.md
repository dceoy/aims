---
name: aims-okf-pr-review
description: Review changes touching OKF, generated knowledge content, adapter code, skills, docs, or CI.
disable-model-invocation: false
---

# AIMS OKF PR review

Check that `okf/` is canonical, `content/knowledge/` is generated, generated content is up to date, and no vector database, external RAG service, custom CMS, or server runtime was introduced.

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
