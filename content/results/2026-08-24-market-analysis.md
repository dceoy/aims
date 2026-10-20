+++
title = "Market Analysis 2026-08-24"
date = "2026-08-24T00:00:00+00:00"
draft = false
summary = "Bullish market: 26 reliable instruments. Top signal: ZC=F (score 81.8)."
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
source_files = ["data/analysis/2026-08-24.json", "data/history/2026-08-24.json"]
market_regime = "Bullish"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "f9f1bbf"
+++

## Market Regime

**Bullish** — 17 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Corn / ZC=F** — score 81.8, 20d return +16.0%, RSI14=71. 20d up +16.0%; above MA20 by 13.6%; RSI14=71
- **Gold / GC=F** — score 81.2, 20d return +16.7%, RSI14=81. 20d up +16.7%; above MA20 by 8.3%; RSI14=81
- **Wheat / ZW=F** — score 77.9, 20d return +7.9%, RSI14=73. 20d up +7.9%; above MA20 by 8.0%; RSI14=73
- **Soybeans / ZS=F** — score 71.2, 20d return +4.8%, RSI14=76. 20d up +4.8%; above MA20 by 4.5%; RSI14=76
- **Platinum / PL=F** — score 63.6, 20d return +19.1%, RSI14=72. 20d up +19.1%; above MA20 by 8.0%; RSI14=72

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                 | Applies To |
| ---------- | --------------------- | ---------- |
| 2026-08-26 | NVDA earnings release | NVDA       |

## Signal History

Compared with the previous available report (**2026-08-21**).

