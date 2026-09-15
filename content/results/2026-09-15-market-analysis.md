+++
title = "Market Analysis 2026-09-15"
date = "2026-09-15T00:00:00+00:00"
draft = false
summary = "Bearish market: 25 reliable instruments. Top signal: MSFT (score 76.4)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-09-15.json", "data/history/2026-09-15.json"]
market_regime = "Bearish"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "93f3cd2"
+++

## Market Regime

**Bearish** — 8 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Microsoft Corporation / MSFT** — score 76.4, 20d return +2.2%, RSI14=60. 20d up +2.2%; above MA20 by 2.1%; RSI14=60 ⚠️ Upcoming: FOMC rate decision (2026-09-16)
- **Meta Platforms Inc. / META** — score 76.1, 20d return +12.8%, RSI14=85. 20d up +12.8%; above MA20 by 12.8%; RSI14=85 ⚠️ Upcoming: FOMC rate decision (2026-09-16)
- **Brent Crude Oil / BZ=F** — score 74.5, 20d return +16.1%, RSI14=83. 20d up +16.1%; above MA20 by 10.9%; RSI14=83 ⚠️ Upcoming: FOMC rate decision (2026-09-16)
- **Apple Inc. / AAPL** — score 72.7, 20d return +8.9%, RSI14=71. 20d up +8.9%; above MA20 by 4.7%; RSI14=71 ⚠️ Upcoming: FOMC rate decision (2026-09-16)
- **Soybeans / ZS=F** — score 71.8, 20d return +7.0%, RSI14=68. 20d up +7.0%; above MA20 by 1.6%; RSI14=68 ⚠️ Upcoming: FOMC rate decision (2026-09-16)

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                        | Applies To                      |
| ---------- | ---------------------------- | ------------------------------- |
| 2026-09-16 | FOMC rate decision           | Commodity, Equity, Equity Index |
| 2026-09-18 | BOJ monetary policy decision | 6758.T, 7203.T, 8306.T, ^N225   |

## Signal History

Compared with the previous available report (**2026-09-14**).

