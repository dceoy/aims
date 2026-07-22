+++
title = "Market Analysis 2026-07-22"
date = "2026-07-22T00:00:00+00:00"
draft = false
summary = "Bullish market: 26 reliable instruments. Top signal: ZW=F (score 73.3)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-07-22.json", "data/history/2026-07-22.json"]
market_regime = "Bullish"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "e99f27c"
+++

## Market Regime

**Bullish** — 18 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Wheat / ZW=F** — score 73.3, 20d return +13.5%, RSI14=82. 20d up +13.5%; above MA20 by 9.6%; RSI14=82 ⚠️ Upcoming: FOMC rate decision (2026-07-29)
- **UnitedHealth Group Inc. / UNH** — score 71.8, 20d return +7.3%, RSI14=62. 20d up +7.3%; above MA20 by 3.2%; RSI14=62 ⚠️ Upcoming: FOMC rate decision (2026-07-29)
- **JPMorgan Chase & Co. / JPM** — score 68.8, 20d return +4.6%, RSI14=67. 20d up +4.6%; above MA20 by 2.8%; RSI14=67 ⚠️ Upcoming: FOMC rate decision (2026-07-29)
- **Apple Inc. / AAPL** — score 68.2, 20d return +10.3%, RSI14=80. 20d up +10.3%; above MA20 by 6.2%; RSI14=80 ⚠️ Upcoming: FOMC rate decision (2026-07-29)
- **Soybeans / ZS=F** — score 63.3, 20d return +9.3%, RSI14=79. 20d up +9.3%; above MA20 by 4.4%; RSI14=79 ⚠️ Upcoming: FOMC rate decision (2026-07-29)

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                        | Applies To                      |
| ---------- | ---------------------------- | ------------------------------- |
| 2026-07-23 | ECB monetary policy decision | ^FCHI, ^GDAXI, ^STOXX50E        |
| 2026-07-29 | FOMC rate decision           | Commodity, Equity, Equity Index |
| 2026-07-29 | META earnings release        | META                            |
| 2026-07-29 | MSFT earnings release        | MSFT                            |

## Signal History

