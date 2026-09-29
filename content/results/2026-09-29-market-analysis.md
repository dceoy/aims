+++
title = "Market Analysis 2026-09-29"
date = "2026-09-29T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: BZ=F (score 75.2)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-09-29.json", "data/history/2026-09-29.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "a5b9d45"
+++

## Market Regime

**Neutral** — 9 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Brent Crude Oil / BZ=F** — score 75.2, 20d return +16.3%, RSI14=60. 20d up +16.3%; above MA20 by 3.3%; RSI14=60
- **NVIDIA Corporation / NVDA** — score 75.2, 20d return +5.3%, RSI14=54. 20d up +5.3%; above MA20 by 3.0%; RSI14=54
- **Microsoft Corporation / MSFT** — score 73.9, 20d return -0.8%, RSI14=59. 20d down -0.8%; above MA20 by 1.9%; RSI14=59
- **Apple Inc. / AAPL** — score 71.2, 20d return +5.8%, RSI14=76. 20d up +5.8%; above MA20 by 2.4%; RSI14=76
- **NASDAQ 100 / ^NDX** — score 69.4, 20d return +2.9%, RSI14=61. 20d up +2.9%; above MA20 by 2.1%; RSI14=61

## Upcoming Events

_No scheduled events for covered instruments in the next 7 days._

## Signal History

Compared with the previous available report (**2026-09-28**).

