+++
title = "Market Analysis 2026-09-14"
date = "2026-09-14T00:00:00+00:00"
draft = false
summary = "Bearish market: 25 reliable instruments. Top signal: AAPL (score 76.7)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-09-14.json", "data/history/2026-09-14.json"]
market_regime = "Bearish"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "671cd3b"
+++

## Market Regime

**Bearish** — 7 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Apple Inc. / AAPL** — score 76.7, 20d return +8.8%, RSI14=71. 20d up +8.8%; above MA20 by 4.9%; RSI14=71 ⚠️ Upcoming: FOMC rate decision (2026-09-16)
- **Meta Platforms Inc. / META** — score 70.3, 20d return +8.9%, RSI14=84. 20d up +8.9%; above MA20 by 10.5%; RSI14=84 ⚠️ Upcoming: FOMC rate decision (2026-09-16)
- **Brent Crude Oil / BZ=F** — score 68.2, 20d return +15.1%, RSI14=72. 20d up +15.1%; above MA20 by 10.6%; RSI14=72 ⚠️ Upcoming: FOMC rate decision (2026-09-16)
- **Microsoft Corporation / MSFT** — score 67.3, 20d return -0.1%, RSI14=57. 20d down -0.1%; above MA20 by 0.3%; RSI14=57 ⚠️ Upcoming: FOMC rate decision (2026-09-16)
- **JPMorgan Chase & Co. / JPM** — score 64.8, 20d return -1.9%, RSI14=57. 20d down -1.9%; below MA20 by 0.1%; RSI14=57 ⚠️ Upcoming: FOMC rate decision (2026-09-16)

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                        | Applies To                      |
| ---------- | ---------------------------- | ------------------------------- |
| 2026-09-16 | FOMC rate decision           | Commodity, Equity, Equity Index |
| 2026-09-18 | BOJ monetary policy decision | 6758.T, 7203.T, 8306.T, ^N225   |

## Signal History

Compared with the previous available report (**2026-09-11**).

