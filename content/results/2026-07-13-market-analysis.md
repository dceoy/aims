+++
title = "Market Analysis 2026-07-13"
date = "2026-07-13T00:00:00+00:00"
draft = false
summary = "Neutral market: 26 reliable instruments. Top signal: ZS=F (score 78.5)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-07-13.json", "data/history/2026-07-13.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "c7c1bf5"
+++

## Market Regime

**Neutral** — 15 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Soybeans / ZS=F** — score 78.5, 20d return +6.5%, RSI14=71. 20d up +6.5%; above MA20 by 5.1%; RSI14=71
- **Wheat / ZW=F** — score 77.3, 20d return +7.6%, RSI14=60. 20d up +7.6%; above MA20 by 6.2%; RSI14=60
- **JPMorgan Chase & Co. / JPM** — score 73.6, 20d return +9.3%, RSI14=63. 20d up +9.3%; above MA20 by 2.1%; RSI14=63 ⚠️ Upcoming: JPM earnings release (2026-07-14)
- **Meta Platforms Inc. / META** — score 73.6, 20d return +17.3%, RSI14=69. 20d up +17.3%; above MA20 by 14.5%; RSI14=69
- **Dow Jones Industrial Average / ^DJI** — score 72.4, 20d return +5.4%, RSI14=70. 20d up +5.4%; above MA20 by 1.1%; RSI14=70

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                | Applies To |
| ---------- | -------------------- | ---------- |
| 2026-07-14 | JPM earnings release | JPM        |
| 2026-07-16 | UNH earnings release | UNH        |

## Signal History

