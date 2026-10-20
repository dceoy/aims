+++
title = "Market Analysis 2026-09-04"
date = "2026-09-04T00:00:00+00:00"
draft = false
summary = "Bullish market: 26 reliable instruments. Top signal: ZS=F (score 77.6)."
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
source_files = ["data/analysis/2026-09-04.json", "data/history/2026-09-04.json"]
market_regime = "Bullish"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "91d26f1"
+++

## Market Regime

**Bullish** — 18 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Soybeans / ZS=F** — score 77.6, 20d return +12.8%, RSI14=83. 20d up +12.8%; above MA20 by 6.3%; RSI14=83
- **Apple Inc. / AAPL** — score 70.0, 20d return +5.1%, RSI14=75. 20d up +5.1%; above MA20 by 4.9%; RSI14=75
- **Microsoft Corporation / MSFT** — score 67.6, 20d return +2.2%, RSI14=59. 20d up +2.2%; above MA20 by 3.0%; RSI14=59
- **Corn / ZC=F** — score 66.4, 20d return +17.6%, RSI14=69. 20d up +17.6%; above MA20 by 5.5%; RSI14=69
- **JPMorgan Chase & Co. / JPM** — score 62.7, 20d return +1.6%, RSI14=49. 20d up +1.6%; above MA20 by 1.1%; RSI14=49

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                        | Applies To               |
| ---------- | ---------------------------- | ------------------------ |
| 2026-09-10 | ECB monetary policy decision | ^FCHI, ^GDAXI, ^STOXX50E |

## Signal History

Compared with the previous available report (**2026-09-03**).

