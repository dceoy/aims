+++
title = "Market Analysis 2026-10-13"
date = "2026-10-13T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: MSFT (score 85.8)."
ticker_symbols = [
  "6758.T",
  "7203.T",
  "8306.T",
  "AAPL",
  "AMZN",
  "BZ=F",
  "CL=F",
  "GC=F",
  "GOOGL",
  "HG=F",
  "JPM",
  "META",
  "MSFT",
  "NG=F",
  "NVDA",
  "PL=F",
  "SI=F",
  "TSLA",
  "UNH",
  "XOM",
  "ZC=F",
  "ZS=F",
  "ZW=F",
  "^DJI",
  "^FCHI",
  "^FTSE",
  "^GDAXI",
  "^GSPC",
  "^HSI",
  "^N225",
  "^NDX",
  "^RUT",
  "^STOXX50E",
]
source_files = ["data/analysis/2026-10-13.json", "data/history/2026-10-13.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "b9858d1"
+++

## Market Regime

**Neutral** — 12 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Microsoft Corporation / MSFT** — score 85.8, 20d return +7.1%, RSI14=78. 20d up +7.1%; above MA20 by 5.7%; RSI14=78
- **Apple Inc. / AAPL** — score 67.9, 20d return +2.4%, RSI14=51. 20d up +2.4%; above MA20 by 1.5%; RSI14=51
- **Brent Crude Oil / BZ=F** — score 67.3, 20d return +0.9%, RSI14=65. 20d up +0.9%; above MA20 by 3.1%; RSI14=65
- **S&P 500 / ^GSPC** — score 66.7, 20d return +2.5%, RSI14=55. 20d up +2.5%; above MA20 by 1.2%; RSI14=55
- **Meta Platforms Inc. / META** — score 63.6, 20d return +11.7%, RSI14=52. 20d up +11.7%; above MA20 by 2.8%; RSI14=52

## Upcoming Events

_No scheduled events for covered instruments in the next 7 days._

## Signal History

Compared with the previous available report (**2026-10-12**).

- **New top-5:** AAPL, BZ=F, META
- **Persistent top signals:** MSFT (12 reports), ^GSPC (10 reports)
- **Dropped from top-5:** AMZN, TSLA, ^NDX

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +1 |    -0.9 |
| 7203.T    |     +0 |    +0.0 |
| 8306.T    |     +0 |    -1.8 |
| AAPL      |     +8 |   +15.8 |
| AMZN      |     -6 |   -10.9 |
| BZ=F      |     +4 |   +10.3 |
| CL=F      |     +0 |   +13.3 |
| GC=F      |     -2 |    -9.1 |
| GOOGL     |     -1 |    +1.2 |
| HG=F      |     +1 |    +4.5 |
| JPM       |     +4 |   +10.9 |
| META      |     +9 |   +17.9 |
| MSFT      |     +0 |    -1.5 |
| NG=F      |     -3 |   -12.1 |
| NVDA      |     -3 |    -6.4 |
| PL=F      |     +0 |    -5.5 |
| SI=F      |     -4 |   -11.5 |
| TSLA      |    -10 |   -18.5 |
| UNH       |     -5 |   -11.2 |
| XOM       |     +1 |    +9.7 |
| ZC=F      |     +1 |    +5.2 |
| ZS=F      |     +0 |    -6.1 |
| ZW=F      |     +0 |    +2.1 |
| ^DJI      |     +0 |    +3.6 |
| ^FCHI     |     +3 |    +2.7 |
| ^FTSE     |     +6 |    +7.9 |
| ^GDAXI    |     +4 |    +6.7 |
| ^GSPC     |     -2 |    -3.9 |
| ^HSI      |     -2 |    -1.8 |
| ^N225     |     +0 |    +0.9 |
| ^NDX      |     -6 |   -10.6 |
| ^RUT      |     -2 |    -5.8 |
| ^STOXX50E |     +4 |    +4.8 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Exxon Mobil Corporation / XOM** — malformed_input
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **Natural Gas / NG=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **WTI Crude Oil / CL=F** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|    3 | Brent Crude Oil / BZ=F |  67.3 |   Yes    | —               | 20d up +0.9%; above MA20 by 3.1%; RSI14=65   |
|   13 | Soybeans / ZS=F        |  43.9 |   Yes    | —               | 20d up +0.2%; below MA20 by 1.2%; RSI14=34   |
|   19 | Gold / GC=F            |  30.9 |   Yes    | —               | 20d down -3.7%; below MA20 by 1.6%; RSI14=32 |
|   22 | Platinum / PL=F        |  23.0 |   Yes    | —               | 20d down -5.4%; below MA20 by 2.8%; RSI14=32 |
|   23 | Corn / ZC=F            |  21.8 |   Yes    | —               | 20d down -5.7%; below MA20 by 6.3%; RSI14=19 |
|   24 | Silver / SI=F          |  18.5 |   Yes    | —               | 20d down -5.3%; below MA20 by 3.6%; RSI14=30 |
|   25 | Wheat / ZW=F           |  17.6 |   Yes    | —               | 20d down -4.9%; below MA20 by 3.9%; RSI14=30 |
|   28 | Copper / HG=F          |  68.2 |    No    | malformed_input | Suppressed: malformed_input                  |
|   29 | Natural Gas / NG=F     |  65.2 |    No    | malformed_input | Suppressed: malformed_input                  |
|   32 | WTI Crude Oil / CL=F   |  44.9 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    1 | Microsoft Corporation / MSFT                                                   |  85.8 |   Yes    | —                             | 20d up +7.1%; above MA20 by 5.7%; RSI14=78   |
|    2 | Apple Inc. / AAPL                                                              |  67.9 |   Yes    | —                             | 20d up +2.4%; above MA20 by 1.5%; RSI14=51   |
|    5 | Meta Platforms Inc. / META                                                     |  63.6 |   Yes    | —                             | 20d up +11.7%; above MA20 by 2.8%; RSI14=52  |
|    7 | Alphabet Inc. Class A / GOOGL                                                  |  58.5 |   Yes    | —                             | 20d up +1.0%; above MA20 by 1.9%; RSI14=52   |
|   10 | Amazon.com Inc. / AMZN                                                         |  57.3 |   Yes    | —                             | 20d up +2.4%; above MA20 by 2.9%; RSI14=55   |
|   12 | NVIDIA Corporation / NVDA                                                      |  46.1 |   Yes    | —                             | 20d up +7.3%; below MA20 by 0.5%; RSI14=46   |
|   15 | Tesla Inc. / TSLA                                                              |  42.4 |   Yes    | —                             | 20d up +5.3%; above MA20 by 2.3%; RSI14=49   |
|   16 | UnitedHealth Group Inc. / UNH                                                  |  40.3 |   Yes    | —                             | 20d down -1.3%; above MA20 by 1.0%; RSI14=55 |
|   17 | JPMorgan Chase & Co. / JPM                                                     |  39.4 |   Yes    | —                             | 20d down -4.0%; below MA20 by 0.9%; RSI14=43 |
|   26 | Exxon Mobil Corporation / XOM                                                  |  83.6 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   27 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  71.8 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   31 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  46.7 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   33 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  20.0 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    4 | S&P 500 / ^GSPC                     |  66.7 |   Yes    | —            | 20d up +2.5%; above MA20 by 1.2%; RSI14=55   |
|    6 | FTSE 100 / ^FTSE                    |  59.4 |   Yes    | —            | 20d down -0.4%; above MA20 by 0.4%; RSI14=46 |
|    8 | Dow Jones Industrial Average / ^DJI |  57.9 |   Yes    | —            | 20d down -1.1%; above MA20 by 0.7%; RSI14=50 |
|    9 | NASDAQ 100 / ^NDX                   |  57.9 |   Yes    | —            | 20d up +5.3%; above MA20 by 0.9%; RSI14=49   |
|   11 | DAX / ^GDAXI                        |  51.8 |   Yes    | —            | 20d down -0.6%; below MA20 by 0.2%; RSI14=44 |
|   14 | Euro Stoxx 50 / ^STOXX50E           |  43.9 |   Yes    | —            | 20d down -0.9%; below MA20 by 0.8%; RSI14=39 |
|   18 | Hang Seng / ^HSI                    |  39.4 |   Yes    | —            | 20d down -2.2%; below MA20 by 1.0%; RSI14=37 |
|   20 | CAC 40 / ^FCHI                      |  28.2 |   Yes    | —            | 20d down -3.5%; below MA20 by 1.9%; RSI14=27 |
|   21 | Russell 2000 / ^RUT                 |  27.6 |   Yes    | —            | 20d down -3.4%; below MA20 by 1.4%; RSI14=29 |
|   30 | Nikkei 225 / ^N225                  |  62.7 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-10-09 |
| 7203.T    | 2026-10-09 |
| 8306.T    | 2026-10-09 |
| AAPL      | 2026-10-12 |
| AMZN      | 2026-10-12 |
| BZ=F      | 2026-10-12 |
| CL=F      | 2026-10-12 |
| GC=F      | 2026-10-12 |
| GOOGL     | 2026-10-12 |
| HG=F      | 2026-10-12 |
| JPM       | 2026-10-12 |
| META      | 2026-10-12 |
| MSFT      | 2026-10-12 |
| NG=F      | 2026-10-12 |
| NVDA      | 2026-10-12 |
| PL=F      | 2026-10-12 |
| SI=F      | 2026-10-12 |
| TSLA      | 2026-10-12 |
| UNH       | 2026-10-12 |
| XOM       | 2026-10-12 |
| ZC=F      | 2026-10-12 |
| ZS=F      | 2026-10-12 |
| ZW=F      | 2026-10-12 |
| ^DJI      | 2026-10-12 |
| ^FCHI     | 2026-10-12 |
| ^FTSE     | 2026-10-12 |
| ^GDAXI    | 2026-10-12 |
| ^GSPC     | 2026-10-12 |
| ^HSI      | 2026-10-12 |
| ^N225     | 2026-10-09 |
| ^NDX      | 2026-10-12 |
| ^RUT      | 2026-10-12 |
| ^STOXX50E | 2026-10-12 |

## Symbol Details

### Microsoft Corporation / MSFT (score 85.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.1% |
| ret_5d     |  +3.0% |
| ret_20d    |  +7.1% |
| ret_60d    | +37.4% |
| ma20_dist  |  +5.7% |
| ma50_dist  |  +7.9% |
| vol_20d    |  21.6% |
| mdd_60d    |   5.1% |
| rsi_14     |   77.9 |
| zscore_20d |    2.0 |

### Apple Inc. / AAPL (score 67.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.3% |
| ret_5d     | +2.4% |
| ret_20d    | +2.4% |
| ret_60d    | +2.3% |
| ma20_dist  | +1.5% |
| ma50_dist  | +5.6% |
| vol_20d    | 16.5% |
| mdd_60d    | 11.0% |
| rsi_14     |  51.3 |
| zscore_20d |   1.5 |

### Brent Crude Oil / BZ=F (score 67.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.8% |
| ret_5d     | +6.3% |
| ret_20d    | +0.9% |
| ret_60d    | +5.9% |
| ma20_dist  | +3.1% |
| ma50_dist  | +9.8% |
| vol_20d    | 34.5% |
| mdd_60d    | 18.0% |
| rsi_14     |  65.1 |
| zscore_20d |   1.3 |

### S&P 500 / ^GSPC (score 66.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | +0.4% |
| ret_20d    | +2.5% |
| ret_60d    | +4.7% |
| ma20_dist  | +1.2% |
| ma50_dist  | +1.3% |
| vol_20d    |  9.5% |
| mdd_60d    |  3.2% |
| rsi_14     |  54.6 |
| zscore_20d |   1.3 |

### Meta Platforms Inc. / META (score 63.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +3.4% |
| ret_5d     |  +0.1% |
| ret_20d    | +11.7% |
| ret_60d    | +15.0% |
| ma20_dist  |  +2.8% |
| ma50_dist  | +15.5% |
| vol_20d    |  52.9% |
| mdd_60d    |  16.5% |
| rsi_14     |   51.6 |
| zscore_20d |    0.7 |

### FTSE 100 / ^FTSE (score 59.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.0% |
| ret_5d     | +1.5% |
| ret_20d    | -0.4% |
| ret_60d    | +0.5% |
| ma20_dist  | +0.4% |
| ma50_dist  | -0.6% |
| vol_20d    | 11.6% |
| mdd_60d    |  4.4% |
| rsi_14     |  46.5 |
| zscore_20d |   0.4 |

### Alphabet Inc. Class A / GOOGL (score 58.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +1.8% |
| ret_20d    | +1.0% |
| ret_60d    | +1.7% |
| ma20_dist  | +1.9% |
| ma50_dist  | +1.9% |
| vol_20d    | 20.5% |
| mdd_60d    | 12.4% |
| rsi_14     |  51.6 |
| zscore_20d |   1.4 |

### Dow Jones Industrial Average / ^DJI (score 57.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | +1.1% |
| ret_20d    | -1.1% |
| ret_60d    | -0.6% |
| ma20_dist  | +0.7% |
| ma50_dist  | -1.5% |
| vol_20d    |  9.6% |
| mdd_60d    |  6.3% |
| rsi_14     |  49.8 |
| zscore_20d |   1.0 |

### NASDAQ 100 / ^NDX (score 57.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | -1.3% |
| ret_20d    | +5.3% |
| ret_60d    | +7.2% |
| ma20_dist  | +0.9% |
| ma50_dist  | +2.8% |
| vol_20d    | 15.1% |
| mdd_60d    |  6.7% |
| rsi_14     |  48.7 |
| zscore_20d |   0.4 |

### Amazon.com Inc. / AMZN (score 57.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.1% |
| ret_5d     | +3.2% |
| ret_20d    | +2.4% |
| ret_60d    | +5.0% |
| ma20_dist  | +2.9% |
| ma50_dist  | +0.3% |
| vol_20d    | 24.7% |
| mdd_60d    | 13.4% |
| rsi_14     |  55.3 |
| zscore_20d |   1.5 |

### DAX / ^GDAXI (score 51.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.8% |
| ret_5d     | +0.1% |
| ret_20d    | -0.6% |
| ret_60d    | +1.7% |
| ma20_dist  | -0.2% |
| ma50_dist  | -2.0% |
| vol_20d    | 13.4% |
| mdd_60d    |  6.6% |
| rsi_14     |  44.2 |
| zscore_20d |  -0.2 |

### NVIDIA Corporation / NVDA (score 46.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.3% |
| ret_5d     |  -5.3% |
| ret_20d    |  +7.3% |
| ret_60d    | +11.6% |
| ma20_dist  |  -0.5% |
| ma50_dist  |  +1.7% |
| vol_20d    |  21.6% |
| mdd_60d    |  10.4% |
| rsi_14     |   46.4 |
| zscore_20d |   -0.2 |

### Soybeans / ZS=F (score 43.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | +0.5% |
| ret_20d    | +0.2% |
| ret_60d    | +4.4% |
| ma20_dist  | -1.2% |
| ma50_dist  | +2.1% |
| vol_20d    | 17.1% |
| mdd_60d    |  8.1% |
| rsi_14     |  34.0 |
| zscore_20d |  -1.0 |

### Euro Stoxx 50 / ^STOXX50E (score 43.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | -0.7% |
| ret_20d    | -0.9% |
| ret_60d    | -0.4% |
| ma20_dist  | -0.8% |
| ma50_dist  | -2.6% |
| vol_20d    | 12.9% |
| mdd_60d    |  6.5% |
| rsi_14     |  39.1 |
| zscore_20d |  -0.9 |

### Tesla Inc. / TSLA (score 42.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.2% |
| ret_5d     | -0.2% |
| ret_20d    | +5.3% |
| ret_60d    | -0.7% |
| ma20_dist  | +2.3% |
| ma50_dist  | +6.2% |
| vol_20d    | 29.4% |
| mdd_60d    | 21.3% |
| rsi_14     |  49.4 |
| zscore_20d |   0.8 |

### UnitedHealth Group Inc. / UNH (score 40.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.2% |
| ret_5d     |  -0.0% |
| ret_20d    |  -1.3% |
| ret_60d    | -11.2% |
| ma20_dist  |  +1.0% |
| ma50_dist  |  -2.3% |
| vol_20d    |  18.2% |
| mdd_60d    |  16.3% |
| rsi_14     |   55.5 |
| zscore_20d |    1.1 |

### JPMorgan Chase & Co. / JPM (score 39.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | +1.1% |
| ret_20d    | -4.0% |
| ret_60d    | -2.0% |
| ma20_dist  | -0.9% |
| ma50_dist  | -4.2% |
| vol_20d    | 16.7% |
| mdd_60d    |  9.9% |
| rsi_14     |  43.4 |
| zscore_20d |  -0.4 |

### Hang Seng / ^HSI (score 39.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | +1.0% |
| ret_20d    | -2.2% |
| ret_60d    | -1.2% |
| ma20_dist  | -1.0% |
| ma50_dist  | -3.4% |
| vol_20d    | 15.6% |
| mdd_60d    |  8.5% |
| rsi_14     |  36.7 |
| zscore_20d |  -0.7 |

### Gold / GC=F (score 30.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | +0.8% |
| ret_20d    | -3.7% |
| ret_60d    | +3.6% |
| ma20_dist  | -1.6% |
| ma50_dist  | -4.7% |
| vol_20d    | 16.9% |
| mdd_60d    | 12.0% |
| rsi_14     |  31.8 |
| zscore_20d |  -0.7 |

### CAC 40 / ^FCHI (score 28.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | -0.0% |
| ret_20d    | -3.5% |
| ret_60d    | -6.1% |
| ma20_dist  | -1.9% |
| ma50_dist  | -5.2% |
| vol_20d    | 12.1% |
| mdd_60d    | 11.4% |
| rsi_14     |  27.5 |
| zscore_20d |  -1.1 |

### Russell 2000 / ^RUT (score 27.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -1.8% |
| ret_20d    | -3.4% |
| ret_60d    | -5.7% |
| ma20_dist  | -1.4% |
| ma50_dist  | -4.6% |
| vol_20d    | 10.6% |
| mdd_60d    |  9.0% |
| rsi_14     |  29.0 |
| zscore_20d |  -1.3 |

### Platinum / PL=F (score 23.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.0% |
| ret_5d     | -1.6% |
| ret_20d    | -5.4% |
| ret_60d    | +5.0% |
| ma20_dist  | -2.8% |
| ma50_dist  | -5.3% |
| vol_20d    | 28.8% |
| mdd_60d    | 15.1% |
| rsi_14     |  32.4 |
| zscore_20d |  -0.9 |

### Corn / ZC=F (score 21.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | -2.9% |
| ret_20d    | -5.7% |
| ret_60d    | +4.5% |
| ma20_dist  | -6.3% |
| ma50_dist  | -3.1% |
| vol_20d    | 30.7% |
| mdd_60d    | 11.6% |
| rsi_14     |  18.8 |
| zscore_20d |  -1.8 |

### Silver / SI=F (score 18.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.9% |
| ret_5d     | -1.2% |
| ret_20d    | -5.3% |
| ret_60d    | +4.1% |
| ma20_dist  | -3.6% |
| ma50_dist  | -7.0% |
| vol_20d    | 27.8% |
| mdd_60d    | 15.0% |
| rsi_14     |  29.6 |
| zscore_20d |  -1.0 |

### Wheat / ZW=F (score 17.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | -2.9% |
| ret_20d    | -4.9% |
| ret_60d    | -4.7% |
| ma20_dist  | -3.9% |
| ma50_dist  | -3.6% |
| vol_20d    | 23.7% |
| mdd_60d    | 12.5% |
| rsi_14     |  30.0 |
| zscore_20d |  -1.4 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Microsoft Corporation / MSFT        |  12.2064 |           2.3% |                 0.46x |       24.4129 |            4.5% |
| Apple Inc. / AAPL                   |   6.4157 |           1.9% |                 0.61x |       12.8314 |            3.8% |
| Brent Crude Oil / BZ=F              |   4.5721 |           4.3% |                 0.29x |        9.1443 |            8.6% |
| S&P 500 / ^GSPC                     |  63.1293 |           0.8% |                 1.05x |      126.2586 |            1.6% |
| Meta Platforms Inc. / META          |  22.4586 |           3.0% |                 0.19x |       44.9172 |            6.0% |
| FTSE 100 / ^FTSE                    | 109.3641 |           1.0% |                 0.86x |      218.7282 |            2.1% |
| Alphabet Inc. Class A / GOOGL       |   8.0964 |           2.3% |                 0.49x |       16.1929 |            4.6% |
| Dow Jones Industrial Average / ^DJI | 458.9272 |           0.9% |                 1.04x |      917.8544 |            1.8% |
| NASDAQ 100 / ^NDX                   | 345.7669 |           1.1% |                 0.66x |      691.5338 |            2.3% |
| Amazon.com Inc. / AMZN              |   5.5729 |           2.1% |                 0.40x |       11.1457 |            4.3% |
| DAX / ^GDAXI                        | 307.0066 |           1.2% |                 0.74x |      614.0131 |            2.4% |
| NVIDIA Corporation / NVDA           |   5.2636 |           2.3% |                 0.46x |       10.5271 |            4.7% |
| Soybeans / ZS=F                     |  21.5179 |           1.7% |                 0.59x |       43.0357 |            3.3% |
| Euro Stoxx 50 / ^STOXX50E           |  74.9071 |           1.2% |                 0.77x |      149.8142 |            2.4% |
| Tesla Inc. / TSLA                   |  10.8557 |           2.9% |                 0.34x |       21.7114 |            5.7% |
| UnitedHealth Group Inc. / UNH       |   8.8886 |           2.3% |                 0.55x |       17.7771 |            4.7% |
| JPMorgan Chase & Co. / JPM          |   4.9099 |           1.5% |                 0.60x |        9.8197 |            2.9% |
| Hang Seng / ^HSI                    | 322.1878 |           1.3% |                 0.64x |      644.3756 |            2.7% |
| Gold / GC=F                         |  80.1857 |           1.9% |                 0.59x |      160.3713 |            3.8% |
| CAC 40 / ^FCHI                      |  91.4942 |           1.2% |                 0.83x |      182.9884 |            2.3% |
| Russell 2000 / ^RUT                 |  33.2386 |           1.2% |                 0.94x |       66.4771 |            2.4% |
| Platinum / PL=F                     |  36.3500 |           2.2% |                 0.35x |       72.7000 |            4.3% |
| Corn / ZC=F                         |  12.2679 |           2.5% |                 0.33x |       24.5357 |            5.1% |
| Silver / SI=F                       |   1.2924 |           2.1% |                 0.36x |        2.5849 |            4.3% |
| Wheat / ZW=F                        |  17.2857 |           2.6% |                 0.42x |       34.5714 |            5.1% |

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

Scoring engine version: **1.0.0** | Git commit: **b9858d1**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
