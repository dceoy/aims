+++
title = "Market Analysis 2026-07-21"
date = "2026-07-21T00:00:00+00:00"
draft = false
summary = "Neutral market: 26 reliable instruments. Top signal: ZS=F (score 78.5)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-07-21.json", "data/history/2026-07-21.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "c154c40"
+++

## Market Regime

**Neutral** — 12 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Soybeans / ZS=F** — score 78.5, 20d return +9.2%, RSI14=83. 20d up +9.2%; above MA20 by 5.4%; RSI14=83
- **Wheat / ZW=F** — score 74.5, 20d return +11.3%, RSI14=83. 20d up +11.3%; above MA20 by 9.6%; RSI14=83
- **Hang Seng / ^HSI** — score 70.6, 20d return +5.1%, RSI14=77. 20d up +5.1%; above MA20 by 5.6%; RSI14=77
- **Apple Inc. / AAPL** — score 68.2, 20d return +9.6%, RSI14=82. 20d up +9.6%; above MA20 by 6.4%; RSI14=82
- **Corn / ZC=F** — score 63.9, 20d return +7.7%, RSI14=74. 20d up +7.7%; above MA20 by 5.1%; RSI14=74

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                        | Applies To               |
| ---------- | ---------------------------- | ------------------------ |
| 2026-07-22 | GOOGL earnings release       | GOOGL                    |
| 2026-07-22 | TSLA earnings release        | TSLA                     |
| 2026-07-23 | ECB monetary policy decision | ^FCHI, ^GDAXI, ^STOXX50E |

## Signal History

