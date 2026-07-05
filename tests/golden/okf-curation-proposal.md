# OKF qualitative theme curation proposal — 2024-06-01

Deterministic pass over 3 qualitative artifact(s) from 2024-01-01 to 2024-01-20. Promotion is a human-reviewed pull request only — never auto-merged.

## Promotion candidates

### Copper supply squeeze deepens

Recurs on 3 distinct dates spanning 19 days:

- 2024-01-01 — "Copper supply squeeze tightens" (`data/qualitative/2024-01-01.json`; evidence: ev-a)
- 2024-01-10 — "Copper supply squeeze persists" (`data/qualitative/2024-01-10.json`; evidence: ev-b)
- 2024-01-20 — "Copper supply squeeze deepens" (`data/qualitative/2024-01-20.json`; evidence: ev-c)

Draft concept skeleton (edit before committing):

```
---
id: okf/concepts/theme-copper-supply-squeeze-deepens
title: Copper supply squeeze deepens
description: TODO — one-sentence qualitative description of the durable driver.
type: concept
tags: [qualitative-theme]
timestamp: 2024-06-01T00:00:00Z
resource:
  path: okf/concepts/theme-copper-supply-squeeze-deepens.md
  source: repository
status: proposed
theme_tokens: [copper, squeeze, supply, tightens]
---

# Copper supply squeeze deepens

TODO — describe the recurring driver qualitatively. Never assert
scores, ranks, dates, prices, risk gates, or data availability as
truth in prose; numeric facts stay pointers into `data/analysis/`.

## Observed in qualitative artifacts

- `data/qualitative/2024-01-01.json` (2024-01-01): "Copper supply squeeze tightens" — evidence: ev-a
- `data/qualitative/2024-01-10.json` (2024-01-10): "Copper supply squeeze persists" — evidence: ev-b
- `data/qualitative/2024-01-20.json` (2024-01-20): "Copper supply squeeze deepens" — evidence: ev-c

# Citations

- `data/qualitative/2024-01-01.json`
- `data/qualitative/2024-01-10.json`
- `data/qualitative/2024-01-20.json`
```

## Per-instrument stance streaks (supporting context)

- **HG=F** (cop) held `conflicting` on 3 dates (2024-01-01 to 2024-01-20)

## Retirement candidates

- `tests/fixtures/okf_concepts/theme-old.md` — Obsolete Regime Theme: last seen never in the loaded artifacts (archive after 60 days without recurrence)

## Curation checklist

- [ ] Review candidates; edit a draft into `okf/concepts/theme-<slug>.md` (cite dated artifacts; numeric facts stay pointers into `data/analysis/`)
- [ ] Record this pass — including "no promotions" — in `okf/logs/log.md`
- [ ] `uv run python tools/okf_hugo_adapter.py --src okf --dst content/knowledge --clean`
- [ ] `uv run python tools/okf_hugo_adapter.py --src okf --dst content/knowledge --check`
- [ ] `hugo --gc --minify`
- [ ] Open a human-reviewed PR — never auto-merge OKF changes
