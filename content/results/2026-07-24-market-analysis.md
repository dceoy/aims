+++
title = "Market Analysis 2026-07-24"
date = "2026-07-24T00:00:00+00:00"
draft = false
summary = "Bearish market: 26 reliable instruments. Top signal: JPM (score 75.5)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-07-24.json", "data/history/2026-07-24.json"]
market_regime = "Bearish"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "e9c3416"
+++

## Market Regime

**Bearish** — 9 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **JPMorgan Chase & Co. / JPM** — score 75.5, 20d return +5.4%, RSI14=66. 20d up +5.4%; above MA20 by 3.7%; RSI14=66 ⚠️ Upcoming: FOMC rate decision (2026-07-29)
- **Soybeans / ZS=F** — score 74.8, 20d return +11.6%, RSI14=80. 20d up +11.6%; above MA20 by 4.8%; RSI14=80 ⚠️ Upcoming: FOMC rate decision (2026-07-29)
- **Wheat / ZW=F** — score 71.5, 20d return +18.9%, RSI14=80. 20d up +18.9%; above MA20 by 10.5%; RSI14=80 ⚠️ Upcoming: FOMC rate decision (2026-07-29)
- **Brent Crude Oil / BZ=F** — score 71.2, 20d return +36.5%, RSI14=92. 20d up +36.5%; above MA20 by 24.8%; RSI14=92 ⚠️ Upcoming: FOMC rate decision (2026-07-29)
- **Corn / ZC=F** — score 69.1, 20d return +14.0%, RSI14=72. 20d up +14.0%; above MA20 by 6.6%; RSI14=72 ⚠️ Upcoming: FOMC rate decision (2026-07-29)

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                        | Applies To                      |
| ---------- | ---------------------------- | ------------------------------- |
| 2026-07-29 | FOMC rate decision           | Commodity, Equity, Equity Index |
| 2026-07-29 | META earnings release        | META                            |
| 2026-07-29 | MSFT earnings release        | MSFT                            |
| 2026-07-30 | AAPL earnings release        | AAPL                            |
| 2026-07-30 | AMZN earnings release        | AMZN                            |
| 2026-07-31 | 6758.T earnings release      | 6758.T                          |
| 2026-07-31 | BOJ monetary policy decision | 6758.T, 7203.T, 8306.T, ^N225   |
| 2026-07-31 | XOM earnings release         | XOM                             |

## Signal History

