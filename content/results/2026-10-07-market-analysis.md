+++
title = "Market Analysis 2026-10-07"
date = "2026-10-07T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: MSFT (score 84.8)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-10-07.json", "data/history/2026-10-07.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "29d1ebc"
+++

## Market Regime

**Neutral** — 11 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Microsoft Corporation / MSFT** — score 84.8, 20d return +7.2%, RSI14=76. 20d up +7.2%; above MA20 by 4.9%; RSI14=76
- **NASDAQ 100 / ^NDX** — score 75.2, 20d return +5.8%, RSI14=83. 20d up +5.8%; above MA20 by 3.8%; RSI14=83
- **NVIDIA Corporation / NVDA** — score 74.8, 20d return +6.1%, RSI14=84. 20d up +6.1%; above MA20 by 6.4%; RSI14=84
- **S&P 500 / ^GSPC** — score 73.6, 20d return +1.9%, RSI14=73. 20d up +1.9%; above MA20 by 1.8%; RSI14=73
- **Amazon.com Inc. / AMZN** — score 62.4, 20d return -0.3%, RSI14=64. 20d down -0.3%; above MA20 by 2.0%; RSI14=64

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                | Applies To |
| ---------- | -------------------- | ---------- |
| 2026-10-13 | JPM earnings release | JPM        |
| 2026-10-13 | UNH earnings release | UNH        |

## Signal History

Compared with the previous available report (**2026-10-06**).