- **New top-5:** JPM, META
- **Persistent top signals:** BZ=F (6 reports), AAPL (2 reports), MSFT (2 reports)
- **Dropped from top-5:** ZC=F, ZS=F

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +1 |   -13.0 |
| 7203.T    |     +1 |    +7.6 |
| 8306.T    |     +0 |    -6.7 |
| AAPL      |     +2 |    +4.5 |
| AMZN      |    +11 |   +17.3 |
| BZ=F      |     -1 |   -11.2 |
| CL=F      |     -1 |    -9.1 |
| GC=F      |     -1 |    +6.1 |
| GOOGL     |     +6 |   +13.0 |
| HG=F      |     +2 |    +4.2 |
| JPM       |     +2 |    +3.6 |
| META      |     +4 |    +6.1 |
| MSFT      |     +1 |    +0.3 |
| NG=F      |     -2 |    -8.2 |
| NVDA      |     -5 |    -0.3 |
| PL=F      |     -4 |    +0.0 |
| SI=F      |     +3 |    +7.9 |
| TSLA      |     -4 |    -2.4 |
| UNH       |     -1 |   -12.1 |
| XOM       |     +1 |    +2.1 |
| ZC=F      |     -3 |    -9.4 |
| ZS=F      |     -5 |   -17.0 |
| ZW=F      |     -8 |   -13.3 |
| ^DJI      |     +3 |    +8.2 |
| ^FCHI     |     +2 |    +6.4 |
| ^FTSE     |     -3 |    +1.2 |
| ^GDAXI    |     +2 |    +9.4 |
| ^GSPC     |     +1 |    +8.5 |
| ^HSI      |     -7 |    -7.3 |
| ^N225     |     -2 |   -19.4 |
| ^NDX      |     +2 |   +10.6 |
| ^RUT      |     -2 |    +1.5 |
| ^STOXX50E |     +5 |   +10.9 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Exxon Mobil Corporation / XOM** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **Natural Gas / NG=F** — malformed_input
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Nikkei 225 / ^N225** — missing_bars

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|    3 | Brent Crude Oil / BZ=F |  68.2 |   Yes    | —               | 20d up +15.1%; above MA20 by 10.6%; RSI14=72 |
|    6 | Soybeans / ZS=F        |  63.6 |   Yes    | —               | 20d up +7.3%; above MA20 by 1.6%; RSI14=61   |
|    7 | Corn / ZC=F            |  62.7 |   Yes    | —               | 20d up +5.3%; above MA20 by 1.7%; RSI14=44   |
|   16 | Wheat / ZW=F           |  45.5 |   Yes    | —               | 20d up +2.3%; below MA20 by 1.1%; RSI14=49   |
|   17 | Platinum / PL=F        |  45.1 |   Yes    | —               | 20d up +0.7%; below MA20 by 1.8%; RSI14=40   |
|   19 | Gold / GC=F            |  41.8 |   Yes    | —               | 20d down -1.2%; below MA20 by 2.7%; RSI14=31 |
|   22 | Silver / SI=F          |  33.0 |   Yes    | —               | 20d down -2.4%; below MA20 by 3.4%; RSI14=38 |
|   27 | WTI Crude Oil / CL=F   |  71.5 |    No    | malformed_input | Suppressed: malformed_input                  |
|   30 | Copper / HG=F          |  43.9 |    No    | malformed_input | Suppressed: malformed_input                  |
|   31 | Natural Gas / NG=F     |  36.4 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    1 | Apple Inc. / AAPL                                                              |  76.7 |   Yes    | —                             | 20d up +8.8%; above MA20 by 4.9%; RSI14=71   |
|    2 | Meta Platforms Inc. / META                                                     |  70.3 |   Yes    | —                             | 20d up +8.9%; above MA20 by 10.5%; RSI14=84  |
|    4 | Microsoft Corporation / MSFT                                                   |  67.3 |   Yes    | —                             | 20d down -0.1%; above MA20 by 0.3%; RSI14=57 |
|    5 | JPMorgan Chase & Co. / JPM                                                     |  64.8 |   Yes    | —                             | 20d down -1.9%; below MA20 by 0.1%; RSI14=57 |
|   10 | Amazon.com Inc. / AMZN                                                         |  50.0 |   Yes    | —                             | 20d down -3.1%; below MA20 by 0.8%; RSI14=48 |
|   13 | Alphabet Inc. Class A / GOOGL                                                  |  46.7 |   Yes    | —                             | 20d down -2.2%; below MA20 by 0.7%; RSI14=44 |
|   14 | Tesla Inc. / TSLA                                                              |  46.7 |   Yes    | —                             | 20d up +7.5%; above MA20 by 2.9%; RSI14=51   |
|   20 | NVIDIA Corporation / NVDA                                                      |  40.3 |   Yes    | —                             | 20d down -3.0%; below MA20 by 0.8%; RSI14=53 |
|   25 | UnitedHealth Group Inc. / UNH                                                  |  15.8 |   Yes    | —                             | 20d down -5.0%; below MA20 by 3.8%; RSI14=42 |
|   26 | Exxon Mobil Corporation / XOM                                                  |  74.5 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   28 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  57.3 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   29 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  50.9 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   32 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  23.3 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    8 | S&P 500 / ^GSPC                     |  61.5 |   Yes    | —            | 20d down -1.8%; below MA20 by 0.4%; RSI14=48 |
|    9 | NASDAQ 100 / ^NDX                   |  56.7 |   Yes    | —            | 20d down -2.4%; below MA20 by 0.1%; RSI14=51 |
|   11 | Dow Jones Industrial Average / ^DJI |  49.1 |   Yes    | —            | 20d down -2.4%; below MA20 by 1.1%; RSI14=42 |
|   12 | Euro Stoxx 50 / ^STOXX50E           |  47.0 |   Yes    | —            | 20d down -3.3%; below MA20 by 1.4%; RSI14=38 |
|   15 | FTSE 100 / ^FTSE                    |  46.7 |   Yes    | —            | 20d down -1.1%; below MA20 by 1.2%; RSI14=36 |
|   18 | DAX / ^GDAXI                        |  43.0 |   Yes    | —            | 20d down -3.3%; below MA20 by 1.8%; RSI14=38 |
|   21 | CAC 40 / ^FCHI                      |  35.5 |   Yes    | —            | 20d down -5.3%; below MA20 by 2.1%; RSI14=30 |
|   23 | Hang Seng / ^HSI                    |  31.8 |   Yes    | —            | 20d down -1.2%; below MA20 by 2.5%; RSI14=31 |
|   24 | Russell 2000 / ^RUT                 |  30.9 |   Yes    | —            | 20d down -4.9%; below MA20 by 2.6%; RSI14=31 |
|   33 | Nikkei 225 / ^N225                  |  21.5 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-09-11 |
| 7203.T    | 2026-09-11 |
| 8306.T    | 2026-09-11 |
| AAPL      | 2026-09-11 |
| AMZN      | 2026-09-11 |
| BZ=F      | 2026-09-11 |
| CL=F      | 2026-09-11 |
| GC=F      | 2026-09-11 |
| GOOGL     | 2026-09-11 |
| HG=F      | 2026-09-11 |
| JPM       | 2026-09-11 |
| META      | 2026-09-11 |
| MSFT      | 2026-09-11 |
| NG=F      | 2026-09-11 |
| NVDA      | 2026-09-11 |
| PL=F      | 2026-09-11 |
| SI=F      | 2026-09-11 |
| TSLA      | 2026-09-11 |
| UNH       | 2026-09-11 |
| XOM       | 2026-09-11 |
| ZC=F      | 2026-09-11 |
| ZS=F      | 2026-09-11 |
| ZW=F      | 2026-09-11 |
| ^DJI      | 2026-09-11 |
| ^FCHI     | 2026-09-11 |
| ^FTSE     | 2026-09-11 |
| ^GDAXI    | 2026-09-11 |
| ^GSPC     | 2026-09-11 |
| ^HSI      | 2026-09-11 |
| ^N225     | 2026-09-11 |
| ^NDX      | 2026-09-11 |
| ^RUT      | 2026-09-11 |
| ^STOXX50E | 2026-09-11 |

