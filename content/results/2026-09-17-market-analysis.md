+++
title = "Market Analysis 2026-09-17"
date = "2026-09-17T00:00:00+00:00"
draft = false
summary = "Bearish market: 25 reliable instruments. Top signal: ZC=F (score 75.2)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-09-17.json", "data/history/2026-09-17.json"]
market_regime = "Bearish"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "1d66b29"
+++

## Market Regime

**Bearish** — 8 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Corn / ZC=F** — score 75.2, 20d return +12.9%, RSI14=65. 20d up +12.9%; above MA20 by 4.6%; RSI14=65
- **Meta Platforms Inc. / META** — score 74.8, 20d return +23.8%, RSI14=84. 20d up +23.8%; above MA20 by 11.9%; RSI14=84
- **Soybeans / ZS=F** — score 73.6, 20d return +8.0%, RSI14=68. 20d up +8.0%; above MA20 by 3.5%; RSI14=68
- **Apple Inc. / AAPL** — score 71.8, 20d return +7.2%, RSI14=67. 20d up +7.2%; above MA20 by 3.8%; RSI14=67
- **Brent Crude Oil / BZ=F** — score 66.1, 20d return +12.8%, RSI14=78. 20d up +12.8%; above MA20 by 9.4%; RSI14=78

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                        | Applies To                    |
| ---------- | ---------------------------- | ----------------------------- |
| 2026-09-18 | BOJ monetary policy decision | 6758.T, 7203.T, 8306.T, ^N225 |

## Signal History

Compared with the previous available report (**2026-09-16**).