Compared with the previous available report (**2026-07-23**).
- **New top-5:** None
- **Persistent top signals:** ZW=F (14 reports), ZS=F (8 reports), JPM (3 reports), BZ=F (2 reports), ZC=F (2 reports)
- **Dropped from top-5:** None

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +1 |   +10.6 |
| 7203.T    |     +1 |    +7.6 |
| 8306.T    |     +0 |    +3.0 |
| AAPL      |     -1 |    -3.3 |
| AMZN      |     -1 |    -9.7 |
| BZ=F      |     +0 |    +3.6 |
| CL=F      |     +0 |    +6.1 |
| GC=F      |     -3 |    -7.0 |
| GOOGL     |     +0 |    -6.4 |
| HG=F      |     -2 |    -8.2 |
| JPM       |     +4 |    +8.8 |
| META      |     -1 |    -2.1 |
| MSFT      |     +4 |    +3.9 |
| NG=F      |     +4 |    +6.4 |
| NVDA      |     +0 |    -4.5 |
| PL=F      |     -4 |    -6.4 |
| SI=F      |     -2 |    -7.6 |
| TSLA      |     +0 |    -7.3 |
| UNH       |     -1 |    -1.5 |
| XOM       |     +0 |    +6.4 |
| ZC=F      |     -2 |    +1.2 |
| ZS=F      |     +0 |    +3.9 |
| ZW=F      |     -2 |    -8.8 |
| ^DJI      |     +3 |    +0.6 |
| ^FCHI     |     -3 |    -7.0 |
| ^FTSE     |     -1 |    -4.2 |
| ^GDAXI    |     +0 |    -4.2 |
| ^GSPC     |     +3 |    +1.8 |
| ^HSI      |     +4 |   +13.9 |
| ^N225     |     +0 |   +12.1 |
| ^NDX      |     +0 |    -1.2 |
| ^RUT      |     +3 |    +6.7 |
| ^STOXX50E |     -4 |    -7.6 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|    2 | Soybeans / ZS=F        |  74.8 |   Yes    | —               | 20d up +11.6%; above MA20 by 4.8%; RSI14=80  |
|    3 | Wheat / ZW=F           |  71.5 |   Yes    | —               | 20d up +18.9%; above MA20 by 10.5%; RSI14=80 |
|    4 | Brent Crude Oil / BZ=F |  71.2 |   Yes    | —               | 20d up +36.5%; above MA20 by 24.8%; RSI14=92 |
|    5 | Corn / ZC=F            |  69.1 |   Yes    | —               | 20d up +14.0%; above MA20 by 6.6%; RSI14=72  |
|   17 | Gold / GC=F            |  40.0 |   Yes    | —               | 20d up +1.4%; below MA20 by 0.5%; RSI14=45   |
|   18 | Natural Gas / NG=F     |  36.7 |   Yes    | —               | 20d down -9.5%; below MA20 by 4.7%; RSI14=30 |
|   22 | Platinum / PL=F        |  27.6 |   Yes    | —               | 20d up +1.2%; below MA20 by 0.8%; RSI14=47   |
|   23 | Silver / SI=F          |  23.6 |   Yes    | —               | 20d down -0.4%; below MA20 by 1.7%; RSI14=43 |
|   29 | WTI Crude Oil / CL=F   |  70.0 |    No    | malformed_input | Suppressed: malformed_input                  |
|   32 | Copper / HG=F          |  52.4 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                    |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | ---------------------------------------------- |
|    1 | JPMorgan Chase & Co. / JPM                                                     |  75.5 |   Yes    | —                             | 20d up +5.4%; above MA20 by 3.7%; RSI14=66     |
|    8 | Apple Inc. / AAPL                                                              |  57.0 |   Yes    | —                             | 20d up +9.8%; above MA20 by 3.3%; RSI14=63     |
|    9 | UnitedHealth Group Inc. / UNH                                                  |  56.4 |   Yes    | —                             | 20d up +4.4%; below MA20 by 0.3%; RSI14=49     |
|   11 | NVIDIA Corporation / NVDA                                                      |  47.3 |   Yes    | —                             | 20d up +4.9%; above MA20 by 3.0%; RSI14=62     |
|   20 | Microsoft Corporation / MSFT                                                   |  30.6 |   Yes    | —                             | 20d up +4.4%; below MA20 by 1.0%; RSI14=44     |
|   21 | Meta Platforms Inc. / META                                                     |  29.4 |   Yes    | —                             | 20d up +8.7%; below MA20 by 2.0%; RSI14=55     |
|   24 | Amazon.com Inc. / AMZN                                                         |  19.7 |   Yes    | —                             | 20d down -0.3%; below MA20 by 4.1%; RSI14=40   |
|   25 | Alphabet Inc. Class A / GOOGL                                                  |   8.8 |   Yes    | —                             | 20d down -8.0%; below MA20 by 10.1%; RSI14=30  |
|   26 | Tesla Inc. / TSLA                                                              |   2.7 |   Yes    | —                             | 20d down -14.9%; below MA20 by 18.4%; RSI14=29 |
|   27 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  80.9 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   28 | Exxon Mobil Corporation / XOM                                                  |  77.9 |    No    | malformed_input               | Suppressed: malformed_input                    |
|   30 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  64.8 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   31 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  60.9 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    6 | Hang Seng / ^HSI                    |  66.4 |   Yes    | —            | 20d up +7.7%; above MA20 by 4.9%; RSI14=74   |
|    7 | FTSE 100 / ^FTSE                    |  61.5 |   Yes    | —            | 20d up +1.0%; above MA20 by 0.7%; RSI14=47   |
|   10 | Dow Jones Industrial Average / ^DJI |  47.9 |   Yes    | —            | 20d down -0.3%; below MA20 by 1.2%; RSI14=31 |
|   12 | S&P 500 / ^GSPC                     |  47.3 |   Yes    | —            | 20d up +0.7%; below MA20 by 1.1%; RSI14=44   |
|   13 | Euro Stoxx 50 / ^STOXX50E           |  46.4 |   Yes    | —            | 20d down -0.9%; below MA20 by 1.2%; RSI14=33 |
|   14 | Russell 2000 / ^RUT                 |  46.1 |   Yes    | —            | 20d down -1.6%; below MA20 by 1.4%; RSI14=40 |
|   15 | CAC 40 / ^FCHI                      |  43.9 |   Yes    | —            | 20d down -1.6%; below MA20 by 1.0%; RSI14=34 |
|   16 | DAX / ^GDAXI                        |  40.9 |   Yes    | —            | 20d down -0.9%; below MA20 by 1.3%; RSI14=28 |
|   19 | NASDAQ 100 / ^NDX                   |  32.1 |   Yes    | —            | 20d down -2.6%; below MA20 by 3.0%; RSI14=41 |
|   33 | Nikkei 225 / ^N225                  |  38.5 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-07-23 |
| 7203.T    | 2026-07-23 |
| 8306.T    | 2026-07-23 |
| AAPL      | 2026-07-23 |
| AMZN      | 2026-07-23 |
| BZ=F      | 2026-07-23 |
| CL=F      | 2026-07-23 |
| GC=F      | 2026-07-23 |
| GOOGL     | 2026-07-23 |
| HG=F      | 2026-07-23 |
| JPM       | 2026-07-23 |
| META      | 2026-07-23 |
| MSFT      | 2026-07-23 |
| NG=F      | 2026-07-23 |
| NVDA      | 2026-07-23 |
| PL=F      | 2026-07-23 |
| SI=F      | 2026-07-23 |
| TSLA      | 2026-07-23 |
| UNH       | 2026-07-23 |
| XOM       | 2026-07-23 |
| ZC=F      | 2026-07-23 |
| ZS=F      | 2026-07-23 |
| ZW=F      | 2026-07-23 |
| ^DJI      | 2026-07-23 |
| ^FCHI     | 2026-07-23 |
| ^FTSE     | 2026-07-23 |
| ^GDAXI    | 2026-07-23 |
| ^GSPC     | 2026-07-23 |
| ^HSI      | 2026-07-23 |
| ^N225     | 2026-07-23 |
| ^NDX      | 2026-07-23 |
| ^RUT      | 2026-07-23 |
| ^STOXX50E | 2026-07-23 |

