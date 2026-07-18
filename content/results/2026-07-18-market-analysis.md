+++
title = "Market Analysis 2026-07-18"
date = "2026-07-18T00:00:00+00:00"
draft = false
summary = "Neutral market: 26 reliable instruments. Top signal: ZW=F (score 82.4)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-07-18.json", "data/history/2026-07-18.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "7a7bce5"
+++

## Market Regime

**Neutral** — 13 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Wheat / ZW=F** — score 82.4, 20d return +11.8%, RSI14=83. 20d up +11.8%; above MA20 by 12.0%; RSI14=83
- **Apple Inc. / AAPL** — score 78.2, 20d return +12.8%, RSI14=89. 20d up +12.8%; above MA20 by 9.2%; RSI14=89
- **Corn / ZC=F** — score 75.8, 20d return +11.2%, RSI14=72. 20d up +11.2%; above MA20 by 9.6%; RSI14=72
- **Soybeans / ZS=F** — score 68.5, 20d return +6.2%, RSI14=72. 20d up +6.2%; above MA20 by 3.8%; RSI14=72
- **JPMorgan Chase & Co. / JPM** — score 66.1, 20d return +2.8%, RSI14=63. 20d up +2.8%; above MA20 by 2.0%; RSI14=63

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                        | Applies To               |
| ---------- | ---------------------------- | ------------------------ |
| 2026-07-22 | GOOGL earnings release       | GOOGL                    |
| 2026-07-22 | TSLA earnings release        | TSLA                     |
| 2026-07-23 | ECB monetary policy decision | ^FCHI, ^GDAXI, ^STOXX50E |

## Signal History

