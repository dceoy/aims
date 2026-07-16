+++
title = "Market Analysis 2026-07-16"
date = "2026-07-16T00:00:00+00:00"
draft = false
summary = "Neutral market: 26 reliable instruments. Top signal: ZW=F (score 83.6)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-07-16.json", "data/history/2026-07-16.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "5bfd661"
+++

## Market Regime

**Neutral** — 16 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Wheat / ZW=F** — score 83.6, 20d return +14.9%, RSI14=77. 20d up +14.9%; above MA20 by 12.2%; RSI14=77
- **Apple Inc. / AAPL** — score 75.8, 20d return +10.5%, RSI14=70. 20d up +10.5%; above MA20 by 8.5%; RSI14=70
- **JPMorgan Chase & Co. / JPM** — score 73.9, 20d return +9.1%, RSI14=64. 20d up +9.1%; above MA20 by 4.1%; RSI14=64
- **Meta Platforms Inc. / META** — score 68.8, 20d return +14.8%, RSI14=73. 20d up +14.8%; above MA20 by 13.9%; RSI14=73
- **Corn / ZC=F** — score 64.5, 20d return +7.7%, RSI14=69. 20d up +7.7%; above MA20 by 5.6%; RSI14=69

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                        | Applies To               |
| ---------- | ---------------------------- | ------------------------ |
| 2026-07-22 | TSLA earnings release        | TSLA                     |
| 2026-07-23 | ECB monetary policy decision | ^FCHI, ^GDAXI, ^STOXX50E |
| 2026-07-23 | GOOGL earnings release       | GOOGL                    |

## Signal History

