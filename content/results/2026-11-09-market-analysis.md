+++
title = "Market Analysis 2026-11-09"
date = "2026-11-09T00:00:00+00:00"
draft = false
summary = "Bearish market: 25 reliable instruments. Top signal: ^FCHI (score 76.1)."
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
source_files = ["data/analysis/2026-11-09.json", "data/history/2026-11-09.json"]
market_regime = "Bearish"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "165a9a7"
+++

## Market Regime

**Bearish** — 5 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **CAC 40 / ^FCHI** — score 76.1, 20d return +4.3%, RSI14=67. 20d up +4.3%; above MA20 by 2.5%; RSI14=67
- **Apple Inc. / AAPL** — score 71.8, 20d return +1.7%, RSI14=50. 20d up +1.7%; below MA20 by 0.3%; RSI14=50
- **DAX / ^GDAXI** — score 70.3, 20d return +2.9%, RSI14=57. 20d up +2.9%; above MA20 by 0.7%; RSI14=57
- **Hang Seng / ^HSI** — score 68.8, 20d return +2.9%, RSI14=54. 20d up +2.9%; above MA20 by 3.2%; RSI14=54
- **Amazon.com Inc. / AMZN** — score 68.5, 20d return -1.2%, RSI14=48. 20d down -1.2%; above MA20 by 2.0%; RSI14=48

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                   | Applies To |
| ---------- | ----------------------- | ---------- |
| 2026-11-13 | 8306.T earnings release | 8306.T     |

## Signal History

Compared with the previous available report (**2026-11-06**).