- **New top-5:** JPM, MSFT
- **Persistent top signals:** ZC=F (17 reports), ZS=F (10 reports), AAPL (3 reports)
- **Dropped from top-5:** BZ=F, ZW=F

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +0 |    -4.8 |
| 7203.T    |     +2 |    -1.5 |
| 8306.T    |     +2 |   +11.2 |
| AAPL      |     +2 |    +1.2 |
| AMZN      |     +4 |    +5.8 |
| BZ=F      |     -5 |    -7.6 |
| CL=F      |     -1 |    -2.7 |
| GC=F      |     +0 |    +5.2 |
| GOOGL     |     +1 |    +3.3 |
| HG=F      |     +0 |    +1.2 |
| JPM       |     +3 |    +4.8 |
| META      |     +3 |   +10.0 |
| MSFT      |     +6 |   +11.5 |
| NG=F      |    -10 |   -22.1 |
| NVDA      |     -3 |    -5.2 |
| PL=F      |     +5 |   +12.1 |
| SI=F      |     +6 |    +6.7 |
| TSLA      |     +8 |   +16.7 |
| UNH       |     -2 |    -5.2 |
| XOM       |     -3 |   -11.5 |
| ZC=F      |     +1 |    -0.6 |
| ZS=F      |     +0 |    +1.2 |
| ZW=F      |     -6 |   -11.5 |
| ^DJI      |     +2 |    +5.5 |
| ^FCHI     |     -1 |    +0.6 |
| ^FTSE     |     -1 |    +1.8 |
| ^GDAXI    |     +0 |    -0.9 |
| ^GSPC     |     -2 |    +0.0 |
| ^HSI      |     -8 |   -10.9 |
| ^N225     |     +0 |    -3.6 |
| ^NDX      |     +1 |    -0.9 |
| ^RUT      |     -2 |    -5.8 |
| ^STOXX50E |     -2 |    -3.9 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **WTI Crude Oil / CL=F** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Copper / HG=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                 |
| ---: | ---------------------- | ----: | :------: | --------------- | ------------------------------------------- |
|    1 | Soybeans / ZS=F        |  77.6 |   Yes    | —               | 20d up +12.8%; above MA20 by 6.3%; RSI14=83 |
|    4 | Corn / ZC=F            |  66.4 |   Yes    | —               | 20d up +17.6%; above MA20 by 5.5%; RSI14=69 |
|    7 | Brent Crude Oil / BZ=F |  61.5 |   Yes    | —               | 20d up +8.9%; above MA20 by 4.9%; RSI14=62  |
|    9 | Wheat / ZW=F           |  57.6 |   Yes    | —               | 20d up +14.9%; above MA20 by 5.0%; RSI14=64 |
|   14 | Platinum / PL=F        |  50.0 |   Yes    | —               | 20d up +4.8%; above MA20 by 1.4%; RSI14=55  |
|   15 | Gold / GC=F            |  47.9 |   Yes    | —               | 20d up +3.0%; above MA20 by 0.1%; RSI14=54  |
|   16 | Natural Gas / NG=F     |  40.0 |   Yes    | —               | 20d up +4.3%; above MA20 by 3.8%; RSI14=69  |
|   17 | Silver / SI=F          |  38.5 |   Yes    | —               | 20d up +2.9%; above MA20 by 0.5%; RSI14=52  |
|   28 | WTI Crude Oil / CL=F   |  68.5 |    No    | malformed_input | Suppressed: malformed_input                 |
|   32 | Copper / HG=F          |  40.6 |    No    | malformed_input | Suppressed: malformed_input                 |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    2 | Apple Inc. / AAPL                                                              |  70.0 |   Yes    | —                             | 20d up +5.1%; above MA20 by 4.9%; RSI14=75   |
|    3 | Microsoft Corporation / MSFT                                                   |  67.6 |   Yes    | —                             | 20d up +2.2%; above MA20 by 3.0%; RSI14=59   |
|    5 | JPMorgan Chase & Co. / JPM                                                     |  62.7 |   Yes    | —                             | 20d up +1.6%; above MA20 by 1.1%; RSI14=49   |
|    6 | Tesla Inc. / TSLA                                                              |  62.7 |   Yes    | —                             | 20d up +17.8%; above MA20 by 8.4%; RSI14=63  |
|    8 | Meta Platforms Inc. / META                                                     |  59.4 |   Yes    | —                             | 20d up +3.5%; above MA20 by 6.1%; RSI14=58   |
|   10 | NVIDIA Corporation / NVDA                                                      |  57.0 |   Yes    | —                             | 20d up +4.3%; above MA20 by 4.0%; RSI14=52   |
|   19 | UnitedHealth Group Inc. / UNH                                                  |  35.8 |   Yes    | —                             | 20d down -0.8%; above MA20 by 0.9%; RSI14=49 |
|   20 | Amazon.com Inc. / AMZN                                                         |  34.2 |   Yes    | —                             | 20d down -4.9%; below MA20 by 1.6%; RSI14=46 |
|   25 | Alphabet Inc. Class A / GOOGL                                                  |  28.2 |   Yes    | —                             | 20d down -4.3%; below MA20 by 0.6%; RSI14=46 |
|   27 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  70.6 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   29 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  55.8 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   30 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  53.3 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   31 | Exxon Mobil Corporation / XOM                                                  |  51.5 |    No    | malformed_input               | Suppressed: malformed_input                  |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|   11 | Dow Jones Industrial Average / ^DJI |  52.4 |   Yes    | —            | 20d down -0.4%; above MA20 by 0.4%; RSI14=49 |
|   12 | S&P 500 / ^GSPC                     |  52.1 |   Yes    | —            | 20d up +0.5%; above MA20 by 0.5%; RSI14=46   |
|   13 | FTSE 100 / ^FTSE                    |  51.2 |   Yes    | —            | 20d down -0.5%; above MA20 by 0.2%; RSI14=56 |
|   18 | DAX / ^GDAXI                        |  37.9 |   Yes    | —            | 20d down -0.5%; below MA20 by 0.8%; RSI14=39 |
|   21 | NASDAQ 100 / ^NDX                   |  34.2 |   Yes    | —            | 20d up +0.4%; below MA20 by 0.0%; RSI14=40   |
|   22 | Euro Stoxx 50 / ^STOXX50E           |  33.9 |   Yes    | —            | 20d down -1.8%; below MA20 by 1.3%; RSI14=32 |
|   23 | Russell 2000 / ^RUT                 |  31.2 |   Yes    | —            | 20d down -1.1%; below MA20 by 1.3%; RSI14=35 |
|   24 | Hang Seng / ^HSI                    |  30.3 |   Yes    | —            | 20d down -1.2%; below MA20 by 1.2%; RSI14=52 |
|   26 | CAC 40 / ^FCHI                      |  27.0 |   Yes    | —            | 20d down -4.8%; below MA20 by 2.5%; RSI14=22 |
|   33 | Nikkei 225 / ^N225                  |  12.4 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-09-03 |
| 7203.T    | 2026-09-03 |
| 8306.T    | 2026-09-03 |
| AAPL      | 2026-09-03 |
| AMZN      | 2026-09-03 |
| BZ=F      | 2026-09-03 |
| CL=F      | 2026-09-03 |
| GC=F      | 2026-09-03 |
| GOOGL     | 2026-09-03 |
| HG=F      | 2026-09-03 |
| JPM       | 2026-09-03 |
| META      | 2026-09-03 |
| MSFT      | 2026-09-03 |
| NG=F      | 2026-09-03 |
| NVDA      | 2026-09-03 |
| PL=F      | 2026-09-03 |
| SI=F      | 2026-09-03 |
| TSLA      | 2026-09-03 |
| UNH       | 2026-09-03 |
| XOM       | 2026-09-03 |
| ZC=F      | 2026-09-03 |
| ZS=F      | 2026-09-03 |
| ZW=F      | 2026-09-03 |
| ^DJI      | 2026-09-03 |
| ^FCHI     | 2026-09-03 |
| ^FTSE     | 2026-09-03 |
| ^GDAXI    | 2026-09-03 |
| ^GSPC     | 2026-09-03 |
| ^HSI      | 2026-09-03 |
| ^N225     | 2026-09-03 |
| ^NDX      | 2026-09-03 |
| ^RUT      | 2026-09-03 |
| ^STOXX50E | 2026-09-03 |

