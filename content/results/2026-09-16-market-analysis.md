+++
title = "Market Analysis 2026-09-16"
date = "2026-09-16T00:00:00+00:00"
draft = false
summary = "Bearish market: 25 reliable instruments. Top signal: ZC=F (score 80.0)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-09-16.json", "data/history/2026-09-16.json"]
market_regime = "Bearish"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "fc60f16"
+++

## Market Regime

**Bearish** — 8 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Corn / ZC=F** — score 80.0, 20d return +15.7%, RSI14=73. 20d up +15.7%; above MA20 by 5.5%; RSI14=73
- **Brent Crude Oil / BZ=F** — score 77.0, 20d return +18.7%, RSI14=87. 20d up +18.7%; above MA20 by 13.1%; RSI14=87
- **Soybeans / ZS=F** — score 75.5, 20d return +9.8%, RSI14=71. 20d up +9.8%; above MA20 by 3.8%; RSI14=71
- **Meta Platforms Inc. / META** — score 72.1, 20d return +17.8%, RSI14=84. 20d up +17.8%; above MA20 by 12.6%; RSI14=84
- **Apple Inc. / AAPL** — score 66.1, 20d return +8.4%, RSI14=69. 20d up +8.4%; above MA20 by 3.8%; RSI14=69

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                        | Applies To                    |
| ---------- | ---------------------------- | ----------------------------- |
| 2026-09-18 | BOJ monetary policy decision | 6758.T, 7203.T, 8306.T, ^N225 |

## Signal History

Compared with the previous available report (**2026-09-15**).