Compared with the previous available report (**2026-07-21**).
- **New top-5:** JPM, UNH
- **Persistent top signals:** ZW=F (12 reports), AAPL (7 reports), ZS=F (6 reports)
- **Dropped from top-5:** ZC=F, ^HSI

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     -5 |   -13.6 |
| 7203.T    |     +2 |    +9.7 |
| 8306.T    |     +2 |   +12.7 |
| AAPL      |     +0 |    +0.0 |
| AMZN      |     -6 |   -13.3 |
| BZ=F      |     +1 |    +1.2 |
| CL=F      |     -1 |    +2.4 |
| GC=F      |     +2 |    +3.3 |
| GOOGL     |     -6 |   -20.3 |
| HG=F      |     +2 |   +13.9 |
| JPM       |     +3 |    +6.1 |
| META      |     -4 |    -8.5 |
| MSFT      |     -6 |   -15.4 |
| NG=F      |     +0 |    +0.9 |
| NVDA      |     +1 |    -2.4 |
| PL=F      |     +1 |    +7.9 |
| SI=F      |     +2 |    +5.8 |
| TSLA      |     +0 |    +6.7 |
| UNH       |     +8 |   +19.1 |
| XOM       |     +0 |    +4.2 |
| ZC=F      |     -2 |    -2.1 |
| ZS=F      |     -4 |   -15.2 |
| ZW=F      |     +1 |    -1.2 |
| ^DJI      |     +3 |    +0.3 |
| ^FCHI     |     -3 |    -7.6 |
| ^FTSE     |     +0 |    -0.9 |
| ^GDAXI    |     +0 |    -4.8 |
| ^GSPC     |     +2 |    +0.6 |
| ^HSI      |     -5 |   -12.7 |
| ^N225     |     +0 |   +10.9 |
| ^NDX      |     +0 |    +0.6 |
| ^RUT      |     +7 |    +9.4 |
| ^STOXX50E |     +5 |    +2.4 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Copper / HG=F** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **WTI Crude Oil / CL=F** — malformed_input
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Nikkei 225 / ^N225** — missing_bars

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|    1 | Wheat / ZW=F           |  73.3 |   Yes    | —               | 20d up +13.5%; above MA20 by 9.6%; RSI14=82   |
|    5 | Soybeans / ZS=F        |  63.3 |   Yes    | —               | 20d up +9.3%; above MA20 by 4.4%; RSI14=79    |
|    6 | Brent Crude Oil / BZ=F |  63.0 |   Yes    | —               | 20d up +16.8%; above MA20 by 16.0%; RSI14=84  |
|    7 | Corn / ZC=F            |  61.8 |   Yes    | —               | 20d up +10.0%; above MA20 by 5.3%; RSI14=72   |
|   20 | Gold / GC=F            |  34.9 |   Yes    | —               | 20d down -2.6%; above MA20 by 0.2%; RSI14=54  |
|   22 | Platinum / PL=F        |  30.0 |   Yes    | —               | 20d down -2.6%; above MA20 by 0.9%; RSI14=61  |
|   23 | Silver / SI=F          |  23.0 |   Yes    | —               | 20d down -10.2%; below MA20 by 0.1%; RSI14=48 |
|   24 | Natural Gas / NG=F     |  20.3 |   Yes    | —               | 20d down -11.9%; below MA20 by 7.1%; RSI14=21 |
|   29 | Copper / HG=F          |  68.8 |    No    | malformed_input | Suppressed: malformed_input                   |
|   31 | WTI Crude Oil / CL=F   |  60.0 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    2 | UnitedHealth Group Inc. / UNH                                                  |  71.8 |   Yes    | —                             | 20d up +7.3%; above MA20 by 3.2%; RSI14=62   |
|    3 | JPMorgan Chase & Co. / JPM                                                     |  68.8 |   Yes    | —                             | 20d up +4.6%; above MA20 by 2.8%; RSI14=67   |
|    4 | Apple Inc. / AAPL                                                              |  68.2 |   Yes    | —                             | 20d up +10.3%; above MA20 by 6.2%; RSI14=80  |
|   14 | Microsoft Corporation / MSFT                                                   |  42.7 |   Yes    | —                             | 20d up +8.3%; above MA20 by 3.6%; RSI14=66   |
|   15 | Meta Platforms Inc. / META                                                     |  42.1 |   Yes    | —                             | 20d up +14.2%; above MA20 by 5.1%; RSI14=65  |
|   18 | Amazon.com Inc. / AMZN                                                         |  36.7 |   Yes    | —                             | 20d up +6.3%; above MA20 by 1.8%; RSI14=62   |
|   19 | NVIDIA Corporation / NVDA                                                      |  36.1 |   Yes    | —                             | 20d down -0.7%; above MA20 by 2.8%; RSI14=57 |
|   25 | Alphabet Inc. Class A / GOOGL                                                  |  18.5 |   Yes    | —                             | 20d down -0.7%; below MA20 by 2.2%; RSI14=44 |
|   26 | Tesla Inc. / TSLA                                                              |  17.3 |   Yes    | —                             | 20d down -6.4%; below MA20 by 4.1%; RSI14=36 |
|   27 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  73.9 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   28 | Exxon Mobil Corporation / XOM                                                  |  70.0 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   30 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  60.6 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   32 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  53.3 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    8 | Hang Seng / ^HSI                    |  57.9 |   Yes    | —            | 20d up +5.7%; above MA20 by 5.3%; RSI14=80   |
|    9 | FTSE 100 / ^FTSE                    |  53.0 |   Yes    | —            | 20d up +1.5%; above MA20 by 0.4%; RSI14=57   |
|   10 | Euro Stoxx 50 / ^STOXX50E           |  51.5 |   Yes    | —            | 20d up +0.9%; above MA20 by 0.1%; RSI14=50   |
|   11 | Russell 2000 / ^RUT                 |  51.2 |   Yes    | —            | 20d down -0.6%; above MA20 by 0.1%; RSI14=43 |
|   12 | S&P 500 / ^GSPC                     |  49.7 |   Yes    | —            | 20d up +0.5%; above MA20 by 0.4%; RSI14=51   |
|   13 | Dow Jones Industrial Average / ^DJI |  48.2 |   Yes    | —            | 20d up +1.0%; below MA20 by 0.2%; RSI14=49   |
|   16 | CAC 40 / ^FCHI                      |  42.1 |   Yes    | —            | 20d up +0.3%; below MA20 by 0.2%; RSI14=52   |
|   17 | DAX / ^GDAXI                        |  41.2 |   Yes    | —            | 20d up +0.5%; below MA20 by 0.3%; RSI14=49   |
|   21 | NASDAQ 100 / ^NDX                   |  34.9 |   Yes    | —            | 20d down -3.9%; below MA20 by 0.8%; RSI14=39 |
|   33 | Nikkei 225 / ^N225                  |  31.8 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-07-21 |
| 7203.T    | 2026-07-21 |
| 8306.T    | 2026-07-21 |
| AAPL      | 2026-07-21 |
| AMZN      | 2026-07-21 |
| BZ=F      | 2026-07-21 |
| CL=F      | 2026-07-21 |
| GC=F      | 2026-07-21 |
| GOOGL     | 2026-07-21 |
| HG=F      | 2026-07-21 |
| JPM       | 2026-07-21 |
| META      | 2026-07-21 |
| MSFT      | 2026-07-21 |
| NG=F      | 2026-07-21 |
| NVDA      | 2026-07-21 |
| PL=F      | 2026-07-21 |
| SI=F      | 2026-07-21 |
| TSLA      | 2026-07-21 |
| UNH       | 2026-07-21 |
| XOM       | 2026-07-21 |
| ZC=F      | 2026-07-21 |
| ZS=F      | 2026-07-21 |
| ZW=F      | 2026-07-21 |
| ^DJI      | 2026-07-21 |
| ^FCHI     | 2026-07-21 |
| ^FTSE     | 2026-07-21 |
| ^GDAXI    | 2026-07-21 |
| ^GSPC     | 2026-07-21 |
| ^HSI      | 2026-07-21 |
| ^N225     | 2026-07-21 |
| ^NDX      | 2026-07-21 |
| ^RUT      | 2026-07-21 |
| ^STOXX50E | 2026-07-21 |

