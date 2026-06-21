+++
title = "Market Analysis 2024-01-01"
date = "2024-01-01T01:00:00+00:00"
draft = false
summary = "Bullish market: 2 reliable instruments. Top signal: ^SPX (score 72.5)."
ticker_symbols = ["^DJI", "^NDX", "^SPX"]
source_files = ["data/analysis/2024-01-01.json"]
market_regime = "Bullish"
data_source = "stooq"
scoring_version = "1.0.0"
git_commit = "abc1234"
+++

## Market Regime

**Bullish** — based on cross-sectional momentum scores of 2 reliable instrument(s) out of 3 total.

## Top Opportunities

- **^SPX** — score 72.5, 20d return +5.3%, RSI14=62. 20d up +5.3%; above MA20 by 2.1%; RSI14=62
- **^DJI** — score 58.3, 20d return +2.1%, RSI14=55. 20d up +2.1%; above MA20 by 0.8%; RSI14=55

## Signal History

_No previous analysis artifact available._

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **^NDX** — insufficient_history

## Key Risks

- **insufficient_history** (1 instrument(s)): Insufficient history: some instruments lack enough historical data for reliable scoring.

## Instrument Scores

| Rank | Instrument | Score | Reliable | Risk Gates           | Explanation                                |
| ---: | ---------- | ----: | :------: | -------------------- | ------------------------------------------ |
|    1 | ^SPX       |  72.5 |   Yes    | —                    | 20d up +5.3%; above MA20 by 2.1%; RSI14=62 |
|    2 | ^DJI       |  58.3 |   Yes    | —                    | 20d up +2.1%; above MA20 by 0.8%; RSI14=55 |
|    3 | ^NDX       |  31.7 |    No    | insufficient_history | Suppressed: insufficient_history           |

## Data Freshness

Data source: **stooq**

| Symbol | Latest Bar |
| ------ | ---------- |
| ^DJI   | 2023-12-29 |
| ^NDX   | 2023-12-28 |
| ^SPX   | 2024-01-01 |

## Methodology

Instruments are scored and ranked cross-sectionally using the following features:

- **Momentum**: 1-day, 5-day, 20-day, and 60-day returns
- **Trend**: Distance from 20-day and 50-day moving averages
- **Volatility**: 20-day realized annualized volatility (lower is better)
- **Drawdown**: Maximum drawdown over 60 days (lower is better)
- **RSI**: 14-day Relative Strength Index
- **Z-score**: Price z-score relative to 20-day mean

Each feature is converted to a cross-sectional percentile rank. The composite score is the mean percentile across all features (0–100).

Scoring engine version: **1.0.0** | Git commit: **abc1234**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