Compared with the previous available report (**2026-07-12**).
- **New top-5:** ^DJI
- **Persistent top signals:** ZS=F (7 reports), JPM (4 reports), META (3 reports), ZW=F (3 reports)
- **Dropped from top-5:** ZC=F

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +1 |    +0.0 |
| 7203.T    |     +0 |    +0.6 |
| 8306.T    |     +0 |    +1.2 |
| AAPL      |     +1 |    +1.5 |
| AMZN      |     +0 |    +0.0 |
| BZ=F      |     +1 |    +1.2 |
| CL=F      |     +0 |    +0.9 |
| GC=F      |     +0 |    -1.5 |
| GOOGL     |     +1 |    +0.9 |
| HG=F      |     -1 |    -5.8 |
| JPM       |     +1 |    +1.2 |
| META      |     +1 |    +1.2 |
| MSFT      |     -1 |    +0.0 |
| NG=F      |     +1 |    +0.0 |
| NVDA      |     +1 |    +2.1 |
| PL=F      |     -2 |    -4.2 |
| SI=F      |     +0 |    -1.8 |
| TSLA      |     +0 |    +1.2 |
| UNH       |     +1 |    +0.9 |
| XOM       |     +0 |    -0.3 |
| ZC=F      |     -8 |   -13.9 |
| ZS=F      |     +2 |    +4.5 |
| ZW=F      |     -1 |    +0.0 |
| ^DJI      |     +1 |    +1.2 |
| ^FCHI     |     +0 |    +1.8 |
| ^FTSE     |     +0 |    +1.2 |
| ^GDAXI    |     +0 |    +0.6 |
| ^GSPC     |     +1 |    +1.2 |
| ^HSI      |     +0 |    +0.9 |
| ^N225     |     +0 |    +0.3 |
| ^NDX      |     +0 |    +1.5 |
| ^RUT      |     +0 |    +0.9 |
| ^STOXX50E |     +0 |    +0.3 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|    1 | Soybeans / ZS=F        |  78.5 |   Yes    | —               | 20d up +6.5%; above MA20 by 5.1%; RSI14=71    |
|    2 | Wheat / ZW=F           |  77.3 |   Yes    | —               | 20d up +7.6%; above MA20 by 6.2%; RSI14=60    |
|   10 | Corn / ZC=F            |  62.1 |   Yes    | —               | 20d up +4.5%; above MA20 by 4.4%; RSI14=61    |
|   22 | Gold / GC=F            |  25.1 |   Yes    | —               | 20d down -0.1%; below MA20 by 0.9%; RSI14=41  |
|   23 | Brent Crude Oil / BZ=F |  20.3 |   Yes    | —               | 20d down -18.4%; below MA20 by 1.4%; RSI14=41 |
|   24 | Natural Gas / NG=F     |  18.8 |   Yes    | —               | 20d down -7.7%; below MA20 by 7.7%; RSI14=36  |
|   25 | Platinum / PL=F        |  17.6 |   Yes    | —               | 20d down -4.1%; below MA20 by 2.0%; RSI14=41  |
|   26 | Silver / SI=F          |   7.9 |   Yes    | —               | 20d down -7.4%; below MA20 by 4.4%; RSI14=34  |
|   29 | Copper / HG=F          |  45.8 |    No    | malformed_input | Suppressed: malformed_input                   |
|   33 | WTI Crude Oil / CL=F   |  15.2 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    3 | JPMorgan Chase & Co. / JPM                                                     |  73.6 |   Yes    | —                             | 20d up +9.3%; above MA20 by 2.1%; RSI14=63   |
|    4 | Meta Platforms Inc. / META                                                     |  73.6 |   Yes    | —                             | 20d up +17.3%; above MA20 by 14.5%; RSI14=69 |
|    7 | Apple Inc. / AAPL                                                              |  69.7 |   Yes    | —                             | 20d up +8.1%; above MA20 by 5.8%; RSI14=62   |
|    8 | UnitedHealth Group Inc. / UNH                                                  |  67.0 |   Yes    | —                             | 20d up +4.8%; above MA20 by 2.2%; RSI14=63   |
|    9 | NVIDIA Corporation / NVDA                                                      |  62.7 |   Yes    | —                             | 20d up +5.3%; above MA20 by 4.5%; RSI14=50   |
|   12 | Tesla Inc. / TSLA                                                              |  54.2 |   Yes    | —                             | 20d up +6.9%; above MA20 by 1.7%; RSI14=52   |
|   18 | Amazon.com Inc. / AMZN                                                         |  42.4 |   Yes    | —                             | 20d up +3.1%; above MA20 by 2.1%; RSI14=51   |
|   20 | Alphabet Inc. Class A / GOOGL                                                  |  33.3 |   Yes    | —                             | 20d up +0.2%; below MA20 by 0.2%; RSI14=43   |
|   21 | Microsoft Corporation / MSFT                                                   |  32.7 |   Yes    | —                             | 20d down -3.1%; above MA20 by 1.2%; RSI14=53 |
|   27 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  83.9 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   28 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  46.1 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   31 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  39.7 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   32 | Exxon Mobil Corporation / XOM                                                  |  36.4 |    No    | malformed_input               | Suppressed: malformed_input                  |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    5 | Dow Jones Industrial Average / ^DJI |  72.4 |   Yes    | —            | 20d up +5.4%; above MA20 by 1.1%; RSI14=70   |
|    6 | S&P 500 / ^GSPC                     |  70.9 |   Yes    | —            | 20d up +4.2%; above MA20 by 1.5%; RSI14=57   |
|   11 | NASDAQ 100 / ^NDX                   |  57.0 |   Yes    | —            | 20d up +4.6%; above MA20 by 0.4%; RSI14=45   |
|   13 | Russell 2000 / ^RUT                 |  53.9 |   Yes    | —            | 20d up +5.0%; below MA20 by 0.1%; RSI14=50   |
|   14 | Hang Seng / ^HSI                    |  52.7 |   Yes    | —            | 20d down -1.0%; above MA20 by 1.9%; RSI14=53 |
|   15 | FTSE 100 / ^FTSE                    |  50.3 |   Yes    | —            | 20d up +0.2%; below MA20 by 0.1%; RSI14=55   |
|   16 | DAX / ^GDAXI                        |  48.2 |   Yes    | —            | 20d up +1.8%; below MA20 by 0.0%; RSI14=49   |
|   17 | Euro Stoxx 50 / ^STOXX50E           |  45.8 |   Yes    | —            | 20d up +1.3%; below MA20 by 0.3%; RSI14=47   |
|   19 | CAC 40 / ^FCHI                      |  40.6 |   Yes    | —            | 20d down -0.1%; below MA20 by 0.7%; RSI14=46 |
|   30 | Nikkei 225 / ^N225                  |  44.2 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-07-10 |
| 7203.T    | 2026-07-10 |
| 8306.T    | 2026-07-10 |
| AAPL      | 2026-07-10 |
| AMZN      | 2026-07-10 |
| BZ=F      | 2026-07-10 |
| CL=F      | 2026-07-10 |
| GC=F      | 2026-07-10 |
| GOOGL     | 2026-07-10 |
| HG=F      | 2026-07-10 |
| JPM       | 2026-07-10 |
| META      | 2026-07-10 |
| MSFT      | 2026-07-10 |
| NG=F      | 2026-07-10 |
| NVDA      | 2026-07-10 |
| PL=F      | 2026-07-10 |
| SI=F      | 2026-07-10 |
| TSLA      | 2026-07-10 |
| UNH       | 2026-07-10 |
| XOM       | 2026-07-10 |
| ZC=F      | 2026-07-10 |
| ZS=F      | 2026-07-10 |
| ZW=F      | 2026-07-10 |
| ^DJI      | 2026-07-10 |
| ^FCHI     | 2026-07-10 |
| ^FTSE     | 2026-07-10 |
| ^GDAXI    | 2026-07-10 |
| ^GSPC     | 2026-07-10 |
| ^HSI      | 2026-07-10 |
| ^N225     | 2026-07-10 |
| ^NDX      | 2026-07-10 |
| ^RUT      | 2026-07-10 |
| ^STOXX50E | 2026-07-10 |

