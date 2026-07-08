+++
title = "Market Analysis 2026-07-08"
date = "2026-07-08T00:00:00+00:00"
draft = false
summary = "Bullish market: 26 reliable instruments. Top signal: ZS=F (score 77.3)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-07-08.json", "data/history/2026-07-08.json"]
market_regime = "Bullish"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "1820d0d"
+++

## Market Regime

**Bullish** — 19 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Soybeans / ZS=F** — score 77.3, 20d return +6.7%, RSI14=74. 20d up +6.7%; above MA20 by 6.2%; RSI14=74
- **UnitedHealth Group Inc. / UNH** — score 77.0, 20d return +7.8%, RSI14=60. 20d up +7.8%; above MA20 by 3.8%; RSI14=60
- **JPMorgan Chase & Co. / JPM** — score 73.0, 20d return +9.1%, RSI14=69. 20d up +9.1%; above MA20 by 4.1%; RSI14=69 ⚠️ Upcoming: JPM earnings release (2026-07-14)
- **Dow Jones Industrial Average / ^DJI** — score 69.1, 20d return +4.0%, RSI14=73. 20d up +4.0%; above MA20 by 2.3%; RSI14=73
- **Corn / ZC=F** — score 67.9, 20d return +6.0%, RSI14=66. 20d up +6.0%; above MA20 by 6.0%; RSI14=66

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                | Applies To |
| ---------- | -------------------- | ---------- |
| 2026-07-14 | JPM earnings release | JPM        |

## Signal History

