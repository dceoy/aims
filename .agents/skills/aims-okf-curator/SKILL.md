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

## Qualitative theme curation (#96)

Daily qualitative artifacts (`data/qualitative/*.json`) are point-in-time
snapshots; some of what they surface is durable and belongs in OKF. Run a
curation pass **monthly** (or when a theme visibly persists) once artifacts
have accumulated on `main`:

```sh
uv run .agents/skills/aims-okf-curator/scripts/curate_themes.py \
    --qualitative-dir data/qualitative \
    --concepts-dir okf/concepts
```

The script (delegating to `src/aims/okf_curation.py`) deterministically
clusters recurring theme titles across artifacts, prints promotion
candidates with dated artifact and evidence citations plus a ready-to-edit
concept skeleton, lists supporting per-instrument stance streaks, and flags
retirement candidates. Its output is a **proposal for human review** — it
never writes to `okf/` itself. With no accumulated artifacts it prints a
recorded empty pass. Promoted theme concepts must carry the
`qualitative-theme` tag and a `theme_tokens` front-matter list (the skeleton
includes both) so later passes can assess recurrence and retirement.

- **Promotion criteria:** promote a theme only when it recurs in artifacts
  from at least 3 distinct analysis dates spanning at least 14 days — never a
  single-day observation. Judge recurrence from `market.themes` titles and
  per-instrument drivers.
- **Concept content:** describe the driver qualitatively; cite the dated
  qualitative artifacts (`data/qualitative/YYYY-MM-DD.json`) and the evidence
  IDs they rest on. Numeric facts stay pointers into `data/analysis/`, per
  the guardrail above — never asserted as truth in OKF prose.
- **Review:** curation output is a human-reviewed pull request only; never
  auto-merge OKF changes. Record each pass (including "no promotions") in
  `okf/logs/log.md`, then regenerate shadow content (`--clean`), verify with
  `--check`, and build with `hugo --gc --minify`.
- **Retirement criteria:** archive a theme concept when it has not recurred
  in any qualitative artifact for 60 days (`curate_themes.py` flags these
  from `theme_tokens`), when the #93 gates repeatedly withheld the entries
  it rests on, or when it is contradicted by newer artifacts. Retirement
  follows the stale-concept cleanup flow (reviewed PR plus a log entry); do
  not silently delete.

## OKF primary references

- Google Cloud announcement: https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing
- OKF v0.1 draft specification: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