## Symbol Details

### JPMorgan Chase & Co. / JPM (score 75.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.5% |
| ret_5d     |  +2.0% |
| ret_20d    |  +5.4% |
| ret_60d    | +12.8% |
| ma20_dist  |  +3.7% |
| ma50_dist  |  +9.2% |
| vol_20d    |  20.1% |
| mdd_60d    |   6.1% |
| rsi_14     |   65.6 |
| zscore_20d |    1.8 |

### Soybeans / ZS=F (score 74.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.4% |
| ret_5d     |  +3.6% |
| ret_20d    | +11.6% |
| ret_60d    |  +5.1% |
| ma20_dist  |  +4.8% |
| ma50_dist  |  +6.1% |
| vol_20d    |  20.1% |
| mdd_60d    |   8.8% |
| rsi_14     |   79.8 |
| zscore_20d |    1.4 |

### Wheat / ZW=F (score 71.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.3% |
| ret_5d     |  +3.2% |
| ret_20d    | +18.9% |
| ret_60d    | +12.0% |
| ma20_dist  | +10.5% |
| ma50_dist  | +12.1% |
| vol_20d    |  35.8% |
| mdd_60d    |  14.6% |
| rsi_14     |   79.8 |
| zscore_20d |    1.5 |

### Brent Crude Oil / BZ=F (score 71.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +7.0% |
| ret_5d     | +19.5% |
| ret_20d    | +36.5% |
| ret_60d    |  -7.0% |
| ma20_dist  | +24.8% |
| ma50_dist  | +13.4% |
| vol_20d    |  50.4% |
| mdd_60d    |  39.4% |
| rsi_14     |   92.1 |
| zscore_20d |    2.4 |

