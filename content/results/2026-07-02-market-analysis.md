+++
title = "Market Analysis 2026-07-02"
date = "2026-07-02T00:00:00+00:00"
draft = false
summary = "Neutral market: 5 reliable instruments. Top signal: ^DJI (score 64.0)."
ticker_symbols = ["^DJI", "^GDAXI", "^GSPC", "^N225", "^NDX"]
source_files = ["data/analysis/2026-07-02.json", "data/history/2026-07-02.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "496d9c1"
+++

## Market Regime

**Neutral** — based on cross-sectional momentum scores of 5 reliable instrument(s) out of 5 total.

## Top Opportunities

- **^DJI** — score 64.0, 20d return +1.9%, RSI14=83. 20d up +1.9%; above MA20 by 1.6%; RSI14=83
- **^GDAXI** — score 50.0, 20d return +1.0%, RSI14=67. 20d up +1.0%; above MA20 by 1.0%; RSI14=67
- **^N225** — score 42.0, 20d return +3.2%, RSI14=60. 20d up +3.2%; above MA20 by 1.3%; RSI14=60
- **^GSPC** — score 40.0, 20d return -1.7%, RSI14=63. 20d down -1.7%; above MA20 by 0.6%; RSI14=63
- **^NDX** — score 24.0, 20d return -2.8%, RSI14=59. 20d down -2.8%; above MA20 by 0.4%; RSI14=59

## Signal History

_No previous analysis artifact available._

## Instruments to Avoid

_All instruments passed quality checks._

## Key Risks

_No risk gates triggered._

## Instrument Scores

| Rank | Instrument | Score | Reliable | Risk Gates | Explanation                                  |
| ---: | ---------- | ----: | :------: | ---------- | -------------------------------------------- |
|    1 | ^DJI       |  64.0 |   Yes    | —          | 20d up +1.9%; above MA20 by 1.6%; RSI14=83   |
|    2 | ^GDAXI     |  50.0 |   Yes    | —          | 20d up +1.0%; above MA20 by 1.0%; RSI14=67   |
|    3 | ^N225      |  42.0 |   Yes    | —          | 20d up +3.2%; above MA20 by 1.3%; RSI14=60   |
|    4 | ^GSPC      |  40.0 |   Yes    | —          | 20d down -1.7%; above MA20 by 0.6%; RSI14=63 |
|    5 | ^NDX       |  24.0 |   Yes    | —          | 20d down -2.8%; above MA20 by 0.4%; RSI14=59 |

## Data Freshness

Data source: **yfinance**

| Symbol | Latest Bar |
| ------ | ---------- |
| ^DJI   | 2026-07-01 |
| ^GDAXI | 2026-07-01 |
| ^GSPC  | 2026-07-01 |
| ^N225  | 2026-07-02 |
| ^NDX   | 2026-07-01 |

## Symbol Details

### ^DJI (score 64.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.0% |
| ret_5d     |  +0.9% |
| ret_20d    |  +1.9% |
| ret_60d    | +12.1% |
| ma20_dist  |  +1.6% |
| ma50_dist  |  +3.6% |
| vol_20d    |  14.4% |
| mdd_60d    |   3.2% |
| rsi_14     |   83.1 |
| zscore_20d |    1.4 |

### ^GDAXI (score 50.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | +1.2% |
| ret_20d    | +1.0% |
| ret_60d    | +9.2% |
| ma20_dist  | +1.0% |
| ma50_dist  | +1.7% |
| vol_20d    | 13.2% |
| mdd_60d    |  4.7% |
| rsi_14     |  67.0 |
| zscore_20d |   1.0 |

### ^N225 (score 42.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.2% |
| ret_5d     |  -3.8% |
| ret_20d    |  +3.2% |
| ret_60d    | +31.0% |
| ma20_dist  |  +1.3% |
| ma50_dist  |  +7.1% |
| vol_20d    |  38.4% |
| mdd_60d    |   6.4% |
| rsi_14     |   60.1 |
| zscore_20d |    0.3 |

### ^GSPC (score 40.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.2% |
| ret_5d     |  +1.7% |
| ret_20d    |  -1.7% |
| ret_60d    | +13.2% |
| ma20_dist  |  +0.6% |
| ma50_dist  |  +1.3% |
| vol_20d    |  17.3% |
| mdd_60d    |   4.5% |
| rsi_14     |   63.3 |
| zscore_20d |    0.6 |

### ^NDX (score 24.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.5% |
| ret_5d     |  +2.0% |
| ret_20d    |  -2.8% |
| ret_60d    | +23.2% |
| ma20_dist  |  +0.4% |
| ma50_dist  |  +2.5% |
| vol_20d    |  32.7% |
| mdd_60d    |   7.0% |
| rsi_14     |   59.3 |
| zscore_20d |    0.2 |

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