- **New top-5:** None
- **Persistent top signals:** BZ=F (9 reports), AAPL (5 reports), META (4 reports), ZS=F (3 reports), ZC=F (2 reports)
- **Dropped from top-5:** None

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +0 |    +0.9 |
| 7203.T    |     +1 |    -2.4 |
| 8306.T    |     +1 |    +4.2 |
| AAPL      |     +1 |    +5.8 |
| AMZN      |     +0 |    +0.9 |
| BZ=F      |     -3 |   -10.9 |
| CL=F      |     +0 |   -11.2 |
| GC=F      |     +4 |    +7.3 |
| GOOGL     |     +1 |    +2.7 |
| HG=F      |     +0 |    +5.2 |
| JPM       |    -11 |   -19.1 |
| META      |     +2 |    +2.7 |
| MSFT      |     -1 |    -4.8 |
| NG=F      |     -1 |    -3.9 |
| NVDA      |     +3 |   +10.3 |
| PL=F      |     -1 |    +0.3 |
| SI=F      |     +1 |    +5.5 |
| TSLA      |     +0 |    +6.4 |
| UNH       |     +0 |    +1.8 |
| XOM       |     -1 |   -20.6 |
| ZC=F      |     +0 |    -4.8 |
| ZS=F      |     +0 |    -1.8 |
| ZW=F      |     +1 |    -0.3 |
| ^DJI      |     -9 |   -14.8 |
| ^FCHI     |     +3 |    +9.7 |
| ^FTSE     |     +1 |    +3.6 |
| ^GDAXI    |     +3 |    +5.5 |
| ^GSPC     |     -1 |    -3.9 |
| ^HSI      |     -1 |    +3.3 |
| ^N225     |     +0 |    +8.2 |
| ^NDX      |     +2 |    +5.8 |
| ^RUT      |     +0 |    -0.9 |
| ^STOXX50E |     +5 |    +9.7 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **WTI Crude Oil / CL=F** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Natural Gas / NG=F** — malformed_input
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
|    1 | Corn / ZC=F            |  75.2 |   Yes    | —               | 20d up +12.9%; above MA20 by 4.6%; RSI14=65  |
|    3 | Soybeans / ZS=F        |  73.6 |   Yes    | —               | 20d up +8.0%; above MA20 by 3.5%; RSI14=68   |
|    5 | Brent Crude Oil / BZ=F |  66.1 |   Yes    | —               | 20d up +12.8%; above MA20 by 9.4%; RSI14=78  |
|    6 | Wheat / ZW=F           |  64.5 |   Yes    | —               | 20d up +7.4%; above MA20 by 1.1%; RSI14=50   |
|   14 | Gold / GC=F            |  43.6 |   Yes    | —               | 20d down -4.0%; below MA20 by 2.7%; RSI14=31 |
|   15 | Platinum / PL=F        |  43.6 |   Yes    | —               | 20d down -2.6%; below MA20 by 2.3%; RSI14=42 |
|   21 | Silver / SI=F          |  35.5 |   Yes    | —               | 20d down -5.5%; below MA20 by 3.3%; RSI14=35 |
|   26 | WTI Crude Oil / CL=F   |  69.1 |    No    | malformed_input | Suppressed: malformed_input                  |
|   30 | Natural Gas / NG=F     |  50.6 |    No    | malformed_input | Suppressed: malformed_input                  |
|   32 | Copper / HG=F          |  44.2 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    2 | Meta Platforms Inc. / META                                                     |  74.8 |   Yes    | —                             | 20d up +23.8%; above MA20 by 11.9%; RSI14=84 |
|    4 | Apple Inc. / AAPL                                                              |  71.8 |   Yes    | —                             | 20d up +7.2%; above MA20 by 3.8%; RSI14=67   |
|    7 | Microsoft Corporation / MSFT                                                   |  60.9 |   Yes    | —                             | 20d up +2.0%; below MA20 by 1.2%; RSI14=47   |
|   10 | Alphabet Inc. Class A / GOOGL                                                  |  50.9 |   Yes    | —                             | 20d down -0.3%; above MA20 by 0.5%; RSI14=51 |
|   16 | Tesla Inc. / TSLA                                                              |  43.3 |   Yes    | —                             | 20d up +6.3%; above MA20 by 0.1%; RSI14=55   |
|   18 | NVIDIA Corporation / NVDA                                                      |  41.2 |   Yes    | —                             | 20d down -2.5%; below MA20 by 2.0%; RSI14=53 |
|   19 | JPMorgan Chase & Co. / JPM                                                     |  40.6 |   Yes    | —                             | 20d down -3.9%; below MA20 by 1.7%; RSI14=41 |
|   24 | Amazon.com Inc. / AMZN                                                         |  19.1 |   Yes    | —                             | 20d down -5.2%; below MA20 by 4.4%; RSI14=36 |
|   25 | UnitedHealth Group Inc. / UNH                                                  |  18.2 |   Yes    | —                             | 20d down -4.2%; below MA20 by 3.6%; RSI14=33 |
|   27 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  61.8 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   28 | Exxon Mobil Corporation / XOM                                                  |  57.9 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   29 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  50.9 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   31 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  49.1 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    8 | FTSE 100 / ^FTSE                    |  57.3 |   Yes    | —            | 20d down -0.4%; below MA20 by 0.7%; RSI14=35 |
|    9 | DAX / ^GDAXI                        |  52.1 |   Yes    | —            | 20d down -2.1%; below MA20 by 1.5%; RSI14=32 |
|   11 | S&P 500 / ^GSPC                     |  46.7 |   Yes    | —            | 20d down -1.8%; below MA20 by 1.4%; RSI14=40 |
|   12 | Euro Stoxx 50 / ^STOXX50E           |  46.7 |   Yes    | —            | 20d down -2.8%; below MA20 by 1.8%; RSI14=36 |
|   13 | NASDAQ 100 / ^NDX                   |  44.2 |   Yes    | —            | 20d down -1.9%; below MA20 by 1.1%; RSI14=45 |
|   17 | CAC 40 / ^FCHI                      |  42.4 |   Yes    | —            | 20d down -4.2%; below MA20 by 1.9%; RSI14=36 |
|   20 | Hang Seng / ^HSI                    |  37.0 |   Yes    | —            | 20d down -3.1%; below MA20 by 2.4%; RSI14=30 |
|   22 | Dow Jones Industrial Average / ^DJI |  28.8 |   Yes    | —            | 20d down -3.5%; below MA20 by 2.8%; RSI14=30 |
|   23 | Russell 2000 / ^RUT                 |  24.6 |   Yes    | —            | 20d down -5.3%; below MA20 by 3.3%; RSI14=26 |
|   33 | Nikkei 225 / ^N225                  |  33.6 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-09-16 |
| 7203.T    | 2026-09-16 |
| 8306.T    | 2026-09-16 |
| AAPL      | 2026-09-16 |
| AMZN      | 2026-09-16 |
| BZ=F      | 2026-09-16 |
| CL=F      | 2026-09-16 |
| GC=F      | 2026-09-16 |
| GOOGL     | 2026-09-16 |
| HG=F      | 2026-09-16 |
| JPM       | 2026-09-16 |
| META      | 2026-09-16 |
| MSFT      | 2026-09-16 |
| NG=F      | 2026-09-16 |
| NVDA      | 2026-09-16 |
| PL=F      | 2026-09-16 |
| SI=F      | 2026-09-16 |
| TSLA      | 2026-09-16 |
| UNH       | 2026-09-16 |
| XOM       | 2026-09-16 |
| ZC=F      | 2026-09-16 |
| ZS=F      | 2026-09-16 |
| ZW=F      | 2026-09-16 |
| ^DJI      | 2026-09-16 |
| ^FCHI     | 2026-09-16 |
| ^FTSE     | 2026-09-16 |
| ^GDAXI    | 2026-09-16 |
| ^GSPC     | 2026-09-16 |
| ^HSI      | 2026-09-16 |
| ^N225     | 2026-09-16 |
| ^NDX      | 2026-09-16 |
| ^RUT      | 2026-09-16 |
| ^STOXX50E | 2026-09-16 |

