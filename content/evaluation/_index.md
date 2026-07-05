+++
title = "AI Stance Evaluation"
date = "2026-07-04T00:00:00+00:00"
draft = false
summary = "AI stance evaluation as of 2026-07-04: no matured observations yet."
source_files = ["data/performance/2026-07-04.json"]
+++

This page evaluates the AI qualitative layer's published per-instrument stances (supportive / neutral / conflicting) against realized forward returns reconstructed deterministically from committed analysis artifacts. A supportive stance counts as a hit when the instrument's forward return is positive; a conflicting stance counts as a hit when it is negative; neutral stances are tracked but not scored directionally.

> **Informational association only. These figures measure whether published AI stances lined up with subsequent price moves in committed data; they are not an investable or executable track record, exclude fees, slippage, financing, and order timing, rest on small overlapping samples, and are not investment advice.**

## Stance Hit Rates

_No matured stance observations yet. Stances need enough subsequent committed analysis artifacts to cover each forward horizon before they can be scored; this page fills in as qualitative artifacts and forward bars accumulate._

## Data Status

- Analysis artifacts: 5 (2026-06-29 to 2026-07-04)
- Qualitative artifacts: none
- Stance entries evaluated: 0 (gate-excluded: 0, unmatched: 0)
- Warnings (1):
  - no qualitative artifacts found; stance evaluation is empty

## Methodology

Forward returns are compounded from each symbol's trailing `ret_1d` feature chained across committed analysis artifacts, keyed by the per-symbol bar date in `data_freshness` — no live price fetches. Wherever a later artifact carries `ret_5d`, the compounded chain must reproduce it within tolerance; windows failing that self-check are skipped as broken rather than scored. Stances withheld by the qualitative consistency gates are excluded. Details: `data/schema/performance.schema.json` and OPERATIONS.md §12.
