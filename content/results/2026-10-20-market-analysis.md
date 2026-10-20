+++
title = "Market Analysis 2026-10-20"
date = "2026-10-20T00:00:00+00:00"
draft = false
summary = "Bearish market: 25 reliable instruments. Top signal: MSFT (score 73.6)."
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
source_files = ["data/analysis/2026-10-20.json", "data/history/2026-10-20.json"]
market_regime = "Bearish"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "d6ffae1"
+++

## Market Regime

**Bearish** — 8 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Microsoft Corporation / MSFT** — score 73.6, 20d return +6.4%, RSI14=65. 20d up +6.4%; above MA20 by 2.2%; RSI14=65
- **Brent Crude Oil / BZ=F** — score 71.2, 20d return +9.2%, RSI14=71. 20d up +9.2%; above MA20 by 5.2%; RSI14=71
- **Amazon.com Inc. / AMZN** — score 67.0, 20d return +1.5%, RSI14=64. 20d up +1.5%; above MA20 by 3.6%; RSI14=64
- **UnitedHealth Group Inc. / UNH** — score 67.0, 20d return +7.8%, RSI14=70. 20d up +7.8%; above MA20 by 7.1%; RSI14=70
- **Apple Inc. / AAPL** — score 65.8, 20d return +1.2%, RSI14=72. 20d up +1.2%; above MA20 by 1.6%; RSI14=72

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                 | Applies To |
| ---------- | --------------------- | ---------- |
| 2026-10-21 | TSLA earnings release | TSLA       |

## Signal History

Compared with the previous available report (**2026-10-19**).