## Symbol Details

### Apple Inc. / AAPL (score 76.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.7% |
| ret_5d     |  +1.2% |
| ret_20d    |  +8.8% |
| ret_60d    | +11.0% |
| ma20_dist  |  +4.9% |
| ma50_dist  |  +4.5% |
| vol_20d    |  23.3% |
| mdd_60d    |  11.0% |
| rsi_14     |   70.6 |
| zscore_20d |    2.1 |

### Meta Platforms Inc. / META (score 70.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.6% |
| ret_5d     |  +6.1% |
| ret_20d    |  +8.9% |
| ret_60d    |  +8.0% |
| ma20_dist  | +10.5% |
| ma50_dist  |  +7.8% |
| vol_20d    |  36.1% |
| mdd_60d    |  20.9% |
| rsi_14     |   83.9 |
| zscore_20d |    1.8 |

### Brent Crude Oil / BZ=F (score 68.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.8% |
| ret_5d     |  +8.7% |
| ret_20d    | +15.1% |
| ret_60d    | +35.7% |
| ma20_dist  | +10.6% |
| ma50_dist  | +16.3% |
| vol_20d    |  36.7% |
| mdd_60d    |  21.2% |
| rsi_14     |   72.1 |
| zscore_20d |    2.0 |

### Microsoft Corporation / MSFT (score 67.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.6% |
| ret_5d     |  -2.8% |
| ret_20d    |  -0.1% |
| ret_60d    | +25.8% |
| ma20_dist  |  +0.3% |
| ma50_dist  |  +9.3% |
| vol_20d    |  21.1% |
| mdd_60d    |   7.0% |
| rsi_14     |   57.5 |
| zscore_20d |    0.1 |

