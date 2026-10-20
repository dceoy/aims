+++
title = "Market Analysis 2026-09-02"
date = "2026-09-02T00:00:00+00:00"
draft = false
summary = "Bearish market: 26 reliable instruments. Top signal: ZS=F (score 83.3)."
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
source_files = ["data/analysis/2026-09-02.json", "data/history/2026-09-02.json"]
market_regime = "Bearish"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "9ddbea4"
+++

## Market Regime

**Bearish** — 9 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Soybeans / ZS=F** — score 83.3, 20d return +13.0%, RSI14=88. 20d up +13.0%; above MA20 by 7.5%; RSI14=88
- **Wheat / ZW=F** — score 77.9, 20d return +19.4%, RSI14=70. 20d up +19.4%; above MA20 by 10.6%; RSI14=70
- **Corn / ZC=F** — score 74.8, 20d return +18.8%, RSI14=68. 20d up +18.8%; above MA20 by 8.2%; RSI14=68
- **Apple Inc. / AAPL** — score 72.7, 20d return +5.2%, RSI14=75. 20d up +5.2%; above MA20 by 4.4%; RSI14=75
- **Brent Crude Oil / BZ=F** — score 64.8, 20d return +13.3%, RSI14=65. 20d up +13.3%; above MA20 by 5.1%; RSI14=65

## Upcoming Events

_No scheduled events for covered instruments in the next 7 days._

## Signal History

Compared with the previous available report (**2026-09-01**).

