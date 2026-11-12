+++
title = "Market Analysis 2026-11-12"
date = "2026-11-12T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: AAPL (score 79.4)."
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
source_files = ["data/analysis/2026-11-12.json", "data/history/2026-11-12.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "bb1bf80"
+++

## Market Regime

**Neutral** — 12 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Apple Inc. / AAPL** — score 79.4, 20d return +3.7%, RSI14=55. 20d up +3.7%; above MA20 by 3.1%; RSI14=55
- **DAX / ^GDAXI** — score 78.5, 20d return +5.4%, RSI14=68. 20d up +5.4%; above MA20 by 3.3%; RSI14=68
- **Euro Stoxx 50 / ^STOXX50E** — score 77.9, 20d return +3.3%, RSI14=70. 20d up +3.3%; above MA20 by 3.3%; RSI14=70
- **CAC 40 / ^FCHI** — score 77.3, 20d return +5.8%, RSI14=84. 20d up +5.8%; above MA20 by 4.1%; RSI14=84
- **FTSE 100 / ^FTSE** — score 69.7, 20d return +1.0%, RSI14=56. 20d up +1.0%; above MA20 by 0.8%; RSI14=56

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                   | Applies To |
| ---------- | ----------------------- | ---------- |
| 2026-11-13 | 8306.T earnings release | 8306.T     |
| 2026-11-17 | NVDA earnings release   | NVDA       |

## Signal History

Compared with the previous available report (**2026-11-11**).

- **New top-5:** ^FTSE
- **Persistent top signals:** ^GDAXI (12 reports), ^FCHI (5 reports), AAPL (4 reports), ^STOXX50E (2 reports)
- **Dropped from top-5:** AMZN

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +0 |    -2.7 |
| 7203.T    |     +2 |    +2.1 |
| 8306.T    |     +0 |    +3.3 |
| AAPL      |     +4 |    +6.7 |
| AMZN      |     -5 |   -14.8 |
| BZ=F      |     +0 |    +4.5 |
| CL=F      |     +0 |    -0.9 |
| GC=F      |     -1 |    -6.7 |
| GOOGL     |     +0 |    +5.8 |
| HG=F      |     +1 |    +5.2 |
| JPM       |     -4 |    -9.4 |
| META      |     -3 |    -9.1 |
| MSFT      |     -4 |   -16.4 |
| NG=F      |     -2 |   -11.5 |
| NVDA      |     +0 |    +9.4 |
| PL=F      |     +1 |    +1.8 |
| SI=F      |     +0 |    +8.2 |
| TSLA      |     +8 |   +16.4 |
| UNH       |     -6 |   -13.0 |
| XOM       |     -1 |    +3.0 |
| ZC=F      |     -1 |    -6.4 |
| ZS=F      |     -2 |    -5.2 |
| ZW=F      |     -1 |    +2.1 |
| ^DJI      |     +0 |    -0.9 |
| ^FCHI     |     -3 |    -1.8 |
| ^FTSE     |     +2 |    +6.4 |
| ^GDAXI    |     +2 |    +4.2 |
| ^GSPC     |     +6 |   +11.2 |
| ^HSI      |     -4 |   -11.8 |
| ^N225     |     +0 |    -0.6 |
| ^NDX      |     +6 |   +14.8 |
| ^RUT      |     +5 |    +4.2 |
| ^STOXX50E |     +0 |    +1.8 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Natural Gas / NG=F** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
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
|   12 | Soybeans / ZS=F        |  52.7 |   Yes    | —               | 20d down -3.8%; above MA20 by 0.2%; RSI14=42   |
|   17 | Corn / ZC=F            |  36.4 |   Yes    | —               | 20d down -6.8%; below MA20 by 1.2%; RSI14=36   |
|   18 | Platinum / PL=F        |  36.1 |   Yes    | —               | 20d down -3.9%; below MA20 by 0.4%; RSI14=46   |
|   19 | Gold / GC=F            |  31.8 |   Yes    | —               | 20d down -2.6%; below MA20 by 1.6%; RSI14=46   |
|   21 | Wheat / ZW=F           |  31.5 |   Yes    | —               | 20d down -11.0%; below MA20 by 2.6%; RSI14=31  |
|   23 | Silver / SI=F          |  24.9 |   Yes    | —               | 20d down -6.6%; below MA20 by 3.0%; RSI14=41   |
|   24 | Brent Crude Oil / BZ=F |  19.1 |   Yes    | —               | 20d down -12.5%; below MA20 by 12.8%; RSI14=28 |
|   28 | Natural Gas / NG=F     |  63.9 |    No    | malformed_input | Suppressed: malformed_input                    |
|   30 | Copper / HG=F          |  39.1 |    No    | malformed_input | Suppressed: malformed_input                    |
|   33 | WTI Crude Oil / CL=F   |  20.0 |    No    | malformed_input | Suppressed: malformed_input                    |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                    |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | ---------------------------------------------- |
|    1 | Apple Inc. / AAPL                                                              |  79.4 |   Yes    | —                             | 20d up +3.7%; above MA20 by 3.1%; RSI14=55     |
|    6 | Tesla Inc. / TSLA                                                              |  66.7 |   Yes    | —                             | 20d up +6.4%; above MA20 by 2.4%; RSI14=55     |
|    7 | Amazon.com Inc. / AMZN                                                         |  62.1 |   Yes    | —                             | 20d up +4.8%; above MA20 by 4.0%; RSI14=61     |
|   13 | JPMorgan Chase & Co. / JPM                                                     |  50.6 |   Yes    | —                             | 20d up +2.4%; above MA20 by 1.5%; RSI14=55     |
|   14 | UnitedHealth Group Inc. / UNH                                                  |  49.1 |   Yes    | —                             | 20d up +1.9%; below MA20 by 1.1%; RSI14=34     |
|   16 | Microsoft Corporation / MSFT                                                   |  40.6 |   Yes    | —                             | 20d down -2.4%; below MA20 by 1.8%; RSI14=50   |
|   20 | Meta Platforms Inc. / META                                                     |  31.8 |   Yes    | —                             | 20d down -14.7%; below MA20 by 2.7%; RSI14=44  |
|   22 | Alphabet Inc. Class A / GOOGL                                                  |  27.0 |   Yes    | —                             | 20d down -15.6%; below MA20 by 4.8%; RSI14=33  |
|   25 | NVIDIA Corporation / NVDA                                                      |  11.8 |   Yes    | —                             | 20d down -21.5%; below MA20 by 14.8%; RSI14=26 |
|   26 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  73.9 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   27 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  71.5 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   29 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  58.5 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   31 | Exxon Mobil Corporation / XOM                                                  |  37.6 |    No    | malformed_input               | Suppressed: malformed_input                    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    2 | DAX / ^GDAXI                        |  78.5 |   Yes    | —            | 20d up +5.4%; above MA20 by 3.3%; RSI14=68   |
|    3 | Euro Stoxx 50 / ^STOXX50E           |  77.9 |   Yes    | —            | 20d up +3.3%; above MA20 by 3.3%; RSI14=70   |
|    4 | CAC 40 / ^FCHI                      |  77.3 |   Yes    | —            | 20d up +5.8%; above MA20 by 4.1%; RSI14=84   |
|    5 | FTSE 100 / ^FTSE                    |  69.7 |   Yes    | —            | 20d up +1.0%; above MA20 by 0.8%; RSI14=56   |
|    8 | Russell 2000 / ^RUT                 |  57.9 |   Yes    | —            | 20d up +4.3%; above MA20 by 1.8%; RSI14=57   |
|    9 | S&P 500 / ^GSPC                     |  57.0 |   Yes    | —            | 20d down -1.3%; below MA20 by 0.1%; RSI14=48 |
|   10 | Hang Seng / ^HSI                    |  56.7 |   Yes    | —            | 20d down -0.1%; above MA20 by 2.4%; RSI14=72 |
|   11 | Dow Jones Industrial Average / ^DJI |  56.4 |   Yes    | —            | 20d up +1.7%; above MA20 by 0.5%; RSI14=47   |
|   15 | NASDAQ 100 / ^NDX                   |  43.0 |   Yes    | —            | 20d down -5.3%; below MA20 by 1.2%; RSI14=46 |
|   32 | Nikkei 225 / ^N225                  |  29.7 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-11-11 |
| 7203.T    | 2026-11-11 |
| 8306.T    | 2026-11-11 |
| AAPL      | 2026-11-11 |
| AMZN      | 2026-11-11 |
| BZ=F      | 2026-11-11 |
| CL=F      | 2026-11-11 |
| GC=F      | 2026-11-11 |
| GOOGL     | 2026-11-11 |
| HG=F      | 2026-11-11 |
| JPM       | 2026-11-11 |
| META      | 2026-11-11 |
| MSFT      | 2026-11-11 |
| NG=F      | 2026-11-11 |
| NVDA      | 2026-11-11 |
| PL=F      | 2026-11-11 |
| SI=F      | 2026-11-11 |
| TSLA      | 2026-11-11 |
| UNH       | 2026-11-11 |
| XOM       | 2026-11-11 |
| ZC=F      | 2026-11-11 |
| ZS=F      | 2026-11-11 |
| ZW=F      | 2026-11-11 |
| ^DJI      | 2026-11-11 |
| ^FCHI     | 2026-11-11 |
| ^FTSE     | 2026-11-11 |
| ^GDAXI    | 2026-11-11 |
| ^GSPC     | 2026-11-11 |
| ^HSI      | 2026-11-11 |
| ^N225     | 2026-11-11 |
| ^NDX      | 2026-11-11 |
| ^RUT      | 2026-11-11 |
| ^STOXX50E | 2026-11-11 |

## Symbol Details

### Apple Inc. / AAPL (score 79.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.0% |
| ret_5d     |  +1.8% |
| ret_20d    |  +3.7% |
| ret_60d    | +14.7% |
| ma20_dist  |  +3.1% |
| ma50_dist  |  +5.3% |
| vol_20d    |  27.2% |
| mdd_60d    |   4.9% |
| rsi_14     |   54.9 |
| zscore_20d |    2.2 |

### DAX / ^GDAXI (score 78.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.2% |
| ret_5d     | +0.9% |
| ret_20d    | +5.4% |
| ret_60d    | +2.2% |
| ma20_dist  | +3.3% |
| ma50_dist  | +4.2% |
| vol_20d    | 16.8% |
| mdd_60d    |  6.6% |
| rsi_14     |  68.0 |
| zscore_20d |   2.0 |

### Euro Stoxx 50 / ^STOXX50E (score 77.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.0% |
| ret_5d     | +2.0% |
| ret_20d    | +3.3% |
| ret_60d    | -0.8% |
| ma20_dist  | +3.3% |
| ma50_dist  | +2.5% |
| vol_20d    | 16.3% |
| mdd_60d    |  6.4% |
| rsi_14     |  70.5 |
| zscore_20d |   2.6 |

### CAC 40 / ^FCHI (score 77.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | +1.9% |
| ret_20d    | +5.8% |
| ret_60d    | -2.0% |
| ma20_dist  | +4.1% |
| ma50_dist  | +3.8% |
| vol_20d    | 13.0% |
| mdd_60d    |  8.9% |
| rsi_14     |  84.0 |
| zscore_20d |   2.0 |

### FTSE 100 / ^FTSE (score 69.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.8% |
| ret_5d     | +0.1% |
| ret_20d    | +1.0% |
| ret_60d    | +1.0% |
| ma20_dist  | +0.8% |
| ma50_dist  | +1.3% |
| vol_20d    | 12.0% |
| mdd_60d    |  4.2% |
| rsi_14     |  55.8 |
| zscore_20d |   1.4 |

### Tesla Inc. / TSLA (score 66.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.9% |
| ret_5d     |  +1.5% |
| ret_20d    |  +6.4% |
| ret_60d    | +16.0% |
| ma20_dist  |  +2.4% |
| ma50_dist  |  +4.6% |
| vol_20d    |  58.7% |
| mdd_60d    |  15.7% |
| rsi_14     |   55.2 |
| zscore_20d |    0.5 |

### Amazon.com Inc. / AMZN (score 62.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.7% |
| ret_5d     | +0.1% |
| ret_20d    | +4.8% |
| ret_60d    | +2.6% |
| ma20_dist  | +4.0% |
| ma50_dist  | +4.6% |
| vol_20d    | 41.6% |
| mdd_60d    |  9.8% |
| rsi_14     |  61.0 |
| zscore_20d |   1.2 |

### Russell 2000 / ^RUT (score 57.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | -0.4% |
| ret_20d    | +4.3% |
| ret_60d    | -5.7% |
| ma20_dist  | +1.8% |
| ma50_dist  | +0.5% |
| vol_20d    | 24.2% |
| mdd_60d    | 10.3% |
| rsi_14     |  56.5 |
| zscore_20d |   1.2 |

### S&P 500 / ^GSPC (score 57.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.3% |
| ret_5d     | -0.9% |
| ret_20d    | -1.3% |
| ret_60d    | -0.9% |
| ma20_dist  | -0.1% |
| ma50_dist  | -0.7% |
| vol_20d    | 21.6% |
| mdd_60d    |  5.9% |
| rsi_14     |  48.1 |
| zscore_20d |  -0.1 |

### Hang Seng / ^HSI (score 56.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | +1.7% |
| ret_20d    | -0.1% |
| ret_60d    | -4.5% |
| ma20_dist  | +2.4% |
| ma50_dist  | -0.1% |
| vol_20d    | 21.4% |
| mdd_60d    | 11.8% |
| rsi_14     |  71.8 |
| zscore_20d |   0.9 |

### Dow Jones Industrial Average / ^DJI (score 56.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | -1.6% |
| ret_20d    | +1.7% |
| ret_60d    | -1.6% |
| ma20_dist  | +0.5% |
| ma50_dist  | +0.9% |
| vol_20d    | 20.1% |
| mdd_60d    |  5.2% |
| rsi_14     |  47.3 |
| zscore_20d |   0.5 |

### Soybeans / ZS=F (score 52.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | +3.0% |
| ret_20d    | -3.8% |
| ret_60d    | +0.6% |
| ma20_dist  | +0.2% |
| ma50_dist  | -3.3% |
| vol_20d    | 16.6% |
| mdd_60d    | 11.1% |
| rsi_14     |  41.8 |
| zscore_20d |   0.1 |

### JPMorgan Chase & Co. / JPM (score 50.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | -2.5% |
| ret_20d    | +2.4% |
| ret_60d    | -5.5% |
| ma20_dist  | +1.5% |
| ma50_dist  | +0.9% |
| vol_20d    | 26.8% |
| mdd_60d    |  9.1% |
| rsi_14     |  54.9 |
| zscore_20d |   1.1 |

### UnitedHealth Group Inc. / UNH (score 49.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | -1.6% |
| ret_20d    | +1.9% |
| ret_60d    | +2.9% |
| ma20_dist  | -1.1% |
| ma50_dist  | +3.1% |
| vol_20d    | 26.0% |
| mdd_60d    |  8.4% |
| rsi_14     |  34.1 |
| zscore_20d |  -0.6 |

### NASDAQ 100 / ^NDX (score 43.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.3% |
| ret_5d     | -0.2% |
| ret_20d    | -5.3% |
| ret_60d    | -3.8% |
| ma20_dist  | -1.2% |
| ma50_dist  | -4.0% |
| vol_20d    | 34.7% |
| mdd_60d    | 14.7% |
| rsi_14     |  45.8 |
| zscore_20d |  -0.4 |

### Microsoft Corporation / MSFT (score 40.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.3% |
| ret_5d     | -6.2% |
| ret_20d    | -2.4% |
| ret_60d    | +8.4% |
| ma20_dist  | -1.8% |
| ma50_dist  | +0.6% |
| vol_20d    | 36.8% |
| mdd_60d    |  6.7% |
| rsi_14     |  50.0 |
| zscore_20d |  -1.0 |

### Corn / ZC=F (score 36.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | +0.8% |
| ret_20d    | -6.8% |
| ret_60d    | -5.3% |
| ma20_dist  | -1.2% |
| ma50_dist  | -8.4% |
| vol_20d    | 13.5% |
| mdd_60d    | 19.1% |
| rsi_14     |  36.3 |
| zscore_20d |  -0.5 |

### Platinum / PL=F (score 36.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.0% |
| ret_5d     |  +2.5% |
| ret_20d    |  -3.9% |
| ret_60d    | -15.9% |
| ma20_dist  |  -0.4% |
| ma50_dist  |  -7.7% |
| vol_20d    |  31.9% |
| mdd_60d    |  25.2% |
| rsi_14     |   46.0 |
| zscore_20d |   -0.1 |

### Gold / GC=F (score 31.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.7% |
| ret_5d     |  -1.8% |
| ret_20d    |  -2.6% |
| ret_60d    | -12.5% |
| ma20_dist  |  -1.6% |
| ma50_dist  |  -4.9% |
| vol_20d    |  23.6% |
| mdd_60d    |  17.2% |
| rsi_14     |   46.1 |
| zscore_20d |   -0.8 |

### Meta Platforms Inc. / META (score 31.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.0% |
| ret_5d     |  -0.2% |
| ret_20d    | -14.7% |
| ret_60d    | +15.7% |
| ma20_dist  |  -2.7% |
| ma50_dist  |  -7.3% |
| vol_20d    |  39.6% |
| mdd_60d    |  22.2% |
| rsi_14     |   43.9 |
| zscore_20d |   -0.4 |

### Wheat / ZW=F (score 31.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.1% |
| ret_5d     |  +0.2% |
| ret_20d    | -11.0% |
| ret_60d    | -11.9% |
| ma20_dist  |  -2.6% |
| ma50_dist  | -10.4% |
| vol_20d    |  15.0% |
| mdd_60d    |  23.3% |
| rsi_14     |   30.8 |
| zscore_20d |   -0.7 |

### Alphabet Inc. Class A / GOOGL (score 27.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.1% |
| ret_5d     |  +1.6% |
| ret_20d    | -15.6% |
| ret_60d    | -14.7% |
| ma20_dist  |  -4.8% |
| ma50_dist  | -11.0% |
| vol_20d    |  50.0% |
| mdd_60d    |  21.4% |
| rsi_14     |   32.9 |
| zscore_20d |   -0.6 |

### Silver / SI=F (score 24.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.5% |
| ret_5d     |  -0.5% |
| ret_20d    |  -6.6% |
| ret_60d    | -23.7% |
| ma20_dist  |  -3.0% |
| ma50_dist  | -12.3% |
| vol_20d    |  40.4% |
| mdd_60d    |  29.3% |
| rsi_14     |   40.8 |
| zscore_20d |   -0.6 |

### Brent Crude Oil / BZ=F (score 19.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.4% |
| ret_5d     |  -2.0% |
| ret_20d    | -12.5% |
| ret_60d    |  -1.1% |
| ma20_dist  | -12.8% |
| ma50_dist  | -11.0% |
| vol_20d    |  60.7% |
| mdd_60d    |  22.2% |
| rsi_14     |   27.7 |
| zscore_20d |   -1.6 |

### NVIDIA Corporation / NVDA (score 11.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.9% |
| ret_5d     | -13.2% |
| ret_20d    | -21.5% |
| ret_60d    | -20.8% |
| ma20_dist  | -14.8% |
| ma50_dist  | -20.0% |
| vol_20d    |  50.2% |
| mdd_60d    |  29.4% |
| rsi_14     |   26.4 |
| zscore_20d |   -1.9 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Apple Inc. / AAPL                   |   9.5821 |           2.7% |                 0.37x |       19.1643 |            5.4% |
| DAX / ^GDAXI                        | 392.7037 |           1.5% |                 0.60x |      785.4074 |            2.9% |
| Euro Stoxx 50 / ^STOXX50E           |  90.0301 |           1.4% |                 0.61x |      180.0601 |            2.8% |
| CAC 40 / ^FCHI                      | 105.4386 |           1.3% |                 0.77x |      210.8772 |            2.5% |
| FTSE 100 / ^FTSE                    | 125.3572 |           1.2% |                 0.83x |      250.7144 |            2.3% |
| Tesla Inc. / TSLA                   |  18.3422 |           4.7% |                 0.17x |       36.6843 |            9.4% |
| Amazon.com Inc. / AMZN              |  10.3107 |           3.9% |                 0.24x |       20.6214 |            7.7% |
| Russell 2000 / ^RUT                 |  50.2436 |           1.8% |                 0.41x |      100.4872 |            3.5% |
| S&P 500 / ^GSPC                     | 116.6408 |           1.5% |                 0.46x |      233.2815 |            3.1% |
| Hang Seng / ^HSI                    | 363.6025 |           1.5% |                 0.47x |      727.2051 |            3.0% |
| Dow Jones Industrial Average / ^DJI | 769.6702 |           1.5% |                 0.50x |     1539.3404 |            2.9% |
| Soybeans / ZS=F                     |  18.7679 |           1.5% |                 0.60x |       37.5357 |            3.1% |
| JPMorgan Chase & Co. / JPM          |   7.9379 |           2.3% |                 0.37x |       15.8757 |            4.6% |
| UnitedHealth Group Inc. / UNH       |  11.3221 |           2.8% |                 0.39x |       22.6443 |            5.6% |
| NASDAQ 100 / ^NDX                   | 718.0172 |           2.5% |                 0.29x |     1436.0343 |            5.1% |
| Microsoft Corporation / MSFT        |  17.5086 |           3.4% |                 0.27x |       35.0172 |            6.7% |
| Corn / ZC=F                         |   7.1429 |           1.6% |                 0.74x |       14.2857 |            3.2% |
| Platinum / PL=F                     |  32.0857 |           2.1% |                 0.31x |       64.1714 |            4.2% |
| Gold / GC=F                         |  92.4857 |           2.3% |                 0.42x |      184.9714 |            4.6% |
| Meta Platforms Inc. / META          |  21.2279 |           3.4% |                 0.25x |       42.4557 |            6.8% |
| Wheat / ZW=F                        |  12.8393 |           2.1% |                 0.67x |       25.6786 |            4.3% |
| Alphabet Inc. Class A / GOOGL       |  11.0957 |           3.8% |                 0.20x |       22.1914 |            7.6% |
| Silver / SI=F                       |   1.4125 |           2.7% |                 0.25x |        2.8250 |            5.4% |
| Brent Crude Oil / BZ=F              |   5.5879 |           6.0% |                 0.16x |       11.1757 |           12.0% |
| NVIDIA Corporation / NVDA           |   9.1421 |           5.3% |                 0.20x |       18.2843 |           10.5% |

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

Scoring engine version: **1.0.0** | Git commit: **bb1bf80**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
