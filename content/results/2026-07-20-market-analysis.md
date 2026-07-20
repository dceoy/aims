+++
title = "Market Analysis 2026-07-20"
date = "2026-07-20T00:00:00+00:00"
draft = false
summary = "Neutral market: 26 reliable instruments. Top signal: ZW=F (score 82.7)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-07-20.json", "data/history/2026-07-20.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "48d3eec"
+++

## Market Regime

**Neutral** — 13 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Wheat / ZW=F** — score 82.7, 20d return +11.4%, RSI14=83. 20d up +11.4%; above MA20 by 11.7%; RSI14=83
- **Apple Inc. / AAPL** — score 79.1, 20d return +12.8%, RSI14=89. 20d up +12.8%; above MA20 by 9.2%; RSI14=89
- **Soybeans / ZS=F** — score 71.2, 20d return +6.4%, RSI14=73. 20d up +6.4%; above MA20 by 4.0%; RSI14=73
- **JPMorgan Chase & Co. / JPM** — score 66.4, 20d return +2.8%, RSI14=63. 20d up +2.8%; above MA20 by 2.0%; RSI14=63
- **FTSE 100 / ^FTSE** — score 64.5, 20d return +2.3%, RSI14=59. 20d up +2.3%; above MA20 by 0.6%; RSI14=59

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                        | Applies To               |
| ---------- | ---------------------------- | ------------------------ |
| 2026-07-22 | GOOGL earnings release       | GOOGL                    |
| 2026-07-22 | TSLA earnings release        | TSLA                     |
| 2026-07-23 | ECB monetary policy decision | ^FCHI, ^GDAXI, ^STOXX50E |

## Signal History

