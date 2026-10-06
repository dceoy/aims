+++
title = "Market Analysis 2026-10-06"
date = "2026-10-06T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: MSFT (score 84.8)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-10-06.json", "data/history/2026-10-06.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "016c187"
+++

## Market Regime

**Neutral** — 10 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Microsoft Corporation / MSFT** — score 84.8, 20d return +5.1%, RSI14=68. 20d up +5.1%; above MA20 by 4.4%; RSI14=68
- **NVIDIA Corporation / NVDA** — score 80.6, 20d return +3.8%, RSI14=85. 20d up +3.8%; above MA20 by 6.6%; RSI14=85
- **NASDAQ 100 / ^NDX** — score 76.1, 20d return +5.2%, RSI14=82. 20d up +5.2%; above MA20 by 3.6%; RSI14=82
- **S&P 500 / ^GSPC** — score 74.2, 20d return +0.7%, RSI14=67. 20d up +0.7%; above MA20 by 1.3%; RSI14=67
- **Meta Platforms Inc. / META** — score 70.9, 20d return +20.4%, RSI14=64. 20d up +20.4%; above MA20 by 5.7%; RSI14=64

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                | Applies To |
| ---------- | -------------------- | ---------- |
| 2026-10-13 | JPM earnings release | JPM        |
| 2026-10-13 | UNH earnings release | UNH        |

## Signal History

Compared with the previous available report (**2026-10-05**).