Compared with the previous available report (**2026-07-07**).
- **New top-5:** UNH, ZC=F, ^DJI
- **Persistent top signals:** JPM (2 reports), ZS=F (2 reports)
- **Dropped from top-5:** 8306.T, AAPL, ^GDAXI
- **6758.T risk gates:** added malformed_input, missing_bars; removed none
- **7203.T risk gates:** added malformed_input, missing_bars; removed none
- **8306.T risk gates:** added malformed_input, missing_bars; removed none
- **CL=F risk gates:** added malformed_input; removed none
- **HG=F risk gates:** added malformed_input; removed none
- **XOM risk gates:** added malformed_input; removed none
- **^N225 risk gates:** added missing_bars; removed none

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |    -13 |   +12.4 |
| 7203.T    |    -18 |    -0.3 |
| 8306.T    |    -26 |    +5.5 |
| AAPL      |     -3 |    -9.7 |
| AMZN      |     +6 |    +1.2 |
| BZ=F      |     +7 |    +7.6 |
| CL=F      |     +0 |    +7.0 |
| GC=F      |     +4 |    +0.9 |
| GOOGL     |     +1 |    -6.4 |
| HG=F      |     -7 |    +1.5 |
| JPM       |     +0 |    -0.6 |
| META      |    +10 |    +8.8 |
| MSFT      |     +9 |   +10.0 |
| NG=F      |    +10 |    +9.4 |
| NVDA      |     +5 |    +5.5 |
| PL=F      |     +8 |   +10.9 |
| SI=F      |     +2 |    -8.8 |
| TSLA      |     -9 |   -30.3 |
| UNH       |    +14 |   +21.8 |
| XOM       |     +0 |   +24.5 |
| ZC=F      |     +2 |    -1.2 |
| ZS=F      |     +1 |    +0.9 |
| ZW=F      |     +2 |    -0.6 |
| ^DJI      |     +2 |    -2.4 |
| ^FCHI     |     +5 |    -2.4 |
| ^FTSE     |     +7 |    +4.5 |
| ^GDAXI    |     -6 |   -13.9 |
| ^GSPC     |     -2 |    -8.5 |
| ^HSI      |     +3 |    -7.0 |
| ^N225     |    -13 |   -10.9 |
| ^NDX      |     +2 |   -15.4 |
| ^RUT      |     +1 |    -3.9 |
| ^STOXX50E |     -4 |   -10.0 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars
- **Copper / HG=F** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|    1 | Soybeans / ZS=F        |  77.3 |   Yes    | —               | 20d up +6.7%; above MA20 by 6.2%; RSI14=74    |
|    5 | Corn / ZC=F            |  67.9 |   Yes    | —               | 20d up +6.0%; above MA20 by 6.0%; RSI14=66    |
|    7 | Wheat / ZW=F           |  63.0 |   Yes    | —               | 20d up +5.0%; above MA20 by 3.1%; RSI14=58    |
|    9 | Natural Gas / NG=F     |  60.3 |   Yes    | —               | 20d up +1.1%; above MA20 by 2.0%; RSI14=56    |
|   22 | Gold / GC=F            |  29.1 |   Yes    | —               | 20d down -4.4%; below MA20 by 0.3%; RSI14=37  |
|   23 | Platinum / PL=F        |  26.7 |   Yes    | —               | 20d down -7.9%; below MA20 by 1.0%; RSI14=38  |
|   25 | Brent Crude Oil / BZ=F |  16.7 |   Yes    | —               | 20d down -20.3%; below MA20 by 6.7%; RSI14=29 |
|   26 | Silver / SI=F          |  13.3 |   Yes    | —               | 20d down -11.6%; below MA20 by 4.1%; RSI14=28 |
|   32 | Copper / HG=F          |  36.1 |    No    | malformed_input | Suppressed: malformed_input                   |
|   33 | WTI Crude Oil / CL=F   |  13.0 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    2 | UnitedHealth Group Inc. / UNH                                                  |  77.0 |   Yes    | —                             | 20d up +7.8%; above MA20 by 3.8%; RSI14=60   |
|    3 | JPMorgan Chase & Co. / JPM                                                     |  73.0 |   Yes    | —                             | 20d up +9.1%; above MA20 by 4.1%; RSI14=69   |
|    8 | Apple Inc. / AAPL                                                              |  62.7 |   Yes    | —                             | 20d up +1.1%; above MA20 by 5.3%; RSI14=60   |
|   11 | Meta Platforms Inc. / META                                                     |  57.9 |   Yes    | —                             | 20d up +3.9%; above MA20 by 6.8%; RSI14=55   |
|   16 | Alphabet Inc. Class A / GOOGL                                                  |  47.3 |   Yes    | —                             | 20d down -0.3%; above MA20 by 2.5%; RSI14=49 |
|   17 | Amazon.com Inc. / AMZN                                                         |  45.5 |   Yes    | —                             | 20d down -0.0%; above MA20 by 2.6%; RSI14=50 |
|   18 | Microsoft Corporation / MSFT                                                   |  36.1 |   Yes    | —                             | 20d down -6.7%; above MA20 by 1.4%; RSI14=45 |
|   19 | Tesla Inc. / TSLA                                                              |  32.7 |   Yes    | —                             | 20d up +3.0%; above MA20 by 0.8%; RSI14=48   |
|   24 | NVIDIA Corporation / NVDA                                                      |  26.4 |   Yes    | —                             | 20d down -4.0%; below MA20 by 2.5%; RSI14=33 |
|   27 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  82.4 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   28 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  68.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   29 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  60.6 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   30 | Exxon Mobil Corporation / XOM                                                  |  42.4 |    No    | malformed_input               | Suppressed: malformed_input                  |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    4 | Dow Jones Industrial Average / ^DJI |  69.1 |   Yes    | —            | 20d up +4.0%; above MA20 by 2.3%; RSI14=73   |
|    6 | FTSE 100 / ^FTSE                    |  63.3 |   Yes    | —            | 20d up +4.3%; above MA20 by 1.7%; RSI14=62   |
|   10 | DAX / ^GDAXI                        |  59.4 |   Yes    | —            | 20d up +4.2%; above MA20 by 2.0%; RSI14=59   |
|   12 | Euro Stoxx 50 / ^STOXX50E           |  55.1 |   Yes    | —            | 20d up +4.5%; above MA20 by 0.9%; RSI14=52   |
|   13 | Russell 2000 / ^RUT                 |  54.9 |   Yes    | —            | 20d up +5.3%; above MA20 by 0.7%; RSI14=53   |
|   14 | S&P 500 / ^GSPC                     |  52.1 |   Yes    | —            | 20d up +1.6%; above MA20 by 0.9%; RSI14=46   |
|   15 | CAC 40 / ^FCHI                      |  48.5 |   Yes    | —            | 20d up +2.8%; above MA20 by 0.5%; RSI14=50   |
|   20 | NASDAQ 100 / ^NDX                   |  31.5 |   Yes    | —            | 20d up +0.7%; below MA20 by 1.5%; RSI14=39   |
|   21 | Hang Seng / ^HSI                    |  29.4 |   Yes    | —            | 20d down -5.9%; below MA20 by 1.2%; RSI14=32 |
|   31 | Nikkei 225 / ^N225                  |  41.2 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-07-07 |
| 7203.T    | 2026-07-07 |
| 8306.T    | 2026-07-07 |
| AAPL      | 2026-07-07 |
| AMZN      | 2026-07-07 |
| BZ=F      | 2026-07-07 |
| CL=F      | 2026-07-07 |
| GC=F      | 2026-07-07 |
| GOOGL     | 2026-07-07 |
| HG=F      | 2026-07-07 |
| JPM       | 2026-07-07 |
| META      | 2026-07-07 |
| MSFT      | 2026-07-07 |
| NG=F      | 2026-07-07 |
| NVDA      | 2026-07-07 |
| PL=F      | 2026-07-07 |
| SI=F      | 2026-07-07 |
| TSLA      | 2026-07-07 |
| UNH       | 2026-07-07 |
| XOM       | 2026-07-07 |
| ZC=F      | 2026-07-07 |
| ZS=F      | 2026-07-07 |
| ZW=F      | 2026-07-07 |
| ^DJI      | 2026-07-07 |
| ^FCHI     | 2026-07-07 |
| ^FTSE     | 2026-07-07 |
| ^GDAXI    | 2026-07-07 |
| ^GSPC     | 2026-07-07 |
| ^HSI      | 2026-07-07 |
| ^N225     | 2026-07-07 |
| ^NDX      | 2026-07-07 |
| ^RUT      | 2026-07-07 |
| ^STOXX50E | 2026-07-07 |