- **New top-5:** AAPL, AMZN
- **Persistent top signals:** ^GDAXI (9 reports), ^FCHI (2 reports), ^HSI (2 reports)
- **Dropped from top-5:** ^FTSE, ^STOXX50E

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +0 |    -8.5 |
| 7203.T    |     +0 |   -10.3 |
| 8306.T    |     -4 |   -37.0 |
| AAPL      |     +4 |    +3.3 |
| AMZN      |     +3 |    +0.9 |
| BZ=F      |     -2 |    -2.4 |
| CL=F      |     +0 |    -2.1 |
| GC=F      |     -4 |    -4.5 |
| GOOGL     |     +0 |    +5.8 |
| HG=F      |     +0 |    +1.5 |
| JPM       |     +2 |    +5.2 |
| META      |     +2 |    +8.5 |
| MSFT      |     +0 |    -2.7 |
| NG=F      |     +1 |   +11.8 |
| NVDA      |     +0 |   +12.1 |
| PL=F      |     -1 |    +4.5 |
| SI=F      |     -2 |    -0.6 |
| TSLA      |     +5 |   +18.8 |
| UNH       |     +1 |    +2.1 |
| XOM       |     +3 |    +6.1 |
| ZC=F      |     -1 |    +3.0 |
| ZS=F      |     -1 |    +4.8 |
| ZW=F      |     -4 |    -7.9 |
| ^DJI      |     +0 |    +1.8 |
| ^FCHI     |     +1 |    -2.4 |
| ^FTSE     |     -4 |    -8.2 |
| ^GDAXI    |     -2 |   -10.3 |
| ^GSPC     |     +2 |    +8.2 |
| ^HSI      |     -1 |    -8.2 |
| ^N225     |     +0 |   -17.0 |
| ^NDX      |     +2 |   +11.5 |
| ^RUT      |     +1 |   +14.8 |
| ^STOXX50E |     -1 |    -2.7 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Natural Gas / NG=F** — malformed_input
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Copper / HG=F** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Nikkei 225 / ^N225** — missing_bars

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|   13 | Gold / GC=F            |  53.0 |   Yes    | —               | 20d down -3.4%; below MA20 by 0.1%; RSI14=44  |
|   15 | Soybeans / ZS=F        |  46.1 |   Yes    | —               | 20d down -8.0%; below MA20 by 3.9%; RSI14=20  |
|   16 | Platinum / PL=F        |  44.9 |   Yes    | —               | 20d down -8.4%; below MA20 by 1.4%; RSI14=37  |
|   18 | Corn / ZC=F            |  38.2 |   Yes    | —               | 20d down -8.0%; below MA20 by 3.8%; RSI14=19  |
|   20 | Brent Crude Oil / BZ=F |  32.4 |   Yes    | —               | 20d down -6.1%; below MA20 by 9.3%; RSI14=37  |
|   22 | Silver / SI=F          |  28.5 |   Yes    | —               | 20d down -14.6%; below MA20 by 4.8%; RSI14=34 |
|   23 | Wheat / ZW=F           |  25.1 |   Yes    | —               | 20d down -11.9%; below MA20 by 5.8%; RSI14=11 |
|   28 | Natural Gas / NG=F     |  62.1 |    No    | malformed_input | Suppressed: malformed_input                   |
|   30 | Copper / HG=F          |  41.2 |    No    | malformed_input | Suppressed: malformed_input                   |
|   31 | WTI Crude Oil / CL=F   |  37.0 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                    |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | ---------------------------------------------- |
|    2 | Apple Inc. / AAPL                                                              |  71.8 |   Yes    | —                             | 20d up +1.7%; below MA20 by 0.3%; RSI14=50     |
|    5 | Amazon.com Inc. / AMZN                                                         |  68.5 |   Yes    | —                             | 20d down -1.2%; above MA20 by 2.0%; RSI14=48   |
|    7 | Microsoft Corporation / MSFT                                                   |  65.5 |   Yes    | —                             | 20d down -0.8%; below MA20 by 0.2%; RSI14=49   |
|    9 | UnitedHealth Group Inc. / UNH                                                  |  58.8 |   Yes    | —                             | 20d up +3.9%; below MA20 by 2.6%; RSI14=42     |
|   10 | JPMorgan Chase & Co. / JPM                                                     |  57.3 |   Yes    | —                             | 20d up +0.5%; below MA20 by 0.8%; RSI14=51     |
|   17 | Tesla Inc. / TSLA                                                              |  43.9 |   Yes    | —                             | 20d down -6.4%; below MA20 by 5.8%; RSI14=47   |
|   19 | Meta Platforms Inc. / META                                                     |  34.2 |   Yes    | —                             | 20d down -15.1%; below MA20 by 7.9%; RSI14=24  |
|   24 | Alphabet Inc. Class A / GOOGL                                                  |  24.6 |   Yes    | —                             | 20d down -19.0%; below MA20 by 10.3%; RSI14=20 |
|   25 | NVIDIA Corporation / NVDA                                                      |  17.9 |   Yes    | —                             | 20d down -18.6%; below MA20 by 11.8%; RSI14=30 |
|   26 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  76.7 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   27 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  73.9 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   29 | Exxon Mobil Corporation / XOM                                                  |  42.7 |    No    | malformed_input               | Suppressed: malformed_input                    |
|   32 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  23.6 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                   |
| ---: | ----------------------------------- | ----: | :------: | ------------ | --------------------------------------------- |
|    1 | CAC 40 / ^FCHI                      |  76.1 |   Yes    | —            | 20d up +4.3%; above MA20 by 2.5%; RSI14=67    |
|    3 | DAX / ^GDAXI                        |  70.3 |   Yes    | —            | 20d up +2.9%; above MA20 by 0.7%; RSI14=57    |
|    4 | Hang Seng / ^HSI                    |  68.8 |   Yes    | —            | 20d up +2.9%; above MA20 by 3.2%; RSI14=54    |
|    6 | Euro Stoxx 50 / ^STOXX50E           |  66.4 |   Yes    | —            | 20d down -0.0%; above MA20 by 0.1%; RSI14=52  |
|    8 | FTSE 100 / ^FTSE                    |  64.2 |   Yes    | —            | 20d up +1.2%; below MA20 by 0.6%; RSI14=44    |
|   11 | Dow Jones Industrial Average / ^DJI |  57.3 |   Yes    | —            | 20d down -0.7%; below MA20 by 1.7%; RSI14=45  |
|   12 | Russell 2000 / ^RUT                 |  56.4 |   Yes    | —            | 20d down -1.9%; below MA20 by 1.1%; RSI14=53  |
|   14 | S&P 500 / ^GSPC                     |  47.6 |   Yes    | —            | 20d down -5.6%; below MA20 by 3.7%; RSI14=35  |
|   21 | NASDAQ 100 / ^NDX                   |  30.9 |   Yes    | —            | 20d down -12.6%; below MA20 by 7.2%; RSI14=31 |
|   33 | Nikkei 225 / ^N225                  |  14.2 |    No    | missing_bars | Suppressed: missing_bars                      |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-11-06 |
| 7203.T    | 2026-11-06 |
| 8306.T    | 2026-11-06 |
| AAPL      | 2026-11-06 |
| AMZN      | 2026-11-06 |
| BZ=F      | 2026-11-06 |
| CL=F      | 2026-11-06 |
| GC=F      | 2026-11-06 |
| GOOGL     | 2026-11-06 |
| HG=F      | 2026-11-06 |
| JPM       | 2026-11-06 |
| META      | 2026-11-06 |
| MSFT      | 2026-11-06 |
| NG=F      | 2026-11-06 |
| NVDA      | 2026-11-06 |
| PL=F      | 2026-11-06 |
| SI=F      | 2026-11-06 |
| TSLA      | 2026-11-06 |
| UNH       | 2026-11-06 |
| XOM       | 2026-11-06 |
| ZC=F      | 2026-11-06 |
| ZS=F      | 2026-11-06 |
| ZW=F      | 2026-11-06 |
| ^DJI      | 2026-11-06 |
| ^FCHI     | 2026-11-06 |
| ^FTSE     | 2026-11-06 |
| ^GDAXI    | 2026-11-06 |
| ^GSPC     | 2026-11-06 |
| ^HSI      | 2026-11-06 |
| ^N225     | 2026-11-06 |
| ^NDX      | 2026-11-06 |
| ^RUT      | 2026-11-06 |
| ^STOXX50E | 2026-11-06 |