- **New top-5:** ZS=F
- **Persistent top signals:** ZC=F (8 reports), ZW=F (6 reports), GC=F (3 reports), PL=F (2 reports)
- **Dropped from top-5:** SI=F

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     -1 |   -10.9 |
| 7203.T    |     +2 |    +7.6 |
| 8306.T    |     +1 |    +4.8 |
| AAPL      |     +0 |    -0.9 |
| AMZN      |     -3 |    -4.5 |
| BZ=F      |     -9 |   -17.3 |
| CL=F      |     -2 |   -16.4 |
| GC=F      |     +1 |    +8.5 |
| GOOGL     |     +2 |    +6.7 |
| HG=F      |     +1 |    -4.5 |
| JPM       |     +1 |    +0.3 |
| META      |     +0 |    -2.1 |
| MSFT      |     -5 |    -3.0 |
| NG=F      |     +2 |    +7.6 |
| NVDA      |     -7 |    -9.1 |
| PL=F      |     -1 |    -4.5 |
| SI=F      |     -1 |    -6.1 |
| TSLA      |     +9 |   +16.4 |
| UNH       |     +0 |    +6.1 |
| XOM       |     +0 |    -9.7 |
| ZC=F      |     +0 |    +2.4 |
| ZS=F      |     +2 |    +3.9 |
| ZW=F      |     -1 |    +3.0 |
| ^DJI      |     +4 |    +7.9 |
| ^FCHI     |     -1 |    -1.2 |
| ^FTSE     |     -2 |    +2.4 |
| ^GDAXI    |     -1 |    -1.2 |
| ^GSPC     |     -2 |    +1.2 |
| ^HSI      |     +5 |   +10.0 |
| ^N225     |     -1 |   -10.0 |
| ^NDX      |     +3 |    +2.4 |
| ^RUT      |     +4 |    +9.4 |
| ^STOXX50E |     +0 |    +0.9 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Exxon Mobil Corporation / XOM** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Nikkei 225 / ^N225** — missing_bars

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|    1 | Corn / ZC=F            |  81.8 |   Yes    | —               | 20d up +16.0%; above MA20 by 13.6%; RSI14=71 |
|    2 | Gold / GC=F            |  81.2 |   Yes    | —               | 20d up +16.7%; above MA20 by 8.3%; RSI14=81  |
|    3 | Wheat / ZW=F           |  77.9 |   Yes    | —               | 20d up +7.9%; above MA20 by 8.0%; RSI14=73   |
|    4 | Soybeans / ZS=F        |  71.2 |   Yes    | —               | 20d up +4.8%; above MA20 by 4.5%; RSI14=76   |
|    5 | Platinum / PL=F        |  63.6 |   Yes    | —               | 20d up +19.1%; above MA20 by 8.0%; RSI14=72  |
|    6 | Silver / SI=F          |  61.8 |   Yes    | —               | 20d up +19.7%; above MA20 by 8.3%; RSI14=77  |
|   16 | Brent Crude Oil / BZ=F |  45.8 |   Yes    | —               | 20d up +2.1%; above MA20 by 5.5%; RSI14=79   |
|   20 | Natural Gas / NG=F     |  38.8 |   Yes    | —               | 20d up +1.7%; above MA20 by 1.2%; RSI14=60   |
|   30 | Copper / HG=F          |  42.7 |    No    | malformed_input | Suppressed: malformed_input                  |
|   31 | WTI Crude Oil / CL=F   |  41.2 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    8 | Tesla Inc. / TSLA                                                              |  58.2 |   Yes    | —                             | 20d up +15.9%; above MA20 by 10.6%; RSI14=73 |
|   14 | Microsoft Corporation / MSFT                                                   |  50.9 |   Yes    | —                             | 20d up +26.8%; above MA20 by 2.3%; RSI14=48  |
|   18 | JPMorgan Chase & Co. / JPM                                                     |  40.9 |   Yes    | —                             | 20d down -0.5%; below MA20 by 1.5%; RSI14=49 |
|   21 | NVIDIA Corporation / NVDA                                                      |  36.1 |   Yes    | —                             | 20d up +3.8%; above MA20 by 0.7%; RSI14=59   |
|   22 | Alphabet Inc. Class A / GOOGL                                                  |  31.5 |   Yes    | —                             | 20d up +7.8%; below MA20 by 1.0%; RSI14=26   |
|   23 | Apple Inc. / AAPL                                                              |  29.7 |   Yes    | —                             | 20d down -7.0%; below MA20 by 1.5%; RSI14=57 |
|   24 | Amazon.com Inc. / AMZN                                                         |  27.9 |   Yes    | —                             | 20d up +11.4%; below MA20 by 1.1%; RSI14=25  |
|   25 | UnitedHealth Group Inc. / UNH                                                  |  27.9 |   Yes    | —                             | 20d down -7.3%; below MA20 by 3.9%; RSI14=31 |
|   26 | Meta Platforms Inc. / META                                                     |  10.6 |   Yes    | —                             | 20d down -7.6%; below MA20 by 4.6%; RSI14=31 |
|   27 | Exxon Mobil Corporation / XOM                                                  |  65.5 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   28 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  62.7 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   29 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  48.5 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   32 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  36.1 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                |
| ---: | ----------------------------------- | ----: | :------: | ------------ | ------------------------------------------ |
|    7 | Hang Seng / ^HSI                    |  59.7 |   Yes    | —            | 20d up +4.2%; above MA20 by 1.5%; RSI14=50 |
|    9 | DAX / ^GDAXI                        |  55.1 |   Yes    | —            | 20d up +4.1%; above MA20 by 0.4%; RSI14=55 |
|   10 | Euro Stoxx 50 / ^STOXX50E           |  54.2 |   Yes    | —            | 20d up +2.9%; above MA20 by 0.2%; RSI14=55 |
|   11 | Dow Jones Industrial Average / ^DJI |  52.1 |   Yes    | —            | 20d up +2.6%; below MA20 by 0.1%; RSI14=51 |
|   12 | Russell 2000 / ^RUT                 |  52.1 |   Yes    | —            | 20d up +3.0%; above MA20 by 0.4%; RSI14=56 |
|   13 | S&P 500 / ^GSPC                     |  51.2 |   Yes    | —            | 20d up +3.5%; above MA20 by 0.4%; RSI14=57 |
|   15 | FTSE 100 / ^FTSE                    |  48.8 |   Yes    | —            | 20d up +0.7%; below MA20 by 0.1%; RSI14=44 |
|   17 | NASDAQ 100 / ^NDX                   |  41.8 |   Yes    | —            | 20d up +4.2%; above MA20 by 0.6%; RSI14=58 |
|   19 | CAC 40 / ^FCHI                      |  40.6 |   Yes    | —            | 20d up +1.3%; below MA20 by 1.1%; RSI14=34 |
|   33 | Nikkei 225 / ^N225                  |  31.8 |    No    | missing_bars | Suppressed: missing_bars                   |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-08-21 |
| 7203.T    | 2026-08-21 |
| 8306.T    | 2026-08-21 |
| AAPL      | 2026-08-21 |
| AMZN      | 2026-08-21 |
| BZ=F      | 2026-08-23 |
| CL=F      | 2026-08-23 |
| GC=F      | 2026-08-23 |
| GOOGL     | 2026-08-21 |
| HG=F      | 2026-08-23 |
| JPM       | 2026-08-21 |
| META      | 2026-08-21 |
| MSFT      | 2026-08-21 |
| NG=F      | 2026-08-23 |
| NVDA      | 2026-08-21 |
| PL=F      | 2026-08-23 |
| SI=F      | 2026-08-23 |
| TSLA      | 2026-08-21 |
| UNH       | 2026-08-21 |
| XOM       | 2026-08-21 |
| ZC=F      | 2026-08-23 |
| ZS=F      | 2026-08-23 |
| ZW=F      | 2026-08-23 |
| ^DJI      | 2026-08-21 |
| ^FCHI     | 2026-08-21 |
| ^FTSE     | 2026-08-21 |
| ^GDAXI    | 2026-08-21 |
| ^GSPC     | 2026-08-21 |
| ^HSI      | 2026-08-21 |
| ^N225     | 2026-08-21 |
| ^NDX      | 2026-08-21 |
| ^RUT      | 2026-08-21 |
| ^STOXX50E | 2026-08-21 |