- **New top-5:** META
- **Persistent top signals:** MSFT (7 reports), ^NDX (7 reports), ^GSPC (5 reports), NVDA (4 reports)
- **Dropped from top-5:** AAPL

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     -2 |    -6.7 |
| 7203.T    |     +1 |    +8.2 |
| 8306.T    |     +1 |   +12.7 |
| AAPL      |     -2 |   -10.6 |
| AMZN      |     +0 |    -7.0 |
| BZ=F      |     -7 |   -19.1 |
| CL=F      |     -1 |    -9.4 |
| GC=F      |     +0 |    +1.8 |
| GOOGL     |     +4 |    -1.2 |
| HG=F      |     +1 |    +7.0 |
| JPM       |     -2 |    -1.5 |
| META      |     +1 |    +8.2 |
| MSFT      |     +1 |    +4.2 |
| NG=F      |     +1 |    +3.6 |
| NVDA      |     -1 |    -1.2 |
| PL=F      |     +4 |   +12.4 |
| SI=F      |     +4 |   +14.2 |
| TSLA      |     +3 |    +7.6 |
| UNH       |     +3 |    +8.5 |
| XOM       |     -2 |    -8.5 |
| ZC=F      |     -1 |    -5.8 |
| ZS=F      |     +1 |    -1.5 |
| ZW=F      |     +2 |    +3.6 |
| ^DJI      |     +0 |    -1.2 |
| ^FCHI     |     -5 |   -11.5 |
| ^FTSE     |     +0 |    -1.5 |
| ^GDAXI    |     -1 |    -7.6 |
| ^GSPC     |     +0 |    +1.5 |
| ^HSI      |     -1 |    +2.4 |
| ^N225     |     +1 |   +12.4 |
| ^NDX      |     +0 |    -2.1 |
| ^RUT      |     +1 |    -2.1 |
| ^STOXX50E |     -4 |   -10.0 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Nikkei 225 / ^N225** — missing_bars
- **Natural Gas / NG=F** — malformed_input
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Copper / HG=F** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **WTI Crude Oil / CL=F** — malformed_input

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|   12 | Soybeans / ZS=F        |  47.6 |   Yes    | —               | 20d down -1.0%; below MA20 by 1.8%; RSI14=34 |
|   17 | Wheat / ZW=F           |  38.5 |   Yes    | —               | 20d down -3.3%; below MA20 by 2.2%; RSI14=33 |
|   18 | Brent Crude Oil / BZ=F |  34.5 |   Yes    | —               | 20d up +4.2%; below MA20 by 3.1%; RSI14=34   |
|   19 | Corn / ZC=F            |  31.5 |   Yes    | —               | 20d down -2.9%; below MA20 by 4.3%; RSI14=24 |
|   20 | Platinum / PL=F        |  30.3 |   Yes    | —               | 20d down -6.5%; below MA20 by 3.5%; RSI14=40 |
|   21 | Silver / SI=F          |  30.3 |   Yes    | —               | 20d down -8.8%; below MA20 by 4.4%; RSI14=41 |
|   23 | Gold / GC=F            |  26.7 |   Yes    | —               | 20d down -7.1%; below MA20 by 3.7%; RSI14=31 |
|   27 | Natural Gas / NG=F     |  65.2 |    No    | malformed_input | Suppressed: malformed_input                  |
|   29 | Copper / HG=F          |  59.7 |    No    | malformed_input | Suppressed: malformed_input                  |
|   33 | WTI Crude Oil / CL=F   |  24.9 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    1 | Microsoft Corporation / MSFT                                                   |  84.8 |   Yes    | —                             | 20d up +5.1%; above MA20 by 4.4%; RSI14=68   |
|    2 | NVIDIA Corporation / NVDA                                                      |  80.6 |   Yes    | —                             | 20d up +3.8%; above MA20 by 6.6%; RSI14=85   |
|    5 | Meta Platforms Inc. / META                                                     |  70.9 |   Yes    | —                             | 20d up +20.4%; above MA20 by 5.7%; RSI14=64  |
|    6 | Tesla Inc. / TSLA                                                              |  63.9 |   Yes    | —                             | 20d up +7.0%; above MA20 by 3.5%; RSI14=64   |
|    7 | Apple Inc. / AAPL                                                              |  52.4 |   Yes    | —                             | 20d up +4.0%; above MA20 by 0.1%; RSI14=52   |
|    8 | Alphabet Inc. Class A / GOOGL                                                  |  51.2 |   Yes    | —                             | 20d up +2.4%; above MA20 by 1.0%; RSI14=51   |
|   10 | Amazon.com Inc. / AMZN                                                         |  48.2 |   Yes    | —                             | 20d down -2.8%; above MA20 by 0.0%; RSI14=54 |
|   14 | UnitedHealth Group Inc. / UNH                                                  |  45.8 |   Yes    | —                             | 20d down -4.1%; above MA20 by 0.3%; RSI14=53 |
|   24 | JPMorgan Chase & Co. / JPM                                                     |  24.9 |   Yes    | —                             | 20d down -7.3%; below MA20 by 3.4%; RSI14=26 |
|   28 | Exxon Mobil Corporation / XOM                                                  |  60.6 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   30 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  53.0 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   31 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  49.7 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   32 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  33.3 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    3 | NASDAQ 100 / ^NDX                   |  76.1 |   Yes    | —            | 20d up +5.2%; above MA20 by 3.6%; RSI14=82   |
|    4 | S&P 500 / ^GSPC                     |  74.2 |   Yes    | —            | 20d up +0.7%; above MA20 by 1.3%; RSI14=67   |
|    9 | DAX / ^GDAXI                        |  50.0 |   Yes    | —            | 20d down -2.9%; below MA20 by 0.7%; RSI14=47 |
|   11 | Euro Stoxx 50 / ^STOXX50E           |  48.2 |   Yes    | —            | 20d down -2.5%; below MA20 by 0.7%; RSI14=50 |
|   13 | Russell 2000 / ^RUT                 |  46.7 |   Yes    | —            | 20d down -4.3%; below MA20 by 0.5%; RSI14=45 |
|   15 | Dow Jones Industrial Average / ^DJI |  44.5 |   Yes    | —            | 20d down -4.0%; below MA20 by 0.9%; RSI14=39 |
|   16 | FTSE 100 / ^FTSE                    |  42.4 |   Yes    | —            | 20d down -3.0%; below MA20 by 1.5%; RSI14=40 |
|   22 | Hang Seng / ^HSI                    |  30.0 |   Yes    | —            | 20d down -6.3%; below MA20 by 3.0%; RSI14=33 |
|   25 | CAC 40 / ^FCHI                      |  21.5 |   Yes    | —            | 20d down -5.7%; below MA20 by 3.0%; RSI14=33 |
|   26 | Nikkei 225 / ^N225                  |  77.9 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-10-05 |
| 7203.T    | 2026-10-05 |
| 8306.T    | 2026-10-05 |
| AAPL      | 2026-10-05 |
| AMZN      | 2026-10-05 |
| BZ=F      | 2026-10-05 |
| CL=F      | 2026-10-05 |
| GC=F      | 2026-10-05 |
| GOOGL     | 2026-10-05 |
| HG=F      | 2026-10-05 |
| JPM       | 2026-10-05 |
| META      | 2026-10-05 |
| MSFT      | 2026-10-05 |
| NG=F      | 2026-10-05 |
| NVDA      | 2026-10-05 |
| PL=F      | 2026-10-05 |
| SI=F      | 2026-10-05 |
| TSLA      | 2026-10-05 |
| UNH       | 2026-10-05 |
| XOM       | 2026-10-05 |
| ZC=F      | 2026-10-05 |
| ZS=F      | 2026-10-05 |
| ZW=F      | 2026-10-05 |
| ^DJI      | 2026-10-05 |
| ^FCHI     | 2026-10-05 |
| ^FTSE     | 2026-10-05 |
| ^GDAXI    | 2026-10-05 |
| ^GSPC     | 2026-10-05 |
| ^HSI      | 2026-10-05 |
| ^N225     | 2026-10-05 |
| ^NDX      | 2026-10-05 |
| ^RUT      | 2026-10-05 |
| ^STOXX50E | 2026-10-05 |