Compared with the previous available report (**2026-07-15**).
- **New top-5:** AAPL, JPM, ZC=F
- **Persistent top signals:** ZW=F (6 reports), META (2 reports)
- **Dropped from top-5:** ZS=F, ^FCHI, ^FTSE
- **AAPL risk gates:** added none; removed high_volatility, malformed_input
- **AMZN risk gates:** added none; removed high_volatility, malformed_input
- **GOOGL risk gates:** added none; removed high_volatility, malformed_input
- **JPM risk gates:** added none; removed high_volatility, malformed_input
- **MSFT risk gates:** added none; removed high_volatility, malformed_input
- **NVDA risk gates:** added none; removed high_volatility, malformed_input
- **TSLA risk gates:** added none; removed high_volatility, malformed_input
- **UNH risk gates:** added none; removed high_volatility, malformed_input
- **XOM risk gates:** added none; removed high_volatility
- **^DJI risk gates:** added none; removed high_volatility, malformed_input
- **^GSPC risk gates:** added none; removed high_volatility, malformed_input
- **^NDX risk gates:** added none; removed high_volatility, malformed_input

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |    -15 |   -27.0 |
| 7203.T    |    -11 |   -19.4 |
| 8306.T    |    -11 |    -5.5 |
| AAPL      |    +20 |   +65.2 |
| AMZN      |    +23 |   +55.5 |
| BZ=F      |     -6 |   -19.1 |
| CL=F      |    -13 |   -20.0 |
| GC=F      |    -12 |   -35.8 |
| GOOGL     |    +16 |   +46.1 |
| HG=F      |    -12 |   -27.3 |
| JPM       |    +29 |   +66.7 |
| META      |     -1 |    -8.8 |
| MSFT      |     +6 |   +32.1 |
| NG=F      |     -8 |   -28.2 |
| NVDA      |    +10 |   +40.0 |
| PL=F      |    -10 |   -32.1 |
| SI=F      |    -11 |   -42.4 |
| TSLA      |     -1 |    +8.2 |
| UNH       |    +12 |   +39.4 |
| XOM       |     +0 |   +38.5 |
| ZC=F      |     +5 |    -1.5 |
| ZS=F      |     -7 |   -20.6 |
| ZW=F      |     +1 |    +2.7 |
| ^DJI      |    +24 |   +53.0 |
| ^FCHI     |    -11 |   -23.0 |
| ^FTSE     |    -14 |   -24.6 |
| ^GDAXI    |    -14 |   -29.4 |
| ^GSPC     |    +24 |   +54.9 |
| ^HSI      |     -1 |   -13.9 |
| ^N225     |     -9 |   -13.9 |
| ^NDX      |     +9 |   +29.7 |
| ^RUT      |     -2 |   -15.8 |
| ^STOXX50E |    -10 |   -23.6 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Copper / HG=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **WTI Crude Oil / CL=F** — malformed_input
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|    1 | Wheat / ZW=F           |  83.6 |   Yes    | —               | 20d up +14.9%; above MA20 by 12.2%; RSI14=77  |
|    5 | Corn / ZC=F            |  64.5 |   Yes    | —               | 20d up +7.7%; above MA20 by 5.6%; RSI14=69    |
|    8 | Soybeans / ZS=F        |  60.9 |   Yes    | —               | 20d up +7.4%; above MA20 by 4.4%; RSI14=77    |
|   14 | Brent Crude Oil / BZ=F |  50.0 |   Yes    | —               | 20d up +2.1%; above MA20 by 10.8%; RSI14=72   |
|   22 | Natural Gas / NG=F     |  23.0 |   Yes    | —               | 20d down -7.1%; below MA20 by 7.3%; RSI14=34  |
|   23 | Platinum / PL=F        |  23.0 |   Yes    | —               | 20d down -7.8%; below MA20 by 0.3%; RSI14=56  |
|   24 | Gold / GC=F            |  19.4 |   Yes    | —               | 20d down -6.6%; below MA20 by 1.7%; RSI14=54  |
|   26 | Silver / SI=F          |   4.5 |   Yes    | —               | 20d down -18.5%; below MA20 by 6.6%; RSI14=47 |
|   29 | Copper / HG=F          |  46.4 |    No    | malformed_input | Suppressed: malformed_input                   |
|   32 | WTI Crude Oil / CL=F   |  43.9 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    2 | Apple Inc. / AAPL                                                              |  75.8 |   Yes    | —                             | 20d up +10.5%; above MA20 by 8.5%; RSI14=70  |
|    3 | JPMorgan Chase & Co. / JPM                                                     |  73.9 |   Yes    | —                             | 20d up +9.1%; above MA20 by 4.1%; RSI14=64   |
|    4 | Meta Platforms Inc. / META                                                     |  68.8 |   Yes    | —                             | 20d up +14.8%; above MA20 by 13.9%; RSI14=73 |
|    6 | Amazon.com Inc. / AMZN                                                         |  63.6 |   Yes    | —                             | 20d up +3.6%; above MA20 by 5.6%; RSI14=72   |
|   10 | Alphabet Inc. Class A / GOOGL                                                  |  55.5 |   Yes    | —                             | 20d up +0.4%; above MA20 by 3.7%; RSI14=68   |
|   13 | NVIDIA Corporation / NVDA                                                      |  50.3 |   Yes    | —                             | 20d up +0.0%; above MA20 by 5.1%; RSI14=62   |
|   15 | UnitedHealth Group Inc. / UNH                                                  |  48.5 |   Yes    | —                             | 20d up +1.8%; above MA20 by 0.1%; RSI14=57   |
|   19 | Microsoft Corporation / MSFT                                                   |  42.1 |   Yes    | —                             | 20d down -1.0%; above MA20 by 4.1%; RSI14=66 |
|   25 | Tesla Inc. / TSLA                                                              |  18.5 |   Yes    | —                             | 20d down -4.1%; below MA20 by 1.2%; RSI14=56 |
|   27 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  85.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   28 | Exxon Mobil Corporation / XOM                                                  |  47.6 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   31 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  44.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   33 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  41.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    7 | S&P 500 / ^GSPC                     |  62.7 |   Yes    | —            | 20d up +0.2%; above MA20 by 1.3%; RSI14=72   |
|    9 | Dow Jones Industrial Average / ^DJI |  60.0 |   Yes    | —            | 20d up +1.9%; above MA20 by 0.8%; RSI14=65   |
|   11 | Russell 2000 / ^RUT                 |  50.9 |   Yes    | —            | 20d up +0.4%; below MA20 by 0.3%; RSI14=48   |
|   12 | Hang Seng / ^HSI                    |  50.6 |   Yes    | —            | 20d down -0.7%; above MA20 by 4.1%; RSI14=68 |
|   16 | CAC 40 / ^FCHI                      |  46.7 |   Yes    | —            | 20d down -0.6%; below MA20 by 0.1%; RSI14=47 |
|   17 | Euro Stoxx 50 / ^STOXX50E           |  46.1 |   Yes    | —            | 20d down -0.5%; below MA20 by 0.4%; RSI14=50 |
|   18 | FTSE 100 / ^FTSE                    |  45.5 |   Yes    | —            | 20d up +0.1%; above MA20 by 0.0%; RSI14=49   |
|   20 | DAX / ^GDAXI                        |  40.3 |   Yes    | —            | 20d up +0.3%; below MA20 by 0.4%; RSI14=50   |
|   21 | NASDAQ 100 / ^NDX                   |  37.9 |   Yes    | —            | 20d down -3.4%; below MA20 by 0.5%; RSI14=53 |
|   30 | Nikkei 225 / ^N225                  |  44.9 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-07-15 |
| 7203.T    | 2026-07-15 |
| 8306.T    | 2026-07-15 |
| AAPL      | 2026-07-15 |
| AMZN      | 2026-07-15 |
| BZ=F      | 2026-07-15 |
| CL=F      | 2026-07-15 |
| GC=F      | 2026-07-15 |
| GOOGL     | 2026-07-15 |
| HG=F      | 2026-07-15 |
| JPM       | 2026-07-15 |
| META      | 2026-07-15 |
| MSFT      | 2026-07-15 |
| NG=F      | 2026-07-15 |
| NVDA      | 2026-07-15 |
| PL=F      | 2026-07-15 |
| SI=F      | 2026-07-15 |
| TSLA      | 2026-07-15 |
| UNH       | 2026-07-15 |
| XOM       | 2026-07-15 |
| ZC=F      | 2026-07-15 |
| ZS=F      | 2026-07-15 |
| ZW=F      | 2026-07-15 |
| ^DJI      | 2026-07-15 |
| ^FCHI     | 2026-07-15 |
| ^FTSE     | 2026-07-15 |
| ^GDAXI    | 2026-07-15 |
| ^GSPC     | 2026-07-15 |
| ^HSI      | 2026-07-15 |
| ^N225     | 2026-07-15 |
| ^NDX      | 2026-07-15 |
| ^RUT      | 2026-07-15 |
| ^STOXX50E | 2026-07-15 |