Compared with the previous available report (**2026-07-20**).
- **New top-5:** ZC=F, ^HSI
- **Persistent top signals:** ZW=F (11 reports), AAPL (6 reports), ZS=F (5 reports)
- **Dropped from top-5:** JPM, ^FTSE

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +0 |    -2.7 |
| 7203.T    |     -1 |    -3.6 |
| 8306.T    |     +0 |    +0.0 |
| AAPL      |     -2 |   -10.9 |
| AMZN      |     +3 |    +2.4 |
| BZ=F      |     +1 |    -0.3 |
| CL=F      |     +0 |    -2.7 |
| GC=F      |     +0 |    +4.8 |
| GOOGL     |     +4 |   +13.0 |
| HG=F      |     +1 |   +10.9 |
| JPM       |     -2 |    -3.6 |
| META      |     +5 |    +3.6 |
| MSFT      |    +10 |   +13.3 |
| NG=F      |     -4 |   -11.2 |
| NVDA      |     +1 |    +8.2 |
| PL=F      |     +1 |    +3.6 |
| SI=F      |     +1 |    +6.1 |
| TSLA      |     -1 |    -6.1 |
| UNH       |     -4 |   -11.5 |
| XOM       |     +0 |    -0.6 |
| ZC=F      |     +2 |    +0.9 |
| ZS=F      |     +2 |    +7.3 |
| ZW=F      |     -1 |    -8.2 |
| ^DJI      |     -7 |    -8.8 |
| ^FCHI     |     +0 |    +0.9 |
| ^FTSE     |     -4 |   -10.6 |
| ^GDAXI    |     +0 |    -0.9 |
| ^GSPC     |     -3 |    -3.0 |
| ^HSI      |     +7 |   +14.8 |
| ^N225     |     +0 |    +0.3 |
| ^NDX      |     -2 |    +1.8 |
| ^RUT      |     -4 |    -7.0 |
| ^STOXX50E |     -3 |    -0.3 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **WTI Crude Oil / CL=F** — malformed_input
- **Copper / HG=F** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Nikkei 225 / ^N225** — missing_bars

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|    1 | Soybeans / ZS=F        |  78.5 |   Yes    | —               | 20d up +9.2%; above MA20 by 5.4%; RSI14=83    |
|    2 | Wheat / ZW=F           |  74.5 |   Yes    | —               | 20d up +11.3%; above MA20 by 9.6%; RSI14=83   |
|    5 | Corn / ZC=F            |  63.9 |   Yes    | —               | 20d up +7.7%; above MA20 by 5.1%; RSI14=74    |
|    7 | Brent Crude Oil / BZ=F |  61.8 |   Yes    | —               | 20d up +11.7%; above MA20 by 14.6%; RSI14=83  |
|   22 | Gold / GC=F            |  31.5 |   Yes    | —               | 20d down -5.1%; below MA20 by 1.4%; RSI14=49  |
|   23 | Platinum / PL=F        |  22.1 |   Yes    | —               | 20d down -6.6%; below MA20 by 1.3%; RSI14=53  |
|   24 | Natural Gas / NG=F     |  19.4 |   Yes    | —               | 20d down -11.5%; below MA20 by 7.9%; RSI14=30 |
|   25 | Silver / SI=F          |  17.3 |   Yes    | —               | 20d down -14.3%; below MA20 by 4.1%; RSI14=46 |
|   30 | WTI Crude Oil / CL=F   |  57.6 |    No    | malformed_input | Suppressed: malformed_input                   |
|   31 | Copper / HG=F          |  54.9 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    4 | Apple Inc. / AAPL                                                              |  68.2 |   Yes    | —                             | 20d up +9.6%; above MA20 by 6.4%; RSI14=82   |
|    6 | JPMorgan Chase & Co. / JPM                                                     |  62.7 |   Yes    | —                             | 20d up +4.7%; above MA20 by 1.1%; RSI14=60   |
|    8 | Microsoft Corporation / MSFT                                                   |  58.2 |   Yes    | —                             | 20d up +6.0%; above MA20 by 5.2%; RSI14=71   |
|   10 | UnitedHealth Group Inc. / UNH                                                  |  52.7 |   Yes    | —                             | 20d up +5.1%; above MA20 by 0.1%; RSI14=51   |
|   11 | Meta Platforms Inc. / META                                                     |  50.6 |   Yes    | —                             | 20d up +11.9%; above MA20 by 6.1%; RSI14=66  |
|   12 | Amazon.com Inc. / AMZN                                                         |  50.0 |   Yes    | —                             | 20d up +2.3%; above MA20 by 3.2%; RSI14=63   |
|   19 | Alphabet Inc. Class A / GOOGL                                                  |  38.8 |   Yes    | —                             | 20d down -4.4%; below MA20 by 0.9%; RSI14=49 |
|   20 | NVIDIA Corporation / NVDA                                                      |  38.5 |   Yes    | —                             | 20d down -3.5%; above MA20 by 0.8%; RSI14=57 |
|   26 | Tesla Inc. / TSLA                                                              |  10.6 |   Yes    | —                             | 20d down -7.7%; below MA20 by 6.7%; RSI14=36 |
|   27 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  67.0 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   28 | Exxon Mobil Corporation / XOM                                                  |  65.8 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   29 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  61.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   32 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  50.9 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    3 | Hang Seng / ^HSI                    |  70.6 |   Yes    | —            | 20d up +5.1%; above MA20 by 5.6%; RSI14=77   |
|    9 | FTSE 100 / ^FTSE                    |  53.9 |   Yes    | —            | 20d up +0.8%; below MA20 by 0.1%; RSI14=52   |
|   13 | CAC 40 / ^FCHI                      |  49.7 |   Yes    | —            | 20d down -0.7%; below MA20 by 0.5%; RSI14=45 |
|   14 | S&P 500 / ^GSPC                     |  49.1 |   Yes    | —            | 20d down -0.8%; below MA20 by 0.4%; RSI14=50 |
|   15 | Euro Stoxx 50 / ^STOXX50E           |  49.1 |   Yes    | —            | 20d down -1.3%; below MA20 by 0.8%; RSI14=41 |
|   16 | Dow Jones Industrial Average / ^DJI |  47.9 |   Yes    | —            | 20d up +0.5%; below MA20 by 0.9%; RSI14=44   |
|   17 | DAX / ^GDAXI                        |  46.1 |   Yes    | —            | 20d down -1.2%; below MA20 by 0.9%; RSI14=47 |
|   18 | Russell 2000 / ^RUT                 |  41.8 |   Yes    | —            | 20d down -1.3%; below MA20 by 1.5%; RSI14=36 |
|   21 | NASDAQ 100 / ^NDX                   |  34.2 |   Yes    | —            | 20d down -5.9%; below MA20 by 2.9%; RSI14=38 |
|   33 | Nikkei 225 / ^N225                  |  20.9 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-07-17 |
| 7203.T    | 2026-07-17 |
| 8306.T    | 2026-07-17 |
| AAPL      | 2026-07-20 |
| AMZN      | 2026-07-20 |
| BZ=F      | 2026-07-20 |
| CL=F      | 2026-07-20 |
| GC=F      | 2026-07-20 |
| GOOGL     | 2026-07-20 |
| HG=F      | 2026-07-20 |
| JPM       | 2026-07-20 |
| META      | 2026-07-20 |
| MSFT      | 2026-07-20 |
| NG=F      | 2026-07-20 |
| NVDA      | 2026-07-20 |
| PL=F      | 2026-07-20 |
| SI=F      | 2026-07-20 |
| TSLA      | 2026-07-20 |
| UNH       | 2026-07-20 |
| XOM       | 2026-07-20 |
| ZC=F      | 2026-07-20 |
| ZS=F      | 2026-07-20 |
| ZW=F      | 2026-07-20 |
| ^DJI      | 2026-07-20 |
| ^FCHI     | 2026-07-20 |
| ^FTSE     | 2026-07-20 |
| ^GDAXI    | 2026-07-20 |
| ^GSPC     | 2026-07-20 |
| ^HSI      | 2026-07-20 |
| ^N225     | 2026-07-17 |
| ^NDX      | 2026-07-20 |
| ^RUT      | 2026-07-20 |
| ^STOXX50E | 2026-07-20 |