## Symbol Details

### Corn / ZC=F (score 81.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +7.6% |
| ret_5d     | +12.0% |
| ret_20d    | +16.0% |
| ret_60d    | +17.3% |
| ma20_dist  | +13.6% |
| ma50_dist  | +17.4% |
| vol_20d    |  51.2% |
| mdd_60d    |   8.7% |
| rsi_14     |   70.6 |
| zscore_20d |    2.9 |

### Gold / GC=F (score 81.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.8% |
| ret_5d     |  +6.5% |
| ret_20d    | +16.7% |
| ret_60d    |  +5.2% |
| ma20_dist  |  +8.3% |
| ma50_dist  | +12.2% |
| vol_20d    |  21.8% |
| mdd_60d    |  11.2% |
| rsi_14     |   80.6 |
| zscore_20d |    2.1 |

### Wheat / ZW=F (score 77.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +4.6% |
| ret_5d     |  +5.6% |
| ret_20d    |  +7.9% |
| ret_60d    | +17.1% |
| ma20_dist  |  +8.0% |
| ma50_dist  | +11.2% |
| vol_20d    |  34.7% |
| mdd_60d    |  10.7% |
| rsi_14     |   72.8 |
| zscore_20d |    2.4 |

### Soybeans / ZS=F (score 71.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.8% |
| ret_5d     | +2.8% |
| ret_20d    | +4.8% |
| ret_60d    | +4.6% |
| ma20_dist  | +4.5% |
| ma50_dist  | +4.9% |
| vol_20d    | 16.0% |
| mdd_60d    |  8.1% |
| rsi_14     |  75.6 |
| zscore_20d |   2.0 |

### Platinum / PL=F (score 63.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.4% |
| ret_5d     |  +6.3% |
| ret_20d    | +19.1% |
| ret_60d    |  -1.5% |
| ma20_dist  |  +8.0% |
| ma50_dist  | +12.8% |
| vol_20d    |  38.7% |
| mdd_60d    |  20.0% |
| rsi_14     |   72.0 |
| zscore_20d |    2.1 |

