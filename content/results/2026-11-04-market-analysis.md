+++
title = "Market Analysis 2026-11-04"
date = "2026-11-04T00:00:00+00:00"
draft = false
summary = "Bearish market: 25 reliable instruments. Top signal: ^GDAXI (score 76.7)."
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
source_files = ["data/analysis/2026-11-04.json", "data/history/2026-11-04.json"]
market_regime = "Bearish"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "fa5311e"
+++

## Market Regime

**Bearish** — 6 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **DAX / ^GDAXI** — score 76.7, 20d return +1.6%, RSI14=60. 20d up +1.6%; above MA20 by 1.6%; RSI14=60
- **UnitedHealth Group Inc. / UNH** — score 72.4, 20d return +7.5%, RSI14=55. 20d up +7.5%; above MA20 by 0.8%; RSI14=55
- **CAC 40 / ^FCHI** — score 72.1, 20d return +2.0%, RSI14=60. 20d up +2.0%; above MA20 by 1.8%; RSI14=60
- **Tesla Inc. / TSLA** — score 70.6, 20d return +4.7%, RSI14=64. 20d up +4.7%; above MA20 by 4.1%; RSI14=64
- **Russell 2000 / ^RUT** — score 66.1, 20d return -0.6%, RSI14=64. 20d down -0.6%; above MA20 by 0.9%; RSI14=64

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                   | Applies To |
| ---------- | ----------------------- | ---------- |
| 2026-11-05 | 6758.T earnings release | 6758.T     |
| 2026-11-05 | 7203.T earnings release | 7203.T     |

## Signal History

Compared with the previous available report (**2026-11-03**).