### JPMorgan Chase & Co. / JPM (score 64.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.8% |
| ret_5d     | -1.6% |
| ret_20d    | -1.9% |
| ret_60d    | +8.1% |
| ma20_dist  | -0.1% |
| ma50_dist  | +1.3% |
| vol_20d    | 14.1% |
| mdd_60d    |  3.7% |
| rsi_14     |  56.8 |
| zscore_20d |  -0.2 |

### Soybeans / ZS=F (score 63.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.7% |
| ret_5d     |  -2.0% |
| ret_20d    |  +7.3% |
| ret_60d    | +14.7% |
| ma20_dist  |  +1.6% |
| ma50_dist  |  +5.1% |
| vol_20d    |  19.5% |
| mdd_60d    |   8.1% |
| rsi_14     |   61.1 |
| zscore_20d |    0.5 |

### Corn / ZC=F (score 62.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.7% |
| ret_5d     |  -1.0% |
| ret_20d    |  +5.3% |
| ret_60d    | +24.0% |
| ma20_dist  |  +1.7% |
| ma50_dist  |  +8.7% |
| vol_20d    |  40.3% |
| mdd_60d    |   6.0% |
| rsi_14     |   44.2 |
| zscore_20d |    0.5 |

### S&P 500 / ^GSPC (score 61.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | -1.2% |
| ret_20d    | -1.8% |
| ret_60d    | +1.9% |
| ma20_dist  | -0.4% |
| ma50_dist  | +0.7% |
| vol_20d    |  8.8% |
| mdd_60d    |  3.4% |
| rsi_14     |  48.4 |
| zscore_20d |  -0.6 |

### NASDAQ 100 / ^NDX (score 56.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | -0.4% |
| ret_20d    | -2.4% |
| ret_60d    | -2.0% |
| ma20_dist  | -0.1% |
| ma50_dist  | +0.6% |
| vol_20d    | 12.5% |
| mdd_60d    | 10.6% |
| rsi_14     |  51.1 |
| zscore_20d |  -0.1 |

### Amazon.com Inc. / AMZN (score 50.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.9% |
| ret_5d     | -0.8% |
| ret_20d    | -3.1% |
| ret_60d    | +4.4% |
| ma20_dist  | -0.8% |
| ma50_dist  | +0.6% |
| vol_20d    | 25.6% |
| mdd_60d    | 11.3% |
| rsi_14     |  48.0 |
| zscore_20d |  -0.6 |

### Dow Jones Industrial Average / ^DJI (score 49.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.0% |
| ret_5d     | -2.1% |
| ret_20d    | -2.4% |
| ret_60d    | +1.1% |
| ma20_dist  | -1.1% |
| ma50_dist  | -0.7% |
| vol_20d    | 10.9% |
| mdd_60d    |  4.2% |
| rsi_14     |  42.0 |
| zscore_20d |  -1.3 |

### Euro Stoxx 50 / ^STOXX50E (score 47.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | -1.1% |
| ret_20d    | -3.3% |
| ret_60d    | +0.5% |
| ma20_dist  | -1.4% |
| ma50_dist  | -0.9% |
| vol_20d    | 10.1% |
| mdd_60d    |  4.3% |
| rsi_14     |  37.8 |
| zscore_20d |  -1.4 |

### Alphabet Inc. Class A / GOOGL (score 46.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.8% |
| ret_5d     | -1.1% |
| ret_20d    | -2.2% |
| ret_60d    | -9.3% |
| ma20_dist  | -0.7% |
| ma50_dist  | -2.5% |
| vol_20d    | 18.8% |
| mdd_60d    | 14.4% |
| rsi_14     |  44.5 |
| zscore_20d |  -0.5 |