- **New top-5:** AAPL, BZ=F
- **Persistent top signals:** ZC=F (15 reports), ZW=F (13 reports), ZS=F (8 reports)
- **Dropped from top-5:** MSFT, NG=F

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     -1 |    +1.2 |
| 7203.T    |     +1 |    +9.1 |
| 8306.T    |     -1 |    -2.1 |
| AAPL      |     +3 |   +14.8 |
| AMZN      |     -2 |    -2.7 |
| BZ=F      |     +6 |   +14.8 |
| CL=F      |     +2 |   +10.3 |
| GC=F      |     -2 |    -3.3 |
| GOOGL     |     +0 |    +0.9 |
| HG=F      |     -1 |   -13.3 |
| JPM       |     +4 |    +5.2 |
| META      |     +9 |   +14.2 |
| MSFT      |     -1 |    -1.5 |
| NG=F      |     -5 |   -11.8 |
| NVDA      |     -3 |   -11.8 |
| PL=F      |     +0 |    -0.3 |
| SI=F      |     -5 |   -10.9 |
| TSLA      |    -13 |   -22.7 |
| UNH       |     +9 |   +19.1 |
| XOM       |     -1 |    +6.1 |
| ZC=F      |     -1 |    -1.2 |
| ZS=F      |     +0 |    +6.1 |
| ZW=F      |     +1 |    +4.8 |
| ^DJI      |     +0 |    -1.2 |
| ^FCHI     |     +0 |    +2.4 |
| ^FTSE     |     +2 |    +0.3 |
| ^GDAXI    |     +0 |    -7.3 |
| ^GSPC     |     +1 |    -2.7 |
| ^HSI      |     +1 |    -3.3 |
| ^N225     |     +1 |    +1.5 |
| ^NDX      |     -6 |   -10.6 |
| ^RUT      |     -3 |    -4.2 |
| ^STOXX50E |     +5 |    +0.3 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **WTI Crude Oil / CL=F** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars
- **Copper / HG=F** — malformed_input

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|    1 | Soybeans / ZS=F        |  83.3 |   Yes    | —               | 20d up +13.0%; above MA20 by 7.5%; RSI14=88  |
|    2 | Wheat / ZW=F           |  77.9 |   Yes    | —               | 20d up +19.4%; above MA20 by 10.6%; RSI14=70 |
|    3 | Corn / ZC=F            |  74.8 |   Yes    | —               | 20d up +18.8%; above MA20 by 8.2%; RSI14=68  |
|    5 | Brent Crude Oil / BZ=F |  64.8 |   Yes    | —               | 20d up +13.3%; above MA20 by 5.1%; RSI14=65  |
|    9 | Natural Gas / NG=F     |  49.7 |   Yes    | —               | 20d up +9.1%; above MA20 by 4.1%; RSI14=64   |
|   18 | Gold / GC=F            |  38.2 |   Yes    | —               | 20d up +0.2%; below MA20 by 2.9%; RSI14=48   |
|   20 | Platinum / PL=F        |  35.5 |   Yes    | —               | 20d up +0.7%; below MA20 by 2.1%; RSI14=51   |
|   23 | Silver / SI=F          |  28.5 |   Yes    | —               | 20d up +2.0%; below MA20 by 2.8%; RSI14=49   |
|   29 | WTI Crude Oil / CL=F   |  67.9 |    No    | malformed_input | Suppressed: malformed_input                  |
|   33 | Copper / HG=F          |  39.7 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                   |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | --------------------------------------------- |
|    4 | Apple Inc. / AAPL                                                              |  72.7 |   Yes    | —                             | 20d up +5.2%; above MA20 by 4.4%; RSI14=75    |
|    6 | Microsoft Corporation / MSFT                                                   |  59.4 |   Yes    | —                             | 20d up +1.9%; above MA20 by 1.4%; RSI14=57    |
|    8 | JPMorgan Chase & Co. / JPM                                                     |  53.0 |   Yes    | —                             | 20d down -0.7%; below MA20 by 0.9%; RSI14=34  |
|   11 | NVIDIA Corporation / NVDA                                                      |  45.1 |   Yes    | —                             | 20d up +2.6%; below MA20 by 0.7%; RSI14=45    |
|   15 | Meta Platforms Inc. / META                                                     |  39.1 |   Yes    | —                             | 20d down -1.6%; above MA20 by 0.7%; RSI14=50  |
|   16 | UnitedHealth Group Inc. / UNH                                                  |  38.5 |   Yes    | —                             | 20d down -2.8%; below MA20 by 0.5%; RSI14=43  |
|   19 | Tesla Inc. / TSLA                                                              |  36.7 |   Yes    | —                             | 20d up +8.8%; above MA20 by 4.0%; RSI14=62    |
|   25 | Amazon.com Inc. / AMZN                                                         |  22.7 |   Yes    | —                             | 20d down -8.1%; below MA20 by 3.6%; RSI14=38  |
|   26 | Alphabet Inc. Class A / GOOGL                                                  |  14.8 |   Yes    | —                             | 20d down -11.3%; below MA20 by 3.3%; RSI14=40 |
|   27 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  77.6 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars     |
|   28 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  71.8 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars     |
|   30 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  65.5 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars     |
|   31 | Exxon Mobil Corporation / XOM                                                  |  65.5 |    No    | malformed_input               | Suppressed: malformed_input                   |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    7 | FTSE 100 / ^FTSE                    |  55.1 |   Yes    | —            | 20d down -0.6%; below MA20 by 0.3%; RSI14=44 |
|   10 | DAX / ^GDAXI                        |  45.8 |   Yes    | —            | 20d down -0.9%; below MA20 by 1.0%; RSI14=40 |
|   12 | S&P 500 / ^GSPC                     |  43.9 |   Yes    | —            | 20d down -1.4%; below MA20 by 1.0%; RSI14=38 |
|   13 | Hang Seng / ^HSI                    |  42.4 |   Yes    | —            | 20d down -2.0%; below MA20 by 1.0%; RSI14=48 |
|   14 | Euro Stoxx 50 / ^STOXX50E           |  39.7 |   Yes    | —            | 20d down -1.8%; below MA20 by 1.7%; RSI14=31 |
|   17 | Dow Jones Industrial Average / ^DJI |  38.5 |   Yes    | —            | 20d down -2.4%; below MA20 by 1.5%; RSI14=34 |
|   21 | NASDAQ 100 / ^NDX                   |  32.1 |   Yes    | —            | 20d down -2.2%; below MA20 by 1.5%; RSI14=38 |
|   22 | CAC 40 / ^FCHI                      |  31.5 |   Yes    | —            | 20d down -4.2%; below MA20 by 2.7%; RSI14=21 |
|   24 | Russell 2000 / ^RUT                 |  27.0 |   Yes    | —            | 20d down -3.8%; below MA20 by 3.1%; RSI14=29 |
|   32 | Nikkei 225 / ^N225                  |  41.2 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-09-01 |
| 7203.T    | 2026-09-01 |
| 8306.T    | 2026-09-01 |
| AAPL      | 2026-09-01 |
| AMZN      | 2026-09-01 |
| BZ=F      | 2026-09-01 |
| CL=F      | 2026-09-01 |
| GC=F      | 2026-09-01 |
| GOOGL     | 2026-09-01 |
| HG=F      | 2026-09-01 |
| JPM       | 2026-09-01 |
| META      | 2026-09-01 |
| MSFT      | 2026-09-01 |
| NG=F      | 2026-09-01 |
| NVDA      | 2026-09-01 |
| PL=F      | 2026-09-01 |
| SI=F      | 2026-09-01 |
| TSLA      | 2026-09-01 |
| UNH       | 2026-09-01 |
| XOM       | 2026-09-01 |
| ZC=F      | 2026-09-01 |
| ZS=F      | 2026-09-01 |
| ZW=F      | 2026-09-01 |
| ^DJI      | 2026-09-01 |
| ^FCHI     | 2026-09-01 |
| ^FTSE     | 2026-09-01 |
| ^GDAXI    | 2026-09-01 |
| ^GSPC     | 2026-09-01 |
| ^HSI      | 2026-09-01 |
| ^N225     | 2026-09-01 |
| ^NDX      | 2026-09-01 |
| ^RUT      | 2026-09-01 |
| ^STOXX50E | 2026-09-01 |