- **New top-5:** AMZN
- **Persistent top signals:** MSFT (8 reports), ^NDX (8 reports), ^GSPC (6 reports), NVDA (5 reports)
- **Dropped from top-5:** META

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +1 |    +7.9 |
| 7203.T    |     +0 |    +6.7 |
| 8306.T    |     +1 |    +8.5 |
| AAPL      |     -1 |    +2.1 |
| AMZN      |     +5 |   +14.2 |
| BZ=F      |     -1 |    -1.8 |
| CL=F      |     +0 |    -3.9 |
| GC=F      |     +2 |    +2.7 |
| GOOGL     |     -3 |    -2.7 |
| HG=F      |     -2 |    -9.1 |
| JPM       |     +1 |    -2.1 |
| META      |     -4 |   -16.4 |
| MSFT      |     +0 |    +0.0 |
| NG=F      |     +0 |    +5.2 |
| NVDA      |     -1 |    -5.8 |
| PL=F      |     -5 |   -12.4 |
| SI=F      |     -1 |    -2.7 |
| TSLA      |     -1 |    -4.8 |
| UNH       |     -6 |   -16.1 |
| XOM       |     +0 |    +1.5 |
| ZC=F      |     +6 |   +14.8 |
| ZS=F      |     +6 |   +12.7 |
| ZW=F      |     +2 |    +6.4 |
| ^DJI      |     +3 |    +2.4 |
| ^FCHI     |     +1 |    +1.2 |
| ^FTSE     |     +0 |    -1.2 |
| ^GDAXI    |     -1 |    +3.6 |
| ^GSPC     |     +0 |    -0.6 |
| ^HSI      |     +4 |    +5.2 |
| ^N225     |     +0 |    -1.2 |
| ^NDX      |     +1 |    -0.9 |
| ^RUT      |     -4 |   -11.2 |
| ^STOXX50E |     -3 |    -2.1 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Nikkei 225 / ^N225** — missing_bars
- **Natural Gas / NG=F** — malformed_input
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **WTI Crude Oil / CL=F** — malformed_input

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|    6 | Soybeans / ZS=F        |  60.3 |   Yes    | —               | 20d up +0.0%; below MA20 by 0.0%; RSI14=44   |
|   13 | Corn / ZC=F            |  46.4 |   Yes    | —               | 20d down -0.6%; below MA20 by 2.2%; RSI14=34 |
|   15 | Wheat / ZW=F           |  44.9 |   Yes    | —               | 20d down -3.6%; below MA20 by 0.3%; RSI14=39 |
|   19 | Brent Crude Oil / BZ=F |  32.7 |   Yes    | —               | 20d up +2.7%; below MA20 by 3.0%; RSI14=39   |
|   21 | Gold / GC=F            |  29.4 |   Yes    | —               | 20d down -5.7%; below MA20 by 2.8%; RSI14=28 |
|   22 | Silver / SI=F          |  27.6 |   Yes    | —               | 20d down -7.7%; below MA20 by 3.6%; RSI14=38 |
|   25 | Platinum / PL=F        |  17.9 |   Yes    | —               | 20d down -8.4%; below MA20 by 3.9%; RSI14=37 |
|   27 | Natural Gas / NG=F     |  70.3 |    No    | malformed_input | Suppressed: malformed_input                  |
|   31 | Copper / HG=F          |  50.6 |    No    | malformed_input | Suppressed: malformed_input                  |
|   33 | WTI Crude Oil / CL=F   |  20.9 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    1 | Microsoft Corporation / MSFT                                                   |  84.8 |   Yes    | —                             | 20d up +7.2%; above MA20 by 4.9%; RSI14=76   |
|    3 | NVIDIA Corporation / NVDA                                                      |  74.8 |   Yes    | —                             | 20d up +6.1%; above MA20 by 6.4%; RSI14=84   |
|    5 | Amazon.com Inc. / AMZN                                                         |  62.4 |   Yes    | —                             | 20d down -0.3%; above MA20 by 2.0%; RSI14=64 |
|    7 | Tesla Inc. / TSLA                                                              |  59.1 |   Yes    | —                             | 20d up +3.4%; above MA20 by 3.8%; RSI14=64   |
|    8 | Apple Inc. / AAPL                                                              |  54.5 |   Yes    | —                             | 20d up +5.5%; above MA20 by 0.1%; RSI14=51   |
|    9 | Meta Platforms Inc. / META                                                     |  54.5 |   Yes    | —                             | 20d up +20.5%; above MA20 by 4.3%; RSI14=62  |
|   11 | Alphabet Inc. Class A / GOOGL                                                  |  48.5 |   Yes    | —                             | 20d up +2.8%; above MA20 by 1.2%; RSI14=54   |
|   20 | UnitedHealth Group Inc. / UNH                                                  |  29.7 |   Yes    | —                             | 20d down -5.5%; above MA20 by 0.0%; RSI14=51 |
|   23 | JPMorgan Chase & Co. / JPM                                                     |  22.7 |   Yes    | —                             | 20d down -5.8%; below MA20 by 2.9%; RSI14=30 |
|   28 | Exxon Mobil Corporation / XOM                                                  |  62.1 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   29 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  61.5 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   30 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  57.6 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   32 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  40.0 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    2 | NASDAQ 100 / ^NDX                   |  75.2 |   Yes    | —            | 20d up +5.8%; above MA20 by 3.8%; RSI14=83   |
|    4 | S&P 500 / ^GSPC                     |  73.6 |   Yes    | —            | 20d up +1.9%; above MA20 by 1.8%; RSI14=73   |
|   10 | DAX / ^GDAXI                        |  53.6 |   Yes    | —            | 20d down -2.1%; above MA20 by 0.2%; RSI14=48 |
|   12 | Dow Jones Industrial Average / ^DJI |  47.0 |   Yes    | —            | 20d down -2.4%; below MA20 by 0.3%; RSI14=51 |
|   14 | Euro Stoxx 50 / ^STOXX50E           |  46.1 |   Yes    | —            | 20d down -2.2%; below MA20 by 0.1%; RSI14=50 |
|   16 | FTSE 100 / ^FTSE                    |  41.2 |   Yes    | —            | 20d down -2.5%; below MA20 by 0.9%; RSI14=41 |
|   17 | Russell 2000 / ^RUT                 |  35.5 |   Yes    | —            | 20d down -4.4%; below MA20 by 0.8%; RSI14=44 |
|   18 | Hang Seng / ^HSI                    |  35.1 |   Yes    | —            | 20d down -4.5%; below MA20 by 1.8%; RSI14=42 |
|   24 | CAC 40 / ^FCHI                      |  22.7 |   Yes    | —            | 20d down -5.4%; below MA20 by 2.4%; RSI14=31 |
|   26 | Nikkei 225 / ^N225                  |  76.7 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-10-06 |
| 7203.T    | 2026-10-06 |
| 8306.T    | 2026-10-06 |
| AAPL      | 2026-10-06 |
| AMZN      | 2026-10-06 |
| BZ=F      | 2026-10-06 |
| CL=F      | 2026-10-06 |
| GC=F      | 2026-10-06 |
| GOOGL     | 2026-10-06 |
| HG=F      | 2026-10-06 |
| JPM       | 2026-10-06 |
| META      | 2026-10-06 |
| MSFT      | 2026-10-06 |
| NG=F      | 2026-10-06 |
| NVDA      | 2026-10-06 |
| PL=F      | 2026-10-06 |
| SI=F      | 2026-10-06 |
| TSLA      | 2026-10-06 |
| UNH       | 2026-10-06 |
| XOM       | 2026-10-06 |
| ZC=F      | 2026-10-06 |
| ZS=F      | 2026-10-06 |
| ZW=F      | 2026-10-06 |
| ^DJI      | 2026-10-06 |
| ^FCHI     | 2026-10-06 |
| ^FTSE     | 2026-10-06 |
| ^GDAXI    | 2026-10-06 |
| ^GSPC     | 2026-10-06 |
| ^HSI      | 2026-10-06 |
| ^N225     | 2026-10-06 |
| ^NDX      | 2026-10-06 |
| ^RUT      | 2026-10-06 |
| ^STOXX50E | 2026-10-06 |