- **New top-5:** BZ=F, NVDA
- **Persistent top signals:** AAPL (2 reports), MSFT (2 reports), ^NDX (2 reports)
- **Dropped from top-5:** META, ^GSPC

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     -2 |    -4.2 |
| 7203.T    |     +1 |    +6.7 |
| 8306.T    |     -1 |    +0.0 |
| AAPL      |     -2 |    -5.2 |
| AMZN      |     +0 |    -3.9 |
| BZ=F      |     +7 |   +16.1 |
| CL=F      |     +2 |   +13.9 |
| GC=F      |     -4 |   -14.8 |
| GOOGL     |     +1 |    +4.5 |
| HG=F      |     -2 |    -8.8 |
| JPM       |     -2 |    -8.2 |
| META      |     -5 |    -7.9 |
| MSFT      |     -2 |    -7.6 |
| NG=F      |     -1 |    -6.1 |
| NVDA      |     +8 |   +21.5 |
| PL=F      |     -6 |   -17.3 |
| SI=F      |     -8 |   -20.9 |
| TSLA      |     -7 |   -21.2 |
| UNH       |     +7 |   +12.1 |
| XOM       |     +4 |   +23.0 |
| ZC=F      |     -1 |    -1.2 |
| ZS=F      |     -5 |   -14.2 |
| ZW=F      |     -1 |    -5.5 |
| ^DJI      |     -3 |    -1.8 |
| ^FCHI     |     +5 |   +12.1 |
| ^FTSE     |     +1 |    +6.1 |
| ^GDAXI    |     +3 |    +6.4 |
| ^GSPC     |     -1 |    -0.9 |
| ^HSI      |     +9 |   +17.3 |
| ^N225     |     -1 |    -3.6 |
| ^NDX      |     -2 |    -0.9 |
| ^RUT      |     +7 |    +8.5 |
| ^STOXX50E |     +1 |    +6.1 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Exxon Mobil Corporation / XOM** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Nikkei 225 / ^N225** — missing_bars
- **Natural Gas / NG=F** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input
- **Copper / HG=F** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|    1 | Brent Crude Oil / BZ=F |  75.2 |   Yes    | —               | 20d up +16.3%; above MA20 by 3.3%; RSI14=60   |
|    7 | Corn / ZC=F            |  64.2 |   Yes    | —               | 20d up +2.1%; above MA20 by 0.1%; RSI14=57    |
|   12 | Soybeans / ZS=F        |  49.1 |   Yes    | —               | 20d up +0.9%; below MA20 by 1.4%; RSI14=46    |
|   21 | Platinum / PL=F        |  26.1 |   Yes    | —               | 20d down -3.8%; below MA20 by 4.1%; RSI14=35  |
|   22 | Wheat / ZW=F           |  25.1 |   Yes    | —               | 20d down -10.2%; below MA20 by 4.7%; RSI14=35 |
|   24 | Gold / GC=F            |  16.7 |   Yes    | —               | 20d down -7.0%; below MA20 by 5.0%; RSI14=25  |
|   25 | Silver / SI=F          |  13.6 |   Yes    | —               | 20d down -7.6%; below MA20 by 5.8%; RSI14=35  |
|   29 | Natural Gas / NG=F     |  55.1 |    No    | malformed_input | Suppressed: malformed_input                   |
|   30 | WTI Crude Oil / CL=F   |  51.5 |    No    | malformed_input | Suppressed: malformed_input                   |
|   31 | Copper / HG=F          |  50.3 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    2 | NVIDIA Corporation / NVDA                                                      |  75.2 |   Yes    | —                             | 20d up +5.3%; above MA20 by 3.0%; RSI14=54   |
|    3 | Microsoft Corporation / MSFT                                                   |  73.9 |   Yes    | —                             | 20d down -0.8%; above MA20 by 1.9%; RSI14=59 |
|    4 | Apple Inc. / AAPL                                                              |  71.2 |   Yes    | —                             | 20d up +5.8%; above MA20 by 2.4%; RSI14=76   |
|    9 | Meta Platforms Inc. / META                                                     |  59.4 |   Yes    | —                             | 20d up +23.9%; above MA20 by 7.2%; RSI14=68  |
|   15 | Alphabet Inc. Class A / GOOGL                                                  |  45.5 |   Yes    | —                             | 20d down -1.0%; above MA20 by 0.2%; RSI14=53 |
|   17 | UnitedHealth Group Inc. / UNH                                                  |  38.2 |   Yes    | —                             | 20d down -3.3%; below MA20 by 1.4%; RSI14=30 |
|   19 | Tesla Inc. / TSLA                                                              |  28.5 |   Yes    | —                             | 20d up +2.5%; below MA20 by 2.4%; RSI14=42   |
|   20 | JPMorgan Chase & Co. / JPM                                                     |  26.1 |   Yes    | —                             | 20d down -5.9%; below MA20 by 3.9%; RSI14=32 |
|   23 | Amazon.com Inc. / AMZN                                                         |  24.6 |   Yes    | —                             | 20d down -7.6%; below MA20 by 2.8%; RSI14=38 |
|   26 | Exxon Mobil Corporation / XOM                                                  |  70.6 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   27 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  69.4 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   32 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  40.9 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   33 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  37.0 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    5 | NASDAQ 100 / ^NDX                   |  69.4 |   Yes    | —            | 20d up +2.9%; above MA20 by 2.1%; RSI14=61   |
|    6 | S&P 500 / ^GSPC                     |  65.8 |   Yes    | —            | 20d down -0.4%; above MA20 by 0.2%; RSI14=51 |
|    8 | FTSE 100 / ^FTSE                    |  60.3 |   Yes    | —            | 20d down -1.3%; below MA20 by 0.4%; RSI14=42 |
|   10 | Euro Stoxx 50 / ^STOXX50E           |  58.2 |   Yes    | —            | 20d down -1.9%; below MA20 by 0.3%; RSI14=41 |
|   11 | DAX / ^GDAXI                        |  50.3 |   Yes    | —            | 20d down -3.4%; below MA20 by 1.0%; RSI14=37 |
|   13 | Hang Seng / ^HSI                    |  47.6 |   Yes    | —            | 20d down -3.6%; below MA20 by 1.4%; RSI14=35 |
|   14 | CAC 40 / ^FCHI                      |  46.4 |   Yes    | —            | 20d down -3.1%; below MA20 by 1.2%; RSI14=34 |
|   16 | Dow Jones Industrial Average / ^DJI |  43.9 |   Yes    | —            | 20d down -3.9%; below MA20 by 1.5%; RSI14=36 |
|   18 | Russell 2000 / ^RUT                 |  31.5 |   Yes    | —            | 20d down -5.2%; below MA20 by 2.7%; RSI14=23 |
|   28 | Nikkei 225 / ^N225                  |  59.4 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-09-28 |
| 7203.T    | 2026-09-28 |
| 8306.T    | 2026-09-28 |
| AAPL      | 2026-09-28 |
| AMZN      | 2026-09-28 |
| BZ=F      | 2026-09-28 |
| CL=F      | 2026-09-28 |
| GC=F      | 2026-09-28 |
| GOOGL     | 2026-09-28 |
| HG=F      | 2026-09-28 |
| JPM       | 2026-09-28 |
| META      | 2026-09-28 |
| MSFT      | 2026-09-28 |
| NG=F      | 2026-09-28 |
| NVDA      | 2026-09-28 |
| PL=F      | 2026-09-28 |
| SI=F      | 2026-09-28 |
| TSLA      | 2026-09-28 |
| UNH       | 2026-09-28 |
| XOM       | 2026-09-28 |
| ZC=F      | 2026-09-28 |
| ZS=F      | 2026-09-28 |
| ZW=F      | 2026-09-28 |
| ^DJI      | 2026-09-28 |
| ^FCHI     | 2026-09-28 |
| ^FTSE     | 2026-09-28 |
| ^GDAXI    | 2026-09-28 |
| ^GSPC     | 2026-09-28 |
| ^HSI      | 2026-09-28 |
| ^N225     | 2026-09-28 |
| ^NDX      | 2026-09-28 |
| ^RUT      | 2026-09-28 |
| ^STOXX50E | 2026-09-28 |