Compared with the previous available report (**2026-07-17**).
- **New top-5:** ZC=F
- **Persistent top signals:** ZW=F (8 reports), AAPL (3 reports), JPM (3 reports), ZS=F (2 reports)
- **Dropped from top-5:** ^HSI

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +2 |    +9.1 |
| 7203.T    |     -1 |    -3.3 |
| 8306.T    |     -2 |   -18.2 |
| AAPL      |     -1 |    -4.2 |
| AMZN      |     +2 |    +1.2 |
| BZ=F      |     +6 |   +11.8 |
| CL=F      |     +2 |   +12.1 |
| GC=F      |     +2 |    +8.5 |
| GOOGL     |     -2 |    -1.8 |
| HG=F      |     -1 |    -2.1 |
| JPM       |     -1 |    +1.2 |
| META      |     -6 |   -10.3 |
| MSFT      |     -9 |   -12.7 |
| NG=F      |     +5 |   +13.9 |
| NVDA      |     -2 |    -7.6 |
| PL=F      |     -2 |    -8.8 |
| SI=F      |     +0 |    +6.1 |
| TSLA      |     -2 |    -6.1 |
| UNH       |     +4 |    +6.4 |
| XOM       |     +0 |    +4.5 |
| ZC=F      |    +10 |   +22.1 |
| ZS=F      |     +1 |    +5.5 |
| ZW=F      |     +1 |    +4.5 |
| ^DJI      |     -3 |    -4.5 |
| ^FCHI     |     +1 |    -2.1 |
| ^FTSE     |     +0 |    +5.2 |
| ^GDAXI    |     +2 |    +3.0 |
| ^GSPC     |     -3 |    -5.8 |
| ^HSI      |     -7 |   -12.1 |
| ^N225     |     +0 |    -7.9 |
| ^NDX      |     +1 |    -1.2 |
| ^RUT      |     +3 |    -1.2 |
| ^STOXX50E |     +0 |    -5.2 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **WTI Crude Oil / CL=F** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|    1 | Wheat / ZW=F           |  82.4 |   Yes    | —               | 20d up +11.8%; above MA20 by 12.0%; RSI14=83  |
|    3 | Corn / ZC=F            |  75.8 |   Yes    | —               | 20d up +11.2%; above MA20 by 9.6%; RSI14=72   |
|    4 | Soybeans / ZS=F        |  68.5 |   Yes    | —               | 20d up +6.2%; above MA20 by 3.8%; RSI14=72    |
|    8 | Brent Crude Oil / BZ=F |  61.8 |   Yes    | —               | 20d up +10.7%; above MA20 by 13.9%; RSI14=83  |
|   20 | Natural Gas / NG=F     |  31.2 |   Yes    | —               | 20d down -7.3%; below MA20 by 6.6%; RSI14=31  |
|   22 | Gold / GC=F            |  28.5 |   Yes    | —               | 20d down -7.7%; below MA20 by 1.4%; RSI14=46  |
|   24 | Platinum / PL=F        |  17.3 |   Yes    | —               | 20d down -10.5%; below MA20 by 1.0%; RSI14=46 |
|   26 | Silver / SI=F          |  11.8 |   Yes    | —               | 20d down -20.5%; below MA20 by 5.9%; RSI14=42 |
|   30 | WTI Crude Oil / CL=F   |  57.6 |    No    | malformed_input | Suppressed: malformed_input                   |
|   32 | Copper / HG=F          |  49.7 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    2 | Apple Inc. / AAPL                                                              |  78.2 |   Yes    | —                             | 20d up +12.8%; above MA20 by 9.2%; RSI14=89  |
|    5 | JPMorgan Chase & Co. / JPM                                                     |  66.1 |   Yes    | —                             | 20d up +2.8%; above MA20 by 2.0%; RSI14=63   |
|    6 | UnitedHealth Group Inc. / UNH                                                  |  63.6 |   Yes    | —                             | 20d up +6.6%; above MA20 by 1.4%; RSI14=49   |
|   15 | Amazon.com Inc. / AMZN                                                         |  47.0 |   Yes    | —                             | 20d up +4.1%; above MA20 by 2.1%; RSI14=67   |
|   17 | Meta Platforms Inc. / META                                                     |  46.1 |   Yes    | —                             | 20d up +13.8%; above MA20 by 6.7%; RSI14=67  |
|   18 | Microsoft Corporation / MSFT                                                   |  44.5 |   Yes    | —                             | 20d up +3.9%; above MA20 by 3.3%; RSI14=64   |
|   21 | NVIDIA Corporation / NVDA                                                      |  30.0 |   Yes    | —                             | 20d down -0.9%; above MA20 by 0.3%; RSI14=59 |
|   23 | Alphabet Inc. Class A / GOOGL                                                  |  25.1 |   Yes    | —                             | 20d down -4.7%; below MA20 by 2.6%; RSI14=55 |
|   25 | Tesla Inc. / TSLA                                                              |  15.8 |   Yes    | —                             | 20d down -3.9%; below MA20 by 4.3%; RSI14=50 |
|   27 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  68.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   28 | Exxon Mobil Corporation / XOM                                                  |  65.2 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   29 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  60.0 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   31 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  54.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    7 | FTSE 100 / ^FTSE                    |  63.6 |   Yes    | —            | 20d up +2.3%; above MA20 by 0.6%; RSI14=59   |
|    9 | Dow Jones Industrial Average / ^DJI |  56.4 |   Yes    | —            | 20d up +1.3%; below MA20 by 0.3%; RSI14=54   |
|   10 | Hang Seng / ^HSI                    |  55.1 |   Yes    | —            | 20d up +1.0%; above MA20 by 3.5%; RSI14=76   |
|   11 | S&P 500 / ^GSPC                     |  51.8 |   Yes    | —            | 20d up +0.5%; below MA20 by 0.3%; RSI14=59   |
|   12 | Euro Stoxx 50 / ^STOXX50E           |  49.1 |   Yes    | —            | 20d down -1.0%; below MA20 by 0.8%; RSI14=50 |
|   13 | Russell 2000 / ^RUT                 |  48.8 |   Yes    | —            | 20d up +1.5%; below MA20 by 0.9%; RSI14=39   |
|   14 | CAC 40 / ^FCHI                      |  47.9 |   Yes    | —            | 20d down -1.0%; below MA20 by 0.6%; RSI14=48 |
|   16 | DAX / ^GDAXI                        |  46.4 |   Yes    | —            | 20d down -0.6%; below MA20 by 1.0%; RSI14=54 |
|   19 | NASDAQ 100 / ^NDX                   |  31.5 |   Yes    | —            | 20d down -3.6%; below MA20 by 3.2%; RSI14=45 |
|   33 | Nikkei 225 / ^N225                  |  20.9 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-07-17 |
| 7203.T    | 2026-07-17 |
| 8306.T    | 2026-07-17 |
| AAPL      | 2026-07-17 |
| AMZN      | 2026-07-17 |
| BZ=F      | 2026-07-17 |
| CL=F      | 2026-07-17 |
| GC=F      | 2026-07-17 |
| GOOGL     | 2026-07-17 |
| HG=F      | 2026-07-17 |
| JPM       | 2026-07-17 |
| META      | 2026-07-17 |
| MSFT      | 2026-07-17 |
| NG=F      | 2026-07-17 |
| NVDA      | 2026-07-17 |
| PL=F      | 2026-07-17 |
| SI=F      | 2026-07-17 |
| TSLA      | 2026-07-17 |
| UNH       | 2026-07-17 |
| XOM       | 2026-07-17 |
| ZC=F      | 2026-07-17 |
| ZS=F      | 2026-07-17 |
| ZW=F      | 2026-07-17 |
| ^DJI      | 2026-07-17 |
| ^FCHI     | 2026-07-17 |
| ^FTSE     | 2026-07-17 |
| ^GDAXI    | 2026-07-17 |
| ^GSPC     | 2026-07-17 |
| ^HSI      | 2026-07-17 |
| ^N225     | 2026-07-17 |
| ^NDX      | 2026-07-17 |
| ^RUT      | 2026-07-17 |
| ^STOXX50E | 2026-07-17 |