### Tesla Inc. / TSLA (score 46.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | -2.9% |
| ret_20d    | +7.5% |
| ret_60d    | -9.7% |
| ma20_dist  | +2.9% |
| ma50_dist  | +3.1% |
| vol_20d    | 49.5% |
| mdd_60d    | 29.9% |
| rsi_14     |  51.0 |
| zscore_20d |   1.0 |

### FTSE 100 / ^FTSE (score 46.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | -1.7% |
| ret_20d    | -1.1% |
| ret_60d    | +2.4% |
| ma20_dist  | -1.2% |
| ma50_dist  | -0.8% |
| vol_20d    |  7.4% |
| mdd_60d    |  2.7% |
| rsi_14     |  36.2 |
| zscore_20d |  -1.7 |

### Wheat / ZW=F (score 45.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.2% |
| ret_5d     |  -3.9% |
| ret_20d    |  +2.3% |
| ret_60d    | +18.3% |
| ma20_dist  |  -1.1% |
| ma50_dist  |  +4.1% |
| vol_20d    |  43.0% |
| mdd_60d    |  10.7% |
| rsi_14     |   48.8 |
| zscore_20d |   -0.3 |

### Platinum / PL=F (score 45.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | -1.5% |
| ret_20d    | +0.7% |
| ret_60d    | +8.0% |
| ma20_dist  | -1.8% |
| ma50_dist  | +3.5% |
| vol_20d    | 39.6% |
| mdd_60d    |  7.1% |
| rsi_14     |  40.0 |
| zscore_20d |  -0.7 |

### DAX / ^GDAXI (score 43.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.8% |
| ret_5d     | -1.8% |
| ret_20d    | -3.3% |
| ret_60d    | +2.3% |
| ma20_dist  | -1.8% |
| ma50_dist  | -0.7% |
| vol_20d    | 10.8% |
| mdd_60d    |  4.5% |
| rsi_14     |  38.3 |
| zscore_20d |  -1.7 |

### Gold / GC=F (score 41.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.0% |
| ret_5d     | -1.4% |
| ret_20d    | -1.2% |
| ret_60d    | +5.7% |
| ma20_dist  | -2.7% |
| ma50_dist  | +1.6% |
| vol_20d    | 25.2% |
| mdd_60d    |  7.6% |
| rsi_14     |  31.1 |
| zscore_20d |  -1.1 |

### NVIDIA Corporation / NVDA (score 40.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.0% |
| ret_5d     | -4.3% |
| ret_20d    | -3.0% |
| ret_60d    | +5.2% |
| ma20_dist  | -0.8% |
| ma50_dist  | +2.7% |
| vol_20d    | 43.3% |
| mdd_60d    | 10.6% |
| rsi_14     |  52.6 |
| zscore_20d |  -0.3 |

### CAC 40 / ^FCHI (score 35.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.8% |
| ret_5d     | -1.2% |
| ret_20d    | -5.3% |
| ret_60d    | -2.9% |
| ma20_dist  | -2.1% |
| ma50_dist  | -3.0% |
| vol_20d    | 11.1% |
| mdd_60d    |  7.0% |
| rsi_14     |  30.4 |
| zscore_20d |  -1.4 |

### Silver / SI=F (score 33.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | -2.3% |
| ret_20d    | -2.4% |
| ret_60d    | +4.1% |
| ma20_dist  | -3.4% |
| ma50_dist  | +2.5% |
| vol_20d    | 37.6% |
| mdd_60d    |  9.7% |
| rsi_14     |  38.3 |
| zscore_20d |  -1.3 |

### Hang Seng / ^HSI (score 31.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | -3.3% |
| ret_20d    | -1.2% |
| ret_60d    | +2.0% |
| ma20_dist  | -2.5% |
| ma50_dist  | -1.6% |
| vol_20d    | 13.7% |
| mdd_60d    |  5.2% |
| rsi_14     |  31.4 |
| zscore_20d |  -2.5 |