## Symbol Details

### Soybeans / ZS=F (score 78.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.4% |
| ret_5d     | +5.7% |
| ret_20d    | +6.5% |
| ret_60d    | +3.3% |
| ma20_dist  | +5.1% |
| ma50_dist  | +2.9% |
| vol_20d    | 20.4% |
| mdd_60d    |  8.8% |
| rsi_14     |  71.0 |
| zscore_20d |   1.9 |

### Wheat / ZW=F (score 77.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +3.4% |
| ret_5d     | +7.0% |
| ret_20d    | +7.6% |
| ret_60d    | +6.8% |
| ma20_dist  | +6.2% |
| ma50_dist  | +3.3% |
| vol_20d    | 26.1% |
| mdd_60d    | 14.6% |
| rsi_14     |  60.0 |
| zscore_20d |   2.6 |

### JPMorgan Chase & Co. / JPM (score 73.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +1.1% |
| ret_20d    | +9.3% |
| ret_60d    | +8.6% |
| ma20_dist  | +2.1% |
| ma50_dist  | +7.2% |
| vol_20d    | 24.3% |
| mdd_60d    |  6.7% |
| rsi_14     |  63.4 |
| zscore_20d |   1.0 |

### Meta Platforms Inc. / META (score 73.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +6.0% |
| ret_5d     | +14.8% |
| ret_20d    | +17.3% |
| ret_60d    |  +1.1% |
| ma20_dist  | +14.5% |
| ma50_dist  | +11.5% |
| vol_20d    |  55.1% |
| mdd_60d    |  21.1% |
| rsi_14     |   68.7 |
| zscore_20d |    2.8 |

### Dow Jones Industrial Average / ^DJI (score 72.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | -0.5% |
| ret_20d    | +5.4% |
| ret_60d    | +8.4% |
| ma20_dist  | +1.1% |
| ma50_dist  | +3.4% |
| vol_20d    | 10.1% |
| mdd_60d    |  3.2% |
| rsi_14     |  69.9 |
| zscore_20d |   1.0 |