## Symbol Details

### CAC 40 / ^FCHI (score 76.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | +2.1% |
| ret_20d    | +4.3% |
| ret_60d    | -5.8% |
| ma20_dist  | +2.5% |
| ma50_dist  | +1.4% |
| vol_20d    | 12.6% |
| mdd_60d    |  9.9% |
| rsi_14     |  67.0 |
| zscore_20d |   1.7 |

### Apple Inc. / AAPL (score 71.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.5% |
| ret_5d     |  -0.7% |
| ret_20d    |  +1.7% |
| ret_60d    | +12.2% |
| ma20_dist  |  -0.3% |
| ma50_dist  |  +1.9% |
| vol_20d    |  25.3% |
| mdd_60d    |   4.9% |
| rsi_14     |   49.6 |
| zscore_20d |   -0.3 |

### DAX / ^GDAXI (score 70.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.9% |
| ret_5d     | +0.0% |
| ret_20d    | +2.9% |
| ret_60d    | -2.3% |
| ma20_dist  | +0.7% |
| ma50_dist  | +1.0% |
| vol_20d    | 15.6% |
| mdd_60d    |  6.6% |
| rsi_14     |  57.4 |
| zscore_20d |   0.5 |

### Hang Seng / ^HSI (score 68.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.3% |
| ret_5d     | +5.1% |
| ret_20d    | +2.9% |
| ret_60d    | -3.8% |
| ma20_dist  | +3.2% |
| ma50_dist  | +0.3% |
| vol_20d    | 21.9% |
| mdd_60d    | 11.8% |
| rsi_14     |  53.6 |
| zscore_20d |   1.3 |