## Symbol Details

### Soybeans / ZS=F (score 77.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.2% |
| ret_5d     | +7.9% |
| ret_20d    | +6.7% |
| ret_60d    | +2.7% |
| ma20_dist  | +6.2% |
| ma50_dist  | +3.1% |
| vol_20d    | 19.5% |
| mdd_60d    |  8.8% |
| rsi_14     |  73.6 |
| zscore_20d |   3.2 |

### UnitedHealth Group Inc. / UNH (score 77.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.4% |
| ret_5d     |  +2.0% |
| ret_20d    |  +7.8% |
| ret_60d    | +40.3% |
| ma20_dist  |  +3.8% |
| ma50_dist  |  +9.3% |
| vol_20d    |  25.0% |
| mdd_60d    |   6.1% |
| rsi_14     |   59.7 |
| zscore_20d |    1.8 |

### JPMorgan Chase & Co. / JPM (score 73.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | +3.4% |
| ret_20d    | +9.1% |
| ret_60d    | +9.8% |
| ma20_dist  | +4.1% |
| ma50_dist  | +8.6% |
| vol_20d    | 22.5% |
| mdd_60d    |  6.7% |
| rsi_14     |  69.2 |
| zscore_20d |   1.4 |

### Dow Jones Industrial Average / ^DJI (score 69.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | +1.4% |
| ret_20d    | +4.0% |
| ret_60d    | +9.8% |
| ma20_dist  | +2.3% |
| ma50_dist  | +4.4% |
| vol_20d    | 11.8% |
| mdd_60d    |  3.2% |
| rsi_14     |  72.9 |
| zscore_20d |   1.5 |

### Corn / ZC=F (score 67.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.4% |
| ret_5d     | +10.1% |
| ret_20d    |  +6.0% |
| ret_60d    |  -0.3% |
| ma20_dist  |  +6.0% |
| ma50_dist  |  +0.4% |
| vol_20d    |  23.8% |
| mdd_60d    |  15.7% |
| rsi_14     |   66.1 |
| zscore_20d |    2.6 |