Compared with the previous available report (**2026-07-19**).
- **New top-5:** ^FTSE
- **Persistent top signals:** ZW=F (10 reports), AAPL (5 reports), JPM (5 reports), ZS=F (4 reports)
- **Dropped from top-5:** ZC=F
- **GC=F risk gates:** added none; removed malformed_input
- **SI=F risk gates:** added none; removed malformed_input

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     -2 |    +1.2 |
| 7203.T    |     -2 |    +0.6 |
| 8306.T    |     -2 |    +1.2 |
| AAPL      |     +0 |    +0.9 |
| AMZN      |     +0 |    +0.6 |
| BZ=F      |     +0 |    +0.3 |
| CL=F      |     -2 |    +2.7 |
| GC=F      |     +9 |    -1.5 |
| GOOGL     |     -1 |    +0.3 |
| HG=F      |     -2 |    -4.2 |
| JPM       |     +1 |    +0.3 |
| META      |     +1 |    +0.9 |
| MSFT      |     +0 |    +0.6 |
| NG=F      |     +0 |    +0.6 |
| NVDA      |     +0 |    +0.3 |
| PL=F      |     -1 |    -2.4 |
| SI=F      |     +7 |    -1.2 |
| TSLA      |     -1 |    +0.9 |
| UNH       |     +1 |    +0.9 |
| XOM       |     -2 |    +1.2 |
| ZC=F      |     -4 |   -12.7 |
| ZS=F      |     +1 |    +2.1 |
| ZW=F      |     +0 |    +0.3 |
| ^DJI      |     +0 |    +0.3 |
| ^FCHI     |     +1 |    +0.9 |
| ^FTSE     |     +1 |    +0.9 |
| ^GDAXI    |     -1 |    +0.3 |
| ^GSPC     |     +0 |    +0.6 |
| ^HSI      |     +0 |    +0.9 |
| ^N225     |     -1 |    +0.0 |
| ^NDX      |     +0 |    +0.9 |
| ^RUT      |     -2 |    +0.3 |
| ^STOXX50E |     +1 |    +0.9 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **WTI Crude Oil / CL=F** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|    1 | Wheat / ZW=F           |  82.7 |   Yes    | —               | 20d up +11.4%; above MA20 by 11.7%; RSI14=83  |
|    3 | Soybeans / ZS=F        |  71.2 |   Yes    | —               | 20d up +6.4%; above MA20 by 4.0%; RSI14=73    |
|    7 | Corn / ZC=F            |  63.0 |   Yes    | —               | 20d up +5.6%; above MA20 by 4.4%; RSI14=65    |
|    8 | Brent Crude Oil / BZ=F |  62.1 |   Yes    | —               | 20d up +10.7%; above MA20 by 13.9%; RSI14=83  |
|   20 | Natural Gas / NG=F     |  30.6 |   Yes    | —               | 20d down -7.4%; below MA20 by 6.8%; RSI14=30  |
|   22 | Gold / GC=F            |  26.7 |   Yes    | —               | 20d down -7.9%; below MA20 by 1.6%; RSI14=45  |
|   24 | Platinum / PL=F        |  18.5 |   Yes    | —               | 20d down -10.3%; below MA20 by 0.8%; RSI14=47 |
|   26 | Silver / SI=F          |  11.2 |   Yes    | —               | 20d down -20.7%; below MA20 by 6.2%; RSI14=41 |
|   30 | WTI Crude Oil / CL=F   |  60.3 |    No    | malformed_input | Suppressed: malformed_input                   |
|   32 | Copper / HG=F          |  43.9 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    2 | Apple Inc. / AAPL                                                              |  79.1 |   Yes    | —                             | 20d up +12.8%; above MA20 by 9.2%; RSI14=89  |
|    4 | JPMorgan Chase & Co. / JPM                                                     |  66.4 |   Yes    | —                             | 20d up +2.8%; above MA20 by 2.0%; RSI14=63   |
|    6 | UnitedHealth Group Inc. / UNH                                                  |  64.2 |   Yes    | —                             | 20d up +6.6%; above MA20 by 1.4%; RSI14=49   |
|   15 | Amazon.com Inc. / AMZN                                                         |  47.6 |   Yes    | —                             | 20d up +4.1%; above MA20 by 2.1%; RSI14=67   |
|   16 | Meta Platforms Inc. / META                                                     |  47.0 |   Yes    | —                             | 20d up +13.8%; above MA20 by 6.7%; RSI14=67  |
|   18 | Microsoft Corporation / MSFT                                                   |  44.9 |   Yes    | —                             | 20d up +3.9%; above MA20 by 3.3%; RSI14=64   |
|   21 | NVIDIA Corporation / NVDA                                                      |  30.3 |   Yes    | —                             | 20d down -0.9%; above MA20 by 0.3%; RSI14=59 |
|   23 | Alphabet Inc. Class A / GOOGL                                                  |  25.8 |   Yes    | —                             | 20d down -4.7%; below MA20 by 2.6%; RSI14=55 |
|   25 | Tesla Inc. / TSLA                                                              |  16.7 |   Yes    | —                             | 20d down -3.9%; below MA20 by 4.3%; RSI14=50 |
|   27 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  69.7 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   28 | Exxon Mobil Corporation / XOM                                                  |  66.4 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   29 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  61.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   31 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  54.5 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    5 | FTSE 100 / ^FTSE                    |  64.5 |   Yes    | —            | 20d up +2.3%; above MA20 by 0.6%; RSI14=59   |
|    9 | Dow Jones Industrial Average / ^DJI |  56.7 |   Yes    | —            | 20d up +1.3%; below MA20 by 0.3%; RSI14=54   |
|   10 | Hang Seng / ^HSI                    |  55.8 |   Yes    | —            | 20d up +1.0%; above MA20 by 3.5%; RSI14=76   |
|   11 | S&P 500 / ^GSPC                     |  52.1 |   Yes    | —            | 20d up +0.5%; below MA20 by 0.3%; RSI14=59   |
|   12 | Euro Stoxx 50 / ^STOXX50E           |  49.4 |   Yes    | —            | 20d down -1.0%; below MA20 by 0.8%; RSI14=50 |
|   13 | CAC 40 / ^FCHI                      |  48.8 |   Yes    | —            | 20d down -1.0%; below MA20 by 0.6%; RSI14=48 |
|   14 | Russell 2000 / ^RUT                 |  48.8 |   Yes    | —            | 20d up +1.5%; below MA20 by 0.9%; RSI14=39   |
|   17 | DAX / ^GDAXI                        |  47.0 |   Yes    | —            | 20d down -0.6%; below MA20 by 1.0%; RSI14=54 |
|   19 | NASDAQ 100 / ^NDX                   |  32.4 |   Yes    | —            | 20d down -3.6%; below MA20 by 3.2%; RSI14=45 |
|   33 | Nikkei 225 / ^N225                  |  20.6 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-07-17 |
| 7203.T    | 2026-07-17 |
| 8306.T    | 2026-07-17 |
| AAPL      | 2026-07-17 |
| AMZN      | 2026-07-17 |
| BZ=F      | 2026-07-17 |
| CL=F      | 2026-07-17 |
| GC=F      | 2026-07-17 |
| GOOGL     | 2026-07-17 |
| HG=F      | 2026-07-17 |
| JPM       | 2026-07-17 |
| META      | 2026-07-17 |
| MSFT      | 2026-07-17 |
| NG=F      | 2026-07-17 |
| NVDA      | 2026-07-17 |
| PL=F      | 2026-07-17 |
| SI=F      | 2026-07-17 |
| TSLA      | 2026-07-17 |
| UNH       | 2026-07-17 |
| XOM       | 2026-07-17 |
| ZC=F      | 2026-07-17 |
| ZS=F      | 2026-07-17 |
| ZW=F      | 2026-07-17 |
| ^DJI      | 2026-07-17 |
| ^FCHI     | 2026-07-17 |
| ^FTSE     | 2026-07-17 |
| ^GDAXI    | 2026-07-17 |
| ^GSPC     | 2026-07-17 |
| ^HSI      | 2026-07-17 |
| ^N225     | 2026-07-17 |
| ^NDX      | 2026-07-17 |
| ^RUT      | 2026-07-17 |
| ^STOXX50E | 2026-07-17 |

