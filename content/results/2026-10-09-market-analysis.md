+++
title = "Market Analysis 2026-10-09"
date = "2026-10-09T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: MSFT (score 78.5)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-10-09.json", "data/history/2026-10-09.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "a7520f5"
+++

## Market Regime

**Neutral** — 10 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Microsoft Corporation / MSFT** — score 78.5, 20d return +6.1%, RSI14=71. 20d up +6.1%; above MA20 by 2.9%; RSI14=71
- **Apple Inc. / AAPL** — score 75.8, 20d return +4.2%, RSI14=55. 20d up +4.2%; above MA20 by 1.6%; RSI14=55
- **S&P 500 / ^GSPC** — score 74.2, 20d return +2.3%, RSI14=61. 20d up +2.3%; above MA20 by 0.9%; RSI14=61
- **NASDAQ 100 / ^NDX** — score 70.9, 20d return +5.6%, RSI14=67. 20d up +5.6%; above MA20 by 1.6%; RSI14=67
- **Brent Crude Oil / BZ=F** — score 60.6, 20d return -3.1%, RSI14=51. 20d down -3.1%; above MA20 by 0.8%; RSI14=51

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                | Applies To |
| ---------- | -------------------- | ---------- |
| 2026-10-13 | JPM earnings release | JPM        |
| 2026-10-13 | UNH earnings release | UNH        |

## Signal History

Compared with the previous available report (**2026-10-08**).