### FTSE 100 / ^FTSE (score 63.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | +1.6% |
| ret_20d    | +4.3% |
| ret_60d    | +0.6% |
| ma20_dist  | +1.7% |
| ma50_dist  | +2.5% |
| vol_20d    | 10.0% |
| mdd_60d    |  4.4% |
| rsi_14     |  62.1 |
| zscore_20d |   1.6 |

### Wheat / ZW=F (score 63.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | +7.0% |
| ret_20d    | +5.0% |
| ret_60d    | +6.0% |
| ma20_dist  | +3.1% |
| ma50_dist  | -0.5% |
| vol_20d    | 22.0% |
| mdd_60d    | 14.6% |
| rsi_14     |  58.2 |
| zscore_20d |   1.7 |

### Apple Inc. / AAPL (score 62.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.6% |
| ret_5d     | +10.3% |
| ret_20d    |  +1.1% |
| ret_60d    | +19.4% |
| ma20_dist  |  +5.3% |
| ma50_dist  |  +5.3% |
| vol_20d    |  37.5% |
| mdd_60d    |  12.7% |
| rsi_14     |   59.5 |
| zscore_20d |    1.7 |

### Natural Gas / NG=F (score 60.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.6% |
| ret_5d     |  +2.6% |
| ret_20d    |  +1.1% |
| ret_60d    | +22.3% |
| ma20_dist  |  +2.0% |
| ma50_dist  |  +7.5% |
| vol_20d    |  36.2% |
| mdd_60d    |   7.5% |
| rsi_14     |   55.9 |
| zscore_20d |    1.0 |

### DAX / ^GDAXI (score 59.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.4% |
| ret_5d     | +1.9% |
| ret_20d    | +4.2% |
| ret_60d    | +7.3% |
| ma20_dist  | +2.0% |
| ma50_dist  | +2.9% |
| vol_20d    | 15.2% |
| mdd_60d    |  4.7% |
| rsi_14     |  59.3 |
| zscore_20d |   1.2 |

### Meta Platforms Inc. / META (score 57.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.5% |
| ret_5d     | +9.4% |
| ret_20d    | +3.9% |
| ret_60d    | -1.9% |
| ma20_dist  | +6.8% |
| ma50_dist  | +2.2% |
| vol_20d    | 50.2% |
| mdd_60d    | 21.1% |
| rsi_14     |  55.1 |
| zscore_20d |   2.0 |

### Euro Stoxx 50 / ^STOXX50E (score 55.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.2% |
| ret_5d     | -0.1% |
| ret_20d    | +4.5% |
| ret_60d    | +7.2% |
| ma20_dist  | +0.9% |
| ma50_dist  | +4.0% |
| vol_20d    | 14.2% |
| mdd_60d    |  4.9% |
| rsi_14     |  51.5 |
| zscore_20d |   0.6 |

### Russell 2000 / ^RUT (score 54.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.9% |
| ret_5d     |  -0.9% |
| ret_20d    |  +5.3% |
| ret_60d    | +13.1% |
| ma20_dist  |  +0.7% |
| ma50_dist  |  +3.1% |
| vol_20d    |  16.1% |
| mdd_60d    |   4.8% |
| rsi_14     |   53.1 |
| zscore_20d |    0.4 |

### S&P 500 / ^GSPC (score 52.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.4% |
| ret_5d     |  +0.9% |
| ret_20d    |  +1.6% |
| ret_60d    | +10.0% |
| ma20_dist  |  +0.9% |
| ma50_dist  |  +1.3% |
| vol_20d    |  14.5% |
| mdd_60d    |   4.5% |
| rsi_14     |   45.9 |
| zscore_20d |    0.9 |