- **New top-5:** AMZN, UNH
- **Persistent top signals:** MSFT (17 reports), AAPL (2 reports), BZ=F (2 reports)
- **Dropped from top-5:** ^FTSE, ^GDAXI

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     -1 |    -5.5 |
| 7203.T    |     -1 |    -3.3 |
| 8306.T    |     +1 |    +3.6 |
| AAPL      |     -1 |    -2.1 |
| AMZN      |    +13 |   +29.4 |
| BZ=F      |     -1 |    -3.6 |
| CL=F      |     +2 |    +3.6 |
| GC=F      |     -2 |    -4.8 |
| GOOGL     |     +6 |   +14.6 |
| HG=F      |     +1 |    -1.2 |
| JPM       |     -7 |   -17.0 |
| META      |     -6 |   -10.6 |
| MSFT      |     +2 |    +5.2 |
| NG=F      |     -1 |    -8.2 |
| NVDA      |     +4 |   +13.9 |
| PL=F      |     +1 |    +4.2 |
| SI=F      |     +0 |    -1.2 |
| TSLA      |     +9 |   +24.6 |
| UNH       |     +3 |    +9.1 |
| XOM       |     +0 |    -4.8 |
| ZC=F      |     -4 |    -8.2 |
| ZS=F      |     -4 |    -7.9 |
| ZW=F      |     -1 |    -5.5 |
| ^DJI      |     +0 |    +1.5 |
| ^FCHI     |     -5 |    -8.2 |
| ^FTSE     |     -5 |    -8.8 |
| ^GDAXI    |     -5 |   -15.2 |
| ^GSPC     |     +2 |    +7.6 |
| ^HSI      |     +0 |    +0.6 |
| ^N225     |     -1 |    -7.3 |
| ^NDX      |     +6 |   +14.2 |
| ^RUT      |     +0 |    +6.1 |
| ^STOXX50E |     -5 |   -14.8 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Exxon Mobil Corporation / XOM** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **Natural Gas / NG=F** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Nikkei 225 / ^N225** — missing_bars

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|    2 | Brent Crude Oil / BZ=F |  71.2 |   Yes    | —               | 20d up +9.2%; above MA20 by 5.2%; RSI14=71    |
|   17 | Gold / GC=F            |  37.6 |   Yes    | —               | 20d down -5.1%; below MA20 by 1.0%; RSI14=48  |
|   18 | Soybeans / ZS=F        |  36.7 |   Yes    | —               | 20d down -5.6%; below MA20 by 2.9%; RSI14=28  |
|   22 | Platinum / PL=F        |  27.0 |   Yes    | —               | 20d down -8.9%; below MA20 by 2.8%; RSI14=44  |
|   23 | Wheat / ZW=F           |  17.6 |   Yes    | —               | 20d down -9.8%; below MA20 by 4.3%; RSI14=32  |
|   24 | Corn / ZC=F            |  15.4 |   Yes    | —               | 20d down -14.0%; below MA20 by 6.8%; RSI14=18 |
|   25 | Silver / SI=F          |  12.4 |   Yes    | —               | 20d down -13.4%; below MA20 by 5.7%; RSI14=36 |
|   27 | WTI Crude Oil / CL=F   |  77.3 |    No    | malformed_input | Suppressed: malformed_input                   |
|   30 | Copper / HG=F          |  50.6 |    No    | malformed_input | Suppressed: malformed_input                   |
|   31 | Natural Gas / NG=F     |  44.2 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    1 | Microsoft Corporation / MSFT                                                   |  73.6 |   Yes    | —                             | 20d up +6.4%; above MA20 by 2.2%; RSI14=65   |
|    3 | Amazon.com Inc. / AMZN                                                         |  67.0 |   Yes    | —                             | 20d up +1.5%; above MA20 by 3.6%; RSI14=64   |
|    4 | UnitedHealth Group Inc. / UNH                                                  |  67.0 |   Yes    | —                             | 20d up +7.8%; above MA20 by 7.1%; RSI14=70   |
|    5 | Apple Inc. / AAPL                                                              |  65.8 |   Yes    | —                             | 20d up +1.2%; above MA20 by 1.6%; RSI14=72   |
|    9 | Tesla Inc. / TSLA                                                              |  57.9 |   Yes    | —                             | 20d down -1.9%; below MA20 by 0.5%; RSI14=59 |
|   11 | Alphabet Inc. Class A / GOOGL                                                  |  51.8 |   Yes    | —                             | 20d down -3.0%; below MA20 by 0.5%; RSI14=53 |
|   15 | JPMorgan Chase & Co. / JPM                                                     |  39.4 |   Yes    | —                             | 20d down -4.8%; below MA20 by 0.1%; RSI14=50 |
|   19 | Meta Platforms Inc. / META                                                     |  34.9 |   Yes    | —                             | 20d down -4.8%; below MA20 by 3.9%; RSI14=39 |
|   20 | NVIDIA Corporation / NVDA                                                      |  33.9 |   Yes    | —                             | 20d down -4.5%; below MA20 by 4.6%; RSI14=39 |
|   26 | Exxon Mobil Corporation / XOM                                                  |  80.3 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   28 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  74.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   29 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  70.9 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   32 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  37.3 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    6 | Dow Jones Industrial Average / ^DJI |  64.8 |   Yes    | —            | 20d down -0.2%; above MA20 by 0.9%; RSI14=60 |
|    7 | FTSE 100 / ^FTSE                    |  64.5 |   Yes    | —            | 20d up +0.2%; above MA20 by 1.3%; RSI14=56   |
|    8 | S&P 500 / ^GSPC                     |  61.2 |   Yes    | —            | 20d down -1.0%; below MA20 by 0.6%; RSI14=52 |
|   10 | DAX / ^GDAXI                        |  52.1 |   Yes    | —            | 20d down -1.0%; above MA20 by 0.1%; RSI14=49 |
|   12 | Hang Seng / ^HSI                    |  47.0 |   Yes    | —            | 20d down -1.7%; below MA20 by 0.9%; RSI14=44 |
|   13 | NASDAQ 100 / ^NDX                   |  43.0 |   Yes    | —            | 20d down -3.1%; below MA20 by 3.1%; RSI14=39 |
|   14 | Euro Stoxx 50 / ^STOXX50E           |  40.0 |   Yes    | —            | 20d down -2.7%; below MA20 by 1.3%; RSI14=36 |
|   16 | CAC 40 / ^FCHI                      |  38.5 |   Yes    | —            | 20d down -3.3%; below MA20 by 0.7%; RSI14=40 |
|   21 | Russell 2000 / ^RUT                 |  29.4 |   Yes    | —            | 20d down -5.1%; below MA20 by 2.7%; RSI14=37 |
|   33 | Nikkei 225 / ^N225                  |  35.5 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-10-19 |
| 7203.T    | 2026-10-19 |
| 8306.T    | 2026-10-19 |
| AAPL      | 2026-10-19 |
| AMZN      | 2026-10-19 |
| BZ=F      | 2026-10-19 |
| CL=F      | 2026-10-19 |
| GC=F      | 2026-10-19 |
| GOOGL     | 2026-10-19 |
| HG=F      | 2026-10-19 |
| JPM       | 2026-10-19 |
| META      | 2026-10-19 |
| MSFT      | 2026-10-19 |
| NG=F      | 2026-10-19 |
| NVDA      | 2026-10-19 |
| PL=F      | 2026-10-19 |
| SI=F      | 2026-10-19 |
| TSLA      | 2026-10-19 |
| UNH       | 2026-10-19 |
| XOM       | 2026-10-19 |
| ZC=F      | 2026-10-19 |
| ZS=F      | 2026-10-19 |
| ZW=F      | 2026-10-19 |
| ^DJI      | 2026-10-19 |
| ^FCHI     | 2026-10-19 |
| ^FTSE     | 2026-10-19 |
| ^GDAXI    | 2026-10-19 |
| ^GSPC     | 2026-10-19 |
| ^HSI      | 2026-10-16 |
| ^N225     | 2026-10-19 |
| ^NDX      | 2026-10-19 |
| ^RUT      | 2026-10-19 |
| ^STOXX50E | 2026-10-19 |