## Symbol Details

### Microsoft Corporation / MSFT (score 84.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.8% |
| ret_5d     |  +4.0% |
| ret_20d    |  +7.2% |
| ret_60d    | +35.4% |
| ma20_dist  |  +4.9% |
| ma50_dist  |  +7.3% |
| vol_20d    |  20.3% |
| mdd_60d    |   5.1% |
| rsi_14     |   76.3 |
| zscore_20d |    2.2 |

### NASDAQ 100 / ^NDX (score 75.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | +2.9% |
| ret_20d    | +5.8% |
| ret_60d    | +6.7% |
| ma20_dist  | +3.8% |
| ma50_dist  | +5.6% |
| vol_20d    | 15.0% |
| mdd_60d    |  8.1% |
| rsi_14     |  82.9 |
| zscore_20d |   1.6 |

### NVIDIA Corporation / NVDA (score 74.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.1% |
| ret_5d     |  +5.3% |
| ret_20d    |  +6.1% |
| ret_60d    | +17.5% |
| ma20_dist  |  +6.4% |
| ma50_dist  |  +8.9% |
| vol_20d    |  23.5% |
| mdd_60d    |  10.6% |
| rsi_14     |   84.0 |
| zscore_20d |    1.9 |

### S&P 500 / ^GSPC (score 73.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | +1.9% |
| ret_20d    | +1.9% |
| ret_60d    | +4.0% |
| ma20_dist  | +1.8% |
| ma50_dist  | +1.9% |
| vol_20d    | 10.2% |
| mdd_60d    |  3.4% |
| rsi_14     |  73.3 |
| zscore_20d |   2.0 |

### Amazon.com Inc. / AMZN (score 62.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.9% |
| ret_5d     | +3.9% |
| ret_20d    | -0.3% |
| ret_60d    | +3.6% |
| ma20_dist  | +2.0% |
| ma50_dist  | -0.4% |
| vol_20d    | 21.9% |
| mdd_60d    | 13.4% |
| rsi_14     |  63.7 |
| zscore_20d |   1.5 |

### Soybeans / ZS=F (score 60.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.7% |
| ret_5d     | +0.4% |
| ret_20d    | +0.0% |
| ret_60d    | +9.0% |
| ma20_dist  | -0.0% |
| ma50_dist  | +4.2% |
| vol_20d    | 20.2% |
| mdd_60d    |  8.1% |
| rsi_14     |  43.7 |
| zscore_20d |  -0.0 |

### Tesla Inc. / TSLA (score 59.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | +7.9% |
| ret_20d    | +3.4% |
| ret_60d    | -3.6% |
| ma20_dist  | +3.8% |
| ma50_dist  | +8.7% |
| vol_20d    | 29.1% |
| mdd_60d    | 24.7% |
| rsi_14     |  63.7 |
| zscore_20d |   1.5 |

### Apple Inc. / AAPL (score 54.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | +1.3% |
| ret_20d    | +5.5% |
| ret_60d    | +5.2% |
| ma20_dist  | +0.1% |
| ma50_dist  | +3.5% |
| vol_20d    | 19.8% |
| mdd_60d    | 11.0% |
| rsi_14     |  51.5 |
| zscore_20d |   0.0 |

### Meta Platforms Inc. / META (score 54.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.4% |
| ret_5d     |  +0.0% |
| ret_20d    | +20.5% |
| ret_60d    | +12.5% |
| ma20_dist  |  +4.3% |
| ma50_dist  | +17.2% |
| vol_20d    |  55.6% |
| mdd_60d    |  20.9% |
| rsi_14     |   62.4 |
| zscore_20d |    0.8 |

### DAX / ^GDAXI (score 53.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.8% |
| ret_5d     | +0.2% |
| ret_20d    | -2.1% |
| ret_60d    | +1.2% |
| ma20_dist  | +0.2% |
| ma50_dist  | -1.5% |
| vol_20d    | 13.0% |
| mdd_60d    |  6.1% |
| rsi_14     |  48.1 |
| zscore_20d |   0.3 |