### S&P 500 / ^GSPC (score 70.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | +1.2% |
| ret_20d    | +4.2% |
| ret_60d    | +8.7% |
| ma20_dist  | +1.5% |
| ma50_dist  | +1.9% |
| vol_20d    | 13.3% |
| mdd_60d    |  4.5% |
| rsi_14     |  57.3 |
| zscore_20d |   1.6 |

### Apple Inc. / AAPL (score 69.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.3% |
| ret_5d     |  +2.2% |
| ret_20d    |  +8.1% |
| ret_60d    | +21.9% |
| ma20_dist  |  +5.8% |
| ma50_dist  |  +5.9% |
| vol_20d    |  34.3% |
| mdd_60d    |  12.7% |
| rsi_14     |   61.9 |
| zscore_20d |    1.5 |

### UnitedHealth Group Inc. / UNH (score 67.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.6% |
| ret_5d     |  -0.2% |
| ret_20d    |  +4.8% |
| ret_60d    | +35.9% |
| ma20_dist  |  +2.2% |
| ma50_dist  |  +7.2% |
| vol_20d    |  24.9% |
| mdd_60d    |   6.1% |
| rsi_14     |   62.9 |
| zscore_20d |    0.9 |

### NVIDIA Corporation / NVDA (score 62.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +4.0% |
| ret_5d     | +8.3% |
| ret_20d    | +5.3% |
| ret_60d    | +7.4% |
| ma20_dist  | +4.5% |
| ma50_dist  | +0.8% |
| vol_20d    | 35.2% |
| mdd_60d    | 18.3% |
| rsi_14     |  50.3 |
| zscore_20d |   1.5 |

### Corn / ZC=F (score 62.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.4% |
| ret_5d     | +3.1% |
| ret_20d    | +4.5% |
| ret_60d    | -1.1% |
| ma20_dist  | +4.4% |
| ma50_dist  | -0.3% |
| vol_20d    | 26.8% |
| mdd_60d    | 15.7% |
| rsi_14     |  60.6 |
| zscore_20d |   1.6 |

### NASDAQ 100 / ^NDX (score 57.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.3% |
| ret_5d     |  +1.7% |
| ret_20d    |  +4.6% |
| ret_60d    | +15.4% |
| ma20_dist  |  +0.4% |
| ma50_dist  |  +1.5% |
| vol_20d    |  28.3% |
| mdd_60d    |   7.0% |
| rsi_14     |   44.6 |
| zscore_20d |    0.3 |

### Tesla Inc. / TSLA (score 54.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.3% |
| ret_5d     |  +3.6% |
| ret_20d    |  +6.9% |
| ret_60d    | +12.0% |
| ma20_dist  |  +1.7% |
| ma50_dist  |  -0.4% |
| vol_20d    |  59.2% |
| mdd_60d    |  15.8% |
| rsi_14     |   52.0 |
| zscore_20d |    0.5 |

### Russell 2000 / ^RUT (score 53.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.5% |
| ret_5d     |  -0.6% |
| ret_20d    |  +5.0% |
| ret_60d    | +10.1% |
| ma20_dist  |  -0.1% |
| ma50_dist  |  +2.5% |
| vol_20d    |  16.3% |
| mdd_60d    |   4.8% |
| rsi_14     |   49.6 |
| zscore_20d |   -0.1 |

### Hang Seng / ^HSI (score 52.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | +3.5% |
| ret_20d    | -1.0% |
| ret_60d    | -5.8% |
| ma20_dist  | +1.9% |
| ma50_dist  | -2.9% |
| vol_20d    | 20.9% |
| mdd_60d    | 14.9% |
| rsi_14     |  53.3 |
| zscore_20d |   0.7 |

### FTSE 100 / ^FTSE (score 50.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | -1.7% |
| ret_20d    | +0.2% |
| ret_60d    | -0.6% |
| ma20_dist  | -0.1% |
| ma50_dist  | +0.8% |
| vol_20d    | 10.5% |
| mdd_60d    |  4.4% |
| rsi_14     |  54.6 |
| zscore_20d |  -0.1 |