- **New top-5:** UNH, ^RUT
- **Persistent top signals:** TSLA (7 reports), ^GDAXI (6 reports), ^FCHI (2 reports)
- **Dropped from top-5:** JPM, ^FTSE

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +0 |    +1.5 |
| 7203.T    |     +0 |    +0.3 |
| 8306.T    |     +0 |    +0.9 |
| AAPL      |     -6 |   -14.2 |
| AMZN      |     +1 |    +8.5 |
| BZ=F      |     -3 |    -1.5 |
| CL=F      |     +1 |    +5.2 |
| GC=F      |     -4 |    -9.4 |
| GOOGL     |     +2 |    +3.6 |
| HG=F      |     -4 |   -27.0 |
| JPM       |     -2 |    -7.9 |
| META      |     +3 |   +14.5 |
| MSFT      |     +8 |   +25.8 |
| NG=F      |     +3 |   +11.2 |
| NVDA      |     +4 |   +12.4 |
| PL=F      |     -2 |    -9.4 |
| SI=F      |     -1 |   -11.5 |
| TSLA      |     -3 |   -11.8 |
| UNH       |     +7 |   +13.9 |
| XOM       |     +0 |    +0.3 |
| ZC=F      |     -3 |    -6.7 |
| ZS=F      |     +0 |    +3.3 |
| ZW=F      |     -3 |    -7.3 |
| ^DJI      |     +0 |    -1.2 |
| ^FCHI     |     +0 |    -2.7 |
| ^FTSE     |     -4 |   -10.3 |
| ^GDAXI    |     +1 |    -3.6 |
| ^GSPC     |     +0 |    +7.3 |
| ^HSI      |     +0 |    +3.3 |
| ^N225     |     +0 |    +1.2 |
| ^NDX      |     +3 |    +8.5 |
| ^RUT      |     +5 |    +7.9 |
| ^STOXX50E |     -3 |    -5.2 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **WTI Crude Oil / CL=F** — malformed_input
- **Natural Gas / NG=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                    |
| ---: | ---------------------- | ----: | :------: | --------------- | ---------------------------------------------- |
|   15 | Soybeans / ZS=F        |  43.6 |   Yes    | —               | 20d down -7.7%; below MA20 by 4.0%; RSI14=14   |
|   16 | Brent Crude Oil / BZ=F |  42.4 |   Yes    | —               | 20d up +3.0%; below MA20 by 5.2%; RSI14=46     |
|   20 | Gold / GC=F            |  29.7 |   Yes    | —               | 20d down -5.9%; below MA20 by 3.7%; RSI14=36   |
|   21 | Corn / ZC=F            |  28.8 |   Yes    | —               | 20d down -12.9%; below MA20 by 5.2%; RSI14=10  |
|   22 | Wheat / ZW=F           |  25.1 |   Yes    | —               | 20d down -14.8%; below MA20 by 6.3%; RSI14=9   |
|   24 | Platinum / PL=F        |  10.9 |   Yes    | —               | 20d down -15.4%; below MA20 by 9.3%; RSI14=24  |
|   25 | Silver / SI=F          |   6.4 |   Yes    | —               | 20d down -18.9%; below MA20 by 10.8%; RSI14=30 |
|   29 | WTI Crude Oil / CL=F   |  54.5 |    No    | malformed_input | Suppressed: malformed_input                    |
|   30 | Natural Gas / NG=F     |  49.7 |    No    | malformed_input | Suppressed: malformed_input                    |
|   33 | Copper / HG=F          |  37.0 |    No    | malformed_input | Suppressed: malformed_input                    |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                    |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | ---------------------------------------------- |
|    2 | UnitedHealth Group Inc. / UNH                                                  |  72.4 |   Yes    | —                             | 20d up +7.5%; above MA20 by 0.8%; RSI14=55     |
|    4 | Tesla Inc. / TSLA                                                              |  70.6 |   Yes    | —                             | 20d up +4.7%; above MA20 by 4.1%; RSI14=64     |
|    7 | JPMorgan Chase & Co. / JPM                                                     |  65.5 |   Yes    | —                             | 20d up +2.0%; above MA20 by 0.7%; RSI14=53     |
|    9 | Microsoft Corporation / MSFT                                                   |  62.7 |   Yes    | —                             | 20d down -1.6%; below MA20 by 1.6%; RSI14=43   |
|   13 | Amazon.com Inc. / AMZN                                                         |  50.6 |   Yes    | —                             | 20d down -2.2%; below MA20 by 1.2%; RSI14=47   |
|   14 | Apple Inc. / AAPL                                                              |  46.4 |   Yes    | —                             | 20d down -0.5%; below MA20 by 3.0%; RSI14=38   |
|   18 | Meta Platforms Inc. / META                                                     |  35.5 |   Yes    | —                             | 20d down -15.9%; below MA20 by 8.5%; RSI14=17  |
|   19 | NVIDIA Corporation / NVDA                                                      |  32.1 |   Yes    | —                             | 20d down -13.6%; below MA20 by 5.2%; RSI14=37  |
|   23 | Alphabet Inc. Class A / GOOGL                                                  |  12.1 |   Yes    | —                             | 20d down -19.5%; below MA20 by 14.4%; RSI14=15 |
|   26 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  71.5 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   27 | Exxon Mobil Corporation / XOM                                                  |  69.7 |    No    | malformed_input               | Suppressed: malformed_input                    |
|   28 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  68.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   32 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  42.1 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    1 | DAX / ^GDAXI                        |  76.7 |   Yes    | —            | 20d up +1.6%; above MA20 by 1.6%; RSI14=60   |
|    3 | CAC 40 / ^FCHI                      |  72.1 |   Yes    | —            | 20d up +2.0%; above MA20 by 1.8%; RSI14=60   |
|    5 | Russell 2000 / ^RUT                 |  66.1 |   Yes    | —            | 20d down -0.6%; above MA20 by 0.9%; RSI14=64 |
|    6 | Dow Jones Industrial Average / ^DJI |  65.8 |   Yes    | —            | 20d up +0.5%; below MA20 by 0.5%; RSI14=52   |
|    8 | FTSE 100 / ^FTSE                    |  64.2 |   Yes    | —            | 20d up +0.9%; below MA20 by 0.5%; RSI14=44   |
|   10 | Euro Stoxx 50 / ^STOXX50E           |  59.4 |   Yes    | —            | 20d down -2.0%; below MA20 by 0.2%; RSI14=47 |
|   11 | S&P 500 / ^GSPC                     |  56.1 |   Yes    | —            | 20d down -3.2%; below MA20 by 1.8%; RSI14=39 |
|   12 | Hang Seng / ^HSI                    |  52.1 |   Yes    | —            | 20d down -2.1%; below MA20 by 0.7%; RSI14=36 |
|   17 | NASDAQ 100 / ^NDX                   |  36.4 |   Yes    | —            | 20d down -9.7%; below MA20 by 4.9%; RSI14=33 |
|   31 | Nikkei 225 / ^N225                  |  43.6 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-11-02 |
| 7203.T    | 2026-11-02 |
| 8306.T    | 2026-11-02 |
| AAPL      | 2026-11-03 |
| AMZN      | 2026-11-03 |
| BZ=F      | 2026-11-03 |
| CL=F      | 2026-11-03 |
| GC=F      | 2026-11-03 |
| GOOGL     | 2026-11-03 |
| HG=F      | 2026-11-03 |
| JPM       | 2026-11-03 |
| META      | 2026-11-03 |
| MSFT      | 2026-11-03 |
| NG=F      | 2026-11-03 |
| NVDA      | 2026-11-03 |
| PL=F      | 2026-11-03 |
| SI=F      | 2026-11-03 |
| TSLA      | 2026-11-03 |
| UNH       | 2026-11-03 |
| XOM       | 2026-11-03 |
| ZC=F      | 2026-11-03 |
| ZS=F      | 2026-11-03 |
| ZW=F      | 2026-11-03 |
| ^DJI      | 2026-11-03 |
| ^FCHI     | 2026-11-03 |
| ^FTSE     | 2026-11-03 |
| ^GDAXI    | 2026-11-03 |
| ^GSPC     | 2026-11-03 |
| ^HSI      | 2026-11-03 |
| ^N225     | 2026-11-02 |
| ^NDX      | 2026-11-03 |
| ^RUT      | 2026-11-03 |
| ^STOXX50E | 2026-11-03 |

