+++
title = "Market Analysis 2026-09-01"
date = "2026-09-01T00:00:00+00:00"
draft = false
summary = "Neutral market: 26 reliable instruments. Top signal: ZS=F (score 77.3)."
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
source_files = ["data/analysis/2026-09-01.json", "data/history/2026-09-01.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "4e96b44"
+++

## Market Regime

**Neutral** — 11 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Soybeans / ZS=F** — score 77.3, 20d return +10.2%, RSI14=86. 20d up +10.2%; above MA20 by 5.6%; RSI14=86
- **Corn / ZC=F** — score 76.1, 20d return +17.3%, RSI14=69. 20d up +17.3%; above MA20 by 7.8%; RSI14=69
- **Wheat / ZW=F** — score 73.0, 20d return +19.8%, RSI14=71. 20d up +19.8%; above MA20 by 10.5%; RSI14=71
- **Natural Gas / NG=F** — score 61.5, 20d return +11.2%, RSI14=68. 20d up +11.2%; above MA20 by 5.6%; RSI14=68
- **Microsoft Corporation / MSFT** — score 60.9, 20d return +4.2%, RSI14=53. 20d up +4.2%; above MA20 by 2.7%; RSI14=53

## Upcoming Events

_No scheduled events for covered instruments in the next 7 days._

## Signal History

Compared with the previous available report (**2026-08-31**).

- **New top-5:** NG=F
- **Persistent top signals:** ZC=F (14 reports), ZW=F (12 reports), ZS=F (7 reports), MSFT (3 reports)
- **Dropped from top-5:** ^GDAXI

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +0 |    +3.3 |
| 7203.T    |     +1 |    +6.4 |
| 8306.T    |     -1 |    +1.2 |
| AAPL      |     -1 |    -7.6 |
| AMZN      |     -8 |   -19.4 |
| BZ=F      |     +7 |   +11.2 |
| CL=F      |     +0 |   +16.7 |
| GC=F      |     -3 |    -5.2 |
| GOOGL     |     -1 |   -12.4 |
| HG=F      |     +0 |   +15.8 |
| JPM       |     -5 |    -8.8 |
| META      |     -7 |   -15.4 |
| MSFT      |     -2 |   -15.2 |
| NG=F      |     +7 |   +13.3 |
| NVDA      |    +11 |   +20.9 |
| PL=F      |    -12 |   -20.3 |
| SI=F      |     -2 |    -2.1 |
| TSLA      |    +16 |   +26.1 |
| UNH       |     +1 |    -5.8 |
| XOM       |     +3 |   +26.7 |
| ZC=F      |     +3 |    +7.3 |
| ZS=F      |     +1 |    -4.5 |
| ZW=F      |     -2 |    -9.7 |
| ^DJI      |     -5 |    -7.6 |
| ^FCHI     |     +1 |    -4.2 |
| ^FTSE     |     +1 |    +4.2 |
| ^GDAXI    |     -6 |   -17.0 |
| ^GSPC     |     +1 |    +0.0 |
| ^HSI      |     +6 |    +9.7 |
| ^N225     |     -3 |    -3.6 |
| ^NDX      |     +6 |    +8.2 |
| ^RUT      |     +3 |    +0.9 |
| ^STOXX50E |    -10 |   -13.0 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input
- **Copper / HG=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|    1 | Soybeans / ZS=F        |  77.3 |   Yes    | —               | 20d up +10.2%; above MA20 by 5.6%; RSI14=86  |
|    2 | Corn / ZC=F            |  76.1 |   Yes    | —               | 20d up +17.3%; above MA20 by 7.8%; RSI14=69  |
|    3 | Wheat / ZW=F           |  73.0 |   Yes    | —               | 20d up +19.8%; above MA20 by 10.5%; RSI14=71 |
|    4 | Natural Gas / NG=F     |  61.5 |   Yes    | —               | 20d up +11.2%; above MA20 by 5.6%; RSI14=68  |
|   11 | Brent Crude Oil / BZ=F |  50.0 |   Yes    | —               | 20d up +9.7%; above MA20 by 1.1%; RSI14=60   |
|   16 | Gold / GC=F            |  41.5 |   Yes    | —               | 20d up +4.5%; below MA20 by 1.1%; RSI14=54   |
|   18 | Silver / SI=F          |  39.4 |   Yes    | —               | 20d up +7.8%; below MA20 by 0.3%; RSI14=54   |
|   20 | Platinum / PL=F        |  35.8 |   Yes    | —               | 20d up +3.4%; below MA20 by 0.6%; RSI14=58   |
|   31 | WTI Crude Oil / CL=F   |  57.6 |    No    | malformed_input | Suppressed: malformed_input                  |
|   32 | Copper / HG=F          |  53.0 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    5 | Microsoft Corporation / MSFT                                                   |  60.9 |   Yes    | —                             | 20d up +4.2%; above MA20 by 2.7%; RSI14=53   |
|    6 | Tesla Inc. / TSLA                                                              |  59.4 |   Yes    | —                             | 20d up +14.2%; above MA20 by 7.9%; RSI14=65  |
|    7 | Apple Inc. / AAPL                                                              |  57.9 |   Yes    | —                             | 20d up +4.5%; above MA20 by 2.1%; RSI14=65   |
|    8 | NVIDIA Corporation / NVDA                                                      |  57.0 |   Yes    | —                             | 20d up +6.8%; above MA20 by 0.9%; RSI14=53   |
|   12 | JPMorgan Chase & Co. / JPM                                                     |  47.9 |   Yes    | —                             | 20d up +1.0%; below MA20 by 0.6%; RSI14=41   |
|   23 | Amazon.com Inc. / AMZN                                                         |  25.4 |   Yes    | —                             | 20d down -8.5%; below MA20 by 2.2%; RSI14=38 |
|   24 | Meta Platforms Inc. / META                                                     |  24.9 |   Yes    | —                             | 20d down -3.0%; below MA20 by 0.4%; RSI14=40 |
|   25 | UnitedHealth Group Inc. / UNH                                                  |  19.4 |   Yes    | —                             | 20d down -6.2%; below MA20 by 2.3%; RSI14=40 |
|   26 | Alphabet Inc. Class A / GOOGL                                                  |  13.9 |   Yes    | —                             | 20d down -9.1%; below MA20 by 2.6%; RSI14=44 |
|   27 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  70.6 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   28 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  68.5 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   29 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  67.6 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   30 | Exxon Mobil Corporation / XOM                                                  |  59.4 |    No    | malformed_input               | Suppressed: malformed_input                  |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    9 | FTSE 100 / ^FTSE                    |  54.9 |   Yes    | —            | 20d down -0.4%; above MA20 by 0.0%; RSI14=46 |
|   10 | DAX / ^GDAXI                        |  53.0 |   Yes    | —            | 20d up +1.0%; above MA20 by 0.0%; RSI14=46   |
|   13 | S&P 500 / ^GSPC                     |  46.7 |   Yes    | —            | 20d up +1.1%; below MA20 by 0.4%; RSI14=45   |
|   14 | Hang Seng / ^HSI                    |  45.8 |   Yes    | —            | 20d down -1.7%; below MA20 by 0.1%; RSI14=48 |
|   15 | NASDAQ 100 / ^NDX                   |  42.7 |   Yes    | —            | 20d up +2.4%; below MA20 by 0.3%; RSI14=49   |
|   17 | Dow Jones Industrial Average / ^DJI |  39.7 |   Yes    | —            | 20d up +0.0%; below MA20 by 0.8%; RSI14=39   |
|   19 | Euro Stoxx 50 / ^STOXX50E           |  39.4 |   Yes    | —            | 20d down -0.1%; below MA20 by 1.0%; RSI14=34 |
|   21 | Russell 2000 / ^RUT                 |  31.2 |   Yes    | —            | 20d down -0.9%; below MA20 by 2.1%; RSI14=37 |
|   22 | CAC 40 / ^FCHI                      |  29.1 |   Yes    | —            | 20d down -3.2%; below MA20 by 2.6%; RSI14=21 |
|   33 | Nikkei 225 / ^N225                  |  39.7 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-08-31 |
| 7203.T    | 2026-08-31 |
| 8306.T    | 2026-08-31 |
| AAPL      | 2026-08-31 |
| AMZN      | 2026-08-31 |
| BZ=F      | 2026-08-31 |
| CL=F      | 2026-08-31 |
| GC=F      | 2026-08-31 |
| GOOGL     | 2026-08-31 |
| HG=F      | 2026-08-31 |
| JPM       | 2026-08-31 |
| META      | 2026-08-31 |
| MSFT      | 2026-08-31 |
| NG=F      | 2026-08-31 |
| NVDA      | 2026-08-31 |
| PL=F      | 2026-08-31 |
| SI=F      | 2026-08-31 |
| TSLA      | 2026-08-31 |
| UNH       | 2026-08-31 |
| XOM       | 2026-08-31 |
| ZC=F      | 2026-08-31 |
| ZS=F      | 2026-08-31 |
| ZW=F      | 2026-08-31 |
| ^DJI      | 2026-08-31 |
| ^FCHI     | 2026-08-31 |
| ^FTSE     | 2026-08-28 |
| ^GDAXI    | 2026-08-31 |
| ^GSPC     | 2026-08-31 |
| ^HSI      | 2026-08-31 |
| ^N225     | 2026-08-31 |
| ^NDX      | 2026-08-31 |
| ^RUT      | 2026-08-31 |
| ^STOXX50E | 2026-08-31 |

## Symbol Details

### Soybeans / ZS=F (score 77.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.1% |
| ret_5d     |  +4.9% |
| ret_20d    | +10.2% |
| ret_60d    | +14.5% |
| ma20_dist  |  +5.6% |
| ma50_dist  |  +7.0% |
| vol_20d    |  17.7% |
| mdd_60d    |   8.1% |
| rsi_14     |   85.8 |
| zscore_20d |    1.7 |

### Corn / ZC=F (score 76.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.6% |
| ret_5d     |  +4.8% |
| ret_20d    | +17.3% |
| ret_60d    | +22.8% |
| ma20_dist  |  +7.8% |
| ma50_dist  | +13.2% |
| vol_20d    |  54.9% |
| mdd_60d    |   6.0% |
| rsi_14     |   69.0 |
| zscore_20d |    1.4 |

### Wheat / ZW=F (score 73.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.4% |
| ret_5d     | +11.0% |
| ret_20d    | +19.8% |
| ret_60d    | +29.3% |
| ma20_dist  | +10.5% |
| ma50_dist  | +15.2% |
| vol_20d    |  41.2% |
| mdd_60d    |  10.7% |
| rsi_14     |   71.4 |
| zscore_20d |    1.9 |

### Natural Gas / NG=F (score 61.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.6% |
| ret_5d     |  +5.5% |
| ret_20d    | +11.2% |
| ret_60d    |  -6.5% |
| ma20_dist  |  +5.6% |
| ma50_dist  |  +1.9% |
| vol_20d    |  28.0% |
| mdd_60d    |  21.0% |
| rsi_14     |   68.1 |
| zscore_20d |    2.2 |

### Microsoft Corporation / MSFT (score 60.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.2% |
| ret_5d     |  +4.1% |
| ret_20d    |  +4.2% |
| ret_60d    | +18.5% |
| ma20_dist  |  +2.7% |
| ma50_dist  | +17.2% |
| vol_20d    |  21.1% |
| mdd_60d    |  15.3% |
| rsi_14     |   52.9 |
| zscore_20d |    1.4 |

### Tesla Inc. / TSLA (score 59.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +5.5% |
| ret_5d     |  +5.4% |
| ret_20d    | +14.2% |
| ret_60d    | -12.1% |
| ma20_dist  |  +7.9% |
| ma50_dist  |  +2.3% |
| vol_20d    |  40.1% |
| mdd_60d    |  29.9% |
| rsi_14     |   65.0 |
| zscore_20d |    2.1 |

### Apple Inc. / AAPL (score 57.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.9% |
| ret_5d     | +2.1% |
| ret_20d    | +4.5% |
| ret_60d    | +1.8% |
| ma20_dist  | +2.1% |
| ma50_dist  | +1.5% |
| vol_20d    | 17.4% |
| mdd_60d    | 11.0% |
| rsi_14     |  65.1 |
| zscore_20d |   1.5 |

### NVIDIA Corporation / NVDA (score 57.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.5% |
| ret_5d     | +5.9% |
| ret_20d    | +6.8% |
| ret_60d    | +1.0% |
| ma20_dist  | +0.9% |
| ma50_dist  | +5.8% |
| vol_20d    | 45.1% |
| mdd_60d    | 10.6% |
| rsi_14     |  52.5 |
| zscore_20d |   0.4 |

### FTSE 100 / ^FTSE (score 54.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +0.1% |
| ret_20d    | -0.4% |
| ret_60d    | +4.4% |
| ma20_dist  | +0.0% |
| ma50_dist  | +1.2% |
| vol_20d    |  5.2% |
| mdd_60d    |  1.9% |
| rsi_14     |  45.6 |
| zscore_20d |   0.0 |

### DAX / ^GDAXI (score 53.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.2% |
| ret_5d     | +0.6% |
| ret_20d    | +1.0% |
| ret_60d    | +6.7% |
| ma20_dist  | +0.0% |
| ma50_dist  | +2.6% |
| vol_20d    |  8.2% |
| mdd_60d    |  4.1% |
| rsi_14     |  46.0 |
| zscore_20d |   0.0 |

### Brent Crude Oil / BZ=F (score 50.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.3% |
| ret_5d     | -1.8% |
| ret_20d    | +9.7% |
| ret_60d    | -1.0% |
| ma20_dist  | +1.1% |
| ma50_dist  | +6.0% |
| vol_20d    | 27.5% |
| mdd_60d    | 23.1% |
| rsi_14     |  59.9 |
| zscore_20d |   0.4 |

### JPMorgan Chase & Co. / JPM (score 47.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.4% |
| ret_5d     |  -0.1% |
| ret_20d    |  +1.0% |
| ret_60d    | +15.0% |
| ma20_dist  |  -0.6% |
| ma50_dist  |  +2.4% |
| vol_20d    |  13.3% |
| mdd_60d    |   3.7% |
| rsi_14     |   41.1 |
| zscore_20d |   -0.6 |

### S&P 500 / ^GSPC (score 46.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | +0.4% |
| ret_20d    | +1.1% |
| ret_60d    | +1.3% |
| ma20_dist  | -0.4% |
| ma50_dist  | +1.6% |
| vol_20d    |  9.3% |
| mdd_60d    |  3.4% |
| rsi_14     |  45.2 |
| zscore_20d |  -0.7 |

### Hang Seng / ^HSI (score 45.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | +0.2% |
| ret_20d    | -1.7% |
| ret_60d    | +1.2% |
| ma20_dist  | -0.1% |
| ma50_dist  | +2.9% |
| vol_20d    | 13.7% |
| mdd_60d    |  9.2% |
| rsi_14     |  48.0 |
| zscore_20d |  -0.2 |

### NASDAQ 100 / ^NDX (score 42.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | +1.5% |
| ret_20d    | +2.4% |
| ret_60d    | -3.1% |
| ma20_dist  | -0.3% |
| ma50_dist  | +0.7% |
| vol_20d    | 16.8% |
| mdd_60d    | 11.0% |
| rsi_14     |  48.7 |
| zscore_20d |  -0.3 |

### Gold / GC=F (score 41.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | -4.5% |
| ret_20d    | +4.5% |
| ret_60d    | +4.0% |
| ma20_dist  | -1.1% |
| ma50_dist  | +4.6% |
| vol_20d    | 22.7% |
| mdd_60d    |  8.6% |
| rsi_14     |  54.2 |
| zscore_20d |  -0.4 |

### Dow Jones Industrial Average / ^DJI (score 39.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | -0.4% |
| ret_20d    | +0.0% |
| ret_60d    | +3.1% |
| ma20_dist  | -0.8% |
| ma50_dist  | +0.7% |
| vol_20d    | 10.0% |
| mdd_60d    |  2.9% |
| rsi_14     |  39.3 |
| zscore_20d |  -1.3 |

### Silver / SI=F (score 39.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.2% |
| ret_5d     | -3.4% |
| ret_20d    | +7.8% |
| ret_60d    | +1.7% |
| ma20_dist  | -0.3% |
| ma50_dist  | +7.0% |
| vol_20d    | 30.3% |
| mdd_60d    | 20.9% |
| rsi_14     |  54.4 |
| zscore_20d |  -0.1 |

### Euro Stoxx 50 / ^STOXX50E (score 39.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | -0.4% |
| ret_20d    | -0.1% |
| ret_60d    | +5.9% |
| ma20_dist  | -1.0% |
| ma50_dist  | +0.8% |
| vol_20d    |  8.3% |
| mdd_60d    |  3.2% |
| rsi_14     |  33.7 |
| zscore_20d |  -1.5 |

### Platinum / PL=F (score 35.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -3.2% |
| ret_5d     | -4.9% |
| ret_20d    | +3.4% |
| ret_60d    | +4.7% |
| ma20_dist  | -0.6% |
| ma50_dist  | +5.5% |
| vol_20d    | 28.7% |
| mdd_60d    | 14.5% |
| rsi_14     |  57.7 |
| zscore_20d |  -0.2 |

### Russell 2000 / ^RUT (score 31.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | -1.3% |
| ret_20d    | -0.9% |
| ret_60d    | +0.7% |
| ma20_dist  | -2.1% |
| ma50_dist  | -1.2% |
| vol_20d    | 13.3% |
| mdd_60d    |  3.9% |
| rsi_14     |  37.4 |
| zscore_20d |  -2.3 |

### CAC 40 / ^FCHI (score 29.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | -1.4% |
| ret_20d    | -3.2% |
| ret_60d    | +1.6% |
| ma20_dist  | -2.6% |
| ma50_dist  | -1.5% |
| vol_20d    |  9.1% |
| mdd_60d    |  4.7% |
| rsi_14     |  20.8 |
| zscore_20d |  -1.7 |

### Amazon.com Inc. / AMZN (score 25.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.5% |
| ret_5d     | -0.9% |
| ret_20d    | -8.5% |
| ret_60d    | +2.4% |
| ma20_dist  | -2.2% |
| ma50_dist  | +3.1% |
| vol_20d    | 26.2% |
| mdd_60d    | 11.1% |
| rsi_14     |  38.1 |
| zscore_20d |  -0.9 |

### Meta Platforms Inc. / META (score 24.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | +2.4% |
| ret_20d    | -3.0% |
| ret_60d    | -8.7% |
| ma20_dist  | -0.4% |
| ma50_dist  | -3.3% |
| vol_20d    | 28.5% |
| mdd_60d    | 20.9% |
| rsi_14     |  40.3 |
| zscore_20d |  -0.1 |

### UnitedHealth Group Inc. / UNH (score 19.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.9% |
| ret_5d     | -2.3% |
| ret_20d    | -6.2% |
| ret_60d    | -1.2% |
| ma20_dist  | -2.3% |
| ma50_dist  | -5.6% |
| vol_20d    | 20.0% |
| mdd_60d    | 11.8% |
| rsi_14     |  39.6 |
| zscore_20d |  -1.3 |

### Alphabet Inc. Class A / GOOGL (score 13.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.1% |
| ret_5d     | -2.5% |
| ret_20d    | -9.1% |
| ret_60d    | -8.8% |
| ma20_dist  | -2.6% |
| ma50_dist  | -2.8% |
| vol_20d    | 24.0% |
| mdd_60d    | 14.9% |
| rsi_14     |  44.2 |
| zscore_20d |  -1.0 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Soybeans / ZS=F                     |  19.9286 |           1.6% |                 0.57x |       39.8571 |            3.1% |
| Corn / ZC=F                         |  16.7857 |           3.3% |                 0.18x |       33.5714 |            6.5% |
| Wheat / ZW=F                        |  26.1429 |           3.5% |                 0.24x |       52.2857 |            6.9% |
| Natural Gas / NG=F                  |   0.0941 |           3.2% |                 0.36x |        0.1883 |            6.4% |
| Microsoft Corporation / MSFT        |   9.7961 |           1.9% |                 0.47x |       19.5921 |            3.9% |
| Tesla Inc. / TSLA                   |  13.5079 |           3.7% |                 0.25x |       27.0157 |            7.3% |
| Apple Inc. / AAPL                   |   6.1271 |           1.9% |                 0.57x |       12.2543 |            3.9% |
| NVIDIA Corporation / NVDA           |   6.8107 |           3.1% |                 0.22x |       13.6214 |            6.2% |
| FTSE 100 / ^FTSE                    |  72.6643 |           0.7% |                 1.93x |      145.3285 |            1.3% |
| DAX / ^GDAXI                        | 210.6973 |           0.8% |                 1.22x |      421.3945 |            1.6% |
| Brent Crude Oil / BZ=F              |   2.7707 |           3.1% |                 0.36x |        5.5414 |            6.1% |
| JPMorgan Chase & Co. / JPM          |   5.1000 |           1.4% |                 0.75x |       10.2000 |            2.9% |
| S&P 500 / ^GSPC                     |  50.4700 |           0.7% |                 1.08x |      100.9399 |            1.3% |
| Hang Seng / ^HSI                    | 321.6028 |           1.3% |                 0.73x |      643.2056 |            2.5% |
| NASDAQ 100 / ^NDX                   | 333.6143 |           1.1% |                 0.59x |      667.2285 |            2.3% |
| Gold / GC=F                         |  82.3929 |           1.9% |                 0.44x |      164.7858 |            3.7% |
| Dow Jones Industrial Average / ^DJI | 359.7651 |           0.7% |                 1.00x |      719.5301 |            1.4% |
| Silver / SI=F                       |   1.8775 |           2.8% |                 0.33x |        3.7550 |            5.7% |
| Euro Stoxx 50 / ^STOXX50E           |  49.8707 |           0.8% |                 1.20x |       99.7414 |            1.6% |
| Platinum / PL=F                     |  34.4429 |           1.9% |                 0.35x |       68.8857 |            3.9% |
| Russell 2000 / ^RUT                 |  26.6964 |           0.9% |                 0.75x |       53.3929 |            1.8% |
| CAC 40 / ^FCHI                      |  70.6148 |           0.8% |                 1.10x |      141.2296 |            1.7% |
| Amazon.com Inc. / AMZN              |   5.9357 |           2.3% |                 0.38x |       11.8714 |            4.6% |
| Meta Platforms Inc. / META          |  18.0064 |           3.1% |                 0.35x |       36.0128 |            6.3% |
| UnitedHealth Group Inc. / UNH       |   7.6436 |           2.0% |                 0.50x |       15.2871 |            3.9% |
| Alphabet Inc. Class A / GOOGL       |   6.1564 |           1.8% |                 0.42x |       12.3129 |            3.6% |

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

Scoring engine version: **1.0.0** | Git commit: **4e96b44**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