- **New top-5:** ZC=F
- **Persistent top signals:** BZ=F (8 reports), AAPL (4 reports), META (3 reports), ZS=F (2 reports)
- **Dropped from top-5:** MSFT

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     -2 |   -12.7 |
| 7203.T    |     +1 |    +7.0 |
| 8306.T    |     +0 |   -10.9 |
| AAPL      |     -1 |    -6.7 |
| AMZN      |     -5 |   -15.8 |
| BZ=F      |     +1 |    +2.4 |
| CL=F      |     +0 |    +2.1 |
| GC=F      |     +0 |    +0.0 |
| GOOGL     |     -4 |   -11.5 |
| HG=F      |     +0 |   +16.1 |
| JPM       |     +8 |   +20.0 |
| META      |     -2 |    -3.9 |
| MSFT      |     -5 |   -10.6 |
| NG=F      |     +1 |    +3.9 |
| NVDA      |     +4 |   +10.6 |
| PL=F      |     +1 |    +2.4 |
| SI=F      |     +2 |    +2.7 |
| TSLA      |     -2 |    -5.8 |
| UNH       |     -4 |   -15.5 |
| XOM       |     +0 |    +9.1 |
| ZC=F      |     +5 |   +10.6 |
| ZS=F      |     +2 |    +3.6 |
| ZW=F      |     +2 |    +8.8 |
| ^DJI      |     -2 |    -3.0 |
| ^FCHI     |     +3 |    +3.9 |
| ^FTSE     |     -1 |    -4.8 |
| ^GDAXI    |     +5 |   +10.0 |
| ^GSPC     |     +0 |    -3.0 |
| ^HSI      |     -6 |   -10.3 |
| ^N225     |     +0 |    +9.1 |
| ^NDX      |     -3 |    -6.1 |
| ^RUT      |     -1 |    -5.5 |
| ^STOXX50E |     +3 |    +3.6 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **WTI Crude Oil / CL=F** — malformed_input
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Natural Gas / NG=F** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|    1 | Corn / ZC=F            |  80.0 |   Yes    | —               | 20d up +15.7%; above MA20 by 5.5%; RSI14=73  |
|    2 | Brent Crude Oil / BZ=F |  77.0 |   Yes    | —               | 20d up +18.7%; above MA20 by 13.1%; RSI14=87 |
|    3 | Soybeans / ZS=F        |  75.5 |   Yes    | —               | 20d up +9.8%; above MA20 by 3.8%; RSI14=71   |
|    7 | Wheat / ZW=F           |  64.8 |   Yes    | —               | 20d up +9.6%; above MA20 by 1.2%; RSI14=59   |
|   14 | Platinum / PL=F        |  43.3 |   Yes    | —               | 20d down -1.6%; below MA20 by 3.0%; RSI14=42 |
|   18 | Gold / GC=F            |  36.4 |   Yes    | —               | 20d down -4.7%; below MA20 by 4.1%; RSI14=26 |
|   22 | Silver / SI=F          |  30.0 |   Yes    | —               | 20d down -3.8%; below MA20 by 5.2%; RSI14=36 |
|   26 | WTI Crude Oil / CL=F   |  80.3 |    No    | malformed_input | Suppressed: malformed_input                  |
|   29 | Natural Gas / NG=F     |  54.5 |    No    | malformed_input | Suppressed: malformed_input                  |
|   32 | Copper / HG=F          |  39.1 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    4 | Meta Platforms Inc. / META                                                     |  72.1 |   Yes    | —                             | 20d up +17.8%; above MA20 by 12.6%; RSI14=84 |
|    5 | Apple Inc. / AAPL                                                              |  66.1 |   Yes    | —                             | 20d up +8.4%; above MA20 by 3.8%; RSI14=69   |
|    6 | Microsoft Corporation / MSFT                                                   |  65.8 |   Yes    | —                             | 20d up +3.7%; above MA20 by 0.3%; RSI14=53   |
|    8 | JPMorgan Chase & Co. / JPM                                                     |  59.7 |   Yes    | —                             | 20d down -2.3%; below MA20 by 0.9%; RSI14=44 |
|   11 | Alphabet Inc. Class A / GOOGL                                                  |  48.2 |   Yes    | —                             | 20d up +0.3%; above MA20 by 1.1%; RSI14=49   |
|   16 | Tesla Inc. / TSLA                                                              |  37.0 |   Yes    | —                             | 20d up +5.1%; below MA20 by 0.1%; RSI14=53   |
|   21 | NVIDIA Corporation / NVDA                                                      |  30.9 |   Yes    | —                             | 20d down -5.6%; below MA20 by 2.9%; RSI14=50 |
|   24 | Amazon.com Inc. / AMZN                                                         |  18.2 |   Yes    | —                             | 20d down -4.9%; below MA20 by 3.7%; RSI14=38 |
|   25 | UnitedHealth Group Inc. / UNH                                                  |  16.4 |   Yes    | —                             | 20d down -4.4%; below MA20 by 3.6%; RSI14=37 |
|   27 | Exxon Mobil Corporation / XOM                                                  |  78.5 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   28 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  57.6 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   30 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  53.3 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   31 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  48.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    9 | FTSE 100 / ^FTSE                    |  53.6 |   Yes    | —            | 20d down -0.6%; below MA20 by 1.0%; RSI14=32 |
|   10 | S&P 500 / ^GSPC                     |  50.6 |   Yes    | —            | 20d down -2.1%; below MA20 by 1.1%; RSI14=42 |
|   12 | DAX / ^GDAXI                        |  46.7 |   Yes    | —            | 20d down -2.8%; below MA20 by 2.2%; RSI14=31 |
|   13 | Dow Jones Industrial Average / ^DJI |  43.6 |   Yes    | —            | 20d down -2.6%; below MA20 by 1.8%; RSI14=34 |
|   15 | NASDAQ 100 / ^NDX                   |  38.5 |   Yes    | —            | 20d down -3.5%; below MA20 by 1.3%; RSI14=45 |
|   17 | Euro Stoxx 50 / ^STOXX50E           |  37.0 |   Yes    | —            | 20d down -3.6%; below MA20 by 2.4%; RSI14=29 |
|   19 | Hang Seng / ^HSI                    |  33.6 |   Yes    | —            | 20d down -3.2%; below MA20 by 2.8%; RSI14=27 |
|   20 | CAC 40 / ^FCHI                      |  32.7 |   Yes    | —            | 20d down -4.9%; below MA20 by 2.7%; RSI14=25 |
|   23 | Russell 2000 / ^RUT                 |  25.4 |   Yes    | —            | 20d down -6.1%; below MA20 by 3.1%; RSI14=26 |
|   33 | Nikkei 225 / ^N225                  |  25.4 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-09-15 |
| 7203.T    | 2026-09-15 |
| 8306.T    | 2026-09-15 |
| AAPL      | 2026-09-15 |
| AMZN      | 2026-09-15 |
| BZ=F      | 2026-09-15 |
| CL=F      | 2026-09-15 |
| GC=F      | 2026-09-15 |
| GOOGL     | 2026-09-15 |
| HG=F      | 2026-09-15 |
| JPM       | 2026-09-15 |
| META      | 2026-09-15 |
| MSFT      | 2026-09-15 |
| NG=F      | 2026-09-15 |
| NVDA      | 2026-09-15 |
| PL=F      | 2026-09-15 |
| SI=F      | 2026-09-15 |
| TSLA      | 2026-09-15 |
| UNH       | 2026-09-15 |
| XOM       | 2026-09-15 |
| ZC=F      | 2026-09-15 |
| ZS=F      | 2026-09-15 |
| ZW=F      | 2026-09-15 |
| ^DJI      | 2026-09-15 |
| ^FCHI     | 2026-09-15 |
| ^FTSE     | 2026-09-15 |
| ^GDAXI    | 2026-09-15 |
| ^GSPC     | 2026-09-15 |
| ^HSI      | 2026-09-15 |
| ^N225     | 2026-09-15 |
| ^NDX      | 2026-09-15 |
| ^RUT      | 2026-09-15 |
| ^STOXX50E | 2026-09-15 |