- **New top-5:** ZS=F
- **Persistent top signals:** BZ=F (7 reports), AAPL (3 reports), MSFT (3 reports), META (2 reports)
- **Dropped from top-5:** JPM

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +3 |   +37.6 |
| 7203.T    |     -2 |    -4.5 |
| 8306.T    |     +0 |   +11.2 |
| AAPL      |     -3 |    -3.9 |
| AMZN      |     -9 |   -16.1 |
| BZ=F      |     +0 |    +6.4 |
| CL=F      |     +1 |    +6.7 |
| GC=F      |     +1 |    -5.5 |
| GOOGL     |     +6 |   +13.0 |
| HG=F      |     -2 |   -20.9 |
| JPM       |    -11 |   -25.1 |
| META      |     +0 |    +5.8 |
| MSFT      |     +3 |    +9.1 |
| NG=F      |     +1 |   +14.2 |
| NVDA      |     -5 |   -20.0 |
| PL=F      |     +2 |    -4.2 |
| SI=F      |     -2 |    -5.8 |
| TSLA      |     +0 |    -3.9 |
| UNH       |     +4 |   +16.1 |
| XOM       |     -1 |    -5.2 |
| ZC=F      |     +1 |    +6.7 |
| ZS=F      |     +1 |    +8.2 |
| ZW=F      |     +7 |   +10.6 |
| ^DJI      |     +0 |    -2.4 |
| ^FCHI     |     -2 |    -6.7 |
| ^FTSE     |     +7 |   +11.8 |
| ^GDAXI    |     +1 |    -6.4 |
| ^GSPC     |     -2 |    -7.9 |
| ^HSI      |    +10 |   +12.1 |
| ^N225     |     +0 |    -5.2 |
| ^NDX      |     -3 |   -12.1 |
| ^RUT      |     +2 |    +0.0 |
| ^STOXX50E |     -8 |   -13.6 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **WTI Crude Oil / CL=F** — malformed_input
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Natural Gas / NG=F** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|    3 | Brent Crude Oil / BZ=F |  74.5 |   Yes    | —               | 20d up +16.1%; above MA20 by 10.9%; RSI14=83 |
|    5 | Soybeans / ZS=F        |  71.8 |   Yes    | —               | 20d up +7.0%; above MA20 by 1.6%; RSI14=68   |
|    6 | Corn / ZC=F            |  69.4 |   Yes    | —               | 20d up +10.1%; above MA20 by 1.5%; RSI14=66  |
|    9 | Wheat / ZW=F           |  56.1 |   Yes    | —               | 20d up +4.8%; below MA20 by 1.4%; RSI14=56   |
|   15 | Platinum / PL=F        |  40.9 |   Yes    | —               | 20d up +2.9%; below MA20 by 2.9%; RSI14=41   |
|   18 | Gold / GC=F            |  36.4 |   Yes    | —               | 20d down -0.3%; below MA20 by 3.1%; RSI14=33 |
|   24 | Silver / SI=F          |  27.3 |   Yes    | —               | 20d down -0.7%; below MA20 by 4.9%; RSI14=36 |
|   26 | WTI Crude Oil / CL=F   |  78.2 |    No    | malformed_input | Suppressed: malformed_input                  |
|   30 | Natural Gas / NG=F     |  50.6 |    No    | malformed_input | Suppressed: malformed_input                  |
|   32 | Copper / HG=F          |  23.0 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    1 | Microsoft Corporation / MSFT                                                   |  76.4 |   Yes    | —                             | 20d up +2.2%; above MA20 by 2.1%; RSI14=60   |
|    2 | Meta Platforms Inc. / META                                                     |  76.1 |   Yes    | —                             | 20d up +12.8%; above MA20 by 12.8%; RSI14=85 |
|    4 | Apple Inc. / AAPL                                                              |  72.7 |   Yes    | —                             | 20d up +8.9%; above MA20 by 4.7%; RSI14=71   |
|    7 | Alphabet Inc. Class A / GOOGL                                                  |  59.7 |   Yes    | —                             | 20d up +1.1%; above MA20 by 2.4%; RSI14=51   |
|   14 | Tesla Inc. / TSLA                                                              |  42.7 |   Yes    | —                             | 20d up +4.9%; above MA20 by 0.8%; RSI14=54   |
|   16 | JPMorgan Chase & Co. / JPM                                                     |  39.7 |   Yes    | —                             | 20d down -3.5%; below MA20 by 1.7%; RSI14=41 |
|   19 | Amazon.com Inc. / AMZN                                                         |  33.9 |   Yes    | —                             | 20d down -3.5%; below MA20 by 1.9%; RSI14=41 |
|   21 | UnitedHealth Group Inc. / UNH                                                  |  31.8 |   Yes    | —                             | 20d down -3.9%; below MA20 by 1.9%; RSI14=40 |
|   25 | NVIDIA Corporation / NVDA                                                      |  20.3 |   Yes    | —                             | 20d down -6.2%; below MA20 by 3.8%; RSI14=52 |
|   27 | Exxon Mobil Corporation / XOM                                                  |  69.4 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   28 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  68.5 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   29 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  60.9 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   31 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  46.4 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    8 | FTSE 100 / ^FTSE                    |  58.5 |   Yes    | —            | 20d down -0.5%; below MA20 by 0.7%; RSI14=37 |
|   10 | S&P 500 / ^GSPC                     |  53.6 |   Yes    | —            | 20d down -2.1%; below MA20 by 0.7%; RSI14=47 |
|   11 | Dow Jones Industrial Average / ^DJI |  46.7 |   Yes    | —            | 20d down -2.4%; below MA20 by 1.3%; RSI14=39 |
|   12 | NASDAQ 100 / ^NDX                   |  44.5 |   Yes    | —            | 20d down -3.1%; below MA20 by 0.8%; RSI14=52 |
|   13 | Hang Seng / ^HSI                    |  43.9 |   Yes    | —            | 20d down -2.1%; below MA20 by 1.9%; RSI14=35 |
|   17 | DAX / ^GDAXI                        |  36.7 |   Yes    | —            | 20d down -3.4%; below MA20 by 2.2%; RSI14=32 |
|   20 | Euro Stoxx 50 / ^STOXX50E           |  33.3 |   Yes    | —            | 20d down -4.1%; below MA20 by 2.2%; RSI14=33 |
|   22 | Russell 2000 / ^RUT                 |  30.9 |   Yes    | —            | 20d down -5.7%; below MA20 by 2.7%; RSI14=32 |
|   23 | CAC 40 / ^FCHI                      |  28.8 |   Yes    | —            | 20d down -5.4%; below MA20 by 2.6%; RSI14=28 |
|   33 | Nikkei 225 / ^N225                  |  16.4 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-09-14 |
| 7203.T    | 2026-09-14 |
| 8306.T    | 2026-09-14 |
| AAPL      | 2026-09-14 |
| AMZN      | 2026-09-14 |
| BZ=F      | 2026-09-14 |
| CL=F      | 2026-09-14 |
| GC=F      | 2026-09-14 |
| GOOGL     | 2026-09-14 |
| HG=F      | 2026-09-14 |
| JPM       | 2026-09-14 |
| META      | 2026-09-14 |
| MSFT      | 2026-09-14 |
| NG=F      | 2026-09-14 |
| NVDA      | 2026-09-14 |
| PL=F      | 2026-09-14 |
| SI=F      | 2026-09-14 |
| TSLA      | 2026-09-14 |
| UNH       | 2026-09-14 |
| XOM       | 2026-09-14 |
| ZC=F      | 2026-09-14 |
| ZS=F      | 2026-09-14 |
| ZW=F      | 2026-09-14 |
| ^DJI      | 2026-09-14 |
| ^FCHI     | 2026-09-14 |
| ^FTSE     | 2026-09-14 |
| ^GDAXI    | 2026-09-14 |
| ^GSPC     | 2026-09-14 |
| ^HSI      | 2026-09-14 |
| ^N225     | 2026-09-14 |
| ^NDX      | 2026-09-14 |
| ^RUT      | 2026-09-14 |
| ^STOXX50E | 2026-09-14 |