## Symbol Details

### Soybeans / ZS=F (score 77.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.3% |
| ret_5d     |  +4.0% |
| ret_20d    | +12.8% |
| ret_60d    | +17.3% |
| ma20_dist  |  +6.3% |
| ma50_dist  |  +8.6% |
| vol_20d    |  15.7% |
| mdd_60d    |   8.1% |
| rsi_14     |   83.4 |
| zscore_20d |    1.7 |

### Apple Inc. / AAPL (score 70.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.0% |
| ret_5d     |  +4.3% |
| ret_20d    |  +5.1% |
| ret_60d    | +13.0% |
| ma20_dist  |  +4.9% |
| ma50_dist  |  +4.5% |
| vol_20d    |  18.5% |
| mdd_60d    |  11.0% |
| rsi_14     |   74.8 |
| zscore_20d |    2.2 |

### Microsoft Corporation / MSFT (score 67.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.7% |
| ret_5d     |  +1.0% |
| ret_20d    |  +2.2% |
| ret_60d    | +26.5% |
| ma20_dist  |  +3.0% |
| ma50_dist  | +15.7% |
| vol_20d    |  21.5% |
| mdd_60d    |  11.7% |
| rsi_14     |   59.4 |
| zscore_20d |    1.5 |

### Corn / ZC=F (score 66.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.7% |
| ret_5d     |  +1.0% |
| ret_20d    | +17.6% |
| ret_60d    | +24.8% |
| ma20_dist  |  +5.5% |
| ma50_dist  | +11.7% |
| vol_20d    |  47.1% |
| mdd_60d    |   6.0% |
| rsi_14     |   69.0 |
| zscore_20d |    1.0 |

### JPMorgan Chase & Co. / JPM (score 62.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.6% |
| ret_5d     |  +2.2% |
| ret_20d    |  +1.6% |
| ret_60d    | +16.3% |
| ma20_dist  |  +1.1% |
| ma50_dist  |  +3.7% |
| vol_20d    |  13.3% |
| mdd_60d    |   3.7% |
| rsi_14     |   48.9 |
| zscore_20d |    1.0 |

