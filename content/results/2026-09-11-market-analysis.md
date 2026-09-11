+++
title = "Market Analysis 2026-09-11"
date = "2026-09-11T00:00:00+00:00"
draft = false
summary = "Bearish market: 25 reliable instruments. Top signal: ZS=F (score 80.6)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-09-11.json", "data/history/2026-09-11.json"]
market_regime = "Bearish"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "4831788"
+++

## Market Regime

**Bearish** — 7 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Soybeans / ZS=F** — score 80.6, 20d return +12.1%, RSI14=75. 20d up +12.1%; above MA20 by 4.8%; RSI14=75 ⚠️ Upcoming: FOMC rate decision (2026-09-16)
- **Brent Crude Oil / BZ=F** — score 79.4, 20d return +20.6%, RSI14=79. 20d up +20.6%; above MA20 by 14.7%; RSI14=79 ⚠️ Upcoming: FOMC rate decision (2026-09-16)
- **Apple Inc. / AAPL** — score 72.1, 20d return +8.0%, RSI14=65. 20d up +8.0%; above MA20 by 3.6%; RSI14=65 ⚠️ Upcoming: FOMC rate decision (2026-09-16)
- **Corn / ZC=F** — score 72.1, 20d return +12.0%, RSI14=62. 20d up +12.0%; above MA20 by 2.7%; RSI14=62 ⚠️ Upcoming: FOMC rate decision (2026-09-16)
- **Microsoft Corporation / MSFT** — score 67.0, 20d return +0.2%, RSI14=57. 20d up +0.2%; below MA20 by 0.4%; RSI14=57 ⚠️ Upcoming: FOMC rate decision (2026-09-16)

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                        | Applies To                      |
| ---------- | ---------------------------- | ------------------------------- |
| 2026-09-16 | FOMC rate decision           | Commodity, Equity, Equity Index |
| 2026-09-18 | BOJ monetary policy decision | 6758.T, 7203.T, 8306.T, ^N225   |

## Signal History

Compared with the previous available report (**2026-09-10**).

