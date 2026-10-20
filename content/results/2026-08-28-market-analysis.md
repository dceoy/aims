+++
title = "Market Analysis 2026-08-28"
date = "2026-08-28T00:00:00+00:00"
draft = false
summary = "Neutral market: 26 reliable instruments. Top signal: ZW=F (score 81.5)."
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
source_files = ["data/analysis/2026-08-28.json", "data/history/2026-08-28.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "0c1b5b7"
+++

## Market Regime

**Neutral** — 15 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Wheat / ZW=F** — score 81.5, 20d return +16.3%, RSI14=74. 20d up +16.3%; above MA20 by 10.5%; RSI14=74
- **Soybeans / ZS=F** — score 74.8, 20d return +8.8%, RSI14=86. 20d up +8.8%; above MA20 by 5.1%; RSI14=86
- **Corn / ZC=F** — score 73.6, 20d return +15.4%, RSI14=68. 20d up +15.4%; above MA20 by 8.5%; RSI14=68
- **Microsoft Corporation / MSFT** — score 70.9, 20d return +12.2%, RSI14=54. 20d up +12.2%; above MA20 by 3.0%; RSI14=54
- **NVIDIA Corporation / NVDA** — score 68.2, 20d return +16.9%, RSI14=54. 20d up +16.9%; above MA20 by 5.0%; RSI14=54

## Upcoming Events

_No scheduled events for covered instruments in the next 7 days._

## Signal History

Compared with the previous available report (**2026-08-27**).

- **New top-5:** MSFT, NVDA
- **Persistent top signals:** ZC=F (12 reports), ZW=F (10 reports), ZS=F (5 reports)
- **Dropped from top-5:** GC=F, ^GDAXI

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     -1 |   -13.6 |
| 7203.T    |     +0 |    -3.3 |
| 8306.T    |     +1 |    +0.6 |
| AAPL      |     -2 |    -0.9 |
| AMZN      |     -1 |    -8.5 |
| BZ=F      |     +6 |   +14.5 |
| CL=F      |     +2 |   +10.3 |
| GC=F      |     -2 |    -1.8 |
| GOOGL     |     +0 |    +3.9 |
| HG=F      |     +1 |    +0.6 |
| JPM       |     -4 |    -5.5 |
| META      |     -2 |    -8.5 |
| MSFT      |     +2 |   +10.0 |
| NG=F      |     +2 |    +6.1 |
| NVDA      |    +20 |   +46.4 |
| PL=F      |     -1 |    +1.5 |
| SI=F      |     +1 |    +8.2 |
| TSLA      |     +8 |   +14.8 |
| UNH       |     -4 |   -12.7 |
| XOM       |     -1 |    -5.5 |
| ZC=F      |     -2 |    -9.1 |
| ZS=F      |     +0 |    -7.0 |
| ZW=F      |     +2 |    +0.3 |
| ^DJI      |     +1 |    +3.0 |
| ^FCHI     |     -5 |   -13.9 |
| ^FTSE     |    -12 |   -18.2 |
| ^GDAXI    |     -3 |    -0.3 |
| ^GSPC     |     +4 |    +9.4 |
| ^HSI      |     -8 |   -15.4 |
| ^N225     |     -2 |    -9.4 |
| ^NDX      |     +8 |   +13.9 |
| ^RUT      |     +2 |    +3.3 |
| ^STOXX50E |    -10 |   -13.3 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|    1 | Wheat / ZW=F           |  81.5 |   Yes    | —               | 20d up +16.3%; above MA20 by 10.5%; RSI14=74 |
|    2 | Soybeans / ZS=F        |  74.8 |   Yes    | —               | 20d up +8.8%; above MA20 by 5.1%; RSI14=86   |
|    3 | Corn / ZC=F            |  73.6 |   Yes    | —               | 20d up +15.4%; above MA20 by 8.5%; RSI14=68  |
|    6 | Gold / GC=F            |  65.8 |   Yes    | —               | 20d up +12.6%; above MA20 by 3.4%; RSI14=66  |
|    7 | Silver / SI=F          |  63.3 |   Yes    | —               | 20d up +15.6%; above MA20 by 5.3%; RSI14=67  |
|    9 | Natural Gas / NG=F     |  57.3 |   Yes    | —               | 20d up +8.4%; above MA20 by 5.6%; RSI14=61   |
|   10 | Platinum / PL=F        |  54.9 |   Yes    | —               | 20d up +5.6%; above MA20 by 3.1%; RSI14=62   |
|   17 | Brent Crude Oil / BZ=F |  45.1 |   Yes    | —               | 20d up +13.0%; above MA20 by 1.2%; RSI14=52  |
|   30 | Copper / HG=F          |  44.5 |    No    | malformed_input | Suppressed: malformed_input                  |
|   31 | WTI Crude Oil / CL=F   |  41.2 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    4 | Microsoft Corporation / MSFT                                                   |  70.9 |   Yes    | —                             | 20d up +12.2%; above MA20 by 3.0%; RSI14=54  |
|    5 | NVIDIA Corporation / NVDA                                                      |  68.2 |   Yes    | —                             | 20d up +16.9%; above MA20 by 5.0%; RSI14=54  |
|   12 | Tesla Inc. / TSLA                                                              |  52.7 |   Yes    | —                             | 20d up +14.9%; above MA20 by 5.3%; RSI14=64  |
|   16 | JPMorgan Chase & Co. / JPM                                                     |  45.5 |   Yes    | —                             | 20d up +1.0%; below MA20 by 1.0%; RSI14=45   |
|   18 | Apple Inc. / AAPL                                                              |  42.4 |   Yes    | —                             | 20d down -5.6%; above MA20 by 1.7%; RSI14=52 |
|   22 | UnitedHealth Group Inc. / UNH                                                  |  28.2 |   Yes    | —                             | 20d down -6.3%; below MA20 by 1.5%; RSI14=41 |
|   23 | Meta Platforms Inc. / META                                                     |  27.3 |   Yes    | —                             | 20d up +5.9%; below MA20 by 0.6%; RSI14=42   |
|   25 | Amazon.com Inc. / AMZN                                                         |  21.5 |   Yes    | —                             | 20d up +8.8%; below MA20 by 4.1%; RSI14=30   |
|   26 | Alphabet Inc. Class A / GOOGL                                                  |  17.6 |   Yes    | —                             | 20d up +2.1%; below MA20 by 2.9%; RSI14=34   |
|   27 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  57.6 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   28 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  57.0 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   29 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  52.7 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   33 | Exxon Mobil Corporation / XOM                                                  |  36.4 |    No    | malformed_input               | Suppressed: malformed_input                  |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    8 | DAX / ^GDAXI                        |  62.4 |   Yes    | —            | 20d up +2.9%; above MA20 by 0.7%; RSI14=52   |
|   11 | S&P 500 / ^GSPC                     |  54.5 |   Yes    | —            | 20d up +3.9%; above MA20 by 0.4%; RSI14=47   |
|   13 | Dow Jones Industrial Average / ^DJI |  51.5 |   Yes    | —            | 20d up +2.6%; below MA20 by 0.0%; RSI14=41   |
|   14 | NASDAQ 100 / ^NDX                   |  49.1 |   Yes    | —            | 20d up +5.5%; above MA20 by 0.7%; RSI14=48   |
|   15 | Russell 2000 / ^RUT                 |  46.7 |   Yes    | —            | 20d up +2.3%; below MA20 by 0.1%; RSI14=46   |
|   19 | FTSE 100 / ^FTSE                    |  40.9 |   Yes    | —            | 20d down -1.0%; below MA20 by 0.3%; RSI14=38 |
|   20 | Euro Stoxx 50 / ^STOXX50E           |  39.7 |   Yes    | —            | 20d up +1.3%; below MA20 by 0.9%; RSI14=34   |
|   21 | Hang Seng / ^HSI                    |  33.9 |   Yes    | —            | 20d down -1.1%; below MA20 by 0.3%; RSI14=48 |
|   24 | CAC 40 / ^FCHI                      |  24.2 |   Yes    | —            | 20d down -2.0%; below MA20 by 3.0%; RSI14=12 |
|   32 | Nikkei 225 / ^N225                  |  37.0 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-08-27 |
| 7203.T    | 2026-08-27 |
| 8306.T    | 2026-08-27 |
| AAPL      | 2026-08-27 |
| AMZN      | 2026-08-27 |
| BZ=F      | 2026-08-27 |
| CL=F      | 2026-08-27 |
| GC=F      | 2026-08-27 |
| GOOGL     | 2026-08-27 |
| HG=F      | 2026-08-27 |
| JPM       | 2026-08-27 |
| META      | 2026-08-27 |
| MSFT      | 2026-08-27 |
| NG=F      | 2026-08-27 |
| NVDA      | 2026-08-27 |
| PL=F      | 2026-08-27 |
| SI=F      | 2026-08-27 |
| TSLA      | 2026-08-27 |
| UNH       | 2026-08-27 |
| XOM       | 2026-08-27 |
| ZC=F      | 2026-08-27 |
| ZS=F      | 2026-08-27 |
| ZW=F      | 2026-08-27 |
| ^DJI      | 2026-08-27 |
| ^FCHI     | 2026-08-27 |
| ^FTSE     | 2026-08-27 |
| ^GDAXI    | 2026-08-27 |
| ^GSPC     | 2026-08-27 |
| ^HSI      | 2026-08-27 |
| ^N225     | 2026-08-27 |
| ^NDX      | 2026-08-27 |
| ^RUT      | 2026-08-27 |
| ^STOXX50E | 2026-08-27 |

## Symbol Details

### Wheat / ZW=F (score 81.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.7% |
| ret_5d     |  +9.0% |
| ret_20d    | +16.3% |
| ret_60d    | +28.1% |
| ma20_dist  | +10.5% |
| ma50_dist  | +14.4% |
| vol_20d    |  40.6% |
| mdd_60d    |  10.7% |
| rsi_14     |   74.4 |
| zscore_20d |    2.3 |

### Soybeans / ZS=F (score 74.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.2% |
| ret_5d     |  +2.6% |
| ret_20d    |  +8.8% |
| ret_60d    | +12.0% |
| ma20_dist  |  +5.1% |
| ma50_dist  |  +6.0% |
| vol_20d    |  17.3% |
| mdd_60d    |   8.1% |
| rsi_14     |   86.5 |
| zscore_20d |    1.8 |

### Corn / ZC=F (score 73.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.7% |
| ret_5d     |  +5.5% |
| ret_20d    | +15.4% |
| ret_60d    | +22.2% |
| ma20_dist  |  +8.5% |
| ma50_dist  | +13.3% |
| vol_20d    |  55.4% |
| mdd_60d    |   6.0% |
| rsi_14     |   68.3 |
| zscore_20d |    1.5 |

### Microsoft Corporation / MSFT (score 70.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.8% |
| ret_5d     |  +5.0% |
| ret_20d    | +12.2% |
| ret_60d    | +14.4% |
| ma20_dist  |  +3.0% |
| ma50_dist  | +18.1% |
| vol_20d    |  27.1% |
| mdd_60d    |  17.6% |
| rsi_14     |   54.2 |
| zscore_20d |    1.5 |

### NVIDIA Corporation / NVDA (score 68.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +8.7% |
| ret_5d     |  +5.1% |
| ret_20d    | +16.9% |
| ret_60d    |  +2.3% |
| ma20_dist  |  +5.0% |
| ma50_dist  |  +9.5% |
| vol_20d    |  42.7% |
| mdd_60d    |  13.1% |
| rsi_14     |   53.5 |
| zscore_20d |    1.5 |

### Gold / GC=F (score 65.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.3% |
| ret_5d     |  -0.3% |
| ret_20d    | +12.6% |
| ret_60d    |  +6.3% |
| ma20_dist  |  +3.4% |
| ma50_dist  |  +9.2% |
| vol_20d    |  22.1% |
| mdd_60d    |   8.6% |
| rsi_14     |   66.1 |
| zscore_20d |    1.1 |

### Silver / SI=F (score 63.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.1% |
| ret_5d     |  -0.1% |
| ret_20d    | +15.6% |
| ret_60d    |  +0.7% |
| ma20_dist  |  +5.3% |
| ma50_dist  | +12.7% |
| vol_20d    |  28.4% |
| mdd_60d    |  20.9% |
| rsi_14     |   67.2 |
| zscore_20d |    1.5 |

### DAX / ^GDAXI (score 62.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +1.5% |
| ret_20d    | +2.9% |
| ret_60d    | +5.7% |
| ma20_dist  | +0.7% |
| ma50_dist  | +3.2% |
| vol_20d    |  8.0% |
| mdd_60d    |  4.1% |
| rsi_14     |  52.0 |
| zscore_20d |   0.9 |

### Natural Gas / NG=F (score 57.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.3% |
| ret_5d     |  +4.8% |
| ret_20d    |  +8.4% |
| ret_60d    | -10.0% |
| ma20_dist  |  +5.6% |
| ma50_dist  |  +0.5% |
| vol_20d    |  28.6% |
| mdd_60d    |  21.0% |
| rsi_14     |   61.3 |
| zscore_20d |    2.4 |

### Platinum / PL=F (score 54.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | -2.2% |
| ret_20d    | +5.6% |
| ret_60d    | +3.0% |
| ma20_dist  | +3.1% |
| ma50_dist  | +9.4% |
| vol_20d    | 26.3% |
| mdd_60d    | 14.5% |
| rsi_14     |  62.5 |
| zscore_20d |   1.0 |

### S&P 500 / ^GSPC (score 54.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | +1.2% |
| ret_20d    | +3.9% |
| ret_60d    | +1.6% |
| ma20_dist  | +0.4% |
| ma50_dist  | +2.3% |
| vol_20d    | 10.4% |
| mdd_60d    |  4.2% |
| rsi_14     |  46.9 |
| zscore_20d |   0.4 |

### Tesla Inc. / TSLA (score 52.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.6% |
| ret_5d     |  +2.8% |
| ret_20d    | +14.9% |
| ret_60d    | -16.3% |
| ma20_dist  |  +5.3% |
| ma50_dist  |  -1.8% |
| vol_20d    |  36.6% |
| mdd_60d    |  29.9% |
| rsi_14     |   63.6 |
| zscore_20d |    1.4 |

### Dow Jones Industrial Average / ^DJI (score 51.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | +1.5% |
| ret_20d    | +2.6% |
| ret_60d    | +4.4% |
| ma20_dist  | -0.0% |
| ma50_dist  | +1.5% |
| vol_20d    | 10.7% |
| mdd_60d    |  3.2% |
| rsi_14     |  41.3 |
| zscore_20d |  -0.0 |

### NASDAQ 100 / ^NDX (score 49.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.4% |
| ret_5d     | +1.5% |
| ret_20d    | +5.5% |
| ret_60d    | -3.3% |
| ma20_dist  | +0.7% |
| ma50_dist  | +1.3% |
| vol_20d    | 17.5% |
| mdd_60d    | 11.1% |
| rsi_14     |  48.5 |
| zscore_20d |   0.5 |

### Russell 2000 / ^RUT (score 46.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +0.7% |
| ret_20d    | +2.3% |
| ret_60d    | +2.8% |
| ma20_dist  | -0.1% |
| ma50_dist  | +0.8% |
| vol_20d    | 13.7% |
| mdd_60d    |  3.9% |
| rsi_14     |  46.0 |
| zscore_20d |  -0.1 |

### JPMorgan Chase & Co. / JPM (score 45.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.6% |
| ret_5d     |  +0.8% |
| ret_20d    |  +1.0% |
| ret_60d    | +18.2% |
| ma20_dist  |  -1.0% |
| ma50_dist  |  +2.3% |
| vol_20d    |  12.9% |
| mdd_60d    |   3.7% |
| rsi_14     |   45.1 |
| zscore_20d |   -0.9 |

### Brent Crude Oil / BZ=F (score 45.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.1% |
| ret_5d     |  -5.0% |
| ret_20d    | +13.0% |
| ret_60d    |  -3.6% |
| ma20_dist  |  +1.2% |
| ma50_dist  |  +5.8% |
| vol_20d    |  29.6% |
| mdd_60d    |  24.1% |
| rsi_14     |   52.2 |
| zscore_20d |    0.3 |

### Apple Inc. / AAPL (score 42.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | +1.1% |
| ret_20d    | -5.6% |
| ret_60d    | -0.2% |
| ma20_dist  | +1.7% |
| ma50_dist  | +1.0% |
| vol_20d    | 31.3% |
| mdd_60d    | 11.6% |
| rsi_14     |  51.9 |
| zscore_20d |   1.4 |

### FTSE 100 / ^FTSE (score 40.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | +0.4% |
| ret_20d    | -1.0% |
| ret_60d    | +4.2% |
| ma20_dist  | -0.3% |
| ma50_dist  | +1.0% |
| vol_20d    |  5.1% |
| mdd_60d    |  1.9% |
| rsi_14     |  37.7 |
| zscore_20d |  -0.5 |

### Euro Stoxx 50 / ^STOXX50E (score 39.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | +0.0% |
| ret_20d    | +1.3% |
| ret_60d    | +5.3% |
| ma20_dist  | -0.9% |
| ma50_dist  | +1.0% |
| vol_20d    |  7.7% |
| mdd_60d    |  3.2% |
| rsi_14     |  33.6 |
| zscore_20d |  -1.1 |

### Hang Seng / ^HSI (score 33.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | -0.5% |
| ret_20d    | -1.1% |
| ret_60d    | -1.8% |
| ma20_dist  | -0.3% |
| ma50_dist  | +3.1% |
| vol_20d    | 13.9% |
| mdd_60d    | 11.6% |
| rsi_14     |  48.1 |
| zscore_20d |  -0.3 |

### UnitedHealth Group Inc. / UNH (score 28.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.5% |
| ret_5d     | +2.7% |
| ret_20d    | -6.3% |
| ret_60d    | +5.1% |
| ma20_dist  | -1.5% |
| ma50_dist  | -4.3% |
| vol_20d    | 20.5% |
| mdd_60d    | 11.8% |
| rsi_14     |  40.6 |
| zscore_20d |  -0.7 |

### Meta Platforms Inc. / META (score 27.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.9% |
| ret_5d     | +4.6% |
| ret_20d    | +5.9% |
| ret_60d    | -4.4% |
| ma20_dist  | -0.6% |
| ma50_dist  | -3.5% |
| vol_20d    | 36.8% |
| mdd_60d    | 20.9% |
| rsi_14     |  42.1 |
| zscore_20d |  -0.2 |

### CAC 40 / ^FCHI (score 24.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.7% |
| ret_5d     | -1.6% |
| ret_20d    | -2.0% |
| ret_60d    | +0.9% |
| ma20_dist  | -3.0% |
| ma50_dist  | -1.7% |
| vol_20d    |  9.3% |
| mdd_60d    |  4.7% |
| rsi_14     |  12.5 |
| zscore_20d |  -2.2 |

### Amazon.com Inc. / AMZN (score 21.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.5% |
| ret_5d     | -1.5% |
| ret_20d    | +8.8% |
| ret_60d    | -0.1% |
| ma20_dist  | -4.1% |
| ma50_dist  | +2.1% |
| vol_20d    | 60.1% |
| mdd_60d    | 11.1% |
| rsi_14     |  29.8 |
| zscore_20d |  -1.4 |

### Alphabet Inc. Class A / GOOGL (score 17.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -0.0% |
| ret_20d    | +2.1% |
| ret_60d    | -5.8% |
| ma20_dist  | -2.9% |
| ma50_dist  | -2.7% |
| vol_20d    | 37.5% |
| mdd_60d    | 14.9% |
| rsi_14     |  33.7 |
| zscore_20d |  -1.0 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Wheat / ZW=F                        |  25.1250 |           3.4% |                 0.25x |       50.2500 |            6.8% |
| Soybeans / ZS=F                     |  19.1964 |           1.5% |                 0.58x |       38.3929 |            3.1% |
| Corn / ZC=F                         |  17.7143 |           3.5% |                 0.18x |       35.4286 |            6.9% |
| Microsoft Corporation / MSFT        |   9.8076 |           1.9% |                 0.37x |       19.6152 |            3.9% |
| NVIDIA Corporation / NVDA           |   6.5129 |           2.9% |                 0.23x |       13.0257 |            5.7% |
| Gold / GC=F                         |  75.6143 |           1.6% |                 0.45x |      151.2286 |            3.3% |
| Silver / SI=F                       |   1.6197 |           2.3% |                 0.35x |        3.2394 |            4.7% |
| DAX / ^GDAXI                        | 198.3251 |           0.8% |                 1.25x |      396.6501 |            1.5% |
| Natural Gas / NG=F                  |   0.0918 |           3.2% |                 0.35x |        0.1836 |            6.3% |
| Platinum / PL=F                     |  30.8286 |           1.7% |                 0.38x |       61.6572 |            3.3% |
| S&P 500 / ^GSPC                     |  47.8728 |           0.6% |                 0.96x |       95.7457 |            1.2% |
| Tesla Inc. / TSLA                   |  11.8793 |           3.3% |                 0.27x |       23.7586 |            6.7% |
| Dow Jones Industrial Average / ^DJI | 354.9283 |           0.7% |                 0.93x |      709.8566 |            1.3% |
| NASDAQ 100 / ^NDX                   | 327.0187 |           1.1% |                 0.57x |      654.0374 |            2.2% |
| Russell 2000 / ^RUT                 |  24.3643 |           0.8% |                 0.73x |       48.7286 |            1.6% |
| JPMorgan Chase & Co. / JPM          |   5.1357 |           1.4% |                 0.78x |       10.2714 |            2.9% |
| Brent Crude Oil / BZ=F              |   2.8686 |           3.2% |                 0.34x |        5.7371 |            6.4% |
| Apple Inc. / AAPL                   |   6.0843 |           1.9% |                 0.32x |       12.1686 |            3.9% |
| FTSE 100 / ^FTSE                    |  74.7572 |           0.7% |                 1.96x |      149.5144 |            1.4% |
| Euro Stoxx 50 / ^STOXX50E           |  46.0085 |           0.7% |                 1.30x |       92.0170 |            1.4% |
| Hang Seng / ^HSI                    | 330.1494 |           1.3% |                 0.72x |      660.2988 |            2.6% |
| UnitedHealth Group Inc. / UNH       |   7.9800 |           2.0% |                 0.49x |       15.9600 |            4.0% |
| Meta Platforms Inc. / META          |  18.5407 |           3.2% |                 0.27x |       37.0814 |            6.5% |
| CAC 40 / ^FCHI                      |  63.0463 |           0.8% |                 1.07x |      126.0926 |            1.5% |
| Amazon.com Inc. / AMZN              |   5.4650 |           2.1% |                 0.17x |       10.9300 |            4.3% |
| Alphabet Inc. Class A / GOOGL       |   6.2086 |           1.8% |                 0.27x |       12.4171 |            3.6% |

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

Scoring engine version: **1.0.0** | Git commit: **0c1b5b7**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
