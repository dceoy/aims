+++
title = "AI Stance Evaluation"
date = "2024-01-25T00:00:00+00:00"
draft = false
summary = "AI stance evaluation as of 2024-01-25: 10 matured stance observations."
source_files = ["data/performance/2024-01-25.json"]
+++

This page evaluates the AI qualitative layer's published per-instrument stances (supportive / neutral / conflicting) against realized forward returns reconstructed deterministically from committed analysis artifacts. A supportive stance counts as a hit when the instrument's forward return is positive; a conflicting stance counts as a hit when it is negative; neutral stances are tracked but not scored directionally.

> **Informational association only. These figures measure whether published AI stances lined up with subsequent price moves in committed data; they are not an investable or executable track record, exclude fees, slippage, financing, and order timing, rest on small overlapping samples, and are not investment advice.**

## Stance Hit Rates

### 1d horizon

4 matured, 0 pending, 0 skipped (broken bar chain).

| Stance      | Count | Hit rate | Average return |
| ----------- | ----: | -------: | -------------: |
| supportive  |     2 |     100% |         +1.00% |
| neutral     |     1 |      n/a |         +0.20% |
| conflicting |     1 |     100% |         -0.50% |

### 5d horizon

3 matured, 1 pending, 0 skipped (broken bar chain).

| Stance      | Count | Hit rate | Average return |
| ----------- | ----: | -------: | -------------: |
| supportive  |     1 |     100% |         +5.10% |
| neutral     |     1 |      n/a |         +1.00% |
| conflicting |     1 |     100% |         -2.48% |

### 20d horizon

3 matured, 1 pending, 0 skipped (broken bar chain).

| Stance      | Count | Hit rate | Average return |
| ----------- | ----: | -------: | -------------: |
| supportive  |     1 |     100% |        +22.02% |
| neutral     |     1 |      n/a |         +4.08% |
| conflicting |     1 |     100% |         -9.54% |

## Confidence Calibration

Directional stances (supportive and conflicting) grouped by the model's stated confidence; higher confidence should show a higher hit rate.

| Horizon / Confidence | Count | Hit rate |
| -------------------- | ----: | -------: |
| 1d / low             |     0 |      n/a |
| 1d / medium          |     1 |     100% |
| 1d / high            |     2 |     100% |
| 5d / low             |     0 |      n/a |
| 5d / medium          |     1 |     100% |
| 5d / high            |     1 |     100% |
| 20d / low            |     0 |      n/a |
| 20d / medium         |     1 |     100% |
| 20d / high           |     1 |     100% |

## Data Status

- Analysis artifacts: 25 (2024-01-01 to 2024-01-25)
- Qualitative artifacts: 2 (2024-01-01 to 2024-01-21)
- Stance entries evaluated: 4 (gate-excluded: 0, unmatched: 0)

## Methodology

Forward returns are compounded from each symbol's trailing `ret_1d` feature chained across committed analysis artifacts, keyed by the per-symbol bar date in `data_freshness` — no live price fetches. Wherever a later artifact carries `ret_5d`, the compounded chain must reproduce it within tolerance; windows failing that self-check are skipped as broken rather than scored. Stances withheld by the qualitative consistency gates are excluded. Details: `data/schema/performance.schema.json` and OPERATIONS.md §12.