- **New top-5:** AAPL, MSFT
- **Persistent top signals:** ZC=F (22 reports), ZS=F (15 reports), BZ=F (5 reports)
- **Dropped from top-5:** META, PL=F

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +0 |   +11.2 |
| 7203.T    |     +1 |   +10.0 |
| 8306.T    |     +1 |   +15.8 |
| AAPL      |    +10 |   +21.8 |
| AMZN      |     +3 |    +9.4 |
| BZ=F      |     -1 |    +1.2 |
| CL=F      |     +0 |    +2.1 |
| GC=F      |     -3 |   -12.4 |
| GOOGL     |     +6 |   +18.8 |
| HG=F      |     -5 |   -33.3 |
| JPM       |     +0 |    +3.9 |
| META      |     -4 |   -11.5 |
| MSFT      |     +4 |   +12.7 |
| NG=F      |     +3 |   +13.0 |
| NVDA      |     -7 |   -14.2 |
| PL=F      |    -10 |   -30.6 |
| SI=F      |    -19 |   -34.2 |
| TSLA      |     +0 |    -4.8 |
| UNH       |     -3 |    -5.5 |
| XOM       |     +1 |    +4.5 |
| ZC=F      |     +1 |    +9.4 |
| ZS=F      |     +3 |   +10.6 |
| ZW=F      |     +6 |   +10.3 |
| ^DJI      |     +4 |    +1.2 |
| ^FCHI     |     +0 |    +5.2 |
| ^FTSE     |     +5 |    +0.9 |
| ^GDAXI    |     +0 |    -1.8 |
| ^GSPC     |     +2 |    -0.6 |
| ^HSI      |     +0 |    -9.1 |
| ^N225     |     -1 |    +7.0 |
| ^NDX      |     +1 |    -7.3 |
| ^RUT      |     +0 |    -3.9 |
| ^STOXX50E |     +2 |    +0.3 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **WTI Crude Oil / CL=F** — malformed_input
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Natural Gas / NG=F** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Nikkei 225 / ^N225** — missing_bars
- **Copper / HG=F** — malformed_input
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|    1 | Soybeans / ZS=F        |  80.6 |   Yes    | —               | 20d up +12.1%; above MA20 by 4.8%; RSI14=75  |
|    2 | Brent Crude Oil / BZ=F |  79.4 |   Yes    | —               | 20d up +20.6%; above MA20 by 14.7%; RSI14=79 |
|    4 | Corn / ZC=F            |  72.1 |   Yes    | —               | 20d up +12.0%; above MA20 by 2.7%; RSI14=62  |
|    8 | Wheat / ZW=F           |  58.8 |   Yes    | —               | 20d up +7.2%; above MA20 by 1.2%; RSI14=58   |
|   13 | Platinum / PL=F        |  45.1 |   Yes    | —               | 20d up +1.8%; below MA20 by 1.6%; RSI14=39   |
|   18 | Gold / GC=F            |  35.8 |   Yes    | —               | 20d down -1.9%; below MA20 by 2.8%; RSI14=28 |
|   25 | Silver / SI=F          |  25.1 |   Yes    | —               | 20d down -2.4%; below MA20 by 3.9%; RSI14=36 |
|   26 | WTI Crude Oil / CL=F   |  80.6 |    No    | malformed_input | Suppressed: malformed_input                  |
|   29 | Natural Gas / NG=F     |  44.5 |    No    | malformed_input | Suppressed: malformed_input                  |
|   32 | Copper / HG=F          |  39.7 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    3 | Apple Inc. / AAPL                                                              |  72.1 |   Yes    | —                             | 20d up +8.0%; above MA20 by 3.6%; RSI14=65   |
|    5 | Microsoft Corporation / MSFT                                                   |  67.0 |   Yes    | —                             | 20d up +0.2%; below MA20 by 0.4%; RSI14=57   |
|    6 | Meta Platforms Inc. / META                                                     |  64.2 |   Yes    | —                             | 20d up +11.3%; above MA20 by 10.4%; RSI14=84 |
|    7 | JPMorgan Chase & Co. / JPM                                                     |  61.2 |   Yes    | —                             | 20d down -3.2%; below MA20 by 1.0%; RSI14=53 |
|   10 | Tesla Inc. / TSLA                                                              |  49.1 |   Yes    | —                             | 20d up +11.0%; above MA20 by 2.7%; RSI14=56  |
|   15 | NVIDIA Corporation / NVDA                                                      |  40.6 |   Yes    | —                             | 20d down -2.4%; below MA20 by 0.9%; RSI14=51 |
|   19 | Alphabet Inc. Class A / GOOGL                                                  |  33.6 |   Yes    | —                             | 20d down -3.1%; below MA20 by 2.5%; RSI14=43 |
|   21 | Amazon.com Inc. / AMZN                                                         |  32.7 |   Yes    | —                             | 20d down -5.8%; below MA20 by 2.9%; RSI14=41 |
|   24 | UnitedHealth Group Inc. / UNH                                                  |  27.9 |   Yes    | —                             | 20d down -4.3%; below MA20 by 1.7%; RSI14=53 |
|   27 | Exxon Mobil Corporation / XOM                                                  |  72.4 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   28 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  63.9 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   30 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  43.3 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   33 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  36.4 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    9 | S&P 500 / ^GSPC                     |  53.0 |   Yes    | —            | 20d down -2.0%; below MA20 by 1.3%; RSI14=45 |
|   11 | NASDAQ 100 / ^NDX                   |  46.1 |   Yes    | —            | 20d down -2.1%; below MA20 by 1.1%; RSI14=48 |
|   12 | FTSE 100 / ^FTSE                    |  45.5 |   Yes    | —            | 20d down -2.1%; below MA20 by 1.6%; RSI14=39 |
|   14 | Dow Jones Industrial Average / ^DJI |  40.9 |   Yes    | —            | 20d down -3.2%; below MA20 by 2.2%; RSI14=42 |
|   16 | Hang Seng / ^HSI                    |  39.1 |   Yes    | —            | 20d down -1.7%; below MA20 by 2.0%; RSI14=27 |
|   17 | Euro Stoxx 50 / ^STOXX50E           |  36.1 |   Yes    | —            | 20d down -4.2%; below MA20 by 2.4%; RSI14=29 |
|   20 | DAX / ^GDAXI                        |  33.6 |   Yes    | —            | 20d down -3.6%; below MA20 by 2.8%; RSI14=32 |
|   22 | Russell 2000 / ^RUT                 |  29.4 |   Yes    | —            | 20d down -5.1%; below MA20 by 3.3%; RSI14=34 |
|   23 | CAC 40 / ^FCHI                      |  29.1 |   Yes    | —            | 20d down -6.2%; below MA20 by 3.2%; RSI14=22 |
|   31 | Nikkei 225 / ^N225                  |  40.9 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-09-10 |
| 7203.T    | 2026-09-10 |
| 8306.T    | 2026-09-10 |
| AAPL      | 2026-09-10 |
| AMZN      | 2026-09-10 |
| BZ=F      | 2026-09-10 |
| CL=F      | 2026-09-10 |
| GC=F      | 2026-09-10 |
| GOOGL     | 2026-09-10 |
| HG=F      | 2026-09-10 |
| JPM       | 2026-09-10 |
| META      | 2026-09-10 |
| MSFT      | 2026-09-10 |
| NG=F      | 2026-09-10 |
| NVDA      | 2026-09-10 |
| PL=F      | 2026-09-10 |
| SI=F      | 2026-09-10 |
| TSLA      | 2026-09-10 |
| UNH       | 2026-09-10 |
| XOM       | 2026-09-10 |
| ZC=F      | 2026-09-10 |
| ZS=F      | 2026-09-10 |
| ZW=F      | 2026-09-10 |
| ^DJI      | 2026-09-10 |
| ^FCHI     | 2026-09-10 |
| ^FTSE     | 2026-09-10 |
| ^GDAXI    | 2026-09-10 |
| ^GSPC     | 2026-09-10 |
| ^HSI      | 2026-09-10 |
| ^N225     | 2026-09-10 |
| ^NDX      | 2026-09-10 |
| ^RUT      | 2026-09-10 |
| ^STOXX50E | 2026-09-10 |