### Corn / ZC=F (score 69.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.4% |
| ret_5d     |  +5.1% |
| ret_20d    | +14.0% |
| ret_60d    |  +0.7% |
| ma20_dist  |  +6.6% |
| ma50_dist  |  +6.2% |
| vol_20d    |  27.1% |
| mdd_60d    |  15.7% |
| rsi_14     |   71.9 |
| zscore_20d |    1.8 |

### Hang Seng / ^HSI (score 66.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.3% |
| ret_5d     | +0.8% |
| ret_20d    | +7.7% |
| ret_60d    | -3.0% |
| ma20_dist  | +4.9% |
| ma50_dist  | +2.2% |
| vol_20d    | 20.7% |
| mdd_60d    | 14.9% |
| rsi_14     |  74.3 |
| zscore_20d |   1.4 |

### FTSE 100 / ^FTSE (score 61.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | +0.6% |
| ret_20d    | +1.0% |
| ret_60d    | +3.0% |
| ma20_dist  | +0.7% |
| ma50_dist  | +1.7% |
| vol_20d    | 10.8% |
| mdd_60d    |  2.6% |
| rsi_14     |  47.3 |
| zscore_20d |   1.0 |

### Apple Inc. / AAPL (score 57.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.3% |
| ret_5d     |  -3.5% |
| ret_20d    |  +9.8% |
| ret_60d    | +20.3% |
| ma20_dist  |  +3.3% |
| ma50_dist  |  +5.3% |
| vol_20d    |  36.8% |
| mdd_60d    |  12.7% |
| rsi_14     |   63.0 |
| zscore_20d |    0.6 |

### UnitedHealth Group Inc. / UNH (score 56.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.8% |
| ret_5d     |  +0.0% |
| ret_20d    |  +4.4% |
| ret_60d    | +20.1% |
| ma20_dist  |  -0.3% |
| ma50_dist  |  +4.3% |
| vol_20d    |  28.2% |
| mdd_60d    |   6.1% |
| rsi_14     |   49.0 |
| zscore_20d |   -0.2 |

### Dow Jones Industrial Average / ^DJI (score 47.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | -1.6% |
| ret_20d    | -0.3% |
| ret_60d    | +5.2% |
| ma20_dist  | -1.2% |
| ma50_dist  | +0.6% |
| vol_20d    |  8.6% |
| mdd_60d    |  3.2% |
| rsi_14     |  31.2 |
| zscore_20d |  -1.8 |

### NVIDIA Corporation / NVDA (score 47.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.6% |
| ret_5d     | +0.7% |
| ret_20d    | +4.9% |
| ret_60d    | -3.6% |
| ma20_dist  | +3.0% |
| ma50_dist  | -0.3% |
| vol_20d    | 35.1% |
| mdd_60d    | 18.3% |
| rsi_14     |  62.1 |
| zscore_20d |   0.9 |

### S&P 500 / ^GSPC (score 47.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.2% |
| ret_5d     | -1.7% |
| ret_20d    | +0.7% |
| ret_60d    | +3.3% |
| ma20_dist  | -1.1% |
| ma50_dist  | -0.8% |
| vol_20d    | 10.1% |
| mdd_60d    |  4.5% |
| rsi_14     |  43.9 |
| zscore_20d |  -1.3 |

### Euro Stoxx 50 / ^STOXX50E (score 46.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.7% |
| ret_5d     | -1.2% |
| ret_20d    | -0.9% |
| ret_60d    | +6.0% |
| ma20_dist  | -1.2% |
| ma50_dist  | +0.7% |
| vol_20d    | 14.7% |
| mdd_60d    |  3.6% |
| rsi_14     |  33.0 |
| zscore_20d |  -1.3 |

### Russell 2000 / ^RUT (score 46.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | -1.2% |
| ret_20d    | -1.6% |
| ret_60d    | +5.5% |
| ma20_dist  | -1.4% |
| ma50_dist  | +0.4% |
| vol_20d    | 11.1% |
| mdd_60d    |  4.8% |
| rsi_14     |  40.4 |
| zscore_20d |  -1.7 |