## Symbol Details

### Wheat / ZW=F (score 82.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.2% |
| ret_5d     |  +8.0% |
| ret_20d    | +11.4% |
| ret_60d    | +12.9% |
| ma20_dist  | +11.7% |
| ma50_dist  | +11.0% |
| vol_20d    |  34.9% |
| mdd_60d    |  14.6% |
| rsi_14     |   82.7 |
| zscore_20d |    2.2 |

### Apple Inc. / AAPL (score 79.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.1% |
| ret_5d     |  +5.8% |
| ret_20d    | +12.8% |
| ret_60d    | +25.5% |
| ma20_dist  |  +9.2% |
| ma50_dist  | +10.3% |
| vol_20d    |  35.4% |
| mdd_60d    |  12.7% |
| rsi_14     |   88.6 |
| zscore_20d |    1.7 |

### Soybeans / ZS=F (score 71.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.8% |
| ret_5d     | +0.7% |
| ret_20d    | +6.4% |
| ret_60d    | +2.6% |
| ma20_dist  | +4.0% |
| ma50_dist  | +3.5% |
| vol_20d    | 20.4% |
| mdd_60d    |  8.8% |
| rsi_14     |  72.8 |
| zscore_20d |   1.2 |

### JPMorgan Chase & Co. / JPM (score 66.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | +1.4% |
| ret_20d    | +2.8% |
| ret_60d    | +9.5% |
| ma20_dist  | +2.0% |
| ma50_dist  | +7.6% |
| vol_20d    | 22.1% |
| mdd_60d    |  6.1% |
| rsi_14     |  63.4 |
| zscore_20d |   1.1 |

### FTSE 100 / ^FTSE (score 64.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +1.0% |
| ret_20d    | +2.3% |
| ret_60d    | +1.2% |
| ma20_dist  | +0.6% |
| ma50_dist  | +1.6% |
| vol_20d    |  9.5% |
| mdd_60d    |  2.6% |
| rsi_14     |  59.3 |
| zscore_20d |   0.9 |