### Tesla Inc. / TSLA (score 62.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +5.4% |
| ret_5d     |  +6.1% |
| ret_20d    | +17.8% |
| ret_60d    |  -5.1% |
| ma20_dist  |  +8.4% |
| ma50_dist  |  +5.0% |
| vol_20d    |  44.4% |
| mdd_60d    |  29.9% |
| rsi_14     |   63.2 |
| zscore_20d |    2.3 |

### Brent Crude Oil / BZ=F (score 61.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.1% |
| ret_5d     |  +6.5% |
| ret_20d    |  +8.9% |
| ret_60d    |  +9.4% |
| ma20_dist  |  +4.9% |
| ma50_dist  | +10.2% |
| vol_20d    |  28.4% |
| mdd_60d    |  21.2% |
| rsi_14     |   62.4 |
| zscore_20d |    1.7 |

### Meta Platforms Inc. / META (score 59.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +3.0% |
| ret_5d     | +6.9% |
| ret_20d    | +3.5% |
| ret_60d    | +4.6% |
| ma20_dist  | +6.1% |
| ma50_dist  | +2.8% |
| vol_20d    | 31.8% |
| mdd_60d    | 20.9% |
| rsi_14     |  57.7 |
| zscore_20d |   1.9 |

### Wheat / ZW=F (score 57.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.5% |
| ret_5d     |  -0.9% |
| ret_20d    | +14.9% |
| ret_60d    | +25.9% |
| ma20_dist  |  +5.0% |
| ma50_dist  | +10.4% |
| vol_20d    |  42.4% |
| mdd_60d    |  10.7% |
| rsi_14     |   63.7 |
| zscore_20d |    0.9 |

### NVIDIA Corporation / NVDA (score 57.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.8% |
| ret_5d     | +0.2% |
| ret_20d    | +4.3% |
| ret_60d    | +9.7% |
| ma20_dist  | +4.0% |
| ma50_dist  | +8.9% |
| vol_20d    | 44.9% |
| mdd_60d    | 10.6% |
| rsi_14     |  52.3 |
| zscore_20d |   1.6 |

### Dow Jones Industrial Average / ^DJI (score 52.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.2% |
| ret_5d     | +0.2% |
| ret_20d    | -0.4% |
| ret_60d    | +5.5% |
| ma20_dist  | +0.4% |
| ma50_dist  | +1.5% |
| vol_20d    |  9.0% |
| mdd_60d    |  2.9% |
| rsi_14     |  49.4 |
| zscore_20d |   0.6 |

### S&P 500 / ^GSPC (score 52.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | +0.2% |
| ret_20d    | +0.5% |
| ret_60d    | +4.9% |
| ma20_dist  | +0.5% |
| ma50_dist  | +2.2% |
| vol_20d    |  8.3% |
| mdd_60d    |  3.4% |
| rsi_14     |  46.4 |
| zscore_20d |   0.8 |

### FTSE 100 / ^FTSE (score 51.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | -0.4% |
| ret_20d    | -0.5% |
| ret_60d    | +5.6% |
| ma20_dist  | +0.2% |
| ma50_dist  | +1.1% |
| vol_20d    |  5.9% |
| mdd_60d    |  1.9% |
| rsi_14     |  56.0 |
| zscore_20d |   0.4 |

### Platinum / PL=F (score 50.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +3.9% |
| ret_5d     | -0.9% |
| ret_20d    | +4.8% |
| ret_60d    | +7.0% |
| ma20_dist  | +1.4% |
| ma50_dist  | +7.2% |
| vol_20d    | 31.7% |
| mdd_60d    | 14.5% |
| rsi_14     |  55.2 |
| zscore_20d |   0.5 |