### CAC 40 / ^FCHI (score 43.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.6% |
| ret_5d     | -0.9% |
| ret_20d    | -1.6% |
| ret_60d    | +2.8% |
| ma20_dist  | -1.0% |
| ma50_dist  | +0.1% |
| vol_20d    | 13.2% |
| mdd_60d    |  4.2% |
| rsi_14     |  34.3 |
| zscore_20d |  -1.3 |

### DAX / ^GDAXI (score 40.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.6% |
| ret_5d     | -0.6% |
| ret_20d    | -0.9% |
| ret_60d    | +3.4% |
| ma20_dist  | -1.3% |
| ma50_dist  | -0.6% |
| vol_20d    | 16.2% |
| mdd_60d    |  4.7% |
| rsi_14     |  28.3 |
| zscore_20d |  -1.0 |

### Gold / GC=F (score 40.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.4% |
| ret_5d     |  +1.5% |
| ret_20d    |  +1.4% |
| ret_60d    | -13.4% |
| ma20_dist  |  -0.5% |
| ma50_dist  |  -5.2% |
| vol_20d    |  21.7% |
| mdd_60d    |  15.6% |
| rsi_14     |   45.4 |
| zscore_20d |   -0.4 |

### Natural Gas / NG=F (score 36.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.3% |
| ret_5d     |  +2.0% |
| ret_20d    |  -9.5% |
| ret_60d    | +14.4% |
| ma20_dist  |  -4.7% |
| ma50_dist  |  -5.6% |
| vol_20d    |  36.3% |
| mdd_60d    |  14.5% |
| rsi_14     |   30.2 |
| zscore_20d |   -0.8 |

### NASDAQ 100 / ^NDX (score 32.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.9% |
| ret_5d     | -2.0% |
| ret_20d    | -2.6% |
| ret_60d    | +4.2% |
| ma20_dist  | -3.0% |
| ma50_dist  | -3.7% |
| vol_20d    | 22.2% |
| mdd_60d    |  7.2% |
| rsi_14     |  40.7 |
| zscore_20d |  -1.9 |

### Microsoft Corporation / MSFT (score 30.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.2% |
| ret_5d     |  -4.9% |
| ret_20d    |  +4.4% |
| ret_60d    | -10.0% |
| ma20_dist  |  -1.0% |
| ma50_dist  |  -4.5% |
| vol_20d    |  34.3% |
| mdd_60d    |  23.4% |
| rsi_14     |   44.3 |
| zscore_20d |   -0.3 |

### Meta Platforms Inc. / META (score 29.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -3.4% |
| ret_5d     |  -8.8% |
| ret_20d    |  +8.7% |
| ret_60d    | -10.6% |
| ma20_dist  |  -2.0% |
| ma50_dist  |  +0.0% |
| vol_20d    |  54.2% |
| mdd_60d    |  19.1% |
| rsi_14     |   55.2 |
| zscore_20d |   -0.3 |

### Platinum / PL=F (score 27.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.7% |
| ret_5d     |  -2.2% |
| ret_20d    |  +1.2% |
| ret_60d    | -19.3% |
| ma20_dist  |  -0.8% |
| ma50_dist  |  -9.1% |
| vol_20d    |  31.7% |
| mdd_60d    |  29.1% |
| rsi_14     |   47.4 |
| zscore_20d |   -0.5 |

### Silver / SI=F (score 23.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -3.7% |
| ret_5d     |  +3.4% |
| ret_20d    |  -0.4% |
| ret_60d    | -22.9% |
| ma20_dist  |  -1.7% |
| ma50_dist  | -13.8% |
| vol_20d    |  38.5% |
| mdd_60d    |  37.1% |
| rsi_14     |   43.0 |
| zscore_20d |   -0.6 |

### Amazon.com Inc. / AMZN (score 19.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -4.6% |
| ret_5d     |  -6.5% |
| ret_20d    |  -0.3% |
| ret_60d    | -10.5% |
| ma20_dist  |  -4.1% |
| ma50_dist  |  -6.5% |
| vol_20d    |  30.2% |
| mdd_60d    |  17.4% |
| rsi_14     |   40.5 |
| zscore_20d |   -1.5 |