## Symbol Details

### Wheat / ZW=F (score 83.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +7.3% |
| ret_5d     | +13.0% |
| ret_20d    | +14.9% |
| ret_60d    | +14.6% |
| ma20_dist  | +12.2% |
| ma50_dist  | +10.6% |
| vol_20d    |  35.6% |
| mdd_60d    |  14.6% |
| rsi_14     |   77.4 |
| zscore_20d |    3.1 |

### Apple Inc. / AAPL (score 75.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +4.0% |
| ret_5d     |  +4.5% |
| ret_20d    | +10.5% |
| ret_60d    | +21.3% |
| ma20_dist  |  +8.5% |
| ma50_dist  |  +9.0% |
| vol_20d    |  35.6% |
| mdd_60d    |  12.7% |
| rsi_14     |   70.2 |
| zscore_20d |    1.9 |

### JPMorgan Chase & Co. / JPM (score 73.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.2% |
| ret_5d     |  +4.9% |
| ret_20d    |  +9.1% |
| ret_60d    | +12.3% |
| ma20_dist  |  +4.1% |
| ma50_dist  |  +9.9% |
| vol_20d    |  24.5% |
| mdd_60d    |   6.7% |
| rsi_14     |   64.3 |
| zscore_20d |    2.5 |

### Meta Platforms Inc. / META (score 68.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +3.1% |
| ret_5d     | +13.0% |
| ret_20d    | +14.8% |
| ret_60d    |  -1.0% |
| ma20_dist  | +13.9% |
| ma50_dist  | +13.1% |
| vol_20d    |  54.4% |
| mdd_60d    |  19.9% |
| rsi_14     |   73.5 |
| zscore_20d |    2.0 |