## Symbol Details

### Wheat / ZW=F (score 82.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.5% |
| ret_5d     |  +8.3% |
| ret_20d    | +11.8% |
| ret_60d    | +13.2% |
| ma20_dist  | +12.0% |
| ma50_dist  | +11.4% |
| vol_20d    |  35.0% |
| mdd_60d    |  14.6% |
| rsi_14     |   82.9 |
| zscore_20d |    2.2 |

### Apple Inc. / AAPL (score 78.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.1% |
| ret_5d     |  +5.8% |
| ret_20d    | +12.8% |
| ret_60d    | +25.5% |
| ma20_dist  |  +9.2% |
| ma50_dist  | +10.3% |
| vol_20d    |  35.4% |
| mdd_60d    |  12.7% |
| rsi_14     |   88.6 |
| zscore_20d |    1.7 |

### Corn / ZC=F (score 75.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +6.1% |
| ret_5d     |  +6.9% |
| ret_20d    | +11.2% |
| ret_60d    |  +3.2% |
| ma20_dist  |  +9.6% |
| ma50_dist  |  +7.1% |
| vol_20d    |  34.5% |
| mdd_60d    |  15.7% |
| rsi_14     |   71.9 |
| zscore_20d |    2.5 |

### Soybeans / ZS=F (score 68.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | +0.5% |
| ret_20d    | +6.2% |
| ret_60d    | +2.4% |
| ma20_dist  | +3.8% |
| ma50_dist  | +3.4% |
| vol_20d    | 20.3% |
| mdd_60d    |  8.8% |
| rsi_14     |  72.5 |
| zscore_20d |   1.1 |

### JPMorgan Chase & Co. / JPM (score 66.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | +1.4% |
| ret_20d    | +2.8% |
| ret_60d    | +9.5% |
| ma20_dist  | +2.0% |
| ma50_dist  | +7.6% |
| vol_20d    | 22.1% |
| mdd_60d    |  6.1% |
| rsi_14     |  63.4 |
| zscore_20d |   1.1 |