## Symbol Details

### Microsoft Corporation / MSFT (score 73.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.8% |
| ret_5d     |  -1.4% |
| ret_20d    |  +6.4% |
| ret_60d    | +40.0% |
| ma20_dist  |  +2.2% |
| ma50_dist  |  +5.4% |
| vol_20d    |  21.4% |
| mdd_60d    |   5.1% |
| rsi_14     |   65.5 |
| zscore_20d |    0.8 |

### Brent Crude Oil / BZ=F (score 71.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.3% |
| ret_5d     |  +2.7% |
| ret_20d    |  +9.2% |
| ret_60d    | +23.0% |
| ma20_dist  |  +5.2% |
| ma50_dist  | +10.4% |
| vol_20d    |  31.0% |
| mdd_60d    |  11.9% |
| rsi_14     |   70.5 |
| zscore_20d |    1.9 |

### Amazon.com Inc. / AMZN (score 67.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +5.0% |
| ret_5d     |  +1.1% |
| ret_20d    |  +1.5% |
| ret_60d    | +13.1% |
| ma20_dist  |  +3.6% |
| ma50_dist  |  +2.2% |
| vol_20d    |  28.9% |
| mdd_60d    |  13.4% |
| rsi_14     |   64.1 |
| zscore_20d |    1.8 |

### UnitedHealth Group Inc. / UNH (score 67.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.4% |
| ret_5d     | +7.5% |
| ret_20d    | +7.8% |
| ret_60d    | -3.3% |
| ma20_dist  | +7.1% |
| ma50_dist  | +5.3% |
| vol_20d    | 25.8% |
| mdd_60d    | 14.8% |
| rsi_14     |  69.9 |
| zscore_20d |   2.2 |