### Corn / ZC=F (score 64.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +3.2% |
| ret_5d     | +2.9% |
| ret_20d    | +7.7% |
| ret_60d    | -0.3% |
| ma20_dist  | +5.6% |
| ma50_dist  | +2.2% |
| vol_20d    | 28.1% |
| mdd_60d    | 15.7% |
| rsi_14     |  69.5 |
| zscore_20d |   1.8 |

### Amazon.com Inc. / AMZN (score 63.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +3.0% |
| ret_5d     | +4.7% |
| ret_20d    | +3.6% |
| ret_60d    | +1.8% |
| ma20_dist  | +5.6% |
| ma50_dist  | +0.7% |
| vol_20d    | 32.8% |
| mdd_60d    | 17.4% |
| rsi_14     |  72.0 |
| zscore_20d |   2.1 |

### S&P 500 / ^GSPC (score 62.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | +1.2% |
| ret_20d    | +0.2% |
| ret_60d    | +6.3% |
| ma20_dist  | +1.3% |
| ma50_dist  | +1.6% |
| vol_20d    | 11.1% |
| mdd_60d    |  4.5% |
| rsi_14     |  72.1 |
| zscore_20d |   1.4 |

### Soybeans / ZS=F (score 60.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | +0.6% |
| ret_20d    | +7.4% |
| ret_60d    | +3.0% |
| ma20_dist  | +4.4% |
| ma50_dist  | +3.3% |
| vol_20d    | 20.2% |
| mdd_60d    |  8.8% |
| rsi_14     |  76.7 |
| zscore_20d |   1.4 |

### Dow Jones Industrial Average / ^DJI (score 60.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +0.6% |
| ret_20d    | +1.9% |
| ret_60d    | +6.5% |
| ma20_dist  | +0.8% |
| ma50_dist  | +3.1% |
| vol_20d    |  7.8% |
| mdd_60d    |  3.2% |
| rsi_14     |  65.5 |
| zscore_20d |   0.9 |

### Alphabet Inc. Class A / GOOGL (score 55.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +3.2% |
| ret_5d     | +2.5% |
| ret_20d    | +0.4% |
| ret_60d    | +8.6% |
| ma20_dist  | +3.7% |
| ma50_dist  | -0.3% |
| vol_20d    | 32.9% |
| mdd_60d    | 16.2% |
| rsi_14     |  67.5 |
| zscore_20d |   1.4 |

### Russell 2000 / ^RUT (score 50.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | +0.7% |
| ret_20d    | +0.4% |
| ret_60d    | +7.2% |
| ma20_dist  | -0.3% |
| ma50_dist  | +2.1% |
| vol_20d    | 12.9% |
| mdd_60d    |  4.8% |
| rsi_14     |  47.8 |
| zscore_20d |  -0.3 |

### Hang Seng / ^HSI (score 50.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.4% |
| ret_5d     | +2.0% |
| ret_20d    | -0.7% |
| ret_60d    | -6.5% |
| ma20_dist  | +4.1% |
| ma50_dist  | -0.5% |
| vol_20d    | 20.3% |
| mdd_60d    | 14.9% |
| rsi_14     |  67.5 |
| zscore_20d |   1.7 |

### NVIDIA Corporation / NVDA (score 50.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +4.1% |
| ret_20d    | +0.0% |
| ret_60d    | +5.4% |
| ma20_dist  | +5.1% |
| ma50_dist  | +1.4% |
| vol_20d    | 37.5% |
| mdd_60d    | 18.3% |
| rsi_14     |  62.4 |
| zscore_20d |   1.6 |

### Brent Crude Oil / BZ=F (score 50.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.3% |
| ret_5d     |  +8.9% |
| ret_20d    |  +2.1% |
| ret_60d    |  -6.0% |
| ma20_dist  | +10.8% |
| ma50_dist  |  -6.1% |
| vol_20d    |  52.3% |
| mdd_60d    |  39.4% |
| rsi_14     |   72.5 |
| zscore_20d |    2.0 |

