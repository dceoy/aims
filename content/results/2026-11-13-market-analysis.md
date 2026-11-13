+++
title = "Market Analysis 2026-11-13"
date = "2026-11-13T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: ^GDAXI (score 79.1)."
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
source_files = ["data/analysis/2026-11-13.json", "data/history/2026-11-13.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "cd7e781"
+++

## Market Regime

**Neutral** — 12 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **DAX / ^GDAXI** — score 79.1, 20d return +5.5%, RSI14=73. 20d up +5.5%; above MA20 by 3.5%; RSI14=73
- **CAC 40 / ^FCHI** — score 77.3, 20d return +5.4%, RSI14=88. 20d up +5.4%; above MA20 by 4.2%; RSI14=88
- **Euro Stoxx 50 / ^STOXX50E** — score 76.1, 20d return +3.7%, RSI14=72. 20d up +3.7%; above MA20 by 3.2%; RSI14=72
- **Apple Inc. / AAPL** — score 73.9, 20d return +3.8%, RSI14=55. 20d up +3.8%; above MA20 by 2.8%; RSI14=55
- **Tesla Inc. / TSLA** — score 70.0, 20d return +9.7%, RSI14=58. 20d up +9.7%; above MA20 by 3.6%; RSI14=58

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                 | Applies To |
| ---------- | --------------------- | ---------- |
| 2026-11-17 | NVDA earnings release | NVDA       |

## Signal History

Compared with the previous available report (**2026-11-12**).

- **New top-5:** TSLA
- **Persistent top signals:** ^GDAXI (13 reports), ^FCHI (6 reports), AAPL (5 reports), ^STOXX50E (3 reports)
- **Dropped from top-5:** ^FTSE

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +0 |    +5.5 |
| 7203.T    |     -2 |   -10.6 |
| 8306.T    |     +0 |    -5.2 |
| AAPL      |     -3 |    -5.5 |
| AMZN      |     +0 |    +7.6 |
| BZ=F      |     +3 |    +7.0 |
| CL=F      |     +1 |   +10.9 |
| GC=F      |     -3 |   -10.3 |
| GOOGL     |     +4 |    +6.7 |
| HG=F      |     -1 |    -7.0 |
| JPM       |     +4 |    +8.8 |
| META      |     +3 |    +4.8 |
| MSFT      |     +3 |   +10.6 |
| NG=F      |     +2 |   +13.3 |
| NVDA      |     +0 |    -9.1 |
| PL=F      |     -2 |    -8.2 |
| SI=F      |     -1 |   -14.6 |
| TSLA      |     +1 |    +3.3 |
| UNH       |     +6 |   +11.5 |
| XOM       |     +1 |   +11.2 |
| ZC=F      |     -2 |    -5.2 |
| ZS=F      |     +0 |    +2.7 |
| ZW=F      |     -2 |   -13.9 |
| ^DJI      |     +1 |    +1.5 |
| ^FCHI     |     +2 |    +0.0 |
| ^FTSE     |     -1 |    +0.3 |
| ^GDAXI    |     +1 |    +0.6 |
| ^GSPC     |     -2 |    +0.3 |
| ^HSI      |     -5 |    -7.9 |
| ^N225     |     -1 |    -1.5 |
| ^NDX      |     -1 |    +1.8 |
| ^RUT      |     -6 |    -7.9 |
| ^STOXX50E |     +0 |    -1.8 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Natural Gas / NG=F** — malformed_input
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Copper / HG=F** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|   12 | Soybeans / ZS=F        |  55.5 |   Yes    | —               | 20d down -2.9%; above MA20 by 0.2%; RSI14=40  |
|   19 | Corn / ZC=F            |  31.2 |   Yes    | —               | 20d down -7.4%; below MA20 by 2.0%; RSI14=35  |
|   20 | Platinum / PL=F        |  27.9 |   Yes    | —               | 20d down -5.7%; below MA20 by 1.5%; RSI14=45  |
|   21 | Brent Crude Oil / BZ=F |  26.1 |   Yes    | —               | 20d down -9.5%; below MA20 by 9.5%; RSI14=27  |
|   22 | Gold / GC=F            |  21.5 |   Yes    | —               | 20d down -6.8%; below MA20 by 4.1%; RSI14=43  |
|   23 | Wheat / ZW=F           |  17.6 |   Yes    | —               | 20d down -12.8%; below MA20 by 4.5%; RSI14=25 |
|   24 | Silver / SI=F          |  10.3 |   Yes    | —               | 20d down -12.1%; below MA20 by 6.0%; RSI14=39 |
|   26 | Natural Gas / NG=F     |  77.3 |    No    | malformed_input | Suppressed: malformed_input                   |
|   31 | Copper / HG=F          |  32.1 |    No    | malformed_input | Suppressed: malformed_input                   |
|   32 | WTI Crude Oil / CL=F   |  30.9 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                    |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | ---------------------------------------------- |
|    4 | Apple Inc. / AAPL                                                              |  73.9 |   Yes    | —                             | 20d up +3.8%; above MA20 by 2.8%; RSI14=55     |
|    5 | Tesla Inc. / TSLA                                                              |  70.0 |   Yes    | —                             | 20d up +9.7%; above MA20 by 3.6%; RSI14=58     |
|    7 | Amazon.com Inc. / AMZN                                                         |  69.7 |   Yes    | —                             | 20d up +5.0%; above MA20 by 4.3%; RSI14=64     |
|    8 | UnitedHealth Group Inc. / UNH                                                  |  60.6 |   Yes    | —                             | 20d down -0.4%; below MA20 by 0.6%; RSI14=40   |
|    9 | JPMorgan Chase & Co. / JPM                                                     |  59.4 |   Yes    | —                             | 20d up +2.2%; above MA20 by 1.2%; RSI14=59     |
|   13 | Microsoft Corporation / MSFT                                                   |  51.2 |   Yes    | —                             | 20d down -3.0%; below MA20 by 1.3%; RSI14=49   |
|   17 | Meta Platforms Inc. / META                                                     |  36.7 |   Yes    | —                             | 20d down -15.4%; below MA20 by 2.6%; RSI14=44  |
|   18 | Alphabet Inc. Class A / GOOGL                                                  |  33.6 |   Yes    | —                             | 20d down -14.5%; below MA20 by 2.3%; RSI14=38  |
|   25 | NVIDIA Corporation / NVDA                                                      |   2.7 |   Yes    | —                             | 20d down -23.5%; below MA20 by 17.4%; RSI14=24 |
|   27 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  77.0 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   28 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  63.3 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   29 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  53.3 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   30 | Exxon Mobil Corporation / XOM                                                  |  48.8 |    No    | malformed_input               | Suppressed: malformed_input                    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    1 | DAX / ^GDAXI                        |  79.1 |   Yes    | —            | 20d up +5.5%; above MA20 by 3.5%; RSI14=73   |
|    2 | CAC 40 / ^FCHI                      |  77.3 |   Yes    | —            | 20d up +5.4%; above MA20 by 4.2%; RSI14=88   |
|    3 | Euro Stoxx 50 / ^STOXX50E           |  76.1 |   Yes    | —            | 20d up +3.7%; above MA20 by 3.2%; RSI14=72   |
|    6 | FTSE 100 / ^FTSE                    |  70.0 |   Yes    | —            | 20d up +0.2%; above MA20 by 1.0%; RSI14=59   |
|   10 | Dow Jones Industrial Average / ^DJI |  57.9 |   Yes    | —            | 20d up +0.2%; above MA20 by 0.1%; RSI14=51   |
|   11 | S&P 500 / ^GSPC                     |  57.3 |   Yes    | —            | 20d down -2.0%; below MA20 by 0.3%; RSI14=49 |
|   14 | Russell 2000 / ^RUT                 |  50.0 |   Yes    | —            | 20d up +1.1%; above MA20 by 0.1%; RSI14=52   |
|   15 | Hang Seng / ^HSI                    |  48.8 |   Yes    | —            | 20d down -1.3%; above MA20 by 1.1%; RSI14=64 |
|   16 | NASDAQ 100 / ^NDX                   |  44.9 |   Yes    | —            | 20d down -5.5%; below MA20 by 1.3%; RSI14=45 |
|   33 | Nikkei 225 / ^N225                  |  28.2 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-11-12 |
| 7203.T    | 2026-11-12 |
| 8306.T    | 2026-11-12 |
| AAPL      | 2026-11-12 |
| AMZN      | 2026-11-12 |
| BZ=F      | 2026-11-12 |
| CL=F      | 2026-11-12 |
| GC=F      | 2026-11-12 |
| GOOGL     | 2026-11-12 |
| HG=F      | 2026-11-12 |
| JPM       | 2026-11-12 |
| META      | 2026-11-12 |
| MSFT      | 2026-11-12 |
| NG=F      | 2026-11-12 |
| NVDA      | 2026-11-12 |
| PL=F      | 2026-11-12 |
| SI=F      | 2026-11-12 |
| TSLA      | 2026-11-12 |
| UNH       | 2026-11-12 |
| XOM       | 2026-11-12 |
| ZC=F      | 2026-11-12 |
| ZS=F      | 2026-11-12 |
| ZW=F      | 2026-11-12 |
| ^DJI      | 2026-11-12 |
| ^FCHI     | 2026-11-12 |
| ^FTSE     | 2026-11-12 |
| ^GDAXI    | 2026-11-12 |
| ^GSPC     | 2026-11-12 |
| ^HSI      | 2026-11-12 |
| ^N225     | 2026-11-12 |
| ^NDX      | 2026-11-12 |
| ^RUT      | 2026-11-12 |
| ^STOXX50E | 2026-11-12 |

## Symbol Details

### DAX / ^GDAXI (score 79.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | +1.7% |
| ret_20d    | +5.5% |
| ret_60d    | +3.0% |
| ma20_dist  | +3.5% |
| ma50_dist  | +4.6% |
| vol_20d    | 16.8% |
| mdd_60d    |  6.6% |
| rsi_14     |  72.7 |
| zscore_20d |   2.0 |

### CAC 40 / ^FCHI (score 77.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +1.9% |
| ret_20d    | +5.4% |
| ret_60d    | -1.1% |
| ma20_dist  | +4.2% |
| ma50_dist  | +4.2% |
| vol_20d    | 12.9% |
| mdd_60d    |  8.9% |
| rsi_14     |  87.7 |
| zscore_20d |   1.9 |

### Euro Stoxx 50 / ^STOXX50E (score 76.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | +2.7% |
| ret_20d    | +3.7% |
| ret_60d    | -0.4% |
| ma20_dist  | +3.2% |
| ma50_dist  | +2.5% |
| vol_20d    | 16.2% |
| mdd_60d    |  6.4% |
| rsi_14     |  72.5 |
| zscore_20d |   2.2 |

### Apple Inc. / AAPL (score 73.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.1% |
| ret_5d     |  +3.2% |
| ret_20d    |  +3.8% |
| ret_60d    | +12.0% |
| ma20_dist  |  +2.8% |
| ma50_dist  |  +4.9% |
| vol_20d    |  27.2% |
| mdd_60d    |   4.9% |
| rsi_14     |   54.9 |
| zscore_20d |    1.8 |

### Tesla Inc. / TSLA (score 70.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.7% |
| ret_5d     | +15.6% |
| ret_20d    |  +9.7% |
| ret_60d    | +13.2% |
| ma20_dist  |  +3.6% |
| ma50_dist  |  +6.1% |
| vol_20d    |  58.5% |
| mdd_60d    |  15.7% |
| rsi_14     |   57.8 |
| zscore_20d |    0.8 |

### FTSE 100 / ^FTSE (score 70.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +0.7% |
| ret_20d    | +0.2% |
| ret_60d    | +1.1% |
| ma20_dist  | +1.0% |
| ma50_dist  | +1.6% |
| vol_20d    | 11.4% |
| mdd_60d    |  4.2% |
| rsi_14     |  59.1 |
| zscore_20d |   1.8 |

### Amazon.com Inc. / AMZN (score 69.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | +2.8% |
| ret_20d    | +5.0% |
| ret_60d    | +0.6% |
| ma20_dist  | +4.3% |
| ma50_dist  | +5.0% |
| vol_20d    | 41.6% |
| mdd_60d    |  9.8% |
| rsi_14     |  63.7 |
| zscore_20d |   1.2 |

### UnitedHealth Group Inc. / UNH (score 60.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | +2.4% |
| ret_20d    | -0.4% |
| ret_60d    | +4.9% |
| ma20_dist  | -0.6% |
| ma50_dist  | +3.6% |
| vol_20d    | 24.1% |
| mdd_60d    |  8.4% |
| rsi_14     |  40.0 |
| zscore_20d |  -0.3 |

### JPMorgan Chase & Co. / JPM (score 59.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | +1.6% |
| ret_20d    | +2.2% |
| ret_60d    | -4.0% |
| ma20_dist  | +1.2% |
| ma50_dist  | +0.8% |
| vol_20d    | 26.8% |
| mdd_60d    |  9.1% |
| rsi_14     |  58.5 |
| zscore_20d |   0.9 |

### Dow Jones Industrial Average / ^DJI (score 57.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | +1.5% |
| ret_20d    | +0.2% |
| ret_60d    | -2.2% |
| ma20_dist  | +0.1% |
| ma50_dist  | +0.6% |
| vol_20d    | 19.8% |
| mdd_60d    |  5.2% |
| rsi_14     |  50.6 |
| zscore_20d |   0.1 |

### S&P 500 / ^GSPC (score 57.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | +3.2% |
| ret_20d    | -2.0% |
| ret_60d    | -1.5% |
| ma20_dist  | -0.3% |
| ma50_dist  | -1.0% |
| vol_20d    | 21.6% |
| mdd_60d    |  5.9% |
| rsi_14     |  48.6 |
| zscore_20d |  -0.2 |

### Soybeans / ZS=F (score 55.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | +3.9% |
| ret_20d    | -2.9% |
| ret_60d    | +0.5% |
| ma20_dist  | +0.2% |
| ma50_dist  | -3.3% |
| vol_20d    | 16.2% |
| mdd_60d    | 11.1% |
| rsi_14     |  39.8 |
| zscore_20d |   0.1 |

### Microsoft Corporation / MSFT (score 51.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | -2.4% |
| ret_20d    | -3.0% |
| ret_60d    | +8.2% |
| ma20_dist  | -1.3% |
| ma50_dist  | +0.8% |
| vol_20d    | 36.6% |
| mdd_60d    |  6.7% |
| rsi_14     |  49.5 |
| zscore_20d |  -0.7 |

### Russell 2000 / ^RUT (score 50.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.7% |
| ret_5d     | +2.5% |
| ret_20d    | +1.1% |
| ret_60d    | -7.7% |
| ma20_dist  | +0.1% |
| ma50_dist  | -1.0% |
| vol_20d    | 24.6% |
| mdd_60d    |  9.8% |
| rsi_14     |  52.2 |
| zscore_20d |   0.1 |

### Hang Seng / ^HSI (score 48.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.3% |
| ret_5d     | -3.2% |
| ret_20d    | -1.3% |
| ret_60d    | -5.7% |
| ma20_dist  | +1.1% |
| ma50_dist  | -1.3% |
| vol_20d    | 21.9% |
| mdd_60d    | 11.8% |
| rsi_14     |  63.8 |
| zscore_20d |   0.5 |

### NASDAQ 100 / ^NDX (score 44.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | +6.2% |
| ret_20d    | -5.5% |
| ret_60d    | -3.9% |
| ma20_dist  | -1.3% |
| ma50_dist  | -4.2% |
| vol_20d    | 34.7% |
| mdd_60d    | 14.7% |
| rsi_14     |  45.3 |
| zscore_20d |  -0.4 |

### Meta Platforms Inc. / META (score 36.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.8% |
| ret_5d     |  +3.1% |
| ret_20d    | -15.4% |
| ret_60d    | +14.3% |
| ma20_dist  |  -2.6% |
| ma50_dist  |  -8.2% |
| vol_20d    |  39.6% |
| mdd_60d    |  22.2% |
| rsi_14     |   44.1 |
| zscore_20d |   -0.5 |

### Alphabet Inc. Class A / GOOGL (score 33.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.8% |
| ret_5d     |  +5.7% |
| ret_20d    | -14.5% |
| ret_60d    | -13.3% |
| ma20_dist  |  -2.3% |
| ma50_dist  |  -9.2% |
| vol_20d    |  50.6% |
| mdd_60d    |  21.4% |
| rsi_14     |   38.2 |
| zscore_20d |   -0.3 |

### Corn / ZC=F (score 31.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.2% |
| ret_5d     | +0.6% |
| ret_20d    | -7.4% |
| ret_60d    | -7.6% |
| ma20_dist  | -2.0% |
| ma50_dist  | -9.2% |
| vol_20d    | 13.8% |
| mdd_60d    | 19.1% |
| rsi_14     |  35.5 |
| zscore_20d |  -1.0 |

### Platinum / PL=F (score 27.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.4% |
| ret_5d     |  -0.4% |
| ret_20d    |  -5.7% |
| ret_60d    | -19.6% |
| ma20_dist  |  -1.5% |
| ma50_dist  |  -8.6% |
| vol_20d    |  32.0% |
| mdd_60d    |  25.2% |
| rsi_14     |   45.0 |
| zscore_20d |   -0.4 |

### Brent Crude Oil / BZ=F (score 26.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +3.3% |
| ret_5d     | -2.5% |
| ret_20d    | -9.5% |
| ret_60d    | +1.5% |
| ma20_dist  | -9.5% |
| ma50_dist  | -8.1% |
| vol_20d    | 62.2% |
| mdd_60d    | 22.2% |
| rsi_14     |  27.0 |
| zscore_20d |  -1.1 |

### Gold / GC=F (score 21.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.9% |
| ret_5d     |  -5.5% |
| ret_20d    |  -6.8% |
| ret_60d    | -17.0% |
| ma20_dist  |  -4.1% |
| ma50_dist  |  -7.3% |
| vol_20d    |  24.7% |
| mdd_60d    |  17.4% |
| rsi_14     |   42.5 |
| zscore_20d |   -2.0 |

### Wheat / ZW=F (score 17.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.5% |
| ret_5d     |  -2.5% |
| ret_20d    | -12.8% |
| ret_60d    | -14.4% |
| ma20_dist  |  -4.5% |
| ma50_dist  | -12.2% |
| vol_20d    |  16.5% |
| mdd_60d    |  23.8% |
| rsi_14     |   24.8 |
| zscore_20d |   -1.3 |

### Silver / SI=F (score 10.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -3.7% |
| ret_5d     |  -4.3% |
| ret_20d    | -12.1% |
| ret_60d    | -28.1% |
| ma20_dist  |  -6.0% |
| ma50_dist  | -15.1% |
| vol_20d    |  40.8% |
| mdd_60d    |  29.3% |
| rsi_14     |   38.7 |
| zscore_20d |   -1.2 |

### NVIDIA Corporation / NVDA (score 2.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -4.3% |
| ret_5d     |  -8.5% |
| ret_20d    | -23.5% |
| ret_60d    | -23.5% |
| ma20_dist  | -17.4% |
| ma50_dist  | -23.0% |
| vol_20d    |  51.4% |
| mdd_60d    |  30.5% |
| rsi_14     |   24.5 |
| zscore_20d |   -2.0 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| DAX / ^GDAXI                        | 391.3244 |           1.5% |                 0.60x |      782.6487 |            2.9% |
| CAC 40 / ^FCHI                      | 104.3343 |           1.2% |                 0.78x |      208.6687 |            2.5% |
| Euro Stoxx 50 / ^STOXX50E           |  88.7815 |           1.4% |                 0.62x |      177.5630 |            2.8% |
| Apple Inc. / AAPL                   |   9.5023 |           2.7% |                 0.37x |       19.0047 |            5.4% |
| Tesla Inc. / TSLA                   |  18.6257 |           4.7% |                 0.17x |       37.2514 |            9.4% |
| FTSE 100 / ^FTSE                    | 121.5786 |           1.1% |                 0.88x |      243.1572 |            2.2% |
| Amazon.com Inc. / AMZN              |  10.5607 |           3.9% |                 0.24x |       21.1214 |            7.9% |
| UnitedHealth Group Inc. / UNH       |  11.1307 |           2.7% |                 0.41x |       22.2614 |            5.5% |
| JPMorgan Chase & Co. / JPM          |   7.8450 |           2.3% |                 0.37x |       15.6900 |            4.6% |
| Dow Jones Industrial Average / ^DJI | 745.8973 |           1.4% |                 0.50x |     1491.7946 |            2.9% |
| S&P 500 / ^GSPC                     | 120.2522 |           1.6% |                 0.46x |      240.5043 |            3.2% |
| Soybeans / ZS=F                     |  18.4643 |           1.5% |                 0.62x |       36.9286 |            3.0% |
| Microsoft Corporation / MSFT        |  17.4793 |           3.3% |                 0.27x |       34.9586 |            6.7% |
| Russell 2000 / ^RUT                 |  51.5314 |           1.8% |                 0.41x |      103.0628 |            3.7% |
| Hang Seng / ^HSI                    | 359.6967 |           1.5% |                 0.46x |      719.3934 |            3.0% |
| NASDAQ 100 / ^NDX                   | 737.4930 |           2.6% |                 0.29x |     1474.9860 |            5.2% |
| Meta Platforms Inc. / META          |  20.9293 |           3.4% |                 0.25x |       41.8586 |            6.7% |
| Alphabet Inc. Class A / GOOGL       |  11.4357 |           3.8% |                 0.20x |       22.8714 |            7.7% |
| Corn / ZC=F                         |   7.1250 |           1.6% |                 0.72x |       14.2500 |            3.2% |
| Platinum / PL=F                     |  32.6286 |           2.1% |                 0.31x |       65.2571 |            4.3% |
| Brent Crude Oil / BZ=F              |   5.6143 |           5.9% |                 0.16x |       11.2286 |           11.7% |
| Gold / GC=F                         |  98.0500 |           2.5% |                 0.41x |      196.1000 |            5.0% |
| Wheat / ZW=F                        |  13.7500 |           2.4% |                 0.61x |       27.5000 |            4.7% |
| Silver / SI=F                       |   1.4945 |           3.0% |                 0.25x |        2.9890 |            6.0% |
| NVIDIA Corporation / NVDA           |  10.6607 |           6.4% |                 0.19x |       21.3214 |           12.8% |

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

Scoring engine version: **1.0.0** | Git commit: **cd7e781**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