### Apple Inc. / AAPL (score 65.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | +0.6% |
| ret_20d    | +1.2% |
| ret_60d    | +3.1% |
| ma20_dist  | +1.6% |
| ma50_dist  | +5.1% |
| vol_20d    | 15.6% |
| mdd_60d    | 11.0% |
| rsi_14     |  71.8 |
| zscore_20d |   1.3 |

### Dow Jones Industrial Average / ^DJI (score 64.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | +0.2% |
| ret_20d    | -0.2% |
| ret_60d    | +0.0% |
| ma20_dist  | +0.9% |
| ma50_dist  | -0.9% |
| vol_20d    |  8.7% |
| mdd_60d    |  6.3% |
| rsi_14     |  60.0 |
| zscore_20d |   1.3 |

### FTSE 100 / ^FTSE (score 64.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.1% |
| ret_5d     | +1.0% |
| ret_20d    | +0.2% |
| ret_60d    | +0.3% |
| ma20_dist  | +1.3% |
| ma50_dist  | +0.5% |
| vol_20d    | 10.9% |
| mdd_60d    |  4.4% |
| rsi_14     |  56.5 |
| zscore_20d |   1.1 |

### S&P 500 / ^GSPC (score 61.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | -1.5% |
| ret_20d    | -1.0% |
| ret_60d    | +3.8% |
| ma20_dist  | -0.6% |
| ma50_dist  | -0.2% |
| vol_20d    |  8.8% |
| mdd_60d    |  3.2% |
| rsi_14     |  51.9 |
| zscore_20d |  -0.8 |

### Tesla Inc. / TSLA (score 57.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +3.8% |
| ret_5d     |  -2.6% |
| ret_20d    |  -1.9% |
| ret_60d    | +17.6% |
| ma20_dist  |  -0.5% |
| ma50_dist  |  +2.2% |
| vol_20d    |  31.8% |
| mdd_60d    |   7.3% |
| rsi_14     |   59.1 |
| zscore_20d |   -0.2 |

### DAX / ^GDAXI (score 52.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.2% |
| ret_5d     | +0.2% |
| ret_20d    | -1.0% |
| ret_60d    | -0.2% |
| ma20_dist  | +0.1% |
| ma50_dist  | -1.5% |
| vol_20d    | 12.4% |
| mdd_60d    |  6.6% |
| rsi_14     |  48.6 |
| zscore_20d |   0.2 |

### Alphabet Inc. Class A / GOOGL (score 51.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | -2.4% |
| ret_20d    | -3.0% |
| ret_60d    | +7.6% |
| ma20_dist  | -0.5% |
| ma50_dist  | -0.0% |
| vol_20d    | 21.6% |
| mdd_60d    | 12.4% |
| rsi_14     |  53.3 |
| zscore_20d |  -0.4 |

### Hang Seng / ^HSI (score 47.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | -0.1% |
| ret_20d    | -1.7% |
| ret_60d    | -4.1% |
| ma20_dist  | -0.9% |
| ma50_dist  | -3.2% |
| vol_20d    | 15.6% |
| mdd_60d    |  8.5% |
| rsi_14     |  44.1 |
| zscore_20d |  -0.7 |

### NASDAQ 100 / ^NDX (score 43.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.2% |
| ret_5d     | -3.7% |
| ret_20d    | -3.1% |
| ret_60d    | +5.0% |
| ma20_dist  | -3.1% |
| ma50_dist  | -1.1% |
| vol_20d    | 15.5% |
| mdd_60d    |  6.5% |
| rsi_14     |  38.7 |
| zscore_20d |  -1.9 |

### Euro Stoxx 50 / ^STOXX50E (score 40.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | -0.9% |
| ret_20d    | -2.7% |
| ret_60d    | -2.2% |
| ma20_dist  | -1.3% |
| ma50_dist  | -3.0% |
| vol_20d    | 11.2% |
| mdd_60d    |  6.5% |
| rsi_14     |  36.2 |
| zscore_20d |  -1.4 |