### CAC 40 / ^FCHI (score 48.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | +0.4% |
| ret_20d    | +2.8% |
| ret_60d    | +2.4% |
| ma20_dist  | +0.5% |
| ma50_dist  | +2.5% |
| vol_20d    | 11.4% |
| mdd_60d    |  5.6% |
| rsi_14     |  50.4 |
| zscore_20d |   0.5 |

### Alphabet Inc. Class A / GOOGL (score 47.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.2% |
| ret_5d     |  +3.8% |
| ret_20d    |  -0.3% |
| ret_60d    | +15.3% |
| ma20_dist  |  +2.5% |
| ma50_dist  |  -1.3% |
| vol_20d    |  32.1% |
| mdd_60d    |  16.2% |
| rsi_14     |   48.6 |
| zscore_20d |    0.9 |

### Amazon.com Inc. / AMZN (score 45.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | +2.4% |
| ret_20d    | -0.0% |
| ret_60d    | +5.3% |
| ma20_dist  | +2.6% |
| ma50_dist  | -3.5% |
| vol_20d    | 34.3% |
| mdd_60d    | 17.4% |
| rsi_14     |  50.0 |
| zscore_20d |   1.2 |

### Microsoft Corporation / MSFT (score 36.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | +5.5% |
| ret_20d    | -6.7% |
| ret_60d    | +4.5% |
| ma20_dist  | +1.4% |
| ma50_dist  | -4.2% |
| vol_20d    | 37.2% |
| mdd_60d    | 23.4% |
| rsi_14     |  45.2 |
| zscore_20d |   0.4 |

### Tesla Inc. / TSLA (score 32.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -4.0% |
| ret_5d     |  -2.2% |
| ret_20d    |  +3.0% |
| ret_60d    | +16.6% |
| ma20_dist  |  +0.8% |
| ma50_dist  |  -1.2% |
| vol_20d    |  62.5% |
| mdd_60d    |  15.8% |
| rsi_14     |   47.7 |
| zscore_20d |    0.2 |

### NASDAQ 100 / ^NDX (score 31.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.8% |
| ret_5d     |  -2.0% |
| ret_20d    |  +0.7% |
| ret_60d    | +16.3% |
| ma20_dist  |  -1.5% |
| ma50_dist  |  -0.3% |
| vol_20d    |  29.6% |
| mdd_60d    |   7.0% |
| rsi_14     |   39.2 |
| zscore_20d |   -0.9 |

### Hang Seng / ^HSI (score 29.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | +2.0% |
| ret_20d    | -5.9% |
| ret_60d    | -9.3% |
| ma20_dist  | -1.2% |
| ma50_dist  | -6.0% |
| vol_20d    | 17.9% |
| mdd_60d    | 14.9% |
| rsi_14     |  31.7 |
| zscore_20d |  -0.4 |

### Gold / GC=F (score 29.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.2% |
| ret_5d     |  +3.1% |
| ret_20d    |  -4.4% |
| ret_60d    | -13.5% |
| ma20_dist  |  -0.3% |
| ma50_dist  |  -5.9% |
| vol_20d    |  28.3% |
| mdd_60d    |  17.9% |
| rsi_14     |   36.7 |
| zscore_20d |   -0.1 |

### Platinum / PL=F (score 26.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.2% |
| ret_5d     |  +4.9% |
| ret_20d    |  -7.9% |
| ret_60d    | -21.2% |
| ma20_dist  |  -1.0% |
| ma50_dist  | -10.8% |
| vol_20d    |  39.1% |
| mdd_60d    |  29.1% |
| rsi_14     |   38.3 |
| zscore_20d |   -0.2 |

### NVIDIA Corporation / NVDA (score 26.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | +1.0% |
| ret_20d    | -4.0% |
| ret_60d    | +7.1% |
| ma20_dist  | -2.5% |
| ma50_dist  | -6.0% |
| vol_20d    | 32.9% |
| mdd_60d    | 18.3% |
| rsi_14     |  33.5 |
| zscore_20d |  -0.8 |

