+++
title = "Market Analysis 2026-06-29"
date = "2026-06-29T00:00:00+00:00"
draft = false
summary = "Bearish market: 5 reliable instruments. Top signal: ^DJI (score 70.0)."
ticker_symbols = ["^DJI", "^GDAXI", "^GSPC", "^N225", "^NDX"]
source_files = ["data/analysis/2026-06-29.json", "data/history/2026-06-29.json"]
market_regime = "Bearish"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "55dedd9"
+++

## Market Regime

**Bearish** — based on cross-sectional momentum scores of 5 reliable instrument(s) out of 5 total.

## Top Opportunities

- **^DJI** — score 70.0, 20d return +2.4%, RSI14=62. 20d up +2.4%; above MA20 by 1.1%; RSI14=62
- **^N225** — score 52.0, 20d return +2.7%, RSI14=59. 20d up +2.7%; above MA20 by 0.7%; RSI14=59
- **^GDAXI** — score 38.0, 20d return -1.7%, RSI14=51. 20d down -1.7%; below MA20 by 0.5%; RSI14=51
- **^GSPC** — score 36.0, 20d return -2.8%, RSI14=48. 20d down -2.8%; below MA20 by 1.3%; RSI14=48
- **^NDX** — score 24.0, 20d return -3.7%, RSI14=51. 20d down -3.7%; below MA20 by 2.2%; RSI14=51

## Signal History

_No previous analysis artifact available._

## Instruments to Avoid

_All instruments passed quality checks._

## Key Risks

_No risk gates triggered._

## Instrument Scores

| Rank | Instrument | Score | Reliable | Risk Gates | Explanation                                  |
| ---: | ---------- | ----: | :------: | ---------- | -------------------------------------------- |
|    1 | ^DJI       |  70.0 |   Yes    | —          | 20d up +2.4%; above MA20 by 1.1%; RSI14=62   |
|    2 | ^N225      |  52.0 |   Yes    | —          | 20d up +2.7%; above MA20 by 0.7%; RSI14=59   |
|    3 | ^GDAXI     |  38.0 |   Yes    | —          | 20d down -1.7%; below MA20 by 0.5%; RSI14=51 |
|    4 | ^GSPC      |  36.0 |   Yes    | —          | 20d down -2.8%; below MA20 by 1.3%; RSI14=48 |
|    5 | ^NDX       |  24.0 |   Yes    | —          | 20d down -3.7%; below MA20 by 2.2%; RSI14=51 |

## Data Freshness

Data source: **yfinance**

| Symbol | Latest Bar |
| ------ | ---------- |
| ^DJI   | 2026-06-26 |
| ^GDAXI | 2026-06-26 |
| ^GSPC  | 2026-06-26 |
| ^N225  | 2026-06-29 |
| ^NDX   | 2026-06-26 |

## Symbol Details

### ^DJI (score 70.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.1% |
| ret_5d     |  +0.6% |
| ret_20d    |  +2.4% |
| ret_60d    | +11.9% |
| ma20_dist  |  +1.1% |
| ma50_dist  |  +3.1% |
| vol_20d    |  14.5% |
| mdd_60d    |   3.2% |
| rsi_14     |   61.8 |
| zscore_20d |    1.1 |

### ^N225 (score 52.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.9% |
| ret_5d     |  -5.0% |
| ret_20d    |  +2.7% |
| ret_60d    | +34.7% |
| ma20_dist  |  +0.7% |
| ma50_dist  |  +6.9% |
| vol_20d    |  39.5% |
| mdd_60d    |   6.4% |
| rsi_14     |   58.6 |
| zscore_20d |    0.2 |

### ^GDAXI (score 38.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.3% |
| ret_5d     | -1.3% |
| ret_20d    | -1.7% |
| ret_60d    | +8.8% |
| ma20_dist  | -0.5% |
| ma50_dist  | +0.3% |
| vol_20d    | 13.1% |
| mdd_60d    |  4.7% |
| rsi_14     |  51.1 |
| zscore_20d |  -0.5 |

### ^GSPC (score 36.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.0% |
| ret_5d     |  -2.0% |
| ret_20d    |  -2.8% |
| ret_60d    | +12.6% |
| ma20_dist  |  -1.3% |
| ma50_dist  |  -0.1% |
| vol_20d    |  16.5% |
| mdd_60d    |   4.5% |
| rsi_14     |   48.2 |
| zscore_20d |   -1.0 |

### ^NDX (score 24.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.1% |
| ret_5d     |  -4.2% |
| ret_20d    |  -3.7% |
| ret_60d    | +22.7% |
| ma20_dist  |  -2.2% |
| ma50_dist  |  +0.8% |
| vol_20d    |  30.8% |
| mdd_60d    |   7.0% |
| rsi_14     |   51.2 |
| zscore_20d |   -1.0 |

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