### JPMorgan Chase & Co. / JPM (score 39.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.8% |
| ret_5d     | -0.2% |
| ret_20d    | -4.8% |
| ret_60d    | -5.6% |
| ma20_dist  | -0.1% |
| ma50_dist  | -3.9% |
| vol_20d    | 18.4% |
| mdd_60d    |  9.9% |
| rsi_14     |  50.3 |
| zscore_20d |  -0.1 |

### CAC 40 / ^FCHI (score 38.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.1% |
| ret_5d     | +0.4% |
| ret_20d    | -3.3% |
| ret_60d    | -6.4% |
| ma20_dist  | -0.7% |
| ma50_dist  | -3.8% |
| vol_20d    | 11.3% |
| mdd_60d    | 11.4% |
| rsi_14     |  39.7 |
| zscore_20d |  -0.5 |

### Gold / GC=F (score 37.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | -0.7% |
| ret_20d    | -5.1% |
| ret_60d    | +1.5% |
| ma20_dist  | -1.0% |
| ma50_dist  | -4.9% |
| vol_20d    | 17.6% |
| mdd_60d    | 12.7% |
| rsi_14     |  47.7 |
| zscore_20d |  -0.6 |

### Soybeans / ZS=F (score 36.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | -2.7% |
| ret_20d    | -5.6% |
| ret_60d    | +6.4% |
| ma20_dist  | -2.9% |
| ma50_dist  | -1.4% |
| vol_20d    | 12.1% |
| mdd_60d    |  5.6% |
| rsi_14     |  28.5 |
| zscore_20d |  -1.9 |

### Meta Platforms Inc. / META (score 34.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.5% |
| ret_5d     |  -5.1% |
| ret_20d    |  -4.8% |
| ret_60d    | +18.5% |
| ma20_dist  |  -3.9% |
| ma50_dist  |  +7.3% |
| vol_20d    |  39.1% |
| mdd_60d    |   9.3% |
| rsi_14     |   39.2 |
| zscore_20d |   -1.7 |

### NVIDIA Corporation / NVDA (score 33.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.4% |
| ret_5d     | -4.1% |
| ret_20d    | -4.5% |
| ret_60d    | +5.0% |
| ma20_dist  | -4.6% |
| ma50_dist  | -2.6% |
| vol_20d    | 23.1% |
| mdd_60d    | 10.5% |
| rsi_14     |  38.6 |
| zscore_20d |  -1.6 |

### Russell 2000 / ^RUT (score 29.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | -2.4% |
| ret_20d    | -5.1% |
| ret_60d    | -6.9% |
| ma20_dist  | -2.7% |
| ma50_dist  | -6.0% |
| vol_20d    | 13.8% |
| mdd_60d    | 11.3% |
| rsi_14     |  36.6 |
| zscore_20d |  -1.8 |

### Platinum / PL=F (score 27.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.0% |
| ret_5d     | -2.4% |
| ret_20d    | -8.9% |
| ret_60d    | -0.8% |
| ma20_dist  | -2.8% |
| ma50_dist  | -6.9% |
| vol_20d    | 31.2% |
| mdd_60d    | 16.4% |
| rsi_14     |  43.6 |
| zscore_20d |  -0.9 |

### Wheat / ZW=F (score 17.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | -2.5% |
| ret_20d    | -9.8% |
| ret_60d    | -0.8% |
| ma20_dist  | -4.3% |
| ma50_dist  | -6.4% |
| vol_20d    | 18.8% |
| mdd_60d    | 14.6% |
| rsi_14     |  32.1 |
| zscore_20d |  -1.8 |

### Corn / ZC=F (score 15.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.5% |
| ret_5d     |  -3.3% |
| ret_20d    | -14.0% |
| ret_60d    |  +4.0% |
| ma20_dist  |  -6.8% |
| ma50_dist  |  -6.9% |
| vol_20d    |  21.9% |
| mdd_60d    |  14.0% |
| rsi_14     |   18.0 |
| zscore_20d |   -1.7 |

