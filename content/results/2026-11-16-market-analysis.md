+++
title = "Market Analysis 2026-11-16"
date = "2026-11-16T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: AAPL (score 79.1)."
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
source_files = ["data/analysis/2026-11-16.json", "data/history/2026-11-16.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "f5bda3a"
+++

## Market Regime

**Neutral** — 11 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Apple Inc. / AAPL** — score 79.1, 20d return +3.8%, RSI14=59. 20d up +3.8%; above MA20 by 3.0%; RSI14=59
- **DAX / ^GDAXI** — score 77.0, 20d return +4.4%, RSI14=70. 20d up +4.4%; above MA20 by 3.2%; RSI14=70
- **CAC 40 / ^FCHI** — score 74.8, 20d return +5.2%, RSI14=87. 20d up +5.2%; above MA20 by 4.0%; RSI14=87
- **Euro Stoxx 50 / ^STOXX50E** — score 72.7, 20d return +2.9%, RSI14=69. 20d up +2.9%; above MA20 by 2.8%; RSI14=69
- **FTSE 100 / ^FTSE** — score 70.9, 20d return +0.2%, RSI14=57. 20d up +0.2%; above MA20 by 1.4%; RSI14=57

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                 | Applies To |
| ---------- | --------------------- | ---------- |
| 2026-11-17 | NVDA earnings release | NVDA       |

## Signal History

Compared with the previous available report (**2026-11-13**).

- **New top-5:** ^FTSE
- **Persistent top signals:** ^GDAXI (14 reports), ^FCHI (7 reports), AAPL (6 reports), ^STOXX50E (4 reports)
- **Dropped from top-5:** TSLA

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +1 |    +4.8 |
| 7203.T    |     +1 |    +6.7 |
| 8306.T    |     +0 |    +2.7 |
| AAPL      |     +3 |    +5.2 |
| AMZN      |     +0 |    -4.2 |
| BZ=F      |     -1 |    -5.8 |
| CL=F      |     -1 |    -7.3 |
| GC=F      |     +2 |    +4.5 |
| GOOGL     |     -3 |    -7.9 |
| HG=F      |     -1 |    -5.8 |
| JPM       |     +3 |    +7.3 |
| META      |     +5 |   +18.2 |
| MSFT      |     +0 |    +0.0 |
| NG=F      |     -2 |   -11.8 |
| NVDA      |     +0 |    +0.3 |
| PL=F      |     -3 |    -9.7 |
| SI=F      |     +0 |    -1.8 |
| TSLA      |     -6 |   -12.4 |
| UNH       |     +0 |    +3.6 |
| XOM       |     +0 |    -4.2 |
| ZC=F      |     +2 |    +8.2 |
| ZS=F      |     +3 |    +8.5 |
| ZW=F      |     +4 |   +13.6 |
| ^DJI      |     +0 |    +1.8 |
| ^FCHI     |     -1 |    -2.4 |
| ^FTSE     |     +1 |    +0.9 |
| ^GDAXI    |     -1 |    -2.1 |
| ^GSPC     |     -3 |    -6.7 |
| ^HSI      |     -1 |    -7.0 |
| ^N225     |     +2 |   +14.6 |
| ^NDX      |     -2 |    -8.2 |
| ^RUT      |     -1 |    -0.3 |
| ^STOXX50E |     -1 |    -3.3 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Natural Gas / NG=F** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars
- **Copper / HG=F** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|    9 | Soybeans / ZS=F        |  63.9 |   Yes    | —               | 20d down -1.4%; above MA20 by 1.6%; RSI14=51  |
|   17 | Corn / ZC=F            |  39.4 |   Yes    | —               | 20d down -6.1%; below MA20 by 1.0%; RSI14=40  |
|   19 | Wheat / ZW=F           |  31.2 |   Yes    | —               | 20d down -10.2%; below MA20 by 2.4%; RSI14=36 |
|   20 | Gold / GC=F            |  26.1 |   Yes    | —               | 20d down -7.1%; below MA20 by 3.7%; RSI14=40  |
|   22 | Brent Crude Oil / BZ=F |  20.3 |   Yes    | —               | 20d down -12.8%; below MA20 by 8.8%; RSI14=28 |
|   23 | Platinum / PL=F        |  18.2 |   Yes    | —               | 20d down -8.3%; below MA20 by 3.0%; RSI14=44  |
|   24 | Silver / SI=F          |   8.5 |   Yes    | —               | 20d down -14.0%; below MA20 by 7.0%; RSI14=35 |
|   28 | Natural Gas / NG=F     |  65.5 |    No    | malformed_input | Suppressed: malformed_input                   |
|   32 | Copper / HG=F          |  26.4 |    No    | malformed_input | Suppressed: malformed_input                   |
|   33 | WTI Crude Oil / CL=F   |  23.6 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                    |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | ---------------------------------------------- |
|    1 | Apple Inc. / AAPL                                                              |  79.1 |   Yes    | —                             | 20d up +3.8%; above MA20 by 3.0%; RSI14=59     |
|    6 | JPMorgan Chase & Co. / JPM                                                     |  66.7 |   Yes    | —                             | 20d up +1.9%; above MA20 by 2.1%; RSI14=59     |
|    7 | Amazon.com Inc. / AMZN                                                         |  65.5 |   Yes    | —                             | 20d up +6.7%; above MA20 by 3.6%; RSI14=62     |
|    8 | UnitedHealth Group Inc. / UNH                                                  |  64.2 |   Yes    | —                             | 20d up +1.5%; below MA20 by 0.1%; RSI14=47     |
|   11 | Tesla Inc. / TSLA                                                              |  57.6 |   Yes    | —                             | 20d up +10.0%; above MA20 by 1.3%; RSI14=50    |
|   12 | Meta Platforms Inc. / META                                                     |  54.9 |   Yes    | —                             | 20d down -9.5%; above MA20 by 0.7%; RSI14=53   |
|   13 | Microsoft Corporation / MSFT                                                   |  51.2 |   Yes    | —                             | 20d down -1.0%; below MA20 by 1.0%; RSI14=47   |
|   21 | Alphabet Inc. Class A / GOOGL                                                  |  25.8 |   Yes    | —                             | 20d down -13.2%; below MA20 by 2.5%; RSI14=38  |
|   25 | NVIDIA Corporation / NVDA                                                      |   3.0 |   Yes    | —                             | 20d down -23.9%; below MA20 by 18.0%; RSI14=19 |
|   26 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  81.8 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   27 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  70.0 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   29 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  56.1 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   30 | Exxon Mobil Corporation / XOM                                                  |  44.5 |    No    | malformed_input               | Suppressed: malformed_input                    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    2 | DAX / ^GDAXI                        |  77.0 |   Yes    | —            | 20d up +4.4%; above MA20 by 3.2%; RSI14=70   |
|    3 | CAC 40 / ^FCHI                      |  74.8 |   Yes    | —            | 20d up +5.2%; above MA20 by 4.0%; RSI14=87   |
|    4 | Euro Stoxx 50 / ^STOXX50E           |  72.7 |   Yes    | —            | 20d up +2.9%; above MA20 by 2.8%; RSI14=69   |
|    5 | FTSE 100 / ^FTSE                    |  70.9 |   Yes    | —            | 20d up +0.2%; above MA20 by 1.4%; RSI14=57   |
|   10 | Dow Jones Industrial Average / ^DJI |  59.7 |   Yes    | —            | 20d up +0.7%; above MA20 by 0.1%; RSI14=50   |
|   14 | S&P 500 / ^GSPC                     |  50.6 |   Yes    | —            | 20d down -1.3%; below MA20 by 0.7%; RSI14=45 |
|   15 | Russell 2000 / ^RUT                 |  49.7 |   Yes    | —            | 20d up +2.5%; below MA20 by 0.4%; RSI14=50   |
|   16 | Hang Seng / ^HSI                    |  41.8 |   Yes    | —            | 20d down -1.8%; below MA20 by 0.4%; RSI14=56 |
|   18 | NASDAQ 100 / ^NDX                   |  36.7 |   Yes    | —            | 20d down -4.3%; below MA20 by 2.3%; RSI14=41 |
|   31 | Nikkei 225 / ^N225                  |  42.7 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-11-13 |
| 7203.T    | 2026-11-13 |
| 8306.T    | 2026-11-13 |
| AAPL      | 2026-11-13 |
| AMZN      | 2026-11-13 |
| BZ=F      | 2026-11-13 |
| CL=F      | 2026-11-13 |
| GC=F      | 2026-11-13 |
| GOOGL     | 2026-11-13 |
| HG=F      | 2026-11-13 |
| JPM       | 2026-11-13 |
| META      | 2026-11-13 |
| MSFT      | 2026-11-13 |
| NG=F      | 2026-11-13 |
| NVDA      | 2026-11-13 |
| PL=F      | 2026-11-13 |
| SI=F      | 2026-11-13 |
| TSLA      | 2026-11-13 |
| UNH       | 2026-11-13 |
| XOM       | 2026-11-13 |
| ZC=F      | 2026-11-13 |
| ZS=F      | 2026-11-13 |
| ZW=F      | 2026-11-13 |
| ^DJI      | 2026-11-13 |
| ^FCHI     | 2026-11-13 |
| ^FTSE     | 2026-11-13 |
| ^GDAXI    | 2026-11-13 |
| ^GSPC     | 2026-11-13 |
| ^HSI      | 2026-11-13 |
| ^N225     | 2026-11-13 |
| ^NDX      | 2026-11-13 |
| ^RUT      | 2026-11-13 |
| ^STOXX50E | 2026-11-13 |

## Symbol Details

### Apple Inc. / AAPL (score 79.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.4% |
| ret_5d     |  +4.1% |
| ret_20d    |  +3.8% |
| ret_60d    | +14.4% |
| ma20_dist  |  +3.0% |
| ma50_dist  |  +5.1% |
| vol_20d    |  27.1% |
| mdd_60d    |   4.9% |
| rsi_14     |   58.7 |
| zscore_20d |    1.8 |

### DAX / ^GDAXI (score 77.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | +3.6% |
| ret_20d    | +4.4% |
| ret_60d    | +2.3% |
| ma20_dist  | +3.2% |
| ma50_dist  | +4.5% |
| vol_20d    | 16.6% |
| mdd_60d    |  6.6% |
| rsi_14     |  70.3 |
| zscore_20d |   1.7 |

### CAC 40 / ^FCHI (score 74.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | +2.8% |
| ret_20d    | +5.2% |
| ret_60d    | -1.4% |
| ma20_dist  | +4.0% |
| ma50_dist  | +4.2% |
| vol_20d    | 12.9% |
| mdd_60d    |  8.7% |
| rsi_14     |  86.7 |
| zscore_20d |   1.7 |

### Euro Stoxx 50 / ^STOXX50E (score 72.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | +3.5% |
| ret_20d    | +2.9% |
| ret_60d    | -1.2% |
| ma20_dist  | +2.8% |
| ma50_dist  | +2.4% |
| vol_20d    | 16.2% |
| mdd_60d    |  6.4% |
| rsi_14     |  69.3 |
| zscore_20d |   1.8 |

### FTSE 100 / ^FTSE (score 70.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | +2.1% |
| ret_20d    | +0.2% |
| ret_60d    | +1.4% |
| ma20_dist  | +1.4% |
| ma50_dist  | +1.9% |
| vol_20d    | 11.4% |
| mdd_60d    |  4.2% |
| rsi_14     |  57.4 |
| zscore_20d |   2.3 |

### JPMorgan Chase & Co. / JPM (score 66.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.0% |
| ret_5d     | +3.5% |
| ret_20d    | +1.9% |
| ret_60d    | -1.5% |
| ma20_dist  | +2.1% |
| ma50_dist  | +1.9% |
| vol_20d    | 26.7% |
| mdd_60d    |  9.1% |
| rsi_14     |  59.1 |
| zscore_20d |   1.5 |

### Amazon.com Inc. / AMZN (score 65.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | +2.8% |
| ret_20d    | +6.7% |
| ret_60d    | +2.5% |
| ma20_dist  | +3.6% |
| ma50_dist  | +4.6% |
| vol_20d    | 40.9% |
| mdd_60d    |  9.8% |
| rsi_14     |  62.5 |
| zscore_20d |   1.0 |

### UnitedHealth Group Inc. / UNH (score 64.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | +3.4% |
| ret_20d    | +1.5% |
| ret_60d    | +6.5% |
| ma20_dist  | -0.1% |
| ma50_dist  | +4.2% |
| vol_20d    | 23.7% |
| mdd_60d    |  8.4% |
| rsi_14     |  47.3 |
| zscore_20d |  -0.0 |

### Soybeans / ZS=F (score 63.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.3% |
| ret_5d     | +4.5% |
| ret_20d    | -1.4% |
| ret_60d    | +1.5% |
| ma20_dist  | +1.6% |
| ma50_dist  | -2.0% |
| vol_20d    | 17.0% |
| mdd_60d    | 11.1% |
| rsi_14     |  50.6 |
| zscore_20d |   0.8 |

### Dow Jones Industrial Average / ^DJI (score 59.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | +2.1% |
| ret_20d    | +0.7% |
| ret_60d    | -0.8% |
| ma20_dist  | +0.1% |
| ma50_dist  | +0.7% |
| vol_20d    | 19.8% |
| mdd_60d    |  5.2% |
| rsi_14     |  49.9 |
| zscore_20d |   0.2 |

### Tesla Inc. / TSLA (score 57.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.8% |
| ret_5d     |  +8.9% |
| ret_20d    | +10.0% |
| ret_60d    | +13.1% |
| ma20_dist  |  +1.3% |
| ma50_dist  |  +4.1% |
| vol_20d    |  58.4% |
| mdd_60d    |  15.7% |
| rsi_14     |   49.5 |
| zscore_20d |    0.3 |

### Meta Platforms Inc. / META (score 54.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.9% |
| ret_5d     |  +5.2% |
| ret_20d    |  -9.5% |
| ret_60d    | +17.7% |
| ma20_dist  |  +0.7% |
| ma50_dist  |  -5.6% |
| vol_20d    |  40.0% |
| mdd_60d    |  22.2% |
| rsi_14     |   53.3 |
| zscore_20d |    0.2 |

### Microsoft Corporation / MSFT (score 51.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | -1.3% |
| ret_20d    | -1.0% |
| ret_60d    | +8.9% |
| ma20_dist  | -1.0% |
| ma50_dist  | +0.9% |
| vol_20d    | 36.0% |
| mdd_60d    |  6.7% |
| rsi_14     |  46.9 |
| zscore_20d |  -0.6 |

### S&P 500 / ^GSPC (score 50.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | +2.5% |
| ret_20d    | -1.3% |
| ret_60d    | -1.0% |
| ma20_dist  | -0.7% |
| ma50_dist  | -1.4% |
| vol_20d    | 21.4% |
| mdd_60d    |  5.9% |
| rsi_14     |  44.9 |
| zscore_20d |  -0.5 |

### Russell 2000 / ^RUT (score 49.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | +1.3% |
| ret_20d    | +2.5% |
| ret_60d    | -6.7% |
| ma20_dist  | -0.4% |
| ma50_dist  | -1.2% |
| vol_20d    | 23.9% |
| mdd_60d    |  9.8% |
| rsi_14     |  50.4 |
| zscore_20d |  -0.3 |

### Hang Seng / ^HSI (score 41.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.5% |
| ret_5d     | -3.4% |
| ret_20d    | -1.8% |
| ret_60d    | -7.3% |
| ma20_dist  | -0.4% |
| ma50_dist  | -2.7% |
| vol_20d    | 22.2% |
| mdd_60d    | 11.8% |
| rsi_14     |  56.0 |
| zscore_20d |  -0.1 |

### Corn / ZC=F (score 39.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | +0.9% |
| ret_20d    | -6.1% |
| ret_60d    | -7.9% |
| ma20_dist  | -1.0% |
| ma50_dist  | -8.3% |
| vol_20d    | 14.2% |
| mdd_60d    | 19.1% |
| rsi_14     |  40.2 |
| zscore_20d |  -0.6 |

### NASDAQ 100 / ^NDX (score 36.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.2% |
| ret_5d     | +3.5% |
| ret_20d    | -4.3% |
| ret_60d    | -4.3% |
| ma20_dist  | -2.3% |
| ma50_dist  | -5.3% |
| vol_20d    | 34.0% |
| mdd_60d    | 14.7% |
| rsi_14     |  40.7 |
| zscore_20d |  -0.7 |

### Wheat / ZW=F (score 31.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.5% |
| ret_5d     |  +0.3% |
| ret_20d    | -10.2% |
| ret_60d    | -12.9% |
| ma20_dist  |  -2.4% |
| ma50_dist  | -10.5% |
| vol_20d    |  17.9% |
| mdd_60d    |  23.8% |
| rsi_14     |   35.9 |
| zscore_20d |   -0.8 |

### Gold / GC=F (score 26.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.0% |
| ret_5d     |  -4.6% |
| ret_20d    |  -7.1% |
| ret_60d    | -17.4% |
| ma20_dist  |  -3.7% |
| ma50_dist  |  -7.1% |
| vol_20d    |  24.6% |
| mdd_60d    |  17.3% |
| rsi_14     |   40.4 |
| zscore_20d |   -1.8 |

### Alphabet Inc. Class A / GOOGL (score 25.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.0% |
| ret_5d     |  +3.9% |
| ret_20d    | -13.2% |
| ret_60d    | -13.1% |
| ma20_dist  |  -2.5% |
| ma50_dist  |  -9.9% |
| vol_20d    |  50.2% |
| mdd_60d    |  21.4% |
| rsi_14     |   38.4 |
| zscore_20d |   -0.4 |

### Brent Crude Oil / BZ=F (score 20.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.0% |
| ret_5d     |  -2.5% |
| ret_20d    | -12.8% |
| ret_60d    |  +3.5% |
| ma20_dist  |  -8.8% |
| ma50_dist  |  -8.1% |
| vol_20d    |  60.4% |
| mdd_60d    |  22.2% |
| rsi_14     |   27.5 |
| zscore_20d |   -1.0 |

### Platinum / PL=F (score 18.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.9% |
| ret_5d     |  -3.2% |
| ret_20d    |  -8.3% |
| ret_60d    | -21.4% |
| ma20_dist  |  -3.0% |
| ma50_dist  | -10.0% |
| vol_20d    |  32.3% |
| mdd_60d    |  25.2% |
| rsi_14     |   43.6 |
| zscore_20d |   -0.8 |

### Silver / SI=F (score 8.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.9% |
| ret_5d     |  -5.4% |
| ret_20d    | -14.0% |
| ret_60d    | -29.2% |
| ma20_dist  |  -7.0% |
| ma50_dist  | -16.2% |
| vol_20d    |  40.9% |
| mdd_60d    |  29.4% |
| rsi_14     |   35.1 |
| zscore_20d |   -1.5 |

### NVIDIA Corporation / NVDA (score 3.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.0% |
| ret_5d     | -12.7% |
| ret_20d    | -23.9% |
| ret_60d    | -24.8% |
| ma20_dist  | -18.0% |
| ma50_dist  | -24.1% |
| vol_20d    |  51.4% |
| mdd_60d    |  31.9% |
| rsi_14     |   19.1 |
| zscore_20d |   -1.9 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Apple Inc. / AAPL                   |   9.4491 |           2.7% |                 0.37x |       18.8983 |            5.3% |
| DAX / ^GDAXI                        | 378.9187 |           1.4% |                 0.60x |      757.8373 |            2.8% |
| CAC 40 / ^FCHI                      | 100.7264 |           1.2% |                 0.77x |      201.4528 |            2.4% |
| Euro Stoxx 50 / ^STOXX50E           |  86.6750 |           1.4% |                 0.62x |      173.3501 |            2.7% |
| FTSE 100 / ^FTSE                    | 120.8215 |           1.1% |                 0.88x |      241.6430 |            2.2% |
| JPMorgan Chase & Co. / JPM          |   7.7807 |           2.2% |                 0.37x |       15.5614 |            4.5% |
| Amazon.com Inc. / AMZN              |  10.7450 |           4.0% |                 0.24x |       21.4900 |            8.1% |
| UnitedHealth Group Inc. / UNH       |  10.8129 |           2.7% |                 0.42x |       21.6257 |            5.3% |
| Soybeans / ZS=F                     |  18.1964 |           1.5% |                 0.59x |       36.3929 |            2.9% |
| Dow Jones Industrial Average / ^DJI | 752.9395 |           1.4% |                 0.51x |     1505.8789 |            2.9% |
| Tesla Inc. / TSLA                   |  18.1629 |           4.7% |                 0.17x |       36.3257 |            9.3% |
| Meta Platforms Inc. / META          |  20.9586 |           3.3% |                 0.25x |       41.9171 |            6.5% |
| Microsoft Corporation / MSFT        |  17.5536 |           3.4% |                 0.28x |       35.1072 |            6.7% |
| S&P 500 / ^GSPC                     | 123.3900 |           1.6% |                 0.47x |      246.7801 |            3.3% |
| Russell 2000 / ^RUT                 |  52.5086 |           1.9% |                 0.42x |      105.0171 |            3.8% |
| Hang Seng / ^HSI                    | 371.4003 |           1.6% |                 0.45x |      742.8005 |            3.1% |
| Corn / ZC=F                         |   7.3214 |           1.6% |                 0.70x |       14.6429 |            3.3% |
| NASDAQ 100 / ^NDX                   | 754.5773 |           2.7% |                 0.29x |     1509.1546 |            5.4% |
| Wheat / ZW=F                        |  13.9643 |           2.4% |                 0.56x |       27.9286 |            4.7% |
| Gold / GC=F                         |  98.2643 |           2.5% |                 0.41x |      196.5285 |            5.1% |
| Alphabet Inc. Class A / GOOGL       |  11.9107 |           4.0% |                 0.20x |       23.8214 |            8.1% |
| Brent Crude Oil / BZ=F              |   5.5164 |           5.8% |                 0.17x |       11.0329 |           11.5% |
| Platinum / PL=F                     |  33.1143 |           2.2% |                 0.31x |       66.2286 |            4.4% |
| Silver / SI=F                       |   1.5813 |           3.2% |                 0.24x |        3.1626 |            6.5% |
| NVIDIA Corporation / NVDA           |  11.0050 |           6.8% |                 0.19x |       22.0100 |           13.5% |

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

Scoring engine version: **1.0.0** | Git commit: **f5bda3a**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