## Symbol Details

### Microsoft Corporation / MSFT (score 84.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.5% |
| ret_5d     |  +3.1% |
| ret_20d    |  +5.1% |
| ret_60d    | +36.4% |
| ma20_dist  |  +4.4% |
| ma50_dist  |  +7.1% |
| vol_20d    |  20.9% |
| mdd_60d    |   5.1% |
| rsi_14     |   68.3 |
| zscore_20d |    2.3 |

### NVIDIA Corporation / NVDA (score 80.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.1% |
| ret_5d     |  +4.4% |
| ret_20d    |  +3.8% |
| ret_60d    | +13.2% |
| ma20_dist  |  +6.6% |
| ma50_dist  |  +9.2% |
| vol_20d    |  24.8% |
| mdd_60d    |  10.6% |
| rsi_14     |   84.6 |
| zscore_20d |    2.1 |

### NASDAQ 100 / ^NDX (score 76.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | +2.6% |
| ret_20d    | +5.2% |
| ret_60d    | +4.2% |
| ma20_dist  | +3.6% |
| ma50_dist  | +5.3% |
| vol_20d    | 15.1% |
| mdd_60d    |  8.1% |
| rsi_14     |  82.2 |
| zscore_20d |   1.6 |

### S&P 500 / ^GSPC (score 74.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | +1.2% |
| ret_20d    | +0.7% |
| ret_60d    | +2.6% |
| ma20_dist  | +1.3% |
| ma50_dist  | +1.4% |
| vol_20d    | 10.3% |
| mdd_60d    |  3.4% |
| rsi_14     |  66.8 |
| zscore_20d |   1.7 |

### Meta Platforms Inc. / META (score 70.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.9% |
| ret_5d     |  +3.7% |
| ret_20d    | +20.4% |
| ret_60d    | +10.9% |
| ma20_dist  |  +5.7% |
| ma50_dist  | +18.2% |
| vol_20d    |  55.6% |
| mdd_60d    |  20.9% |
| rsi_14     |   63.6 |
| zscore_20d |    0.9 |

### Tesla Inc. / TSLA (score 63.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.2% |
| ret_5d     | +6.0% |
| ret_20d    | +7.0% |
| ret_60d    | -7.1% |
| ma20_dist  | +3.5% |
| ma50_dist  | +8.6% |
| vol_20d    | 31.9% |
| mdd_60d    | 24.7% |
| rsi_14     |  63.5 |
| zscore_20d |   1.4 |

### Apple Inc. / AAPL (score 52.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | -1.6% |
| ret_20d    | +4.0% |
| ret_60d    | +5.7% |
| ma20_dist  | +0.1% |
| ma50_dist  | +3.3% |
| vol_20d    | 20.5% |
| mdd_60d    | 11.0% |
| rsi_14     |  51.9 |
| zscore_20d |   0.1 |

### Alphabet Inc. Class A / GOOGL (score 51.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | +1.1% |
| ret_20d    | +2.4% |
| ret_60d    | -3.0% |
| ma20_dist  | +1.0% |
| ma50_dist  | +0.5% |
| vol_20d    | 25.1% |
| mdd_60d    | 14.4% |
| rsi_14     |  51.3 |
| zscore_20d |   0.6 |

### DAX / ^GDAXI (score 50.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | -0.5% |
| ret_20d    | -2.9% |
| ret_60d    | +0.6% |
| ma20_dist  | -0.7% |
| ma50_dist  | -2.2% |
| vol_20d    | 12.6% |
| mdd_60d    |  6.1% |
| rsi_14     |  46.8 |
| zscore_20d |  -0.8 |

### Amazon.com Inc. / AMZN (score 48.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.0% |
| ret_5d     | +2.1% |
| ret_20d    | -2.8% |
| ret_60d    | +2.5% |
| ma20_dist  | +0.0% |
| ma50_dist  | -2.2% |
| vol_20d    | 20.8% |
| mdd_60d    | 13.4% |
| rsi_14     |  54.2 |
| zscore_20d |   0.0 |