### Gold / GC=F (score 47.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.9% |
| ret_5d     | -2.6% |
| ret_20d    | +3.0% |
| ret_60d    | +6.6% |
| ma20_dist  | +0.1% |
| ma50_dist  | +5.5% |
| vol_20d    | 24.3% |
| mdd_60d    |  8.6% |
| rsi_14     |  54.0 |
| zscore_20d |   0.1 |

### Natural Gas / NG=F (score 40.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.5% |
| ret_5d     | +0.2% |
| ret_20d    | +4.3% |
| ret_60d    | -6.6% |
| ma20_dist  | +3.8% |
| ma50_dist  | +1.8% |
| vol_20d    | 27.7% |
| mdd_60d    | 21.0% |
| rsi_14     |  68.6 |
| zscore_20d |   1.3 |

### Silver / SI=F (score 38.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +3.5% |
| ret_5d     | -3.5% |
| ret_20d    | +2.9% |
| ret_60d    | -1.3% |
| ma20_dist  | +0.5% |
| ma50_dist  | +7.5% |
| vol_20d    | 31.3% |
| mdd_60d    | 20.9% |
| rsi_14     |  52.4 |
| zscore_20d |   0.2 |

### DAX / ^GDAXI (score 37.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | -1.4% |
| ret_20d    | -0.5% |
| ret_60d    | +7.4% |
| ma20_dist  | -0.8% |
| ma50_dist  | +1.3% |
| vol_20d    |  9.1% |
| mdd_60d    |  4.1% |
| rsi_14     |  39.1 |
| zscore_20d |  -1.2 |

### UnitedHealth Group Inc. / UNH (score 35.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +1.5% |
| ret_20d    | -0.8% |
| ret_60d    | -2.4% |
| ma20_dist  | +0.9% |
| ma50_dist  | -2.7% |
| vol_20d    | 18.7% |
| mdd_60d    | 11.8% |
| rsi_14     |  49.3 |
| zscore_20d |   0.6 |

### Amazon.com Inc. / AMZN (score 34.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.5% |
| ret_5d     | +1.0% |
| ret_20d    | -4.9% |
| ret_60d    | +6.0% |
| ma20_dist  | -1.6% |
| ma50_dist  | +2.2% |
| vol_20d    | 26.2% |
| mdd_60d    | 11.1% |
| rsi_14     |  46.4 |
| zscore_20d |  -0.7 |

### NASDAQ 100 / ^NDX (score 34.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.2% |
| ret_5d     | -0.5% |
| ret_20d    | +0.4% |
| ret_60d    | +1.4% |
| ma20_dist  | -0.0% |
| ma50_dist  | +0.9% |
| vol_20d    | 13.3% |
| mdd_60d    | 11.0% |
| rsi_14     |  40.1 |
| zscore_20d |  -0.0 |

### Euro Stoxx 50 / ^STOXX50E (score 33.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | -0.7% |
| ret_20d    | -1.8% |
| ret_60d    | +5.4% |
| ma20_dist  | -1.3% |
| ma50_dist  | +0.1% |
| vol_20d    |  7.9% |
| mdd_60d    |  3.2% |
| rsi_14     |  32.4 |
| zscore_20d |  -1.5 |

### Russell 2000 / ^RUT (score 31.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | -1.5% |
| ret_20d    | -1.1% |
| ret_60d    | +3.5% |
| ma20_dist  | -1.3% |
| ma50_dist  | -0.7% |
| vol_20d    | 12.8% |
| mdd_60d    |  4.8% |
| rsi_14     |  34.6 |
| zscore_20d |  -1.1 |

### Hang Seng / ^HSI (score 30.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -1.4% |
| ret_20d    | -1.2% |
| ret_60d    | +2.6% |
| ma20_dist  | -1.2% |
| ma50_dist  | +1.0% |
| vol_20d    | 13.0% |
| mdd_60d    |  8.7% |
| rsi_14     |  52.4 |
| zscore_20d |  -1.5 |

