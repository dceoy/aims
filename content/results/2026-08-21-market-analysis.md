+++
title = "Market Analysis 2026-08-21"
date = "2026-08-21T00:00:00+00:00"
draft = false
summary = "Neutral market: 26 reliable instruments. Top signal: ZC=F (score 79.4)."
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
source_files = ["data/analysis/2026-08-21.json", "data/history/2026-08-21.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "226cdab"
+++

## Market Regime

**Neutral** — 15 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Corn / ZC=F** — score 79.4, 20d return +10.7%, RSI14=66. 20d up +10.7%; above MA20 by 10.0%; RSI14=66
- **Wheat / ZW=F** — score 74.8, 20d return +6.2%, RSI14=68. 20d up +6.2%; above MA20 by 6.7%; RSI14=68
- **Gold / GC=F** — score 72.7, 20d return +12.3%, RSI14=81. 20d up +12.3%; above MA20 by 6.7%; RSI14=81
- **Platinum / PL=F** — score 68.2, 20d return +15.8%, RSI14=67. 20d up +15.8%; above MA20 by 8.7%; RSI14=67
- **Silver / SI=F** — score 67.9, 20d return +17.1%, RSI14=76. 20d up +17.1%; above MA20 by 9.1%; RSI14=76

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                 | Applies To |
| ---------- | --------------------- | ---------- |
| 2026-08-26 | NVDA earnings release | NVDA       |

## Signal History

Compared with the previous available report (**2026-08-20**).

- **New top-5:** PL=F
- **Persistent top signals:** ZC=F (7 reports), ZW=F (5 reports), GC=F (2 reports), SI=F (2 reports)
- **Dropped from top-5:** ZS=F

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +1 |   +18.8 |
| 7203.T    |     +3 |   +31.8 |
| 8306.T    |     -2 |    +1.5 |
| AAPL      |     -4 |   -13.3 |
| AMZN      |     -8 |   -20.0 |
| BZ=F      |     +5 |   +10.0 |
| CL=F      |     +1 |   +17.9 |
| GC=F      |     -1 |    -2.4 |
| GOOGL     |     +0 |    -5.5 |
| HG=F      |     -3 |    +6.4 |
| JPM       |     -4 |    -9.7 |
| META      |     +0 |    -1.2 |
| MSFT      |     +0 |    -6.1 |
| NG=F      |     +1 |    -5.8 |
| NVDA      |     +4 |    -0.3 |
| PL=F      |     +2 |    +3.0 |
| SI=F      |     +0 |    +1.2 |
| TSLA      |     -1 |    -5.2 |
| UNH       |     +0 |    +2.1 |
| XOM       |     +0 |    +6.1 |
| ZC=F      |     +0 |    +3.3 |
| ZS=F      |     -2 |    -3.6 |
| ZW=F      |     +1 |    +0.6 |
| ^DJI      |     -5 |   -14.8 |
| ^FCHI     |     +2 |    -0.9 |
| ^FTSE     |     +8 |    +3.9 |
| ^GDAXI    |     +3 |    -2.1 |
| ^GSPC     |     -4 |   -14.2 |
| ^HSI      |    +10 |    +7.6 |
| ^N225     |     +0 |   +14.6 |
| ^NDX      |     -3 |    -6.7 |
| ^RUT      |     -8 |   -18.5 |
| ^STOXX50E |     +4 |    +1.5 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Exxon Mobil Corporation / XOM** — malformed_input
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **WTI Crude Oil / CL=F** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|    1 | Corn / ZC=F            |  79.4 |   Yes    | —               | 20d up +10.7%; above MA20 by 10.0%; RSI14=66 |
|    2 | Wheat / ZW=F           |  74.8 |   Yes    | —               | 20d up +6.2%; above MA20 by 6.7%; RSI14=68   |
|    3 | Gold / GC=F            |  72.7 |   Yes    | —               | 20d up +12.3%; above MA20 by 6.7%; RSI14=81  |
|    4 | Platinum / PL=F        |  68.2 |   Yes    | —               | 20d up +15.8%; above MA20 by 8.7%; RSI14=67  |
|    5 | Silver / SI=F          |  67.9 |   Yes    | —               | 20d up +17.1%; above MA20 by 9.1%; RSI14=76  |
|    6 | Soybeans / ZS=F        |  67.3 |   Yes    | —               | 20d up +1.7%; above MA20 by 4.3%; RSI14=74   |
|    7 | Brent Crude Oil / BZ=F |  63.0 |   Yes    | —               | 20d up +6.1%; above MA20 by 7.5%; RSI14=90   |
|   22 | Natural Gas / NG=F     |  31.2 |   Yes    | —               | 20d up +0.0%; above MA20 by 1.3%; RSI14=57   |
|   29 | WTI Crude Oil / CL=F   |  57.6 |    No    | malformed_input | Suppressed: malformed_input                  |
|   31 | Copper / HG=F          |  47.3 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    9 | Microsoft Corporation / MSFT                                                   |  53.9 |   Yes    | —                             | 20d up +26.3%; above MA20 by 3.0%; RSI14=59  |
|   14 | NVIDIA Corporation / NVDA                                                      |  45.1 |   Yes    | —                             | 20d up +3.9%; above MA20 by 1.9%; RSI14=67   |
|   17 | Tesla Inc. / TSLA                                                              |  41.8 |   Yes    | —                             | 20d up +8.0%; above MA20 by 6.0%; RSI14=70   |
|   19 | JPMorgan Chase & Co. / JPM                                                     |  40.6 |   Yes    | —                             | 20d up +0.5%; below MA20 by 1.6%; RSI14=50   |
|   21 | Amazon.com Inc. / AMZN                                                         |  32.4 |   Yes    | —                             | 20d up +11.3%; above MA20 by 0.0%; RSI14=41  |
|   23 | Apple Inc. / AAPL                                                              |  30.6 |   Yes    | —                             | 20d down -3.1%; below MA20 by 1.3%; RSI14=53 |
|   24 | Alphabet Inc. Class A / GOOGL                                                  |  24.9 |   Yes    | —                             | 20d up +7.2%; below MA20 by 1.9%; RSI14=39   |
|   25 | UnitedHealth Group Inc. / UNH                                                  |  21.8 |   Yes    | —                             | 20d down -9.1%; below MA20 by 5.6%; RSI14=27 |
|   26 | Meta Platforms Inc. / META                                                     |  12.7 |   Yes    | —                             | 20d down -9.9%; below MA20 by 5.7%; RSI14=46 |
|   27 | Exxon Mobil Corporation / XOM                                                  |  75.2 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   28 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  59.4 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   30 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  55.1 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   33 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  31.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                |
| ---: | ----------------------------------- | ----: | :------: | ------------ | ------------------------------------------ |
|    8 | DAX / ^GDAXI                        |  56.4 |   Yes    | —            | 20d up +4.9%; below MA20 by 0.0%; RSI14=61 |
|   10 | Euro Stoxx 50 / ^STOXX50E           |  53.3 |   Yes    | —            | 20d up +3.4%; below MA20 by 0.3%; RSI14=59 |
|   11 | S&P 500 / ^GSPC                     |  50.0 |   Yes    | —            | 20d up +3.1%; above MA20 by 0.1%; RSI14=62 |
|   12 | Hang Seng / ^HSI                    |  49.7 |   Yes    | —            | 20d up +1.9%; above MA20 by 0.4%; RSI14=46 |
|   13 | FTSE 100 / ^FTSE                    |  46.4 |   Yes    | —            | 20d up +1.0%; below MA20 by 0.7%; RSI14=30 |
|   15 | Dow Jones Industrial Average / ^DJI |  44.2 |   Yes    | —            | 20d up +2.0%; below MA20 by 0.9%; RSI14=53 |
|   16 | Russell 2000 / ^RUT                 |  42.7 |   Yes    | —            | 20d up +1.8%; below MA20 by 0.3%; RSI14=59 |
|   18 | CAC 40 / ^FCHI                      |  41.8 |   Yes    | —            | 20d up +1.9%; below MA20 by 1.4%; RSI14=44 |
|   20 | NASDAQ 100 / ^NDX                   |  39.4 |   Yes    | —            | 20d up +2.7%; above MA20 by 0.4%; RSI14=62 |
|   32 | Nikkei 225 / ^N225                  |  41.8 |    No    | missing_bars | Suppressed: missing_bars                   |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-08-20 |
| 7203.T    | 2026-08-20 |
| 8306.T    | 2026-08-20 |
| AAPL      | 2026-08-20 |
| AMZN      | 2026-08-20 |
| BZ=F      | 2026-08-20 |
| CL=F      | 2026-08-20 |
| GC=F      | 2026-08-20 |
| GOOGL     | 2026-08-20 |
| HG=F      | 2026-08-20 |
| JPM       | 2026-08-20 |
| META      | 2026-08-20 |
| MSFT      | 2026-08-20 |
| NG=F      | 2026-08-20 |
| NVDA      | 2026-08-20 |
| PL=F      | 2026-08-20 |
| SI=F      | 2026-08-20 |
| TSLA      | 2026-08-20 |
| UNH       | 2026-08-20 |
| XOM       | 2026-08-20 |
| ZC=F      | 2026-08-20 |
| ZS=F      | 2026-08-20 |
| ZW=F      | 2026-08-20 |
| ^DJI      | 2026-08-20 |
| ^FCHI     | 2026-08-20 |
| ^FTSE     | 2026-08-20 |
| ^GDAXI    | 2026-08-20 |
| ^GSPC     | 2026-08-20 |
| ^HSI      | 2026-08-20 |
| ^N225     | 2026-08-20 |
| ^NDX      | 2026-08-20 |
| ^RUT      | 2026-08-20 |
| ^STOXX50E | 2026-08-20 |

## Symbol Details

### Corn / ZC=F (score 79.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +5.7% |
| ret_5d     |  +8.9% |
| ret_20d    | +10.7% |
| ret_60d    |  +9.7% |
| ma20_dist  | +10.0% |
| ma50_dist  | +13.5% |
| vol_20d    |  49.2% |
| mdd_60d    |  10.0% |
| rsi_14     |   65.6 |
| zscore_20d |    2.7 |

### Wheat / ZW=F (score 74.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +3.1% |
| ret_5d     |  +3.9% |
| ret_20d    |  +6.2% |
| ret_60d    | +12.4% |
| ma20_dist  |  +6.7% |
| ma50_dist  | +10.1% |
| vol_20d    |  32.7% |
| mdd_60d    |  10.7% |
| rsi_14     |   67.5 |
| zscore_20d |    2.3 |

### Gold / GC=F (score 72.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.9% |
| ret_5d     |  +4.5% |
| ret_20d    | +12.3% |
| ret_60d    |  +1.7% |
| ma20_dist  |  +6.7% |
| ma50_dist  |  +9.5% |
| vol_20d    |  22.0% |
| mdd_60d    |  12.6% |
| rsi_14     |   80.7 |
| zscore_20d |    1.7 |

### Platinum / PL=F (score 68.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +4.1% |
| ret_5d     |  +7.2% |
| ret_20d    | +15.8% |
| ret_60d    |  -2.3% |
| ma20_dist  |  +8.7% |
| ma50_dist  | +12.1% |
| vol_20d    |  40.6% |
| mdd_60d    |  20.0% |
| rsi_14     |   67.2 |
| zscore_20d |    2.2 |

### Silver / SI=F (score 67.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +4.2% |
| ret_5d     |  +5.4% |
| ret_20d    | +17.1% |
| ret_60d    |  -9.5% |
| ma20_dist  |  +9.1% |
| ma50_dist  | +11.2% |
| vol_20d    |  32.8% |
| mdd_60d    |  26.1% |
| rsi_14     |   76.1 |
| zscore_20d |    1.7 |

### Soybeans / ZS=F (score 67.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | +4.7% |
| ret_20d    | +1.7% |
| ret_60d    | +2.9% |
| ma20_dist  | +4.3% |
| ma50_dist  | +4.8% |
| vol_20d    | 19.0% |
| mdd_60d    |  8.1% |
| rsi_14     |  74.4 |
| zscore_20d |   2.2 |

### Brent Crude Oil / BZ=F (score 63.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.4% |
| ret_5d     |  +6.0% |
| ret_20d    |  +6.1% |
| ret_60d    |  +0.1% |
| ma20_dist  |  +7.5% |
| ma50_dist  | +12.2% |
| vol_20d    |  52.5% |
| mdd_60d    |  26.8% |
| rsi_14     |   89.5 |
| zscore_20d |    1.7 |

### DAX / ^GDAXI (score 56.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -1.2% |
| ret_20d    | +4.9% |
| ret_60d    | +3.6% |
| ma20_dist  | -0.0% |
| ma50_dist  | +2.2% |
| vol_20d    |  9.3% |
| mdd_60d    |  4.1% |
| rsi_14     |  61.0 |
| zscore_20d |  -0.0 |

### Microsoft Corporation / MSFT (score 53.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.5% |
| ret_5d     |  -3.0% |
| ret_20d    | +26.3% |
| ret_60d    | +15.7% |
| ma20_dist  |  +3.0% |
| ma50_dist  | +15.2% |
| vol_20d    |  58.9% |
| mdd_60d    |  23.4% |
| rsi_14     |   59.3 |
| zscore_20d |    0.3 |

### Euro Stoxx 50 / ^STOXX50E (score 53.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | -1.9% |
| ret_20d    | +3.4% |
| ret_60d    | +6.1% |
| ma20_dist  | -0.3% |
| ma50_dist  | +1.3% |
| vol_20d    |  9.6% |
| mdd_60d    |  3.2% |
| rsi_14     |  58.8 |
| zscore_20d |  -0.2 |

### S&P 500 / ^GSPC (score 50.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.9% |
| ret_5d     | -2.0% |
| ret_20d    | +3.1% |
| ret_60d    | +1.6% |
| ma20_dist  | +0.1% |
| ma50_dist  | +1.4% |
| vol_20d    | 12.8% |
| mdd_60d    |  4.5% |
| rsi_14     |  62.4 |
| zscore_20d |   0.1 |

### Hang Seng / ^HSI (score 49.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.8% |
| ret_5d     | +1.2% |
| ret_20d    | +1.9% |
| ret_60d    | +0.4% |
| ma20_dist  | +0.4% |
| ma50_dist  | +4.1% |
| vol_20d    | 14.0% |
| mdd_60d    | 12.9% |
| rsi_14     |  46.3 |
| zscore_20d |   0.4 |

### FTSE 100 / ^FTSE (score 46.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.0% |
| ret_5d     | -0.2% |
| ret_20d    | +1.0% |
| ret_60d    | +3.1% |
| ma20_dist  | -0.7% |
| ma50_dist  | +1.0% |
| vol_20d    |  5.8% |
| mdd_60d    |  1.9% |
| rsi_14     |  30.2 |
| zscore_20d |  -1.1 |

### NVIDIA Corporation / NVDA (score 45.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | -3.8% |
| ret_20d    | +3.9% |
| ret_60d    | +0.9% |
| ma20_dist  | +1.9% |
| ma50_dist  | +4.6% |
| vol_20d    | 37.1% |
| mdd_60d    | 15.3% |
| rsi_14     |  67.4 |
| zscore_20d |   0.4 |

### Dow Jones Industrial Average / ^DJI (score 44.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.3% |
| ret_5d     | -2.0% |
| ret_20d    | +2.0% |
| ret_60d    | +4.6% |
| ma20_dist  | -0.9% |
| ma50_dist  | +0.5% |
| vol_20d    | 14.1% |
| mdd_60d    |  3.2% |
| rsi_14     |  53.3 |
| zscore_20d |  -0.6 |

### Russell 2000 / ^RUT (score 42.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.3% |
| ret_5d     | -2.0% |
| ret_20d    | +1.8% |
| ret_60d    | +2.5% |
| ma20_dist  | -0.3% |
| ma50_dist  | +0.3% |
| vol_20d    | 15.2% |
| mdd_60d    |  3.9% |
| rsi_14     |  58.8 |
| zscore_20d |  -0.2 |

### Tesla Inc. / TSLA (score 41.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.7% |
| ret_5d     |  +1.5% |
| ret_20d    |  +8.0% |
| ret_60d    | -20.4% |
| ma20_dist  |  +6.0% |
| ma50_dist  |  -5.8% |
| vol_20d    |  34.0% |
| mdd_60d    |  32.5% |
| rsi_14     |   70.4 |
| zscore_20d |    1.4 |

### CAC 40 / ^FCHI (score 41.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | -2.3% |
| ret_20d    | +1.9% |
| ret_60d    | +3.2% |
| ma20_dist  | -1.4% |
| ma50_dist  | -0.1% |
| vol_20d    |  8.9% |
| mdd_60d    |  3.1% |
| rsi_14     |  44.2 |
| zscore_20d |  -1.0 |

### JPMorgan Chase & Co. / JPM (score 40.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.6% |
| ret_5d     |  -3.2% |
| ret_20d    |  +0.5% |
| ret_60d    | +15.1% |
| ma20_dist  |  -1.6% |
| ma50_dist  |  +2.6% |
| vol_20d    |  18.8% |
| mdd_60d    |   3.7% |
| rsi_14     |   49.7 |
| zscore_20d |   -1.1 |

### NASDAQ 100 / ^NDX (score 39.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | -2.9% |
| ret_20d    | +2.7% |
| ret_60d    | -2.6% |
| ma20_dist  | +0.4% |
| ma50_dist  | -0.3% |
| vol_20d    | 22.4% |
| mdd_60d    | 11.3% |
| rsi_14     |  62.4 |
| zscore_20d |   0.2 |

### Amazon.com Inc. / AMZN (score 32.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.2% |
| ret_5d     |  -1.9% |
| ret_20d    | +11.3% |
| ret_60d    |  -2.0% |
| ma20_dist  |  +0.0% |
| ma50_dist  |  +4.3% |
| vol_20d    |  61.4% |
| mdd_60d    |  17.3% |
| rsi_14     |   40.6 |
| zscore_20d |    0.0 |

### Natural Gas / NG=F (score 31.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.7% |
| ret_5d     |  +1.2% |
| ret_20d    |  +0.0% |
| ret_60d    | -15.8% |
| ma20_dist  |  +1.3% |
| ma50_dist  |  -5.8% |
| vol_20d    |  32.5% |
| mdd_60d    |  21.0% |
| rsi_14     |   56.9 |
| zscore_20d |    0.7 |

### Apple Inc. / AAPL (score 30.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.7% |
| ret_5d     | +2.0% |
| ret_20d    | -3.1% |
| ret_60d    | +1.0% |
| ma20_dist  | -1.3% |
| ma50_dist  | +0.5% |
| vol_20d    | 34.3% |
| mdd_60d    | 12.7% |
| rsi_14     |  52.8 |
| zscore_20d |  -0.3 |

### Alphabet Inc. Class A / GOOGL (score 24.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.2% |
| ret_5d     |  -1.6% |
| ret_20d    |  +7.2% |
| ret_60d    | -12.3% |
| ma20_dist  |  -1.9% |
| ma50_dist  |  -3.2% |
| vol_20d    |  38.2% |
| mdd_60d    |  18.5% |
| rsi_14     |   39.3 |
| zscore_20d |   -0.5 |

### UnitedHealth Group Inc. / UNH (score 21.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | -3.6% |
| ret_20d    | -9.1% |
| ret_60d    | +2.7% |
| ma20_dist  | -5.6% |
| ma50_dist  | -7.0% |
| vol_20d    | 20.2% |
| mdd_60d    | 11.8% |
| rsi_14     |  26.8 |
| zscore_20d |  -2.0 |

### Meta Platforms Inc. / META (score 12.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.0% |
| ret_5d     |  -8.3% |
| ret_20d    |  -9.9% |
| ret_60d    | -10.8% |
| ma20_dist  |  -5.7% |
| ma50_dist  |  -8.0% |
| vol_20d    |  45.5% |
| mdd_60d    |  20.9% |
| rsi_14     |   46.0 |
| zscore_20d |   -1.6 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Corn / ZC=F                         |  16.0536 |           3.2% |                 0.20x |       32.1071 |            6.4% |
| Wheat / ZW=F                        |  20.9821 |           3.0% |                 0.31x |       41.9643 |            6.0% |
| Gold / GC=F                         |  95.0715 |           2.1% |                 0.45x |      190.1430 |            4.2% |
| Platinum / PL=F                     |  28.7071 |           1.5% |                 0.25x |       57.4143 |            3.1% |
| Silver / SI=F                       |   1.7201 |           2.5% |                 0.30x |        3.4403 |            5.0% |
| Soybeans / ZS=F                     |  15.8750 |           1.3% |                 0.53x |       31.7500 |            2.6% |
| Brent Crude Oil / BZ=F              |   2.6893 |           2.9% |                 0.19x |        5.3786 |            5.7% |
| DAX / ^GDAXI                        | 231.8993 |           0.9% |                 1.07x |      463.7985 |            1.8% |
| Microsoft Corporation / MSFT        |  11.8754 |           2.5% |                 0.17x |       23.7508 |            4.9% |
| Euro Stoxx 50 / ^STOXX50E           |  50.3971 |           0.8% |                 1.05x |      100.7943 |            1.6% |
| S&P 500 / ^GSPC                     |  63.8108 |           0.8% |                 0.78x |      127.6215 |            1.7% |
| Hang Seng / ^HSI                    | 333.4029 |           1.3% |                 0.71x |      666.8058 |            2.6% |
| FTSE 100 / ^FTSE                    |  79.5643 |           0.7% |                 1.73x |      159.1286 |            1.5% |
| NVIDIA Corporation / NVDA           |   6.2971 |           2.9% |                 0.27x |       12.5943 |            5.8% |
| Dow Jones Industrial Average / ^DJI | 476.2143 |           0.9% |                 0.71x |      952.4286 |            1.8% |
| Russell 2000 / ^RUT                 |  32.1990 |           1.1% |                 0.66x |       64.3980 |            2.2% |
| Tesla Inc. / TSLA                   |  10.9979 |           3.2% |                 0.29x |       21.9957 |            6.4% |
| CAC 40 / ^FCHI                      |  62.3142 |           0.7% |                 1.13x |      124.6285 |            1.5% |
| JPMorgan Chase & Co. / JPM          |   5.6064 |           1.6% |                 0.53x |       11.2129 |            3.2% |
| NASDAQ 100 / ^NDX                   | 424.7889 |           1.5% |                 0.45x |      849.5778 |            2.9% |
| Amazon.com Inc. / AMZN              |   7.2136 |           2.8% |                 0.16x |       14.4271 |            5.5% |
| Natural Gas / NG=F                  |   0.0815 |           2.9% |                 0.31x |        0.1630 |            5.9% |
| Apple Inc. / AAPL                   |   6.6621 |           2.1% |                 0.29x |       13.3242 |            4.3% |
| Alphabet Inc. Class A / GOOGL       |   9.3468 |           2.7% |                 0.26x |       18.6936 |            5.5% |
| UnitedHealth Group Inc. / UNH       |   9.3578 |           2.4% |                 0.50x |       18.7157 |            4.9% |
| Meta Platforms Inc. / META          |  19.1756 |           3.5% |                 0.22x |       38.3511 |            7.0% |

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

Scoring engine version: **1.0.0** | Git commit: **226cdab**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