## Symbol Details

### Soybeans / ZS=F (score 78.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.8% |
| ret_5d     | +2.0% |
| ret_20d    | +9.2% |
| ret_60d    | +5.3% |
| ma20_dist  | +5.4% |
| ma50_dist  | +5.3% |
| vol_20d    | 20.6% |
| mdd_60d    |  8.8% |
| rsi_14     |  83.4 |
| zscore_20d |   1.5 |

### Wheat / ZW=F (score 74.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.3% |
| ret_5d     |  +7.5% |
| ret_20d    | +11.3% |
| ret_60d    | +12.5% |
| ma20_dist  |  +9.6% |
| ma50_dist  |  +9.4% |
| vol_20d    |  35.0% |
| mdd_60d    |  14.6% |
| rsi_14     |   82.7 |
| zscore_20d |    1.7 |

### Hang Seng / ^HSI (score 70.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.4% |
| ret_5d     | +3.8% |
| ret_20d    | +5.1% |
| ret_60d    | -5.1% |
| ma20_dist  | +5.6% |
| ma50_dist  | +1.6% |
| vol_20d    | 21.5% |
| mdd_60d    | 14.9% |
| rsi_14     |  77.3 |
| zscore_20d |   1.9 |

### Apple Inc. / AAPL (score 68.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.1% |
| ret_5d     |  +2.9% |
| ret_20d    |  +9.6% |
| ret_60d    | +19.7% |
| ma20_dist  |  +6.4% |
| ma50_dist  |  +7.6% |
| vol_20d    |  36.6% |
| mdd_60d    |  12.7% |
| rsi_14     |   82.1 |
| zscore_20d |    1.2 |

### Corn / ZC=F (score 63.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | +2.7% |
| ret_20d    | +7.7% |
| ret_60d    | -1.0% |
| ma20_dist  | +5.1% |
| ma50_dist  | +3.0% |
| vol_20d    | 28.0% |
| mdd_60d    | 15.7% |
| rsi_14     |  74.4 |
| zscore_20d |   1.5 |