### Amazon.com Inc. / AMZN (score 68.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | +7.9% |
| ret_20d    | -1.2% |
| ret_60d    | -2.2% |
| ma20_dist  | +2.0% |
| ma50_dist  | +2.1% |
| vol_20d    | 40.3% |
| mdd_60d    |  9.8% |
| rsi_14     |  47.7 |
| zscore_20d |   0.7 |

### Euro Stoxx 50 / ^STOXX50E (score 66.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | +0.6% |
| ret_20d    | -0.0% |
| ret_60d    | -5.6% |
| ma20_dist  | +0.1% |
| ma50_dist  | -1.2% |
| vol_20d    | 14.7% |
| mdd_60d    |  7.1% |
| rsi_14     |  51.7 |
| zscore_20d |   0.1 |

### Microsoft Corporation / MSFT (score 65.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | +1.7% |
| ret_20d    | -0.8% |
| ret_60d    | +7.0% |
| ma20_dist  | -0.2% |
| ma50_dist  | +2.7% |
| vol_20d    | 34.5% |
| mdd_60d    |  6.7% |
| rsi_14     |  48.8 |
| zscore_20d |  -0.1 |

### FTSE 100 / ^FTSE (score 64.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | -0.5% |
| ret_20d    | +1.2% |
| ret_60d    | -0.9% |
| ma20_dist  | -0.6% |
| ma50_dist  | -0.2% |
| vol_20d    | 11.8% |
| mdd_60d    |  4.2% |
| rsi_14     |  44.4 |
| zscore_20d |  -1.0 |

### UnitedHealth Group Inc. / UNH (score 58.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -3.2% |
| ret_20d    | +3.9% |
| ret_60d    | -0.6% |
| ma20_dist  | -2.6% |
| ma50_dist  | +1.0% |
| vol_20d    | 29.8% |
| mdd_60d    |  8.5% |
| rsi_14     |  41.9 |
| zscore_20d |  -0.9 |

### JPMorgan Chase & Co. / JPM (score 57.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | -0.8% |
| ret_20d    | +0.5% |
| ret_60d    | -7.9% |
| ma20_dist  | -0.8% |
| ma50_dist  | -2.0% |
| vol_20d    | 26.2% |
| mdd_60d    |  9.4% |
| rsi_14     |  50.7 |
| zscore_20d |  -0.6 |

### Dow Jones Industrial Average / ^DJI (score 57.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | -0.9% |
| ret_20d    | -0.7% |
| ret_60d    | -4.7% |
| ma20_dist  | -1.7% |
| ma50_dist  | -1.5% |
| vol_20d    | 18.6% |
| mdd_60d    |  5.3% |
| rsi_14     |  44.8 |
| zscore_20d |  -1.7 |

### Russell 2000 / ^RUT (score 56.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | -2.1% |
| ret_20d    | -1.9% |
| ret_60d    | -9.8% |
| ma20_dist  | -1.1% |
| ma50_dist  | -3.0% |
| vol_20d    | 22.5% |
| mdd_60d    | 11.3% |
| rsi_14     |  53.2 |
| zscore_20d |  -0.8 |

### Gold / GC=F (score 53.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.9% |
| ret_5d     | +4.5% |
| ret_20d    | -3.4% |
| ret_60d    | -8.9% |
| ma20_dist  | -0.1% |
| ma50_dist  | -3.7% |
| vol_20d    | 22.9% |
| mdd_60d    | 17.2% |
| rsi_14     |  44.1 |
| zscore_20d |  -0.1 |

### S&P 500 / ^GSPC (score 47.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | -2.7% |
| ret_20d    | -5.6% |
| ret_60d    | -5.4% |
| ma20_dist  | -3.7% |
| ma50_dist  | -3.9% |
| vol_20d    | 19.3% |
| mdd_60d    |  5.9% |
| rsi_14     |  34.7 |
| zscore_20d |  -2.3 |