### DAX / ^GDAXI (score 48.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | -2.8% |
| ret_20d    | +1.8% |
| ret_60d    | +3.8% |
| ma20_dist  | -0.0% |
| ma50_dist  | +1.0% |
| vol_20d    | 16.2% |
| mdd_60d    |  4.7% |
| rsi_14     |  48.9 |
| zscore_20d |  -0.0 |

### Euro Stoxx 50 / ^STOXX50E (score 45.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | -2.2% |
| ret_20d    | +1.3% |
| ret_60d    | +4.8% |
| ma20_dist  | -0.3% |
| ma50_dist  | +2.8% |
| vol_20d    | 14.3% |
| mdd_60d    |  4.9% |
| rsi_14     |  47.3 |
| zscore_20d |  -0.3 |

### Amazon.com Inc. / AMZN (score 42.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | +1.1% |
| ret_20d    | +3.1% |
| ret_60d    | -1.5% |
| ma20_dist  | +2.1% |
| ma50_dist  | -3.4% |
| vol_20d    | 33.5% |
| mdd_60d    | 17.4% |
| rsi_14     |  50.9 |
| zscore_20d |   0.9 |

### CAC 40 / ^FCHI (score 40.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | -2.0% |
| ret_20d    | -0.1% |
| ret_60d    | +0.9% |
| ma20_dist  | -0.7% |
| ma50_dist  | +1.2% |
| vol_20d    | 12.5% |
| mdd_60d    |  5.6% |
| rsi_14     |  46.3 |
| zscore_20d |  -1.0 |

### Alphabet Inc. Class A / GOOGL (score 33.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | -0.8% |
| ret_20d    | +0.2% |
| ret_60d    | +7.4% |
| ma20_dist  | -0.2% |
| ma50_dist  | -4.1% |
| vol_20d    | 31.3% |
| mdd_60d    | 16.2% |
| rsi_14     |  42.5 |
| zscore_20d |  -0.1 |

### Microsoft Corporation / MSFT (score 32.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | -1.4% |
| ret_20d    | -3.1% |
| ret_60d    | -1.8% |
| ma20_dist  | +1.2% |
| ma50_dist  | -4.5% |
| vol_20d    | 36.5% |
| mdd_60d    | 23.4% |
| rsi_14     |  52.9 |
| zscore_20d |   0.4 |

### Gold / GC=F (score 25.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.6% |
| ret_5d     |  -0.2% |
| ret_20d    |  -0.1% |
| ret_60d    | -14.9% |
| ma20_dist  |  -0.9% |
| ma50_dist  |  -6.2% |
| vol_20d    |  26.2% |
| mdd_60d    |  17.9% |
| rsi_14     |   41.2 |
| zscore_20d |   -0.3 |

### Brent Crude Oil / BZ=F (score 20.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.4% |
| ret_5d     |  +5.9% |
| ret_20d    | -18.4% |
| ret_60d    | -19.8% |
| ma20_dist  |  -1.4% |
| ma50_dist  | -17.6% |
| vol_20d    |  43.0% |
| mdd_60d    |  39.4% |
| rsi_14     |   41.3 |
| zscore_20d |   -0.2 |

### Natural Gas / NG=F (score 18.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.4% |
| ret_5d     |  -8.0% |
| ret_20d    |  -7.7% |
| ret_60d    | +13.1% |
| ma20_dist  |  -7.7% |
| ma50_dist  |  -4.2% |
| vol_20d    |  42.0% |
| mdd_60d    |  12.1% |
| rsi_14     |   36.1 |
| zscore_20d |   -2.7 |

### Platinum / PL=F (score 17.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.0% |
| ret_5d     |  +0.1% |
| ret_20d    |  -4.1% |
| ret_60d    | -22.4% |
| ma20_dist  |  -2.0% |
| ma50_dist  | -11.5% |
| vol_20d    |  41.8% |
| mdd_60d    |  29.1% |
| rsi_14     |   40.8 |
| zscore_20d |   -0.5 |