### Silver / SI=F (score 12.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.0% |
| ret_5d     |  -5.3% |
| ret_20d    | -13.4% |
| ret_60d    |  -3.1% |
| ma20_dist  |  -5.7% |
| ma50_dist  | -10.8% |
| vol_20d    |  33.3% |
| mdd_60d    |  20.0% |
| rsi_14     |   36.2 |
| zscore_20d |   -1.3 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Microsoft Corporation / MSFT        |  11.4743 |           2.2% |                 0.47x |       22.9486 |            4.3% |
| Brent Crude Oil / BZ=F              |   3.8529 |           3.5% |                 0.32x |        7.7057 |            7.0% |
| Amazon.com Inc. / AMZN              |   6.6179 |           2.5% |                 0.35x |       13.2357 |            5.0% |
| UnitedHealth Group Inc. / UNH       |  12.8714 |           3.2% |                 0.39x |       25.7429 |            6.3% |
| Apple Inc. / AAPL                   |   6.4171 |           1.9% |                 0.64x |       12.8343 |            3.7% |
| Dow Jones Industrial Average / ^DJI | 513.4568 |           1.0% |                 1.15x |     1026.9135 |            2.0% |
| FTSE 100 / ^FTSE                    | 122.9213 |           1.1% |                 0.92x |      245.8426 |            2.3% |
| S&P 500 / ^GSPC                     |  71.2321 |           0.9% |                 1.14x |      142.4643 |            1.9% |
| Tesla Inc. / TSLA                   |  11.4314 |           3.1% |                 0.31x |       22.8629 |            6.2% |
| DAX / ^GDAXI                        | 310.7697 |           1.2% |                 0.81x |      621.5393 |            2.5% |
| Alphabet Inc. Class A / GOOGL       |   9.0443 |           2.6% |                 0.46x |       18.0886 |            5.3% |
| Hang Seng / ^HSI                    | 344.0658 |           1.4% |                 0.64x |      688.1317 |            2.8% |
| NASDAQ 100 / ^NDX                   | 443.0873 |           1.5% |                 0.65x |      886.1747 |            3.0% |
| Euro Stoxx 50 / ^STOXX50E           |  75.5379 |           1.2% |                 0.89x |      151.0758 |            2.5% |
| JPMorgan Chase & Co. / JPM          |   6.2889 |           1.9% |                 0.54x |       12.5778 |            3.8% |
| CAC 40 / ^FCHI                      |  93.3300 |           1.2% |                 0.89x |      186.6599 |            2.4% |
| Gold / GC=F                         |  71.7571 |           1.7% |                 0.57x |      143.5142 |            3.4% |
| Soybeans / ZS=F                     |  18.8750 |           1.5% |                 0.83x |       37.7500 |            3.0% |
| Meta Platforms Inc. / META          |  21.4086 |           3.0% |                 0.26x |       42.8171 |            6.1% |
| NVIDIA Corporation / NVDA           |   5.7400 |           2.6% |                 0.43x |       11.4800 |            5.3% |
| Russell 2000 / ^RUT                 |  36.4557 |           1.3% |                 0.72x |       72.9114 |            2.7% |
| Platinum / PL=F                     |  31.4857 |           1.9% |                 0.32x |       62.9715 |            3.8% |
| Wheat / ZW=F                        |  16.0357 |           2.4% |                 0.53x |       32.0714 |            4.9% |
| Corn / ZC=F                         |  11.5714 |           2.5% |                 0.46x |       23.1429 |            5.0% |
| Silver / SI=F                       |   1.1941 |           2.1% |                 0.30x |        2.3883 |            4.2% |

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

Scoring engine version: **1.0.0** | Git commit: **d6ffae1**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