### UnitedHealth Group Inc. / UNH (score 64.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.6% |
| ret_5d     |  +0.3% |
| ret_20d    |  +6.6% |
| ret_60d    | +23.8% |
| ma20_dist  |  +1.4% |
| ma50_dist  |  +6.1% |
| vol_20d    |  24.4% |
| mdd_60d    |   6.1% |
| rsi_14     |   48.9 |
| zscore_20d |    0.7 |

### Corn / ZC=F (score 63.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | +1.5% |
| ret_20d    | +5.6% |
| ret_60d    | -2.0% |
| ma20_dist  | +4.4% |
| ma50_dist  | +1.9% |
| vol_20d    | 28.2% |
| mdd_60d    | 15.7% |
| rsi_14     |  65.5 |
| zscore_20d |   1.3 |

### Brent Crude Oil / BZ=F (score 62.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +4.6% |
| ret_5d     | +15.9% |
| ret_20d    | +10.7% |
| ret_60d    | -10.5% |
| ma20_dist  | +13.9% |
| ma50_dist  |  -1.5% |
| vol_20d    |  51.1% |
| mdd_60d    |  39.4% |
| rsi_14     |   82.6 |
| zscore_20d |    2.1 |

### Dow Jones Industrial Average / ^DJI (score 56.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | -0.9% |
| ret_20d    | +1.3% |
| ret_60d    | +6.1% |
| ma20_dist  | -0.3% |
| ma50_dist  | +1.8% |
| vol_20d    |  7.2% |
| mdd_60d    |  3.2% |
| rsi_14     |  54.5 |
| zscore_20d |  -0.4 |

### Hang Seng / ^HSI (score 55.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.8% |
| ret_5d     | +1.6% |
| ret_20d    | +1.0% |
| ret_60d    | -6.8% |
| ma20_dist  | +3.5% |
| ma50_dist  | -0.8% |
| vol_20d    | 21.0% |
| mdd_60d    | 14.9% |
| rsi_14     |  75.9 |
| zscore_20d |   1.3 |

### S&P 500 / ^GSPC (score 52.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | -1.6% |
| ret_20d    | +0.5% |
| ret_60d    | +5.6% |
| ma20_dist  | -0.3% |
| ma50_dist  | -0.1% |
| vol_20d    | 10.8% |
| mdd_60d    |  4.5% |
| rsi_14     |  58.7 |
| zscore_20d |  -0.3 |

### Euro Stoxx 50 / ^STOXX50E (score 49.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | -0.6% |
| ret_20d    | -1.0% |
| ret_60d    | +5.1% |
| ma20_dist  | -0.8% |
| ma50_dist  | +1.5% |
| vol_20d    | 14.0% |
| mdd_60d    |  3.6% |
| rsi_14     |  49.9 |
| zscore_20d |  -0.9 |

### CAC 40 / ^FCHI (score 48.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | -0.0% |
| ret_20d    | -1.0% |
| ret_60d    | +1.4% |
| ma20_dist  | -0.6% |
| ma50_dist  | +0.9% |
| vol_20d    | 12.0% |
| mdd_60d    |  4.2% |
| rsi_14     |  48.0 |
| zscore_20d |  -0.8 |

### Russell 2000 / ^RUT (score 48.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -0.5% |
| ret_20d    | +1.5% |
| ret_60d    | +7.1% |
| ma20_dist  | -0.9% |
| ma50_dist  | +1.4% |
| vol_20d    | 12.3% |
| mdd_60d    |  4.8% |
| rsi_14     |  39.2 |
| zscore_20d |  -1.3 |

### Amazon.com Inc. / AMZN (score 47.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.1% |
| ret_5d     | +0.8% |
| ret_20d    | +4.1% |
| ret_60d    | -1.1% |
| ma20_dist  | +2.1% |
| ma50_dist  | -1.9% |
| vol_20d    | 31.4% |
| mdd_60d    | 17.4% |
| rsi_14     |  67.4 |
| zscore_20d |   0.8 |