### UnitedHealth Group Inc. / UNH (score 48.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.6% |
| ret_5d     |  -1.7% |
| ret_20d    |  +1.8% |
| ret_60d    | +29.7% |
| ma20_dist  |  +0.1% |
| ma50_dist  |  +4.8% |
| vol_20d    |  25.7% |
| mdd_60d    |   6.1% |
| rsi_14     |   56.7 |
| zscore_20d |    0.0 |

### CAC 40 / ^FCHI (score 46.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | +1.6% |
| ret_20d    | -0.6% |
| ret_60d    | +1.8% |
| ma20_dist  | -0.1% |
| ma50_dist  | +1.5% |
| vol_20d    | 12.2% |
| mdd_60d    |  4.2% |
| rsi_14     |  46.6 |
| zscore_20d |  -0.2 |

### Euro Stoxx 50 / ^STOXX50E (score 46.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | +1.0% |
| ret_20d    | -0.5% |
| ret_60d    | +3.4% |
| ma20_dist  | -0.4% |
| ma50_dist  | +2.3% |
| vol_20d    | 13.8% |
| mdd_60d    |  3.7% |
| rsi_14     |  49.9 |
| zscore_20d |  -0.4 |

### FTSE 100 / ^FTSE (score 45.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | +0.3% |
| ret_20d    | +0.1% |
| ret_60d    | -0.9% |
| ma20_dist  | +0.0% |
| ma50_dist  | +0.9% |
| vol_20d    | 10.2% |
| mdd_60d    |  2.9% |
| rsi_14     |  48.8 |
| zscore_20d |   0.0 |

### Microsoft Corporation / MSFT (score 42.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.8% |
| ret_5d     | +3.2% |
| ret_20d    | -1.0% |
| ret_60d    | -6.2% |
| ma20_dist  | +4.1% |
| ma50_dist  | -1.6% |
| vol_20d    | 37.2% |
| mdd_60d    | 23.4% |
| rsi_14     |  65.9 |
| zscore_20d |   1.5 |

### DAX / ^GDAXI (score 40.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | +0.4% |
| ret_20d    | +0.3% |
| ret_60d    | +3.0% |
| ma20_dist  | -0.4% |
| ma50_dist  | +0.6% |
| vol_20d    | 16.0% |
| mdd_60d    |  4.7% |
| rsi_14     |  50.1 |
| zscore_20d |  -0.3 |

### NASDAQ 100 / ^NDX (score 37.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.3% |
| ret_5d     |  +0.9% |
| ret_20d    |  -3.4% |
| ret_60d    | +10.6% |
| ma20_dist  |  -0.5% |
| ma50_dist  |  -0.0% |
| vol_20d    |  24.7% |
| mdd_60d    |   7.0% |
| rsi_14     |   52.7 |
| zscore_20d |   -0.4 |

### Natural Gas / NG=F (score 23.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | -9.0% |
| ret_20d    | -7.1% |
| ret_60d    | +9.3% |
| ma20_dist  | -7.3% |
| ma50_dist  | -5.1% |
| vol_20d    | 40.7% |
| mdd_60d    | 13.3% |
| rsi_14     |  33.9 |
| zscore_20d |  -1.7 |

### Platinum / PL=F (score 23.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.0% |
| ret_5d     |  +3.5% |
| ret_20d    |  -7.8% |
| ret_60d    | -23.2% |
| ma20_dist  |  -0.3% |
| ma50_dist  |  -9.8% |
| vol_20d    |  38.6% |
| mdd_60d    |  29.1% |
| rsi_14     |   56.4 |
| zscore_20d |   -0.1 |

### Gold / GC=F (score 19.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.4% |
| ret_5d     |  -0.7% |
| ret_20d    |  -6.6% |
| ret_60d    | -16.7% |
| ma20_dist  |  -1.7% |
| ma50_dist  |  -6.8% |
| vol_20d    |  23.8% |
| mdd_60d    |  17.0% |
| rsi_14     |   54.2 |
| zscore_20d |   -0.7 |