### UnitedHealth Group Inc. / UNH (score 63.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.6% |
| ret_5d     |  +0.3% |
| ret_20d    |  +6.6% |
| ret_60d    | +23.8% |
| ma20_dist  |  +1.4% |
| ma50_dist  |  +6.1% |
| vol_20d    |  24.4% |
| mdd_60d    |   6.1% |
| rsi_14     |   48.9 |
| zscore_20d |    0.7 |

### FTSE 100 / ^FTSE (score 63.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +1.0% |
| ret_20d    | +2.3% |
| ret_60d    | +1.2% |
| ma20_dist  | +0.6% |
| ma50_dist  | +1.6% |
| vol_20d    |  9.5% |
| mdd_60d    |  2.6% |
| rsi_14     |  59.3 |
| zscore_20d |   0.9 |

### Brent Crude Oil / BZ=F (score 61.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +4.6% |
| ret_5d     | +15.9% |
| ret_20d    | +10.7% |
| ret_60d    | -10.6% |
| ma20_dist  | +13.9% |
| ma50_dist  |  -1.5% |
| vol_20d    |  51.1% |
| mdd_60d    |  39.4% |
| rsi_14     |   82.6 |
| zscore_20d |    2.1 |

### Dow Jones Industrial Average / ^DJI (score 56.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | -0.9% |
| ret_20d    | +1.3% |
| ret_60d    | +6.1% |
| ma20_dist  | -0.3% |
| ma50_dist  | +1.8% |
| vol_20d    |  7.2% |
| mdd_60d    |  3.2% |
| rsi_14     |  54.5 |
| zscore_20d |  -0.4 |

### Hang Seng / ^HSI (score 55.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.8% |
| ret_5d     | +1.6% |
| ret_20d    | +1.0% |
| ret_60d    | -6.8% |
| ma20_dist  | +3.5% |
| ma50_dist  | -0.8% |
| vol_20d    | 21.0% |
| mdd_60d    | 14.9% |
| rsi_14     |  75.9 |
| zscore_20d |   1.3 |

### S&P 500 / ^GSPC (score 51.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | -1.6% |
| ret_20d    | +0.5% |
| ret_60d    | +5.6% |
| ma20_dist  | -0.3% |
| ma50_dist  | -0.1% |
| vol_20d    | 10.8% |
| mdd_60d    |  4.5% |
| rsi_14     |  58.7 |
| zscore_20d |  -0.3 |

### Euro Stoxx 50 / ^STOXX50E (score 49.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | -0.6% |
| ret_20d    | -1.0% |
| ret_60d    | +5.1% |
| ma20_dist  | -0.8% |
| ma50_dist  | +1.5% |
| vol_20d    | 14.0% |
| mdd_60d    |  3.6% |
| rsi_14     |  49.9 |
| zscore_20d |  -0.9 |

### Russell 2000 / ^RUT (score 48.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -0.5% |
| ret_20d    | +1.5% |
| ret_60d    | +7.1% |
| ma20_dist  | -0.9% |
| ma50_dist  | +1.4% |
| vol_20d    | 12.3% |
| mdd_60d    |  4.8% |
| rsi_14     |  39.2 |
| zscore_20d |  -1.3 |

### CAC 40 / ^FCHI (score 47.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | -0.0% |
| ret_20d    | -1.0% |
| ret_60d    | +1.4% |
| ma20_dist  | -0.6% |
| ma50_dist  | +0.9% |
| vol_20d    | 12.0% |
| mdd_60d    |  4.2% |
| rsi_14     |  48.0 |
| zscore_20d |  -0.8 |

### Amazon.com Inc. / AMZN (score 47.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.1% |
| ret_5d     | +0.8% |
| ret_20d    | +4.1% |
| ret_60d    | -1.1% |
| ma20_dist  | +2.1% |
| ma50_dist  | -1.9% |
| vol_20d    | 31.4% |
| mdd_60d    | 17.4% |
| rsi_14     |  67.4 |
| zscore_20d |   0.8 |