### Meta Platforms Inc. / META (score 47.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.8% |
| ret_5d     |  -3.5% |
| ret_20d    | +13.8% |
| ret_60d    |  -3.3% |
| ma20_dist  |  +6.7% |
| ma50_dist  |  +6.9% |
| vol_20d    |  52.5% |
| mdd_60d    |  19.9% |
| rsi_14     |   67.3 |
| zscore_20d |    0.9 |

### DAX / ^GDAXI (score 47.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | -0.9% |
| ret_20d    | -0.6% |
| ret_60d    | +2.8% |
| ma20_dist  | -1.0% |
| ma50_dist  | -0.1% |
| vol_20d    | 16.0% |
| mdd_60d    |  4.7% |
| rsi_14     |  53.7 |
| zscore_20d |  -0.8 |

### Microsoft Corporation / MSFT (score 44.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.8% |
| ret_5d     | +2.3% |
| ret_20d    | +3.9% |
| ret_60d    | -7.0% |
| ma20_dist  | +3.3% |
| ma50_dist  | -1.9% |
| vol_20d    | 35.1% |
| mdd_60d    | 23.4% |
| rsi_14     |  63.9 |
| zscore_20d |   1.1 |

### NASDAQ 100 / ^NDX (score 32.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.5% |
| ret_5d     | -4.1% |
| ret_20d    | -3.6% |
| ret_60d    | +8.0% |
| ma20_dist  | -3.2% |
| ma50_dist  | -3.2% |
| vol_20d    | 24.7% |
| mdd_60d    |  7.0% |
| rsi_14     |  45.2 |
| zscore_20d |  -2.1 |

### Natural Gas / NG=F (score 30.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.9% |
| ret_5d     | -1.0% |
| ret_20d    | -7.4% |
| ret_60d    | +7.9% |
| ma20_dist  | -6.8% |
| ma50_dist  | -5.6% |
| vol_20d    | 39.4% |
| mdd_60d    | 14.5% |
| rsi_14     |  30.1 |
| zscore_20d |  -1.4 |

### NVIDIA Corporation / NVDA (score 30.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.2% |
| ret_5d     | -3.9% |
| ret_20d    | -0.9% |
| ret_60d    | +1.5% |
| ma20_dist  | +0.3% |
| ma50_dist  | -3.4% |
| vol_20d    | 38.0% |
| mdd_60d    | 18.3% |
| rsi_14     |  58.9 |
| zscore_20d |   0.1 |

### Gold / GC=F (score 26.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.7% |
| ret_5d     |  -2.2% |
| ret_20d    |  -7.9% |
| ret_60d    | -14.6% |
| ma20_dist  |  -1.6% |
| ma50_dist  |  -7.1% |
| vol_20d    |  24.1% |
| mdd_60d    |  15.8% |
| rsi_14     |   44.8 |
| zscore_20d |   -1.0 |

### Alphabet Inc. Class A / GOOGL (score 25.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.2% |
| ret_5d     | -2.9% |
| ret_20d    | -4.7% |
| ret_60d    | +4.4% |
| ma20_dist  | -2.6% |
| ma50_dist  | -6.4% |
| vol_20d    | 35.8% |
| mdd_60d    | 16.2% |
| rsi_14     |  55.3 |
| zscore_20d |  -1.0 |

### Platinum / PL=F (score 18.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.8% |
| ret_5d     |  -0.8% |
| ret_20d    | -10.3% |
| ret_60d    | -20.7% |
| ma20_dist  |  -0.8% |
| ma50_dist  | -10.5% |
| vol_20d    |  37.5% |
| mdd_60d    |  29.1% |
| rsi_14     |   46.7 |
| zscore_20d |   -0.4 |

### Tesla Inc. / TSLA (score 16.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.6% |
| ret_5d     | -6.6% |
| ret_20d    | -3.9% |
| ret_60d    | -1.4% |
| ma20_dist  | -4.3% |
| ma50_dist  | -7.1% |
| vol_20d    | 58.0% |
| mdd_60d    | 15.8% |
| rsi_14     |  50.3 |
| zscore_20d |  -1.2 |

