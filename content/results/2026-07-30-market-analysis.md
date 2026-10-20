+++
title = "Market Analysis 2026-07-30"
date = "2026-07-30T00:00:00+00:00"
draft = false
summary = "Neutral market: 26 reliable instruments. Top signal: ^FTSE (score 81.8)."
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
source_files = ["data/analysis/2026-07-30.json", "data/history/2026-07-30.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "cb0d3ec"
+++

## Market Regime

**Neutral** — 10 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **FTSE 100 / ^FTSE** — score 81.8, 20d return +4.1%, RSI14=78. 20d up +4.1%; above MA20 by 2.6%; RSI14=78
- **Apple Inc. / AAPL** — score 76.1, 20d return +16.9%, RSI14=69. 20d up +16.9%; above MA20 by 4.9%; RSI14=69
- **Hang Seng / ^HSI** — score 74.5, 20d return +12.8%, RSI14=74. 20d up +12.8%; above MA20 by 5.3%; RSI14=74
- **DAX / ^GDAXI** — score 68.5, 20d return +1.7%, RSI14=59. 20d up +1.7%; above MA20 by 1.1%; RSI14=59
- **CAC 40 / ^FCHI** — score 63.0, 20d return +0.9%, RSI14=57. 20d up +0.9%; above MA20 by 0.3%; RSI14=57

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                        | Applies To                    |
| ---------- | ---------------------------- | ----------------------------- |
| 2026-07-31 | 6758.T earnings release      | 6758.T                        |
| 2026-07-31 | BOJ monetary policy decision | 6758.T, 7203.T, 8306.T, ^N225 |
| 2026-07-31 | XOM earnings release         | XOM                           |
| 2026-08-03 | 8306.T earnings release      | 8306.T                        |
| 2026-08-04 | 7203.T earnings release      | 7203.T                        |

## Signal History

Compared with the previous available report (**2026-07-29**).

- **New top-5:** ^GDAXI, ^HSI
- **Persistent top signals:** ^FTSE (6 reports), AAPL (4 reports), ^FCHI (2 reports)
- **Dropped from top-5:** JPM, ZC=F

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     -1 |    +2.4 |
| 7203.T    |     +2 |   +15.4 |
| 8306.T    |     -2 |    +2.1 |
| AAPL      |     -1 |    -6.4 |
| AMZN      |     -1 |    -1.8 |
| BZ=F      |    +10 |   +25.4 |
| CL=F      |     +1 |   +23.9 |
| GC=F      |     +1 |    +7.3 |
| GOOGL     |     +4 |    +6.4 |
| HG=F      |     -1 |    -2.1 |
| JPM       |     -4 |   -20.0 |
| META      |     -2 |    +0.3 |
| MSFT      |     +2 |    -0.3 |
| NG=F      |     +2 |   +11.2 |
| NVDA      |     -4 |   -12.1 |
| PL=F      |     -2 |    -2.7 |
| SI=F      |     +3 |    +9.4 |
| TSLA      |     +0 |    -1.2 |
| UNH       |     +0 |   -11.2 |
| XOM       |     +1 |   +12.1 |
| ZC=F      |     -6 |   -17.6 |
| ZS=F      |     -3 |   -14.8 |
| ZW=F      |     +2 |    -3.3 |
| ^DJI      |     -7 |   -18.8 |
| ^FCHI     |     -1 |    -5.5 |
| ^FTSE     |     +2 |    +2.7 |
| ^GDAXI    |     +3 |    +1.8 |
| ^GSPC     |     -2 |    -5.8 |
| ^HSI      |     +5 |    +8.2 |
| ^N225     |     +0 |    +2.7 |
| ^NDX      |     -2 |    -2.1 |
| ^RUT      |     -3 |    -6.7 |
| ^STOXX50E |     +4 |    +0.9 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **WTI Crude Oil / CL=F** — malformed_input
- **Copper / HG=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|    7 | Wheat / ZW=F           |  59.4 |   Yes    | —               | 20d up +13.8%; above MA20 by 2.1%; RSI14=64   |
|    9 | Brent Crude Oil / BZ=F |  55.1 |   Yes    | —               | 20d up +24.4%; above MA20 by 8.0%; RSI14=65   |
|   11 | Corn / ZC=F            |  50.0 |   Yes    | —               | 20d up +8.8%; above MA20 by 1.0%; RSI14=62    |
|   14 | Soybeans / ZS=F        |  43.9 |   Yes    | —               | 20d up +5.5%; below MA20 by 1.8%; RSI14=50    |
|   15 | Gold / GC=F            |  43.3 |   Yes    | —               | 20d up +0.3%; below MA20 by 0.8%; RSI14=42    |
|   19 | Platinum / PL=F        |  30.9 |   Yes    | —               | 20d up +2.6%; below MA20 by 1.5%; RSI14=44    |
|   21 | Silver / SI=F          |  27.9 |   Yes    | —               | 20d down -2.7%; below MA20 by 1.4%; RSI14=42  |
|   23 | Natural Gas / NG=F     |  22.7 |   Yes    | —               | 20d down -16.8%; below MA20 by 7.9%; RSI14=30 |
|   31 | WTI Crude Oil / CL=F   |  55.5 |    No    | malformed_input | Suppressed: malformed_input                   |
|   32 | Copper / HG=F          |  53.0 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                   |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | --------------------------------------------- |
|    2 | Apple Inc. / AAPL                                                              |  76.1 |   Yes    | —                             | 20d up +16.9%; above MA20 by 4.9%; RSI14=69   |
|    6 | JPMorgan Chase & Co. / JPM                                                     |  61.8 |   Yes    | —                             | 20d up +5.8%; above MA20 by 0.7%; RSI14=58    |
|   10 | UnitedHealth Group Inc. / UNH                                                  |  51.2 |   Yes    | —                             | 20d up +1.2%; below MA20 by 1.1%; RSI14=44    |
|   12 | Microsoft Corporation / MSFT                                                   |  48.2 |   Yes    | —                             | 20d up +4.7%; above MA20 by 0.2%; RSI14=54    |
|   18 | Alphabet Inc. Class A / GOOGL                                                  |  31.2 |   Yes    | —                             | 20d down -5.8%; below MA20 by 3.7%; RSI14=40  |
|   20 | Meta Platforms Inc. / META                                                     |  30.3 |   Yes    | —                             | 20d up +4.0%; below MA20 by 6.4%; RSI14=37    |
|   24 | Amazon.com Inc. / AMZN                                                         |  20.0 |   Yes    | —                             | 20d down -4.9%; below MA20 by 6.6%; RSI14=27  |
|   25 | NVIDIA Corporation / NVDA                                                      |  15.8 |   Yes    | —                             | 20d down -5.0%; below MA20 by 6.5%; RSI14=40  |
|   26 | Tesla Inc. / TSLA                                                              |   4.8 |   Yes    | —                             | 20d down -29.1%; below MA20 by 20.2%; RSI14=9 |
|   27 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  82.4 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars     |
|   28 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  81.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars     |
|   29 | Exxon Mobil Corporation / XOM                                                  |  74.5 |    No    | malformed_input               | Suppressed: malformed_input                   |
|   30 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  71.5 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars     |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                   |
| ---: | ----------------------------------- | ----: | :------: | ------------ | --------------------------------------------- |
|    1 | FTSE 100 / ^FTSE                    |  81.8 |   Yes    | —            | 20d up +4.1%; above MA20 by 2.6%; RSI14=78    |
|    3 | Hang Seng / ^HSI                    |  74.5 |   Yes    | —            | 20d up +12.8%; above MA20 by 5.3%; RSI14=74   |
|    4 | DAX / ^GDAXI                        |  68.5 |   Yes    | —            | 20d up +1.7%; above MA20 by 1.1%; RSI14=59    |
|    5 | CAC 40 / ^FCHI                      |  63.0 |   Yes    | —            | 20d up +0.9%; above MA20 by 0.3%; RSI14=57    |
|    8 | Euro Stoxx 50 / ^STOXX50E           |  58.8 |   Yes    | —            | 20d down -0.5%; below MA20 by 0.6%; RSI14=46  |
|   13 | Dow Jones Industrial Average / ^DJI |  48.2 |   Yes    | —            | 20d down -1.4%; below MA20 by 1.5%; RSI14=40  |
|   16 | Russell 2000 / ^RUT                 |  43.0 |   Yes    | —            | 20d down -3.9%; below MA20 by 2.0%; RSI14=34  |
|   17 | S&P 500 / ^GSPC                     |  41.5 |   Yes    | —            | 20d down -2.4%; below MA20 by 2.2%; RSI14=30  |
|   22 | NASDAQ 100 / ^NDX                   |  27.0 |   Yes    | —            | 20d down -10.2%; below MA20 by 6.1%; RSI14=22 |
|   33 | Nikkei 225 / ^N225                  |  22.7 |    No    | missing_bars | Suppressed: missing_bars                      |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-07-29 |
| 7203.T    | 2026-07-29 |
| 8306.T    | 2026-07-29 |
| AAPL      | 2026-07-29 |
| AMZN      | 2026-07-29 |
| BZ=F      | 2026-07-29 |
| CL=F      | 2026-07-29 |
| GC=F      | 2026-07-29 |
| GOOGL     | 2026-07-29 |
| HG=F      | 2026-07-29 |
| JPM       | 2026-07-29 |
| META      | 2026-07-29 |
| MSFT      | 2026-07-29 |
| NG=F      | 2026-07-29 |
| NVDA      | 2026-07-29 |
| PL=F      | 2026-07-29 |
| SI=F      | 2026-07-29 |
| TSLA      | 2026-07-29 |
| UNH       | 2026-07-29 |
| XOM       | 2026-07-29 |
| ZC=F      | 2026-07-29 |
| ZS=F      | 2026-07-29 |
| ZW=F      | 2026-07-29 |
| ^DJI      | 2026-07-29 |
| ^FCHI     | 2026-07-29 |
| ^FTSE     | 2026-07-29 |
| ^GDAXI    | 2026-07-29 |
| ^GSPC     | 2026-07-29 |
| ^HSI      | 2026-07-29 |
| ^N225     | 2026-07-29 |
| ^NDX      | 2026-07-29 |
| ^RUT      | 2026-07-29 |
| ^STOXX50E | 2026-07-29 |

## Symbol Details

### FTSE 100 / ^FTSE (score 81.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +1.8% |
| ret_20d    | +4.1% |
| ret_60d    | +6.7% |
| ma20_dist  | +2.6% |
| ma50_dist  | +3.9% |
| vol_20d    | 11.3% |
| mdd_60d    |  2.6% |
| rsi_14     |  78.3 |
| zscore_20d |   2.3 |

### Apple Inc. / AAPL (score 76.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.6% |
| ret_5d     |  +3.8% |
| ret_20d    | +16.9% |
| ret_60d    | +20.8% |
| ma20_dist  |  +4.9% |
| ma50_dist  |  +9.6% |
| vol_20d    |  27.4% |
| mdd_60d    |  12.7% |
| rsi_14     |   68.6 |
| zscore_20d |    1.4 |

### Hang Seng / ^HSI (score 74.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.0% |
| ret_5d     |  +3.7% |
| ret_20d    | +12.8% |
| ret_60d    |  +0.1% |
| ma20_dist  |  +5.3% |
| ma50_dist  |  +5.0% |
| vol_20d    |  18.6% |
| mdd_60d    |  14.9% |
| rsi_14     |   74.2 |
| zscore_20d |    1.8 |

### DAX / ^GDAXI (score 68.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.0% |
| ret_5d     | +1.2% |
| ret_20d    | +1.7% |
| ret_60d    | +2.2% |
| ma20_dist  | +1.1% |
| ma50_dist  | +1.8% |
| vol_20d    | 15.8% |
| mdd_60d    |  4.7% |
| rsi_14     |  59.2 |
| zscore_20d |   0.9 |

### CAC 40 / ^FCHI (score 63.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | -0.4% |
| ret_20d    | +0.9% |
| ret_60d    | +1.3% |
| ma20_dist  | +0.3% |
| ma50_dist  | +1.0% |
| vol_20d    | 13.5% |
| mdd_60d    |  3.0% |
| rsi_14     |  57.5 |
| zscore_20d |   0.3 |

### JPMorgan Chase & Co. / JPM (score 61.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -3.5% |
| ret_5d     |  -1.0% |
| ret_20d    |  +5.8% |
| ret_60d    | +10.8% |
| ma20_dist  |  +0.7% |
| ma50_dist  |  +6.2% |
| vol_20d    |  23.0% |
| mdd_60d    |   6.1% |
| rsi_14     |   58.5 |
| zscore_20d |    0.3 |

### Wheat / ZW=F (score 59.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.3% |
| ret_5d     |  -6.4% |
| ret_20d    | +13.8% |
| ret_60d    |  +5.8% |
| ma20_dist  |  +2.1% |
| ma50_dist  |  +6.2% |
| vol_20d    |  37.4% |
| mdd_60d    |  14.6% |
| rsi_14     |   63.9 |
| zscore_20d |    0.4 |

### Euro Stoxx 50 / ^STOXX50E (score 58.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | -1.1% |
| ret_20d    | -0.5% |
| ret_60d    | +8.4% |
| ma20_dist  | -0.6% |
| ma50_dist  | +0.7% |
| vol_20d    | 13.9% |
| mdd_60d    |  3.6% |
| rsi_14     |  45.9 |
| zscore_20d |  -0.7 |

### Brent Crude Oil / BZ=F (score 55.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +7.9% |
| ret_5d     |  -3.5% |
| ret_20d    | +24.4% |
| ret_60d    | -16.1% |
| ma20_dist  |  +8.0% |
| ma50_dist  |  +3.8% |
| vol_20d    |  68.9% |
| mdd_60d    |  37.5% |
| rsi_14     |   64.5 |
| zscore_20d |    0.8 |

### UnitedHealth Group Inc. / UNH (score 51.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.9% |
| ret_5d     |  -2.5% |
| ret_20d    |  +1.2% |
| ret_60d    | +14.7% |
| ma20_dist  |  -1.1% |
| ma50_dist  |  +3.0% |
| vol_20d    |  26.8% |
| mdd_60d    |   6.1% |
| rsi_14     |   43.6 |
| zscore_20d |   -1.0 |

### Corn / ZC=F (score 50.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.1% |
| ret_5d     | -2.8% |
| ret_20d    | +8.8% |
| ret_60d    | -4.1% |
| ma20_dist  | +1.0% |
| ma50_dist  | +2.9% |
| vol_20d    | 27.4% |
| mdd_60d    | 15.7% |
| rsi_14     |  62.4 |
| zscore_20d |   0.4 |

### Microsoft Corporation / MSFT (score 48.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | +0.1% |
| ret_20d    | +4.7% |
| ret_60d    | -5.6% |
| ma20_dist  | +0.2% |
| ma50_dist  | -1.8% |
| vol_20d    | 25.5% |
| mdd_60d    | 23.4% |
| rsi_14     |  53.9 |
| zscore_20d |   0.1 |

### Dow Jones Industrial Average / ^DJI (score 48.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.2% |
| ret_5d     | -1.2% |
| ret_20d    | -1.4% |
| ret_60d    | +4.2% |
| ma20_dist  | -1.5% |
| ma50_dist  | +0.0% |
| vol_20d    | 12.1% |
| mdd_60d    |  3.2% |
| rsi_14     |  39.7 |
| zscore_20d |  -2.0 |

### Soybeans / ZS=F (score 43.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.8% |
| ret_5d     | -4.5% |
| ret_20d    | +5.5% |
| ret_60d    | -0.8% |
| ma20_dist  | -1.8% |
| ma50_dist  | +0.8% |
| vol_20d    | 25.0% |
| mdd_60d    |  8.8% |
| rsi_14     |  49.5 |
| zscore_20d |  -0.7 |

### Gold / GC=F (score 43.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.0% |
| ret_5d     |  -2.7% |
| ret_20d    |  +0.3% |
| ret_60d    | -12.9% |
| ma20_dist  |  -0.8% |
| ma50_dist  |  -4.4% |
| vol_20d    |  20.8% |
| mdd_60d    |  15.6% |
| rsi_14     |   42.1 |
| zscore_20d |   -0.7 |

### Russell 2000 / ^RUT (score 43.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.6% |
| ret_5d     | -1.8% |
| ret_20d    | -3.9% |
| ret_60d    | +3.3% |
| ma20_dist  | -2.0% |
| ma50_dist  | -1.0% |
| vol_20d    | 12.1% |
| mdd_60d    |  4.8% |
| rsi_14     |  34.0 |
| zscore_20d |  -2.3 |

### S&P 500 / ^GSPC (score 41.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.5% |
| ret_5d     | -2.4% |
| ret_20d    | -2.4% |
| ret_60d    | +1.2% |
| ma20_dist  | -2.2% |
| ma50_dist  | -2.0% |
| vol_20d    | 10.2% |
| mdd_60d    |  4.5% |
| rsi_14     |  30.3 |
| zscore_20d |  -2.6 |

### Alphabet Inc. Class A / GOOGL (score 31.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.9% |
| ret_5d     |  -1.6% |
| ret_20d    |  -5.8% |
| ret_60d    | -12.6% |
| ma20_dist  |  -3.7% |
| ma50_dist  |  -6.6% |
| vol_20d    |  37.9% |
| mdd_60d    |  21.0% |
| rsi_14     |   39.7 |
| zscore_20d |   -0.8 |

### Platinum / PL=F (score 30.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.4% |
| ret_5d     |  -3.2% |
| ret_20d    |  +2.6% |
| ret_60d    | -20.4% |
| ma20_dist  |  -1.5% |
| ma50_dist  |  -7.6% |
| vol_20d    |  28.7% |
| mdd_60d    |  29.1% |
| rsi_14     |   44.3 |
| zscore_20d |   -1.2 |

### Meta Platforms Inc. / META (score 30.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.3% |
| ret_5d     | -6.6% |
| ret_20d    | +4.0% |
| ret_60d    | -3.7% |
| ma20_dist  | -6.4% |
| ma50_dist  | -3.1% |
| vol_20d    | 53.6% |
| mdd_60d    | 14.5% |
| rsi_14     |  36.5 |
| zscore_20d |  -1.3 |

### Silver / SI=F (score 27.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.0% |
| ret_5d     |  -3.6% |
| ret_20d    |  -2.7% |
| ret_60d    | -23.8% |
| ma20_dist  |  -1.4% |
| ma50_dist  | -11.0% |
| vol_20d    |  37.9% |
| mdd_60d    |  37.1% |
| rsi_14     |   42.1 |
| zscore_20d |   -0.5 |

### NASDAQ 100 / ^NDX (score 27.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.1% |
| ret_5d     |  -6.2% |
| ret_20d    | -10.2% |
| ret_60d    |  -1.9% |
| ma20_dist  |  -6.1% |
| ma50_dist  |  -7.6% |
| vol_20d    |  19.7% |
| mdd_60d    |  11.3% |
| rsi_14     |   21.8 |
| zscore_20d |   -2.5 |

### Natural Gas / NG=F (score 22.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.4% |
| ret_5d     |  -6.8% |
| ret_20d    | -16.8% |
| ret_60d    |  -2.0% |
| ma20_dist  |  -7.9% |
| ma50_dist  | -11.5% |
| vol_20d    |  34.0% |
| mdd_60d    |  20.4% |
| rsi_14     |   29.6 |
| zscore_20d |   -1.4 |

### Amazon.com Inc. / AMZN (score 20.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.8% |
| ret_5d     |  -7.4% |
| ret_20d    |  -4.9% |
| ret_60d    | -15.5% |
| ma20_dist  |  -6.6% |
| ma50_dist  |  -8.2% |
| vol_20d    |  24.7% |
| mdd_60d    |  17.6% |
| rsi_14     |   27.4 |
| zscore_20d |   -2.2 |

### NVIDIA Corporation / NVDA (score 15.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -3.6% |
| ret_5d     | -10.4% |
| ret_20d    |  -5.0% |
| ret_60d    |  -4.3% |
| ma20_dist  |  -6.5% |
| ma50_dist  |  -8.3% |
| vol_20d    |  39.4% |
| mdd_60d    |  19.4% |
| rsi_14     |   40.4 |
| zscore_20d |   -2.0 |

### Tesla Inc. / TSLA (score 4.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -3.0% |
| ret_5d     | -20.2% |
| ret_20d    | -29.1% |
| ret_60d    | -23.7% |
| ma20_dist  | -20.2% |
| ma50_dist  | -24.4% |
| vol_20d    |  65.6% |
| mdd_60d    |  33.0% |
| rsi_14     |    9.1 |
| zscore_20d |   -1.9 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| FTSE 100 / ^FTSE                    | 106.5359 |           1.0% |                 0.89x |      213.0718 |            2.0% |
| Apple Inc. / AAPL                   |   7.8193 |           2.3% |                 0.37x |       15.6386 |            4.6% |
| Hang Seng / ^HSI                    | 453.4801 |           1.8% |                 0.54x |      906.9601 |            3.5% |
| DAX / ^GDAXI                        | 294.6020 |           1.2% |                 0.63x |      589.2040 |            2.3% |
| CAC 40 / ^FCHI                      |  94.0943 |           1.1% |                 0.74x |      188.1886 |            2.2% |
| JPMorgan Chase & Co. / JPM          |   7.9529 |           2.3% |                 0.43x |       15.9057 |            4.6% |
| Wheat / ZW=F                        |  23.6964 |           3.6% |                 0.27x |       47.3929 |            7.2% |
| Euro Stoxx 50 / ^STOXX50E           |  68.8314 |           1.1% |                 0.72x |      137.6628 |            2.2% |
| Brent Crude Oil / BZ=F              |   5.3400 |           5.9% |                 0.15x |       10.6800 |           11.8% |
| UnitedHealth Group Inc. / UNH       |  13.5221 |           3.2% |                 0.37x |       27.0443 |            6.4% |
| Corn / ZC=F                         |  10.8393 |           2.4% |                 0.37x |       21.6786 |            4.8% |
| Microsoft Corporation / MSFT        |  11.7479 |           3.0% |                 0.39x |       23.4957 |            6.0% |
| Dow Jones Industrial Average / ^DJI | 596.3323 |           1.2% |                 0.83x |     1192.6646 |            2.3% |
| Soybeans / ZS=F                     |  20.4286 |           1.7% |                 0.40x |       40.8571 |            3.5% |
| Gold / GC=F                         |  59.7000 |           1.5% |                 0.48x |      119.4000 |            3.0% |
| Russell 2000 / ^RUT                 |  35.5228 |           1.2% |                 0.83x |       71.0457 |            2.4% |
| S&P 500 / ^GSPC                     |  77.6085 |           1.1% |                 0.98x |      155.2171 |            2.1% |
| Alphabet Inc. Class A / GOOGL       |  11.9079 |           3.5% |                 0.26x |       23.8157 |            7.1% |
| Platinum / PL=F                     |  21.4500 |           1.3% |                 0.35x |       42.9000 |            2.7% |
| Meta Platforms Inc. / META          |  23.3057 |           4.0% |                 0.19x |       46.6114 |            8.0% |
| Silver / SI=F                       |   1.3917 |           2.4% |                 0.26x |        2.7834 |            4.8% |
| NASDAQ 100 / ^NDX                   | 562.2070 |           2.1% |                 0.51x |     1124.4141 |            4.1% |
| Natural Gas / NG=F                  |   0.1052 |           3.9% |                 0.29x |        0.2104 |            7.7% |
| Amazon.com Inc. / AMZN              |   6.4843 |           2.9% |                 0.41x |       12.9686 |            5.7% |
| NVIDIA Corporation / NVDA           |   7.8364 |           4.1% |                 0.25x |       15.6729 |            8.2% |
| Tesla Inc. / TSLA                   |  15.8929 |           5.3% |                 0.15x |       31.7857 |           10.7% |

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

Scoring engine version: **1.0.0** | Git commit: **cb0d3ec**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