### Soybeans / ZS=F (score 46.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | -2.7% |
| ret_20d    | -8.0% |
| ret_60d    | -0.3% |
| ma20_dist  | -3.9% |
| ma50_dist  | -6.7% |
| vol_20d    |  9.0% |
| mdd_60d    | 11.1% |
| rsi_14     |  20.1 |
| zscore_20d |  -1.6 |

### Platinum / PL=F (score 44.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.9% |
| ret_5d     |  +7.0% |
| ret_20d    |  -8.4% |
| ret_60d    | -13.7% |
| ma20_dist  |  -1.4% |
| ma50_dist  |  -8.4% |
| vol_20d    |  33.1% |
| mdd_60d    |  25.2% |
| rsi_14     |   37.3 |
| zscore_20d |   -0.3 |

### Tesla Inc. / TSLA (score 43.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +4.2% |
| ret_5d     | -10.4% |
| ret_20d    |  -6.4% |
| ret_60d    |  +5.4% |
| ma20_dist  |  -5.8% |
| ma50_dist  |  -3.7% |
| vol_20d    |  55.2% |
| mdd_60d    |  15.7% |
| rsi_14     |   46.8 |
| zscore_20d |   -1.2 |

### Corn / ZC=F (score 38.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.3% |
| ret_5d     |  -1.4% |
| ret_20d    |  -8.0% |
| ret_60d    |  -8.9% |
| ma20_dist  |  -3.8% |
| ma50_dist  | -10.5% |
| vol_20d    |  10.6% |
| mdd_60d    |  19.0% |
| rsi_14     |   19.3 |
| zscore_20d |   -1.2 |

### Meta Platforms Inc. / META (score 34.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.8% |
| ret_5d     |  -0.8% |
| ret_20d    | -15.1% |
| ret_60d    |  +2.6% |
| ma20_dist  |  -7.9% |
| ma50_dist  |  -9.6% |
| vol_20d    |  39.4% |
| mdd_60d    |  22.2% |
| rsi_14     |   23.9 |
| zscore_20d |   -1.0 |

### Brent Crude Oil / BZ=F (score 32.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.0% |
| ret_5d     | -16.4% |
| ret_20d    |  -6.1% |
| ret_60d    |  +8.2% |
| ma20_dist  |  -9.3% |
| ma50_dist  |  -5.8% |
| vol_20d    |  57.8% |
| mdd_60d    |  19.6% |
| rsi_14     |   36.9 |
| zscore_20d |   -1.6 |

### NASDAQ 100 / ^NDX (score 30.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.4% |
| ret_5d     |  -4.9% |
| ret_20d    | -12.6% |
| ret_60d    | -10.3% |
| ma20_dist  |  -7.2% |
| ma50_dist  |  -8.9% |
| vol_20d    |  30.9% |
| mdd_60d    |  14.7% |
| rsi_14     |   30.6 |
| zscore_20d |   -2.0 |

### Silver / SI=F (score 28.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.8% |
| ret_5d     |  +5.5% |
| ret_20d    | -14.6% |
| ret_60d    | -21.7% |
| ma20_dist  |  -4.8% |
| ma50_dist  | -13.6% |
| vol_20d    |  43.2% |
| mdd_60d    |  29.3% |
| rsi_14     |   34.2 |
| zscore_20d |   -0.9 |

### Wheat / ZW=F (score 25.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.3% |
| ret_5d     |  -2.0% |
| ret_20d    | -11.9% |
| ret_60d    | -14.5% |
| ma20_dist  |  -5.8% |
| ma50_dist  | -12.9% |
| vol_20d    |  13.8% |
| mdd_60d    |  22.9% |
| rsi_14     |   10.7 |
| zscore_20d |   -1.3 |

### Alphabet Inc. Class A / GOOGL (score 24.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.8% |
| ret_5d     |  +1.8% |
| ret_20d    | -19.0% |
| ret_60d    | -17.7% |
| ma20_dist  | -10.3% |
| ma50_dist  | -14.5% |
| vol_20d    |  48.7% |
| mdd_60d    |  21.4% |
| rsi_14     |   20.3 |
| zscore_20d |   -1.2 |

