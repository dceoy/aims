+++
title = "Market Analysis 2026-11-10"
date = "2026-11-10T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: AAPL (score 77.3)."
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
source_files = ["data/analysis/2026-11-10.json", "data/history/2026-11-10.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "c7739e5"
+++

## Market Regime

**Neutral** — 13 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Apple Inc. / AAPL** — score 77.3, 20d return +2.9%, RSI14=57. 20d up +2.9%; above MA20 by 2.0%; RSI14=57
- **Amazon.com Inc. / AMZN** — score 73.0, 20d return +2.9%, RSI14=53. 20d up +2.9%; above MA20 by 4.8%; RSI14=53
- **CAC 40 / ^FCHI** — score 73.0, 20d return +5.1%, RSI14=73. 20d up +5.1%; above MA20 by 3.4%; RSI14=73
- **DAX / ^GDAXI** — score 73.0, 20d return +3.9%, RSI14=63. 20d up +3.9%; above MA20 by 2.3%; RSI14=63
- **Microsoft Corporation / MSFT** — score 71.5, 20d return +0.7%, RSI14=55. 20d up +0.7%; above MA20 by 2.6%; RSI14=55

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                   | Applies To |
| ---------- | ----------------------- | ---------- |
| 2026-11-13 | 8306.T earnings release | 8306.T     |
| 2026-11-17 | NVDA earnings release   | NVDA       |

## Signal History

Compared with the previous available report (**2026-11-09**).

- **New top-5:** MSFT
- **Persistent top signals:** ^GDAXI (10 reports), ^FCHI (3 reports), AAPL (2 reports), AMZN (2 reports)
- **Dropped from top-5:** ^HSI

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +0 |    +6.7 |
| 7203.T    |     +0 |    +8.8 |
| 8306.T    |     +2 |   +19.7 |
| AAPL      |     +1 |    +5.5 |
| AMZN      |     +3 |    +4.5 |
| BZ=F      |     -4 |   -17.6 |
| CL=F      |     -2 |   -15.8 |
| GC=F      |     -2 |    -4.5 |
| GOOGL     |     +1 |    -4.8 |
| HG=F      |     +1 |    +2.7 |
| JPM       |     -1 |    +1.5 |
| META      |     +3 |   +10.3 |
| MSFT      |     +2 |    +6.1 |
| NG=F      |     +0 |   +11.5 |
| NVDA      |     +0 |   -13.0 |
| PL=F      |     -1 |    -4.8 |
| SI=F      |     +1 |    -3.0 |
| TSLA      |     +4 |    +7.9 |
| UNH       |     -5 |    -7.3 |
| XOM       |     -2 |    -9.7 |
| ZC=F      |     -2 |    -9.4 |
| ZS=F      |     -4 |   -11.8 |
| ZW=F      |     +1 |    -3.9 |
| ^DJI      |     +3 |    +3.6 |
| ^FCHI     |     -2 |    -3.0 |
| ^FTSE     |     +1 |    -0.9 |
| ^GDAXI    |     -1 |    +2.7 |
| ^GSPC     |     +2 |    +5.2 |
| ^HSI      |     -6 |    -8.5 |
| ^N225     |     +1 |    +8.5 |
| ^NDX      |     +3 |    +5.5 |
| ^RUT      |     +3 |    +4.2 |
| ^STOXX50E |     +0 |    +3.3 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Natural Gas / NG=F** — malformed_input
- **Copper / HG=F** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars
- **WTI Crude Oil / CL=F** — malformed_input

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                    |
| ---: | ---------------------- | ----: | :------: | --------------- | ---------------------------------------------- |
|   15 | Gold / GC=F            |  48.5 |   Yes    | —               | 20d down -1.8%; above MA20 by 0.9%; RSI14=48   |
|   17 | Platinum / PL=F        |  40.0 |   Yes    | —               | 20d down -7.0%; above MA20 by 0.4%; RSI14=40   |
|   19 | Soybeans / ZS=F        |  34.2 |   Yes    | —               | 20d down -8.2%; below MA20 by 4.0%; RSI14=20   |
|   20 | Corn / ZC=F            |  28.8 |   Yes    | —               | 20d down -9.1%; below MA20 by 3.8%; RSI14=21   |
|   21 | Silver / SI=F          |  25.4 |   Yes    | —               | 20d down -12.6%; below MA20 by 2.8%; RSI14=34  |
|   22 | Wheat / ZW=F           |  21.2 |   Yes    | —               | 20d down -12.5%; below MA20 by 5.7%; RSI14=12  |
|   24 | Brent Crude Oil / BZ=F |  14.8 |   Yes    | —               | 20d down -13.2%; below MA20 by 14.1%; RSI14=33 |
|   28 | Natural Gas / NG=F     |  73.6 |    No    | malformed_input | Suppressed: malformed_input                    |
|   29 | Copper / HG=F          |  43.9 |    No    | malformed_input | Suppressed: malformed_input                    |
|   33 | WTI Crude Oil / CL=F   |  21.2 |    No    | malformed_input | Suppressed: malformed_input                    |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                    |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | ---------------------------------------------- |
|    1 | Apple Inc. / AAPL                                                              |  77.3 |   Yes    | —                             | 20d up +2.9%; above MA20 by 2.0%; RSI14=57     |
|    2 | Amazon.com Inc. / AMZN                                                         |  73.0 |   Yes    | —                             | 20d up +2.9%; above MA20 by 4.8%; RSI14=53     |
|    5 | Microsoft Corporation / MSFT                                                   |  71.5 |   Yes    | —                             | 20d up +0.7%; above MA20 by 2.6%; RSI14=55     |
|   11 | JPMorgan Chase & Co. / JPM                                                     |  58.8 |   Yes    | —                             | 20d up +2.3%; above MA20 by 1.4%; RSI14=55     |
|   13 | Tesla Inc. / TSLA                                                              |  51.8 |   Yes    | —                             | 20d up +0.0%; below MA20 by 0.6%; RSI14=51     |
|   14 | UnitedHealth Group Inc. / UNH                                                  |  51.5 |   Yes    | —                             | 20d up +5.0%; below MA20 by 2.0%; RSI14=35     |
|   16 | Meta Platforms Inc. / META                                                     |  44.5 |   Yes    | —                             | 20d down -13.7%; below MA20 by 2.5%; RSI14=37  |
|   23 | Alphabet Inc. Class A / GOOGL                                                  |  19.7 |   Yes    | —                             | 20d down -18.3%; below MA20 by 8.3%; RSI14=24  |
|   25 | NVIDIA Corporation / NVDA                                                      |   4.8 |   Yes    | —                             | 20d down -21.1%; below MA20 by 14.6%; RSI14=27 |
|   26 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  83.3 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   27 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  82.7 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   30 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  43.3 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   31 | Exxon Mobil Corporation / XOM                                                  |  33.0 |    No    | malformed_input               | Suppressed: malformed_input                    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    3 | CAC 40 / ^FCHI                      |  73.0 |   Yes    | —            | 20d up +5.1%; above MA20 by 3.4%; RSI14=73   |
|    4 | DAX / ^GDAXI                        |  73.0 |   Yes    | —            | 20d up +3.9%; above MA20 by 2.3%; RSI14=63   |
|    6 | Euro Stoxx 50 / ^STOXX50E           |  69.7 |   Yes    | —            | 20d up +1.4%; above MA20 by 1.9%; RSI14=60   |
|    7 | FTSE 100 / ^FTSE                    |  63.3 |   Yes    | —            | 20d up +1.2%; above MA20 by 0.4%; RSI14=53   |
|    8 | Dow Jones Industrial Average / ^DJI |  60.9 |   Yes    | —            | 20d up +1.0%; above MA20 by 0.4%; RSI14=49   |
|    9 | Russell 2000 / ^RUT                 |  60.6 |   Yes    | —            | 20d up +1.7%; above MA20 by 1.9%; RSI14=58   |
|   10 | Hang Seng / ^HSI                    |  60.3 |   Yes    | —            | 20d up +1.0%; above MA20 by 3.0%; RSI14=58   |
|   12 | S&P 500 / ^GSPC                     |  52.7 |   Yes    | —            | 20d down -3.3%; below MA20 by 1.2%; RSI14=43 |
|   18 | NASDAQ 100 / ^NDX                   |  36.4 |   Yes    | —            | 20d down -9.0%; below MA20 by 3.6%; RSI14=39 |
|   32 | Nikkei 225 / ^N225                  |  22.7 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-11-09 |
| 7203.T    | 2026-11-09 |
| 8306.T    | 2026-11-09 |
| AAPL      | 2026-11-09 |
| AMZN      | 2026-11-09 |
| BZ=F      | 2026-11-09 |
| CL=F      | 2026-11-09 |
| GC=F      | 2026-11-09 |
| GOOGL     | 2026-11-09 |
| HG=F      | 2026-11-09 |
| JPM       | 2026-11-09 |
| META      | 2026-11-09 |
| MSFT      | 2026-11-09 |
| NG=F      | 2026-11-09 |
| NVDA      | 2026-11-09 |
| PL=F      | 2026-11-09 |
| SI=F      | 2026-11-09 |
| TSLA      | 2026-11-09 |
| UNH       | 2026-11-09 |
| XOM       | 2026-11-09 |
| ZC=F      | 2026-11-09 |
| ZS=F      | 2026-11-09 |
| ZW=F      | 2026-11-09 |
| ^DJI      | 2026-11-09 |
| ^FCHI     | 2026-11-09 |
| ^FTSE     | 2026-11-09 |
| ^GDAXI    | 2026-11-09 |
| ^GSPC     | 2026-11-09 |
| ^HSI      | 2026-11-09 |
| ^N225     | 2026-11-09 |
| ^NDX      | 2026-11-09 |
| ^RUT      | 2026-11-09 |
| ^STOXX50E | 2026-11-09 |

## Symbol Details

### Apple Inc. / AAPL (score 77.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.4% |
| ret_5d     |  +3.7% |
| ret_20d    |  +2.9% |
| ret_60d    | +14.6% |
| ma20_dist  |  +2.0% |
| ma50_dist  |  +4.2% |
| vol_20d    |  26.2% |
| mdd_60d    |   4.9% |
| rsi_14     |   57.5 |
| zscore_20d |    1.6 |

### Amazon.com Inc. / AMZN (score 73.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.9% |
| ret_5d     | +8.7% |
| ret_20d    | +2.9% |
| ret_60d    | +1.6% |
| ma20_dist  | +4.8% |
| ma50_dist  | +5.1% |
| vol_20d    | 41.4% |
| mdd_60d    |  9.8% |
| rsi_14     |  52.8 |
| zscore_20d |   1.7 |

### CAC 40 / ^FCHI (score 73.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.2% |
| ret_5d     | +2.3% |
| ret_20d    | +5.1% |
| ret_60d    | -4.0% |
| ma20_dist  | +3.4% |
| ma50_dist  | +2.6% |
| vol_20d    | 13.0% |
| mdd_60d    |  9.2% |
| rsi_14     |  72.9 |
| zscore_20d |   2.1 |

### DAX / ^GDAXI (score 73.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.7% |
| ret_5d     | +1.1% |
| ret_20d    | +3.9% |
| ret_60d    | -0.3% |
| ma20_dist  | +2.3% |
| ma50_dist  | +2.8% |
| vol_20d    | 16.4% |
| mdd_60d    |  6.6% |
| rsi_14     |  62.7 |
| zscore_20d |   1.6 |

### Microsoft Corporation / MSFT (score 71.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.7% |
| ret_5d     |  +7.5% |
| ret_20d    |  +0.7% |
| ret_60d    | +10.3% |
| ma20_dist  |  +2.6% |
| ma50_dist  |  +5.4% |
| vol_20d    |  35.6% |
| mdd_60d    |   6.7% |
| rsi_14     |   54.8 |
| zscore_20d |    1.4 |

### Euro Stoxx 50 / ^STOXX50E (score 69.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.9% |
| ret_5d     | +1.9% |
| ret_20d    | +1.4% |
| ret_60d    | -3.7% |
| ma20_dist  | +1.9% |
| ma50_dist  | +0.8% |
| vol_20d    | 16.1% |
| mdd_60d    |  6.4% |
| rsi_14     |  59.9 |
| zscore_20d |   2.2 |

### FTSE 100 / ^FTSE (score 63.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.0% |
| ret_5d     | +0.2% |
| ret_20d    | +1.2% |
| ret_60d    | +0.3% |
| ma20_dist  | +0.4% |
| ma50_dist  | +0.8% |
| vol_20d    | 11.9% |
| mdd_60d    |  4.2% |
| rsi_14     |  52.8 |
| zscore_20d |   0.7 |

### Dow Jones Industrial Average / ^DJI (score 60.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.2% |
| ret_5d     | +0.8% |
| ret_20d    | +1.0% |
| ret_60d    | -2.5% |
| ma20_dist  | +0.4% |
| ma50_dist  | +0.7% |
| vol_20d    | 20.0% |
| mdd_60d    |  5.2% |
| rsi_14     |  49.3 |
| zscore_20d |   0.4 |

### Russell 2000 / ^RUT (score 60.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +3.1% |
| ret_5d     | +1.2% |
| ret_20d    | +1.7% |
| ret_60d    | -7.4% |
| ma20_dist  | +1.9% |
| ma50_dist  | +0.2% |
| vol_20d    | 25.1% |
| mdd_60d    | 11.0% |
| rsi_14     |  57.6 |
| zscore_20d |   1.3 |

### Hang Seng / ^HSI (score 60.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | +4.5% |
| ret_20d    | +1.0% |
| ret_60d    | -3.7% |
| ma20_dist  | +3.0% |
| ma50_dist  | +0.2% |
| vol_20d    | 21.1% |
| mdd_60d    | 11.8% |
| rsi_14     |  57.7 |
| zscore_20d |   1.2 |

### JPMorgan Chase & Co. / JPM (score 58.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.3% |
| ret_5d     | +0.4% |
| ret_20d    | +2.3% |
| ret_60d    | -5.7% |
| ma20_dist  | +1.4% |
| ma50_dist  | +0.4% |
| vol_20d    | 27.3% |
| mdd_60d    |  9.4% |
| rsi_14     |  54.8 |
| zscore_20d |   1.0 |

### S&P 500 / ^GSPC (score 52.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.3% |
| ret_5d     | +0.1% |
| ret_20d    | -3.3% |
| ret_60d    | -3.0% |
| ma20_dist  | -1.2% |
| ma50_dist  | -1.6% |
| vol_20d    | 21.3% |
| mdd_60d    |  5.9% |
| rsi_14     |  43.1 |
| zscore_20d |  -0.8 |

### Tesla Inc. / TSLA (score 51.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +5.5% |
| ret_5d     |  -6.4% |
| ret_20d    |  +0.0% |
| ret_60d    | +10.5% |
| ma20_dist  |  -0.6% |
| ma50_dist  |  +1.4% |
| vol_20d    |  58.6% |
| mdd_60d    |  15.7% |
| rsi_14     |   51.3 |
| zscore_20d |   -0.1 |

### UnitedHealth Group Inc. / UNH (score 51.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | -0.7% |
| ret_20d    | +5.0% |
| ret_60d    | -0.4% |
| ma20_dist  | -2.0% |
| ma50_dist  | +1.9% |
| vol_20d    | 29.9% |
| mdd_60d    |  8.4% |
| rsi_14     |  34.6 |
| zscore_20d |  -0.8 |

### Gold / GC=F (score 48.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.0% |
| ret_5d     | +3.7% |
| ret_20d    | -1.8% |
| ret_60d    | -6.9% |
| ma20_dist  | +0.9% |
| ma50_dist  | -2.5% |
| vol_20d    | 23.2% |
| mdd_60d    | 17.2% |
| rsi_14     |  48.1 |
| zscore_20d |   0.5 |

### Meta Platforms Inc. / META (score 44.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +5.1% |
| ret_5d     |  +5.7% |
| ret_20d    | -13.7% |
| ret_60d    |  +8.7% |
| ma20_dist  |  -2.5% |
| ma50_dist  |  -5.1% |
| vol_20d    |  42.0% |
| mdd_60d    |  22.2% |
| rsi_14     |   36.9 |
| zscore_20d |   -0.3 |

### Platinum / PL=F (score 40.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.5% |
| ret_5d     | +7.0% |
| ret_20d    | -7.0% |
| ret_60d    | -9.6% |
| ma20_dist  | +0.4% |
| ma50_dist  | -6.8% |
| vol_20d    | 33.7% |
| mdd_60d    | 25.2% |
| rsi_14     |  39.6 |
| zscore_20d |   0.1 |

### NASDAQ 100 / ^NDX (score 36.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +3.4% |
| ret_5d     | -0.3% |
| ret_20d    | -9.0% |
| ret_60d    | -7.1% |
| ma20_dist  | -3.6% |
| ma50_dist  | -5.7% |
| vol_20d    | 34.0% |
| mdd_60d    | 14.7% |
| rsi_14     |  39.3 |
| zscore_20d |  -1.0 |

### Soybeans / ZS=F (score 34.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | -1.9% |
| ret_20d    | -8.2% |
| ret_60d    | -1.6% |
| ma20_dist  | -4.0% |
| ma50_dist  | -7.1% |
| vol_20d    |  9.0% |
| mdd_60d    | 11.1% |
| rsi_14     |  19.9 |
| zscore_20d |  -1.6 |

### Corn / ZC=F (score 28.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.5% |
| ret_5d     |  -2.0% |
| ret_20d    |  -9.1% |
| ret_60d    |  -5.5% |
| ma20_dist  |  -3.8% |
| ma50_dist  | -10.7% |
| vol_20d    |   9.8% |
| mdd_60d    |  19.1% |
| rsi_14     |   20.6 |
| zscore_20d |   -1.3 |

### Silver / SI=F (score 25.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.5% |
| ret_5d     |  +3.6% |
| ret_20d    | -12.6% |
| ret_60d    | -17.8% |
| ma20_dist  |  -2.8% |
| ma50_dist  | -11.9% |
| vol_20d    |  43.9% |
| mdd_60d    |  29.3% |
| rsi_14     |   34.3 |
| zscore_20d |   -0.5 |

### Wheat / ZW=F (score 21.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.5% |
| ret_5d     |  -3.1% |
| ret_20d    | -12.5% |
| ret_60d    | -12.9% |
| ma20_dist  |  -5.7% |
| ma50_dist  | -12.9% |
| vol_20d    |  13.4% |
| mdd_60d    |  23.3% |
| rsi_14     |   12.0 |
| zscore_20d |   -1.3 |

### Alphabet Inc. Class A / GOOGL (score 19.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.2% |
| ret_5d     |  +3.3% |
| ret_20d    | -18.3% |
| ret_60d    | -16.6% |
| ma20_dist  |  -8.3% |
| ma50_dist  | -13.1% |
| vol_20d    |  49.1% |
| mdd_60d    |  21.4% |
| rsi_14     |   23.8 |
| zscore_20d |   -1.0 |

### Brent Crude Oil / BZ=F (score 14.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -5.8% |
| ret_5d     | -11.6% |
| ret_20d    | -13.2% |
| ret_60d    |  +1.7% |
| ma20_dist  | -14.1% |
| ma50_dist  | -11.3% |
| vol_20d    |  60.4% |
| mdd_60d    |  21.3% |
| rsi_14     |   33.1 |
| zscore_20d |   -2.1 |

### NVIDIA Corporation / NVDA (score 4.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -4.3% |
| ret_5d     | -11.6% |
| ret_20d    | -21.1% |
| ret_60d    | -20.6% |
| ma20_dist  | -14.6% |
| ma50_dist  | -18.4% |
| vol_20d    |  46.8% |
| mdd_60d    |  25.3% |
| rsi_14     |   27.0 |
| zscore_20d |   -2.3 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Apple Inc. / AAPL                   |   9.4171 |           2.7% |                 0.38x |       18.8343 |            5.4% |
| Amazon.com Inc. / AMZN              |  10.5571 |           4.0% |                 0.24x |       21.1143 |            7.9% |
| CAC 40 / ^FCHI                      | 108.9986 |           1.3% |                 0.77x |      217.9972 |            2.6% |
| DAX / ^GDAXI                        | 399.9307 |           1.5% |                 0.61x |      799.8613 |            3.0% |
| Microsoft Corporation / MSFT        |  16.5400 |           3.0% |                 0.28x |       33.0800 |            6.1% |
| Euro Stoxx 50 / ^STOXX50E           |  94.1601 |           1.5% |                 0.62x |      188.3202 |            3.0% |
| FTSE 100 / ^FTSE                    | 122.0001 |           1.1% |                 0.84x |      244.0001 |            2.3% |
| Dow Jones Industrial Average / ^DJI | 770.8901 |           1.5% |                 0.50x |     1541.7801 |            2.9% |
| Russell 2000 / ^RUT                 |  48.0593 |           1.7% |                 0.40x |       96.1185 |            3.4% |
| Hang Seng / ^HSI                    | 419.1105 |           1.7% |                 0.47x |      838.2210 |            3.4% |
| JPMorgan Chase & Co. / JPM          |   8.0136 |           2.3% |                 0.37x |       16.0271 |            4.7% |
| S&P 500 / ^GSPC                     | 114.8615 |           1.5% |                 0.47x |      229.7230 |            3.0% |
| Tesla Inc. / TSLA                   |  18.7014 |           4.9% |                 0.17x |       37.4029 |            9.9% |
| UnitedHealth Group Inc. / UNH       |  11.2321 |           2.8% |                 0.33x |       22.4643 |            5.6% |
| Gold / GC=F                         |  88.5786 |           2.2% |                 0.43x |      177.1571 |            4.3% |
| Meta Platforms Inc. / META          |  24.7357 |           3.9% |                 0.24x |       49.4714 |            7.7% |
| Platinum / PL=F                     |  36.1357 |           2.3% |                 0.30x |       72.2714 |            4.6% |
| NASDAQ 100 / ^NDX                   | 716.8429 |           2.6% |                 0.29x |     1433.6858 |            5.1% |
| Soybeans / ZS=F                     |  16.5893 |           1.4% |                 1.11x |       33.1786 |            2.8% |
| Corn / ZC=F                         |   6.7321 |           1.5% |                 1.02x |       13.4643 |            3.1% |
| Silver / SI=F                       |   1.5014 |           2.9% |                 0.23x |        3.0029 |            5.7% |
| Wheat / ZW=F                        |  13.0893 |           2.2% |                 0.74x |       26.1786 |            4.5% |
| Alphabet Inc. Class A / GOOGL       |  11.6643 |           4.0% |                 0.20x |       23.3286 |            8.1% |
| Brent Crude Oil / BZ=F              |   5.6857 |           6.1% |                 0.17x |       11.3714 |           12.3% |
| NVIDIA Corporation / NVDA           |   8.7850 |           4.9% |                 0.21x |       17.5700 |            9.8% |

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

Scoring engine version: **1.0.0** | Git commit: **c7739e5**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