### Russell 2000 / ^RUT (score 30.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | -2.2% |
| ret_20d    | -4.9% |
| ret_60d    | -1.2% |
| ma20_dist  | -2.6% |
| ma50_dist  | -2.6% |
| vol_20d    | 12.9% |
| mdd_60d    |  5.8% |
| rsi_14     |  30.9 |
| zscore_20d |  -1.6 |

### UnitedHealth Group Inc. / UNH (score 15.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.4% |
| ret_5d     | -5.4% |
| ret_20d    | -5.0% |
| ret_60d    | -7.0% |
| ma20_dist  | -3.8% |
| ma50_dist  | -7.4% |
| vol_20d    | 20.3% |
| mdd_60d    | 13.1% |
| rsi_14     |  41.9 |
| zscore_20d |  -2.6 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Apple Inc. / AAPL                   |   7.8450 |           2.4% |                 0.43x |       15.6900 |            4.7% |
| Meta Platforms Inc. / META          |  21.3250 |           3.3% |                 0.28x |       42.6500 |            6.6% |
| Brent Crude Oil / BZ=F              |   4.1479 |           4.0% |                 0.27x |        8.2957 |            7.9% |
| Microsoft Corporation / MSFT        |  10.0579 |           2.0% |                 0.47x |       20.1157 |            4.1% |
| JPMorgan Chase & Co. / JPM          |   5.6079 |           1.6% |                 0.71x |       11.2157 |            3.1% |
| Soybeans / ZS=F                     |  21.4643 |           1.7% |                 0.51x |       42.9286 |            3.4% |
| Corn / ZC=F                         |  12.3214 |           2.4% |                 0.25x |       24.6429 |            4.8% |
| S&P 500 / ^GSPC                     |  56.3591 |           0.7% |                 1.14x |      112.7183 |            1.5% |
| NASDAQ 100 / ^NDX                   | 318.6283 |           1.1% |                 0.80x |      637.2567 |            2.2% |
| Amazon.com Inc. / AMZN              |   5.6293 |           2.2% |                 0.39x |       11.2586 |            4.4% |
| Dow Jones Industrial Average / ^DJI | 442.7360 |           0.8% |                 0.92x |      885.4721 |            1.7% |
| Euro Stoxx 50 / ^STOXX50E           |  62.5764 |           1.0% |                 0.99x |      125.1528 |            2.0% |
| Alphabet Inc. Class A / GOOGL       |   7.3185 |           2.2% |                 0.53x |       14.6371 |            4.3% |
| Tesla Inc. / TSLA                   |  14.2721 |           3.9% |                 0.20x |       28.5443 |            7.8% |
| FTSE 100 / ^FTSE                    |  90.4644 |           0.8% |                 1.36x |      180.9287 |            1.7% |
| Wheat / ZW=F                        |  24.5714 |           3.5% |                 0.23x |       49.1429 |            7.0% |
| Platinum / PL=F                     |  35.8000 |           2.0% |                 0.25x |       71.6000 |            4.0% |
| DAX / ^GDAXI                        | 256.9400 |           1.0% |                 0.93x |      513.8800 |            2.0% |
| Gold / GC=F                         |  70.9000 |           1.6% |                 0.40x |      141.8001 |            3.2% |
| NVIDIA Corporation / NVDA           |   7.6672 |           3.5% |                 0.23x |       15.3344 |            7.0% |
| CAC 40 / ^FCHI                      |  85.5322 |           1.0% |                 0.90x |      171.0645 |            2.1% |
| Silver / SI=F                       |   2.0171 |           3.1% |                 0.27x |        4.0341 |            6.2% |
| Hang Seng / ^HSI                    | 319.4679 |           1.3% |                 0.73x |      638.9358 |            2.6% |
| Russell 2000 / ^RUT                 |  29.1400 |           1.0% |                 0.78x |       58.2800 |            2.0% |
| UnitedHealth Group Inc. / UNH       |  10.1814 |           2.7% |                 0.49x |       20.3629 |            5.4% |

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

Scoring engine version: **1.0.0** | Git commit: **671cd3b**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