### DAX / ^GDAXI (score 46.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | -0.9% |
| ret_20d    | -0.6% |
| ret_60d    | +2.8% |
| ma20_dist  | -1.0% |
| ma50_dist  | -0.1% |
| vol_20d    | 16.0% |
| mdd_60d    |  4.7% |
| rsi_14     |  53.7 |
| zscore_20d |  -0.8 |

### Meta Platforms Inc. / META (score 46.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.8% |
| ret_5d     |  -3.5% |
| ret_20d    | +13.8% |
| ret_60d    |  -3.3% |
| ma20_dist  |  +6.7% |
| ma50_dist  |  +6.9% |
| vol_20d    |  52.5% |
| mdd_60d    |  19.9% |
| rsi_14     |   67.3 |
| zscore_20d |    0.9 |

### Microsoft Corporation / MSFT (score 44.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.8% |
| ret_5d     | +2.3% |
| ret_20d    | +3.9% |
| ret_60d    | -7.0% |
| ma20_dist  | +3.3% |
| ma50_dist  | -1.9% |
| vol_20d    | 35.1% |
| mdd_60d    | 23.4% |
| rsi_14     |  63.9 |
| zscore_20d |   1.1 |

### NASDAQ 100 / ^NDX (score 31.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.5% |
| ret_5d     | -4.1% |
| ret_20d    | -3.6% |
| ret_60d    | +8.0% |
| ma20_dist  | -3.2% |
| ma50_dist  | -3.2% |
| vol_20d    | 24.7% |
| mdd_60d    |  7.0% |
| rsi_14     |  45.2 |
| zscore_20d |  -2.1 |

### Natural Gas / NG=F (score 31.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.0% |
| ret_5d     | -0.8% |
| ret_20d    | -7.3% |
| ret_60d    | +8.1% |
| ma20_dist  | -6.6% |
| ma50_dist  | -5.4% |
| vol_20d    | 39.5% |
| mdd_60d    | 14.5% |
| rsi_14     |  30.6 |
| zscore_20d |  -1.3 |

### NVIDIA Corporation / NVDA (score 30.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.2% |
| ret_5d     | -3.9% |
| ret_20d    | -0.9% |
| ret_60d    | +1.5% |
| ma20_dist  | +0.3% |
| ma50_dist  | -3.4% |
| vol_20d    | 38.0% |
| mdd_60d    | 18.3% |
| rsi_14     |  58.9 |
| zscore_20d |   0.1 |

### Gold / GC=F (score 28.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.9% |
| ret_5d     |  -2.0% |
| ret_20d    |  -7.7% |
| ret_60d    | -14.4% |
| ma20_dist  |  -1.4% |
| ma50_dist  |  -6.8% |
| vol_20d    |  24.3% |
| mdd_60d    |  15.8% |
| rsi_14     |   45.7 |
| zscore_20d |   -0.9 |

### Alphabet Inc. Class A / GOOGL (score 25.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.2% |
| ret_5d     | -2.9% |
| ret_20d    | -4.7% |
| ret_60d    | +4.4% |
| ma20_dist  | -2.6% |
| ma50_dist  | -6.4% |
| vol_20d    | 35.8% |
| mdd_60d    | 16.2% |
| rsi_14     |  55.3 |
| zscore_20d |  -1.0 |

### Platinum / PL=F (score 17.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.0% |
| ret_5d     |  -0.9% |
| ret_20d    | -10.5% |
| ret_60d    | -20.8% |
| ma20_dist  |  -1.0% |
| ma50_dist  | -10.7% |
| vol_20d    |  37.6% |
| mdd_60d    |  29.1% |
| rsi_14     |   46.4 |
| zscore_20d |   -0.4 |

### Tesla Inc. / TSLA (score 15.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.6% |
| ret_5d     | -6.6% |
| ret_20d    | -3.9% |
| ret_60d    | -1.4% |
| ma20_dist  | -4.3% |
| ma50_dist  | -7.1% |
| vol_20d    | 58.0% |
| mdd_60d    | 15.8% |
| rsi_14     |  50.3 |
| zscore_20d |  -1.2 |