### JPMorgan Chase & Co. / JPM (score 62.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | +1.3% |
| ret_20d    | +4.7% |
| ret_60d    | +8.7% |
| ma20_dist  | +1.1% |
| ma50_dist  | +6.7% |
| vol_20d    | 20.2% |
| mdd_60d    |  6.1% |
| rsi_14     |  60.5 |
| zscore_20d |   0.7 |

### Brent Crude Oil / BZ=F (score 61.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.3% |
| ret_5d     |  +7.1% |
| ret_20d    | +11.7% |
| ret_60d    | -12.5% |
| ma20_dist  | +14.6% |
| ma50_dist  |  +0.0% |
| vol_20d    |  51.1% |
| mdd_60d    |  39.4% |
| rsi_14     |   82.5 |
| zscore_20d |    2.0 |

### Microsoft Corporation / MSFT (score 58.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.2% |
| ret_5d     | +2.9% |
| ret_20d    | +6.0% |
| ret_60d    | -6.9% |
| ma20_dist  | +5.2% |
| ma50_dist  | +0.3% |
| vol_20d    | 35.7% |
| mdd_60d    | 23.4% |
| rsi_14     |  71.4 |
| zscore_20d |   1.6 |

### FTSE 100 / ^FTSE (score 53.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | +0.3% |
| ret_20d    | +0.8% |
| ret_60d    | +0.6% |
| ma20_dist  | -0.1% |
| ma50_dist  | +0.8% |
| vol_20d    |  9.6% |
| mdd_60d    |  2.6% |
| rsi_14     |  52.0 |
| zscore_20d |  -0.2 |

### UnitedHealth Group Inc. / UNH (score 52.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.1% |
| ret_5d     |  -1.8% |
| ret_20d    |  +5.1% |
| ret_60d    | +19.9% |
| ma20_dist  |  +0.1% |
| ma50_dist  |  +4.7% |
| vol_20d    |  24.9% |
| mdd_60d    |   6.1% |
| rsi_14     |   51.1 |
| zscore_20d |    0.0 |

### Meta Platforms Inc. / META (score 50.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.0% |
| ret_5d     |  -1.7% |
| ret_20d    | +11.9% |
| ret_60d    |  -4.2% |
| ma20_dist  |  +6.1% |
| ma50_dist  |  +6.8% |
| vol_20d    |  52.5% |
| mdd_60d    |  19.9% |
| rsi_14     |   65.8 |
| zscore_20d |    0.8 |

### Amazon.com Inc. / AMZN (score 50.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | +1.1% |
| ret_20d    | +2.3% |
| ret_60d    | -2.1% |
| ma20_dist  | +3.2% |
| ma50_dist  | -0.7% |
| vol_20d    | 30.1% |
| mdd_60d    | 17.4% |
| rsi_14     |  63.3 |
| zscore_20d |   1.1 |

### CAC 40 / ^FCHI (score 49.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.0% |
| ret_5d     | -0.3% |
| ret_20d    | -0.7% |
| ret_60d    | +2.2% |
| ma20_dist  | -0.5% |
| ma50_dist  | +0.8% |
| vol_20d    | 12.0% |
| mdd_60d    |  4.2% |
| rsi_14     |  45.2 |
| zscore_20d |  -0.7 |

### S&P 500 / ^GSPC (score 49.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | -1.0% |
| ret_20d    | -0.8% |
| ret_60d    | +4.3% |
| ma20_dist  | -0.4% |
| ma50_dist  | -0.3% |
| vol_20d    | 10.1% |
| mdd_60d    |  4.5% |
| rsi_14     |  50.3 |
| zscore_20d |  -0.5 |

### Euro Stoxx 50 / ^STOXX50E (score 49.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | -0.7% |
| ret_20d    | -1.3% |
| ret_60d    | +5.4% |
| ma20_dist  | -0.8% |
| ma50_dist  | +1.3% |
| vol_20d    | 14.0% |
| mdd_60d    |  3.6% |
| rsi_14     |  41.3 |
| zscore_20d |  -0.9 |

