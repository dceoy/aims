+++
title = "Market Analysis 2026-10-08"
date = "2026-10-08T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: MSFT (score 86.4)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-10-08.json", "data/history/2026-10-08.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "0980a4c"
+++

## Market Regime

**Neutral** — 10 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Microsoft Corporation / MSFT** — score 86.4, 20d return +7.8%, RSI14=74. 20d up +7.8%; above MA20 by 4.6%; RSI14=74
- **NASDAQ 100 / ^NDX** — score 77.6, 20d return +5.9%, RSI14=78. 20d up +5.9%; above MA20 by 3.3%; RSI14=78
- **S&P 500 / ^GSPC** — score 76.1, 20d return +2.2%, RSI14=66. 20d up +2.2%; above MA20 by 1.5%; RSI14=66
- **NVIDIA Corporation / NVDA** — score 74.5, 20d return +6.3%, RSI14=77. 20d up +6.3%; above MA20 by 5.3%; RSI14=77
- **Amazon.com Inc. / AMZN** — score 70.3, 20d return +3.0%, RSI14=62. 20d up +3.0%; above MA20 by 3.3%; RSI14=62

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                | Applies To |
| ---------- | -------------------- | ---------- |
| 2026-10-13 | JPM earnings release | JPM        |
| 2026-10-13 | UNH earnings release | UNH        |

## Signal History

Compared with the previous available report (**2026-10-07**).

