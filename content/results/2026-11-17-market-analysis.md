+++
title = "Market Analysis 2026-11-17"
date = "2026-11-17T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: ^FCHI (score 83.9)."
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
source_files = ["data/analysis/2026-11-17.json", "data/history/2026-11-17.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "549bd09"
+++

## Market Regime

**Neutral** — 9 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **CAC 40 / ^FCHI** — score 83.9, 20d return +6.2%, RSI14=84. 20d up +6.2%; above MA20 by 3.5%; RSI14=84
- **DAX / ^GDAXI** — score 82.7, 20d return +5.1%, RSI14=65. 20d up +5.1%; above MA20 by 2.3%; RSI14=65
- **FTSE 100 / ^FTSE** — score 81.2, 20d return +1.1%, RSI14=61. 20d up +1.1%; above MA20 by 1.1%; RSI14=61
- **Euro Stoxx 50 / ^STOXX50E** — score 79.1, 20d return +3.3%, RSI14=63. 20d up +3.3%; above MA20 by 2.1%; RSI14=63
- **UnitedHealth Group Inc. / UNH** — score 77.9, 20d return +1.3%, RSI14=51. 20d up +1.3%; above MA20 by 1.0%; RSI14=51

## Upcoming Events

_No scheduled events for covered instruments in the next 7 days._

## Signal History

Compared with the previous available report (**2026-11-16**).

- **New top-5:** UNH
- **Persistent top signals:** ^GDAXI (15 reports), ^FCHI (8 reports), ^STOXX50E (5 reports), ^FTSE (2 reports)
- **Dropped from top-5:** AAPL

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +0 |    -3.0 |
| 7203.T    |     +0 |    +3.6 |
| 8306.T    |     +0 |    -1.5 |
| AAPL      |     -5 |    -2.1 |
| AMZN      |     -6 |   -15.2 |
| BZ=F      |     +1 |    +0.9 |
| CL=F      |     +0 |    +1.2 |
| GC=F      |     +1 |    +5.2 |
| GOOGL     |     -1 |    -6.7 |
| HG=F      |     +0 |    +1.5 |
| JPM       |     -4 |   -10.6 |
| META      |     -5 |   -13.9 |
| MSFT      |     +1 |    +0.3 |
| NG=F      |     +0 |    -7.6 |
| NVDA      |     +0 |    +0.6 |
| PL=F      |     +0 |    +0.0 |
| SI=F      |     +0 |    -2.4 |
| TSLA      |     -3 |    -8.5 |
| UNH       |     +3 |   +13.6 |
| XOM       |     +0 |    +4.5 |
| ZC=F      |     +8 |   +17.6 |
| ZS=F      |     +2 |    -0.6 |
| ZW=F      |     +1 |    +4.5 |
| ^DJI      |     -1 |    -4.2 |
| ^FCHI     |     +2 |    +9.1 |
| ^FTSE     |     +2 |   +10.3 |
| ^GDAXI    |     +0 |    +5.8 |
| ^GSPC     |     -1 |    -5.5 |
| ^HSI      |     +8 |   +16.7 |
| ^N225     |     +0 |    -5.5 |
| ^NDX      |     -2 |    -7.6 |
| ^RUT      |     -1 |    -7.0 |
| ^STOXX50E |     +0 |    +6.4 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Natural Gas / NG=F** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars
- **Copper / HG=F** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                    |
| ---: | ---------------------- | ----: | :------: | --------------- | ---------------------------------------------- |
|    7 | Soybeans / ZS=F        |  63.3 |   Yes    | —               | 20d down -2.0%; above MA20 by 0.5%; RSI14=50   |
|    9 | Corn / ZC=F            |  57.0 |   Yes    | —               | 20d down -3.9%; below MA20 by 0.1%; RSI14=50   |
|   18 | Wheat / ZW=F           |  35.8 |   Yes    | —               | 20d down -10.4%; below MA20 by 2.9%; RSI14=36  |
|   19 | Gold / GC=F            |  31.2 |   Yes    | —               | 20d down -7.4%; below MA20 by 4.2%; RSI14=36   |
|   21 | Brent Crude Oil / BZ=F |  21.2 |   Yes    | —               | 20d down -15.6%; below MA20 by 11.4%; RSI14=27 |
|   23 | Platinum / PL=F        |  18.2 |   Yes    | —               | 20d down -11.6%; below MA20 by 5.0%; RSI14=39  |
|   24 | Silver / SI=F          |   6.1 |   Yes    | —               | 20d down -17.9%; below MA20 by 10.4%; RSI14=30 |
|   28 | Natural Gas / NG=F     |  57.9 |    No    | malformed_input | Suppressed: malformed_input                    |
|   32 | Copper / HG=F          |  27.9 |    No    | malformed_input | Suppressed: malformed_input                    |
|   33 | WTI Crude Oil / CL=F   |  24.9 |    No    | malformed_input | Suppressed: malformed_input                    |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                    |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | ---------------------------------------------- |
|    5 | UnitedHealth Group Inc. / UNH                                                  |  77.9 |   Yes    | —                             | 20d up +1.3%; above MA20 by 1.0%; RSI14=51     |
|    6 | Apple Inc. / AAPL                                                              |  77.0 |   Yes    | —                             | 20d up +2.9%; above MA20 by 1.8%; RSI14=54     |
|   10 | JPMorgan Chase & Co. / JPM                                                     |  56.1 |   Yes    | —                             | 20d up +1.4%; below MA20 by 0.3%; RSI14=52     |
|   12 | Microsoft Corporation / MSFT                                                   |  51.5 |   Yes    | —                             | 20d down -2.9%; below MA20 by 2.0%; RSI14=45   |
|   13 | Amazon.com Inc. / AMZN                                                         |  50.3 |   Yes    | —                             | 20d down -1.8%; above MA20 by 0.3%; RSI14=53   |
|   14 | Tesla Inc. / TSLA                                                              |  49.1 |   Yes    | —                             | 20d up +3.2%; below MA20 by 1.6%; RSI14=40     |
|   17 | Meta Platforms Inc. / META                                                     |  40.9 |   Yes    | —                             | 20d down -11.2%; below MA20 by 1.1%; RSI14=52  |
|   22 | Alphabet Inc. Class A / GOOGL                                                  |  19.1 |   Yes    | —                             | 20d down -17.6%; below MA20 by 5.6%; RSI14=31  |
|   25 | NVIDIA Corporation / NVDA                                                      |   3.6 |   Yes    | —                             | 20d down -28.1%; below MA20 by 20.2%; RSI14=16 |
|   26 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  78.8 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   27 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  73.6 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   29 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  54.5 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   30 | Exxon Mobil Corporation / XOM                                                  |  49.1 |    No    | malformed_input               | Suppressed: malformed_input                    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    1 | CAC 40 / ^FCHI                      |  83.9 |   Yes    | —            | 20d up +6.2%; above MA20 by 3.5%; RSI14=84   |
|    2 | DAX / ^GDAXI                        |  82.7 |   Yes    | —            | 20d up +5.1%; above MA20 by 2.3%; RSI14=65   |
|    3 | FTSE 100 / ^FTSE                    |  81.2 |   Yes    | —            | 20d up +1.1%; above MA20 by 1.1%; RSI14=61   |
|    4 | Euro Stoxx 50 / ^STOXX50E           |  79.1 |   Yes    | —            | 20d up +3.3%; above MA20 by 2.1%; RSI14=63   |
|    8 | Hang Seng / ^HSI                    |  58.5 |   Yes    | —            | 20d down -1.8%; above MA20 by 0.2%; RSI14=60 |
|   11 | Dow Jones Industrial Average / ^DJI |  55.5 |   Yes    | —            | 20d down -0.7%; below MA20 by 1.2%; RSI14=45 |
|   15 | S&P 500 / ^GSPC                     |  45.1 |   Yes    | —            | 20d down -3.6%; below MA20 by 2.4%; RSI14=38 |
|   16 | Russell 2000 / ^RUT                 |  42.7 |   Yes    | —            | 20d up +0.5%; below MA20 by 2.1%; RSI14=43   |
|   20 | NASDAQ 100 / ^NDX                   |  29.1 |   Yes    | —            | 20d down -7.9%; below MA20 by 4.5%; RSI14=34 |
|   31 | Nikkei 225 / ^N225                  |  37.3 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-11-16 |
| 7203.T    | 2026-11-16 |
| 8306.T    | 2026-11-16 |
| AAPL      | 2026-11-16 |
| AMZN      | 2026-11-16 |
| BZ=F      | 2026-11-16 |
| CL=F      | 2026-11-16 |
| GC=F      | 2026-11-16 |
| GOOGL     | 2026-11-16 |
| HG=F      | 2026-11-16 |
| JPM       | 2026-11-16 |
| META      | 2026-11-16 |
| MSFT      | 2026-11-16 |
| NG=F      | 2026-11-16 |
| NVDA      | 2026-11-16 |
| PL=F      | 2026-11-16 |
| SI=F      | 2026-11-16 |
| TSLA      | 2026-11-16 |
| UNH       | 2026-11-16 |
| XOM       | 2026-11-16 |
| ZC=F      | 2026-11-16 |
| ZS=F      | 2026-11-16 |
| ZW=F      | 2026-11-16 |
| ^DJI      | 2026-11-16 |
| ^FCHI     | 2026-11-16 |
| ^FTSE     | 2026-11-16 |
| ^GDAXI    | 2026-11-16 |
| ^GSPC     | 2026-11-16 |
| ^HSI      | 2026-11-16 |
| ^N225     | 2026-11-16 |
| ^NDX      | 2026-11-16 |
| ^RUT      | 2026-11-16 |
| ^STOXX50E | 2026-11-16 |

## Symbol Details

### CAC 40 / ^FCHI (score 83.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | +1.4% |
| ret_20d    | +6.2% |
| ret_60d    | -1.2% |
| ma20_dist  | +3.5% |
| ma50_dist  | +4.0% |
| vol_20d    | 12.0% |
| mdd_60d    |  8.7% |
| rsi_14     |  83.8 |
| zscore_20d |   1.4 |

### DAX / ^GDAXI (score 82.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | +1.3% |
| ret_20d    | +5.1% |
| ret_60d    | +1.9% |
| ma20_dist  | +2.3% |
| ma50_dist  | +3.8% |
| vol_20d    | 16.1% |
| mdd_60d    |  6.6% |
| rsi_14     |  65.4 |
| zscore_20d |   1.2 |

### FTSE 100 / ^FTSE (score 81.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | +0.9% |
| ret_20d    | +1.1% |
| ret_60d    | +0.6% |
| ma20_dist  | +1.1% |
| ma50_dist  | +1.7% |
| vol_20d    | 10.7% |
| mdd_60d    |  4.2% |
| rsi_14     |  61.4 |
| zscore_20d |   1.7 |

### Euro Stoxx 50 / ^STOXX50E (score 79.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | +0.9% |
| ret_20d    | +3.3% |
| ret_60d    | -1.5% |
| ma20_dist  | +2.1% |
| ma50_dist  | +1.8% |
| vol_20d    | 15.9% |
| mdd_60d    |  6.4% |
| rsi_14     |  63.3 |
| zscore_20d |   1.2 |

### UnitedHealth Group Inc. / UNH (score 77.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | +3.6% |
| ret_20d    | +1.3% |
| ret_60d    | +6.3% |
| ma20_dist  | +1.0% |
| ma50_dist  | +5.2% |
| vol_20d    | 23.6% |
| mdd_60d    |  8.4% |
| rsi_14     |  51.3 |
| zscore_20d |   0.5 |

### Apple Inc. / AAPL (score 77.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.0% |
| ret_5d     |  +0.7% |
| ret_20d    |  +2.9% |
| ret_60d    | +14.0% |
| ma20_dist  |  +1.8% |
| ma50_dist  |  +3.9% |
| vol_20d    |  27.4% |
| mdd_60d    |   4.9% |
| rsi_14     |   54.1 |
| zscore_20d |    1.1 |

### Soybeans / ZS=F (score 63.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.1% |
| ret_5d     | +4.0% |
| ret_20d    | -2.0% |
| ret_60d    | -0.4% |
| ma20_dist  | +0.5% |
| ma50_dist  | -3.0% |
| vol_20d    | 17.3% |
| mdd_60d    | 11.1% |
| rsi_14     |  49.9 |
| zscore_20d |   0.3 |

### Hang Seng / ^HSI (score 58.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | -2.8% |
| ret_20d    | -1.8% |
| ret_60d    | -7.6% |
| ma20_dist  | +0.2% |
| ma50_dist  | -2.1% |
| vol_20d    | 22.2% |
| mdd_60d    | 11.8% |
| rsi_14     |  60.1 |
| zscore_20d |   0.1 |

### Corn / ZC=F (score 57.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.7% |
| ret_5d     |  +2.2% |
| ret_20d    |  -3.9% |
| ret_60d    | -13.8% |
| ma20_dist  |  -0.1% |
| ma50_dist  |  -7.4% |
| vol_20d    |  13.9% |
| mdd_60d    |  19.1% |
| rsi_14     |   50.0 |
| zscore_20d |   -0.1 |

### JPMorgan Chase & Co. / JPM (score 56.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.3% |
| ret_5d     | -1.1% |
| ret_20d    | +1.4% |
| ret_60d    | -3.8% |
| ma20_dist  | -0.3% |
| ma50_dist  | -0.3% |
| vol_20d    | 27.2% |
| mdd_60d    |  9.1% |
| rsi_14     |  51.7 |
| zscore_20d |  -0.2 |

### Dow Jones Industrial Average / ^DJI (score 55.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.4% |
| ret_5d     | -1.5% |
| ret_20d    | -0.7% |
| ret_60d    | -3.1% |
| ma20_dist  | -1.2% |
| ma50_dist  | -0.6% |
| vol_20d    | 20.4% |
| mdd_60d    |  5.2% |
| rsi_14     |  44.8 |
| zscore_20d |  -1.3 |

### Microsoft Corporation / MSFT (score 51.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.1% |
| ret_5d     | -5.0% |
| ret_20d    | -2.9% |
| ret_60d    | +7.2% |
| ma20_dist  | -2.0% |
| ma50_dist  | -0.3% |
| vol_20d    | 36.0% |
| mdd_60d    |  6.8% |
| rsi_14     |  45.4 |
| zscore_20d |  -1.1 |

### Amazon.com Inc. / AMZN (score 50.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -3.3% |
| ret_5d     | -3.4% |
| ret_20d    | -1.8% |
| ret_60d    | -0.3% |
| ma20_dist  | +0.3% |
| ma50_dist  | +1.2% |
| vol_20d    | 39.1% |
| mdd_60d    |  9.8% |
| rsi_14     |  53.1 |
| zscore_20d |   0.1 |

### Tesla Inc. / TSLA (score 49.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.7% |
| ret_5d     | +0.4% |
| ret_20d    | +3.2% |
| ret_60d    | +4.7% |
| ma20_dist  | -1.6% |
| ma50_dist  | +1.2% |
| vol_20d    | 58.2% |
| mdd_60d    | 15.7% |
| rsi_14     |  40.3 |
| zscore_20d |  -0.4 |

### S&P 500 / ^GSPC (score 45.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.9% |
| ret_5d     | -1.8% |
| ret_20d    | -3.6% |
| ret_60d    | -3.4% |
| ma20_dist  | -2.4% |
| ma50_dist  | -3.2% |
| vol_20d    | 22.2% |
| mdd_60d    |  5.9% |
| rsi_14     |  37.6 |
| zscore_20d |  -1.6 |

### Russell 2000 / ^RUT (score 42.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.7% |
| ret_5d     | -3.4% |
| ret_20d    | +0.5% |
| ret_60d    | -9.1% |
| ma20_dist  | -2.1% |
| ma50_dist  | -2.7% |
| vol_20d    | 24.7% |
| mdd_60d    |  9.7% |
| rsi_14     |  42.8 |
| zscore_20d |  -1.6 |

### Meta Platforms Inc. / META (score 40.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.4% |
| ret_5d     |  -2.3% |
| ret_20d    | -11.2% |
| ret_60d    | +14.0% |
| ma20_dist  |  -1.1% |
| ma50_dist  |  -7.9% |
| vol_20d    |  40.6% |
| mdd_60d    |  22.2% |
| rsi_14     |   51.8 |
| zscore_20d |   -0.3 |

### Wheat / ZW=F (score 35.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.1% |
| ret_5d     |  -0.2% |
| ret_20d    | -10.4% |
| ret_60d    | -17.6% |
| ma20_dist  |  -2.9% |
| ma50_dist  | -11.1% |
| vol_20d    |  18.0% |
| mdd_60d    |  23.8% |
| rsi_14     |   35.7 |
| zscore_20d |   -1.2 |

### Gold / GC=F (score 31.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.9% |
| ret_5d     |  -6.4% |
| ret_20d    |  -7.4% |
| ret_60d    | -18.0% |
| ma20_dist  |  -4.2% |
| ma50_dist  |  -7.6% |
| vol_20d    |  24.7% |
| mdd_60d    |  17.9% |
| rsi_14     |   36.0 |
| zscore_20d |   -1.9 |

### NASDAQ 100 / ^NDX (score 29.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.7% |
| ret_5d     | -2.5% |
| ret_20d    | -7.9% |
| ret_60d    | -7.2% |
| ma20_dist  | -4.5% |
| ma50_dist  | -7.7% |
| vol_20d    | 34.6% |
| mdd_60d    | 14.7% |
| rsi_14     |  33.6 |
| zscore_20d |  -1.4 |

### Brent Crude Oil / BZ=F (score 21.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -3.5% |
| ret_5d     |  -0.1% |
| ret_20d    | -15.6% |
| ret_60d    |  +0.3% |
| ma20_dist  | -11.4% |
| ma50_dist  | -11.3% |
| vol_20d    |  61.2% |
| mdd_60d    |  22.2% |
| rsi_14     |   26.7 |
| zscore_20d |   -1.2 |

### Alphabet Inc. Class A / GOOGL (score 19.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -4.1% |
| ret_5d     |  -1.5% |
| ret_20d    | -17.6% |
| ret_60d    | -17.7% |
| ma20_dist  |  -5.6% |
| ma50_dist  | -13.3% |
| vol_20d    |  51.1% |
| mdd_60d    |  21.4% |
| rsi_14     |   31.4 |
| zscore_20d |   -0.8 |

### Platinum / PL=F (score 18.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.7% |
| ret_5d     |  -7.3% |
| ret_20d    | -11.6% |
| ret_60d    | -23.0% |
| ma20_dist  |  -5.0% |
| ma50_dist  | -12.0% |
| vol_20d    |  32.8% |
| mdd_60d    |  25.2% |
| rsi_14     |   39.5 |
| zscore_20d |   -1.4 |

### Silver / SI=F (score 6.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -4.6% |
| ret_5d     | -11.0% |
| ret_20d    | -17.9% |
| ret_60d    | -31.7% |
| ma20_dist  | -10.4% |
| ma50_dist  | -19.5% |
| vol_20d    |  42.9% |
| mdd_60d    |  32.6% |
| rsi_14     |   30.4 |
| zscore_20d |   -2.1 |

### NVIDIA Corporation / NVDA (score 3.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -4.1% |
| ret_5d     | -12.6% |
| ret_20d    | -28.1% |
| ret_60d    | -27.2% |
| ma20_dist  | -20.2% |
| ma50_dist  | -26.7% |
| vol_20d    |  51.3% |
| mdd_60d    |  34.7% |
| rsi_14     |   16.0 |
| zscore_20d |   -1.9 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| CAC 40 / ^FCHI                      |  97.2293 |           1.2% |                 0.83x |      194.4586 |            2.3% |
| DAX / ^GDAXI                        | 371.1522 |           1.4% |                 0.62x |      742.3044 |            2.8% |
| FTSE 100 / ^FTSE                    | 118.2001 |           1.1% |                 0.93x |      236.4003 |            2.2% |
| Euro Stoxx 50 / ^STOXX50E           |  84.1100 |           1.3% |                 0.63x |      168.2201 |            2.6% |
| UnitedHealth Group Inc. / UNH       |  10.9807 |           2.7% |                 0.42x |       21.9614 |            5.3% |
| Apple Inc. / AAPL                   |   9.4801 |           2.7% |                 0.36x |       18.9603 |            5.4% |
| Soybeans / ZS=F                     |  17.9821 |           1.5% |                 0.58x |       35.9643 |            2.9% |
| Hang Seng / ^HSI                    | 366.1489 |           1.5% |                 0.45x |      732.2977 |            3.1% |
| Corn / ZC=F                         |   7.2679 |           1.6% |                 0.72x |       14.5357 |            3.2% |
| JPMorgan Chase & Co. / JPM          |   8.2364 |           2.4% |                 0.37x |       16.4729 |            4.9% |
| Dow Jones Industrial Average / ^DJI | 795.0767 |           1.5% |                 0.49x |     1590.1535 |            3.1% |
| Microsoft Corporation / MSFT        |  17.8936 |           3.5% |                 0.28x |       35.7872 |            6.9% |
| Amazon.com Inc. / AMZN              |  11.0314 |           4.3% |                 0.26x |       22.0629 |            8.6% |
| Tesla Inc. / TSLA                   |  18.0029 |           4.7% |                 0.17x |       36.0057 |            9.5% |
| S&P 500 / ^GSPC                     | 130.6793 |           1.8% |                 0.45x |      261.3586 |            3.5% |
| Russell 2000 / ^RUT                 |  53.8986 |           2.0% |                 0.40x |      107.7971 |            3.9% |
| Meta Platforms Inc. / META          |  21.6871 |           3.5% |                 0.25x |       43.3743 |            6.9% |
| Wheat / ZW=F                        |  14.1250 |           2.4% |                 0.56x |       28.2500 |            4.8% |
| Gold / GC=F                         |  97.6429 |           2.5% |                 0.41x |      195.2857 |            5.1% |
| NASDAQ 100 / ^NDX                   | 779.4601 |           2.9% |                 0.29x |     1558.9202 |            5.7% |
| Brent Crude Oil / BZ=F              |   5.6193 |           6.1% |                 0.16x |       11.2386 |           12.2% |
| Alphabet Inc. Class A / GOOGL       |  12.3200 |           4.3% |                 0.20x |       24.6400 |            8.7% |
| Platinum / PL=F                     |  32.9571 |           2.3% |                 0.30x |       65.9143 |            4.6% |
| Silver / SI=F                       |   1.7190 |           3.7% |                 0.23x |        3.4380 |            7.3% |
| NVIDIA Corporation / NVDA           |  11.3286 |           7.3% |                 0.19x |       22.6571 |           14.5% |

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

Scoring engine version: **1.0.0** | Git commit: **549bd09**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
