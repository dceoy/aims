+++
title = "Market Analysis 2026-11-02"
date = "2026-11-02T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: BZ=F (score 83.3)."
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
source_files = ["data/analysis/2026-11-02.json", "data/history/2026-11-02.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "5e6d0e0"
+++

## Market Regime

**Neutral** — 9 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Brent Crude Oil / BZ=F** — score 83.3, 20d return +15.1%, RSI14=75. 20d up +15.1%; above MA20 by 8.0%; RSI14=75
- **Tesla Inc. / TSLA** — score 75.5, 20d return +7.9%, RSI14=60. 20d up +7.9%; above MA20 by 5.0%; RSI14=60
- **DAX / ^GDAXI** — score 74.8, 20d return +2.3%, RSI14=60. 20d up +2.3%; above MA20 by 1.7%; RSI14=60
- **FTSE 100 / ^FTSE** — score 72.1, 20d return +2.6%, RSI14=55. 20d up +2.6%; above MA20 by 0.5%; RSI14=55
- **Apple Inc. / AAPL** — score 71.5, 20d return +3.3%, RSI14=55. 20d up +3.3%; above MA20 by 0.7%; RSI14=55

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                   | Applies To |
| ---------- | ----------------------- | ---------- |
| 2026-11-05 | 6758.T earnings release | 6758.T     |
| 2026-11-05 | 7203.T earnings release | 7203.T     |

## Signal History

Compared with the previous available report (**2026-10-30**).

- **New top-5:** ^FTSE
- **Persistent top signals:** BZ=F (11 reports), TSLA (5 reports), AAPL (4 reports), ^GDAXI (4 reports)
- **Dropped from top-5:** JPM

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +1 |    +8.5 |
| 7203.T    |     -1 |    +3.9 |
| 8306.T    |     +2 |    +3.6 |
| AAPL      |     -4 |    -7.6 |
| AMZN      |     +3 |    +4.5 |
| BZ=F      |     +3 |    +9.1 |
| CL=F      |     +1 |   +10.6 |
| GC=F      |     -3 |    -7.9 |
| GOOGL     |     +1 |    +4.5 |
| HG=F      |     -2 |    -7.9 |
| JPM       |     -4 |   -11.5 |
| META      |     -2 |    -5.8 |
| MSFT      |     -2 |    -7.0 |
| NG=F      |     -1 |    -6.4 |
| NVDA      |     -6 |   -10.9 |
| PL=F      |     +0 |    -0.6 |
| SI=F      |     -1 |    -3.0 |
| TSLA      |     +1 |    +0.6 |
| UNH       |     -1 |    -0.3 |
| XOM       |     +0 |    +5.5 |
| ZC=F      |     +4 |    +7.6 |
| ZS=F      |     +1 |   +12.7 |
| ZW=F      |     +3 |    +5.5 |
| ^DJI      |     +3 |    +0.0 |
| ^FCHI     |     +4 |    +6.7 |
| ^FTSE     |     +3 |    +8.5 |
| ^GDAXI    |     -1 |    -2.7 |
| ^GSPC     |     -1 |    -7.6 |
| ^HSI      |     +3 |   +15.5 |
| ^N225     |     +0 |    -9.1 |
| ^NDX      |     -3 |   -10.6 |
| ^RUT      |     -2 |    -7.3 |
| ^STOXX50E |     +1 |    -1.2 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Exxon Mobil Corporation / XOM** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **Natural Gas / NG=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                    |
| ---: | ---------------------- | ----: | :------: | --------------- | ---------------------------------------------- |
|    1 | Brent Crude Oil / BZ=F |  83.3 |   Yes    | —               | 20d up +15.1%; above MA20 by 8.0%; RSI14=75    |
|   14 | Soybeans / ZS=F        |  50.0 |   Yes    | —               | 20d down -4.4%; below MA20 by 3.1%; RSI14=15   |
|   16 | Corn / ZC=F            |  34.5 |   Yes    | —               | 20d down -10.0%; below MA20 by 5.2%; RSI14=10  |
|   18 | Wheat / ZW=F           |  27.0 |   Yes    | —               | 20d down -11.6%; below MA20 by 7.1%; RSI14=10  |
|   20 | Gold / GC=F            |  22.1 |   Yes    | —               | 20d down -6.3%; below MA20 by 5.3%; RSI14=25   |
|   23 | Platinum / PL=F        |   9.7 |   Yes    | —               | 20d down -14.6%; below MA20 by 10.4%; RSI14=16 |
|   25 | Silver / SI=F          |   4.5 |   Yes    | —               | 20d down -18.1%; below MA20 by 13.4%; RSI14=17 |
|   27 | WTI Crude Oil / CL=F   |  73.9 |    No    | malformed_input | Suppressed: malformed_input                    |
|   31 | Copper / HG=F          |  48.8 |    No    | malformed_input | Suppressed: malformed_input                    |
|   32 | Natural Gas / NG=F     |  43.3 |    No    | malformed_input | Suppressed: malformed_input                    |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                    |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | ---------------------------------------------- |
|    2 | Tesla Inc. / TSLA                                                              |  75.5 |   Yes    | —                             | 20d up +7.9%; above MA20 by 5.0%; RSI14=60     |
|    5 | Apple Inc. / AAPL                                                              |  71.5 |   Yes    | —                             | 20d up +3.3%; above MA20 by 0.7%; RSI14=55     |
|    7 | UnitedHealth Group Inc. / UNH                                                  |  64.5 |   Yes    | —                             | 20d up +9.4%; above MA20 by 2.1%; RSI14=66     |
|    9 | JPMorgan Chase & Co. / JPM                                                     |  59.4 |   Yes    | —                             | 20d up +1.9%; above MA20 by 0.7%; RSI14=53     |
|   11 | Microsoft Corporation / MSFT                                                   |  54.9 |   Yes    | —                             | 20d up +0.8%; below MA20 by 1.7%; RSI14=36     |
|   19 | Amazon.com Inc. / AMZN                                                         |  25.1 |   Yes    | —                             | 20d down -4.4%; below MA20 by 5.5%; RSI14=34   |
|   21 | Meta Platforms Inc. / META                                                     |  21.8 |   Yes    | —                             | 20d down -15.5%; below MA20 by 11.0%; RSI14=18 |
|   22 | NVIDIA Corporation / NVDA                                                      |  19.7 |   Yes    | —                             | 20d down -12.5%; below MA20 by 7.6%; RSI14=31  |
|   24 | Alphabet Inc. Class A / GOOGL                                                  |   7.6 |   Yes    | —                             | 20d down -18.5%; below MA20 by 16.2%; RSI14=14 |
|   26 | Exxon Mobil Corporation / XOM                                                  |  85.8 |    No    | malformed_input               | Suppressed: malformed_input                    |
|   28 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  69.1 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   29 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  64.5 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   30 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  52.1 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    3 | DAX / ^GDAXI                        |  74.8 |   Yes    | —            | 20d up +2.3%; above MA20 by 1.7%; RSI14=60   |
|    4 | FTSE 100 / ^FTSE                    |  72.1 |   Yes    | —            | 20d up +2.6%; above MA20 by 0.5%; RSI14=55   |
|    6 | CAC 40 / ^FCHI                      |  68.2 |   Yes    | —            | 20d up +0.9%; above MA20 by 1.4%; RSI14=60   |
|    8 | Dow Jones Industrial Average / ^DJI |  60.9 |   Yes    | —            | 20d up +1.2%; below MA20 by 0.4%; RSI14=49   |
|   10 | Russell 2000 / ^RUT                 |  55.8 |   Yes    | —            | 20d down -0.7%; above MA20 by 0.8%; RSI14=52 |
|   12 | Euro Stoxx 50 / ^STOXX50E           |  54.9 |   Yes    | —            | 20d down -1.7%; below MA20 by 0.6%; RSI14=45 |
|   13 | S&P 500 / ^GSPC                     |  51.2 |   Yes    | —            | 20d down -1.8%; below MA20 by 1.9%; RSI14=34 |
|   15 | Hang Seng / ^HSI                    |  44.5 |   Yes    | —            | 20d down -5.4%; below MA20 by 1.9%; RSI14=33 |
|   17 | NASDAQ 100 / ^NDX                   |  31.5 |   Yes    | —            | 20d down -7.9%; below MA20 by 5.2%; RSI14=29 |
|   33 | Nikkei 225 / ^N225                  |  37.3 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-10-30 |
| 7203.T    | 2026-10-30 |
| 8306.T    | 2026-10-30 |
| AAPL      | 2026-10-30 |
| AMZN      | 2026-10-30 |
| BZ=F      | 2026-10-30 |
| CL=F      | 2026-10-30 |
| GC=F      | 2026-10-30 |
| GOOGL     | 2026-10-30 |
| HG=F      | 2026-10-30 |
| JPM       | 2026-10-30 |
| META      | 2026-10-30 |
| MSFT      | 2026-10-30 |
| NG=F      | 2026-10-30 |
| NVDA      | 2026-10-30 |
| PL=F      | 2026-10-30 |
| SI=F      | 2026-10-30 |
| TSLA      | 2026-10-30 |
| UNH       | 2026-10-30 |
| XOM       | 2026-10-30 |
| ZC=F      | 2026-10-30 |
| ZS=F      | 2026-10-30 |
| ZW=F      | 2026-10-30 |
| ^DJI      | 2026-10-30 |
| ^FCHI     | 2026-10-30 |
| ^FTSE     | 2026-10-30 |
| ^GDAXI    | 2026-10-30 |
| ^GSPC     | 2026-10-30 |
| ^HSI      | 2026-10-30 |
| ^N225     | 2026-10-30 |
| ^NDX      | 2026-10-30 |
| ^RUT      | 2026-10-30 |
| ^STOXX50E | 2026-10-30 |

## Symbol Details

### Brent Crude Oil / BZ=F (score 83.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.4% |
| ret_5d     |  +0.8% |
| ret_20d    | +15.1% |
| ret_60d    | +32.3% |
| ma20_dist  |  +8.0% |
| ma50_dist  | +13.9% |
| vol_20d    |  28.8% |
| mdd_60d    |   8.7% |
| rsi_14     |   75.1 |
| zscore_20d |    1.6 |

### Tesla Inc. / TSLA (score 75.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.9% |
| ret_5d     |  +7.4% |
| ret_20d    |  +7.9% |
| ret_60d    | +25.1% |
| ma20_dist  |  +5.0% |
| ma50_dist  |  +8.2% |
| vol_20d    |  36.0% |
| mdd_60d    |   7.3% |
| rsi_14     |   59.7 |
| zscore_20d |    1.4 |

### DAX / ^GDAXI (score 74.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.9% |
| ret_5d     | +2.5% |
| ret_20d    | +2.3% |
| ret_60d    | -1.9% |
| ma20_dist  | +1.7% |
| ma50_dist  | +0.9% |
| vol_20d    | 13.9% |
| mdd_60d    |  6.6% |
| rsi_14     |  60.5 |
| zscore_20d |   1.5 |

### FTSE 100 / ^FTSE (score 72.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | +0.4% |
| ret_20d    | +2.6% |
| ret_60d    | -1.3% |
| ma20_dist  | +0.5% |
| ma50_dist  | +0.2% |
| vol_20d    |  9.5% |
| mdd_60d    |  4.3% |
| rsi_14     |  55.5 |
| zscore_20d |   0.5 |

### Apple Inc. / AAPL (score 71.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.2% |
| ret_5d     |  -0.9% |
| ret_20d    |  +3.3% |
| ret_60d    | +10.4% |
| ma20_dist  |  +0.7% |
| ma50_dist  |  +3.5% |
| vol_20d    |  14.2% |
| mdd_60d    |   3.9% |
| rsi_14     |   54.9 |
| zscore_20d |    0.6 |

### CAC 40 / ^FCHI (score 68.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.0% |
| ret_5d     | +2.4% |
| ret_20d    | +0.9% |
| ret_60d    | -8.6% |
| ma20_dist  | +1.4% |
| ma50_dist  | -1.1% |
| vol_20d    | 11.9% |
| mdd_60d    | 11.4% |
| rsi_14     |  60.3 |
| zscore_20d |   1.7 |

### UnitedHealth Group Inc. / UNH (score 64.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | -2.7% |
| ret_20d    | +9.4% |
| ret_60d    | +0.7% |
| ma20_dist  | +2.1% |
| ma50_dist  | +4.5% |
| vol_20d    | 27.8% |
| mdd_60d    | 10.7% |
| rsi_14     |  66.1 |
| zscore_20d |   0.5 |

### Dow Jones Industrial Average / ^DJI (score 60.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.1% |
| ret_5d     | -0.9% |
| ret_20d    | +1.2% |
| ret_60d    | -3.9% |
| ma20_dist  | -0.4% |
| ma50_dist  | -0.8% |
| vol_20d    |  9.6% |
| mdd_60d    |  5.8% |
| rsi_14     |  48.9 |
| zscore_20d |  -0.5 |

### JPMorgan Chase & Co. / JPM (score 59.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.9% |
| ret_5d     | +1.6% |
| ret_20d    | +1.9% |
| ret_60d    | -5.4% |
| ma20_dist  | +0.7% |
| ma50_dist  | -1.6% |
| vol_20d    | 14.8% |
| mdd_60d    |  9.9% |
| rsi_14     |  53.1 |
| zscore_20d |   0.7 |

### Russell 2000 / ^RUT (score 55.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.7% |
| ret_5d     | +1.3% |
| ret_20d    | -0.7% |
| ret_60d    | -6.3% |
| ma20_dist  | +0.8% |
| ma50_dist  | -1.7% |
| vol_20d    | 15.8% |
| mdd_60d    | 11.3% |
| rsi_14     |  52.5 |
| zscore_20d |   0.6 |

### Microsoft Corporation / MSFT (score 54.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.6% |
| ret_5d     | -0.5% |
| ret_20d    | +0.8% |
| ret_60d    | +4.6% |
| ma20_dist  | -1.7% |
| ma50_dist  | +1.8% |
| vol_20d    | 19.7% |
| mdd_60d    |  5.1% |
| rsi_14     |  36.2 |
| zscore_20d |  -1.5 |

### Euro Stoxx 50 / ^STOXX50E (score 54.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.2% |
| ret_5d     | +1.0% |
| ret_20d    | -1.7% |
| ret_60d    | -6.0% |
| ma20_dist  | -0.6% |
| ma50_dist  | -2.2% |
| vol_20d    | 13.6% |
| mdd_60d    |  7.4% |
| rsi_14     |  44.5 |
| zscore_20d |  -0.7 |

### S&P 500 / ^GSPC (score 51.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.8% |
| ret_5d     | -0.6% |
| ret_20d    | -1.8% |
| ret_60d    | -1.7% |
| ma20_dist  | -1.9% |
| ma50_dist  | -1.5% |
| vol_20d    | 11.4% |
| mdd_60d    |  3.2% |
| rsi_14     |  34.1 |
| zscore_20d |  -2.3 |

### Soybeans / ZS=F (score 50.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | -2.7% |
| ret_20d    | -4.4% |
| ret_60d    | +5.6% |
| ma20_dist  | -3.1% |
| ma50_dist  | -4.5% |
| vol_20d    | 10.4% |
| mdd_60d    |  8.2% |
| rsi_14     |  14.8 |
| zscore_20d |  -1.5 |

### Hang Seng / ^HSI (score 44.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.5% |
| ret_5d     |  +0.9% |
| ret_20d    |  -5.4% |
| ret_60d    | -10.1% |
| ma20_dist  |  -1.9% |
| ma50_dist  |  -5.2% |
| vol_20d    |  19.2% |
| mdd_60d    |  11.8% |
| rsi_14     |   33.4 |
| zscore_20d |   -0.9 |

### Corn / ZC=F (score 34.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.8% |
| ret_5d     |  -1.8% |
| ret_20d    | -10.0% |
| ret_60d    |  +2.2% |
| ma20_dist  |  -5.2% |
| ma50_dist  | -10.4% |
| vol_20d    |  18.4% |
| mdd_60d    |  17.5% |
| rsi_14     |    9.7 |
| zscore_20d |   -1.3 |

### NASDAQ 100 / ^NDX (score 31.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -3.5% |
| ret_5d     | -2.0% |
| ret_20d    | -7.9% |
| ret_60d    | -3.4% |
| ma20_dist  | -5.2% |
| ma50_dist  | -4.7% |
| vol_20d    | 22.2% |
| mdd_60d    |  9.1% |
| rsi_14     |  28.6 |
| zscore_20d |  -1.9 |

### Wheat / ZW=F (score 27.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.0% |
| ret_5d     |  -3.4% |
| ret_20d    | -11.6% |
| ret_60d    |  -5.8% |
| ma20_dist  |  -7.1% |
| ma50_dist  | -12.5% |
| vol_20d    |  18.4% |
| mdd_60d    |  21.9% |
| rsi_14     |   10.4 |
| zscore_20d |   -1.4 |

### Amazon.com Inc. / AMZN (score 25.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.4% |
| ret_5d     |  -3.1% |
| ret_20d    |  -4.4% |
| ret_60d    | -11.7% |
| ma20_dist  |  -5.5% |
| ma50_dist  |  -5.5% |
| vol_20d    |  35.2% |
| mdd_60d    |  13.6% |
| rsi_14     |   33.7 |
| zscore_20d |   -2.3 |

### Gold / GC=F (score 22.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -3.3% |
| ret_5d     |  -2.7% |
| ret_20d    |  -6.3% |
| ret_60d    | -11.0% |
| ma20_dist  |  -5.3% |
| ma50_dist  |  -9.1% |
| vol_20d    |  18.5% |
| mdd_60d    |  17.2% |
| rsi_14     |   25.1 |
| zscore_20d |   -2.8 |

### Meta Platforms Inc. / META (score 21.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.5% |
| ret_5d     |  -4.3% |
| ret_20d    | -15.5% |
| ret_60d    |  +4.3% |
| ma20_dist  | -11.0% |
| ma50_dist  |  -8.2% |
| vol_20d    |  36.5% |
| mdd_60d    |  21.2% |
| rsi_14     |   17.6 |
| zscore_20d |   -1.5 |

### NVIDIA Corporation / NVDA (score 19.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -4.2% |
| ret_5d     |  -3.0% |
| ret_20d    | -12.5% |
| ret_60d    |  -6.6% |
| ma20_dist  |  -7.6% |
| ma50_dist  |  -7.7% |
| vol_20d    |  31.4% |
| mdd_60d    |  14.5% |
| rsi_14     |   31.0 |
| zscore_20d |   -1.8 |

### Platinum / PL=F (score 9.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -3.8% |
| ret_5d     |  -7.5% |
| ret_20d    | -14.6% |
| ret_60d    | -17.6% |
| ma20_dist  | -10.4% |
| ma50_dist  | -16.2% |
| vol_20d    |  30.3% |
| mdd_60d    |  24.9% |
| rsi_14     |   16.3 |
| zscore_20d |   -2.4 |

### Alphabet Inc. Class A / GOOGL (score 7.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.4% |
| ret_5d     | -12.6% |
| ret_20d    | -18.5% |
| ret_60d    | -21.7% |
| ma20_dist  | -16.2% |
| ma50_dist  | -17.5% |
| vol_20d    |  47.1% |
| mdd_60d    |  21.7% |
| rsi_14     |   14.1 |
| zscore_20d |   -2.6 |

### Silver / SI=F (score 4.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -5.9% |
| ret_5d     |  -8.6% |
| ret_20d    | -18.1% |
| ret_60d    | -24.2% |
| ma20_dist  | -13.4% |
| ma50_dist  | -20.4% |
| vol_20d    |  38.0% |
| mdd_60d    |  29.3% |
| rsi_14     |   16.7 |
| zscore_20d |   -2.4 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Brent Crude Oil / BZ=F              |   3.6964 |           3.1% |                 0.35x |        7.3929 |            6.3% |
| Tesla Inc. / TSLA                   |  14.3829 |           3.6% |                 0.28x |       28.7657 |            7.2% |
| DAX / ^GDAXI                        | 315.2019 |           1.2% |                 0.72x |      630.4037 |            2.4% |
| FTSE 100 / ^FTSE                    | 102.6214 |           1.0% |                 1.06x |      205.2429 |            1.9% |
| Apple Inc. / AAPL                   |   6.6964 |           1.9% |                 0.70x |       13.3929 |            3.9% |
| CAC 40 / ^FCHI                      |  85.8408 |           1.1% |                 0.84x |      171.6816 |            2.2% |
| UnitedHealth Group Inc. / UNH       |  12.9207 |           3.2% |                 0.36x |       25.8414 |            6.3% |
| Dow Jones Industrial Average / ^DJI | 536.1448 |           1.0% |                 1.04x |     1072.2896 |            2.1% |
| JPMorgan Chase & Co. / JPM          |   6.9750 |           2.1% |                 0.67x |       13.9500 |            4.1% |
| Russell 2000 / ^RUT                 |  37.9786 |           1.4% |                 0.63x |       75.9571 |            2.7% |
| Microsoft Corporation / MSFT        |  11.7379 |           2.2% |                 0.51x |       23.4757 |            4.5% |
| Euro Stoxx 50 / ^STOXX50E           |  74.5136 |           1.2% |                 0.73x |      149.0273 |            2.4% |
| S&P 500 / ^GSPC                     |  82.7108 |           1.1% |                 0.87x |      165.4215 |            2.2% |
| Soybeans / ZS=F                     |  16.5357 |           1.4% |                 0.97x |       33.0714 |            2.7% |
| Hang Seng / ^HSI                    | 372.0445 |           1.6% |                 0.52x |      744.0890 |            3.2% |
| Corn / ZC=F                         |   7.1964 |           1.6% |                 0.54x |       14.3929 |            3.2% |
| NASDAQ 100 / ^NDX                   | 590.9869 |           2.1% |                 0.45x |     1181.9738 |            4.2% |
| Wheat / ZW=F                        |  14.1607 |           2.3% |                 0.54x |       28.3214 |            4.7% |
| Amazon.com Inc. / AMZN              |   7.7150 |           3.2% |                 0.28x |       15.4300 |            6.4% |
| Gold / GC=F                         |  74.9500 |           1.9% |                 0.54x |      149.8999 |            3.8% |
| Meta Platforms Inc. / META          |  25.0507 |           4.1% |                 0.27x |       50.1014 |            8.1% |
| NVIDIA Corporation / NVDA           |   6.5400 |           3.2% |                 0.32x |       13.0800 |            6.4% |
| Platinum / PL=F                     |  32.4286 |           2.3% |                 0.33x |       64.8571 |            4.5% |
| Alphabet Inc. Class A / GOOGL       |  10.8421 |           3.9% |                 0.21x |       21.6843 |            7.7% |
| Silver / SI=F                       |   1.3375 |           2.7% |                 0.26x |        2.6750 |            5.4% |

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

Scoring engine version: **1.0.0** | Git commit: **5e6d0e0**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