## Symbol Details

### Soybeans / ZS=F (score 83.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.5% |
| ret_5d     |  +6.4% |
| ret_20d    | +13.0% |
| ret_60d    | +16.4% |
| ma20_dist  |  +7.5% |
| ma50_dist  |  +9.3% |
| vol_20d    |  18.8% |
| mdd_60d    |   8.1% |
| rsi_14     |   87.9 |
| zscore_20d |    2.2 |

### Wheat / ZW=F (score 77.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.0% |
| ret_5d     | +11.5% |
| ret_20d    | +19.4% |
| ret_60d    | +30.0% |
| ma20_dist  | +10.6% |
| ma50_dist  | +15.8% |
| vol_20d    |  41.2% |
| mdd_60d    |  10.7% |
| rsi_14     |   69.6 |
| zscore_20d |    1.8 |

### Corn / ZC=F (score 74.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.3% |
| ret_5d     |  +4.2% |
| ret_20d    | +18.8% |
| ret_60d    | +24.5% |
| ma20_dist  |  +8.2% |
| ma50_dist  | +14.1% |
| vol_20d    |  54.8% |
| mdd_60d    |   6.0% |
| rsi_14     |   68.2 |
| zscore_20d |    1.5 |

### Apple Inc. / AAPL (score 72.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.6% |
| ret_5d     | +4.9% |
| ret_20d    | +5.2% |
| ret_60d    | +5.8% |
| ma20_dist  | +4.4% |
| ma50_dist  | +3.9% |
| vol_20d    | 18.4% |
| mdd_60d    | 11.0% |
| rsi_14     |  75.4 |
| zscore_20d |   2.6 |

### Brent Crude Oil / BZ=F (score 64.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +4.6% |
| ret_5d     |  +6.9% |
| ret_20d    | +13.3% |
| ret_60d    |  +1.7% |
| ma20_dist  |  +5.1% |
| ma50_dist  | +10.4% |
| vol_20d    |  30.9% |
| mdd_60d    |  21.2% |
| rsi_14     |   65.3 |
| zscore_20d |    1.8 |

