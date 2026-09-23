+++
title = "Market Analysis 2026-09-23"
date = "2026-09-23T00:00:00+00:00"
draft = false
summary = "Neutral market: 13 reliable instruments. Top signal: ZC=F (score 83.0)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-09-23.json", "data/history/2026-09-23.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "a092d79"
+++

## Market Regime

**Neutral** — 5 of 13 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Corn / ZC=F** — score 83.0, 20d return +9.2%, RSI14=60. 20d up +9.2%; above MA20 by 3.4%; RSI14=60
- **Platinum / PL=F** — score 79.4, 20d return -1.6%, RSI14=58. 20d down -1.6%; above MA20 by 0.7%; RSI14=58
- **Soybeans / ZS=F** — score 79.4, 20d return +9.0%, RSI14=55. 20d up +9.0%; above MA20 by 2.4%; RSI14=55
- **FTSE 100 / ^FTSE** — score 73.3, 20d return -0.7%, RSI14=47. 20d down -0.7%; below MA20 by 0.2%; RSI14=47
- **Hang Seng / ^HSI** — score 72.4, 20d return -1.6%, RSI14=46. 20d down -1.6%; below MA20 by 0.3%; RSI14=46

## Upcoming Events

_No scheduled events for covered instruments in the next 7 days._

## Signal History

Compared with the previous available report (**2026-09-22**).

- **New top-5:** PL=F, ^FTSE, ^HSI
- **Persistent top signals:** ZC=F (6 reports), ZS=F (3 reports)
- **Dropped from top-5:** AAPL, META, ^NDX
- **AAPL risk gates:** added high_volatility, malformed_input; removed none
- **AMZN risk gates:** added high_volatility, malformed_input; removed none
- **GOOGL risk gates:** added high_volatility, malformed_input; removed none
- **JPM risk gates:** added high_volatility, malformed_input; removed none
- **META risk gates:** added high_volatility, malformed_input; removed none
- **MSFT risk gates:** added high_volatility, malformed_input; removed none
- **NVDA risk gates:** added high_volatility, malformed_input; removed none
- **TSLA risk gates:** added high_volatility, malformed_input; removed none
- **UNH risk gates:** added high_volatility, malformed_input; removed none
- **XOM risk gates:** added high_volatility; removed none
- **^DJI risk gates:** added high_volatility, malformed_input; removed none
- **^GSPC risk gates:** added high_volatility, malformed_input; removed none
- **^NDX risk gates:** added high_volatility, malformed_input; removed none

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |    +11 |   +28.8 |
| 7203.T    |    +11 |   +27.9 |
| 8306.T    |    +10 |   +24.2 |
| AAPL      |    -19 |   -59.4 |
| AMZN      |    -16 |   -45.1 |
| BZ=F      |     +8 |   +20.6 |
| CL=F      |    +11 |   +19.4 |
| GC=F      |    +11 |   +25.5 |
| GOOGL     |    -17 |   -50.0 |
| HG=F      |    +12 |   +21.8 |
| JPM       |    -14 |   -37.6 |
| META      |    -19 |   -66.1 |
| MSFT      |    -21 |   -55.8 |
| NG=F      |    +18 |   +52.4 |
| NVDA      |    -15 |   -56.7 |
| PL=F      |    +17 |   +36.4 |
| SI=F      |    +10 |   +24.5 |
| TSLA      |    -13 |   -46.7 |
| UNH       |     +0 |    -7.3 |
| XOM       |     +4 |   -18.2 |
| ZC=F      |     +0 |    +1.2 |
| ZS=F      |     +0 |    +4.8 |
| ZW=F      |     +1 |    +5.8 |
| ^DJI      |     -8 |   -24.9 |
| ^FCHI     |    +11 |   +28.8 |
| ^FTSE     |     +9 |   +22.1 |
| ^GDAXI    |    +11 |   +25.1 |
| ^GSPC     |    -26 |   -60.6 |
| ^HSI      |    +10 |   +25.1 |
| ^N225     |    +12 |   +27.3 |
| ^NDX      |    -29 |   -65.5 |
| ^RUT      |    +11 |   +30.6 |
| ^STOXX50E |     +9 |   +23.0 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Copper / HG=F** — malformed_input
- **Natural Gas / NG=F** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Meta Platforms Inc. / META** — malformed_input, high_volatility
- **NVIDIA Corporation / NVDA** — malformed_input, high_volatility
- **Tesla Inc. / TSLA** — malformed_input, high_volatility
- **Apple Inc. / AAPL** — malformed_input, high_volatility
- **UnitedHealth Group Inc. / UNH** — malformed_input, high_volatility
- **Alphabet Inc. Class A / GOOGL** — malformed_input, high_volatility
- **Amazon.com Inc. / AMZN** — malformed_input, high_volatility
- **Exxon Mobil Corporation / XOM** — malformed_input, high_volatility
- **Microsoft Corporation / MSFT** — malformed_input, high_volatility
- **Dow Jones Industrial Average / ^DJI** — malformed_input, high_volatility
- **JPMorgan Chase & Co. / JPM** — malformed_input, high_volatility
- **S&P 500 / ^GSPC** — malformed_input, high_volatility
- **NASDAQ 100 / ^NDX** — malformed_input, high_volatility