## Symbol Details

### Soybeans / ZS=F (score 80.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.6% |
| ret_5d     |  +1.1% |
| ret_20d    | +12.1% |
| ret_60d    | +17.2% |
| ma20_dist  |  +4.8% |
| ma50_dist  |  +8.2% |
| vol_20d    |  16.4% |
| mdd_60d    |   8.1% |
| rsi_14     |   75.3 |
| zscore_20d |    1.5 |

### Brent Crude Oil / BZ=F (score 79.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +6.3% |
| ret_5d     | +12.7% |
| ret_20d    | +20.6% |
| ret_60d    | +38.2% |
| ma20_dist  | +14.7% |
| ma50_dist  | +20.4% |
| vol_20d    |  34.5% |
| mdd_60d    |  21.2% |
| rsi_14     |   79.3 |
| zscore_20d |    3.0 |

### Apple Inc. / AAPL (score 72.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +3.6% |
| ret_5d     |  +0.5% |
| ret_20d    |  +8.0% |
| ret_60d    | +10.2% |
| ma20_dist  |  +3.6% |
| ma50_dist  |  +3.0% |
| vol_20d    |  22.9% |
| mdd_60d    |  11.0% |
| rsi_14     |   64.7 |
| zscore_20d |    1.6 |

### Corn / ZC=F (score 72.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.2% |
| ret_5d     |  -0.9% |
| ret_20d    | +12.0% |
| ret_60d    | +23.1% |
| ma20_dist  |  +2.7% |
| ma50_dist  |  +9.8% |
| vol_20d    |  44.1% |
| mdd_60d    |   6.0% |
| rsi_14     |   62.2 |
| zscore_20d |    0.7 |