### Microsoft Corporation / MSFT (score 59.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.2% |
| ret_5d     |  +1.9% |
| ret_20d    |  +1.9% |
| ret_60d    | +20.2% |
| ma20_dist  |  +1.4% |
| ma50_dist  | +15.0% |
| vol_20d    |  21.4% |
| mdd_60d    |  14.3% |
| rsi_14     |   56.6 |
| zscore_20d |    0.7 |

### FTSE 100 / ^FTSE (score 55.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | -0.6% |
| ret_20d    | -0.6% |
| ret_60d    | +4.0% |
| ma20_dist  | -0.3% |
| ma50_dist  | +0.8% |
| vol_20d    |  5.3% |
| mdd_60d    |  1.9% |
| rsi_14     |  43.9 |
| zscore_20d |  -0.5 |

### JPMorgan Chase & Co. / JPM (score 53.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.3% |
| ret_5d     |  -0.5% |
| ret_20d    |  -0.7% |
| ret_60d    | +14.1% |
| ma20_dist  |  -0.9% |
| ma50_dist  |  +2.0% |
| vol_20d    |  12.5% |
| mdd_60d    |   3.7% |
| rsi_14     |   34.0 |
| zscore_20d |   -0.9 |

### Natural Gas / NG=F (score 49.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.1% |
| ret_5d     | +4.8% |
| ret_20d    | +9.1% |
| ret_60d    | -8.8% |
| ma20_dist  | +4.1% |
| ma50_dist  | +1.1% |
| vol_20d    | 28.5% |
| mdd_60d    | 21.0% |
| rsi_14     |  64.3 |
| zscore_20d |   1.6 |

### DAX / ^GDAXI (score 45.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.1% |
| ret_5d     | -1.1% |
| ret_20d    | -0.9% |
| ret_60d    | +6.3% |
| ma20_dist  | -1.0% |
| ma50_dist  | +1.3% |
| vol_20d    |  8.6% |
| mdd_60d    |  4.1% |
| rsi_14     |  40.4 |
| zscore_20d |  -1.8 |

### NVIDIA Corporation / NVDA (score 45.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.5% |
| ret_5d     | +2.1% |
| ret_20d    | +2.6% |
| ret_60d    | +6.0% |
| ma20_dist  | -0.7% |
| ma50_dist  | +4.1% |
| vol_20d    | 44.8% |
| mdd_60d    | 10.6% |
| rsi_14     |  44.6 |
| zscore_20d |  -0.3 |

### S&P 500 / ^GSPC (score 43.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | -0.6% |
| ret_20d    | -1.4% |
| ret_60d    | +3.4% |
| ma20_dist  | -1.0% |
| ma50_dist  | +0.8% |
| vol_20d    |  7.2% |
| mdd_60d    |  3.4% |
| rsi_14     |  37.7 |
| zscore_20d |  -1.8 |

### Hang Seng / ^HSI (score 42.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.9% |
| ret_5d     | -0.7% |
| ret_20d    | -2.0% |
| ret_60d    | +1.5% |
| ma20_dist  | -1.0% |
| ma50_dist  | +1.8% |
| vol_20d    | 13.9% |
| mdd_60d    |  8.7% |
| rsi_14     |  47.5 |
| zscore_20d |  -1.2 |

### Euro Stoxx 50 / ^STOXX50E (score 39.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | -1.3% |
| ret_20d    | -1.8% |
| ret_60d    | +5.3% |
| ma20_dist  | -1.7% |
| ma50_dist  | -0.0% |
| vol_20d    |  8.0% |
| mdd_60d    |  3.2% |
| rsi_14     |  31.1 |
| zscore_20d |  -2.2 |

### Meta Platforms Inc. / META (score 39.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | +1.5% |
| ret_20d    | -1.6% |
| ret_60d    | -2.3% |
| ma20_dist  | +0.7% |
| ma50_dist  | -2.3% |
| vol_20d    | 28.8% |
| mdd_60d    | 20.9% |
| rsi_14     |  49.9 |
| zscore_20d |   0.2 |