## Symbol Details

### Microsoft Corporation / MSFT (score 76.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.0% |
| ret_5d     |  +1.1% |
| ret_20d    |  +2.2% |
| ret_60d    | +33.4% |
| ma20_dist  |  +2.1% |
| ma50_dist  | +10.9% |
| vol_20d    |  22.2% |
| mdd_60d    |   7.0% |
| rsi_14     |   60.2 |
| zscore_20d |    1.1 |

### Meta Platforms Inc. / META (score 76.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.7% |
| ret_5d     |  +7.9% |
| ret_20d    | +12.8% |
| ret_60d    | +17.3% |
| ma20_dist  | +12.8% |
| ma50_dist  | +10.5% |
| vol_20d    |  36.6% |
| mdd_60d    |  20.9% |
| rsi_14     |   84.8 |
| zscore_20d |    2.0 |

### Brent Crude Oil / BZ=F (score 74.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.0% |
| ret_5d     |  +9.8% |
| ret_20d    | +16.1% |
| ret_60d    | +43.3% |
| ma20_dist  | +10.9% |
| ma50_dist  | +16.7% |
| vol_20d    |  36.6% |
| mdd_60d    |  21.2% |
| rsi_14     |   83.4 |
| zscore_20d |    1.9 |

### Apple Inc. / AAPL (score 72.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.2% |
| ret_5d     |  +4.1% |
| ret_20d    |  +8.9% |
| ret_60d    | +12.5% |
| ma20_dist  |  +4.7% |
| ma50_dist  |  +4.6% |
| vol_20d    |  23.3% |
| mdd_60d    |  11.0% |
| rsi_14     |   70.5 |
| zscore_20d |    1.9 |