### Dow Jones Industrial Average / ^DJI (score 47.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | -1.3% |
| ret_20d    | +0.5% |
| ret_60d    | +4.7% |
| ma20_dist  | -0.9% |
| ma50_dist  | +1.1% |
| vol_20d    |  7.6% |
| mdd_60d    |  3.2% |
| rsi_14     |  44.3 |
| zscore_20d |  -1.2 |

### DAX / ^GDAXI (score 46.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | -1.1% |
| ret_20d    | -1.2% |
| ret_60d    | +3.0% |
| ma20_dist  | -0.9% |
| ma50_dist  | -0.1% |
| vol_20d    | 15.8% |
| mdd_60d    |  4.7% |
| rsi_14     |  46.9 |
| zscore_20d |  -0.7 |

### Russell 2000 / ^RUT (score 41.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | -0.4% |
| ret_20d    | -1.3% |
| ret_60d    | +5.6% |
| ma20_dist  | -1.5% |
| ma50_dist  | +0.7% |
| vol_20d    | 10.0% |
| mdd_60d    |  4.8% |
| rsi_14     |  35.9 |
| zscore_20d |  -1.9 |

### Alphabet Inc. Class A / GOOGL (score 38.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.5% |
| ret_5d     | -0.1% |
| ret_20d    | -4.4% |
| ret_60d    | +3.8% |
| ma20_dist  | -0.9% |
| ma50_dist  | -4.8% |
| vol_20d    | 36.0% |
| mdd_60d    | 16.2% |
| rsi_14     |  48.9 |
| zscore_20d |  -0.4 |

### NVIDIA Corporation / NVDA (score 38.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | -0.1% |
| ret_20d    | -3.5% |
| ret_60d    | +0.4% |
| ma20_dist  | +0.8% |
| ma50_dist  | -3.1% |
| vol_20d    | 36.5% |
| mdd_60d    | 18.3% |
| rsi_14     |  57.5 |
| zscore_20d |   0.3 |

### NASDAQ 100 / ^NDX (score 34.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.0% |
| ret_5d     | -2.3% |
| ret_20d    | -5.9% |
| ret_60d    | +6.2% |
| ma20_dist  | -2.9% |
| ma50_dist  | -3.2% |
| vol_20d    | 22.8% |
| mdd_60d    |  7.0% |
| rsi_14     |  38.0 |
| zscore_20d |  -1.9 |

### Gold / GC=F (score 31.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.1% |
| ret_5d     |  +0.3% |
| ret_20d    |  -5.1% |
| ret_60d    | -15.3% |
| ma20_dist  |  -1.4% |
| ma50_dist  |  -6.8% |
| vol_20d    |  22.0% |
| mdd_60d    |  15.6% |
| rsi_14     |   49.0 |
| zscore_20d |   -1.0 |

### Platinum / PL=F (score 22.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.8% |
| ret_5d     |  -0.6% |
| ret_20d    |  -6.6% |
| ret_60d    | -23.2% |
| ma20_dist  |  -1.3% |
| ma50_dist  | -10.8% |
| vol_20d    |  34.2% |
| mdd_60d    |  29.1% |
| rsi_14     |   52.6 |
| zscore_20d |   -0.7 |

### Natural Gas / NG=F (score 19.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.8% |
| ret_5d     |  -1.3% |
| ret_20d    | -11.5% |
| ret_60d    |  +5.1% |
| ma20_dist  |  -7.9% |
| ma50_dist  |  -7.3% |
| vol_20d    |  37.9% |
| mdd_60d    |  14.5% |
| rsi_14     |   30.1 |
| zscore_20d |   -1.5 |

### Silver / SI=F (score 17.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.4% |
| ret_5d     |  -1.4% |
| ret_20d    | -14.3% |
| ret_60d    | -27.1% |
| ma20_dist  |  -4.1% |
| ma50_dist  | -17.0% |
| vol_20d    |  43.1% |
| mdd_60d    |  37.1% |
| rsi_14     |   46.0 |
| zscore_20d |   -1.1 |

