+++
title = "Signal Performance"
date = "2026-07-08T00:00:00+00:00"
draft = false
summary = "Realized forward returns of the published top-5 signals vs. an equal-weight benchmark."
source_files = ["data/performance/signals.json"]
+++

## Signal Performance

As of **2026-07-08**, 9 daily analysis artifact(s) evaluated.

> Informational association only. These figures measure whether the published top-5 quantitative signals outperformed a naive equal-weight basket of the same day's reliable universe in committed data; they are not an investable or executable track record, exclude fees, slippage, financing, and order timing, rest on small overlapping samples, and are not investment advice.

## Cumulative Overview

| Horizon | Count |  Top-5 | Benchmark | Excess | Hit rate |
| ------- | ----: | -----: | --------: | -----: | -------: |
| 1d      |    28 | +0.24% |    +0.78% | -0.54% |      36% |
| 5d      |     6 | +1.17% |    +1.17% | +0.00% |      67% |
| 20d     |     0 |    n/a |       n/a |    n/a |      n/a |

### By Asset Class

| Horizon / Group   | Count | Excess | Hit rate |
| ----------------- | ----: | -----: | -------: |
| 1d / commodity    |     1 | +0.76% |     100% |
| 1d / equity       |     9 | -0.93% |      33% |
| 1d / equity_index |     6 | -1.26% |       0% |
| 1d / unknown      |    12 | +0.00% |      50% |
| 5d / unknown      |     6 | +0.00% |      67% |

### By Market Regime

| Horizon / Group  | Count | Excess | Hit rate |
| ---------------- | ----: | -----: | -------: |
| 1d / Unavailable |    28 | -0.54% |      36% |
| 5d / Unavailable |     6 | +0.00% |      67% |

## Warnings (19)

- 2026-06-29: ^GDAXI: broken bar chain within 1d forward window
- 2026-06-29: ^GDAXI: broken bar chain within 5d forward window
- 2026-06-29: ^N225: broken bar chain within 1d forward window
- 2026-06-29: ^N225: broken bar chain within 5d forward window
- 2026-06-30: ^GDAXI: broken bar chain within 1d forward window
- 2026-06-30: ^GDAXI: broken bar chain within 5d forward window
- 2026-06-30: ^N225: broken bar chain within 1d forward window
- 2026-06-30: ^N225: broken bar chain within 5d forward window
- 2026-07-01: ^GDAXI: broken bar chain within 1d forward window
- 2026-07-01: ^N225: broken bar chain within 1d forward window
- 2026-07-02: ^GDAXI: broken bar chain within 1d forward window
- 2026-07-02: ^N225: broken bar chain within 1d forward window
- 2026-07-04: ^GDAXI: broken bar chain within 1d forward window
- 2026-07-05: ^GDAXI: broken bar chain within 1d forward window
- 2026-07-06: ^GDAXI: broken bar chain within 1d forward window
- 2026-07-07: ^GDAXI: broken bar chain within 1d forward window
- ZC=F: conflicting ret_1d for bar 2026-07-02 across analysis artifacts; keeping the latest value
- ZS=F: conflicting ret_1d for bar 2026-07-02 across analysis artifacts; keeping the latest value
- ZW=F: conflicting ret_1d for bar 2026-07-02 across analysis artifacts; keeping the latest value