### NVIDIA Corporation / NVDA (score 17.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.8% |
| ret_5d     |  -8.8% |
| ret_20d    | -18.6% |
| ret_60d    | -17.1% |
| ma20_dist  | -11.8% |
| ma50_dist  | -15.1% |
| vol_20d    |  45.4% |
| mdd_60d    |  24.1% |
| rsi_14     |   29.6 |
| zscore_20d |   -2.1 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| CAC 40 / ^FCHI                      | 105.4678 |           1.3% |                 0.79x |      210.9357 |            2.6% |
| Apple Inc. / AAPL                   |   9.0171 |           2.6% |                 0.40x |       18.0343 |            5.3% |
| DAX / ^GDAXI                        | 390.9308 |           1.5% |                 0.64x |      781.8616 |            3.0% |
| Hang Seng / ^HSI                    | 420.6868 |           1.7% |                 0.46x |      841.3736 |            3.4% |
| Amazon.com Inc. / AMZN              |   9.7629 |           3.8% |                 0.25x |       19.5257 |            7.5% |
| Euro Stoxx 50 / ^STOXX50E           |  90.1408 |           1.5% |                 0.68x |      180.2815 |            2.9% |
| Microsoft Corporation / MSFT        |  15.8757 |           3.0% |                 0.29x |       31.7514 |            6.0% |
| FTSE 100 / ^FTSE                    | 119.4358 |           1.1% |                 0.84x |      238.8715 |            2.2% |
| UnitedHealth Group Inc. / UNH       |  11.9836 |           3.0% |                 0.34x |       23.9671 |            6.1% |
| JPMorgan Chase & Co. / JPM          |   7.8800 |           2.4% |                 0.38x |       15.7600 |            4.7% |
| Dow Jones Industrial Average / ^DJI | 734.4813 |           1.4% |                 0.54x |     1468.9626 |            2.9% |
| Russell 2000 / ^RUT                 |  44.9636 |           1.6% |                 0.44x |       89.9271 |            3.3% |
| Gold / GC=F                         |  84.9785 |           2.1% |                 0.44x |      169.9571 |            4.2% |
| S&P 500 / ^GSPC                     | 106.2801 |           1.4% |                 0.52x |      212.5601 |            2.9% |
| Soybeans / ZS=F                     |  16.3393 |           1.4% |                 1.12x |       32.6786 |            2.7% |
| Platinum / PL=F                     |  33.7071 |           2.2% |                 0.30x |       67.4143 |            4.4% |
| Tesla Inc. / TSLA                   |  17.9850 |           5.0% |                 0.18x |       35.9700 |           10.0% |
| Corn / ZC=F                         |   6.8571 |           1.6% |                 0.95x |       13.7143 |            3.1% |
| Meta Platforms Inc. / META          |  23.8279 |           3.9% |                 0.25x |       47.6557 |            7.8% |
| Brent Crude Oil / BZ=F              |   5.5593 |           5.7% |                 0.17x |       11.1186 |           11.3% |
| NASDAQ 100 / ^NDX                   | 678.7658 |           2.5% |                 0.32x |     1357.5315 |            5.0% |
| Silver / SI=F                       |   1.4699 |           2.8% |                 0.23x |        2.9399 |            5.7% |
| Wheat / ZW=F                        |  13.9286 |           2.4% |                 0.73x |       27.8571 |            4.7% |
| Alphabet Inc. Class A / GOOGL       |  11.2971 |           4.0% |                 0.21x |       22.5943 |            7.9% |
| NVIDIA Corporation / NVDA           |   8.0200 |           4.3% |                 0.22x |       16.0400 |            8.6% |

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

Scoring engine version: **1.0.0** | Git commit: **165a9a7**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