### Silver / SI=F (score 7.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.9% |
| ret_5d     |  -1.4% |
| ret_20d    |  -7.4% |
| ret_60d    | -24.7% |
| ma20_dist  |  -4.4% |
| ma50_dist  | -15.1% |
| vol_20d    |  52.1% |
| mdd_60d    |  34.7% |
| rsi_14     |   34.4 |
| zscore_20d |   -0.7 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Soybeans / ZS=F                     |  19.8036 |           1.7% |                 0.49x |       39.6071 |            3.3% |
| Wheat / ZW=F                        |  14.5536 |           2.3% |                 0.38x |       29.1071 |            4.6% |
| JPMorgan Chase & Co. / JPM          |   6.8949 |           2.0% |                 0.41x |       13.7898 |            4.1% |
| Meta Platforms Inc. / META          |  26.8379 |           4.0% |                 0.18x |       53.6757 |            8.0% |
| Dow Jones Industrial Average / ^DJI | 536.5131 |           1.0% |                 0.99x |     1073.0262 |            2.0% |
| S&P 500 / ^GSPC                     |  84.1201 |           1.1% |                 0.75x |      168.2402 |            2.2% |
| Apple Inc. / AAPL                   |   8.9464 |           2.8% |                 0.29x |       17.8929 |            5.7% |
| UnitedHealth Group Inc. / UNH       |  10.4671 |           2.5% |                 0.40x |       20.9343 |            4.9% |
| NVIDIA Corporation / NVDA           |   6.8021 |           3.2% |                 0.28x |       13.6043 |            6.4% |
| Corn / ZC=F                         |   9.7857 |           2.2% |                 0.37x |       19.5714 |            4.5% |
| NASDAQ 100 / ^NDX                   | 639.3541 |           2.1% |                 0.35x |     1278.7081 |            4.3% |
| Tesla Inc. / TSLA                   |  20.1736 |           4.9% |                 0.17x |       40.3471 |            9.9% |
| Russell 2000 / ^RUT                 |  42.9143 |           1.4% |                 0.61x |       85.8286 |            2.9% |
| Hang Seng / ^HSI                    | 485.1609 |           2.0% |                 0.48x |      970.3217 |            4.0% |
| FTSE 100 / ^FTSE                    | 120.9214 |           1.2% |                 0.96x |      241.8428 |            2.3% |
| DAX / ^GDAXI                        | 352.3563 |           1.4% |                 0.62x |      704.7126 |            2.8% |
| Euro Stoxx 50 / ^STOXX50E           |  78.0420 |           1.2% |                 0.70x |      156.0840 |            2.5% |
| Amazon.com Inc. / AMZN              |   8.0521 |           3.3% |                 0.30x |       16.1043 |            6.6% |
| CAC 40 / ^FCHI                      |  92.6143 |           1.1% |                 0.80x |      185.2285 |            2.2% |
| Alphabet Inc. Class A / GOOGL       |  11.4821 |           3.2% |                 0.32x |       22.9643 |            6.4% |
| Microsoft Corporation / MSFT        |  12.6793 |           3.3% |                 0.27x |       25.3586 |            6.6% |
| Gold / GC=F                         |  81.0571 |           2.0% |                 0.38x |      162.1143 |            4.0% |
| Brent Crude Oil / BZ=F              |   3.1614 |           4.2% |                 0.23x |        6.3229 |            8.3% |
| Natural Gas / NG=F                  |   0.1426 |           4.9% |                 0.24x |        0.2853 |            9.7% |
| Platinum / PL=F                     |  40.0571 |           2.5% |                 0.24x |       80.1143 |            5.0% |
| Silver / SI=F                       |   2.1715 |           3.6% |                 0.19x |        4.3430 |            7.3% |

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

Scoring engine version: **1.0.0** | Git commit: **c7c1bf5**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