### Silver / SI=F (score 61.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.3% |
| ret_5d     |  +4.7% |
| ret_20d    | +19.7% |
| ret_60d    |  -7.7% |
| ma20_dist  |  +8.3% |
| ma50_dist  | +12.4% |
| vol_20d    |  30.9% |
| mdd_60d    |  25.8% |
| rsi_14     |   76.6 |
| zscore_20d |    1.6 |

### Hang Seng / ^HSI (score 59.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.2% |
| ret_5d     | +3.6% |
| ret_20d    | +4.2% |
| ret_60d    | +2.7% |
| ma20_dist  | +1.5% |
| ma50_dist  | +5.3% |
| vol_20d    | 14.0% |
| mdd_60d    | 12.9% |
| rsi_14     |  50.0 |
| zscore_20d |   1.4 |

### Tesla Inc. / TSLA (score 58.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +5.1% |
| ret_5d     |  +6.0% |
| ret_20d    | +15.9% |
| ret_60d    | -17.6% |
| ma20_dist  | +10.6% |
| ma50_dist  |  -0.8% |
| vol_20d    |  36.4% |
| mdd_60d    |  32.5% |
| rsi_14     |   72.7 |
| zscore_20d |    2.2 |

### DAX / ^GDAXI (score 55.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | -1.1% |
| ret_20d    | +4.1% |
| ret_60d    | +4.1% |
| ma20_dist  | +0.4% |
| ma50_dist  | +2.7% |
| vol_20d    |  8.5% |
| mdd_60d    |  4.1% |
| rsi_14     |  54.9 |
| zscore_20d |   0.3 |

### Euro Stoxx 50 / ^STOXX50E (score 54.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | -1.2% |
| ret_20d    | +2.9% |
| ret_60d    | +6.8% |
| ma20_dist  | +0.2% |
| ma50_dist  | +1.8% |
| vol_20d    |  9.0% |
| mdd_60d    |  3.2% |
| rsi_14     |  55.3 |
| zscore_20d |   0.1 |

### Dow Jones Industrial Average / ^DJI (score 52.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.0% |
| ret_5d     | -0.8% |
| ret_20d    | +2.6% |
| ret_60d    | +5.2% |
| ma20_dist  | -0.1% |
| ma50_dist  | +1.3% |
| vol_20d    | 14.4% |
| mdd_60d    |  3.2% |
| rsi_14     |  51.2 |
| zscore_20d |  -0.0 |

### Russell 2000 / ^RUT (score 52.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | -1.6% |
| ret_20d    | +3.0% |
| ret_60d    | +3.4% |
| ma20_dist  | +0.4% |
| ma50_dist  | +1.1% |
| vol_20d    | 15.3% |
| mdd_60d    |  3.9% |
| rsi_14     |  55.6 |
| zscore_20d |   0.3 |

### S&P 500 / ^GSPC (score 51.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | -1.4% |
| ret_20d    | +3.5% |
| ret_60d    | +2.0% |
| ma20_dist  | +0.4% |
| ma50_dist  | +1.8% |
| vol_20d    | 12.9% |
| mdd_60d    |  4.5% |
| rsi_14     |  56.9 |
| zscore_20d |   0.2 |

### Microsoft Corporation / MSFT (score 50.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.4% |
| ret_5d     |  -2.3% |
| ret_20d    | +26.8% |
| ret_60d    | +17.1% |
| ma20_dist  |  +2.3% |
| ma50_dist  | +15.2% |
| vol_20d    |  58.8% |
| mdd_60d    |  23.4% |
| rsi_14     |   47.6 |
| zscore_20d |    0.3 |

### FTSE 100 / ^FTSE (score 48.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | +0.6% |
| ret_20d    | +0.7% |
| ret_60d    | +3.9% |
| ma20_dist  | -0.1% |
| ma50_dist  | +1.5% |
| vol_20d    |  5.3% |
| mdd_60d    |  1.9% |
| rsi_14     |  44.3 |
| zscore_20d |  -0.2 |