### Euro Stoxx 50 / ^STOXX50E (score 48.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | -0.9% |
| ret_20d    | -2.5% |
| ret_60d    | -0.5% |
| ma20_dist  | -0.7% |
| ma50_dist  | -2.2% |
| vol_20d    | 13.2% |
| mdd_60d    |  5.7% |
| rsi_14     |  50.5 |
| zscore_20d |  -0.9 |

### Soybeans / ZS=F (score 47.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | -0.6% |
| ret_20d    | -1.0% |
| ret_60d    | +6.5% |
| ma20_dist  | -1.8% |
| ma50_dist  | +2.6% |
| vol_20d    | 19.4% |
| mdd_60d    |  8.1% |
| rsi_14     |  33.8 |
| zscore_20d |  -1.4 |

### Russell 2000 / ^RUT (score 46.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | +1.0% |
| ret_20d    | -4.3% |
| ret_60d    | -4.4% |
| ma20_dist  | -0.5% |
| ma50_dist  | -3.2% |
| vol_20d    | 10.9% |
| mdd_60d    |  8.9% |
| rsi_14     |  44.7 |
| zscore_20d |  -0.3 |

### UnitedHealth Group Inc. / UNH (score 45.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.8% |
| ret_5d     |  +0.2% |
| ret_20d    |  -4.1% |
| ret_60d    | -10.8% |
| ma20_dist  |  +0.3% |
| ma50_dist  |  -3.4% |
| vol_20d    |  20.4% |
| mdd_60d    |  16.3% |
| rsi_14     |   53.2 |
| zscore_20d |    0.2 |

### Dow Jones Industrial Average / ^DJI (score 44.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | -0.4% |
| ret_20d    | -4.0% |
| ret_60d    | -2.6% |
| ma20_dist  | -0.9% |
| ma50_dist  | -2.7% |
| vol_20d    | 10.3% |
| mdd_60d    |  6.3% |
| rsi_14     |  39.3 |
| zscore_20d |  -0.9 |

### FTSE 100 / ^FTSE (score 42.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | -1.8% |
| ret_20d    | -3.0% |
| ret_60d    | +0.0% |
| ma20_dist  | -1.5% |
| ma50_dist  | -2.4% |
| vol_20d    | 11.1% |
| mdd_60d    |  4.4% |
| rsi_14     |  40.1 |
| zscore_20d |  -1.6 |

### Wheat / ZW=F (score 38.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.4% |
| ret_5d     | +0.5% |
| ret_20d    | -3.3% |
| ret_60d    | +2.2% |
| ma20_dist  | -2.2% |
| ma50_dist  | -0.2% |
| vol_20d    | 25.3% |
| mdd_60d    | 11.9% |
| rsi_14     |  33.0 |
| zscore_20d |  -0.9 |

### Brent Crude Oil / BZ=F (score 34.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.9% |
| ret_5d     |  -4.7% |
| ret_20d    |  +4.2% |
| ret_60d    | +19.1% |
| ma20_dist  |  -3.1% |
| ma50_dist  |  +5.5% |
| vol_20d    |  41.5% |
| mdd_60d    |  21.2% |
| rsi_14     |   34.3 |
| zscore_20d |   -1.2 |

### Corn / ZC=F (score 31.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.1% |
| ret_5d     |  -4.9% |
| ret_20d    |  -2.9% |
| ret_60d    | +11.1% |
| ma20_dist  |  -4.3% |
| ma50_dist  |  +0.8% |
| vol_20d    |  26.4% |
| mdd_60d    |   8.4% |
| rsi_14     |   24.0 |
| zscore_20d |   -1.6 |

### Platinum / PL=F (score 30.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.4% |
| ret_5d     | -0.8% |
| ret_20d    | -6.5% |
| ret_60d    | +4.4% |
| ma20_dist  | -3.5% |
| ma50_dist  | -3.9% |
| vol_20d    | 34.4% |
| mdd_60d    | 12.2% |
| rsi_14     |  40.0 |
| zscore_20d |  -1.1 |

### Silver / SI=F (score 30.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.5% |
| ret_5d     | -0.6% |
| ret_20d    | -8.8% |
| ret_60d    | +8.9% |
| ma20_dist  | -4.4% |
| ma50_dist  | -5.8% |
| vol_20d    | 32.3% |
| mdd_60d    | 13.7% |
| rsi_14     |  41.4 |
| zscore_20d |  -1.2 |

### Hang Seng / ^HSI (score 30.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | -1.9% |
| ret_20d    | -6.3% |
| ret_60d    | -0.6% |
| ma20_dist  | -3.0% |
| ma50_dist  | -4.8% |
| vol_20d    | 13.2% |
| mdd_60d    |  7.8% |
| rsi_14     |  32.6 |
| zscore_20d |  -2.0 |