## Symbol Details

### Corn / ZC=F (score 75.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.3% |
| ret_5d     |  +5.2% |
| ret_20d    | +12.9% |
| ret_60d    | +28.8% |
| ma20_dist  |  +4.6% |
| ma50_dist  | +12.4% |
| vol_20d    |  39.4% |
| mdd_60d    |   6.0% |
| rsi_14     |   65.4 |
| zscore_20d |    1.7 |

### Meta Platforms Inc. / META (score 74.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.5% |
| ret_5d     |  +3.0% |
| ret_20d    | +23.8% |
| ret_60d    | +19.4% |
| ma20_dist  | +11.9% |
| ma50_dist  | +11.3% |
| vol_20d    |  27.3% |
| mdd_60d    |  20.9% |
| rsi_14     |   83.8 |
| zscore_20d |    1.7 |

### Soybeans / ZS=F (score 73.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.1% |
| ret_5d     |  +1.9% |
| ret_20d    |  +8.0% |
| ret_60d    | +17.1% |
| ma20_dist  |  +3.5% |
| ma50_dist  |  +7.8% |
| vol_20d    |  20.4% |
| mdd_60d    |   8.1% |
| rsi_14     |   67.5 |
| zscore_20d |    1.3 |

### Apple Inc. / AAPL (score 71.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.3% |
| ret_5d     |  +5.4% |
| ret_20d    |  +7.2% |
| ret_60d    | +11.9% |
| ma20_dist  |  +3.8% |
| ma50_dist  |  +4.2% |
| vol_20d    |  23.1% |
| mdd_60d    |  11.0% |
| rsi_14     |   67.5 |
| zscore_20d |    1.5 |

### Brent Crude Oil / BZ=F (score 66.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.7% |
| ret_5d     |  +4.6% |
| ret_20d    | +12.8% |
| ret_60d    | +47.0% |
| ma20_dist  |  +9.4% |
| ma50_dist  | +15.5% |
| vol_20d    |  38.9% |
| mdd_60d    |  21.2% |
| rsi_14     |   77.8 |
| zscore_20d |    1.4 |

### Wheat / ZW=F (score 64.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.3% |
| ret_5d     |  +2.7% |
| ret_20d    |  +7.4% |
| ret_60d    | +23.6% |
| ma20_dist  |  +1.1% |
| ma50_dist  |  +6.6% |
| vol_20d    |  42.0% |
| mdd_60d    |  10.7% |
| rsi_14     |   50.1 |
| zscore_20d |    0.3 |

### Microsoft Corporation / MSFT (score 60.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.4% |
| ret_5d     |  -0.3% |
| ret_20d    |  +2.0% |
| ret_60d    | +33.5% |
| ma20_dist  |  -1.2% |
| ma50_dist  |  +6.6% |
| vol_20d    |  20.8% |
| mdd_60d    |   5.6% |
| rsi_14     |   46.8 |
| zscore_20d |   -0.7 |

### FTSE 100 / ^FTSE (score 57.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +0.2% |
| ret_20d    | -0.4% |
| ret_60d    | +2.5% |
| ma20_dist  | -0.7% |
| ma50_dist  | -0.5% |
| vol_20d    |  7.7% |
| mdd_60d    |  2.7% |
| rsi_14     |  35.2 |
| zscore_20d |  -1.0 |

### DAX / ^GDAXI (score 52.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | -0.2% |
| ret_20d    | -2.1% |
| ret_60d    | +3.2% |
| ma20_dist  | -1.5% |
| ma50_dist  | -0.8% |
| vol_20d    | 10.9% |
| mdd_60d    |  4.5% |
| rsi_14     |  32.3 |
| zscore_20d |  -1.2 |

### Alphabet Inc. Class A / GOOGL (score 50.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | +3.7% |
| ret_20d    | -0.3% |
| ret_60d    | -1.9% |
| ma20_dist  | +0.5% |
| ma50_dist  | -0.9% |
| vol_20d    | 22.5% |
| mdd_60d    | 14.4% |
| rsi_14     |  50.9 |
| zscore_20d |   0.4 |

