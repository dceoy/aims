+++
title = "Market Analysis 2026-08-31"
date = "2026-08-31T00:00:00+00:00"
draft = false
summary = "Neutral market: 26 reliable instruments. Top signal: ZW=F (score 82.7)."
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
source_files = ["data/analysis/2026-08-31.json", "data/history/2026-08-31.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "1ea3f8d"
+++

## Market Regime

**Neutral** — 14 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Wheat / ZW=F** — score 82.7, 20d return +19.4%, RSI14=75. 20d up +19.4%; above MA20 by 13.1%; RSI14=75
- **Soybeans / ZS=F** — score 81.8, 20d return +10.8%, RSI14=87. 20d up +10.8%; above MA20 by 6.2%; RSI14=87
- **Microsoft Corporation / MSFT** — score 76.1, 20d return +10.7%, RSI14=56. 20d up +10.7%; above MA20 by 4.2%; RSI14=56
- **DAX / ^GDAXI** — score 70.0, 20d return +3.7%, RSI14=59. 20d up +3.7%; above MA20 by 1.2%; RSI14=59
- **Corn / ZC=F** — score 68.8, 20d return +17.2%, RSI14=65. 20d up +17.2%; above MA20 by 8.0%; RSI14=65

## Upcoming Events

_No scheduled events for covered instruments in the next 7 days._

## Signal History

Compared with the previous available report (**2026-08-28**).

- **New top-5:** ^GDAXI
- **Persistent top signals:** ZC=F (13 reports), ZW=F (11 reports), ZS=F (6 reports), MSFT (2 reports)
- **Dropped from top-5:** NVDA

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +1 |   +10.3 |
| 7203.T    |     +0 |    +9.4 |
| 8306.T    |     -1 |    +8.8 |
| AAPL      |    +12 |   +23.0 |
| AMZN      |    +10 |   +23.3 |
| BZ=F      |     -1 |    -6.4 |
| CL=F      |     +0 |    -0.3 |
| GC=F      |     -7 |   -19.1 |
| GOOGL     |     +1 |    +8.8 |
| HG=F      |     -2 |    -7.3 |
| JPM       |     +9 |   +11.2 |
| META      |     +6 |   +13.0 |
| MSFT      |     +1 |    +5.2 |
| NG=F      |     -2 |    -9.1 |
| NVDA      |    -14 |   -32.1 |
| PL=F      |     +2 |    +1.2 |
| SI=F      |     -9 |   -21.8 |
| TSLA      |    -10 |   -19.4 |
| UNH       |     -4 |    -3.0 |
| XOM       |     +0 |    -3.6 |
| ZC=F      |     -2 |    -4.8 |
| ZS=F      |     +0 |    +7.0 |
| ZW=F      |     +0 |    +1.2 |
| ^DJI      |     +1 |    -4.2 |
| ^FCHI     |     +1 |    +9.1 |
| ^FTSE     |     +9 |    +9.7 |
| ^GDAXI    |     +4 |    +7.6 |
| ^GSPC     |     -3 |    -7.9 |
| ^HSI      |     +1 |    +2.1 |
| ^N225     |     +2 |    +6.4 |
| ^NDX      |     -7 |   -14.5 |
| ^RUT      |     -9 |   -16.4 |
| ^STOXX50E |    +11 |   +12.7 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Nikkei 225 / ^N225** — missing_bars
- **WTI Crude Oil / CL=F** — malformed_input
- **Copper / HG=F** — malformed_input
- **Exxon Mobil Corporation / XOM** — malformed_input

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|    1 | Wheat / ZW=F           |  82.7 |   Yes    | —               | 20d up +19.4%; above MA20 by 13.1%; RSI14=75 |
|    2 | Soybeans / ZS=F        |  81.8 |   Yes    | —               | 20d up +10.8%; above MA20 by 6.2%; RSI14=87  |
|    5 | Corn / ZC=F            |  68.8 |   Yes    | —               | 20d up +17.2%; above MA20 by 8.0%; RSI14=65  |
|    8 | Platinum / PL=F        |  56.1 |   Yes    | —               | 20d up +6.3%; above MA20 by 2.9%; RSI14=61   |
|   11 | Natural Gas / NG=F     |  48.2 |   Yes    | —               | 20d up +7.4%; above MA20 by 4.5%; RSI14=57   |
|   13 | Gold / GC=F            |  46.7 |   Yes    | —               | 20d up +5.5%; above MA20 by 0.2%; RSI14=54   |
|   16 | Silver / SI=F          |  41.5 |   Yes    | —               | 20d up +7.9%; above MA20 by 1.2%; RSI14=55   |
|   18 | Brent Crude Oil / BZ=F |  38.8 |   Yes    | —               | 20d up +12.4%; above MA20 by 0.2%; RSI14=51  |
|   31 | WTI Crude Oil / CL=F   |  40.9 |    No    | malformed_input | Suppressed: malformed_input                  |
|   32 | Copper / HG=F          |  37.3 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    3 | Microsoft Corporation / MSFT                                                   |  76.1 |   Yes    | —                             | 20d up +10.7%; above MA20 by 4.2%; RSI14=56  |
|    6 | Apple Inc. / AAPL                                                              |  65.5 |   Yes    | —                             | 20d up +3.6%; above MA20 by 3.2%; RSI14=64   |
|    7 | JPMorgan Chase & Co. / JPM                                                     |  56.7 |   Yes    | —                             | 20d up +1.7%; below MA20 by 0.1%; RSI14=47   |
|   15 | Amazon.com Inc. / AMZN                                                         |  44.9 |   Yes    | —                             | 20d down -1.9%; below MA20 by 0.2%; RSI14=39 |
|   17 | Meta Platforms Inc. / META                                                     |  40.3 |   Yes    | —                             | 20d up +3.8%; above MA20 by 0.4%; RSI14=44   |
|   19 | NVIDIA Corporation / NVDA                                                      |  36.1 |   Yes    | —                             | 20d up +8.4%; below MA20 by 0.2%; RSI14=50   |
|   22 | Tesla Inc. / TSLA                                                              |  33.3 |   Yes    | —                             | 20d up +12.1%; above MA20 by 2.9%; RSI14=59  |
|   25 | Alphabet Inc. Class A / GOOGL                                                  |  26.4 |   Yes    | —                             | 20d down -2.7%; below MA20 by 1.1%; RSI14=38 |
|   26 | UnitedHealth Group Inc. / UNH                                                  |  25.1 |   Yes    | —                             | 20d down -5.2%; below MA20 by 1.8%; RSI14=38 |
|   27 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  67.3 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   28 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  66.4 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   29 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  62.1 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   33 | Exxon Mobil Corporation / XOM                                                  |  32.7 |    No    | malformed_input               | Suppressed: malformed_input                  |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    4 | DAX / ^GDAXI                        |  70.0 |   Yes    | —            | 20d up +3.7%; above MA20 by 1.2%; RSI14=59   |
|    9 | Euro Stoxx 50 / ^STOXX50E           |  52.4 |   Yes    | —            | 20d up +2.0%; below MA20 by 0.0%; RSI14=43   |
|   10 | FTSE 100 / ^FTSE                    |  50.6 |   Yes    | —            | 20d down -0.4%; above MA20 by 0.0%; RSI14=46 |
|   12 | Dow Jones Industrial Average / ^DJI |  47.3 |   Yes    | —            | 20d up +2.0%; below MA20 by 0.1%; RSI14=42   |
|   14 | S&P 500 / ^GSPC                     |  46.7 |   Yes    | —            | 20d up +3.0%; below MA20 by 0.0%; RSI14=45   |
|   20 | Hang Seng / ^HSI                    |  36.1 |   Yes    | —            | 20d down -1.2%; below MA20 by 0.2%; RSI14=43 |
|   21 | NASDAQ 100 / ^NDX                   |  34.5 |   Yes    | —            | 20d up +4.1%; below MA20 by 0.2%; RSI14=47   |
|   23 | CAC 40 / ^FCHI                      |  33.3 |   Yes    | —            | 20d down -1.3%; below MA20 by 2.0%; RSI14=23 |
|   24 | Russell 2000 / ^RUT                 |  30.3 |   Yes    | —            | 20d up +1.4%; below MA20 by 1.6%; RSI14=42   |
|   30 | Nikkei 225 / ^N225                  |  43.3 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-08-28 |
| 7203.T    | 2026-08-28 |
| 8306.T    | 2026-08-28 |
| AAPL      | 2026-08-28 |
| AMZN      | 2026-08-28 |
| BZ=F      | 2026-08-28 |
| CL=F      | 2026-08-28 |
| GC=F      | 2026-08-28 |
| GOOGL     | 2026-08-28 |
| HG=F      | 2026-08-28 |
| JPM       | 2026-08-28 |
| META      | 2026-08-28 |
| MSFT      | 2026-08-28 |
| NG=F      | 2026-08-28 |
| NVDA      | 2026-08-28 |
| PL=F      | 2026-08-28 |
| SI=F      | 2026-08-28 |
| TSLA      | 2026-08-28 |
| UNH       | 2026-08-28 |
| XOM       | 2026-08-28 |
| ZC=F      | 2026-08-28 |
| ZS=F      | 2026-08-28 |
| ZW=F      | 2026-08-28 |
| ^DJI      | 2026-08-28 |
| ^FCHI     | 2026-08-28 |
| ^FTSE     | 2026-08-28 |
| ^GDAXI    | 2026-08-28 |
| ^GSPC     | 2026-08-28 |
| ^HSI      | 2026-08-28 |
| ^N225     | 2026-08-28 |
| ^NDX      | 2026-08-28 |
| ^RUT      | 2026-08-28 |
| ^STOXX50E | 2026-08-28 |

## Symbol Details

### Wheat / ZW=F (score 82.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +3.3% |
| ret_5d     |  +7.6% |
| ret_20d    | +19.4% |
| ret_60d    | +31.5% |
| ma20_dist  | +13.1% |
| ma50_dist  | +17.4% |
| vol_20d    |  41.4% |
| mdd_60d    |  10.7% |
| rsi_14     |   74.6 |
| zscore_20d |    2.5 |

### Soybeans / ZS=F (score 81.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.6% |
| ret_5d     |  +3.4% |
| ret_20d    | +10.8% |
| ret_60d    | +14.4% |
| ma20_dist  |  +6.2% |
| ma50_dist  |  +7.4% |
| vol_20d    |  17.5% |
| mdd_60d    |   8.1% |
| rsi_14     |   86.7 |
| zscore_20d |    2.0 |

### Microsoft Corporation / MSFT (score 76.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.7% |
| ret_5d     |  +6.3% |
| ret_20d    | +10.7% |
| ret_60d    | +20.2% |
| ma20_dist  |  +4.2% |
| ma50_dist  | +19.4% |
| vol_20d    |  26.0% |
| mdd_60d    |  17.6% |
| rsi_14     |   55.8 |
| zscore_20d |    2.3 |

### DAX / ^GDAXI (score 70.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.8% |
| ret_5d     | +1.7% |
| ret_20d    | +3.7% |
| ret_60d    | +7.3% |
| ma20_dist  | +1.2% |
| ma50_dist  | +3.9% |
| vol_20d    |  8.3% |
| mdd_60d    |  4.1% |
| rsi_14     |  58.8 |
| zscore_20d |   2.2 |

### Corn / ZC=F (score 68.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.3% |
| ret_5d     |  -1.7% |
| ret_20d    | +17.2% |
| ret_60d    | +22.3% |
| ma20_dist  |  +8.0% |
| ma50_dist  | +13.1% |
| vol_20d    |  54.9% |
| mdd_60d    |   6.0% |
| rsi_14     |   65.1 |
| zscore_20d |    1.4 |

### Apple Inc. / AAPL (score 65.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.6% |
| ret_5d     | +3.3% |
| ret_20d    | +3.6% |
| ret_60d    | +3.0% |
| ma20_dist  | +3.2% |
| ma50_dist  | +2.5% |
| vol_20d    | 18.4% |
| mdd_60d    | 11.6% |
| rsi_14     |  64.3 |
| zscore_20d |   2.3 |

### JPMorgan Chase & Co. / JPM (score 56.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.0% |
| ret_5d     |  +1.7% |
| ret_20d    |  +1.7% |
| ret_60d    | +19.4% |
| ma20_dist  |  -0.1% |
| ma50_dist  |  +3.1% |
| vol_20d    |  13.2% |
| mdd_60d    |   3.7% |
| rsi_14     |   46.9 |
| zscore_20d |   -0.1 |

### Platinum / PL=F (score 56.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | -2.4% |
| ret_20d    | +6.3% |
| ret_60d    | +5.6% |
| ma20_dist  | +2.9% |
| ma50_dist  | +9.3% |
| vol_20d    | 26.1% |
| mdd_60d    | 14.5% |
| rsi_14     |  61.2 |
| zscore_20d |   0.9 |

### Euro Stoxx 50 / ^STOXX50E (score 52.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | +0.4% |
| ret_20d    | +2.0% |
| ret_60d    | +7.0% |
| ma20_dist  | -0.0% |
| ma50_dist  | +1.9% |
| vol_20d    |  8.3% |
| mdd_60d    |  3.2% |
| rsi_14     |  42.9 |
| zscore_20d |  -0.0 |

### FTSE 100 / ^FTSE (score 50.6)

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

### Natural Gas / NG=F (score 48.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | +4.3% |
| ret_20d    | +7.4% |
| ret_60d    | -8.2% |
| ma20_dist  | +4.5% |
| ma50_dist  | +0.0% |
| vol_20d    | 28.8% |
| mdd_60d    | 21.0% |
| rsi_14     |  57.0 |
| zscore_20d |   1.8 |

### Dow Jones Industrial Average / ^DJI (score 47.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.0% |
| ret_5d     | +0.5% |
| ret_20d    | +2.0% |
| ret_60d    | +5.7% |
| ma20_dist  | -0.1% |
| ma50_dist  | +1.4% |
| vol_20d    | 10.6% |
| mdd_60d    |  3.2% |
| rsi_14     |  42.1 |
| zscore_20d |  -0.2 |

### Gold / GC=F (score 46.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.9% |
| ret_5d     | -4.9% |
| ret_20d    | +5.5% |
| ret_60d    | +3.3% |
| ma20_dist  | +0.2% |
| ma50_dist  | +5.9% |
| vol_20d    | 22.2% |
| mdd_60d    |  8.6% |
| rsi_14     |  54.3 |
| zscore_20d |   0.1 |

### S&P 500 / ^GSPC (score 46.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | +0.5% |
| ret_20d    | +3.0% |
| ret_60d    | +2.1% |
| ma20_dist  | -0.0% |
| ma50_dist  | +2.0% |
| vol_20d    | 10.4% |
| mdd_60d    |  4.2% |
| rsi_14     |  45.3 |
| zscore_20d |  -0.0 |

### Amazon.com Inc. / AMZN (score 44.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +4.0% |
| ret_5d     | +3.0% |
| ret_20d    | -1.9% |
| ret_60d    | +6.6% |
| ma20_dist  | -0.2% |
| ma50_dist  | +5.9% |
| vol_20d    | 30.3% |
| mdd_60d    | 11.1% |
| rsi_14     |  38.7 |
| zscore_20d |  -0.1 |

### Silver / SI=F (score 41.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -3.5% |
| ret_5d     | -3.2% |
| ret_20d    | +7.9% |
| ret_60d    | -2.1% |
| ma20_dist  | +1.2% |
| ma50_dist  | +8.5% |
| vol_20d    | 30.3% |
| mdd_60d    | 20.9% |
| rsi_14     |  54.7 |
| zscore_20d |   0.4 |

### Meta Platforms Inc. / META (score 40.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.2% |
| ret_5d     | +5.1% |
| ret_20d    | +3.8% |
| ret_60d    | -7.1% |
| ma20_dist  | +0.4% |
| ma50_dist  | -2.4% |
| vol_20d    | 35.4% |
| mdd_60d    | 20.9% |
| rsi_14     |  43.8 |
| zscore_20d |   0.1 |

### Brent Crude Oil / BZ=F (score 38.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.4% |
| ret_5d     |  -3.6% |
| ret_20d    | +12.4% |
| ret_60d    |  -5.2% |
| ma20_dist  |  +0.2% |
| ma50_dist  |  +5.0% |
| vol_20d    |  29.8% |
| mdd_60d    |  23.1% |
| rsi_14     |   50.9 |
| zscore_20d |    0.1 |

### NVIDIA Corporation / NVDA (score 36.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -4.6% |
| ret_5d     | +1.3% |
| ret_20d    | +8.4% |
| ret_60d    | +1.3% |
| ma20_dist  | -0.2% |
| ma50_dist  | +4.4% |
| vol_20d    | 45.8% |
| mdd_60d    | 13.1% |
| rsi_14     |  50.0 |
| zscore_20d |  -0.1 |

### Hang Seng / ^HSI (score 36.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | -1.6% |
| ret_20d    | -1.2% |
| ret_60d    | -0.2% |
| ma20_dist  | -0.2% |
| ma50_dist  | +3.1% |
| vol_20d    | 13.9% |
| mdd_60d    | 10.2% |
| rsi_14     |  42.8 |
| zscore_20d |  -0.2 |

### NASDAQ 100 / ^NDX (score 34.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | +0.4% |
| ret_20d    | +4.1% |
| ret_60d    | -3.7% |
| ma20_dist  | -0.2% |
| ma50_dist  | +0.6% |
| vol_20d    | 17.8% |
| mdd_60d    | 11.0% |
| rsi_14     |  46.6 |
| zscore_20d |  -0.2 |

### Tesla Inc. / TSLA (score 33.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.7% |
| ret_5d     |  -3.9% |
| ret_20d    | +12.1% |
| ret_60d    | -17.7% |
| ma20_dist  |  +2.9% |
| ma50_dist  |  -3.3% |
| vol_20d    |  37.6% |
| mdd_60d    |  29.9% |
| rsi_14     |   58.9 |
| zscore_20d |    0.8 |

### CAC 40 / ^FCHI (score 33.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.0% |
| ret_5d     | -1.0% |
| ret_20d    | -1.3% |
| ret_60d    | +2.2% |
| ma20_dist  | -2.0% |
| ma50_dist  | -0.7% |
| vol_20d    | 10.0% |
| mdd_60d    |  4.7% |
| rsi_14     |  22.8 |
| zscore_20d |  -1.4 |

### Russell 2000 / ^RUT (score 30.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.4% |
| ret_5d     | -1.5% |
| ret_20d    | +1.4% |
| ret_60d    | +2.7% |
| ma20_dist  | -1.6% |
| ma50_dist  | -0.7% |
| vol_20d    | 14.5% |
| mdd_60d    |  3.9% |
| rsi_14     |  41.8 |
| zscore_20d |  -1.9 |

### Alphabet Inc. Class A / GOOGL (score 26.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.7% |
| ret_5d     | +0.5% |
| ret_20d    | -2.7% |
| ret_60d    | -3.4% |
| ma20_dist  | -1.1% |
| ma50_dist  | -0.9% |
| vol_20d    | 29.5% |
| mdd_60d    | 14.9% |
| rsi_14     |  37.8 |
| zscore_20d |  -0.4 |

### UnitedHealth Group Inc. / UNH (score 25.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | +0.7% |
| ret_20d    | -5.2% |
| ret_60d    | +4.8% |
| ma20_dist  | -1.8% |
| ma50_dist  | -4.8% |
| vol_20d    | 19.9% |
| mdd_60d    | 11.8% |
| rsi_14     |  37.8 |
| zscore_20d |  -0.9 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Wheat / ZW=F                        |  25.6964 |           3.4% |                 0.24x |       51.3929 |            6.7% |
| Soybeans / ZS=F                     |  19.2857 |           1.5% |                 0.57x |       38.5714 |            3.0% |
| Microsoft Corporation / MSFT        |   9.7502 |           1.9% |                 0.38x |       19.5004 |            3.8% |
| DAX / ^GDAXI                        | 206.3093 |           0.8% |                 1.21x |      412.6186 |            1.6% |
| Corn / ZC=F                         |  16.8929 |           3.3% |                 0.18x |       33.7857 |            6.6% |
| Apple Inc. / AAPL                   |   6.0371 |           1.9% |                 0.54x |       12.0743 |            3.8% |
| JPMorgan Chase & Co. / JPM          |   5.2086 |           1.5% |                 0.76x |       10.4171 |            2.9% |
| Platinum / PL=F                     |  32.7786 |           1.8% |                 0.38x |       65.5572 |            3.5% |
| Euro Stoxx 50 / ^STOXX50E           |  48.5271 |           0.7% |                 1.21x |       97.0542 |            1.5% |
| FTSE 100 / ^FTSE                    |  72.6643 |           0.7% |                 1.93x |      145.3285 |            1.3% |
| Natural Gas / NG=F                  |   0.0927 |           3.2% |                 0.35x |        0.1854 |            6.4% |
| Dow Jones Industrial Average / ^DJI | 362.6261 |           0.7% |                 0.94x |      725.2522 |            1.4% |
| Gold / GC=F                         |  84.3786 |           1.9% |                 0.45x |      168.7572 |            3.8% |
| S&P 500 / ^GSPC                     |  50.7243 |           0.7% |                 0.97x |      101.4485 |            1.3% |
| Amazon.com Inc. / AMZN              |   5.8050 |           2.2% |                 0.33x |       11.6100 |            4.4% |
| Silver / SI=F                       |   1.8375 |           2.7% |                 0.33x |        3.6750 |            5.5% |
| Meta Platforms Inc. / META          |  18.6843 |           3.2% |                 0.28x |       37.3686 |            6.5% |
| Brent Crude Oil / BZ=F              |   2.8193 |           3.2% |                 0.34x |        5.6386 |            6.3% |
| NVIDIA Corporation / NVDA           |   6.8757 |           3.2% |                 0.22x |       13.7514 |            6.3% |
| Hang Seng / ^HSI                    | 330.0714 |           1.3% |                 0.72x |      660.1429 |            2.6% |
| NASDAQ 100 / ^NDX                   | 340.6701 |           1.2% |                 0.56x |      681.3401 |            2.3% |
| Tesla Inc. / TSLA                   |  12.4293 |           3.6% |                 0.27x |       24.8586 |            7.1% |
| CAC 40 / ^FCHI                      |  67.6155 |           0.8% |                 1.00x |      135.2310 |            1.6% |
| Russell 2000 / ^RUT                 |  26.0293 |           0.9% |                 0.69x |       52.0586 |            1.8% |
| Alphabet Inc. Class A / GOOGL       |   6.4921 |           1.9% |                 0.34x |       12.9843 |            3.7% |
| UnitedHealth Group Inc. / UNH       |   7.8436 |           2.0% |                 0.50x |       15.6871 |            4.0% |

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

Scoring engine version: **1.0.0** | Git commit: **1ea3f8d**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