### Tesla Inc. / TSLA (score 18.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | +0.1% |
| ret_20d    | -4.1% |
| ret_60d    | -1.5% |
| ma20_dist  | -1.2% |
| ma50_dist  | -3.8% |
| vol_20d    | 57.9% |
| mdd_60d    | 15.8% |
| rsi_14     |  55.8 |
| zscore_20d |  -0.3 |

### Silver / SI=F (score 4.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.8% |
| ret_5d     |  -1.8% |
| ret_20d    | -18.5% |
| ret_60d    | -30.1% |
| ma20_dist  |  -6.6% |
| ma50_dist  | -17.9% |
| vol_20d    |  46.7% |
| mdd_60d    |  35.8% |
| rsi_14     |   47.3 |
| zscore_20d |   -1.1 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Wheat / ZW=F                        |  16.6607 |           2.5% |                 0.28x |       33.3214 |            4.9% |
| Apple Inc. / AAPL                   |   9.4836 |           2.9% |                 0.28x |       18.9672 |            5.8% |
| JPMorgan Chase & Co. / JPM          |   7.8093 |           2.3% |                 0.41x |       15.6186 |            4.5% |
| Meta Platforms Inc. / META          |  28.7814 |           4.2% |                 0.18x |       57.5629 |            8.4% |
| Corn / ZC=F                         |  10.6964 |           2.4% |                 0.36x |       21.3929 |            4.8% |
| Amazon.com Inc. / AMZN              |   7.5329 |           3.0% |                 0.31x |       15.0657 |            5.9% |
| S&P 500 / ^GSPC                     |  75.6422 |           1.0% |                 0.90x |      151.2844 |            2.0% |
| Soybeans / ZS=F                     |  19.9821 |           1.7% |                 0.50x |       39.9643 |            3.3% |
| Dow Jones Industrial Average / ^DJI | 536.8767 |           1.0% |                 1.29x |     1073.7533 |            2.0% |
| Alphabet Inc. Class A / GOOGL       |  10.3393 |           2.8% |                 0.30x |       20.6786 |            5.6% |
| Russell 2000 / ^RUT                 |  39.1222 |           1.3% |                 0.78x |       78.2444 |            2.6% |
| Hang Seng / ^HSI                    | 481.7513 |           2.0% |                 0.49x |      963.5025 |            3.9% |
| NVIDIA Corporation / NVDA           |   7.1407 |           3.4% |                 0.27x |       14.2814 |            6.7% |
| Brent Crude Oil / BZ=F              |   3.4850 |           4.1% |                 0.19x |        6.9700 |            8.2% |
| UnitedHealth Group Inc. / UNH       |  10.4043 |           2.5% |                 0.39x |       20.8086 |            5.0% |
| CAC 40 / ^FCHI                      |  93.5714 |           1.1% |                 0.82x |      187.1429 |            2.2% |
| Euro Stoxx 50 / ^STOXX50E           |  73.2720 |           1.2% |                 0.72x |      146.5440 |            2.3% |
| FTSE 100 / ^FTSE                    | 117.1643 |           1.1% |                 0.98x |      234.3285 |            2.2% |
| Microsoft Corporation / MSFT        |  12.4886 |           3.2% |                 0.27x |       24.9771 |            6.3% |
| DAX / ^GDAXI                        | 336.2755 |           1.3% |                 0.63x |      672.5511 |            2.7% |
| NASDAQ 100 / ^NDX                   | 603.3789 |           2.0% |                 0.41x |     1206.7578 |            4.1% |
| Natural Gas / NG=F                  |   0.1374 |           4.7% |                 0.25x |        0.2749 |            9.4% |
| Platinum / PL=F                     |  34.9714 |           2.1% |                 0.26x |       69.9429 |            4.3% |
| Gold / GC=F                         |  77.7929 |           1.9% |                 0.42x |      155.5858 |            3.8% |
| Tesla Inc. / TSLA                   |  18.8814 |           4.8% |                 0.17x |       37.7629 |            9.6% |
| Silver / SI=F                       |   1.9705 |           3.5% |                 0.21x |        3.9410 |            6.9% |

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

Scoring engine version: **1.0.0** | Git commit: **5bfd661**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