### S&P 500 / ^GSPC (score 46.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -1.1% |
| ret_20d    | -1.8% |
| ret_60d    | +1.1% |
| ma20_dist  | -1.4% |
| ma50_dist  | -0.8% |
| vol_20d    |  8.7% |
| mdd_60d    |  3.4% |
| rsi_14     |  39.6 |
| zscore_20d |  -2.2 |

### Euro Stoxx 50 / ^STOXX50E (score 46.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | -0.7% |
| ret_20d    | -2.8% |
| ret_60d    | +0.8% |
| ma20_dist  | -1.8% |
| ma50_dist  | -1.7% |
| vol_20d    | 10.5% |
| mdd_60d    |  4.8% |
| rsi_14     |  35.7 |
| zscore_20d |  -1.5 |

### NASDAQ 100 / ^NDX (score 44.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.0% |
| ret_5d     | -1.6% |
| ret_20d    | -1.9% |
| ret_60d    | -4.6% |
| ma20_dist  | -1.1% |
| ma50_dist  | -0.8% |
| vol_20d    | 11.6% |
| mdd_60d    | 10.2% |
| rsi_14     |  44.7 |
| zscore_20d |  -1.7 |

### Gold / GC=F (score 43.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.3% |
| ret_5d     | -1.6% |
| ret_20d    | -4.0% |
| ret_60d    | +7.6% |
| ma20_dist  | -2.7% |
| ma50_dist  | +1.3% |
| vol_20d    | 21.0% |
| mdd_60d    |  7.9% |
| rsi_14     |  30.8 |
| zscore_20d |  -1.0 |

### Platinum / PL=F (score 43.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | -6.9% |
| ret_20d    | -2.6% |
| ret_60d    | +9.3% |
| ma20_dist  | -2.3% |
| ma50_dist  | +2.3% |
| vol_20d    | 34.5% |
| mdd_60d    |  7.4% |
| rsi_14     |  42.4 |
| zscore_20d |  -0.9 |

### Tesla Inc. / TSLA (score 43.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.4% |
| ret_5d     |  -2.6% |
| ret_20d    |  +6.3% |
| ret_60d    | -11.6% |
| ma20_dist  |  +0.1% |
| ma50_dist  |  +1.8% |
| vol_20d    |  49.8% |
| mdd_60d    |  29.9% |
| rsi_14     |   55.1 |
| zscore_20d |    0.0 |

### CAC 40 / ^FCHI (score 42.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | -0.2% |
| ret_20d    | -4.2% |
| ret_60d    | -2.9% |
| ma20_dist  | -1.9% |
| ma50_dist  | -3.3% |
| vol_20d    | 11.4% |
| mdd_60d    |  7.3% |
| rsi_14     |  36.4 |
| zscore_20d |  -1.2 |

### NVIDIA Corporation / NVDA (score 41.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.8% |
| ret_5d     | -4.3% |
| ret_20d    | -2.5% |
| ret_60d    | +2.5% |
| ma20_dist  | -2.0% |
| ma50_dist  | +0.2% |
| vol_20d    | 44.3% |
| mdd_60d    | 10.6% |
| rsi_14     |  53.2 |
| zscore_20d |  -0.7 |

### JPMorgan Chase & Co. / JPM (score 40.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | -1.6% |
| ret_20d    | -3.9% |
| ret_60d    | +5.7% |
| ma20_dist  | -1.7% |
| ma50_dist  | -1.0% |
| vol_20d    | 15.5% |
| mdd_60d    |  4.5% |
| rsi_14     |  40.8 |
| zscore_20d |  -2.0 |

### Hang Seng / ^HSI (score 37.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | -2.2% |
| ret_20d    | -3.1% |
| ret_60d    | +5.9% |
| ma20_dist  | -2.4% |
| ma50_dist  | -2.2% |
| vol_20d    | 13.2% |
| mdd_60d    |  5.2% |
| rsi_14     |  29.5 |
| zscore_20d |  -1.8 |

### Silver / SI=F (score 35.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.7% |
| ret_5d     | -5.4% |
| ret_20d    | -5.5% |
| ret_60d    | +8.6% |
| ma20_dist  | -3.3% |
| ma50_dist  | +1.6% |
| vol_20d    | 32.8% |
| mdd_60d    |  9.7% |
| rsi_14     |  35.0 |
| zscore_20d |  -1.1 |

### Dow Jones Industrial Average / ^DJI (score 28.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.2% |
| ret_5d     | -1.8% |
| ret_20d    | -3.5% |
| ret_60d    | -0.5% |
| ma20_dist  | -2.8% |
| ma50_dist  | -2.7% |
| vol_20d    | 11.6% |
| mdd_60d    |  5.3% |
| rsi_14     |  30.3 |
| zscore_20d |  -2.4 |