### Alphabet Inc. Class A / GOOGL (score 48.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +2.0% |
| ret_20d    | +2.8% |
| ret_60d    | -1.4% |
| ma20_dist  | +1.2% |
| ma50_dist  | +0.7% |
| vol_20d    | 25.1% |
| mdd_60d    | 14.4% |
| rsi_14     |  54.2 |
| zscore_20d |   0.7 |

### Dow Jones Industrial Average / ^DJI (score 47.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | +0.3% |
| ret_20d    | -2.4% |
| ret_60d    | -1.9% |
| ma20_dist  | -0.3% |
| ma50_dist  | -2.2% |
| vol_20d    |  9.9% |
| mdd_60d    |  6.3% |
| rsi_14     |  50.9 |
| zscore_20d |  -0.4 |

### Corn / ZC=F (score 46.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.2% |
| ret_5d     |  -2.7% |
| ret_20d    |  -0.6% |
| ret_60d    | +15.1% |
| ma20_dist  |  -2.2% |
| ma50_dist  |  +2.7% |
| vol_20d    |  27.6% |
| mdd_60d    |   8.4% |
| rsi_14     |   34.2 |
| zscore_20d |   -0.8 |

### Euro Stoxx 50 / ^STOXX50E (score 46.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | -0.8% |
| ret_20d    | -2.2% |
| ret_60d    | -0.1% |
| ma20_dist  | -0.1% |
| ma50_dist  | -1.7% |
| vol_20d    | 13.4% |
| mdd_60d    |  5.7% |
| rsi_14     |  50.5 |
| zscore_20d |  -0.2 |

### Wheat / ZW=F (score 44.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.7% |
| ret_5d     | +1.7% |
| ret_20d    | -3.6% |
| ret_60d    | +4.4% |
| ma20_dist  | -0.3% |
| ma50_dist  | +1.4% |
| vol_20d    | 25.1% |
| mdd_60d    | 11.9% |
| rsi_14     |  38.6 |
| zscore_20d |  -0.1 |

### FTSE 100 / ^FTSE (score 41.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | -0.9% |
| ret_20d    | -2.5% |
| ret_60d    | +0.4% |
| ma20_dist  | -0.9% |
| ma50_dist  | -2.0% |
| vol_20d    | 11.3% |
| mdd_60d    |  4.4% |
| rsi_14     |  41.0 |
| zscore_20d |  -1.1 |

### Russell 2000 / ^RUT (score 35.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | +0.8% |
| ret_20d    | -4.4% |
| ret_60d    | -4.2% |
| ma20_dist  | -0.8% |
| ma50_dist  | -3.7% |
| vol_20d    | 11.0% |
| mdd_60d    |  8.9% |
| rsi_14     |  43.6 |
| zscore_20d |  -0.7 |

### Hang Seng / ^HSI (score 35.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.0% |
| ret_5d     | -1.5% |
| ret_20d    | -4.5% |
| ret_60d    | +0.3% |
| ma20_dist  | -1.8% |
| ma50_dist  | -3.8% |
| vol_20d    | 13.8% |
| mdd_60d    |  7.8% |
| rsi_14     |  42.3 |
| zscore_20d |  -1.3 |

### Brent Crude Oil / BZ=F (score 32.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.3% |
| ret_5d     |  -2.0% |
| ret_20d    |  +2.7% |
| ret_60d    | +14.2% |
| ma20_dist  |  -3.0% |
| ma50_dist  |  +5.5% |
| vol_20d    |  41.1% |
| mdd_60d    |  21.2% |
| rsi_14     |   39.2 |
| zscore_20d |   -1.2 |

### UnitedHealth Group Inc. / UNH (score 29.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.6% |
| ret_5d     |  +0.4% |
| ret_20d    |  -5.5% |
| ret_60d    | -12.3% |
| ma20_dist  |  +0.0% |
| ma50_dist  |  -3.8% |
| vol_20d    |  20.1% |
| mdd_60d    |  16.3% |
| rsi_14     |   51.2 |
| zscore_20d |    0.0 |

### Gold / GC=F (score 29.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | +0.2% |
| ret_20d    | -5.7% |
| ret_60d    | +4.3% |
| ma20_dist  | -2.8% |
| ma50_dist  | -4.7% |
| vol_20d    | 16.4% |
| mdd_60d    | 11.7% |
| rsi_14     |  27.7 |
| zscore_20d |  -1.2 |

### Silver / SI=F (score 27.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | +0.8% |
| ret_20d    | -7.7% |
| ret_60d    | +9.2% |
| ma20_dist  | -3.6% |
| ma50_dist  | -5.4% |
| vol_20d    | 32.4% |
| mdd_60d    | 13.7% |
| rsi_14     |  38.1 |
| zscore_20d |  -1.0 |