- **New top-5:** AAPL, BZ=F
- **Persistent top signals:** MSFT (10 reports), ^NDX (10 reports), ^GSPC (8 reports)
- **Dropped from top-5:** AMZN, NVDA

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +0 |    -2.1 |
| 7203.T    |     +1 |    +8.8 |
| 8306.T    |     -2 |   -15.4 |
| AAPL      |     +4 |    +8.5 |
| AMZN      |     -7 |   -19.7 |
| BZ=F      |    +11 |   +20.9 |
| CL=F      |     +1 |   +14.8 |
| GC=F      |     +1 |    +9.1 |
| GOOGL     |     -4 |    -4.8 |
| HG=F      |     +0 |    -3.9 |
| JPM       |     +1 |    +4.2 |
| META      |     +2 |    +6.1 |
| MSFT      |     +0 |    -7.9 |
| NG=F      |     -1 |    -6.4 |
| NVDA      |     -2 |   -14.6 |
| PL=F      |     +1 |    +7.9 |
| SI=F      |     -1 |    -6.4 |
| TSLA      |     +0 |    +0.9 |
| UNH       |     -8 |    -9.4 |
| XOM       |     +2 |   +14.2 |
| ZC=F      |     -1 |    -1.5 |
| ZS=F      |     -2 |    -3.9 |
| ZW=F      |     +1 |    +2.7 |
| ^DJI      |     +4 |    +7.9 |
| ^FCHI     |     +1 |    +4.2 |
| ^FTSE     |     +2 |    +8.5 |
| ^GDAXI    |     -2 |    -3.3 |
| ^GSPC     |     +0 |    -1.8 |
| ^HSI      |     -5 |   -12.4 |
| ^N225     |     -1 |    -8.8 |
| ^NDX      |     -2 |    -6.7 |
| ^RUT      |     +6 |    +8.2 |
| ^STOXX50E |     +0 |    +2.1 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Exxon Mobil Corporation / XOM** — malformed_input
- **Natural Gas / NG=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars
- **Copper / HG=F** — malformed_input
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **WTI Crude Oil / CL=F** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|    5 | Brent Crude Oil / BZ=F |  60.6 |   Yes    | —               | 20d down -3.1%; above MA20 by 0.8%; RSI14=51 |
|   10 | Soybeans / ZS=F        |  55.5 |   Yes    | —               | 20d down -2.2%; below MA20 by 1.1%; RSI14=44 |
|   14 | Corn / ZC=F            |  43.3 |   Yes    | —               | 20d down -2.7%; below MA20 by 3.5%; RSI14=34 |
|   19 | Wheat / ZW=F           |  36.1 |   Yes    | —               | 20d down -5.5%; below MA20 by 2.9%; RSI14=37 |
|   21 | Gold / GC=F            |  34.5 |   Yes    | —               | 20d down -5.7%; below MA20 by 2.8%; RSI14=22 |
|   24 | Platinum / PL=F        |  17.3 |   Yes    | —               | 20d down -9.5%; below MA20 by 6.5%; RSI14=27 |
|   25 | Silver / SI=F          |  13.9 |   Yes    | —               | 20d down -8.1%; below MA20 by 5.9%; RSI14=21 |
|   27 | Natural Gas / NG=F     |  72.7 |    No    | malformed_input | Suppressed: malformed_input                  |
|   29 | Copper / HG=F          |  53.3 |    No    | malformed_input | Suppressed: malformed_input                  |
|   32 | WTI Crude Oil / CL=F   |  35.1 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    1 | Microsoft Corporation / MSFT                                                   |  78.5 |   Yes    | —                             | 20d up +6.1%; above MA20 by 2.9%; RSI14=71   |
|    2 | Apple Inc. / AAPL                                                              |  75.8 |   Yes    | —                             | 20d up +4.2%; above MA20 by 1.6%; RSI14=55   |
|    6 | NVIDIA Corporation / NVDA                                                      |  60.0 |   Yes    | —                             | 20d up +5.6%; above MA20 by 1.9%; RSI14=61   |
|    8 | Meta Platforms Inc. / META                                                     |  57.9 |   Yes    | —                             | 20d up +12.0%; above MA20 by 0.8%; RSI14=61  |
|    9 | Tesla Inc. / TSLA                                                              |  57.0 |   Yes    | —                             | 20d up +3.1%; above MA20 by 2.0%; RSI14=57   |
|   11 | Alphabet Inc. Class A / GOOGL                                                  |  54.9 |   Yes    | —                             | 20d up +4.7%; above MA20 by 0.9%; RSI14=49   |
|   12 | Amazon.com Inc. / AMZN                                                         |  50.6 |   Yes    | —                             | 20d up +0.9%; above MA20 by 0.9%; RSI14=50   |
|   18 | JPMorgan Chase & Co. / JPM                                                     |  37.6 |   Yes    | —                             | 20d down -5.8%; below MA20 by 2.3%; RSI14=30 |
|   20 | UnitedHealth Group Inc. / UNH                                                  |  35.8 |   Yes    | —                             | 20d down -3.9%; below MA20 by 1.0%; RSI14=44 |
|   26 | Exxon Mobil Corporation / XOM                                                  |  81.5 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   30 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  49.1 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   31 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  43.9 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   33 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  27.6 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    3 | S&P 500 / ^GSPC                     |  74.2 |   Yes    | —            | 20d up +2.3%; above MA20 by 0.9%; RSI14=61   |
|    4 | NASDAQ 100 / ^NDX                   |  70.9 |   Yes    | —            | 20d up +5.6%; above MA20 by 1.6%; RSI14=67   |
|    7 | Dow Jones Industrial Average / ^DJI |  59.7 |   Yes    | —            | 20d down -1.6%; below MA20 by 0.7%; RSI14=44 |
|   13 | FTSE 100 / ^FTSE                    |  50.3 |   Yes    | —            | 20d down -1.6%; below MA20 by 1.7%; RSI14=33 |
|   15 | Russell 2000 / ^RUT                 |  40.6 |   Yes    | —            | 20d down -3.3%; below MA20 by 1.7%; RSI14=36 |
|   16 | DAX / ^GDAXI                        |  39.7 |   Yes    | —            | 20d down -2.2%; below MA20 by 2.1%; RSI14=40 |
|   17 | Euro Stoxx 50 / ^STOXX50E           |  39.4 |   Yes    | —            | 20d down -2.3%; below MA20 by 2.2%; RSI14=41 |
|   22 | CAC 40 / ^FCHI                      |  24.9 |   Yes    | —            | 20d down -4.8%; below MA20 by 3.6%; RSI14=26 |
|   23 | Hang Seng / ^HSI                    |  23.9 |   Yes    | —            | 20d down -5.9%; below MA20 by 3.2%; RSI14=36 |
|   28 | Nikkei 225 / ^N225                  |  63.9 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-10-08 |
| 7203.T    | 2026-10-08 |
| 8306.T    | 2026-10-08 |
| AAPL      | 2026-10-08 |
| AMZN      | 2026-10-08 |
| BZ=F      | 2026-10-08 |
| CL=F      | 2026-10-08 |
| GC=F      | 2026-10-08 |
| GOOGL     | 2026-10-08 |
| HG=F      | 2026-10-08 |
| JPM       | 2026-10-08 |
| META      | 2026-10-08 |
| MSFT      | 2026-10-08 |
| NG=F      | 2026-10-08 |
| NVDA      | 2026-10-08 |
| PL=F      | 2026-10-08 |
| SI=F      | 2026-10-08 |
| TSLA      | 2026-10-08 |
| UNH       | 2026-10-08 |
| XOM       | 2026-10-08 |
| ZC=F      | 2026-10-08 |
| ZS=F      | 2026-10-08 |
| ZW=F      | 2026-10-08 |
| ^DJI      | 2026-10-08 |
| ^FCHI     | 2026-10-08 |
| ^FTSE     | 2026-10-08 |
| ^GDAXI    | 2026-10-08 |
| ^GSPC     | 2026-10-08 |
| ^HSI      | 2026-10-08 |
| ^N225     | 2026-10-08 |
| ^NDX      | 2026-10-08 |
| ^RUT      | 2026-10-08 |
| ^STOXX50E | 2026-10-08 |