### Microsoft Corporation / MSFT (score 67.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.2% |
| ret_5d     |  -0.9% |
| ret_20d    |  +0.2% |
| ret_60d    | +23.2% |
| ma20_dist  |  -0.4% |
| ma50_dist  |  +9.2% |
| vol_20d    |  21.2% |
| mdd_60d    |  10.4% |
| rsi_14     |   56.9 |
| zscore_20d |   -0.2 |

### Meta Platforms Inc. / META (score 64.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.4% |
| ret_5d     |  +8.7% |
| ret_20d    | +11.3% |
| ret_60d    |  +8.6% |
| ma20_dist  | +10.4% |
| ma50_dist  |  +7.4% |
| vol_20d    |  37.0% |
| mdd_60d    |  20.9% |
| rsi_14     |   83.9 |
| zscore_20d |    2.0 |

### JPMorgan Chase & Co. / JPM (score 61.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.3% |
| ret_5d     |  -0.7% |
| ret_20d    |  -3.2% |
| ret_60d    | +11.2% |
| ma20_dist  |  -1.0% |
| ma50_dist  |  +0.7% |
| vol_20d    |  13.9% |
| mdd_60d    |   3.7% |
| rsi_14     |   53.2 |
| zscore_20d |   -1.0 |

### Wheat / ZW=F (score 58.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.7% |
| ret_5d     |  -4.2% |
| ret_20d    |  +7.2% |
| ret_60d    | +19.4% |
| ma20_dist  |  +1.2% |
| ma50_dist  |  +6.8% |
| vol_20d    |  42.8% |
| mdd_60d    |  10.7% |
| rsi_14     |   58.1 |
| zscore_20d |    0.3 |

### S&P 500 / ^GSPC (score 53.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | -1.0% |
| ret_20d    | -2.0% |
| ret_60d    | +0.5% |
| ma20_dist  | -1.3% |
| ma50_dist  | -0.2% |
| vol_20d    |  8.5% |
| mdd_60d    |  3.4% |
| rsi_14     |  45.1 |
| zscore_20d |  -2.0 |

### Tesla Inc. / TSLA (score 49.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.2% |
| ret_5d     |  +1.8% |
| ret_20d    | +11.0% |
| ret_60d    | -11.6% |
| ma20_dist  |  +2.7% |
| ma50_dist  |  +2.2% |
| vol_20d    |  50.9% |
| mdd_60d    |  29.9% |
| rsi_14     |   56.4 |
| zscore_20d |    0.9 |

### NASDAQ 100 / ^NDX (score 46.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.1% |
| ret_5d     | -0.1% |
| ret_20d    | -2.1% |
| ret_60d    | -4.7% |
| ma20_dist  | -1.1% |
| ma50_dist  | -0.4% |
| vol_20d    | 12.8% |
| mdd_60d    | 10.6% |
| rsi_14     |  47.8 |
| zscore_20d |  -1.1 |

### FTSE 100 / ^FTSE (score 45.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | -2.1% |
| ret_20d    | -2.1% |
| ret_60d    | +1.0% |
| ma20_dist  | -1.6% |
| ma50_dist  | -1.2% |
| vol_20d    |  7.4% |
| mdd_60d    |  2.7% |
| rsi_14     |  38.9 |
| zscore_20d |  -2.6 |

### Platinum / PL=F (score 45.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -6.1% |
| ret_5d     | -1.7% |
| ret_20d    | +1.8% |
| ret_60d    | +7.6% |
| ma20_dist  | -1.6% |
| ma50_dist  | +3.9% |
| vol_20d    | 39.7% |
| mdd_60d    |  7.1% |
| rsi_14     |  39.1 |
| zscore_20d |  -0.6 |