### Alphabet Inc. Class A / GOOGL (score 8.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -7.1% |
| ret_5d     | -10.4% |
| ret_20d    |  -8.0% |
| ret_60d    |  -9.3% |
| ma20_dist  | -10.1% |
| ma50_dist  | -13.2% |
| vol_20d    |  40.4% |
| mdd_60d    |  21.0% |
| rsi_14     |   29.6 |
| zscore_20d |   -3.0 |

### Tesla Inc. / TSLA (score 2.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     | -14.5% |
| ret_5d     | -18.3% |
| ret_20d    | -14.9% |
| ret_60d    | -15.6% |
| ma20_dist  | -18.4% |
| ma50_dist  | -21.1% |
| vol_20d    |  75.1% |
| mdd_60d    |  28.2% |
| rsi_14     |   29.0 |
| zscore_20d |   -3.1 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| JPMorgan Chase & Co. / JPM          |   7.6279 |           2.2% |                 0.50x |       15.2557 |            4.4% |
| Soybeans / ZS=F                     |  19.7500 |           1.6% |                 0.50x |       39.5000 |            3.2% |
| Wheat / ZW=F                        |  19.5357 |           2.8% |                 0.28x |       39.0714 |            5.6% |
| Brent Crude Oil / BZ=F              |   4.4793 |           4.4% |                 0.20x |        8.9586 |            8.9% |
| Corn / ZC=F                         |   9.9821 |           2.2% |                 0.37x |       19.9643 |            4.3% |
| Hang Seng / ^HSI                    | 490.9413 |           1.9% |                 0.48x |      981.8825 |            3.9% |
| FTSE 100 / ^FTSE                    | 115.5644 |           1.1% |                 0.93x |      231.1288 |            2.2% |
| Apple Inc. / AAPL                   |   7.4521 |           2.3% |                 0.27x |       14.9043 |            4.6% |
| UnitedHealth Group Inc. / UNH       |  12.9179 |           3.0% |                 0.35x |       25.8357 |            6.1% |
| Dow Jones Industrial Average / ^DJI | 533.6872 |           1.0% |                 1.16x |     1067.3744 |            2.1% |
| NVIDIA Corporation / NVDA           |   7.3457 |           3.5% |                 0.28x |       14.6914 |            7.0% |
| S&P 500 / ^GSPC                     |  70.8743 |           1.0% |                 0.99x |      141.7487 |            1.9% |
| Euro Stoxx 50 / ^STOXX50E           |  73.1314 |           1.2% |                 0.68x |      146.2628 |            2.4% |
| Russell 2000 / ^RUT                 |  36.5107 |           1.2% |                 0.90x |       73.0214 |            2.5% |
| CAC 40 / ^FCHI                      | 101.3714 |           1.2% |                 0.76x |      202.7429 |            2.4% |
| DAX / ^GDAXI                        | 306.7812 |           1.2% |                 0.62x |      613.5625 |            2.5% |
| Gold / GC=F                         |  72.3286 |           1.8% |                 0.46x |      144.6572 |            3.6% |
| Natural Gas / NG=F                  |   0.1139 |           3.9% |                 0.28x |        0.2279 |            7.8% |
| NASDAQ 100 / ^NDX                   | 545.9152 |           1.9% |                 0.45x |     1091.8304 |            3.8% |
| Microsoft Corporation / MSFT        |  11.1979 |           2.9% |                 0.29x |       22.3957 |            5.9% |
| Meta Platforms Inc. / META          |  27.2829 |           4.5% |                 0.18x |       54.5657 |            9.0% |
| Platinum / PL=F                     |  29.6571 |           1.9% |                 0.32x |       59.3143 |            3.7% |
| Silver / SI=F                       |   1.8499 |           3.2% |                 0.26x |        3.6997 |            6.4% |
| Amazon.com Inc. / AMZN              |   6.9071 |           3.0% |                 0.33x |       13.8143 |            5.9% |
| Alphabet Inc. Class A / GOOGL       |  11.8371 |           3.7% |                 0.25x |       23.6743 |            7.5% |
| Tesla Inc. / TSLA                   |  17.7114 |           5.5% |                 0.13x |       35.4229 |           11.1% |

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

Scoring engine version: **1.0.0** | Git commit: **e9c3416**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