## Symbol Details

### Brent Crude Oil / BZ=F (score 75.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.9% |
| ret_5d     |  +4.9% |
| ret_20d    | +16.3% |
| ret_60d    | +38.0% |
| ma20_dist  |  +3.3% |
| ma50_dist  | +12.2% |
| vol_20d    |  41.3% |
| mdd_60d    |  21.2% |
| rsi_14     |   60.0 |
| zscore_20d |    0.8 |

### NVIDIA Corporation / NVDA (score 75.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.7% |
| ret_5d     |  +0.7% |
| ret_20d    |  +5.3% |
| ret_60d    | +17.5% |
| ma20_dist  |  +3.0% |
| ma50_dist  |  +5.8% |
| vol_20d    |  27.2% |
| mdd_60d    |  10.6% |
| rsi_14     |   54.1 |
| zscore_20d |    1.2 |

### Microsoft Corporation / MSFT (score 73.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.3% |
| ret_5d     |  +1.5% |
| ret_20d    |  -0.8% |
| ret_60d    | +30.4% |
| ma20_dist  |  +1.9% |
| ma50_dist  |  +6.6% |
| vol_20d    |  24.4% |
| mdd_60d    |   5.1% |
| rsi_14     |   59.0 |
| zscore_20d |    1.4 |

### Apple Inc. / AAPL (score 71.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | -0.2% |
| ret_20d    | +5.8% |
| ret_60d    | +9.6% |
| ma20_dist  | +2.4% |
| ma50_dist  | +5.1% |
| vol_20d    | 21.7% |
| mdd_60d    | 11.0% |
| rsi_14     |  76.3 |
| zscore_20d |   1.0 |

### NASDAQ 100 / ^NDX (score 69.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.1% |
| ret_5d     | -0.7% |
| ret_20d    | +2.9% |
| ret_60d    | +3.2% |
| ma20_dist  | +2.1% |
| ma50_dist  | +3.3% |
| vol_20d    | 15.9% |
| mdd_60d    |  8.8% |
| rsi_14     |  60.6 |
| zscore_20d |   1.0 |

### S&P 500 / ^GSPC (score 65.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | -1.0% |
| ret_20d    | -0.4% |
| ret_60d    | +2.7% |
| ma20_dist  | +0.2% |
| ma50_dist  | +0.6% |
| vol_20d    | 10.9% |
| mdd_60d    |  3.4% |
| rsi_14     |  50.8 |
| zscore_20d |   0.2 |

### Corn / ZC=F (score 64.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.0% |
| ret_5d     |  -3.7% |
| ret_20d    |  +2.1% |
| ret_60d    | +20.3% |
| ma20_dist  |  +0.1% |
| ma50_dist  |  +7.0% |
| vol_20d    |  22.7% |
| mdd_60d    |   6.0% |
| rsi_14     |   57.1 |
| zscore_20d |    0.0 |

### FTSE 100 / ^FTSE (score 60.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | -0.5% |
| ret_20d    | -1.3% |
| ret_60d    | +0.1% |
| ma20_dist  | -0.4% |
| ma50_dist  | -0.8% |
| vol_20d    |  9.7% |
| mdd_60d    |  2.7% |
| rsi_14     |  42.2 |
| zscore_20d |  -0.6 |

### Meta Platforms Inc. / META (score 59.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -4.8% |
| ret_5d     |  -3.5% |
| ret_20d    | +23.9% |
| ret_60d    | +22.8% |
| ma20_dist  |  +7.2% |
| ma50_dist  | +16.0% |
| vol_20d    |  55.0% |
| mdd_60d    |  20.9% |
| rsi_14     |   67.8 |
| zscore_20d |    0.8 |

### Euro Stoxx 50 / ^STOXX50E (score 58.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.0% |
| ret_5d     | -0.3% |
| ret_20d    | -1.9% |
| ret_60d    | -1.5% |
| ma20_dist  | -0.3% |
| ma50_dist  | -1.3% |
| vol_20d    | 11.7% |
| mdd_60d    |  4.8% |
| rsi_14     |  41.2 |
| zscore_20d |  -0.3 |