## Symbol Details

### Corn / ZC=F (score 80.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +4.6% |
| ret_5d     |  +4.8% |
| ret_20d    | +15.7% |
| ret_60d    | +31.6% |
| ma20_dist  |  +5.5% |
| ma50_dist  | +13.2% |
| vol_20d    |  39.5% |
| mdd_60d    |   6.0% |
| rsi_14     |   72.7 |
| zscore_20d |    1.9 |

### Brent Crude Oil / BZ=F (score 77.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.9% |
| ret_5d     | +11.1% |
| ret_20d    | +18.7% |
| ret_60d    | +44.5% |
| ma20_dist  | +13.1% |
| ma50_dist  | +19.3% |
| vol_20d    |  37.4% |
| mdd_60d    |  21.2% |
| rsi_14     |   87.4 |
| zscore_20d |    2.0 |

### Soybeans / ZS=F (score 75.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.6% |
| ret_5d     |  +1.2% |
| ret_20d    |  +9.8% |
| ret_60d    | +18.9% |
| ma20_dist  |  +3.8% |
| ma50_dist  |  +7.9% |
| vol_20d    |  20.9% |
| mdd_60d    |   8.1% |
| rsi_14     |   71.2 |
| zscore_20d |    1.4 |

### Meta Platforms Inc. / META (score 72.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.7% |
| ret_5d     |  +9.3% |
| ret_20d    | +17.8% |
| ret_60d    | +16.1% |
| ma20_dist  | +12.6% |
| ma50_dist  | +11.0% |
| vol_20d    |  33.3% |
| mdd_60d    |  20.9% |
| rsi_14     |   84.1 |
| zscore_20d |    1.8 |

### Apple Inc. / AAPL (score 66.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.5% |
| ret_5d     |  +4.8% |
| ret_20d    |  +8.4% |
| ret_60d    | +11.2% |
| ma20_dist  |  +3.8% |
| ma50_dist  |  +4.0% |
| vol_20d    |  23.4% |
| mdd_60d    |  11.0% |
| rsi_14     |   68.9 |
| zscore_20d |    1.5 |

### Microsoft Corporation / MSFT (score 65.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.6% |
| ret_5d     |  +0.6% |
| ret_20d    |  +3.7% |
| ret_60d    | +31.0% |
| ma20_dist  |  +0.3% |
| ma50_dist  |  +8.6% |
| vol_20d    |  20.1% |
| mdd_60d    |   5.6% |
| rsi_14     |   52.9 |
| zscore_20d |    0.2 |

### Wheat / ZW=F (score 64.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +3.0% |
| ret_5d     |  -0.2% |
| ret_20d    |  +9.6% |
| ret_60d    | +24.4% |
| ma20_dist  |  +1.2% |
| ma50_dist  |  +6.6% |
| vol_20d    |  42.5% |
| mdd_60d    |  10.7% |
| rsi_14     |   59.3 |
| zscore_20d |    0.3 |

### JPMorgan Chase & Co. / JPM (score 59.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | -0.3% |
| ret_20d    | -2.3% |
| ret_60d    | +8.9% |
| ma20_dist  | -0.9% |
| ma50_dist  | +0.0% |
| vol_20d    | 15.4% |
| mdd_60d    |  4.1% |
| rsi_14     |  44.4 |
| zscore_20d |  -1.0 |

### FTSE 100 / ^FTSE (score 53.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -1.4% |
| ret_20d    | -0.6% |
| ret_60d    | +2.1% |
| ma20_dist  | -1.0% |
| ma50_dist  | -0.8% |
| vol_20d    |  7.6% |
| mdd_60d    |  2.7% |
| rsi_14     |  31.6 |
| zscore_20d |  -1.4 |

### S&P 500 / ^GSPC (score 50.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -1.1% |
| ret_20d    | -2.1% |
| ret_60d    | +1.1% |
| ma20_dist  | -1.1% |
| ma50_dist  | -0.3% |
| vol_20d    |  8.8% |
| mdd_60d    |  3.4% |
| rsi_14     |  41.9 |
| zscore_20d |  -2.0 |