## Symbol Details

### DAX / ^GDAXI (score 76.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | +1.1% |
| ret_20d    | +1.6% |
| ret_60d    | -2.0% |
| ma20_dist  | +1.6% |
| ma50_dist  | +1.2% |
| vol_20d    | 13.9% |
| mdd_60d    |  6.6% |
| rsi_14     |  60.1 |
| zscore_20d |   1.3 |

### UnitedHealth Group Inc. / UNH (score 72.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.0% |
| ret_5d     | -1.4% |
| ret_20d    | +7.5% |
| ret_60d    | -1.1% |
| ma20_dist  | +0.8% |
| ma50_dist  | +3.7% |
| vol_20d    | 28.1% |
| mdd_60d    |  9.4% |
| rsi_14     |  55.5 |
| zscore_20d |   0.2 |

### CAC 40 / ^FCHI (score 72.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | +1.7% |
| ret_20d    | +2.0% |
| ret_60d    | -8.0% |
| ma20_dist  | +1.8% |
| ma50_dist  | -0.2% |
| vol_20d    | 12.0% |
| mdd_60d    | 10.9% |
| rsi_14     |  60.3 |
| zscore_20d |   1.7 |

### Tesla Inc. / TSLA (score 70.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.3% |
| ret_5d     |  -2.2% |
| ret_20d    |  +4.7% |
| ret_60d    | +20.4% |
| ma20_dist  |  +4.1% |
| ma50_dist  |  +7.3% |
| vol_20d    |  36.0% |
| mdd_60d    |   7.3% |
| rsi_14     |   64.2 |
| zscore_20d |    1.0 |