## Symbol Details

### Microsoft Corporation / MSFT (score 78.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.3% |
| ret_5d     |  +1.9% |
| ret_20d    |  +6.1% |
| ret_60d    | +32.1% |
| ma20_dist  |  +2.9% |
| ma50_dist  |  +4.8% |
| vol_20d    |  21.0% |
| mdd_60d    |   5.1% |
| rsi_14     |   70.5 |
| zscore_20d |    1.2 |

### Apple Inc. / AAPL (score 75.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | +3.1% |
| ret_20d    | +4.2% |
| ret_60d    | +4.0% |
| ma20_dist  | +1.6% |
| ma50_dist  | +5.6% |
| vol_20d    | 16.3% |
| mdd_60d    | 11.0% |
| rsi_14     |  55.1 |
| zscore_20d |   1.6 |

### S&P 500 / ^GSPC (score 74.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | +1.3% |
| ret_20d    | +2.3% |
| ret_60d    | +2.5% |
| ma20_dist  | +0.9% |
| ma50_dist  | +1.0% |
| vol_20d    |  9.9% |
| mdd_60d    |  3.2% |
| rsi_14     |  60.9 |
| zscore_20d |   1.0 |

### NASDAQ 100 / ^NDX (score 70.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.4% |
| ret_5d     | +0.7% |
| ret_20d    | +5.6% |
| ret_60d    | +4.1% |
| ma20_dist  | +1.6% |
| ma50_dist  | +3.4% |
| vol_20d    | 15.4% |
| mdd_60d    |  6.7% |
| rsi_14     |  66.6 |
| zscore_20d |   0.7 |

### Brent Crude Oil / BZ=F (score 60.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +4.1% |
| ret_5d     |  +1.9% |
| ret_20d    |  -3.1% |
| ret_60d    | +14.6% |
| ma20_dist  |  +0.8% |
| ma50_dist  |  +8.5% |
| vol_20d    |  35.5% |
| mdd_60d    |  21.2% |
| rsi_14     |   50.8 |
| zscore_20d |    0.4 |

### NVIDIA Corporation / NVDA (score 60.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.9% |
| ret_5d     | -0.2% |
| ret_20d    | +5.6% |
| ret_60d    | +8.5% |
| ma20_dist  | +1.9% |
| ma50_dist  | +4.2% |
| vol_20d    | 24.4% |
| mdd_60d    | 10.4% |
| rsi_14     |  60.9 |
| zscore_20d |   0.5 |

### Dow Jones Industrial Average / ^DJI (score 59.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | +0.6% |
| ret_20d    | -1.6% |
| ret_60d    | -2.7% |
| ma20_dist  | -0.7% |
| ma50_dist  | -2.7% |
| vol_20d    |  9.7% |
| mdd_60d    |  6.3% |
| rsi_14     |  43.5 |
| zscore_20d |  -0.8 |

### Meta Platforms Inc. / META (score 57.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.1% |
| ret_5d     |  -0.7% |
| ret_20d    | +12.0% |
| ret_60d    |  +5.8% |
| ma20_dist  |  +0.8% |
| ma50_dist  | +13.4% |
| vol_20d    |  52.4% |
| mdd_60d    |  18.9% |
| rsi_14     |   60.8 |
| zscore_20d |    0.2 |

### Tesla Inc. / TSLA (score 57.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | +5.9% |
| ret_20d    | +3.1% |
| ret_60d    | -4.9% |
| ma20_dist  | +2.0% |
| ma50_dist  | +6.2% |
| vol_20d    | 29.1% |
| mdd_60d    | 23.7% |
| rsi_14     |  56.9 |
| zscore_20d |   0.7 |

### Soybeans / ZS=F (score 55.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | +0.3% |
| ret_20d    | -2.2% |
| ret_60d    | +5.0% |
| ma20_dist  | -1.1% |
| ma50_dist  | +2.5% |
| vol_20d    | 19.5% |
| mdd_60d    |  8.1% |
| rsi_14     |  44.1 |
| zscore_20d |  -0.9 |