## Symbol Details

### Wheat / ZW=F (score 73.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.6% |
| ret_5d     |  +7.4% |
| ret_20d    | +13.5% |
| ret_60d    | +11.0% |
| ma20_dist  |  +9.6% |
| ma50_dist  |  +9.7% |
| vol_20d    |  34.3% |
| mdd_60d    |  14.6% |
| rsi_14     |   81.8 |
| zscore_20d |    1.6 |

### UnitedHealth Group Inc. / UNH (score 71.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +3.5% |
| ret_5d     |  +2.6% |
| ret_20d    |  +7.3% |
| ret_60d    | +23.8% |
| ma20_dist  |  +3.2% |
| ma50_dist  |  +8.0% |
| vol_20d    |  27.1% |
| mdd_60d    |   6.1% |
| rsi_14     |   61.9 |
| zscore_20d |    1.9 |

### JPMorgan Chase & Co. / JPM (score 68.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.9% |
| ret_5d     |  +0.7% |
| ret_20d    |  +4.6% |
| ret_60d    | +11.3% |
| ma20_dist  |  +2.8% |
| ma50_dist  |  +8.4% |
| vol_20d    |  20.1% |
| mdd_60d    |   6.1% |
| rsi_14     |   67.1 |
| zscore_20d |    1.6 |

### Apple Inc. / AAPL (score 68.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.4% |
| ret_5d     |  +4.1% |
| ret_20d    | +10.3% |
| ret_60d    | +20.0% |
| ma20_dist  |  +6.2% |
| ma50_dist  |  +7.7% |
| vol_20d    |  36.5% |
| mdd_60d    |  12.7% |
| rsi_14     |   80.3 |
| zscore_20d |    1.1 |