- **New top-5:** None
- **Persistent top signals:** MSFT (9 reports), ^NDX (9 reports), ^GSPC (7 reports), NVDA (6 reports), AMZN (2 reports)
- **Dropped from top-5:** None

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +0 |    -6.4 |
| 7203.T    |     +0 |    -4.8 |
| 8306.T    |     -2 |   -18.5 |
| AAPL      |     +2 |   +12.7 |
| AMZN      |     +0 |    +7.9 |
| BZ=F      |     +3 |    +7.0 |
| CL=F      |     +0 |    -0.6 |
| GC=F      |     -1 |    -3.9 |
| GOOGL     |     +4 |   +11.2 |
| HG=F      |     +2 |    +6.7 |
| JPM       |     +4 |   +10.6 |
| META      |     -1 |    -2.7 |
| MSFT      |     +0 |    +1.5 |
| NG=F      |     +1 |    +8.8 |
| NVDA      |     -1 |    -0.3 |
| PL=F      |     +0 |    -8.5 |
| SI=F      |     -2 |    -7.3 |
| TSLA      |     -2 |    -3.0 |
| UNH       |     +8 |   +15.4 |
| XOM       |     +0 |    +5.2 |
| ZC=F      |     +0 |    -1.5 |
| ZS=F      |     -2 |    -0.9 |
| ZW=F      |     -5 |   -11.5 |
| ^DJI      |     +1 |    +4.8 |
| ^FCHI     |     +1 |    -2.1 |
| ^FTSE     |     +1 |    +0.6 |
| ^GDAXI    |     -4 |   -10.6 |
| ^GSPC     |     +1 |    +2.4 |
| ^HSI      |     +0 |    +1.2 |
| ^N225     |     -1 |    -3.9 |
| ^NDX      |     +0 |    +2.4 |
| ^RUT      |     -4 |    -3.0 |
| ^STOXX50E |     -3 |    -8.8 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Natural Gas / NG=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Copper / HG=F** — malformed_input
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **WTI Crude Oil / CL=F** — malformed_input

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|    8 | Soybeans / ZS=F        |  59.4 |   Yes    | —               | 20d up +0.2%; below MA20 by 0.5%; RSI14=42    |
|   13 | Corn / ZC=F            |  44.9 |   Yes    | —               | 20d down -1.1%; below MA20 by 3.3%; RSI14=33  |
|   16 | Brent Crude Oil / BZ=F |  39.7 |   Yes    | —               | 20d down -1.0%; below MA20 by 3.3%; RSI14=40  |
|   20 | Wheat / ZW=F           |  33.3 |   Yes    | —               | 20d down -3.5%; below MA20 by 2.7%; RSI14=34  |
|   22 | Gold / GC=F            |  25.4 |   Yes    | —               | 20d down -7.2%; below MA20 by 3.5%; RSI14=23  |
|   24 | Silver / SI=F          |  20.3 |   Yes    | —               | 20d down -11.8%; below MA20 by 4.9%; RSI14=29 |
|   25 | Platinum / PL=F        |   9.4 |   Yes    | —               | 20d down -14.7%; below MA20 by 6.5%; RSI14=30 |
|   26 | Natural Gas / NG=F     |  79.1 |    No    | malformed_input | Suppressed: malformed_input                   |
|   29 | Copper / HG=F          |  57.3 |    No    | malformed_input | Suppressed: malformed_input                   |
|   33 | WTI Crude Oil / CL=F   |  20.3 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    1 | Microsoft Corporation / MSFT                                                   |  86.4 |   Yes    | —                             | 20d up +7.8%; above MA20 by 4.6%; RSI14=74   |
|    4 | NVIDIA Corporation / NVDA                                                      |  74.5 |   Yes    | —                             | 20d up +6.3%; above MA20 by 5.3%; RSI14=77   |
|    5 | Amazon.com Inc. / AMZN                                                         |  70.3 |   Yes    | —                             | 20d up +3.0%; above MA20 by 3.3%; RSI14=62   |
|    6 | Apple Inc. / AAPL                                                              |  67.3 |   Yes    | —                             | 20d up +6.8%; above MA20 by 0.7%; RSI14=50   |
|    7 | Alphabet Inc. Class A / GOOGL                                                  |  59.7 |   Yes    | —                             | 20d up +6.0%; above MA20 by 1.7%; RSI14=53   |
|    9 | Tesla Inc. / TSLA                                                              |  56.1 |   Yes    | —                             | 20d up +2.7%; above MA20 by 2.9%; RSI14=58   |
|   10 | Meta Platforms Inc. / META                                                     |  51.8 |   Yes    | —                             | 20d up +10.4%; above MA20 by 1.4%; RSI14=57  |
|   12 | UnitedHealth Group Inc. / UNH                                                  |  45.1 |   Yes    | —                             | 20d down -3.8%; above MA20 by 0.1%; RSI14=51 |
|   19 | JPMorgan Chase & Co. / JPM                                                     |  33.3 |   Yes    | —                             | 20d down -6.6%; below MA20 by 3.1%; RSI14=28 |
|   28 | Exxon Mobil Corporation / XOM                                                  |  67.3 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   30 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  51.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   31 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  43.0 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   32 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  35.1 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    2 | NASDAQ 100 / ^NDX                   |  77.6 |   Yes    | —            | 20d up +5.9%; above MA20 by 3.3%; RSI14=78   |
|    3 | S&P 500 / ^GSPC                     |  76.1 |   Yes    | —            | 20d up +2.2%; above MA20 by 1.5%; RSI14=66   |
|   11 | Dow Jones Industrial Average / ^DJI |  51.8 |   Yes    | —            | 20d down -2.3%; below MA20 by 0.9%; RSI14=41 |
|   14 | DAX / ^GDAXI                        |  43.0 |   Yes    | —            | 20d down -1.8%; below MA20 by 1.1%; RSI14=38 |
|   15 | FTSE 100 / ^FTSE                    |  41.8 |   Yes    | —            | 20d down -2.0%; below MA20 by 1.6%; RSI14=27 |
|   17 | Euro Stoxx 50 / ^STOXX50E           |  37.3 |   Yes    | —            | 20d down -2.1%; below MA20 by 1.5%; RSI14=38 |
|   18 | Hang Seng / ^HSI                    |  36.4 |   Yes    | —            | 20d down -4.7%; below MA20 by 2.1%; RSI14=39 |
|   21 | Russell 2000 / ^RUT                 |  32.4 |   Yes    | —            | 20d down -4.4%; below MA20 by 1.9%; RSI14=33 |
|   23 | CAC 40 / ^FCHI                      |  20.6 |   Yes    | —            | 20d down -4.8%; below MA20 by 3.3%; RSI14=23 |
|   27 | Nikkei 225 / ^N225                  |  72.7 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-10-07 |
| 7203.T    | 2026-10-07 |
| 8306.T    | 2026-10-07 |
| AAPL      | 2026-10-07 |
| AMZN      | 2026-10-07 |
| BZ=F      | 2026-10-07 |
| CL=F      | 2026-10-07 |
| GC=F      | 2026-10-07 |
| GOOGL     | 2026-10-07 |
| HG=F      | 2026-10-07 |
| JPM       | 2026-10-07 |
| META      | 2026-10-07 |
| MSFT      | 2026-10-07 |
| NG=F      | 2026-10-07 |
| NVDA      | 2026-10-07 |
| PL=F      | 2026-10-07 |
| SI=F      | 2026-10-07 |
| TSLA      | 2026-10-07 |
| UNH       | 2026-10-07 |
| XOM       | 2026-10-07 |
| ZC=F      | 2026-10-07 |
| ZS=F      | 2026-10-07 |
| ZW=F      | 2026-10-07 |
| ^DJI      | 2026-10-07 |
| ^FCHI     | 2026-10-07 |
| ^FTSE     | 2026-10-07 |
| ^GDAXI    | 2026-10-07 |
| ^GSPC     | 2026-10-07 |
| ^HSI      | 2026-10-07 |
| ^N225     | 2026-10-07 |
| ^NDX      | 2026-10-07 |
| ^RUT      | 2026-10-07 |
| ^STOXX50E | 2026-10-07 |