### Alphabet Inc. Class A / GOOGL (score 54.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | +3.0% |
| ret_20d    | +4.7% |
| ret_60d    | -6.1% |
| ma20_dist  | +0.9% |
| ma50_dist  | +0.7% |
| vol_20d    | 23.8% |
| mdd_60d    | 12.4% |
| rsi_14     |  48.9 |
| zscore_20d |   0.7 |

### Amazon.com Inc. / AMZN (score 50.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.3% |
| ret_5d     | +2.3% |
| ret_20d    | +0.9% |
| ret_60d    | -0.4% |
| ma20_dist  | +0.9% |
| ma50_dist  | -1.7% |
| vol_20d    | 23.0% |
| mdd_60d    | 13.4% |
| rsi_14     |  50.4 |
| zscore_20d |   0.6 |

### FTSE 100 / ^FTSE (score 50.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | +0.1% |
| ret_20d    | -1.6% |
| ret_60d    | -0.7% |
| ma20_dist  | -1.7% |
| ma50_dist  | -2.7% |
| vol_20d    | 10.6% |
| mdd_60d    |  4.4% |
| rsi_14     |  32.9 |
| zscore_20d |  -1.7 |

### Corn / ZC=F (score 43.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.3% |
| ret_5d     |  -0.4% |
| ret_20d    |  -2.7% |
| ret_60d    | +11.3% |
| ma20_dist  |  -3.5% |
| ma50_dist  |  +0.7% |
| vol_20d    |  27.4% |
| mdd_60d    |   8.4% |
| rsi_14     |   33.8 |
| zscore_20d |   -1.2 |

### Russell 2000 / ^RUT (score 40.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.0% |
| ret_5d     | -0.4% |
| ret_20d    | -3.3% |
| ret_60d    | -6.1% |
| ma20_dist  | -1.7% |
| ma50_dist  | -4.8% |
| vol_20d    | 10.6% |
| mdd_60d    |  9.0% |
| rsi_14     |  35.7 |
| zscore_20d |  -1.5 |

### DAX / ^GDAXI (score 39.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.2% |
| ret_5d     | -0.5% |
| ret_20d    | -2.2% |
| ret_60d    | -0.4% |
| ma20_dist  | -2.1% |
| ma50_dist  | -3.9% |
| vol_20d    | 12.9% |
| mdd_60d    |  6.6% |
| rsi_14     |  39.6 |
| zscore_20d |  -2.5 |

### Euro Stoxx 50 / ^STOXX50E (score 39.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.9% |
| ret_5d     | -0.8% |
| ret_20d    | -2.3% |
| ret_60d    | -2.5% |
| ma20_dist  | -2.2% |
| ma50_dist  | -3.9% |
| vol_20d    | 13.3% |
| mdd_60d    |  6.5% |
| rsi_14     |  40.5 |
| zscore_20d |  -2.6 |

### JPMorgan Chase & Co. / JPM (score 37.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | -0.0% |
| ret_20d    | -5.8% |
| ret_60d    | -4.5% |
| ma20_dist  | -2.3% |
| ma50_dist  | -5.3% |
| vol_20d    | 17.5% |
| mdd_60d    |  9.9% |
| rsi_14     |  30.2 |
| zscore_20d |  -0.9 |

### Wheat / ZW=F (score 36.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | +0.1% |
| ret_20d    | -5.5% |
| ret_60d    | +1.4% |
| ma20_dist  | -2.9% |
| ma50_dist  | -1.9% |
| vol_20d    | 24.1% |
| mdd_60d    | 11.9% |
| rsi_14     |  37.2 |
| zscore_20d |  -1.2 |

### UnitedHealth Group Inc. / UNH (score 35.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.3% |
| ret_5d     |  +1.6% |
| ret_20d    |  -3.9% |
| ret_60d    | -11.4% |
| ma20_dist  |  -1.0% |
| ma50_dist  |  -4.6% |
| vol_20d    |  19.2% |
| mdd_60d    |  16.3% |
| rsi_14     |   43.7 |
| zscore_20d |   -1.0 |

### Gold / GC=F (score 34.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | -1.1% |
| ret_20d    | -5.7% |
| ret_60d    | +2.1% |
| ma20_dist  | -2.8% |
| ma50_dist  | -5.4% |
| vol_20d    | 16.3% |
| mdd_60d    | 12.0% |
| rsi_14     |  21.8 |
| zscore_20d |  -1.2 |

### CAC 40 / ^FCHI (score 24.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | -1.3% |
| ret_20d    | -4.8% |
| ret_60d    | -7.7% |
| ma20_dist  | -3.6% |
| ma50_dist  | -6.8% |
| vol_20d    | 11.9% |
| mdd_60d    | 11.4% |
| rsi_14     |  26.1 |
| zscore_20d |  -2.1 |