### Soybeans / ZS=F (score 63.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | +1.0% |
| ret_20d    | +9.3% |
| ret_60d    | +5.2% |
| ma20_dist  | +4.4% |
| ma50_dist  | +4.7% |
| vol_20d    | 20.5% |
| mdd_60d    |  8.8% |
| rsi_14     |  79.5 |
| zscore_20d |   1.2 |

### Brent Crude Oil / BZ=F (score 63.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.0% |
| ret_5d     |  +7.4% |
| ret_20d    | +16.8% |
| ret_60d    | -13.4% |
| ma20_dist  | +16.0% |
| ma50_dist  |  +2.2% |
| vol_20d    |  50.1% |
| mdd_60d    |  39.4% |
| rsi_14     |   84.5 |
| zscore_20d |    2.0 |

### Corn / ZC=F (score 61.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.7% |
| ret_5d     |  +4.4% |
| ret_20d    | +10.0% |
| ret_60d    |  -0.6% |
| ma20_dist  |  +5.3% |
| ma50_dist  |  +3.7% |
| vol_20d    |  27.2% |
| mdd_60d    |  15.7% |
| rsi_14     |   72.2 |
| zscore_20d |    1.5 |

### Hang Seng / ^HSI (score 57.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.0% |
| ret_5d     | +3.3% |
| ret_20d    | +5.7% |
| ret_60d    | -3.9% |
| ma20_dist  | +5.3% |
| ma50_dist  | +1.7% |
| vol_20d    | 21.3% |
| mdd_60d    | 14.9% |
| rsi_14     |  80.1 |
| zscore_20d |   1.7 |

### FTSE 100 / ^FTSE (score 53.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | +0.5% |
| ret_20d    | +1.5% |
| ret_60d    | +2.0% |
| ma20_dist  | +0.4% |
| ma50_dist  | +1.3% |
| vol_20d    |  9.8% |
| mdd_60d    |  2.6% |
| rsi_14     |  57.4 |
| zscore_20d |   0.6 |

### Euro Stoxx 50 / ^STOXX50E (score 51.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | +0.1% |
| ret_20d    | +0.9% |
| ret_60d    | +6.6% |
| ma20_dist  | +0.1% |
| ma50_dist  | +2.2% |
| vol_20d    | 13.6% |
| mdd_60d    |  3.6% |
| rsi_14     |  50.3 |
| zscore_20d |   0.1 |

### Russell 2000 / ^RUT (score 51.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.5% |
| ret_5d     | +0.8% |
| ret_20d    | -0.6% |
| ret_60d    | +7.7% |
| ma20_dist  | +0.1% |
| ma50_dist  | +2.1% |
| vol_20d    | 11.0% |
| mdd_60d    |  4.8% |
| rsi_14     |  43.2 |
| zscore_20d |   0.1 |

### S&P 500 / ^GSPC (score 49.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | -0.5% |
| ret_20d    | +0.5% |
| ret_60d    | +5.6% |
| ma20_dist  | +0.4% |
| ma50_dist  | +0.5% |
| vol_20d    | 10.5% |
| mdd_60d    |  4.5% |
| rsi_14     |  50.9 |
| zscore_20d |   0.4 |

### Dow Jones Industrial Average / ^DJI (score 48.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | -0.5% |
| ret_20d    | +1.0% |
| ret_60d    | +5.9% |
| ma20_dist  | -0.2% |
| ma50_dist  | +1.8% |
| vol_20d    |  7.9% |
| mdd_60d    |  3.2% |
| rsi_14     |  48.6 |
| zscore_20d |  -0.3 |

### Microsoft Corporation / MSFT (score 42.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.1% |
| ret_5d     | +3.3% |
| ret_20d    | +8.3% |
| ret_60d    | -4.1% |
| ma20_dist  | +3.6% |
| ma50_dist  | -0.7% |
| vol_20d    | 33.8% |
| mdd_60d    | 23.4% |
| rsi_14     |  65.7 |
| zscore_20d |   1.1 |