### UnitedHealth Group Inc. / UNH (score 38.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.8% |
| ret_5d     | -0.1% |
| ret_20d    | -2.8% |
| ret_60d    | -0.2% |
| ma20_dist  | -0.5% |
| ma50_dist  | -3.9% |
| vol_20d    | 20.4% |
| mdd_60d    | 11.8% |
| rsi_14     |  42.9 |
| zscore_20d |  -0.3 |

### Dow Jones Industrial Average / ^DJI (score 38.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | -1.5% |
| ret_20d    | -2.4% |
| ret_60d    | +3.7% |
| ma20_dist  | -1.5% |
| ma50_dist  | -0.2% |
| vol_20d    |  8.2% |
| mdd_60d    |  2.9% |
| rsi_14     |  34.5 |
| zscore_20d |  -2.1 |

### Gold / GC=F (score 38.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.9% |
| ret_5d     | -6.3% |
| ret_20d    | +0.2% |
| ret_60d    | +5.8% |
| ma20_dist  | -2.9% |
| ma50_dist  | +2.5% |
| vol_20d    | 22.4% |
| mdd_60d    |  8.6% |
| rsi_14     |  48.2 |
| zscore_20d |  -1.2 |

### Tesla Inc. / TSLA (score 36.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -3.2% |
| ret_5d     | +1.7% |
| ret_20d    | +8.8% |
| ret_60d    | -8.9% |
| ma20_dist  | +4.0% |
| ma50_dist  | -0.8% |
| vol_20d    | 42.1% |
| mdd_60d    | 29.9% |
| rsi_14     |  61.5 |
| zscore_20d |   1.1 |

### Platinum / PL=F (score 35.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.5% |
| ret_5d     | -4.9% |
| ret_20d    | +0.7% |
| ret_60d    | +4.4% |
| ma20_dist  | -2.1% |
| ma50_dist  | +3.7% |
| vol_20d    | 29.0% |
| mdd_60d    | 14.5% |
| rsi_14     |  51.4 |
| zscore_20d |  -0.7 |

### NASDAQ 100 / ^NDX (score 32.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.3% |
| ret_5d     | -0.5% |
| ret_20d    | -2.2% |
| ret_60d    | +0.4% |
| ma20_dist  | -1.5% |
| ma50_dist  | -0.5% |
| vol_20d    | 12.9% |
| mdd_60d    | 11.0% |
| rsi_14     |  38.2 |
| zscore_20d |  -1.5 |

### CAC 40 / ^FCHI (score 31.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -1.6% |
| ret_20d    | -4.2% |
| ret_60d    | +1.2% |
| ma20_dist  | -2.7% |
| ma50_dist  | -1.9% |
| vol_20d    |  8.7% |
| mdd_60d    |  4.9% |
| rsi_14     |  21.1 |
| zscore_20d |  -1.7 |

### Silver / SI=F (score 28.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.4% |
| ret_5d     | -5.9% |
| ret_20d    | +2.0% |
| ret_60d    | +0.0% |
| ma20_dist  | -2.8% |
| ma50_dist  | +4.2% |
| vol_20d    | 30.1% |
| mdd_60d    | 20.9% |
| rsi_14     |  48.9 |
| zscore_20d |  -1.0 |

### Russell 2000 / ^RUT (score 27.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.2% |
| ret_5d     | -3.0% |
| ret_20d    | -3.8% |
| ret_60d    | +3.1% |
| ma20_dist  | -3.1% |
| ma50_dist  | -2.3% |
| vol_20d    | 12.0% |
| mdd_60d    |  4.8% |
| rsi_14     |  29.0 |
| zscore_20d |  -2.7 |

### Amazon.com Inc. / AMZN (score 22.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.9% |
| ret_5d     | -2.4% |
| ret_20d    | -8.1% |
| ret_60d    | +3.6% |
| ma20_dist  | -3.6% |
| ma50_dist  | +1.0% |
| vol_20d    | 25.8% |
| mdd_60d    | 11.1% |
| rsi_14     |  38.2 |
| zscore_20d |  -1.5 |