### Alphabet Inc. Class A / GOOGL (score 48.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.3% |
| ret_5d     | +2.0% |
| ret_20d    | +0.3% |
| ret_60d    | -6.3% |
| ma20_dist  | +1.1% |
| ma50_dist  | -0.4% |
| vol_20d    | 22.4% |
| mdd_60d    | 14.4% |
| rsi_14     |  48.7 |
| zscore_20d |   0.8 |

### DAX / ^GDAXI (score 46.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | -2.3% |
| ret_20d    | -2.8% |
| ret_60d    | +2.0% |
| ma20_dist  | -2.2% |
| ma50_dist  | -1.3% |
| vol_20d    | 10.6% |
| mdd_60d    |  4.5% |
| rsi_14     |  30.6 |
| zscore_20d |  -1.7 |

### Dow Jones Industrial Average / ^DJI (score 43.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | -1.3% |
| ret_20d    | -2.6% |
| ret_60d    | +1.0% |
| ma20_dist  | -1.8% |
| ma50_dist  | -1.6% |
| vol_20d    | 11.0% |
| mdd_60d    |  4.2% |
| rsi_14     |  33.7 |
| zscore_20d |  -1.9 |

### Platinum / PL=F (score 43.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.2% |
| ret_5d     |  -4.1% |
| ret_20d    |  -1.6% |
| ret_60d    | +10.7% |
| ma20_dist  |  -3.0% |
| ma50_dist  |  +1.9% |
| vol_20d    |  34.9% |
| mdd_60d    |   7.4% |
| rsi_14     |   42.4 |
| zscore_20d |   -1.3 |

### NASDAQ 100 / ^NDX (score 38.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | -1.9% |
| ret_20d    | -3.5% |
| ret_60d    | -4.8% |
| ma20_dist  | -1.3% |
| ma50_dist  | -0.8% |
| vol_20d    | 12.8% |
| mdd_60d    | 10.4% |
| rsi_14     |  44.9 |
| zscore_20d |  -1.9 |

### Tesla Inc. / TSLA (score 37.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.7% |
| ret_5d     |  -3.1% |
| ret_20d    |  +5.1% |
| ret_60d    | -11.0% |
| ma20_dist  |  -0.1% |
| ma50_dist  |  +1.1% |
| vol_20d    |  50.0% |
| mdd_60d    |  29.9% |
| rsi_14     |   52.6 |
| zscore_20d |   -0.0 |

### Euro Stoxx 50 / ^STOXX50E (score 37.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -2.8% |
| ret_20d    | -3.6% |
| ret_60d    | +0.1% |
| ma20_dist  | -2.4% |
| ma50_dist  | -2.2% |
| vol_20d    | 10.2% |
| mdd_60d    |  4.8% |
| rsi_14     |  29.5 |
| zscore_20d |  -2.1 |

### Gold / GC=F (score 36.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -2.4% |
| ret_20d    | -4.7% |
| ret_60d    | +7.5% |
| ma20_dist  | -4.1% |
| ma50_dist  | +0.2% |
| vol_20d    | 20.6% |
| mdd_60d    |  7.9% |
| rsi_14     |  26.3 |
| zscore_20d |  -1.5 |

### Hang Seng / ^HSI (score 33.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | -2.6% |
| ret_20d    | -3.2% |
| ret_60d    | +3.8% |
| ma20_dist  | -2.8% |
| ma50_dist  | -2.4% |
| vol_20d    | 13.2% |
| mdd_60d    |  5.2% |
| rsi_14     |  26.8 |
| zscore_20d |  -2.2 |

### CAC 40 / ^FCHI (score 32.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | -2.7% |
| ret_20d    | -4.9% |
| ret_60d    | -3.0% |
| ma20_dist  | -2.7% |
| ma50_dist  | -3.9% |
| vol_20d    | 11.0% |
| mdd_60d    |  7.3% |
| rsi_14     |  25.2 |
| zscore_20d |  -1.8 |

### NVIDIA Corporation / NVDA (score 30.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | -5.9% |
| ret_20d    | -5.6% |
| ret_60d    | +0.7% |
| ma20_dist  | -2.9% |
| ma50_dist  | -0.5% |
| vol_20d    | 44.9% |
| mdd_60d    | 10.6% |
| rsi_14     |  49.6 |
| zscore_20d |  -1.0 |

### Silver / SI=F (score 30.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -4.6% |
| ret_20d    | -3.8% |
| ret_60d    | +8.4% |
| ma20_dist  | -5.2% |
| ma50_dist  | +0.2% |
| vol_20d    | 34.7% |
| mdd_60d    |  9.7% |
| rsi_14     |  36.5 |
| zscore_20d |  -1.8 |