## Symbol Details

### Microsoft Corporation / MSFT (score 86.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.1% |
| ret_5d     |  +3.3% |
| ret_20d    |  +7.8% |
| ret_60d    | +37.6% |
| ma20_dist  |  +4.6% |
| ma50_dist  |  +6.8% |
| vol_20d    |  20.1% |
| mdd_60d    |   5.1% |
| rsi_14     |   73.8 |
| zscore_20d |    1.9 |

### NASDAQ 100 / ^NDX (score 77.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | +2.5% |
| ret_20d    | +5.9% |
| ret_60d    | +5.3% |
| ma20_dist  | +3.3% |
| ma50_dist  | +5.1% |
| vol_20d    | 15.0% |
| mdd_60d    |  7.8% |
| rsi_14     |  78.3 |
| zscore_20d |   1.4 |

### S&P 500 / ^GSPC (score 76.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | +2.0% |
| ret_20d    | +2.2% |
| ret_60d    | +3.4% |
| ma20_dist  | +1.5% |
| ma50_dist  | +1.6% |
| vol_20d    | 10.0% |
| mdd_60d    |  3.4% |
| rsi_14     |  66.3 |
| zscore_20d |   1.6 |

### NVIDIA Corporation / NVDA (score 74.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.7% |
| ret_5d     |  +4.0% |
| ret_20d    |  +6.3% |
| ret_60d    | +12.1% |
| ma20_dist  |  +5.3% |
| ma50_dist  |  +7.7% |
| vol_20d    |  23.4% |
| mdd_60d    |  10.6% |
| rsi_14     |   77.0 |
| zscore_20d |    1.5 |

### Amazon.com Inc. / AMZN (score 70.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.4% |
| ret_5d     | +4.3% |
| ret_20d    | +3.0% |
| ret_60d    | +5.0% |
| ma20_dist  | +3.3% |
| ma50_dist  | +0.7% |
| vol_20d    | 21.5% |
| mdd_60d    | 13.4% |
| rsi_14     |  62.1 |
| zscore_20d |   2.1 |

### Apple Inc. / AAPL (score 67.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | +1.1% |
| ret_20d    | +6.8% |
| ret_60d    | +7.0% |
| ma20_dist  | +0.7% |
| ma50_dist  | +4.5% |
| vol_20d    | 19.9% |
| mdd_60d    | 11.0% |
| rsi_14     |  49.6 |
| zscore_20d |   0.6 |

### Alphabet Inc. Class A / GOOGL (score 59.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.8% |
| ret_5d     | +1.9% |
| ret_20d    | +6.0% |
| ret_60d    | -2.5% |
| ma20_dist  | +1.7% |
| ma50_dist  | +1.4% |
| vol_20d    | 23.6% |
| mdd_60d    | 14.4% |
| rsi_14     |  52.9 |
| zscore_20d |   1.2 |

### Soybeans / ZS=F (score 59.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | +0.3% |
| ret_20d    | +0.2% |
| ret_60d    | +7.7% |
| ma20_dist  | -0.5% |
| ma50_dist  | +3.5% |
| vol_20d    | 20.2% |
| mdd_60d    |  8.1% |
| rsi_14     |  42.2 |
| zscore_20d |  -0.4 |

### Tesla Inc. / TSLA (score 56.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | +6.5% |
| ret_20d    | +2.7% |
| ret_60d    | -4.6% |
| ma20_dist  | +2.9% |
| ma50_dist  | +7.4% |
| vol_20d    | 29.3% |
| mdd_60d    | 24.4% |
| rsi_14     |  57.5 |
| zscore_20d |   1.1 |

### Meta Platforms Inc. / META (score 51.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.4% |
| ret_5d     |  -0.5% |
| ret_20d    | +10.4% |
| ret_60d    |  +9.1% |
| ma20_dist  |  +1.4% |
| ma50_dist  | +13.9% |
| vol_20d    |  52.9% |
| mdd_60d    |  20.9% |
| rsi_14     |   57.2 |
| zscore_20d |    0.3 |