### Russell 2000 / ^RUT (score 66.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | -0.2% |
| ret_20d    | -0.6% |
| ret_60d    | -6.8% |
| ma20_dist  | +0.9% |
| ma50_dist  | -1.4% |
| vol_20d    | 15.6% |
| mdd_60d    | 11.3% |
| rsi_14     |  63.9 |
| zscore_20d |   0.7 |

### Dow Jones Industrial Average / ^DJI (score 65.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -1.1% |
| ret_20d    | +0.5% |
| ret_60d    | -4.1% |
| ma20_dist  | -0.5% |
| ma50_dist  | -0.7% |
| vol_20d    |  9.7% |
| mdd_60d    |  5.4% |
| rsi_14     |  52.2 |
| zscore_20d |  -0.6 |

### JPMorgan Chase & Co. / JPM (score 65.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | +0.7% |
| ret_20d    | +2.0% |
| ret_60d    | -6.1% |
| ma20_dist  | +0.7% |
| ma50_dist  | -1.2% |
| vol_20d    | 15.5% |
| mdd_60d    |  9.9% |
| rsi_14     |  53.1 |
| zscore_20d |   0.7 |

### FTSE 100 / ^FTSE (score 64.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.1% |
| ret_5d     | -0.5% |
| ret_20d    | +0.9% |
| ret_60d    | -2.1% |
| ma20_dist  | -0.5% |
| ma50_dist  | -0.6% |
| vol_20d    | 10.3% |
| mdd_60d    |  4.2% |
| rsi_14     |  44.2 |
| zscore_20d |  -0.5 |

### Microsoft Corporation / MSFT (score 62.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.7% |
| ret_5d     | -1.9% |
| ret_20d    | -1.6% |
| ret_60d    | +3.1% |
| ma20_dist  | -1.6% |
| ma50_dist  | +1.3% |
| vol_20d    | 23.4% |
| mdd_60d    |  6.7% |
| rsi_14     |  42.6 |
| zscore_20d |  -1.1 |

### Euro Stoxx 50 / ^STOXX50E (score 59.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | -0.3% |
| ret_20d    | -2.0% |
| ret_60d    | -6.2% |
| ma20_dist  | -0.2% |
| ma50_dist  | -1.8% |
| vol_20d    | 13.9% |
| mdd_60d    |  7.3% |
| rsi_14     |  46.5 |
| zscore_20d |  -0.3 |

### S&P 500 / ^GSPC (score 56.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | -2.0% |
| ret_20d    | -3.2% |
| ret_60d    | -2.4% |
| ma20_dist  | -1.8% |
| ma50_dist  | -1.6% |
| vol_20d    | 11.0% |
| mdd_60d    |  3.5% |
| rsi_14     |  39.2 |
| zscore_20d |  -1.7 |

### Hang Seng / ^HSI (score 52.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | +2.1% |
| ret_20d    | -2.1% |
| ret_60d    | -8.3% |
| ma20_dist  | -0.7% |
| ma50_dist  | -3.9% |
| vol_20d    | 17.4% |
| mdd_60d    | 11.8% |
| rsi_14     |  35.7 |
| zscore_20d |  -0.3 |

### Amazon.com Inc. / AMZN (score 50.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.1% |
| ret_5d     | -1.0% |
| ret_20d    | -2.2% |
| ret_60d    | -9.9% |
| ma20_dist  | -1.2% |
| ma50_dist  | -1.2% |
| vol_20d    | 36.3% |
| mdd_60d    | 11.7% |
| rsi_14     |  47.3 |
| zscore_20d |  -0.5 |

### Apple Inc. / AAPL (score 46.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.9% |
| ret_5d     | -4.4% |
| ret_20d    | -0.5% |
| ret_60d    | +7.7% |
| ma20_dist  | -3.0% |
| ma50_dist  | -0.6% |
| vol_20d    | 17.2% |
| mdd_60d    |  4.9% |
| rsi_14     |  38.5 |
| zscore_20d |  -2.5 |