### Russell 2000 / ^RUT (score 24.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -2.1% |
| ret_20d    | -5.3% |
| ret_60d    | -4.8% |
| ma20_dist  | -3.3% |
| ma50_dist  | -3.9% |
| vol_20d    | 12.2% |
| mdd_60d    |  6.8% |
| rsi_14     |  25.6 |
| zscore_20d |  -1.9 |

### Amazon.com Inc. / AMZN (score 19.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | -2.6% |
| ret_20d    | -5.2% |
| ret_60d    | +5.7% |
| ma20_dist  | -4.4% |
| ma50_dist  | -3.8% |
| vol_20d    | 26.6% |
| mdd_60d    | 13.4% |
| rsi_14     |  36.3 |
| zscore_20d |  -2.2 |

### UnitedHealth Group Inc. / UNH (score 18.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | -3.9% |
| ret_20d    | -4.2% |
| ret_60d    | -7.7% |
| ma20_dist  | -3.6% |
| ma50_dist  | -7.4% |
| vol_20d    | 21.7% |
| mdd_60d    | 14.0% |
| rsi_14     |  32.6 |
| zscore_20d |  -1.9 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Corn / ZC=F                         |  10.6071 |           2.0% |                 0.25x |       21.2143 |            4.0% |
| Meta Platforms Inc. / META          |  21.3214 |           3.2% |                 0.37x |       42.6429 |            6.3% |
| Soybeans / ZS=F                     |  19.5179 |           1.5% |                 0.49x |       39.0357 |            3.0% |
| Apple Inc. / AAPL                   |   7.6771 |           2.3% |                 0.43x |       15.3543 |            4.6% |
| Brent Crude Oil / BZ=F              |   4.1050 |           3.9% |                 0.26x |        8.2100 |            7.8% |
| Wheat / ZW=F                        |  19.8393 |           2.7% |                 0.24x |       39.6786 |            5.4% |
| Microsoft Corporation / MSFT        |  10.6207 |           2.2% |                 0.48x |       21.2414 |            4.3% |
| FTSE 100 / ^FTSE                    |  96.4286 |           0.9% |                 1.31x |      192.8571 |            1.8% |
| DAX / ^GDAXI                        | 265.5615 |           1.0% |                 0.92x |      531.1230 |            2.1% |
| Alphabet Inc. Class A / GOOGL       |   7.7059 |           2.2% |                 0.44x |       15.4118 |            4.5% |
| S&P 500 / ^GSPC                     |  65.3806 |           0.9% |                 1.15x |      130.7612 |            1.7% |
| Euro Stoxx 50 / ^STOXX50E           |  65.9921 |           1.1% |                 0.96x |      131.9842 |            2.1% |
| NASDAQ 100 / ^NDX                   | 338.5086 |           1.2% |                 0.86x |      677.0173 |            2.3% |
| Gold / GC=F                         | 114.4285 |           2.6% |                 0.48x |      228.8569 |            5.2% |
| Platinum / PL=F                     |  34.1071 |           1.9% |                 0.29x |       68.2143 |            3.8% |
| Tesla Inc. / TSLA                   |  14.0443 |           3.9% |                 0.20x |       28.0886 |            7.8% |
| CAC 40 / ^FCHI                      |  82.9922 |           1.0% |                 0.88x |      165.9844 |            2.0% |
| NVIDIA Corporation / NVDA           |   7.5237 |           3.5% |                 0.23x |       15.0475 |            7.0% |
| JPMorgan Chase & Co. / JPM          |   6.7843 |           1.9% |                 0.65x |       13.5686 |            3.9% |
| Hang Seng / ^HSI                    | 312.5280 |           1.3% |                 0.75x |      625.0561 |            2.5% |
| Silver / SI=F                       |   1.9670 |           3.1% |                 0.30x |        3.9340 |            6.1% |
| Dow Jones Industrial Average / ^DJI | 529.0957 |           1.0% |                 0.86x |     1058.1914 |            2.1% |
| Russell 2000 / ^RUT                 |  32.7436 |           1.1% |                 0.82x |       65.4871 |            2.3% |
| Amazon.com Inc. / AMZN              |   5.9693 |           2.4% |                 0.38x |       11.9386 |            4.9% |
| UnitedHealth Group Inc. / UNH       |  10.2335 |           2.7% |                 0.46x |       20.4670 |            5.5% |

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

Scoring engine version: **1.0.0** | Git commit: **1d66b29**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