### Dow Jones Industrial Average / ^DJI (score 51.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | +0.5% |
| ret_20d    | -2.3% |
| ret_60d    | -2.5% |
| ma20_dist  | -0.9% |
| ma50_dist  | -2.8% |
| vol_20d    |  9.8% |
| mdd_60d    |  6.3% |
| rsi_14     |  41.5 |
| zscore_20d |  -1.0 |

### UnitedHealth Group Inc. / UNH (score 45.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.1% |
| ret_5d     |  +2.4% |
| ret_20d    |  -3.8% |
| ret_60d    | -11.6% |
| ma20_dist  |  +0.1% |
| ma50_dist  |  -3.6% |
| vol_20d    |  19.1% |
| mdd_60d    |  16.3% |
| rsi_14     |   50.9 |
| zscore_20d |    0.1 |

### Corn / ZC=F (score 44.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.2% |
| ret_5d     |  +0.2% |
| ret_20d    |  -1.1% |
| ret_60d    | +12.9% |
| ma20_dist  |  -3.3% |
| ma50_dist  |  +1.2% |
| vol_20d    |  27.8% |
| mdd_60d    |   8.4% |
| rsi_14     |   33.3 |
| zscore_20d |   -1.2 |

### DAX / ^GDAXI (score 43.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.4% |
| ret_5d     | -0.4% |
| ret_20d    | -1.8% |
| ret_60d    | +0.4% |
| ma20_dist  | -1.1% |
| ma50_dist  | -2.8% |
| vol_20d    | 12.6% |
| mdd_60d    |  6.1% |
| rsi_14     |  37.8 |
| zscore_20d |  -1.5 |

### FTSE 100 / ^FTSE (score 41.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | -1.4% |
| ret_20d    | -2.0% |
| ret_60d    | -0.7% |
| ma20_dist  | -1.6% |
| ma50_dist  | -2.7% |
| vol_20d    | 10.7% |
| mdd_60d    |  4.4% |
| rsi_14     |  26.9 |
| zscore_20d |  -1.7 |

### Brent Crude Oil / BZ=F (score 39.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.4% |
| ret_5d     |  -3.2% |
| ret_20d    |  -1.0% |
| ret_60d    | +12.3% |
| ma20_dist  |  -3.3% |
| ma50_dist  |  +4.8% |
| vol_20d    |  39.5% |
| mdd_60d    |  21.2% |
| rsi_14     |   40.2 |
| zscore_20d |   -1.3 |

### Euro Stoxx 50 / ^STOXX50E (score 37.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.5% |
| ret_5d     | -1.4% |
| ret_20d    | -2.1% |
| ret_60d    | -1.4% |
| ma20_dist  | -1.5% |
| ma50_dist  | -3.1% |
| vol_20d    | 13.2% |
| mdd_60d    |  5.7% |
| rsi_14     |  38.3 |
| zscore_20d |  -2.1 |

### Hang Seng / ^HSI (score 36.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | -1.6% |
| ret_20d    | -4.7% |
| ret_60d    | -0.9% |
| ma20_dist  | -2.1% |
| ma50_dist  | -4.3% |
| vol_20d    | 13.8% |
| mdd_60d    |  7.8% |
| rsi_14     |  38.8 |
| zscore_20d |  -1.6 |

### JPMorgan Chase & Co. / JPM (score 33.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | +0.1% |
| ret_20d    | -6.6% |
| ret_60d    | -3.9% |
| ma20_dist  | -3.1% |
| ma50_dist  | -5.9% |
| vol_20d    | 17.2% |
| mdd_60d    |  9.9% |
| rsi_14     |  27.6 |
| zscore_20d |  -1.2 |

### Wheat / ZW=F (score 33.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.5% |
| ret_5d     | +1.6% |
| ret_20d    | -3.5% |
| ret_60d    | +0.5% |
| ma20_dist  | -2.7% |
| ma50_dist  | -1.3% |
| vol_20d    | 25.0% |
| mdd_60d    | 11.9% |
| rsi_14     |  34.5 |
| zscore_20d |  -1.1 |

### Russell 2000 / ^RUT (score 32.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.3% |
| ret_5d     | -0.1% |
| ret_20d    | -4.4% |
| ret_60d    | -5.8% |
| ma20_dist  | -1.9% |
| ma50_dist  | -4.9% |
| vol_20d    | 11.0% |
| mdd_60d    |  9.0% |
| rsi_14     |  33.4 |
| zscore_20d |  -1.7 |

### Gold / GC=F (score 25.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.1% |
| ret_5d     | -1.1% |
| ret_20d    | -7.2% |
| ret_60d    | +3.3% |
| ma20_dist  | -3.5% |
| ma50_dist  | -5.8% |
| vol_20d    | 16.3% |
| mdd_60d    | 12.0% |
| rsi_14     |  23.3 |
| zscore_20d |  -1.5 |