### Alphabet Inc. Class A / GOOGL (score 14.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.3% |
| ret_5d     |  -3.4% |
| ret_20d    | -11.3% |
| ret_60d    |  -9.0% |
| ma20_dist  |  -3.3% |
| ma50_dist  |  -4.0% |
| vol_20d    |  23.4% |
| mdd_60d    |  14.9% |
| rsi_14     |   39.9 |
| zscore_20d |   -1.7 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Soybeans / ZS=F                     |  21.7857 |           1.7% |                 0.53x |       43.5714 |            3.3% |
| Wheat / ZW=F                        |  25.5357 |           3.3% |                 0.24x |       51.0714 |            6.7% |
| Corn / ZC=F                         |  16.8214 |           3.2% |                 0.18x |       33.6429 |            6.5% |
| Apple Inc. / AAPL                   |   6.6614 |           2.0% |                 0.54x |       13.3229 |            4.1% |
| Brent Crude Oil / BZ=F              |   2.9571 |           3.1% |                 0.32x |        5.9143 |            6.2% |
| Microsoft Corporation / MSFT        |   9.6706 |           1.9% |                 0.47x |       19.3411 |            3.9% |
| FTSE 100 / ^FTSE                    |  77.7929 |           0.7% |                 1.90x |      155.5858 |            1.4% |
| JPMorgan Chase & Co. / JPM          |   5.1729 |           1.5% |                 0.80x |       10.3457 |            2.9% |
| Natural Gas / NG=F                  |   0.0964 |           3.3% |                 0.35x |        0.1927 |            6.6% |
| DAX / ^GDAXI                        | 216.5137 |           0.8% |                 1.16x |      433.0273 |            1.7% |
| NVIDIA Corporation / NVDA           |   6.6736 |           3.1% |                 0.22x |       13.3471 |            6.1% |
| S&P 500 / ^GSPC                     |  53.1221 |           0.7% |                 1.39x |      106.2443 |            1.4% |
| Hang Seng / ^HSI                    | 321.4100 |           1.3% |                 0.72x |      642.8200 |            2.5% |
| Euro Stoxx 50 / ^STOXX50E           |  51.3256 |           0.8% |                 1.25x |      102.6513 |            1.6% |
| Meta Platforms Inc. / META          |  18.1893 |           3.1% |                 0.35x |       36.3786 |            6.3% |
| UnitedHealth Group Inc. / UNH       |   7.8929 |           2.0% |                 0.49x |       15.7857 |            4.0% |
| Dow Jones Industrial Average / ^DJI | 378.1359 |           0.7% |                 1.22x |      756.2718 |            1.4% |
| Gold / GC=F                         |  83.8143 |           1.9% |                 0.45x |      167.6286 |            3.9% |
| Tesla Inc. / TSLA                   |  13.7314 |           3.9% |                 0.24x |       27.4629 |            7.7% |
| Platinum / PL=F                     |  34.5929 |           2.0% |                 0.34x |       69.1857 |            3.9% |
| NASDAQ 100 / ^NDX                   | 344.1636 |           1.2% |                 0.78x |      688.3273 |            2.4% |
| CAC 40 / ^FCHI                      |  72.8462 |           0.9% |                 1.15x |      145.6924 |            1.8% |
| Silver / SI=F                       |   2.0725 |           3.2% |                 0.33x |        4.1450 |            6.4% |
| Russell 2000 / ^RUT                 |  27.8186 |           1.0% |                 0.83x |       55.6371 |            1.9% |
| Amazon.com Inc. / AMZN              |   6.0414 |           2.4% |                 0.39x |       12.0829 |            4.7% |
| Alphabet Inc. Class A / GOOGL       |   6.2064 |           1.9% |                 0.43x |       12.4129 |            3.7% |

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

Scoring engine version: **1.0.0** | Git commit: **9ddbea4**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