### Silver / SI=F (score 11.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.6% |
| ret_5d     |  -6.0% |
| ret_20d    | -20.5% |
| ret_60d    | -26.4% |
| ma20_dist  |  -5.9% |
| ma50_dist  | -18.3% |
| vol_20d    |  46.5% |
| mdd_60d    |  37.1% |
| rsi_14     |   41.6 |
| zscore_20d |   -1.3 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Wheat / ZW=F                        |  18.0536 |           2.6% |                 0.29x |       36.1071 |            5.3% |
| Apple Inc. / AAPL                   |   8.2550 |           2.5% |                 0.28x |       16.5099 |            4.9% |
| Corn / ZC=F                         |  12.1250 |           2.6% |                 0.29x |       24.2500 |            5.2% |
| Soybeans / ZS=F                     |  19.6964 |           1.6% |                 0.49x |       39.3929 |            3.3% |
| JPMorgan Chase & Co. / JPM          |   7.8443 |           2.3% |                 0.45x |       15.6886 |            4.6% |
| UnitedHealth Group Inc. / UNH       |  12.7621 |           3.0% |                 0.41x |       25.5243 |            6.0% |
| FTSE 100 / ^FTSE                    | 120.4572 |           1.1% |                 1.05x |      240.9143 |            2.3% |
| Brent Crude Oil / BZ=F              |   3.4436 |           3.9% |                 0.20x |        6.8871 |            7.8% |
| Dow Jones Industrial Average / ^DJI | 526.8463 |           1.0% |                 1.38x |     1053.6925 |            2.0% |
| Hang Seng / ^HSI                    | 509.0292 |           2.1% |                 0.48x |     1018.0583 |            4.1% |
| S&P 500 / ^GSPC                     |  73.9665 |           1.0% |                 0.93x |      147.9330 |            2.0% |
| Euro Stoxx 50 / ^STOXX50E           |  76.2335 |           1.2% |                 0.71x |      152.4669 |            2.4% |
| Russell 2000 / ^RUT                 |  38.4859 |           1.3% |                 0.81x |       76.9718 |            2.6% |
| CAC 40 / ^FCHI                      |  97.6829 |           1.2% |                 0.83x |      195.3658 |            2.3% |
| Amazon.com Inc. / AMZN              |   7.5500 |           3.1% |                 0.32x |       15.1000 |            6.1% |
| DAX / ^GDAXI                        | 331.7683 |           1.3% |                 0.62x |      663.5366 |            2.7% |
| Meta Platforms Inc. / META          |  30.6629 |           4.7% |                 0.19x |       61.3257 |            9.5% |
| Microsoft Corporation / MSFT        |  11.4607 |           2.9% |                 0.29x |       22.9214 |            5.8% |
| NASDAQ 100 / ^NDX                   | 605.0145 |           2.1% |                 0.40x |     1210.0290 |            4.2% |
| Natural Gas / NG=F                  |   0.1246 |           4.3% |                 0.25x |        0.2493 |            8.5% |
| NVIDIA Corporation / NVDA           |   7.3471 |           3.6% |                 0.26x |       14.6943 |            7.2% |
| Gold / GC=F                         |  81.0286 |           2.0% |                 0.41x |      162.0572 |            4.0% |
| Alphabet Inc. Class A / GOOGL       |  11.0664 |           3.2% |                 0.28x |       22.1329 |            6.4% |
| Platinum / PL=F                     |  38.0143 |           2.4% |                 0.27x |       76.0286 |            4.7% |
| Tesla Inc. / TSLA                   |  18.6479 |           4.9% |                 0.17x |       37.2957 |            9.8% |
| Silver / SI=F                       |   2.0766 |           3.7% |                 0.22x |        4.1531 |            7.4% |

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

Scoring engine version: **1.0.0** | Git commit: **7a7bce5**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