### CAC 40 / ^FCHI (score 20.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.2% |
| ret_5d     | -2.5% |
| ret_20d    | -4.8% |
| ret_60d    | -7.3% |
| ma20_dist  | -3.3% |
| ma50_dist  | -6.5% |
| vol_20d    | 11.9% |
| mdd_60d    | 11.0% |
| rsi_14     |  23.4 |
| zscore_20d |  -2.1 |

### Silver / SI=F (score 20.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.1% |
| ret_5d     |  -0.3% |
| ret_20d    | -11.8% |
| ret_60d    |  +5.5% |
| ma20_dist  |  -4.9% |
| ma50_dist  |  -7.4% |
| vol_20d    |  31.2% |
| mdd_60d    |  13.8% |
| rsi_14     |   28.8 |
| zscore_20d |   -1.4 |

### Platinum / PL=F (score 9.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -3.5% |
| ret_5d     |  -4.1% |
| ret_20d    | -14.7% |
| ret_60d    |  +2.6% |
| ma20_dist  |  -6.5% |
| ma50_dist  |  -8.1% |
| vol_20d    |  32.3% |
| mdd_60d    |  14.7% |
| rsi_14     |   29.6 |
| zscore_20d |   -2.2 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Microsoft Corporation / MSFT        |  11.9164 |           2.2% |                 0.50x |       23.8329 |            4.5% |
| NASDAQ 100 / ^NDX                   | 373.4985 |           1.2% |                 0.67x |      746.9969 |            2.4% |
| S&P 500 / ^GSPC                     |  66.7614 |           0.9% |                 1.00x |      133.5229 |            1.7% |
| NVIDIA Corporation / NVDA           |   5.1429 |           2.2% |                 0.43x |       10.2857 |            4.3% |
| Amazon.com Inc. / AMZN              |   5.2900 |           2.0% |                 0.47x |       10.5800 |            4.1% |
| Apple Inc. / AAPL                   |   6.2557 |           1.9% |                 0.50x |       12.5114 |            3.7% |
| Alphabet Inc. Class A / GOOGL       |   8.9429 |           2.6% |                 0.42x |       17.8857 |            5.1% |
| Soybeans / ZS=F                     |  21.5893 |           1.7% |                 0.50x |       43.1786 |            3.3% |
| Tesla Inc. / TSLA                   |  11.0929 |           2.9% |                 0.34x |       22.1857 |            5.9% |
| Meta Platforms Inc. / META          |  28.5773 |           4.0% |                 0.19x |       57.1546 |            7.9% |
| Dow Jones Industrial Average / ^DJI | 477.1616 |           0.9% |                 1.02x |      954.3231 |            1.9% |
| UnitedHealth Group Inc. / UNH       |   7.9136 |           2.1% |                 0.52x |       15.8271 |            4.2% |
| Corn / ZC=F                         |  11.1786 |           2.2% |                 0.36x |       22.3571 |            4.5% |
| DAX / ^GDAXI                        | 321.7930 |           1.3% |                 0.79x |      643.5859 |            2.6% |
| FTSE 100 / ^FTSE                    | 107.4641 |           1.0% |                 0.93x |      214.9282 |            2.1% |
| Brent Crude Oil / BZ=F              |   4.6193 |           4.6% |                 0.25x |        9.2386 |            9.2% |
| Euro Stoxx 50 / ^STOXX50E           |  78.4264 |           1.3% |                 0.76x |      156.8527 |            2.5% |
| Hang Seng / ^HSI                    | 308.6730 |           1.3% |                 0.72x |      617.3460 |            2.6% |
| JPMorgan Chase & Co. / JPM          |   5.7084 |           1.7% |                 0.58x |       11.4168 |            3.5% |
| Wheat / ZW=F                        |  17.1786 |           2.5% |                 0.40x |       34.3571 |            5.0% |
| Russell 2000 / ^RUT                 |  34.4043 |           1.2% |                 0.91x |       68.8086 |            2.5% |
| Gold / GC=F                         |  82.6357 |           2.0% |                 0.61x |      165.2713 |            4.0% |
| CAC 40 / ^FCHI                      |  97.0235 |           1.2% |                 0.84x |      194.0471 |            2.5% |
| Silver / SI=F                       |   1.2673 |           2.1% |                 0.32x |        2.5346 |            4.2% |
| Platinum / PL=F                     |  34.4214 |           2.1% |                 0.31x |       68.8429 |            4.2% |

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

Scoring engine version: **1.0.0** | Git commit: **0980a4c**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