### Brent Crude Oil / BZ=F (score 45.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.9% |
| ret_5d     |  +1.9% |
| ret_20d    |  +2.1% |
| ret_60d    |  -2.5% |
| ma20_dist  |  +5.5% |
| ma50_dist  | +10.3% |
| vol_20d    |  41.8% |
| mdd_60d    |  26.8% |
| rsi_14     |   79.0 |
| zscore_20d |    1.1 |

### NASDAQ 100 / ^NDX (score 41.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | -2.5% |
| ret_20d    | +4.2% |
| ret_60d    | -2.2% |
| ma20_dist  | +0.6% |
| ma50_dist  | -0.1% |
| vol_20d    | 21.9% |
| mdd_60d    | 11.3% |
| rsi_14     |  57.9 |
| zscore_20d |   0.2 |

### JPMorgan Chase & Co. / JPM (score 40.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.0% |
| ret_5d     |  -3.1% |
| ret_20d    |  -0.5% |
| ret_60d    | +18.0% |
| ma20_dist  |  -1.5% |
| ma50_dist  |  +2.4% |
| vol_20d    |  18.5% |
| mdd_60d    |   3.7% |
| rsi_14     |   48.6 |
| zscore_20d |   -1.1 |

### CAC 40 / ^FCHI (score 40.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | -1.8% |
| ret_20d    | +1.3% |
| ret_60d    | +3.7% |
| ma20_dist  | -1.1% |
| ma50_dist  | +0.2% |
| vol_20d    |  8.5% |
| mdd_60d    |  3.1% |
| rsi_14     |  34.5 |
| zscore_20d |  -0.9 |

### Natural Gas / NG=F (score 38.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.1% |
| ret_5d     |  +3.0% |
| ret_20d    |  +1.7% |
| ret_60d    | -12.9% |
| ma20_dist  |  +1.2% |
| ma50_dist  |  -5.3% |
| vol_20d    |  30.0% |
| mdd_60d    |  21.0% |
| rsi_14     |   60.1 |
| zscore_20d |    0.7 |

### NVIDIA Corporation / NVDA (score 36.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | -4.6% |
| ret_20d    | +3.8% |
| ret_60d    | +1.0% |
| ma20_dist  | +0.7% |
| ma50_dist  | +3.4% |
| vol_20d    | 37.2% |
| mdd_60d    | 15.3% |
| rsi_14     |  59.5 |
| zscore_20d |   0.1 |

### Alphabet Inc. Class A / GOOGL (score 31.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.2% |
| ret_5d     |  -0.3% |
| ret_20d    |  +7.8% |
| ret_60d    | -11.3% |
| ma20_dist  |  -1.0% |
| ma50_dist  |  -2.0% |
| vol_20d    |  38.3% |
| mdd_60d    |  18.5% |
| rsi_14     |   25.6 |
| zscore_20d |   -0.3 |

### Apple Inc. / AAPL (score 29.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | +1.1% |
| ret_20d    | -7.0% |
| ret_60d    | -0.5% |
| ma20_dist  | -1.5% |
| ma50_dist  | -0.2% |
| vol_20d    | 31.7% |
| mdd_60d    | 12.7% |
| rsi_14     |  57.1 |
| zscore_20d |  -0.4 |

### Amazon.com Inc. / AMZN (score 27.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.6% |
| ret_5d     |  -1.5% |
| ret_20d    | +11.4% |
| ret_60d    |  -4.9% |
| ma20_dist  |  -1.1% |
| ma50_dist  |  +3.6% |
| vol_20d    |  61.4% |
| mdd_60d    |  17.3% |
| rsi_14     |   24.5 |
| zscore_20d |   -0.2 |

### UnitedHealth Group Inc. / UNH (score 27.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.4% |
| ret_5d     | -2.9% |
| ret_20d    | -7.3% |
| ret_60d    | +2.2% |
| ma20_dist  | -3.9% |
| ma50_dist  | -5.7% |
| vol_20d    | 21.1% |
| mdd_60d    | 11.8% |
| rsi_14     |  31.4 |
| zscore_20d |  -1.4 |