### JPMorgan Chase & Co. / JPM (score 22.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | -0.6% |
| ret_20d    | -5.8% |
| ret_60d    | -1.0% |
| ma20_dist  | -2.9% |
| ma50_dist  | -5.5% |
| vol_20d    | 17.4% |
| mdd_60d    |  9.9% |
| rsi_14     |  29.6 |
| zscore_20d |  -1.2 |

### CAC 40 / ^FCHI (score 22.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | -2.1% |
| ret_20d    | -5.4% |
| ret_60d    | -6.0% |
| ma20_dist  | -2.4% |
| ma50_dist  | -5.5% |
| vol_20d    | 12.9% |
| mdd_60d    | 10.2% |
| rsi_14     |  31.3 |
| zscore_20d |  -1.7 |

### Platinum / PL=F (score 17.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | +0.7% |
| ret_20d    | -8.4% |
| ret_60d    | +5.4% |
| ma20_dist  | -3.9% |
| ma50_dist  | -4.8% |
| vol_20d    | 34.0% |
| mdd_60d    | 12.2% |
| rsi_14     |  36.5 |
| zscore_20d |  -1.2 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Microsoft Corporation / MSFT        |  12.2114 |           2.3% |                 0.49x |       24.4229 |            4.6% |
| NASDAQ 100 / ^NDX                   | 389.9184 |           1.2% |                 0.67x |      779.8368 |            2.5% |
| NVIDIA Corporation / NVDA           |   5.3679 |           2.2% |                 0.43x |       10.7357 |            4.5% |
| S&P 500 / ^GSPC                     |  69.5800 |           0.9% |                 0.98x |      139.1599 |            1.8% |
| Amazon.com Inc. / AMZN              |   5.2757 |           2.1% |                 0.46x |       10.5514 |            4.1% |
| Soybeans / ZS=F                     |  21.8393 |           1.7% |                 0.49x |       43.6786 |            3.4% |
| Tesla Inc. / TSLA                   |  11.6729 |           3.1% |                 0.34x |       23.3457 |            6.1% |
| Apple Inc. / AAPL                   |   6.4179 |           1.9% |                 0.50x |       12.8357 |            3.8% |
| Meta Platforms Inc. / META          |  28.3921 |           3.8% |                 0.18x |       56.7842 |            7.7% |
| DAX / ^GDAXI                        | 311.2351 |           1.2% |                 0.77x |      622.4701 |            2.4% |
| Alphabet Inc. Class A / GOOGL       |   8.8643 |           2.5% |                 0.40x |       17.7286 |            5.1% |
| Dow Jones Industrial Average / ^DJI | 467.8909 |           0.9% |                 1.01x |      935.7818 |            1.8% |
| Corn / ZC=F                         |  11.2143 |           2.2% |                 0.36x |       22.4286 |            4.4% |
| Euro Stoxx 50 / ^STOXX50E           |  74.8750 |           1.2% |                 0.75x |      149.7499 |            2.4% |
| Wheat / ZW=F                        |  16.9821 |           2.4% |                 0.40x |       33.9643 |            4.8% |
| FTSE 100 / ^FTSE                    | 110.1569 |           1.0% |                 0.89x |      220.3139 |            2.1% |
| Russell 2000 / ^RUT                 |  34.4507 |           1.2% |                 0.91x |       68.9014 |            2.4% |
| Hang Seng / ^HSI                    | 309.1023 |           1.3% |                 0.73x |      618.2045 |            2.5% |
| Brent Crude Oil / BZ=F              |   4.7250 |           4.7% |                 0.24x |        9.4500 |            9.4% |
| UnitedHealth Group Inc. / UNH       |   7.5443 |           2.0% |                 0.50x |       15.0886 |            4.0% |
| Gold / GC=F                         |  84.2214 |           2.0% |                 0.61x |      168.4427 |            4.0% |
| Silver / SI=F                       |   1.2347 |           2.0% |                 0.31x |        2.4694 |            4.0% |
| JPMorgan Chase & Co. / JPM          |   5.8491 |           1.8% |                 0.58x |       11.6981 |            3.5% |
| CAC 40 / ^FCHI                      |  93.2778 |           1.2% |                 0.78x |      186.5557 |            2.4% |
| Platinum / PL=F                     |  30.7572 |           1.8% |                 0.29x |       61.5143 |            3.6% |

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

Scoring engine version: **1.0.0** | Git commit: **29d1ebc**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