### Alphabet Inc. Class A / GOOGL (score 28.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.6% |
| ret_5d     | +0.5% |
| ret_20d    | -4.3% |
| ret_60d    | -6.0% |
| ma20_dist  | -0.6% |
| ma50_dist  | -1.8% |
| vol_20d    | 20.9% |
| mdd_60d    | 14.9% |
| rsi_14     |  46.3 |
| zscore_20d |  -0.4 |

### CAC 40 / ^FCHI (score 27.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | -0.4% |
| ret_20d    | -4.8% |
| ret_60d    | +1.0% |
| ma20_dist  | -2.5% |
| ma50_dist  | -2.0% |
| vol_20d    |  8.5% |
| mdd_60d    |  5.1% |
| rsi_14     |  22.3 |
| zscore_20d |  -1.4 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Soybeans / ZS=F                     |  20.7500 |           1.6% |                 0.64x |       41.5000 |            3.2% |
| Apple Inc. / AAPL                   |   6.9779 |           2.1% |                 0.54x |       13.9557 |            4.3% |
| Microsoft Corporation / MSFT        |  10.4611 |           2.1% |                 0.47x |       20.9223 |            4.1% |
| Corn / ZC=F                         |  15.0714 |           2.9% |                 0.21x |       30.1429 |            5.9% |
| JPMorgan Chase & Co. / JPM          |   5.5214 |           1.5% |                 0.75x |       11.0429 |            3.1% |
| Tesla Inc. / TSLA                   |  14.1171 |           3.8% |                 0.23x |       28.2343 |            7.5% |
| Brent Crude Oil / BZ=F              |   3.1479 |           3.3% |                 0.35x |        6.2957 |            6.6% |
| Meta Platforms Inc. / META          |  19.6479 |           3.2% |                 0.31x |       39.2957 |            6.4% |
| Wheat / ZW=F                        |  25.8571 |           3.5% |                 0.24x |       51.7143 |            7.0% |
| NVIDIA Corporation / NVDA           |   7.3871 |           3.2% |                 0.22x |       14.7743 |            6.5% |
| Dow Jones Industrial Average / ^DJI | 413.9302 |           0.8% |                 1.12x |      827.8605 |            1.5% |
| S&P 500 / ^GSPC                     |  55.8350 |           0.7% |                 1.21x |      111.6699 |            1.4% |
| FTSE 100 / ^FTSE                    |  83.2929 |           0.8% |                 1.70x |      166.5858 |            1.5% |
| Platinum / PL=F                     |  36.7357 |           2.0% |                 0.32x |       73.4714 |            4.0% |
| Gold / GC=F                         |  89.9000 |           2.0% |                 0.41x |      179.8000 |            4.0% |
| Natural Gas / NG=F                  |   0.1028 |           3.5% |                 0.36x |        0.2056 |            7.1% |
| Silver / SI=F                       |   2.2044 |           3.3% |                 0.32x |        4.4087 |            6.6% |
| DAX / ^GDAXI                        | 217.8694 |           0.8% |                 1.10x |      435.7388 |            1.7% |
| UnitedHealth Group Inc. / UNH       |   7.8464 |           2.0% |                 0.53x |       15.6929 |            3.9% |
| Amazon.com Inc. / AMZN              |   5.9771 |           2.3% |                 0.38x |       11.9543 |            4.6% |
| NASDAQ 100 / ^NDX                   | 338.3449 |           1.1% |                 0.75x |      676.6897 |            2.3% |
| Euro Stoxx 50 / ^STOXX50E           |  52.5007 |           0.8% |                 1.26x |      105.0013 |            1.6% |
| Russell 2000 / ^RUT                 |  29.5957 |           1.0% |                 0.78x |       59.1914 |            2.0% |
| Hang Seng / ^HSI                    | 332.8344 |           1.3% |                 0.77x |      665.6688 |            2.6% |
| Alphabet Inc. Class A / GOOGL       |   6.5207 |           1.9% |                 0.48x |       13.0414 |            3.8% |
| CAC 40 / ^FCHI                      |  74.8656 |           0.9% |                 1.18x |      149.7312 |            1.8% |

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

Scoring engine version: **1.0.0** | Git commit: **91d26f1**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