### Tesla Inc. / TSLA (score 10.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -3.0% |
| ret_5d     | -6.4% |
| ret_20d    | -7.7% |
| ret_60d    | -4.6% |
| ma20_dist  | -6.7% |
| ma50_dist  | -9.7% |
| vol_20d    | 58.6% |
| mdd_60d    | 17.0% |
| rsi_14     |  36.1 |
| zscore_20d |  -1.7 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Soybeans / ZS=F                     |  20.3036 |           1.7% |                 0.49x |       40.6071 |            3.3% |
| Wheat / ZW=F                        |  18.4821 |           2.7% |                 0.29x |       36.9643 |            5.5% |
| Hang Seng / ^HSI                    | 514.8863 |           2.0% |                 0.46x |     1029.7726 |            4.1% |
| Apple Inc. / AAPL                   |   8.3657 |           2.6% |                 0.27x |       16.7314 |            5.1% |
| Corn / ZC=F                         |  10.4286 |           2.3% |                 0.36x |       20.8571 |            4.6% |
| JPMorgan Chase & Co. / JPM          |   7.9678 |           2.4% |                 0.50x |       15.9355 |            4.7% |
| Brent Crude Oil / BZ=F              |   3.7064 |           4.2% |                 0.20x |        7.4129 |            8.3% |
| Microsoft Corporation / MSFT        |  10.9557 |           2.7% |                 0.28x |       21.9114 |            5.4% |
| FTSE 100 / ^FTSE                    | 117.4787 |           1.1% |                 1.04x |      234.9573 |            2.2% |
| UnitedHealth Group Inc. / UNH       |  12.8736 |           3.1% |                 0.40x |       25.7471 |            6.1% |
| Meta Platforms Inc. / META          |  30.4229 |           4.7% |                 0.19x |       60.8457 |            9.4% |
| Amazon.com Inc. / AMZN              |   6.7386 |           2.7% |                 0.33x |       13.4771 |            5.4% |
| CAC 40 / ^FCHI                      |  98.9194 |           1.2% |                 0.83x |      197.8387 |            2.4% |
| S&P 500 / ^GSPC                     |  72.3422 |           1.0% |                 0.99x |      144.6844 |            1.9% |
| Euro Stoxx 50 / ^STOXX50E           |  72.7528 |           1.2% |                 0.72x |      145.5055 |            2.3% |
| Dow Jones Industrial Average / ^DJI | 540.7377 |           1.0% |                 1.32x |     1081.4754 |            2.1% |
| DAX / ^GDAXI                        | 319.3411 |           1.3% |                 0.63x |      638.6822 |            2.6% |
| Russell 2000 / ^RUT                 |  38.0343 |           1.3% |                 1.00x |       76.0687 |            2.6% |
| Alphabet Inc. Class A / GOOGL       |  10.7771 |           3.1% |                 0.28x |       21.5543 |            6.1% |
| NVIDIA Corporation / NVDA           |   7.2814 |           3.6% |                 0.27x |       14.5629 |            7.2% |
| NASDAQ 100 / ^NDX                   | 578.2801 |           2.0% |                 0.44x |     1156.5603 |            4.0% |
| Gold / GC=F                         |  75.8714 |           1.9% |                 0.45x |      151.7429 |            3.8% |
| Platinum / PL=F                     |  32.3357 |           2.0% |                 0.29x |       64.6714 |            4.1% |
| Natural Gas / NG=F                  |   0.1196 |           4.2% |                 0.26x |        0.2393 |            8.4% |
| Silver / SI=F                       |   2.0281 |           3.6% |                 0.23x |        4.0561 |            7.1% |
| Tesla Inc. / TSLA                   |  17.4486 |           4.7% |                 0.17x |       34.8971 |            9.4% |

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

Scoring engine version: **1.0.0** | Git commit: **c154c40**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
