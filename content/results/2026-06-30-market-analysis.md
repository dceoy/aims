+++
title = "Market Analysis 2026-06-30"
date = "2026-06-30T00:00:00+00:00"
draft = false
summary = "Bearish market: 5 reliable instruments. Top signal: ^DJI (score 62.0)."
ticker_symbols = ["^DJI", "^GDAXI", "^GSPC", "^N225", "^NDX"]
source_files = ["data/analysis/2026-06-30.json", "data/history/2026-06-30.json"]
market_regime = "Bearish"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "55dedd9"
+++

## Market Regime

**Bearish** — based on cross-sectional momentum scores of 5 reliable instrument(s) out of 5 total.

## Top Opportunities

- **^DJI** — score 62.0, 20d return +2.3%, RSI14=66. 20d up +2.3%; above MA20 by 1.6%; RSI14=66
- **^N225** — score 62.0, 20d return +5.2%, RSI14=66. 20d up +5.2%; above MA20 by 2.5%; RSI14=66
- **^NDX** — score 38.0, 20d return -1.8%, RSI14=53. 20d down -1.8%; above MA20 by 0.1%; RSI14=53
- **^GSPC** — score 34.0, 20d return -1.8%, RSI14=52. 20d down -1.8%; below MA20 by 0.1%; RSI14=52
- **^GDAXI** — score 24.0, 20d return -1.5%, RSI14=54. 20d down -1.5%; below MA20 by 0.6%; RSI14=54

## Signal History

_No previous analysis artifact available._

## Instruments to Avoid

_All instruments passed quality checks._

## Key Risks

_No risk gates triggered._

## Instrument Scores

| Rank | Instrument | Score | Reliable | Risk Gates | Explanation                                  |
| ---: | ---------- | ----: | :------: | ---------- | -------------------------------------------- |
|    1 | ^DJI       |  62.0 |   Yes    | —          | 20d up +2.3%; above MA20 by 1.6%; RSI14=66   |
|    2 | ^N225      |  62.0 |   Yes    | —          | 20d up +5.2%; above MA20 by 2.5%; RSI14=66   |
|    3 | ^NDX       |  38.0 |   Yes    | —          | 20d down -1.8%; above MA20 by 0.1%; RSI14=53 |
|    4 | ^GSPC      |  34.0 |   Yes    | —          | 20d down -1.8%; below MA20 by 0.1%; RSI14=52 |
|    5 | ^GDAXI     |  24.0 |   Yes    | —          | 20d down -1.5%; below MA20 by 0.6%; RSI14=54 |

## Data Freshness

Data source: **yfinance**

| Symbol | Latest Bar |
| ------ | ---------- |
| ^DJI   | 2026-06-29 |
| ^GDAXI | 2026-06-29 |
| ^GSPC  | 2026-06-29 |
| ^N225  | 2026-06-30 |
| ^NDX   | 2026-06-29 |

## Symbol Details

### ^DJI (score 62.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.6% |
| ret_5d     |  +0.9% |
| ret_20d    |  +2.3% |
| ret_60d    | +12.1% |
| ma20_dist  |  +1.6% |
| ma50_dist  |  +3.6% |
| vol_20d    |  14.4% |
| mdd_60d    |   3.2% |
| rsi_14     |   65.5 |
| zscore_20d |    1.5 |

### ^N225 (score 62.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.1% |
| ret_5d     |  +0.6% |
| ret_20d    |  +5.2% |
| ret_60d    | +30.7% |
| ma20_dist  |  +2.5% |
| ma50_dist  |  +8.8% |
| vol_20d    |  39.4% |
| mdd_60d    |   6.4% |
| rsi_14     |   66.4 |
| zscore_20d |    0.7 |

### ^NDX (score 38.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.3% |
| ret_5d     |  -1.9% |
| ret_20d    |  -1.8% |
| ret_60d    | +24.0% |
| ma20_dist  |  +0.1% |
| ma50_dist  |  +2.8% |
| vol_20d    |  31.8% |
| mdd_60d    |   7.0% |
| rsi_14     |   52.6 |
| zscore_20d |    0.0 |

### ^GSPC (score 34.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.2% |
| ret_5d     |  -0.4% |
| ret_20d    |  -1.8% |
| ret_60d    | +13.2% |
| ma20_dist  |  -0.1% |
| ma50_dist  |  +0.9% |
| vol_20d    |  17.0% |
| mdd_60d    |   4.5% |
| rsi_14     |   52.0 |
| zscore_20d |   -0.1 |

### ^GDAXI (score 24.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | -2.0% |
| ret_20d    | -1.5% |
| ret_60d    | +5.7% |
| ma20_dist  | -0.6% |
| ma50_dist  | +0.1% |
| vol_20d    | 13.0% |
| mdd_60d    |  4.7% |
| rsi_14     |  54.2 |
| zscore_20d |  -0.6 |

## Methodology

Instruments are scored and ranked cross-sectionally using the following features:

- **Momentum**: 1-day, 5-day, 20-day, and 60-day returns
- **Trend**: Distance from 20-day and 50-day moving averages
- **Volatility**: 20-day realized annualized volatility (lower is better)
- **Drawdown**: Maximum drawdown over 60 days (lower is better)
- **RSI**: 14-day Relative Strength Index
- **Z-score**: Price z-score relative to 20-day mean

Each feature is converted to a cross-sectional percentile rank. The composite score is the mean percentile across all features (0–100).

Scoring engine version: **1.0.0** | Git commit: **55dedd9**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