### Brent Crude Oil / BZ=F (score 16.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +3.0% |
| ret_5d     |  +1.4% |
| ret_20d    | -20.3% |
| ret_60d    | -22.7% |
| ma20_dist  |  -6.7% |
| ma50_dist  | -21.2% |
| vol_20d    |  39.3% |
| mdd_60d    |  39.4% |
| rsi_14     |   28.9 |
| zscore_20d |   -0.7 |

### Silver / SI=F (score 13.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.6% |
| ret_5d     |  +4.7% |
| ret_20d    | -11.6% |
| ret_60d    | -20.1% |
| ma20_dist  |  -4.1% |
| ma50_dist  | -14.7% |
| vol_20d    |  50.2% |
| mdd_60d    |  34.7% |
| rsi_14     |   27.8 |
| zscore_20d |   -0.6 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Soybeans / ZS=F                     |  20.5714 |           1.7% |                 0.51x |       41.1429 |            3.4% |
| UnitedHealth Group Inc. / UNH       |  10.3171 |           2.4% |                 0.40x |       20.6343 |            4.8% |
| JPMorgan Chase & Co. / JPM          |   7.9072 |           2.3% |                 0.44x |       15.8144 |            4.7% |
| Dow Jones Industrial Average / ^DJI | 553.7213 |           1.0% |                 0.85x |     1107.4425 |            2.1% |
| Corn / ZC=F                         |   9.6250 |           2.2% |                 0.42x |       19.2500 |            4.4% |
| FTSE 100 / ^FTSE                    | 114.0428 |           1.1% |                 1.00x |      228.0857 |            2.1% |
| Wheat / ZW=F                        |  15.2143 |           2.5% |                 0.46x |       30.4286 |            5.0% |
| Apple Inc. / AAPL                   |   8.8243 |           2.8% |                 0.27x |       17.6486 |            5.7% |
| Natural Gas / NG=F                  |   0.1346 |           4.1% |                 0.28x |        0.2691 |            8.2% |
| DAX / ^GDAXI                        | 321.4114 |           1.3% |                 0.66x |      642.8228 |            2.5% |
| Meta Platforms Inc. / META          |  22.8650 |           3.7% |                 0.20x |       45.7300 |            7.4% |
| Euro Stoxx 50 / ^STOXX50E           |  69.2442 |           1.1% |                 0.71x |      138.4884 |            2.2% |
| Russell 2000 / ^RUT                 |  46.1315 |           1.5% |                 0.62x |       92.2629 |            3.1% |
| S&P 500 / ^GSPC                     |  88.2522 |           1.2% |                 0.69x |      176.5043 |            2.4% |
| CAC 40 / ^FCHI                      |  84.6257 |           1.0% |                 0.88x |      169.2514 |            2.0% |
| Alphabet Inc. Class A / GOOGL       |  11.7807 |           3.2% |                 0.31x |       23.5614 |            6.4% |
| Amazon.com Inc. / AMZN              |   8.2264 |           3.3% |                 0.29x |       16.4529 |            6.7% |
| Microsoft Corporation / MSFT        |  12.9971 |           3.3% |                 0.27x |       25.9943 |            6.7% |
| Tesla Inc. / TSLA                   |  20.3264 |           5.0% |                 0.16x |       40.6528 |           10.1% |
| NASDAQ 100 / ^NDX                   | 684.6685 |           2.3% |                 0.34x |     1369.3371 |            4.7% |
| Hang Seng / ^HSI                    | 457.6366 |           1.9% |                 0.56x |      915.2732 |            3.9% |
| Gold / GC=F                         |  84.9000 |           2.0% |                 0.35x |      169.7999 |            4.1% |
| Platinum / PL=F                     |  42.1929 |           2.6% |                 0.26x |       84.3857 |            5.1% |
| NVIDIA Corporation / NVDA           |   6.3179 |           3.2% |                 0.30x |       12.6357 |            6.4% |
| Brent Crude Oil / BZ=F              |   3.2743 |           4.4% |                 0.25x |        6.5486 |            8.8% |
| Silver / SI=F                       |   2.2167 |           3.6% |                 0.20x |        4.4334 |            7.3% |

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

Scoring engine version: **1.0.0** | Git commit: **1820d0d**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