### Soybeans / ZS=F (score 43.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | -2.1% |
| ret_20d    | -7.7% |
| ret_60d    | +3.3% |
| ma20_dist  | -4.0% |
| ma50_dist  | -5.9% |
| vol_20d    |  8.2% |
| mdd_60d    |  9.4% |
| rsi_14     |  13.5 |
| zscore_20d |  -1.7 |

### Brent Crude Oil / BZ=F (score 42.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.1% |
| ret_5d     |  -9.0% |
| ret_20d    |  +3.0% |
| ret_60d    | +19.0% |
| ma20_dist  |  -5.2% |
| ma50_dist  |  -0.2% |
| vol_20d    |  49.3% |
| mdd_60d    |  11.9% |
| rsi_14     |   46.4 |
| zscore_20d |   -1.1 |

### NASDAQ 100 / ^NDX (score 36.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | -5.0% |
| ret_20d    | -9.7% |
| ret_60d    | -4.9% |
| ma20_dist  | -4.9% |
| ma50_dist  | -5.3% |
| vol_20d    | 22.1% |
| mdd_60d    | 10.4% |
| rsi_14     |  33.0 |
| zscore_20d |  -1.7 |

### Meta Platforms Inc. / META (score 35.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.4% |
| ret_5d     |  +0.1% |
| ret_20d    | -15.9% |
| ret_60d    |  +4.4% |
| ma20_dist  |  -8.5% |
| ma50_dist  |  -7.6% |
| vol_20d    |  37.0% |
| mdd_60d    |  22.0% |
| rsi_14     |   16.8 |
| zscore_20d |   -1.1 |

### NVIDIA Corporation / NVDA (score 32.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.3% |
| ret_5d     |  -5.2% |
| ret_20d    | -13.6% |
| ret_60d    |  -4.9% |
| ma20_dist  |  -5.2% |
| ma50_dist  |  -6.6% |
| vol_20d    |  31.5% |
| mdd_60d    |  15.5% |
| rsi_14     |   36.7 |
| zscore_20d |   -1.3 |

### Gold / GC=F (score 29.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | -3.3% |
| ret_20d    | -5.9% |
| ret_60d    | -9.7% |
| ma20_dist  | -3.7% |
| ma50_dist  | -7.5% |
| vol_20d    | 19.6% |
| mdd_60d    | 17.2% |
| rsi_14     |  36.1 |
| zscore_20d |  -1.7 |

### Corn / ZC=F (score 28.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.3% |
| ret_5d     |  -1.4% |
| ret_20d    | -12.9% |
| ret_60d    |  -3.2% |
| ma20_dist  |  -5.2% |
| ma50_dist  | -11.0% |
| vol_20d    |  15.9% |
| mdd_60d    |  18.5% |
| rsi_14     |    9.9 |
| zscore_20d |   -1.4 |

### Wheat / ZW=F (score 25.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.1% |
| ret_5d     |  -1.7% |
| ret_20d    | -14.8% |
| ret_60d    |  -8.1% |
| ma20_dist  |  -6.3% |
| ma50_dist  | -12.6% |
| vol_20d    |  15.1% |
| mdd_60d    |  21.9% |
| rsi_14     |    8.9 |
| zscore_20d |   -1.3 |

### Alphabet Inc. Class A / GOOGL (score 12.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.4% |
| ret_5d     | -12.6% |
| ret_20d    | -19.5% |
| ret_60d    | -21.6% |
| ma20_dist  | -14.4% |
| ma50_dist  | -16.7% |
| vol_20d    |  46.7% |
| mdd_60d    |  21.4% |
| rsi_14     |   14.9 |
| zscore_20d |   -1.8 |