### Dow Jones Industrial Average / ^DJI (score 40.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | -1.9% |
| ret_20d    | -3.2% |
| ret_60d    | +0.8% |
| ma20_dist  | -2.2% |
| ma50_dist  | -1.7% |
| vol_20d    | 10.2% |
| mdd_60d    |  4.2% |
| rsi_14     |  42.1 |
| zscore_20d |  -2.6 |

### NVIDIA Corporation / NVDA (score 40.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.3% |
| ret_5d     | -2.6% |
| ret_20d    | -2.4% |
| ret_60d    | +2.8% |
| ma20_dist  | -0.9% |
| ma50_dist  | +3.0% |
| vol_20d    | 43.4% |
| mdd_60d    | 10.6% |
| rsi_14     |  51.1 |
| zscore_20d |  -0.3 |

### Hang Seng / ^HSI (score 39.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.3% |
| ret_5d     | -1.0% |
| ret_20d    | -1.7% |
| ret_60d    | +1.9% |
| ma20_dist  | -2.0% |
| ma50_dist  | -0.9% |
| vol_20d    | 14.0% |
| mdd_60d    |  6.7% |
| rsi_14     |  26.6 |
| zscore_20d |  -2.2 |

### Euro Stoxx 50 / ^STOXX50E (score 36.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | -1.8% |
| ret_20d    | -4.2% |
| ret_60d    | -0.9% |
| ma20_dist  | -2.4% |
| ma50_dist  | -1.8% |
| vol_20d    |  9.4% |
| mdd_60d    |  4.3% |
| rsi_14     |  29.1 |
| zscore_20d |  -2.4 |

### Gold / GC=F (score 35.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.2% |
| ret_5d     | -2.8% |
| ret_20d    | -1.9% |
| ret_60d    | +4.4% |
| ma20_dist  | -2.8% |
| ma50_dist  | +1.7% |
| vol_20d    | 25.3% |
| mdd_60d    |  7.6% |
| rsi_14     |  28.4 |
| zscore_20d |  -1.2 |

### Alphabet Inc. Class A / GOOGL (score 33.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | -1.3% |
| ret_20d    | -3.1% |
| ret_60d    | -9.9% |
| ma20_dist  | -2.5% |
| ma50_dist  | -4.3% |
| vol_20d    | 17.9% |
| mdd_60d    | 14.9% |
| rsi_14     |  42.6 |
| zscore_20d |  -1.8 |

### DAX / ^GDAXI (score 33.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | -2.5% |
| ret_20d    | -3.6% |
| ret_60d    | +1.3% |
| ma20_dist  | -2.8% |
| ma50_dist  | -1.5% |
| vol_20d    | 10.5% |
| mdd_60d    |  4.5% |
| rsi_14     |  31.7 |
| zscore_20d |  -2.7 |

### Amazon.com Inc. / AMZN (score 32.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | -1.2% |
| ret_20d    | -5.8% |
| ret_60d    | +2.4% |
| ma20_dist  | -2.9% |
| ma50_dist  | -1.2% |
| vol_20d    | 24.5% |
| mdd_60d    | 11.3% |
| rsi_14     |  40.5 |
| zscore_20d |  -1.9 |

### Russell 2000 / ^RUT (score 29.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | -2.1% |
| ret_20d    | -5.1% |
| ret_60d    | -2.5% |
| ma20_dist  | -3.3% |
| ma50_dist  | -3.1% |
| vol_20d    | 12.7% |
| mdd_60d    |  5.8% |
| rsi_14     |  33.6 |
| zscore_20d |  -2.1 |

### CAC 40 / ^FCHI (score 29.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | -2.0% |
| ret_20d    | -6.2% |
| ret_60d    | -4.1% |
| ma20_dist  | -3.2% |
| ma50_dist  | -3.8% |
| vol_20d    | 10.4% |
| mdd_60d    |  7.0% |
| rsi_14     |  22.4 |
| zscore_20d |  -2.0 |