### DAX / ^GDAXI (score 50.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | -0.8% |
| ret_20d    | -3.4% |
| ret_60d    | -1.7% |
| ma20_dist  | -1.0% |
| ma50_dist  | -1.7% |
| vol_20d    | 11.9% |
| mdd_60d    |  4.9% |
| rsi_14     |  37.4 |
| zscore_20d |  -0.9 |

### Soybeans / ZS=F (score 49.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.3% |
| ret_5d     | -3.0% |
| ret_20d    | +0.9% |
| ret_60d    | +7.8% |
| ma20_dist  | -1.4% |
| ma50_dist  | +3.8% |
| vol_20d    | 21.2% |
| mdd_60d    |  8.1% |
| rsi_14     |  46.2 |
| zscore_20d |  -1.2 |

### Hang Seng / ^HSI (score 47.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | -1.6% |
| ret_20d    | -3.6% |
| ret_60d    | +4.3% |
| ma20_dist  | -1.4% |
| ma50_dist  | -2.7% |
| vol_20d    | 12.3% |
| mdd_60d    |  5.8% |
| rsi_14     |  34.8 |
| zscore_20d |  -1.1 |

### CAC 40 / ^FCHI (score 46.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.0% |
| ret_5d     | -0.7% |
| ret_20d    | -3.1% |
| ret_60d    | -4.7% |
| ma20_dist  | -1.2% |
| ma50_dist  | -3.6% |
| vol_20d    | 10.9% |
| mdd_60d    |  7.6% |
| rsi_14     |  33.8 |
| zscore_20d |  -1.1 |

### Alphabet Inc. Class A / GOOGL (score 45.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | -3.4% |
| ret_20d    | -1.0% |
| ret_60d    | -4.8% |
| ma20_dist  | +0.2% |
| ma50_dist  | -0.4% |
| vol_20d    | 25.9% |
| mdd_60d    | 14.4% |
| rsi_14     |  53.2 |
| zscore_20d |   0.1 |

### Dow Jones Industrial Average / ^DJI (score 43.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | -1.1% |
| ret_20d    | -3.9% |
| ret_60d    | -2.7% |
| ma20_dist  | -1.5% |
| ma50_dist  | -2.5% |
| vol_20d    | 11.5% |
| mdd_60d    |  5.5% |
| rsi_14     |  36.0 |
| zscore_20d |  -1.2 |

### UnitedHealth Group Inc. / UNH (score 38.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.3% |
| ret_5d     |  +0.1% |
| ret_20d    |  -3.3% |
| ret_60d    | -11.2% |
| ma20_dist  |  -1.4% |
| ma50_dist  |  -4.9% |
| vol_20d    |  18.5% |
| mdd_60d    |  14.9% |
| rsi_14     |   30.2 |
| zscore_20d |   -0.6 |

### Russell 2000 / ^RUT (score 31.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | -2.0% |
| ret_20d    | -5.2% |
| ret_60d    | -5.9% |
| ma20_dist  | -2.7% |
| ma50_dist  | -4.6% |
| vol_20d    | 11.7% |
| mdd_60d    |  8.2% |
| rsi_14     |  22.9 |
| zscore_20d |  -1.6 |

### Tesla Inc. / TSLA (score 28.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -3.9% |
| ret_5d     | -4.8% |
| ret_20d    | +2.5% |
| ret_60d    | -9.1% |
| ma20_dist  | -2.4% |
| ma50_dist  | +2.8% |
| vol_20d    | 44.9% |
| mdd_60d    | 28.9% |
| rsi_14     |  41.8 |
| zscore_20d |  -1.1 |

### JPMorgan Chase & Co. / JPM (score 26.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.9% |
| ret_5d     | -4.4% |
| ret_20d    | -5.9% |
| ret_60d    | +1.1% |
| ma20_dist  | -3.9% |
| ma50_dist  | -4.7% |
| vol_20d    | 18.7% |
| mdd_60d    |  7.8% |
| rsi_14     |  31.9 |
| zscore_20d |  -1.9 |

### Platinum / PL=F (score 26.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -3.0% |
| ret_5d     | -4.3% |
| ret_20d    | -3.8% |
| ret_60d    | +6.3% |
| ma20_dist  | -4.1% |
| ma50_dist  | -2.7% |
| vol_20d    | 35.8% |
| mdd_60d    | 10.1% |
| rsi_14     |  35.1 |
| zscore_20d |  -1.8 |

### Wheat / ZW=F (score 25.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.1% |
| ret_5d     |  -5.2% |
| ret_20d    | -10.2% |
| ret_60d    | +14.9% |
| ma20_dist  |  -4.7% |
| ma50_dist  |  -0.5% |
| vol_20d    |  26.2% |
| mdd_60d    |  10.7% |
| rsi_14     |   35.0 |
| zscore_20d |   -1.8 |