### Silver / SI=F (score 11.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.3% |
| ret_5d     |  -6.3% |
| ret_20d    | -20.7% |
| ret_60d    | -26.7% |
| ma20_dist  |  -6.2% |
| ma50_dist  | -18.6% |
| vol_20d    |  46.4% |
| mdd_60d    |  37.1% |
| rsi_14     |   41.0 |
| zscore_20d |   -1.4 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Wheat / ZW=F                        |  18.0536 |           2.6% |                 0.29x |       36.1071 |            5.3% |
| Apple Inc. / AAPL                   |   8.2557 |           2.5% |                 0.28x |       16.5114 |            4.9% |
| Soybeans / ZS=F                     |  19.7679 |           1.6% |                 0.49x |       39.5357 |            3.3% |
| JPMorgan Chase & Co. / JPM          |   7.8447 |           2.3% |                 0.45x |       15.6893 |            4.6% |
| FTSE 100 / ^FTSE                    | 120.4572 |           1.1% |                 1.05x |      240.9143 |            2.3% |
| UnitedHealth Group Inc. / UNH       |  12.7621 |           3.0% |                 0.41x |       25.5243 |            6.0% |
| Corn / ZC=F                         |  10.8929 |           2.4% |                 0.36x |       21.7857 |            4.9% |
| Brent Crude Oil / BZ=F              |   3.4436 |           3.9% |                 0.20x |        6.8871 |            7.8% |
| Dow Jones Industrial Average / ^DJI | 526.8463 |           1.0% |                 1.38x |     1053.6925 |            2.0% |
| Hang Seng / ^HSI                    | 509.0292 |           2.1% |                 0.48x |     1018.0583 |            4.1% |
| S&P 500 / ^GSPC                     |  73.9665 |           1.0% |                 0.93x |      147.9330 |            2.0% |
| Euro Stoxx 50 / ^STOXX50E           |  76.2335 |           1.2% |                 0.71x |      152.4669 |            2.4% |
| CAC 40 / ^FCHI                      |  97.6829 |           1.2% |                 0.83x |      195.3658 |            2.3% |
| Russell 2000 / ^RUT                 |  38.4858 |           1.3% |                 0.81x |       76.9715 |            2.6% |
| Amazon.com Inc. / AMZN              |   7.5500 |           3.1% |                 0.32x |       15.1000 |            6.1% |
| Meta Platforms Inc. / META          |  30.6629 |           4.7% |                 0.19x |       61.3257 |            9.5% |
| DAX / ^GDAXI                        | 331.7683 |           1.3% |                 0.62x |      663.5366 |            2.7% |
| Microsoft Corporation / MSFT        |  11.4607 |           2.9% |                 0.29x |       22.9214 |            5.8% |
| NASDAQ 100 / ^NDX                   | 605.0145 |           2.1% |                 0.40x |     1210.0290 |            4.2% |
| Natural Gas / NG=F                  |   0.1246 |           4.3% |                 0.25x |        0.2493 |            8.6% |
| NVIDIA Corporation / NVDA           |   7.3471 |           3.6% |                 0.26x |       14.6943 |            7.2% |
| Gold / GC=F                         |  80.1072 |           2.0% |                 0.41x |      160.2143 |            4.0% |
| Alphabet Inc. Class A / GOOGL       |  11.0664 |           3.2% |                 0.28x |       22.1329 |            6.4% |
| Platinum / PL=F                     |  36.0000 |           2.2% |                 0.27x |       72.0000 |            4.5% |
| Tesla Inc. / TSLA                   |  18.6479 |           4.9% |                 0.17x |       37.2957 |            9.8% |
| Silver / SI=F                       |   2.0443 |           3.6% |                 0.22x |        4.0886 |            7.3% |

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

Scoring engine version: **1.0.0** | Git commit: **48d3eec**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