### Soybeans / ZS=F (score 71.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.4% |
| ret_5d     |  -0.7% |
| ret_20d    |  +7.0% |
| ret_60d    | +15.1% |
| ma20_dist  |  +1.6% |
| ma50_dist  |  +5.4% |
| vol_20d    |  19.4% |
| mdd_60d    |   8.1% |
| rsi_14     |   68.0 |
| zscore_20d |    0.6 |

### Corn / ZC=F (score 69.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.3% |
| ret_5d     |  +0.0% |
| ret_20d    | +10.1% |
| ret_60d    | +25.0% |
| ma20_dist  |  +1.5% |
| ma50_dist  |  +8.7% |
| vol_20d    |  37.1% |
| mdd_60d    |   6.0% |
| rsi_14     |   66.3 |
| zscore_20d |    0.5 |

### Alphabet Inc. Class A / GOOGL (score 59.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +3.2% |
| ret_5d     | +3.2% |
| ret_20d    | +1.1% |
| ret_60d    | -4.0% |
| ma20_dist  | +2.4% |
| ma50_dist  | +0.7% |
| vol_20d    | 22.0% |
| mdd_60d    | 14.4% |
| rsi_14     |  51.2 |
| zscore_20d |   1.7 |

### FTSE 100 / ^FTSE (score 58.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | -1.2% |
| ret_20d    | -0.5% |
| ret_60d    | +3.2% |
| ma20_dist  | -0.7% |
| ma50_dist  | -0.4% |
| vol_20d    |  7.5% |
| mdd_60d    |  2.7% |
| rsi_14     |  37.2 |
| zscore_20d |  -1.0 |

### Wheat / ZW=F (score 56.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.0% |
| ret_5d     |  -1.3% |
| ret_20d    |  +4.8% |
| ret_60d    | +20.5% |
| ma20_dist  |  -1.4% |
| ma50_dist  |  +3.8% |
| vol_20d    |  42.0% |
| mdd_60d    |  10.7% |
| rsi_14     |   55.9 |
| zscore_20d |   -0.3 |

### S&P 500 / ^GSPC (score 53.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | -1.3% |
| ret_20d    | -2.1% |
| ret_60d    | +2.7% |
| ma20_dist  | -0.7% |
| ma50_dist  | +0.1% |
| vol_20d    |  8.9% |
| mdd_60d    |  3.4% |
| rsi_14     |  47.0 |
| zscore_20d |  -1.4 |

### Dow Jones Industrial Average / ^DJI (score 46.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | -1.9% |
| ret_20d    | -2.4% |
| ret_60d    | +1.8% |
| ma20_dist  | -1.3% |
| ma50_dist  | -1.0% |
| vol_20d    | 10.9% |
| mdd_60d    |  4.2% |
| rsi_14     |  38.6 |
| zscore_20d |  -1.5 |

### NASDAQ 100 / ^NDX (score 44.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | -1.4% |
| ret_20d    | -3.1% |
| ret_60d    | -1.8% |
| ma20_dist  | -0.8% |
| ma50_dist  | -0.2% |
| vol_20d    | 12.7% |
| mdd_60d    | 10.6% |
| rsi_14     |  52.0 |
| zscore_20d |  -1.0 |

### Hang Seng / ^HSI (score 43.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | -1.9% |
| ret_20d    | -2.1% |
| ret_60d    | +4.1% |
| ma20_dist  | -1.9% |
| ma50_dist  | -1.3% |
| vol_20d    | 12.9% |
| mdd_60d    |  4.6% |
| rsi_14     |  35.3 |
| zscore_20d |  -1.8 |

### Tesla Inc. / TSLA (score 42.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.8% |
| ret_5d     | +1.4% |
| ret_20d    | +4.9% |
| ret_60d    | -9.4% |
| ma20_dist  | +0.8% |
| ma50_dist  | +1.5% |
| vol_20d    | 50.0% |
| mdd_60d    | 29.9% |
| rsi_14     |  54.1 |
| zscore_20d |   0.3 |