### Amazon.com Inc. / AMZN (score 24.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.4% |
| ret_5d     | -4.8% |
| ret_20d    | -7.6% |
| ret_60d    | +1.4% |
| ma20_dist  | -2.8% |
| ma50_dist  | -3.9% |
| vol_20d    | 22.7% |
| mdd_60d    | 13.4% |
| rsi_14     |  38.3 |
| zscore_20d |  -1.7 |

### Gold / GC=F (score 16.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -3.5% |
| ret_5d     | -4.9% |
| ret_20d    | -7.0% |
| ret_60d    | +0.9% |
| ma20_dist  | -5.0% |
| ma50_dist  | -4.8% |
| vol_20d    | 20.4% |
| mdd_60d    | 11.4% |
| rsi_14     |  25.3 |
| zscore_20d |  -2.9 |

### Silver / SI=F (score 13.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -4.7% |
| ret_5d     | -7.0% |
| ret_20d    | -7.6% |
| ret_60d    | +1.4% |
| ma20_dist  | -5.8% |
| ma50_dist  | -4.9% |
| vol_20d    | 35.2% |
| mdd_60d    | 11.9% |
| rsi_14     |  35.4 |
| zscore_20d |  -2.5 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Brent Crude Oil / BZ=F              |   5.2129 |           5.0% |                 0.24x |       10.4257 |            9.9% |
| NVIDIA Corporation / NVDA           |   5.1534 |           2.3% |                 0.37x |       10.3067 |            4.5% |
| Microsoft Corporation / MSFT        |  11.2600 |           2.2% |                 0.41x |       22.5200 |            4.4% |
| Apple Inc. / AAPL                   |   6.7529 |           2.0% |                 0.46x |       13.5057 |            4.0% |
| NASDAQ 100 / ^NDX                   | 408.6343 |           1.3% |                 0.63x |      817.2687 |            2.7% |
| S&P 500 / ^GSPC                     |  70.0235 |           0.9% |                 0.92x |      140.0471 |            1.8% |
| Corn / ZC=F                         |  10.8571 |           2.1% |                 0.44x |       21.7143 |            4.2% |
| FTSE 100 / ^FTSE                    | 102.6856 |           1.0% |                 1.03x |      205.3712 |            1.9% |
| Meta Platforms Inc. / META          |  31.2811 |           4.4% |                 0.18x |       62.5622 |            8.7% |
| Euro Stoxx 50 / ^STOXX50E           |  76.7135 |           1.2% |                 0.85x |      153.4270 |            2.4% |
| DAX / ^GDAXI                        | 301.6031 |           1.2% |                 0.84x |      603.2062 |            2.4% |
| Soybeans / ZS=F                     |  22.0357 |           1.7% |                 0.47x |       44.0714 |            3.4% |
| Hang Seng / ^HSI                    | 288.2960 |           1.2% |                 0.81x |      576.5921 |            2.3% |
| CAC 40 / ^FCHI                      |  91.0237 |           1.1% |                 0.92x |      182.0474 |            2.3% |
| Alphabet Inc. Class A / GOOGL       |   8.8893 |           2.6% |                 0.39x |       17.7786 |            5.2% |
| Dow Jones Industrial Average / ^DJI | 508.6267 |           1.0% |                 0.87x |     1017.2533 |            2.0% |
| UnitedHealth Group Inc. / UNH       |   9.6298 |           2.5% |                 0.54x |       19.2597 |            5.1% |
| Russell 2000 / ^RUT                 |  34.1864 |           1.2% |                 0.85x |       68.3728 |            2.4% |
| Tesla Inc. / TSLA                   |  11.1650 |           3.1% |                 0.22x |       22.3300 |            6.2% |
| JPMorgan Chase & Co. / JPM          |   7.2507 |           2.2% |                 0.54x |       14.5014 |            4.3% |
| Platinum / PL=F                     |  31.1429 |           1.8% |                 0.28x |       62.2857 |            3.6% |
| Wheat / ZW=F                        |  15.9107 |           2.3% |                 0.38x |       31.8214 |            4.6% |
| Amazon.com Inc. / AMZN              |   5.4086 |           2.2% |                 0.44x |       10.8171 |            4.4% |
| Gold / GC=F                         |  99.2000 |           2.4% |                 0.49x |      198.3999 |            4.8% |
| Silver / SI=F                       |   1.5406 |           2.5% |                 0.28x |        3.0813 |            5.0% |

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

Scoring engine version: **1.0.0** | Git commit: **a5b9d45**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