### Meta Platforms Inc. / META (score 42.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.3% |
| ret_5d     |  -2.6% |
| ret_20d    | +14.2% |
| ret_60d    |  -2.2% |
| ma20_dist  |  +5.1% |
| ma50_dist  |  +6.3% |
| vol_20d    |  51.5% |
| mdd_60d    |  19.9% |
| rsi_14     |   65.2 |
| zscore_20d |    0.7 |

### CAC 40 / ^FCHI (score 42.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | -0.0% |
| ret_20d    | +0.3% |
| ret_60d    | +2.7% |
| ma20_dist  | -0.2% |
| ma50_dist  | +1.0% |
| vol_20d    | 11.8% |
| mdd_60d    |  4.2% |
| rsi_14     |  52.1 |
| zscore_20d |  -0.3 |

### DAX / ^GDAXI (score 41.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | -0.5% |
| ret_20d    | +0.5% |
| ret_60d    | +3.9% |
| ma20_dist  | -0.3% |
| ma50_dist  | +0.5% |
| vol_20d    | 15.6% |
| mdd_60d    |  4.7% |
| rsi_14     |  49.4 |
| zscore_20d |  -0.2 |

### Amazon.com Inc. / AMZN (score 36.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | +0.0% |
| ret_20d    | +6.3% |
| ret_60d    | -3.0% |
| ma20_dist  | +1.8% |
| ma50_dist  | -1.4% |
| vol_20d    | 24.7% |
| mdd_60d    | 17.4% |
| rsi_14     |  62.2 |
| zscore_20d |   0.7 |

### NVIDIA Corporation / NVDA (score 36.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.0% |
| ret_5d     | -2.1% |
| ret_20d    | -0.7% |
| ret_60d    | +3.8% |
| ma20_dist  | +2.8% |
| ma50_dist  | -1.2% |
| vol_20d    | 37.1% |
| mdd_60d    | 18.3% |
| rsi_14     |  56.6 |
| zscore_20d |   1.0 |

### Gold / GC=F (score 34.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.5% |
| ret_5d     |  +0.2% |
| ret_20d    |  -2.6% |
| ret_60d    | -13.5% |
| ma20_dist  |  +0.2% |
| ma50_dist  |  -5.1% |
| vol_20d    |  22.7% |
| mdd_60d    |  15.6% |
| rsi_14     |   53.8 |
| zscore_20d |    0.2 |

### NASDAQ 100 / ^NDX (score 34.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.9% |
| ret_5d     | -1.5% |
| ret_20d    | -3.9% |
| ret_60d    | +8.9% |
| ma20_dist  | -0.8% |
| ma50_dist  | -1.4% |
| vol_20d    | 24.0% |
| mdd_60d    |  7.0% |
| rsi_14     |  38.6 |
| zscore_20d |  -0.6 |

### Platinum / PL=F (score 30.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.1% |
| ret_5d     |  -0.3% |
| ret_20d    |  -2.6% |
| ret_60d    | -19.6% |
| ma20_dist  |  +0.9% |
| ma50_dist  |  -8.5% |
| vol_20d    |  34.6% |
| mdd_60d    |  29.1% |
| rsi_14     |   61.0 |
| zscore_20d |    0.5 |

### Silver / SI=F (score 23.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +3.6% |
| ret_5d     |  +0.1% |
| ret_20d    | -10.2% |
| ret_60d    | -22.0% |
| ma20_dist  |  -0.1% |
| ma50_dist  | -13.5% |
| vol_20d    |  45.5% |
| mdd_60d    |  37.1% |
| rsi_14     |   48.2 |
| zscore_20d |   -0.0 |

### Natural Gas / NG=F (score 20.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.2% |
| ret_5d     |  -1.3% |
| ret_20d    | -11.9% |
| ret_60d    |  +9.6% |
| ma20_dist  |  -7.1% |
| ma50_dist  |  -7.2% |
| vol_20d    |  37.7% |
| mdd_60d    |  14.5% |
| rsi_14     |   21.4 |
| zscore_20d |   -1.3 |