### Russell 2000 / ^RUT (score 25.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | -3.0% |
| ret_20d    | -6.1% |
| ret_60d    | -3.7% |
| ma20_dist  | -3.1% |
| ma50_dist  | -3.6% |
| vol_20d    | 12.7% |
| mdd_60d    |  6.5% |
| rsi_14     |  26.2 |
| zscore_20d |  -1.9 |

### Amazon.com Inc. / AMZN (score 18.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.0% |
| ret_5d     | -3.3% |
| ret_20d    | -4.9% |
| ret_60d    | +1.6% |
| ma20_dist  | -3.7% |
| ma50_dist  | -2.8% |
| vol_20d    | 26.5% |
| mdd_60d    | 12.5% |
| rsi_14     |  37.5 |
| zscore_20d |  -2.2 |

### UnitedHealth Group Inc. / UNH (score 16.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.0% |
| ret_5d     | -5.6% |
| ret_20d    | -4.4% |
| ret_60d    | -6.2% |
| ma20_dist  | -3.6% |
| ma50_dist  | -7.5% |
| vol_20d    | 21.7% |
| mdd_60d    | 13.8% |
| rsi_14     |  37.1 |
| zscore_20d |  -2.1 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Corn / ZC=F                         |  11.1607 |           2.1% |                 0.25x |       22.3214 |            4.2% |
| Brent Crude Oil / BZ=F              |   4.0593 |           3.7% |                 0.27x |        8.1186 |            7.5% |
| Soybeans / ZS=F                     |  20.7500 |           1.6% |                 0.48x |       41.5000 |            3.1% |
| Meta Platforms Inc. / META          |  22.4921 |           3.4% |                 0.30x |       44.9843 |            6.7% |
| Apple Inc. / AAPL                   |   7.8093 |           2.4% |                 0.43x |       15.6186 |            4.7% |
| Microsoft Corporation / MSFT        |  10.6350 |           2.1% |                 0.50x |       21.2700 |            4.3% |
| Wheat / ZW=F                        |  22.3036 |           3.1% |                 0.24x |       44.6071 |            6.1% |
| JPMorgan Chase & Co. / JPM          |   6.2729 |           1.8% |                 0.65x |       12.5457 |            3.6% |
| FTSE 100 / ^FTSE                    |  95.3857 |           0.9% |                 1.32x |      190.7715 |            1.8% |
| S&P 500 / ^GSPC                     |  59.2591 |           0.8% |                 1.13x |      118.5183 |            1.6% |
| Alphabet Inc. Class A / GOOGL       |   7.6356 |           2.2% |                 0.45x |       15.2712 |            4.4% |
| DAX / ^GDAXI                        | 260.1094 |           1.0% |                 0.94x |      520.2188 |            2.0% |
| Dow Jones Industrial Average / ^DJI | 477.1903 |           0.9% |                 0.91x |      954.3806 |            1.8% |
| Platinum / PL=F                     |  34.0786 |           1.9% |                 0.29x |       68.1572 |            3.8% |
| NASDAQ 100 / ^NDX                   | 318.3178 |           1.1% |                 0.78x |      636.6356 |            2.2% |
| Tesla Inc. / TSLA                   |  13.9864 |           3.9% |                 0.20x |       27.9729 |            7.8% |
| Euro Stoxx 50 / ^STOXX50E           |  68.0278 |           1.1% |                 0.98x |      136.0556 |            2.2% |
| Gold / GC=F                         | 110.2785 |           2.5% |                 0.49x |      220.5569 |            5.1% |
| Hang Seng / ^HSI                    | 317.9487 |           1.3% |                 0.76x |      635.8973 |            2.6% |
| CAC 40 / ^FCHI                      |  89.2001 |           1.1% |                 0.91x |      178.4002 |            2.2% |
| NVIDIA Corporation / NVDA           |   7.5077 |           3.5% |                 0.22x |       15.0153 |            7.1% |
| Silver / SI=F                       |   1.9770 |           3.1% |                 0.29x |        3.9540 |            6.3% |
| Russell 2000 / ^RUT                 |  29.8521 |           1.0% |                 0.79x |       59.7043 |            2.1% |
| Amazon.com Inc. / AMZN              |   5.8871 |           2.4% |                 0.38x |       11.7743 |            4.7% |
| UnitedHealth Group Inc. / UNH       |  10.4898 |           2.8% |                 0.46x |       20.9795 |            5.6% |

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

Scoring engine version: **1.0.0** | Git commit: **fc60f16**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
