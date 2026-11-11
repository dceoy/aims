+++
title = "Market Analysis 2026-11-11"
date = "2026-11-11T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: ^FCHI (score 79.1)."
ticker_symbols = [
  "6758.T",
  "7203.T",
  "8306.T",
  "AAPL",
  "AMZN",
  "BZ=F",
  "CL=F",
  "GC=F",
  "GOOGL",
  "HG=F",
  "JPM",
  "META",
  "MSFT",
  "NG=F",
  "NVDA",
  "PL=F",
  "SI=F",
  "TSLA",
  "UNH",
  "XOM",
  "ZC=F",
  "ZS=F",
  "ZW=F",
  "^DJI",
  "^FCHI",
  "^FTSE",
  "^GDAXI",
  "^GSPC",
  "^HSI",
  "^N225",
  "^NDX",
  "^RUT",
  "^STOXX50E",
]
source_files = ["data/analysis/2026-11-11.json", "data/history/2026-11-11.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "4ce5958"
+++

## Market Regime

**Neutral** — 11 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **CAC 40 / ^FCHI** — score 79.1, 20d return +5.8%, RSI14=72. 20d up +5.8%; above MA20 by 3.7%; RSI14=72
- **Amazon.com Inc. / AMZN** — score 77.0, 20d return +4.8%, RSI14=55. 20d up +4.8%; above MA20 by 6.1%; RSI14=55
- **Euro Stoxx 50 / ^STOXX50E** — score 76.1, 20d return +2.6%, RSI14=57. 20d up +2.6%; above MA20 by 2.4%; RSI14=57
- **DAX / ^GDAXI** — score 74.2, 20d return +4.3%, RSI14=60. 20d up +4.3%; above MA20 by 2.4%; RSI14=60
- **Apple Inc. / AAPL** — score 72.7, 20d return +2.1%, RSI14=53. 20d up +2.1%; above MA20 by 1.2%; RSI14=53

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                   | Applies To |
| ---------- | ----------------------- | ---------- |
| 2026-11-13 | 8306.T earnings release | 8306.T     |
| 2026-11-17 | NVDA earnings release   | NVDA       |

## Signal History

Compared with the previous available report (**2026-11-10**).

- **New top-5:** ^STOXX50E
- **Persistent top signals:** ^GDAXI (11 reports), ^FCHI (4 reports), AAPL (3 reports), AMZN (3 reports)
- **Dropped from top-5:** MSFT

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     -1 |    -9.1 |
| 7203.T    |     -1 |   -10.9 |
| 8306.T    |     +1 |   +11.8 |
| AAPL      |     -4 |    -4.5 |
| AMZN      |     +0 |    +3.9 |
| BZ=F      |     +0 |    -0.3 |
| CL=F      |     +0 |    -0.3 |
| GC=F      |     -3 |   -10.0 |
| GOOGL     |     +1 |    +1.5 |
| HG=F      |     -2 |   -10.0 |
| JPM       |     +2 |    +1.2 |
| META      |     -1 |    -3.6 |
| MSFT      |     -7 |   -14.6 |
| NG=F      |     +2 |    +1.8 |
| NVDA      |     +0 |    -2.4 |
| PL=F      |     -2 |    -5.8 |
| SI=F      |     -2 |    -8.8 |
| TSLA      |     -1 |    -1.5 |
| UNH       |     +6 |   +10.6 |
| XOM       |     +1 |    +1.5 |
| ZC=F      |     +4 |   +13.9 |
| ZS=F      |     +9 |   +23.6 |
| ZW=F      |     +2 |    +8.2 |
| ^DJI      |     -3 |    -3.6 |
| ^FCHI     |     +2 |    +6.1 |
| ^FTSE     |     +0 |    +0.0 |
| ^GDAXI    |     +0 |    +1.2 |
| ^GSPC     |     -3 |    -7.0 |
| ^HSI      |     +4 |    +8.2 |
| ^N225     |     +0 |    +7.6 |
| ^NDX      |     -3 |    -8.2 |
| ^RUT      |     -4 |    -7.0 |
| ^STOXX50E |     +3 |    +6.4 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Natural Gas / NG=F** — malformed_input
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Copper / HG=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars
- **WTI Crude Oil / CL=F** — malformed_input

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                    |
| ---: | ---------------------- | ----: | :------: | --------------- | ---------------------------------------------- |
|   10 | Soybeans / ZS=F        |  57.9 |   Yes    | —               | 20d down -4.6%; below MA20 by 0.3%; RSI14=43   |
|   16 | Corn / ZC=F            |  42.7 |   Yes    | —               | 20d down -7.0%; below MA20 by 1.3%; RSI14=35   |
|   18 | Gold / GC=F            |  38.5 |   Yes    | —               | 20d down -3.5%; below MA20 by 1.0%; RSI14=43   |
|   19 | Platinum / PL=F        |  34.2 |   Yes    | —               | 20d down -7.1%; below MA20 by 0.6%; RSI14=39   |
|   20 | Wheat / ZW=F           |  29.4 |   Yes    | —               | 20d down -11.4%; below MA20 by 4.3%; RSI14=22  |
|   23 | Silver / SI=F          |  16.7 |   Yes    | —               | 20d down -13.6%; below MA20 by 4.8%; RSI14=32  |
|   24 | Brent Crude Oil / BZ=F |  14.6 |   Yes    | —               | 20d down -13.4%; below MA20 by 14.5%; RSI14=32 |
|   26 | Natural Gas / NG=F     |  75.5 |    No    | malformed_input | Suppressed: malformed_input                    |
|   31 | Copper / HG=F          |  33.9 |    No    | malformed_input | Suppressed: malformed_input                    |
|   33 | WTI Crude Oil / CL=F   |  20.9 |    No    | malformed_input | Suppressed: malformed_input                    |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                    |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | ---------------------------------------------- |
|    2 | Amazon.com Inc. / AMZN                                                         |  77.0 |   Yes    | —                             | 20d up +4.8%; above MA20 by 6.1%; RSI14=55     |
|    5 | Apple Inc. / AAPL                                                              |  72.7 |   Yes    | —                             | 20d up +2.1%; above MA20 by 1.2%; RSI14=53     |
|    8 | UnitedHealth Group Inc. / UNH                                                  |  62.1 |   Yes    | —                             | 20d up +7.2%; below MA20 by 0.5%; RSI14=42     |
|    9 | JPMorgan Chase & Co. / JPM                                                     |  60.0 |   Yes    | —                             | 20d up +3.2%; above MA20 by 1.2%; RSI14=55     |
|   12 | Microsoft Corporation / MSFT                                                   |  57.0 |   Yes    | —                             | 20d down -1.9%; above MA20 by 0.4%; RSI14=50   |
|   14 | Tesla Inc. / TSLA                                                              |  50.3 |   Yes    | —                             | 20d up +1.2%; below MA20 by 0.2%; RSI14=48     |
|   17 | Meta Platforms Inc. / META                                                     |  40.9 |   Yes    | —                             | 20d down -15.9%; below MA20 by 1.6%; RSI14=36  |
|   22 | Alphabet Inc. Class A / GOOGL                                                  |  21.2 |   Yes    | —                             | 20d down -18.8%; below MA20 by 7.6%; RSI14=25  |
|   25 | NVIDIA Corporation / NVDA                                                      |   2.4 |   Yes    | —                             | 20d down -26.1%; below MA20 by 18.1%; RSI14=19 |
|   27 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  74.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   28 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  71.8 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   29 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  55.1 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   30 | Exxon Mobil Corporation / XOM                                                  |  34.5 |    No    | malformed_input               | Suppressed: malformed_input                    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    1 | CAC 40 / ^FCHI                      |  79.1 |   Yes    | —            | 20d up +5.8%; above MA20 by 3.7%; RSI14=72   |
|    3 | Euro Stoxx 50 / ^STOXX50E           |  76.1 |   Yes    | —            | 20d up +2.6%; above MA20 by 2.4%; RSI14=57   |
|    4 | DAX / ^GDAXI                        |  74.2 |   Yes    | —            | 20d up +4.3%; above MA20 by 2.4%; RSI14=60   |
|    6 | Hang Seng / ^HSI                    |  68.5 |   Yes    | —            | 20d up +1.2%; above MA20 by 3.4%; RSI14=62   |
|    7 | FTSE 100 / ^FTSE                    |  63.3 |   Yes    | —            | 20d up +1.0%; above MA20 by 0.0%; RSI14=50   |
|   11 | Dow Jones Industrial Average / ^DJI |  57.3 |   Yes    | —            | 20d up +1.1%; above MA20 by 0.1%; RSI14=46   |
|   13 | Russell 2000 / ^RUT                 |  53.6 |   Yes    | —            | 20d up +1.4%; above MA20 by 1.1%; RSI14=54   |
|   15 | S&P 500 / ^GSPC                     |  45.8 |   Yes    | —            | 20d down -3.6%; below MA20 by 1.4%; RSI14=40 |
|   21 | NASDAQ 100 / ^NDX                   |  28.2 |   Yes    | —            | 20d down -9.3%; below MA20 by 3.7%; RSI14=36 |
|   32 | Nikkei 225 / ^N225                  |  30.3 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-11-10 |
| 7203.T    | 2026-11-10 |
| 8306.T    | 2026-11-10 |
| AAPL      | 2026-11-10 |
| AMZN      | 2026-11-10 |
| BZ=F      | 2026-11-10 |
| CL=F      | 2026-11-10 |
| GC=F      | 2026-11-10 |
| GOOGL     | 2026-11-10 |
| HG=F      | 2026-11-10 |
| JPM       | 2026-11-10 |
| META      | 2026-11-10 |
| MSFT      | 2026-11-10 |
| NG=F      | 2026-11-10 |
| NVDA      | 2026-11-10 |
| PL=F      | 2026-11-10 |
| SI=F      | 2026-11-10 |
| TSLA      | 2026-11-10 |
| UNH       | 2026-11-10 |
| XOM       | 2026-11-10 |
| ZC=F      | 2026-11-10 |
| ZS=F      | 2026-11-10 |
| ZW=F      | 2026-11-10 |
| ^DJI      | 2026-11-10 |
| ^FCHI     | 2026-11-10 |
| ^FTSE     | 2026-11-10 |
| ^GDAXI    | 2026-11-10 |
| ^GSPC     | 2026-11-10 |
| ^HSI      | 2026-11-10 |
| ^N225     | 2026-11-10 |
| ^NDX      | 2026-11-10 |
| ^RUT      | 2026-11-10 |
| ^STOXX50E | 2026-11-10 |

## Symbol Details

### CAC 40 / ^FCHI (score 79.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | +3.2% |
| ret_20d    | +5.8% |
| ret_60d    | -2.7% |
| ma20_dist  | +3.7% |
| ma50_dist  | +3.2% |
| vol_20d    | 13.0% |
| mdd_60d    |  9.1% |
| rsi_14     |  71.7 |
| zscore_20d |   2.0 |

### Amazon.com Inc. / AMZN (score 77.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.5% |
| ret_5d     | +8.0% |
| ret_20d    | +4.8% |
| ret_60d    | +3.7% |
| ma20_dist  | +6.1% |
| ma50_dist  | +6.6% |
| vol_20d    | 41.6% |
| mdd_60d    |  9.8% |
| rsi_14     |  55.4 |
| zscore_20d |   1.9 |

### Euro Stoxx 50 / ^STOXX50E (score 76.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | +3.0% |
| ret_20d    | +2.6% |
| ret_60d    | -2.2% |
| ma20_dist  | +2.4% |
| ma50_dist  | +1.4% |
| vol_20d    | 16.0% |
| mdd_60d    |  6.4% |
| rsi_14     |  57.5 |
| zscore_20d |   2.3 |

### DAX / ^GDAXI (score 74.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +1.9% |
| ret_20d    | +4.3% |
| ret_60d    | +0.8% |
| ma20_dist  | +2.4% |
| ma50_dist  | +3.1% |
| vol_20d    | 16.4% |
| mdd_60d    |  6.6% |
| rsi_14     |  59.9 |
| zscore_20d |   1.6 |

### Apple Inc. / AAPL (score 72.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.6% |
| ret_5d     |  +5.0% |
| ret_20d    |  +2.1% |
| ret_60d    | +14.0% |
| ma20_dist  |  +1.2% |
| ma50_dist  |  +3.3% |
| vol_20d    |  26.4% |
| mdd_60d    |   4.9% |
| rsi_14     |   53.1 |
| zscore_20d |    1.0 |

### Hang Seng / ^HSI (score 68.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | +4.4% |
| ret_20d    | +1.2% |
| ret_60d    | -2.2% |
| ma20_dist  | +3.4% |
| ma50_dist  | +0.8% |
| vol_20d    | 21.2% |
| mdd_60d    | 11.8% |
| rsi_14     |  62.4 |
| zscore_20d |   1.3 |

### FTSE 100 / ^FTSE (score 63.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | +1.1% |
| ret_20d    | +1.0% |
| ret_60d    | +0.3% |
| ma20_dist  | +0.0% |
| ma50_dist  | +0.6% |
| vol_20d    | 11.9% |
| mdd_60d    |  4.2% |
| rsi_14     |  49.9 |
| zscore_20d |   0.1 |

### UnitedHealth Group Inc. / UNH (score 62.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.9% |
| ret_5d     | +0.2% |
| ret_20d    | +7.2% |
| ret_60d    | +3.0% |
| ma20_dist  | -0.5% |
| ma50_dist  | +3.7% |
| vol_20d    | 30.3% |
| mdd_60d    |  8.4% |
| rsi_14     |  42.1 |
| zscore_20d |  -0.2 |

### JPMorgan Chase & Co. / JPM (score 60.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.0% |
| ret_5d     | +1.2% |
| ret_20d    | +3.2% |
| ret_60d    | -5.2% |
| ma20_dist  | +1.2% |
| ma50_dist  | +0.4% |
| vol_20d    | 27.0% |
| mdd_60d    |  9.4% |
| rsi_14     |  54.9 |
| zscore_20d |   0.9 |

### Soybeans / ZS=F (score 57.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +3.6% |
| ret_5d     | +1.8% |
| ret_20d    | -4.6% |
| ret_60d    | +2.0% |
| ma20_dist  | -0.3% |
| ma50_dist  | -3.7% |
| vol_20d    | 16.5% |
| mdd_60d    | 11.1% |
| rsi_14     |  43.0 |
| zscore_20d |  -0.1 |

### Dow Jones Industrial Average / ^DJI (score 57.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | +0.9% |
| ret_20d    | +1.1% |
| ret_60d    | -2.3% |
| ma20_dist  | +0.1% |
| ma50_dist  | +0.4% |
| vol_20d    | 20.0% |
| mdd_60d    |  5.2% |
| rsi_14     |  45.5 |
| zscore_20d |   0.1 |

### Microsoft Corporation / MSFT (score 57.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.2% |
| ret_5d     |  +2.3% |
| ret_20d    |  -1.9% |
| ret_60d    | +11.2% |
| ma20_dist  |  +0.4% |
| ma50_dist  |  +3.0% |
| vol_20d    |  36.4% |
| mdd_60d    |   6.7% |
| rsi_14     |   50.1 |
| zscore_20d |    0.2 |

### Russell 2000 / ^RUT (score 53.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | +0.3% |
| ret_20d    | +1.4% |
| ret_60d    | -7.7% |
| ma20_dist  | +1.1% |
| ma50_dist  | -0.4% |
| vol_20d    | 25.2% |
| mdd_60d    | 10.3% |
| rsi_14     |  54.4 |
| zscore_20d |   0.8 |

### Tesla Inc. / TSLA (score 50.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.5% |
| ret_5d     |  -4.7% |
| ret_20d    |  +1.2% |
| ret_60d    | +11.9% |
| ma20_dist  |  -0.2% |
| ma50_dist  |  +1.8% |
| vol_20d    |  58.6% |
| mdd_60d    |  15.7% |
| rsi_14     |   47.9 |
| zscore_20d |   -0.0 |

### S&P 500 / ^GSPC (score 45.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -0.6% |
| ret_20d    | -3.6% |
| ret_60d    | -2.9% |
| ma20_dist  | -1.4% |
| ma50_dist  | -2.0% |
| vol_20d    | 21.3% |
| mdd_60d    |  5.9% |
| rsi_14     |  39.8 |
| zscore_20d |  -1.0 |

### Corn / ZC=F (score 42.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.2% |
| ret_5d     | +1.5% |
| ret_20d    | -7.0% |
| ret_60d    | -3.1% |
| ma20_dist  | -1.3% |
| ma50_dist  | -8.4% |
| vol_20d    | 13.5% |
| mdd_60d    | 19.1% |
| rsi_14     |  34.9 |
| zscore_20d |  -0.5 |

### Meta Platforms Inc. / META (score 40.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.0% |
| ret_5d     |  +3.3% |
| ret_20d    | -15.9% |
| ret_60d    | +12.7% |
| ma20_dist  |  -1.6% |
| ma50_dist  |  -5.3% |
| vol_20d    |  40.4% |
| mdd_60d    |  22.2% |
| rsi_14     |   35.9 |
| zscore_20d |   -0.2 |

### Gold / GC=F (score 38.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.0% |
| ret_5d     |  +2.3% |
| ret_20d    |  -3.5% |
| ret_60d    | -11.3% |
| ma20_dist  |  -1.0% |
| ma50_dist  |  -4.4% |
| vol_20d    |  24.1% |
| mdd_60d    |  17.2% |
| rsi_14     |   42.7 |
| zscore_20d |   -0.5 |

### Platinum / PL=F (score 34.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.4% |
| ret_5d     |  +7.4% |
| ret_20d    |  -7.1% |
| ret_60d    | -14.6% |
| ma20_dist  |  -0.6% |
| ma50_dist  |  -7.9% |
| vol_20d    |  33.7% |
| mdd_60d    |  25.2% |
| rsi_14     |   39.5 |
| zscore_20d |   -0.2 |

### Wheat / ZW=F (score 29.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.8% |
| ret_5d     |  -1.2% |
| ret_20d    | -11.4% |
| ret_60d    | -10.8% |
| ma20_dist  |  -4.3% |
| ma50_dist  | -11.8% |
| vol_20d    |  14.4% |
| mdd_60d    |  23.3% |
| rsi_14     |   21.6 |
| zscore_20d |   -1.0 |

### NASDAQ 100 / ^NDX (score 28.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | -1.6% |
| ret_20d    | -9.3% |
| ret_60d    | -7.5% |
| ma20_dist  | -3.7% |
| ma50_dist  | -6.2% |
| vol_20d    | 34.0% |
| mdd_60d    | 14.7% |
| rsi_14     |  35.6 |
| zscore_20d |  -1.1 |

### Alphabet Inc. Class A / GOOGL (score 21.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.3% |
| ret_5d     |  +2.6% |
| ret_20d    | -18.8% |
| ret_60d    | -16.4% |
| ma20_dist  |  -7.6% |
| ma50_dist  | -13.1% |
| vol_20d    |  48.9% |
| mdd_60d    |  21.4% |
| rsi_14     |   25.0 |
| zscore_20d |   -0.9 |

### Silver / SI=F (score 16.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.8% |
| ret_5d     |  +3.1% |
| ret_20d    | -13.6% |
| ret_60d    | -22.3% |
| ma20_dist  |  -4.8% |
| ma50_dist  | -14.0% |
| vol_20d    |  44.4% |
| mdd_60d    |  29.3% |
| rsi_14     |   32.0 |
| zscore_20d |   -1.0 |

### Brent Crude Oil / BZ=F (score 14.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.2% |
| ret_5d     | -11.7% |
| ret_20d    | -13.4% |
| ret_60d    |  -0.1% |
| ma20_dist  | -14.5% |
| ma50_dist  | -12.3% |
| vol_20d    |  60.4% |
| mdd_60d    |  22.2% |
| rsi_14     |   32.3 |
| zscore_20d |   -1.9 |

### NVIDIA Corporation / NVDA (score 2.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -5.5% |
| ret_5d     | -18.3% |
| ret_20d    | -26.1% |
| ret_60d    | -24.9% |
| ma20_dist  | -18.1% |
| ma50_dist  | -22.5% |
| vol_20d    |  48.4% |
| mdd_60d    |  29.4% |
| rsi_14     |   19.3 |
| zscore_20d |   -2.5 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| CAC 40 / ^FCHI                      | 109.6279 |           1.3% |                 0.77x |      219.2558 |            2.6% |
| Amazon.com Inc. / AMZN              |  10.6764 |           3.9% |                 0.24x |       21.3529 |            7.9% |
| Euro Stoxx 50 / ^STOXX50E           |  93.7722 |           1.5% |                 0.62x |      187.5444 |            3.0% |
| DAX / ^GDAXI                        | 393.5279 |           1.5% |                 0.61x |      787.0558 |            3.0% |
| Apple Inc. / AAPL                   |   9.4879 |           2.7% |                 0.38x |       18.9757 |            5.4% |
| Hang Seng / ^HSI                    | 398.2227 |           1.6% |                 0.47x |      796.4453 |            3.2% |
| FTSE 100 / ^FTSE                    | 125.2144 |           1.2% |                 0.84x |      250.4287 |            2.3% |
| UnitedHealth Group Inc. / UNH       |  11.4179 |           2.8% |                 0.33x |       22.8357 |            5.6% |
| JPMorgan Chase & Co. / JPM          |   7.9507 |           2.3% |                 0.37x |       15.9014 |            4.6% |
| Soybeans / ZS=F                     |  18.8750 |           1.5% |                 0.61x |       37.7500 |            3.1% |
| Dow Jones Industrial Average / ^DJI | 766.9503 |           1.5% |                 0.50x |     1533.9007 |            2.9% |
| Microsoft Corporation / MSFT        |  17.2936 |           3.2% |                 0.27x |       34.5872 |            6.5% |
| Russell 2000 / ^RUT                 |  49.6421 |           1.8% |                 0.40x |       99.2843 |            3.5% |
| Tesla Inc. / TSLA                   |  18.3064 |           4.8% |                 0.17x |       36.6129 |            9.6% |
| S&P 500 / ^GSPC                     | 116.1793 |           1.5% |                 0.47x |      232.3587 |            3.1% |
| Corn / ZC=F                         |   7.1250 |           1.6% |                 0.74x |       14.2500 |            3.2% |
| Meta Platforms Inc. / META          |  23.8957 |           3.7% |                 0.25x |       47.7914 |            7.5% |
| Gold / GC=F                         |  95.5143 |           2.4% |                 0.41x |      191.0285 |            4.7% |
| Platinum / PL=F                     |  36.2214 |           2.4% |                 0.30x |       72.4429 |            4.7% |
| Wheat / ZW=F                        |  12.5000 |           2.1% |                 0.70x |       25.0000 |            4.2% |
| NASDAQ 100 / ^NDX                   | 726.2093 |           2.6% |                 0.29x |     1452.4185 |            5.2% |
| Alphabet Inc. Class A / GOOGL       |  11.4100 |           4.0% |                 0.20x |       22.8200 |            7.9% |
| Silver / SI=F                       |   1.5734 |           3.1% |                 0.23x |        3.1467 |            6.2% |
| Brent Crude Oil / BZ=F              |   5.6893 |           6.2% |                 0.17x |       11.3786 |           12.4% |
| NVIDIA Corporation / NVDA           |   9.2893 |           5.5% |                 0.21x |       18.5786 |           11.0% |

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

Scoring engine version: **1.0.0** | Git commit: **4ce5958**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