### Alphabet Inc. Class A / GOOGL (score 18.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.4% |
| ret_5d     | -3.4% |
| ret_20d    | -0.7% |
| ret_60d    | +2.5% |
| ma20_dist  | -2.2% |
| ma50_dist  | -5.8% |
| vol_20d    | 31.9% |
| mdd_60d    | 16.2% |
| rsi_14     |  43.6 |
| zscore_20d |  -0.9 |

### Tesla Inc. / TSLA (score 17.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.5% |
| ret_5d     | -4.4% |
| ret_20d    | -6.4% |
| ret_60d    | +1.4% |
| ma20_dist  | -4.1% |
| ma50_dist  | -7.3% |
| vol_20d    | 59.3% |
| mdd_60d    | 17.0% |
| rsi_14     |  36.4 |
| zscore_20d |  -1.0 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Wheat / ZW=F                        |  18.3036 |           2.7% |                 0.29x |       36.6071 |            5.4% |
| UnitedHealth Group Inc. / UNH       |  13.3743 |           3.1% |                 0.37x |       26.7486 |            6.1% |
| JPMorgan Chase & Co. / JPM          |   8.3032 |           2.4% |                 0.50x |       16.6065 |            4.8% |
| Apple Inc. / AAPL                   |   8.2329 |           2.5% |                 0.27x |       16.4657 |            5.0% |
| Soybeans / ZS=F                     |  19.4107 |           1.6% |                 0.49x |       38.8214 |            3.2% |
| Brent Crude Oil / BZ=F              |   3.8979 |           4.3% |                 0.20x |        7.7957 |            8.6% |
| Corn / ZC=F                         |   9.9464 |           2.2% |                 0.37x |       19.8929 |            4.4% |
| Hang Seng / ^HSI                    | 504.9256 |           2.0% |                 0.47x |     1009.8513 |            4.0% |
| FTSE 100 / ^FTSE                    | 119.1716 |           1.1% |                 1.02x |      238.3432 |            2.3% |
| Euro Stoxx 50 / ^STOXX50E           |  72.5256 |           1.2% |                 0.73x |      145.0513 |            2.3% |
| Russell 2000 / ^RUT                 |  39.1515 |           1.3% |                 0.91x |       78.3029 |            2.6% |
| S&P 500 / ^GSPC                     |  72.4694 |           1.0% |                 0.95x |      144.9388 |            1.9% |
| Dow Jones Industrial Average / ^DJI | 553.3853 |           1.1% |                 1.26x |     1106.7706 |            2.1% |
| Microsoft Corporation / MSFT        |  10.9036 |           2.7% |                 0.30x |       21.8071 |            5.5% |
| Meta Platforms Inc. / META          |  30.3207 |           4.7% |                 0.19x |       60.6414 |            9.4% |
| CAC 40 / ^FCHI                      |  98.0608 |           1.2% |                 0.85x |      196.1215 |            2.3% |
| DAX / ^GDAXI                        | 318.2946 |           1.3% |                 0.64x |      636.5893 |            2.5% |
| Amazon.com Inc. / AMZN              |   6.6814 |           2.7% |                 0.40x |       13.3629 |            5.4% |
| NVIDIA Corporation / NVDA           |   7.2607 |           3.5% |                 0.27x |       14.5214 |            7.0% |
| Gold / GC=F                         |  74.7429 |           1.8% |                 0.44x |      149.4858 |            3.7% |
| NASDAQ 100 / ^NDX                   | 580.2108 |           2.0% |                 0.42x |     1160.4216 |            4.0% |
| Platinum / PL=F                     |  32.0286 |           2.0% |                 0.29x |       64.0572 |            3.9% |
| Silver / SI=F                       |   1.9799 |           3.4% |                 0.22x |        3.9597 |            6.7% |
| Natural Gas / NG=F                  |   0.1124 |           3.9% |                 0.26x |        0.2247 |            7.8% |
| Alphabet Inc. Class A / GOOGL       |  10.5464 |           3.0% |                 0.31x |       21.0929 |            6.1% |
| Tesla Inc. / TSLA                   |  17.1600 |           4.5% |                 0.17x |       34.3200 |            9.1% |

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

Scoring engine version: **1.0.0** | Git commit: **e99f27c**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