## Key Risks

- **high_volatility** (13 instrument(s)): High volatility: one or more instruments show extreme volatility.
- **malformed_input** (19 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|    1 | Corn / ZC=F            |  83.0 |   Yes    | —               | 20d up +9.2%; above MA20 by 3.4%; RSI14=60   |
|    2 | Platinum / PL=F        |  79.4 |   Yes    | —               | 20d down -1.6%; above MA20 by 0.7%; RSI14=58 |
|    3 | Soybeans / ZS=F        |  79.4 |   Yes    | —               | 20d up +9.0%; above MA20 by 2.4%; RSI14=55   |
|    6 | Brent Crude Oil / BZ=F |  71.2 |   Yes    | —               | 20d up +12.0%; above MA20 by 0.5%; RSI14=56  |
|    8 | Silver / SI=F          |  68.5 |   Yes    | —               | 20d down -3.9%; above MA20 by 0.1%; RSI14=54 |
|   10 | Gold / GC=F            |  61.5 |   Yes    | —               | 20d down -6.8%; below MA20 by 1.7%; RSI14=46 |
|   11 | Wheat / ZW=F           |  59.4 |   Yes    | —               | 20d up +5.2%; below MA20 by 1.6%; RSI14=36   |
|   14 | Copper / HG=F          |  83.3 |    No    | malformed_input | Suppressed: malformed_input                  |
|   15 | Natural Gas / NG=F     |  74.5 |    No    | malformed_input | Suppressed: malformed_input                  |
|   16 | WTI Crude Oil / CL=F   |  70.3 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                       | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | -------------------------------- | -------------------------------------------- |
|   18 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  65.2 |    No    | malformed_input, missing_bars    | Suppressed: malformed_input, missing_bars    |
|   19 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  59.1 |    No    | malformed_input, missing_bars    | Suppressed: malformed_input, missing_bars    |
|   20 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  57.3 |    No    | malformed_input, missing_bars    | Suppressed: malformed_input, missing_bars    |
|   21 | Meta Platforms Inc. / META                                                     |  11.5 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   22 | NVIDIA Corporation / NVDA                                                      |  10.9 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   23 | Tesla Inc. / TSLA                                                              |  10.9 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   24 | Apple Inc. / AAPL                                                              |  10.6 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   25 | UnitedHealth Group Inc. / UNH                                                  |  10.6 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   26 | Alphabet Inc. Class A / GOOGL                                                  |  10.3 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   27 | Amazon.com Inc. / AMZN                                                         |  10.0 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   28 | Exxon Mobil Corporation / XOM                                                  |  10.0 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   29 | Microsoft Corporation / MSFT                                                   |   8.8 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   31 | JPMorgan Chase & Co. / JPM                                                     |   8.2 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates                       | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | -------------------------------- | -------------------------------------------- |
|    4 | FTSE 100 / ^FTSE                    |  73.3 |   Yes    | —                                | 20d down -0.7%; below MA20 by 0.2%; RSI14=47 |
|    5 | Hang Seng / ^HSI                    |  72.4 |   Yes    | —                                | 20d down -1.6%; below MA20 by 0.3%; RSI14=46 |
|    7 | Euro Stoxx 50 / ^STOXX50E           |  69.7 |   Yes    | —                                | 20d down -2.0%; below MA20 by 0.6%; RSI14=46 |
|    9 | DAX / ^GDAXI                        |  67.0 |   Yes    | —                                | 20d down -2.0%; below MA20 by 1.1%; RSI14=42 |
|   12 | CAC 40 / ^FCHI                      |  58.5 |   Yes    | —                                | 20d down -3.7%; below MA20 by 1.3%; RSI14=39 |
|   13 | Russell 2000 / ^RUT                 |  56.1 |   Yes    | —                                | 20d down -4.7%; below MA20 by 2.0%; RSI14=36 |
|   17 | Nikkei 225 / ^N225                  |  66.7 |    No    | missing_bars                     | Suppressed: missing_bars                     |
|   30 | Dow Jones Industrial Average / ^DJI |   8.8 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   32 | S&P 500 / ^GSPC                     |   7.9 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   33 | NASDAQ 100 / ^NDX                   |   7.6 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-09-18 |
| 7203.T    | 2026-09-18 |
| 8306.T    | 2026-09-18 |
| AAPL      | 2026-09-22 |
| AMZN      | 2026-09-22 |
| BZ=F      | 2026-09-22 |
| CL=F      | 2026-09-22 |
| GC=F      | 2026-09-22 |
| GOOGL     | 2026-09-22 |
| HG=F      | 2026-09-22 |
| JPM       | 2026-09-22 |
| META      | 2026-09-22 |
| MSFT      | 2026-09-22 |
| NG=F      | 2026-09-22 |
| NVDA      | 2026-09-22 |
| PL=F      | 2026-09-22 |
| SI=F      | 2026-09-22 |
| TSLA      | 2026-09-22 |
| UNH       | 2026-09-22 |
| XOM       | 2026-09-22 |
| ZC=F      | 2026-09-22 |
| ZS=F      | 2026-09-22 |
| ZW=F      | 2026-09-22 |
| ^DJI      | 2026-09-22 |
| ^FCHI     | 2026-09-21 |
| ^FTSE     | 2026-09-21 |
| ^GDAXI    | 2026-09-21 |
| ^GSPC     | 2026-09-22 |
| ^HSI      | 2026-09-22 |
| ^N225     | 2026-09-18 |
| ^NDX      | 2026-09-22 |
| ^RUT      | 2026-09-21 |
| ^STOXX50E | 2026-09-21 |

## Symbol Details

### Corn / ZC=F (score 83.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.2% |
| ret_5d     |  +0.2% |
| ret_20d    |  +9.2% |
| ret_60d    | +27.5% |
| ma20_dist  |  +3.4% |
| ma50_dist  | +11.2% |
| vol_20d    |  23.9% |
| mdd_60d    |   6.0% |
| rsi_14     |   59.6 |
| zscore_20d |    1.6 |

### Platinum / PL=F (score 79.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.3% |
| ret_5d     |  +2.8% |
| ret_20d    |  -1.6% |
| ret_60d    | +12.7% |
| ma20_dist  |  +0.7% |
| ma50_dist  |  +3.7% |
| vol_20d    |  32.7% |
| mdd_60d    |   7.4% |
| rsi_14     |   58.5 |
| zscore_20d |    0.3 |

### Soybeans / ZS=F (score 79.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.2% |
| ret_5d     |  +0.5% |
| ret_20d    |  +9.0% |
| ret_60d    | +17.7% |
| ma20_dist  |  +2.4% |
| ma50_dist  |  +7.4% |
| vol_20d    |  20.8% |
| mdd_60d    |   8.1% |
| rsi_14     |   55.2 |
| zscore_20d |    1.2 |

### FTSE 100 / ^FTSE (score 73.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | +0.4% |
| ret_20d    | -0.7% |
| ret_60d    | +2.2% |
| ma20_dist  | -0.2% |
| ma50_dist  | -0.1% |
| vol_20d    | 10.2% |
| mdd_60d    |  2.7% |
| rsi_14     |  47.1 |
| zscore_20d |  -0.3 |

### Hang Seng / ^HSI (score 72.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +1.8% |
| ret_20d    | -1.6% |
| ret_60d    | +9.0% |
| ma20_dist  | -0.3% |
| ma50_dist  | -0.9% |
| vol_20d    | 11.6% |
| mdd_60d    |  5.4% |
| rsi_14     |  45.7 |
| zscore_20d |  -0.2 |

### Brent Crude Oil / BZ=F (score 71.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.1% |
| ret_5d     |  -8.7% |
| ret_20d    | +12.0% |
| ret_60d    | +38.2% |
| ma20_dist  |  +0.5% |
| ma50_dist  |  +6.8% |
| vol_20d    |  38.3% |
| mdd_60d    |  21.2% |
| rsi_14     |   56.3 |
| zscore_20d |    0.1 |

### Euro Stoxx 50 / ^STOXX50E (score 69.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.3% |
| ret_5d     | +0.9% |
| ret_20d    | -2.0% |
| ret_60d    | +1.4% |
| ma20_dist  | -0.6% |
| ma50_dist  | -0.9% |
| vol_20d    | 12.7% |
| mdd_60d    |  4.8% |
| rsi_14     |  45.8 |
| zscore_20d |  -0.5 |

### Silver / SI=F (score 68.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | +4.3% |
| ret_20d    | -3.9% |
| ret_60d    | +8.7% |
| ma20_dist  | +0.1% |
| ma50_dist  | +3.1% |
| vol_20d    | 33.3% |
| mdd_60d    |  9.7% |
| rsi_14     |  53.9 |
| zscore_20d |   0.0 |

### DAX / ^GDAXI (score 67.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | +0.5% |
| ret_20d    | -2.0% |
| ret_60d    | +3.8% |
| ma20_dist  | -1.1% |
| ma50_dist  | -0.8% |
| vol_20d    | 12.8% |
| mdd_60d    |  4.8% |
| rsi_14     |  41.8 |
| zscore_20d |  -0.8 |

### Gold / GC=F (score 61.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | +1.0% |
| ret_20d    | -6.8% |
| ret_60d    | +6.4% |
| ma20_dist  | -1.7% |
| ma50_dist  | +0.3% |
| vol_20d    | 19.0% |
| mdd_60d    |  7.9% |
| rsi_14     |  46.3 |
| zscore_20d |  -0.8 |

### Wheat / ZW=F (score 59.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.3% |
| ret_5d     |  -1.5% |
| ret_20d    |  +5.2% |
| ret_60d    | +21.2% |
| ma20_dist  |  -1.6% |
| ma50_dist  |  +3.8% |
| vol_20d    |  37.1% |
| mdd_60d    |  10.7% |
| rsi_14     |   36.4 |
| zscore_20d |   -0.6 |

### CAC 40 / ^FCHI (score 58.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | +0.3% |
| ret_20d    | -3.7% |
| ret_60d    | -2.7% |
| ma20_dist  | -1.3% |
| ma50_dist  | -3.2% |
| vol_20d    | 12.9% |
| mdd_60d    |  7.6% |
| rsi_14     |  38.7 |
| zscore_20d |  -0.9 |

### Russell 2000 / ^RUT (score 56.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | -0.6% |
| ret_20d    | -4.7% |
| ret_60d    | -4.4% |
| ma20_dist  | -2.0% |
| ma50_dist  | -3.1% |
| vol_20d    | 11.3% |
| mdd_60d    |  6.8% |
| rsi_14     |  35.5 |
| zscore_20d |  -1.1 |

## Risk Context

| Instrument                |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Corn / ZC=F               |  10.7500 |           2.0% |                 0.42x |       21.5000 |            4.0% |
| Platinum / PL=F           |  28.8500 |           1.6% |                 0.31x |       57.7000 |            3.2% |
| Soybeans / ZS=F           |  19.0357 |           1.4% |                 0.48x |       38.0714 |            2.9% |
| FTSE 100 / ^FTSE          | 105.0213 |           1.0% |                 0.98x |      210.0427 |            2.0% |
| Hang Seng / ^HSI          | 305.4987 |           1.2% |                 0.87x |      610.9975 |            2.4% |
| Brent Crude Oil / BZ=F    |   4.5529 |           4.6% |                 0.26x |        9.1057 |            9.2% |
| Euro Stoxx 50 / ^STOXX50E |  69.9357 |           1.1% |                 0.79x |      139.8713 |            2.2% |
| Silver / SI=F             |   1.4837 |           2.3% |                 0.30x |        2.9674 |            4.5% |
| DAX / ^GDAXI              | 272.3015 |           1.1% |                 0.78x |      544.6030 |            2.1% |
| Gold / GC=F               | 101.1571 |           2.3% |                 0.53x |      202.3141 |            4.6% |
| Wheat / ZW=F              |  17.2321 |           2.4% |                 0.27x |       34.4643 |            4.8% |
| CAC 40 / ^FCHI            |  83.7731 |           1.0% |                 0.77x |      167.5461 |            2.1% |
| Russell 2000 / ^RUT       |  32.9093 |           1.1% |                 0.89x |       65.8186 |            2.3% |

> Volatility-targeted sizing and ATR-based stop distances are informational sizing/stop hints derived from historical price action, not investment advice, account-level guidance, or margin-call simulation. They ignore account size, existing exposure, broker margin rules, and execution costs.

## Methodology

Instruments are scored and ranked cross-sectionally using the following features:

- **Momentum**: 1-day, 5-day, 20-day, and 60-day returns
- **Trend**: Distance from 20-day and 50-day moving averages
- **Volatility**: 20-day realized annualized volatility (lower is better)
- **Drawdown**: Maximum drawdown over 60 days (lower is better)
- **RSI**: 14-day Relative Strength Index
- **Z-score**: Price z-score relative to 20-day mean

Each feature is converted to a cross-sectional percentile rank. The composite score is the mean percentile across all features (0–100).

Scoring engine version: **1.0.0** | Git commit: **a092d79**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