### Platinum / PL=F (score 10.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.8% |
| ret_5d     |  -6.7% |
| ret_20d    | -15.4% |
| ret_60d    | -17.0% |
| ma20_dist  |  -9.3% |
| ma50_dist  | -15.7% |
| vol_20d    |  30.6% |
| mdd_60d    |  25.2% |
| rsi_14     |   24.2 |
| zscore_20d |   -2.0 |

### Silver / SI=F (score 6.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.2% |
| ret_5d     |  -8.7% |
| ret_20d    | -18.9% |
| ret_60d    | -23.6% |
| ma20_dist  | -10.8% |
| ma50_dist  | -18.6% |
| vol_20d    |  39.8% |
| mdd_60d    |  29.3% |
| rsi_14     |   29.8 |
| zscore_20d |   -1.8 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| DAX / ^GDAXI                        | 331.4855 |           1.3% |                 0.72x |      662.9710 |            2.6% |
| UnitedHealth Group Inc. / UNH       |  11.3071 |           2.8% |                 0.36x |       22.6143 |            5.6% |
| CAC 40 / ^FCHI                      |  92.8600 |           1.2% |                 0.84x |      185.7201 |            2.3% |
| Tesla Inc. / TSLA                   |  14.9864 |           3.8% |                 0.28x |       29.9729 |            7.5% |
| Russell 2000 / ^RUT                 |  36.6207 |           1.3% |                 0.64x |       73.2414 |            2.6% |
| Dow Jones Industrial Average / ^DJI | 522.6766 |           1.0% |                 1.04x |     1045.3532 |            2.0% |
| JPMorgan Chase & Co. / JPM          |   6.0700 |           1.8% |                 0.64x |       12.1400 |            3.6% |
| FTSE 100 / ^FTSE                    | 102.9072 |           1.0% |                 0.97x |      205.8143 |            1.9% |
| Microsoft Corporation / MSFT        |  13.0079 |           2.5% |                 0.43x |       26.0157 |            5.0% |
| Euro Stoxx 50 / ^STOXX50E           |  78.5829 |           1.3% |                 0.72x |      157.1659 |            2.6% |
| S&P 500 / ^GSPC                     |  85.2736 |           1.1% |                 0.91x |      170.5472 |            2.3% |
| Hang Seng / ^HSI                    | 361.6318 |           1.5% |                 0.58x |      723.2637 |            3.1% |
| Amazon.com Inc. / AMZN              |   8.3486 |           3.3% |                 0.28x |       16.6971 |            6.7% |
| Apple Inc. / AAPL                   |   7.3086 |           2.2% |                 0.58x |       14.6171 |            4.4% |
| Soybeans / ZS=F                     |  15.9107 |           1.3% |                 1.22x |       31.8214 |            2.6% |
| Brent Crude Oil / BZ=F              |   4.8743 |           4.7% |                 0.20x |        9.7486 |            9.4% |
| NASDAQ 100 / ^NDX                   | 598.3592 |           2.1% |                 0.45x |     1196.7185 |            4.2% |
| Meta Platforms Inc. / META          |  22.8186 |           3.7% |                 0.27x |       45.6371 |            7.3% |
| NVIDIA Corporation / NVDA           |   6.6071 |           3.2% |                 0.32x |       13.2143 |            6.4% |
| Gold / GC=F                         |  76.0786 |           1.9% |                 0.51x |      152.1571 |            3.9% |
| Corn / ZC=F                         |   6.9464 |           1.6% |                 0.63x |       13.8929 |            3.1% |
| Wheat / ZW=F                        |  13.7321 |           2.3% |                 0.66x |       27.4643 |            4.6% |
| Alphabet Inc. Class A / GOOGL       |  10.3114 |           3.7% |                 0.21x |       20.6229 |            7.4% |
| Platinum / PL=F                     |  30.2500 |           2.1% |                 0.33x |       60.5000 |            4.2% |
| Silver / SI=F                       |   1.2912 |           2.6% |                 0.25x |        2.5824 |            5.2% |

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

Scoring engine version: **1.0.0** | Git commit: **fa5311e**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