### UnitedHealth Group Inc. / UNH (score 27.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.2% |
| ret_5d     | -2.8% |
| ret_20d    | -4.3% |
| ret_60d    | -5.5% |
| ma20_dist  | -1.7% |
| ma50_dist  | -5.3% |
| vol_20d    | 19.4% |
| mdd_60d    | 11.8% |
| rsi_14     |  52.7 |
| zscore_20d |  -1.4 |

### Silver / SI=F (score 25.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -5.4% |
| ret_5d     | -4.0% |
| ret_20d    | -2.4% |
| ret_60d    | -1.9% |
| ma20_dist  | -3.9% |
| ma50_dist  | +2.3% |
| vol_20d    | 37.6% |
| mdd_60d    |  9.9% |
| rsi_14     |  35.8 |
| zscore_20d |  -1.6 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Soybeans / ZS=F                     |  19.9464 |           1.5% |                 0.61x |       39.8929 |            3.0% |
| Brent Crude Oil / BZ=F              |   3.8129 |           3.5% |                 0.29x |        7.6257 |            7.1% |
| Apple Inc. / AAPL                   |   7.5200 |           2.3% |                 0.44x |       15.0400 |            4.6% |
| Corn / ZC=F                         |  14.5893 |           2.8% |                 0.23x |       29.1786 |            5.7% |
| Microsoft Corporation / MSFT        |  10.1507 |           2.1% |                 0.47x |       20.3014 |            4.1% |
| Meta Platforms Inc. / META          |  20.6664 |           3.2% |                 0.27x |       41.3329 |            6.4% |
| JPMorgan Chase & Co. / JPM          |   5.6079 |           1.6% |                 0.72x |       11.2157 |            3.2% |
| Wheat / ZW=F                        |  25.6607 |           3.5% |                 0.23x |       51.3214 |            7.1% |
| S&P 500 / ^GSPC                     |  54.2613 |           0.7% |                 1.17x |      108.5225 |            1.4% |
| Tesla Inc. / TSLA                   |  15.2943 |           4.2% |                 0.20x |       30.5886 |            8.4% |
| NASDAQ 100 / ^NDX                   | 310.9905 |           1.1% |                 0.78x |      621.9810 |            2.1% |
| FTSE 100 / ^FTSE                    |  89.3285 |           0.8% |                 1.36x |      178.6571 |            1.7% |
| Platinum / PL=F                     |  36.5357 |           2.0% |                 0.25x |       73.0714 |            4.1% |
| Dow Jones Industrial Average / ^DJI | 438.4914 |           0.8% |                 0.98x |      876.9827 |            1.7% |
| NVIDIA Corporation / NVDA           |   7.6947 |           3.5% |                 0.23x |       15.3895 |            7.0% |
| Hang Seng / ^HSI                    | 333.3458 |           1.3% |                 0.71x |      666.6917 |            2.7% |
| Euro Stoxx 50 / ^STOXX50E           |  59.5228 |           0.9% |                 1.06x |      119.0456 |            1.9% |
| Gold / GC=F                         |  74.2143 |           1.7% |                 0.39x |      148.4286 |            3.4% |
| Alphabet Inc. Class A / GOOGL       |   6.9911 |           2.1% |                 0.56x |       13.9822 |            4.2% |
| DAX / ^GDAXI                        | 250.7656 |           1.0% |                 0.95x |      501.5312 |            2.0% |
| Amazon.com Inc. / AMZN              |   5.5114 |           2.2% |                 0.41x |       11.0229 |            4.4% |
| Russell 2000 / ^RUT                 |  28.5736 |           1.0% |                 0.78x |       57.1471 |            2.0% |
| CAC 40 / ^FCHI                      |  82.2815 |           1.0% |                 0.96x |      164.5631 |            2.0% |
| UnitedHealth Group Inc. / UNH       |   9.6800 |           2.5% |                 0.51x |       19.3600 |            5.0% |
| Silver / SI=F                       |   1.9710 |           3.1% |                 0.27x |        3.9420 |            6.1% |

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

Scoring engine version: **1.0.0** | Git commit: **4831788**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