### Platinum / PL=F (score 40.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.0% |
| ret_5d     |  -2.7% |
| ret_20d    |  +2.9% |
| ret_60d    | +12.4% |
| ma20_dist  |  -2.9% |
| ma50_dist  |  +2.3% |
| vol_20d    |  38.2% |
| mdd_60d    |   7.2% |
| rsi_14     |   41.0 |
| zscore_20d |   -1.3 |

### JPMorgan Chase & Co. / JPM (score 39.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.7% |
| ret_5d     | -2.4% |
| ret_20d    | -3.5% |
| ret_60d    | +5.5% |
| ma20_dist  | -1.7% |
| ma50_dist  | -0.5% |
| vol_20d    | 15.2% |
| mdd_60d    |  4.1% |
| rsi_14     |  41.2 |
| zscore_20d |  -1.8 |

### DAX / ^GDAXI (score 36.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | -2.2% |
| ret_20d    | -3.4% |
| ret_60d    | +1.2% |
| ma20_dist  | -2.2% |
| ma50_dist  | -1.2% |
| vol_20d    | 10.8% |
| mdd_60d    |  4.5% |
| rsi_14     |  31.8 |
| zscore_20d |  -1.8 |

### Gold / GC=F (score 36.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.3% |
| ret_5d     | -2.8% |
| ret_20d    | -0.3% |
| ret_60d    | +9.1% |
| ma20_dist  | -3.1% |
| ma50_dist  | +1.2% |
| vol_20d    | 25.6% |
| mdd_60d    |  7.6% |
| rsi_14     |  32.6 |
| zscore_20d |  -1.3 |

### Amazon.com Inc. / AMZN (score 33.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.3% |
| ret_5d     | -1.9% |
| ret_20d    | -3.5% |
| ret_60d    | +6.8% |
| ma20_dist  | -1.9% |
| ma50_dist  | -0.8% |
| vol_20d    | 25.7% |
| mdd_60d    | 11.3% |
| rsi_14     |  40.8 |
| zscore_20d |  -1.3 |

### Euro Stoxx 50 / ^STOXX50E (score 33.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | -2.2% |
| ret_20d    | -4.1% |
| ret_60d    | -0.8% |
| ma20_dist  | -2.2% |
| ma50_dist  | -1.8% |
| vol_20d    | 10.6% |
| mdd_60d    |  4.4% |
| rsi_14     |  32.6 |
| zscore_20d |  -2.2 |

### UnitedHealth Group Inc. / UNH (score 31.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.8% |
| ret_5d     | -2.8% |
| ret_20d    | -3.9% |
| ret_60d    | -4.0% |
| ma20_dist  | -1.9% |
| ma50_dist  | -5.8% |
| vol_20d    | 21.3% |
| mdd_60d    | 13.7% |
| rsi_14     |  40.2 |
| zscore_20d |  -1.3 |

### Russell 2000 / ^RUT (score 30.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -2.8% |
| ret_20d    | -5.7% |
| ret_60d    | -0.9% |
| ma20_dist  | -2.7% |
| ma50_dist  | -2.9% |
| vol_20d    | 12.6% |
| mdd_60d    |  5.8% |
| rsi_14     |  32.1 |
| zscore_20d |  -1.7 |

### CAC 40 / ^FCHI (score 28.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | -2.3% |
| ret_20d    | -5.4% |
| ret_60d    | -3.4% |
| ma20_dist  | -2.6% |
| ma50_dist  | -3.7% |
| vol_20d    | 11.1% |
| mdd_60d    |  7.0% |
| rsi_14     |  28.5 |
| zscore_20d |  -1.8 |