### Hang Seng / ^HSI (score 23.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.4% |
| ret_5d     | -3.4% |
| ret_20d    | -5.9% |
| ret_60d    | -3.6% |
| ma20_dist  | -3.2% |
| ma50_dist  | -5.5% |
| vol_20d    | 14.4% |
| mdd_60d    |  8.5% |
| rsi_14     |  35.6 |
| zscore_20d |  -2.2 |

### Platinum / PL=F (score 17.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | -4.7% |
| ret_20d    | -9.5% |
| ret_60d    | -0.0% |
| ma20_dist  | -6.5% |
| ma50_dist  | -8.4% |
| vol_20d    | 25.8% |
| mdd_60d    | 15.1% |
| rsi_14     |  26.7 |
| zscore_20d |  -2.0 |

### Silver / SI=F (score 13.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.4% |
| ret_5d     | -2.7% |
| ret_20d    | -8.1% |
| ret_60d    | +0.4% |
| ma20_dist  | -5.9% |
| ma50_dist  | -8.7% |
| vol_20d    | 26.1% |
| mdd_60d    | 15.0% |
| rsi_14     |  21.0 |
| zscore_20d |  -1.6 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Microsoft Corporation / MSFT        |  12.4286 |           2.4% |                 0.48x |       24.8571 |            4.8% |
| Apple Inc. / AAPL                   |   6.2350 |           1.8% |                 0.61x |       12.4700 |            3.7% |
| S&P 500 / ^GSPC                     |  68.4658 |           0.9% |                 1.01x |      136.9315 |            1.8% |
| NASDAQ 100 / ^NDX                   | 396.9106 |           1.3% |                 0.65x |      793.8211 |            2.6% |
| Brent Crude Oil / BZ=F              |   4.8071 |           4.6% |                 0.28x |        9.6143 |            9.2% |
| NVIDIA Corporation / NVDA           |   5.3514 |           2.3% |                 0.41x |       10.7029 |            4.6% |
| Dow Jones Industrial Average / ^DJI | 475.5165 |           0.9% |                 1.03x |      951.0329 |            1.9% |
| Meta Platforms Inc. / META          |  27.4304 |           3.8% |                 0.19x |       54.8607 |            7.6% |
| Tesla Inc. / TSLA                   |  11.0664 |           3.0% |                 0.34x |       22.1329 |            5.9% |
| Soybeans / ZS=F                     |  21.1250 |           1.6% |                 0.51x |       42.2500 |            3.3% |
| Alphabet Inc. Class A / GOOGL       |   8.8143 |           2.5% |                 0.42x |       17.6286 |            5.1% |
| Amazon.com Inc. / AMZN              |   5.4257 |           2.1% |                 0.43x |       10.8514 |            4.3% |
| FTSE 100 / ^FTSE                    | 104.9927 |           1.0% |                 0.95x |      209.9854 |            2.0% |
| Corn / ZC=F                         |  11.0893 |           2.2% |                 0.36x |       22.1786 |            4.4% |
| Russell 2000 / ^RUT                 |  34.7521 |           1.2% |                 0.95x |       69.5043 |            2.5% |
| DAX / ^GDAXI                        | 313.2758 |           1.3% |                 0.78x |      626.5516 |            2.5% |
| Euro Stoxx 50 / ^STOXX50E           |  77.2735 |           1.3% |                 0.75x |      154.5470 |            2.5% |
| JPMorgan Chase & Co. / JPM          |   5.8543 |           1.8% |                 0.57x |       11.7087 |            3.5% |
| Wheat / ZW=F                        |  16.6071 |           2.4% |                 0.42x |       33.2143 |            4.9% |
| UnitedHealth Group Inc. / UNH       |   8.0479 |           2.2% |                 0.52x |       16.0957 |            4.3% |
| Gold / GC=F                         |  80.8500 |           1.9% |                 0.62x |      161.7000 |            3.9% |
| CAC 40 / ^FCHI                      |  93.3778 |           1.2% |                 0.84x |      186.7557 |            2.4% |
| Hang Seng / ^HSI                    | 312.4429 |           1.3% |                 0.69x |      624.8859 |            2.6% |
| Platinum / PL=F                     |  34.0929 |           2.1% |                 0.39x |       68.1857 |            4.2% |
| Silver / SI=F                       |   1.2326 |           2.1% |                 0.38x |        2.4651 |            4.2% |

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

Scoring engine version: **1.0.0** | Git commit: **a7520f5**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
