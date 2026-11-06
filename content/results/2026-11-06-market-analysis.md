+++
title = "Market Analysis 2026-11-06"
date = "2026-11-06T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: ^GDAXI (score 80.6)."
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
source_files = ["data/analysis/2026-11-06.json", "data/history/2026-11-06.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "521c388"
+++

## Market Regime

**Neutral** — 10 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **DAX / ^GDAXI** — score 80.6, 20d return +6.1%, RSI14=61. 20d up +6.1%; above MA20 by 2.8%; RSI14=61
- **CAC 40 / ^FCHI** — score 78.5, 20d return +6.2%, RSI14=65. 20d up +6.2%; above MA20 by 3.6%; RSI14=65
- **Hang Seng / ^HSI** — score 77.0, 20d return +2.8%, RSI14=60. 20d up +2.8%; above MA20 by 4.6%; RSI14=60
- **FTSE 100 / ^FTSE** — score 72.4, 20d return +3.3%, RSI14=44. 20d up +3.3%; above MA20 by 0.5%; RSI14=44
- **Euro Stoxx 50 / ^STOXX50E** — score 69.1, 20d return +1.7%, RSI14=52. 20d up +1.7%; above MA20 by 1.0%; RSI14=52

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                   | Applies To |
| ---------- | ----------------------- | ---------- |
| 2026-11-13 | 8306.T earnings release | 8306.T     |

## Signal History

Compared with the previous available report (**2026-11-05**).

- **New top-5:** ^FCHI, ^FTSE, ^HSI, ^STOXX50E
- **Persistent top signals:** ^GDAXI (8 reports)
- **Dropped from top-5:** AAPL, JPM, MSFT, ^DJI

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +0 |   +24.5 |
| 7203.T    |     +0 |   +28.2 |
| 8306.T    |     +3 |   +23.0 |
| AAPL      |     -1 |    -8.5 |
| AMZN      |     -1 |    -4.2 |
| BZ=F      |     +5 |   +16.1 |
| CL=F      |     +2 |   +14.8 |
| GC=F      |     +6 |   +13.0 |
| GOOGL     |     +1 |    +4.2 |
| HG=F      |     -1 |    -2.4 |
| JPM       |     -9 |   -26.7 |
| META      |     -3 |    -7.9 |
| MSFT      |     -6 |   -15.2 |
| NG=F      |     -1 |    +0.9 |
| NVDA      |     -1 |    -9.4 |
| PL=F      |     +5 |   +13.3 |
| SI=F      |     +2 |    +7.0 |
| TSLA      |     -9 |   -31.2 |
| UNH       |     -1 |    -9.7 |
| XOM       |     -2 |    -4.5 |
| ZC=F      |     +2 |    +4.2 |
| ZS=F      |     +2 |    +3.6 |
| ZW=F      |     +2 |    +8.5 |
| ^DJI      |     -7 |   -21.8 |
| ^FCHI     |     +4 |    +5.2 |
| ^FTSE     |     +4 |    +2.1 |
| ^GDAXI    |     +1 |    -0.9 |
| ^GSPC     |     -4 |   -20.6 |
| ^HSI      |    +11 |   +24.2 |
| ^N225     |     -1 |    +1.8 |
| ^NDX      |     -6 |   -14.8 |
| ^RUT      |     -2 |   -20.9 |
| ^STOXX50E |     +5 |    +3.9 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Natural Gas / NG=F** — malformed_input
- **Copper / HG=F** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|    9 | Gold / GC=F            |  57.6 |   Yes    | —               | 20d down -1.0%; above MA20 by 0.6%; RSI14=45  |
|   14 | Soybeans / ZS=F        |  41.2 |   Yes    | —               | 20d down -8.3%; below MA20 by 4.9%; RSI14=13  |
|   15 | Platinum / PL=F        |  40.3 |   Yes    | —               | 20d down -6.2%; below MA20 by 2.8%; RSI14=38  |
|   17 | Corn / ZC=F            |  35.1 |   Yes    | —               | 20d down -12.0%; below MA20 by 4.5%; RSI14=14 |
|   18 | Brent Crude Oil / BZ=F |  34.9 |   Yes    | —               | 20d down -5.7%; below MA20 by 9.6%; RSI14=37  |
|   19 | Wheat / ZW=F           |  33.0 |   Yes    | —               | 20d down -12.3%; below MA20 by 5.1%; RSI14=11 |
|   20 | Silver / SI=F          |  29.1 |   Yes    | —               | 20d down -11.6%; below MA20 by 4.8%; RSI14=35 |
|   29 | Natural Gas / NG=F     |  50.3 |    No    | malformed_input | Suppressed: malformed_input                   |
|   30 | Copper / HG=F          |  39.7 |    No    | malformed_input | Suppressed: malformed_input                   |
|   31 | WTI Crude Oil / CL=F   |  39.1 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                    |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | ---------------------------------------------- |
|    6 | Apple Inc. / AAPL                                                              |  68.5 |   Yes    | —                             | 20d up +1.1%; above MA20 by 0.3%; RSI14=51     |
|    7 | Microsoft Corporation / MSFT                                                   |  68.2 |   Yes    | —                             | 20d up +2.5%; above MA20 by 0.8%; RSI14=53     |
|    8 | Amazon.com Inc. / AMZN                                                         |  67.6 |   Yes    | —                             | 20d up +2.4%; above MA20 by 2.3%; RSI14=56     |
|   10 | UnitedHealth Group Inc. / UNH                                                  |  56.7 |   Yes    | —                             | 20d up +6.7%; below MA20 by 2.1%; RSI14=47     |
|   12 | JPMorgan Chase & Co. / JPM                                                     |  52.1 |   Yes    | —                             | 20d up +1.8%; above MA20 by 0.1%; RSI14=48     |
|   21 | Meta Platforms Inc. / META                                                     |  25.8 |   Yes    | —                             | 20d down -16.1%; below MA20 by 9.4%; RSI14=21  |
|   22 | Tesla Inc. / TSLA                                                              |  25.1 |   Yes    | —                             | 20d down -8.3%; below MA20 by 9.9%; RSI14=46   |
|   24 | Alphabet Inc. Class A / GOOGL                                                  |  18.8 |   Yes    | —                             | 20d down -18.9%; below MA20 by 11.9%; RSI14=21 |
|   25 | NVIDIA Corporation / NVDA                                                      |   5.8 |   Yes    | —                             | 20d down -21.2%; below MA20 by 15.0%; RSI14=28 |
|   26 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  85.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   27 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  84.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   28 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  60.6 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   32 | Exxon Mobil Corporation / XOM                                                  |  36.7 |    No    | malformed_input               | Suppressed: malformed_input                    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                   |
| ---: | ----------------------------------- | ----: | :------: | ------------ | --------------------------------------------- |
|    1 | DAX / ^GDAXI                        |  80.6 |   Yes    | —            | 20d up +6.1%; above MA20 by 2.8%; RSI14=61    |
|    2 | CAC 40 / ^FCHI                      |  78.5 |   Yes    | —            | 20d up +6.2%; above MA20 by 3.6%; RSI14=65    |
|    3 | Hang Seng / ^HSI                    |  77.0 |   Yes    | —            | 20d up +2.8%; above MA20 by 4.6%; RSI14=60    |
|    4 | FTSE 100 / ^FTSE                    |  72.4 |   Yes    | —            | 20d up +3.3%; above MA20 by 0.5%; RSI14=44    |
|    5 | Euro Stoxx 50 / ^STOXX50E           |  69.1 |   Yes    | —            | 20d up +1.7%; above MA20 by 1.0%; RSI14=52    |
|   11 | Dow Jones Industrial Average / ^DJI |  55.5 |   Yes    | —            | 20d up +0.6%; below MA20 by 1.2%; RSI14=46    |
|   13 | Russell 2000 / ^RUT                 |  41.5 |   Yes    | —            | 20d down -2.3%; below MA20 by 2.1%; RSI14=51  |
|   16 | S&P 500 / ^GSPC                     |  39.4 |   Yes    | —            | 20d down -5.3%; below MA20 by 4.2%; RSI14=35  |
|   23 | NASDAQ 100 / ^NDX                   |  19.4 |   Yes    | —            | 20d down -13.3%; below MA20 by 9.1%; RSI14=30 |
|   33 | Nikkei 225 / ^N225                  |  31.2 |    No    | missing_bars | Suppressed: missing_bars                      |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-11-05 |
| 7203.T    | 2026-11-05 |
| 8306.T    | 2026-11-05 |
| AAPL      | 2026-11-05 |
| AMZN      | 2026-11-05 |
| BZ=F      | 2026-11-05 |
| CL=F      | 2026-11-05 |
| GC=F      | 2026-11-05 |
| GOOGL     | 2026-11-05 |
| HG=F      | 2026-11-05 |
| JPM       | 2026-11-05 |
| META      | 2026-11-05 |
| MSFT      | 2026-11-05 |
| NG=F      | 2026-11-05 |
| NVDA      | 2026-11-05 |
| PL=F      | 2026-11-05 |
| SI=F      | 2026-11-05 |
| TSLA      | 2026-11-05 |
| UNH       | 2026-11-05 |
| XOM       | 2026-11-05 |
| ZC=F      | 2026-11-05 |
| ZS=F      | 2026-11-05 |
| ZW=F      | 2026-11-05 |
| ^DJI      | 2026-11-05 |
| ^FCHI     | 2026-11-05 |
| ^FTSE     | 2026-11-05 |
| ^GDAXI    | 2026-11-05 |
| ^GSPC     | 2026-11-05 |
| ^HSI      | 2026-11-05 |
| ^N225     | 2026-11-05 |
| ^NDX      | 2026-11-05 |
| ^RUT      | 2026-11-05 |
| ^STOXX50E | 2026-11-05 |

## Symbol Details

### DAX / ^GDAXI (score 80.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | +1.1% |
| ret_20d    | +6.1% |
| ret_60d    | +0.1% |
| ma20_dist  | +2.8% |
| ma50_dist  | +3.0% |
| vol_20d    | 14.0% |
| mdd_60d    |  6.6% |
| rsi_14     |  61.1 |
| zscore_20d |   2.0 |

### CAC 40 / ^FCHI (score 78.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +3.0% |
| ret_20d    | +6.2% |
| ret_60d    | -5.1% |
| ma20_dist  | +3.6% |
| ma50_dist  | +2.2% |
| vol_20d    | 12.3% |
| mdd_60d    | 10.5% |
| rsi_14     |  65.2 |
| zscore_20d |   2.5 |

### Hang Seng / ^HSI (score 77.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +3.7% |
| ret_5d     | +8.0% |
| ret_20d    | +2.8% |
| ret_60d    | -3.3% |
| ma20_dist  | +4.6% |
| ma50_dist  | +1.5% |
| vol_20d    | 22.1% |
| mdd_60d    | 11.8% |
| rsi_14     |  59.5 |
| zscore_20d |   2.0 |

### FTSE 100 / ^FTSE (score 72.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | +0.6% |
| ret_20d    | +3.3% |
| ret_60d    | -0.5% |
| ma20_dist  | +0.5% |
| ma50_dist  | +0.8% |
| vol_20d    | 11.6% |
| mdd_60d    |  4.2% |
| rsi_14     |  44.0 |
| zscore_20d |   0.7 |

### Euro Stoxx 50 / ^STOXX50E (score 69.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | +0.4% |
| ret_20d    | +1.7% |
| ret_60d    | -4.8% |
| ma20_dist  | +1.0% |
| ma50_dist  | -0.3% |
| vol_20d    | 14.4% |
| mdd_60d    |  7.2% |
| rsi_14     |  51.8 |
| zscore_20d |   1.4 |

### Apple Inc. / AAPL (score 68.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.5% |
| ret_5d     |  -1.4% |
| ret_20d    |  +1.1% |
| ret_60d    | +13.9% |
| ma20_dist  |  +0.3% |
| ma50_dist  |  +2.6% |
| vol_20d    |  25.5% |
| mdd_60d    |   4.9% |
| rsi_14     |   50.5 |
| zscore_20d |    0.3 |

### Microsoft Corporation / MSFT (score 68.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -3.6% |
| ret_5d     | +1.1% |
| ret_20d    | +2.5% |
| ret_60d    | +9.0% |
| ma20_dist  | +0.8% |
| ma50_dist  | +3.8% |
| vol_20d    | 35.3% |
| mdd_60d    |  6.7% |
| rsi_14     |  52.8 |
| zscore_20d |   0.4 |

### Amazon.com Inc. / AMZN (score 67.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.2% |
| ret_5d     | +6.7% |
| ret_20d    | +2.4% |
| ret_60d    | -2.6% |
| ma20_dist  | +2.3% |
| ma50_dist  | +2.5% |
| vol_20d    | 41.9% |
| mdd_60d    |  9.8% |
| rsi_14     |  56.4 |
| zscore_20d |   0.8 |

### Gold / GC=F (score 57.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.0% |
| ret_5d     | +2.0% |
| ret_20d    | -1.0% |
| ret_60d    | -7.6% |
| ma20_dist  | +0.6% |
| ma50_dist  | -2.9% |
| vol_20d    | 23.4% |
| mdd_60d    | 17.2% |
| rsi_14     |  45.2 |
| zscore_20d |   0.3 |

### UnitedHealth Group Inc. / UNH (score 56.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -3.3% |
| ret_5d     | -3.7% |
| ret_20d    | +6.7% |
| ret_60d    | -1.8% |
| ma20_dist  | -2.1% |
| ma50_dist  | +1.4% |
| vol_20d    | 30.5% |
| mdd_60d    |  8.5% |
| rsi_14     |  46.6 |
| zscore_20d |  -0.6 |

### Dow Jones Industrial Average / ^DJI (score 55.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -3.4% |
| ret_5d     | -1.6% |
| ret_20d    | +0.6% |
| ret_60d    | -4.2% |
| ma20_dist  | -1.2% |
| ma50_dist  | -1.1% |
| vol_20d    | 18.8% |
| mdd_60d    |  5.4% |
| rsi_14     |  46.2 |
| zscore_20d |  -1.4 |

### JPMorgan Chase & Co. / JPM (score 52.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -4.2% |
| ret_5d     | -1.8% |
| ret_20d    | +1.8% |
| ret_60d    | -7.6% |
| ma20_dist  | +0.1% |
| ma50_dist  | -1.2% |
| vol_20d    | 26.0% |
| mdd_60d    |  9.4% |
| rsi_14     |  48.2 |
| zscore_20d |   0.1 |

### Russell 2000 / ^RUT (score 41.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -4.4% |
| ret_5d     |  -4.5% |
| ret_20d    |  -2.3% |
| ret_60d    | -10.4% |
| ma20_dist  |  -2.1% |
| ma50_dist  |  -4.0% |
| vol_20d    |  22.3% |
| mdd_60d    |  11.3% |
| rsi_14     |   51.1 |
| zscore_20d |   -1.5 |

### Soybeans / ZS=F (score 41.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | -3.2% |
| ret_20d    | -8.3% |
| ret_60d    | +0.6% |
| ma20_dist  | -4.9% |
| ma50_dist  | -7.5% |
| vol_20d    |  8.5% |
| mdd_60d    | 11.1% |
| rsi_14     |  12.8 |
| zscore_20d |  -2.0 |

### Platinum / PL=F (score 40.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.6% |
| ret_5d     |  +2.0% |
| ret_20d    |  -6.2% |
| ret_60d    | -13.7% |
| ma20_dist  |  -2.8% |
| ma50_dist  |  -9.6% |
| vol_20d    |  35.2% |
| mdd_60d    |  25.2% |
| rsi_14     |   37.6 |
| zscore_20d |   -0.6 |

### S&P 500 / ^GSPC (score 39.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -4.4% |
| ret_5d     | -4.7% |
| ret_20d    | -5.3% |
| ret_60d    | -5.1% |
| ma20_dist  | -4.2% |
| ma50_dist  | -4.3% |
| vol_20d    | 19.4% |
| mdd_60d    |  5.9% |
| rsi_14     |  35.2 |
| zscore_20d |  -3.1 |

### Corn / ZC=F (score 35.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.0% |
| ret_5d     |  -2.5% |
| ret_20d    | -12.0% |
| ret_60d    |  -4.1% |
| ma20_dist  |  -4.5% |
| ma50_dist  | -11.0% |
| vol_20d    |  16.2% |
| mdd_60d    |  19.0% |
| rsi_14     |   13.8 |
| zscore_20d |   -1.5 |

### Brent Crude Oil / BZ=F (score 34.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +3.9% |
| ret_5d     | -14.4% |
| ret_20d    |  -5.7% |
| ret_60d    | +10.1% |
| ma20_dist  |  -9.6% |
| ma50_dist  |  -5.6% |
| vol_20d    |  57.9% |
| mdd_60d    |  19.6% |
| rsi_14     |   36.6 |
| zscore_20d |   -1.7 |

### Wheat / ZW=F (score 33.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.1% |
| ret_5d     |  -0.7% |
| ret_20d    | -12.3% |
| ret_60d    | -11.2% |
| ma20_dist  |  -5.1% |
| ma50_dist  | -12.1% |
| vol_20d    |  14.1% |
| mdd_60d    |  22.0% |
| rsi_14     |   11.1 |
| zscore_20d |   -1.1 |

### Silver / SI=F (score 29.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.2% |
| ret_5d     |  +0.1% |
| ret_20d    | -11.6% |
| ret_60d    | -20.7% |
| ma20_dist  |  -4.8% |
| ma50_dist  | -13.3% |
| vol_20d    |  44.9% |
| mdd_60d    |  29.3% |
| rsi_14     |   35.1 |
| zscore_20d |   -0.8 |

### Meta Platforms Inc. / META (score 25.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -4.0% |
| ret_5d     |  -3.1% |
| ret_20d    | -16.1% |
| ret_60d    |  +4.5% |
| ma20_dist  |  -9.4% |
| ma50_dist  | -10.2% |
| vol_20d    |  39.0% |
| mdd_60d    |  22.2% |
| rsi_14     |   21.3 |
| zscore_20d |   -1.2 |

### Tesla Inc. / TSLA (score 25.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     | -10.8% |
| ret_5d     | -14.8% |
| ret_20d    |  -8.3% |
| ret_60d    |  +4.9% |
| ma20_dist  |  -9.9% |
| ma50_dist  |  -7.6% |
| vol_20d    |  53.5% |
| mdd_60d    |  15.7% |
| rsi_14     |   46.4 |
| zscore_20d |   -2.2 |

### NASDAQ 100 / ^NDX (score 19.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -6.4% |
| ret_5d     |  -9.4% |
| ret_20d    | -13.3% |
| ret_60d    | -10.5% |
| ma20_dist  |  -9.1% |
| ma50_dist  | -10.3% |
| vol_20d    |  30.4% |
| mdd_60d    |  14.7% |
| rsi_14     |   30.4 |
| zscore_20d |   -2.7 |

### Alphabet Inc. Class A / GOOGL (score 18.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.2% |
| ret_5d     |  -0.4% |
| ret_20d    | -18.9% |
| ret_60d    | -17.7% |
| ma20_dist  | -11.9% |
| ma50_dist  | -15.4% |
| vol_20d    |  48.8% |
| mdd_60d    |  21.4% |
| rsi_14     |   21.4 |
| zscore_20d |   -1.4 |

### NVIDIA Corporation / NVDA (score 5.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -9.3% |
| ret_5d     | -15.0% |
| ret_20d    | -21.2% |
| ret_60d    | -18.9% |
| ma20_dist  | -15.0% |
| ma50_dist  | -17.7% |
| vol_20d    |  43.3% |
| mdd_60d    |  24.1% |
| rsi_14     |   27.6 |
| zscore_20d |   -3.0 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| DAX / ^GDAXI                        | 370.6571 |           1.4% |                 0.71x |      741.3142 |            2.8% |
| CAC 40 / ^FCHI                      | 104.0164 |           1.3% |                 0.82x |      208.0329 |            2.5% |
| Hang Seng / ^HSI                    | 412.2511 |           1.7% |                 0.45x |      824.5022 |            3.3% |
| FTSE 100 / ^FTSE                    | 112.5500 |           1.0% |                 0.86x |      225.1000 |            2.1% |
| Euro Stoxx 50 / ^STOXX50E           |  88.8000 |           1.4% |                 0.69x |      177.6001 |            2.9% |
| Apple Inc. / AAPL                   |   8.9021 |           2.6% |                 0.39x |       17.8043 |            5.2% |
| Microsoft Corporation / MSFT        |  15.4221 |           2.9% |                 0.28x |       30.8443 |            5.8% |
| Amazon.com Inc. / AMZN              |  10.3393 |           4.0% |                 0.24x |       20.6786 |            7.9% |
| Gold / GC=F                         |  83.1571 |           2.0% |                 0.43x |      166.3142 |            4.0% |
| UnitedHealth Group Inc. / UNH       |  12.0079 |           3.0% |                 0.33x |       24.0157 |            6.1% |
| Dow Jones Industrial Average / ^DJI | 705.9902 |           1.4% |                 0.53x |     1411.9805 |            2.7% |
| JPMorgan Chase & Co. / JPM          |   7.8086 |           2.3% |                 0.38x |       15.6171 |            4.6% |
| Russell 2000 / ^RUT                 |  43.5671 |           1.6% |                 0.45x |       87.1342 |            3.2% |
| Soybeans / ZS=F                     |  16.4643 |           1.4% |                 1.17x |       32.9286 |            2.8% |
| Platinum / PL=F                     |  33.8286 |           2.2% |                 0.28x |       67.6571 |            4.4% |
| S&P 500 / ^GSPC                     | 104.9422 |           1.4% |                 0.51x |      209.8844 |            2.9% |
| Corn / ZC=F                         |   7.1786 |           1.6% |                 0.62x |       14.3571 |            3.3% |
| Brent Crude Oil / BZ=F              |   5.5307 |           5.6% |                 0.17x |       11.0614 |           11.3% |
| Wheat / ZW=F                        |  13.5893 |           2.3% |                 0.71x |       27.1786 |            4.5% |
| Silver / SI=F                       |   1.4589 |           2.8% |                 0.22x |        2.9179 |            5.6% |
| Meta Platforms Inc. / META          |  23.4671 |           3.9% |                 0.26x |       46.9343 |            7.8% |
| Tesla Inc. / TSLA                   |  17.6250 |           5.1% |                 0.19x |       35.2500 |           10.3% |
| NASDAQ 100 / ^NDX                   | 672.6893 |           2.5% |                 0.33x |     1345.3786 |            5.1% |
| Alphabet Inc. Class A / GOOGL       |  11.1593 |           3.9% |                 0.21x |       22.3186 |            7.9% |
| NVIDIA Corporation / NVDA           |   7.4621 |           4.1% |                 0.23x |       14.9243 |            8.2% |

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

Scoring engine version: **1.0.0** | Git commit: **521c388**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
