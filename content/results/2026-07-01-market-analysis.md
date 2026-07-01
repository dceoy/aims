+++
title = "Market Analysis 2026-07-01"
date = "2026-07-01T00:00:00+00:00"
draft = false
summary = "Neutral market: 5 reliable instruments. Top signal: ^N225 (score 56.0)."
ticker_symbols = ["^DJI", "^GDAXI", "^GSPC", "^N225", "^NDX"]
source_files = ["data/analysis/2026-07-01.json", "data/history/2026-07-01.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "496d9c1"
+++

## Market Regime

**Neutral** — based on cross-sectional momentum scores of 5 reliable instrument(s) out of 5 total.

## Top Opportunities

- **^N225** — score 56.0, 20d return +3.1%, RSI14=67. 20d up +3.1%; above MA20 by 2.8%; RSI14=67
- **^DJI** — score 48.0, 20d return +2.4%, RSI14=66. 20d up +2.4%; above MA20 by 1.8%; RSI14=66
- **^NDX** — score 48.0, 20d return -0.8%, RSI14=58. 20d down -0.8%; above MA20 by 1.8%; RSI14=58
- **^GDAXI** — score 40.0, 20d return -0.5%, RSI14=67. 20d down -0.5%; above MA20 by 0.9%; RSI14=67
- **^GSPC** — score 28.0, 20d return -1.3%, RSI14=56. 20d down -1.3%; above MA20 by 0.8%; RSI14=56

## Signal History

_No previous analysis artifact available._

## Instruments to Avoid

_All instruments passed quality checks._

## Key Risks

_No risk gates triggered._

## Instrument Scores

| Rank | Instrument | Score | Reliable | Risk Gates | Explanation                                  |
| ---: | ---------- | ----: | :------: | ---------- | -------------------------------------------- |
|    1 | ^N225      |  56.0 |   Yes    | —          | 20d up +3.1%; above MA20 by 2.8%; RSI14=67   |
|    2 | ^DJI       |  48.0 |   Yes    | —          | 20d up +2.4%; above MA20 by 1.8%; RSI14=66   |
|    3 | ^NDX       |  48.0 |   Yes    | —          | 20d down -0.8%; above MA20 by 1.8%; RSI14=58 |
|    4 | ^GDAXI     |  40.0 |   Yes    | —          | 20d down -0.5%; above MA20 by 0.9%; RSI14=67 |
|    5 | ^GSPC      |  28.0 |   Yes    | —          | 20d down -1.3%; above MA20 by 0.8%; RSI14=56 |

## Data Freshness

Data source: **yfinance**

| Symbol | Latest Bar |
| ------ | ---------- |
| ^DJI   | 2026-06-30 |
| ^GDAXI | 2026-06-30 |
| ^GSPC  | 2026-06-30 |
| ^N225  | 2026-07-01 |
| ^NDX   | 2026-06-30 |

## Symbol Details

### ^N225 (score 56.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.6% |
| ret_5d     |  +1.9% |
| ret_20d    |  +3.1% |
| ret_60d    | +34.4% |
| ma20_dist  |  +2.8% |
| ma50_dist  |  +8.8% |
| vol_20d    |  38.5% |
| mdd_60d    |   6.4% |
| rsi_14     |   66.8 |
| zscore_20d |    0.7 |

### ^DJI (score 48.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.3% |
| ret_5d     |  +1.3% |
| ret_20d    |  +2.4% |
| ret_60d    | +12.5% |
| ma20_dist  |  +1.8% |
| ma50_dist  |  +3.8% |
| vol_20d    |  14.4% |
| mdd_60d    |   3.2% |
| rsi_14     |   65.9 |
| zscore_20d |    1.5 |

### ^NDX (score 48.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.7% |
| ret_5d     |  +3.2% |
| ret_20d    |  -0.8% |
| ret_60d    | +25.9% |
| ma20_dist  |  +1.8% |
| ma50_dist  |  +4.3% |
| vol_20d    |  32.4% |
| mdd_60d    |   7.0% |
| rsi_14     |   58.4 |
| zscore_20d |    0.9 |

### ^GDAXI (score 40.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.5% |
| ret_5d     | +0.4% |
| ret_20d    | -0.5% |
| ret_60d    | +7.9% |
| ma20_dist  | +0.9% |
| ma50_dist  | +1.6% |
| vol_20d    | 14.0% |
| mdd_60d    |  4.7% |
| rsi_14     |  66.6 |
| zscore_20d |   0.9 |

### ^GSPC (score 28.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.8% |
| ret_5d     |  +1.8% |
| ret_20d    |  -1.3% |
| ret_60d    | +13.9% |
| ma20_dist  |  +0.8% |
| ma50_dist  |  +1.6% |
| vol_20d    |  17.3% |
| mdd_60d    |   4.5% |
| rsi_14     |   56.2 |
| zscore_20d |    0.6 |

## Methodology

Instruments are scored and ranked cross-sectionally using the following features:

- **Momentum**: 1-day, 5-day, 20-day, and 60-day returns
- **Trend**: Distance from 20-day and 50-day moving averages
- **Volatility**: 20-day realized annualized volatility (lower is better)
- **Drawdown**: Maximum drawdown over 60 days (lower is better)
- **RSI**: 14-day Relative Strength Index
- **Z-score**: Price z-score relative to 20-day mean

Each feature is converted to a cross-sectional percentile rank. The composite score is the mean percentile across all features (0–100).

Scoring engine version: **1.0.0** | Git commit: **496d9c1**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