### Gold / GC=F (score 26.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | -0.3% |
| ret_20d    | -7.1% |
| ret_60d    | +4.3% |
| ma20_dist  | -3.7% |
| ma50_dist  | -5.3% |
| vol_20d    | 16.0% |
| mdd_60d    | 11.7% |
| rsi_14     |  31.5 |
| zscore_20d |  -1.6 |

### JPMorgan Chase & Co. / JPM (score 24.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.0% |
| ret_5d     | -1.3% |
| ret_20d    | -7.3% |
| ret_60d    | -1.2% |
| ma20_dist  | -3.4% |
| ma50_dist  | -5.5% |
| vol_20d    | 17.7% |
| mdd_60d    |  9.4% |
| rsi_14     |  26.1 |
| zscore_20d |  -1.3 |

### CAC 40 / ^FCHI (score 21.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | -3.0% |
| ret_20d    | -5.7% |
| ret_60d    | -6.3% |
| ma20_dist  | -3.0% |
| ma50_dist  | -6.0% |
| vol_20d    | 12.7% |
| mdd_60d    | 10.2% |
| rsi_14     |  33.0 |
| zscore_20d |  -2.1 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Microsoft Corporation / MSFT        |  12.1671 |           2.3% |                 0.48x |       24.3343 |            4.6% |
| NVIDIA Corporation / NVDA           |   5.3764 |           2.3% |                 0.40x |       10.7529 |            4.5% |
| NASDAQ 100 / ^NDX                   | 404.0378 |           1.3% |                 0.66x |      808.0756 |            2.6% |
| S&P 500 / ^GSPC                     |  73.0407 |           0.9% |                 0.98x |      146.0814 |            1.9% |
| Meta Platforms Inc. / META          |  28.6884 |           3.9% |                 0.18x |       57.3768 |            7.7% |
| Tesla Inc. / TSLA                   |  12.0586 |           3.2% |                 0.31x |       24.1171 |            6.4% |
| Apple Inc. / AAPL                   |   6.4907 |           1.9% |                 0.49x |       12.9814 |            3.9% |
| Alphabet Inc. Class A / GOOGL       |   9.1036 |           2.6% |                 0.40x |       18.2071 |            5.3% |
| DAX / ^GDAXI                        | 309.0559 |           1.2% |                 0.79x |      618.1119 |            2.4% |
| Amazon.com Inc. / AMZN              |   5.2300 |           2.1% |                 0.48x |       10.4600 |            4.2% |
| Euro Stoxx 50 / ^STOXX50E           |  73.2650 |           1.2% |                 0.75x |      146.5299 |            2.3% |
| Soybeans / ZS=F                     |  21.2679 |           1.7% |                 0.52x |       42.5357 |            3.3% |
| Russell 2000 / ^RUT                 |  35.6364 |           1.3% |                 0.91x |       71.2728 |            2.5% |
| UnitedHealth Group Inc. / UNH       |   7.5357 |           2.0% |                 0.49x |       15.0714 |            4.0% |
| Dow Jones Industrial Average / ^DJI | 509.5106 |           1.0% |                 0.97x |     1019.0212 |            2.0% |
| FTSE 100 / ^FTSE                    | 108.3570 |           1.0% |                 0.90x |      216.7140 |            2.1% |
| Wheat / ZW=F                        |  16.7321 |           2.4% |                 0.39x |       33.4643 |            4.8% |
| Brent Crude Oil / BZ=F              |   4.7586 |           4.7% |                 0.24x |        9.5171 |            9.5% |
| Corn / ZC=F                         |  11.0179 |           2.2% |                 0.38x |       22.0357 |            4.4% |
| Platinum / PL=F                     |  30.4572 |           1.8% |                 0.29x |       60.9143 |            3.6% |
| Silver / SI=F                       |   1.2914 |           2.1% |                 0.31x |        2.5827 |            4.2% |
| Hang Seng / ^HSI                    | 306.4795 |           1.3% |                 0.76x |      612.9590 |            2.5% |
| Gold / GC=F                         |  88.3714 |           2.1% |                 0.62x |      176.7428 |            4.3% |
| JPMorgan Chase & Co. / JPM          |   6.4379 |           1.9% |                 0.56x |       12.8757 |            3.9% |
| CAC 40 / ^FCHI                      |  92.1900 |           1.2% |                 0.79x |      184.3800 |            2.4% |

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

Scoring engine version: **1.0.0** | Git commit: **016c187**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