### Meta Platforms Inc. / META (score 10.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.7% |
| ret_5d     |  -6.8% |
| ret_20d    |  -7.6% |
| ret_60d    | -13.4% |
| ma20_dist  |  -4.6% |
| ma50_dist  |  -7.3% |
| vol_20d    |  45.4% |
| mdd_60d    |  20.9% |
| rsi_14     |   31.3 |
| zscore_20d |   -1.3 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Corn / ZC=F                         |  17.0893 |           3.3% |                 0.20x |       34.1786 |            6.6% |
| Gold / GC=F                         |  87.3072 |           1.9% |                 0.46x |      174.6144 |            3.7% |
| Wheat / ZW=F                        |  20.6964 |           2.9% |                 0.29x |       41.3929 |            5.8% |
| Soybeans / ZS=F                     |  16.7321 |           1.4% |                 0.63x |       33.4643 |            2.7% |
| Platinum / PL=F                     |  30.0286 |           1.6% |                 0.26x |       60.0571 |            3.2% |
| Silver / SI=F                       |   1.7341 |           2.5% |                 0.32x |        3.4681 |            5.0% |
| Hang Seng / ^HSI                    | 332.6051 |           1.3% |                 0.72x |      665.2101 |            2.6% |
| Tesla Inc. / TSLA                   |  11.5086 |           3.2% |                 0.27x |       23.0172 |            6.3% |
| DAX / ^GDAXI                        | 212.5451 |           0.8% |                 1.17x |      425.0901 |            1.6% |
| Euro Stoxx 50 / ^STOXX50E           |  47.8828 |           0.7% |                 1.11x |       95.7657 |            1.5% |
| Dow Jones Industrial Average / ^DJI | 465.6189 |           0.9% |                 0.70x |      931.2377 |            1.7% |
| Russell 2000 / ^RUT                 |  30.3036 |           1.0% |                 0.65x |       60.6072 |            2.0% |
| S&P 500 / ^GSPC                     |  59.2129 |           0.8% |                 0.78x |      118.4258 |            1.5% |
| Microsoft Corporation / MSFT        |  10.5147 |           2.2% |                 0.17x |       21.0295 |            4.4% |
| FTSE 100 / ^FTSE                    |  80.4071 |           0.7% |                 1.88x |      160.8142 |            1.5% |
| Brent Crude Oil / BZ=F              |   2.5350 |           2.7% |                 0.24x |        5.0700 |            5.5% |
| NASDAQ 100 / ^NDX                   | 397.4459 |           1.4% |                 0.46x |      794.8917 |            2.7% |
| JPMorgan Chase & Co. / JPM          |   5.7286 |           1.6% |                 0.54x |       11.4571 |            3.3% |
| CAC 40 / ^FCHI                      |  56.5827 |           0.7% |                 1.18x |      113.1655 |            1.3% |
| Natural Gas / NG=F                  |   0.0820 |           3.0% |                 0.33x |        0.1640 |            5.9% |
| NVIDIA Corporation / NVDA           |   5.7507 |           2.7% |                 0.27x |       11.5014 |            5.4% |
| Alphabet Inc. Class A / GOOGL       |   8.2921 |           2.4% |                 0.26x |       16.5843 |            4.8% |
| Apple Inc. / AAPL                   |   6.3862 |           2.1% |                 0.32x |       12.7725 |            4.1% |
| Amazon.com Inc. / AMZN              |   6.3871 |           2.5% |                 0.16x |       12.7743 |            4.9% |
| UnitedHealth Group Inc. / UNH       |   9.5571 |           2.4% |                 0.47x |       19.1143 |            4.9% |
| Meta Platforms Inc. / META          |  17.0207 |           3.1% |                 0.22x |       34.0414 |            6.2% |

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

Scoring engine version: **1.0.0** | Git commit: **f9f1bbf**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