### Silver / SI=F (score 27.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.6% |
| ret_5d     | -4.8% |
| ret_20d    | -0.7% |
| ret_60d    | +9.4% |
| ma20_dist  | -4.9% |
| ma50_dist  | +0.7% |
| vol_20d    | 36.2% |
| mdd_60d    |  9.7% |
| rsi_14     |  35.7 |
| zscore_20d |  -1.8 |

### NVIDIA Corporation / NVDA (score 20.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -3.4% |
| ret_5d     | -8.3% |
| ret_20d    | -6.2% |
| ret_60d    | +3.1% |
| ma20_dist  | -3.8% |
| ma50_dist  | -0.9% |
| vol_20d    | 44.8% |
| mdd_60d    | 10.6% |
| rsi_14     |  51.8 |
| zscore_20d |  -1.4 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Microsoft Corporation / MSFT        |  10.4764 |           2.1% |                 0.45x |       20.9529 |            4.1% |
| Meta Platforms Inc. / META          |  21.7143 |           3.3% |                 0.27x |       43.4286 |            6.5% |
| Brent Crude Oil / BZ=F              |   4.0350 |           3.8% |                 0.27x |        8.0700 |            7.6% |
| Apple Inc. / AAPL                   |   7.8557 |           2.4% |                 0.43x |       15.7114 |            4.7% |
| Soybeans / ZS=F                     |  19.7321 |           1.5% |                 0.51x |       39.4643 |            3.1% |
| Corn / ZC=F                         |  10.3393 |           2.0% |                 0.27x |       20.6786 |            4.0% |
| Alphabet Inc. Class A / GOOGL       |   7.4832 |           2.1% |                 0.45x |       14.9665 |            4.3% |
| FTSE 100 / ^FTSE                    |  91.8001 |           0.9% |                 1.33x |      183.6002 |            1.7% |
| Wheat / ZW=F                        |  22.0893 |           3.1% |                 0.24x |       44.1786 |            6.2% |
| S&P 500 / ^GSPC                     |  58.3948 |           0.8% |                 1.13x |      116.7897 |            1.5% |
| Dow Jones Industrial Average / ^DJI | 458.8616 |           0.9% |                 0.92x |      917.7232 |            1.8% |
| NASDAQ 100 / ^NDX                   | 323.4763 |           1.1% |                 0.79x |      646.9526 |            2.2% |
| Hang Seng / ^HSI                    | 318.8108 |           1.3% |                 0.78x |      637.6217 |            2.6% |
| Tesla Inc. / TSLA                   |  13.9657 |           3.9% |                 0.20x |       27.9314 |            7.8% |
| Platinum / PL=F                     |  35.0929 |           2.0% |                 0.26x |       70.1857 |            4.0% |
| JPMorgan Chase & Co. / JPM          |   5.7493 |           1.6% |                 0.66x |       11.4986 |            3.3% |
| DAX / ^GDAXI                        | 257.5201 |           1.0% |                 0.92x |      515.0402 |            2.0% |
| Gold / GC=F                         |  84.3429 |           1.9% |                 0.39x |      168.6858 |            3.9% |
| Amazon.com Inc. / AMZN              |   5.7257 |           2.3% |                 0.39x |       11.4514 |            4.5% |
| Euro Stoxx 50 / ^STOXX50E           |  66.0914 |           1.1% |                 0.95x |      132.1828 |            2.1% |
| UnitedHealth Group Inc. / UNH       |  10.1390 |           2.6% |                 0.47x |       20.2780 |            5.3% |
| Russell 2000 / ^RUT                 |  28.8793 |           1.0% |                 0.80x |       57.7585 |            2.0% |
| CAC 40 / ^FCHI                      |  87.7508 |           1.1% |                 0.90x |      175.5017 |            2.2% |
| Silver / SI=F                       |   2.0277 |           3.2% |                 0.28x |        4.0554 |            6.4% |
| NVIDIA Corporation / NVDA           |   7.7407 |           3.7% |                 0.22x |       15.4815 |            7.3% |

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

Scoring engine version: **1.0.0** | Git commit: **93f3cd2**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
