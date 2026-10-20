+++
title = "Market Analysis 2026-08-01"
date = "2026-08-01T00:00:00+00:00"
draft = false
summary = "Neutral market: 26 reliable instruments. Top signal: MSFT (score 77.6)."
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
source_files = ["data/analysis/2026-08-01.json", "data/history/2026-08-01.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "3431bfe"
+++

## Market Regime

**Neutral** — 13 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Microsoft Corporation / MSFT** — score 77.6, 20d return +19.0%, RSI14=75. 20d up +19.0%; above MA20 by 17.1%; RSI14=75
- **FTSE 100 / ^FTSE** — score 72.1, 20d return +1.8%, RSI14=74. 20d up +1.8%; above MA20 by 2.0%; RSI14=74
- **Amazon.com Inc. / AMZN** — score 70.6, 20d return +11.9%, RSI14=64. 20d up +11.9%; above MA20 by 11.4%; RSI14=64
- **JPMorgan Chase & Co. / JPM** — score 70.0, 20d return +5.7%, RSI14=65. 20d up +5.7%; above MA20 by 2.2%; RSI14=65
- **Hang Seng / ^HSI** — score 69.7, 20d return +10.9%, RSI14=73. 20d up +10.9%; above MA20 by 4.4%; RSI14=73

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                   | Applies To |
| ---------- | ----------------------- | ---------- |
| 2026-08-03 | 8306.T earnings release | 8306.T     |
| 2026-08-04 | 7203.T earnings release | 7203.T     |

## Signal History

Compared with the previous available report (**2026-07-31**).

- **New top-5:** AMZN
- **Persistent top signals:** ^FTSE (8 reports), ^HSI (3 reports), JPM (2 reports), MSFT (2 reports)
- **Dropped from top-5:** AAPL

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +0 |    -1.2 |
| 7203.T    |     +0 |    -5.8 |
| 8306.T    |     +1 |   +12.1 |
| AAPL      |    -17 |   -38.2 |
| AMZN      |    +17 |   +35.8 |
| BZ=F      |     +4 |    +7.3 |
| CL=F      |     +0 |    +8.5 |
| GC=F      |     -6 |   -13.0 |
| GOOGL     |    +12 |   +21.5 |
| HG=F      |     +0 |    -4.2 |
| JPM       |     -1 |    -0.3 |
| META      |     +2 |   +10.9 |
| MSFT      |     +0 |    +0.3 |
| NG=F      |     +1 |    -1.8 |
| NVDA      |     +6 |   +12.4 |
| PL=F      |     -1 |    -5.8 |
| SI=F      |     -4 |   -14.8 |
| TSLA      |     -1 |    -0.9 |
| UNH       |     -4 |   -12.1 |
| XOM       |     -1 |    -4.2 |
| ZC=F      |     -4 |    -6.4 |
| ZS=F      |     -3 |    -4.5 |
| ZW=F      |     -5 |   -14.2 |
| ^DJI      |     +0 |    +3.9 |
| ^FCHI     |     +1 |    +2.7 |
| ^FTSE     |     +0 |    -0.9 |
| ^GDAXI    |     -1 |    +0.6 |
| ^GSPC     |     +2 |    +6.1 |
| ^HSI      |     -1 |    +1.8 |
| ^N225     |     +0 |   +10.0 |
| ^NDX      |     +2 |    +0.6 |
| ^RUT      |     +1 |    -6.4 |
| ^STOXX50E |     +0 |    +0.3 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|   12 | Platinum / PL=F        |  46.1 |   Yes    | —               | 20d up +2.1%; above MA20 by 1.9%; RSI14=58    |
|   13 | Brent Crude Oil / BZ=F |  45.8 |   Yes    | —               | 20d up +25.5%; above MA20 by 5.0%; RSI14=58   |
|   15 | Wheat / ZW=F           |  39.4 |   Yes    | —               | 20d up +8.3%; below MA20 by 2.2%; RSI14=53    |
|   19 | Gold / GC=F            |  36.4 |   Yes    | —               | 20d down -1.5%; below MA20 by 0.4%; RSI14=54  |
|   20 | Corn / ZC=F            |  35.8 |   Yes    | —               | 20d up +3.7%; below MA20 by 1.3%; RSI14=52    |
|   21 | Soybeans / ZS=F        |  33.6 |   Yes    | —               | 20d up +3.6%; below MA20 by 2.6%; RSI14=41    |
|   23 | Natural Gas / NG=F     |  19.4 |   Yes    | —               | 20d down -14.0%; below MA20 by 5.7%; RSI14=38 |
|   25 | Silver / SI=F          |  17.6 |   Yes    | —               | 20d down -5.0%; below MA20 by 1.5%; RSI14=50  |
|   28 | Copper / HG=F          |  65.2 |    No    | malformed_input | Suppressed: malformed_input                   |
|   32 | WTI Crude Oil / CL=F   |  48.5 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                    |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | ---------------------------------------------- |
|    1 | Microsoft Corporation / MSFT                                                   |  77.6 |   Yes    | —                             | 20d up +19.0%; above MA20 by 17.1%; RSI14=75   |
|    3 | Amazon.com Inc. / AMZN                                                         |  70.6 |   Yes    | —                             | 20d up +11.9%; above MA20 by 11.4%; RSI14=64   |
|    4 | JPMorgan Chase & Co. / JPM                                                     |  70.0 |   Yes    | —                             | 20d up +5.7%; above MA20 by 2.2%; RSI14=65     |
|   11 | Alphabet Inc. Class A / GOOGL                                                  |  46.4 |   Yes    | —                             | 20d down -1.1%; above MA20 by 2.3%; RSI14=51   |
|   16 | NVIDIA Corporation / NVDA                                                      |  38.5 |   Yes    | —                             | 20d up +3.0%; below MA20 by 1.3%; RSI14=48     |
|   18 | UnitedHealth Group Inc. / UNH                                                  |  37.3 |   Yes    | —                             | 20d down -2.6%; below MA20 by 2.3%; RSI14=41   |
|   22 | Apple Inc. / AAPL                                                              |  29.1 |   Yes    | —                             | 20d up +0.1%; below MA20 by 4.8%; RSI14=45     |
|   24 | Meta Platforms Inc. / META                                                     |  18.8 |   Yes    | —                             | 20d down -4.5%; below MA20 by 10.3%; RSI14=23  |
|   26 | Tesla Inc. / TSLA                                                              |  14.2 |   Yes    | —                             | 20d down -20.9%; below MA20 by 14.5%; RSI14=18 |
|   27 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  76.4 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   29 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  62.4 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   30 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  60.6 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   31 | Exxon Mobil Corporation / XOM                                                  |  59.1 |    No    | malformed_input               | Suppressed: malformed_input                    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    2 | FTSE 100 / ^FTSE                    |  72.1 |   Yes    | —            | 20d up +1.8%; above MA20 by 2.0%; RSI14=74   |
|    5 | Hang Seng / ^HSI                    |  69.7 |   Yes    | —            | 20d up +10.9%; above MA20 by 4.4%; RSI14=73  |
|    6 | CAC 40 / ^FCHI                      |  68.2 |   Yes    | —            | 20d up +0.0%; above MA20 by 1.5%; RSI14=62   |
|    7 | DAX / ^GDAXI                        |  66.4 |   Yes    | —            | 20d down -0.6%; above MA20 by 1.7%; RSI14=63 |
|    8 | Euro Stoxx 50 / ^STOXX50E           |  63.9 |   Yes    | —            | 20d down -0.9%; above MA20 by 1.2%; RSI14=58 |
|    9 | Dow Jones Industrial Average / ^DJI |  59.7 |   Yes    | —            | 20d down -0.8%; above MA20 by 0.3%; RSI14=50 |
|   10 | S&P 500 / ^GSPC                     |  57.0 |   Yes    | —            | 20d up +0.1%; above MA20 by 0.1%; RSI14=48   |
|   14 | Russell 2000 / ^RUT                 |  43.0 |   Yes    | —            | 20d down -2.2%; below MA20 by 1.0%; RSI14=46 |
|   17 | NASDAQ 100 / ^NDX                   |  37.9 |   Yes    | —            | 20d down -3.6%; below MA20 by 1.9%; RSI14=40 |
|   33 | Nikkei 225 / ^N225                  |  33.6 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-07-31 |
| 7203.T    | 2026-07-31 |
| 8306.T    | 2026-07-31 |
| AAPL      | 2026-07-31 |
| AMZN      | 2026-07-31 |
| BZ=F      | 2026-07-31 |
| CL=F      | 2026-07-31 |
| GC=F      | 2026-07-31 |
| GOOGL     | 2026-07-31 |
| HG=F      | 2026-07-31 |
| JPM       | 2026-07-31 |
| META      | 2026-07-31 |
| MSFT      | 2026-07-31 |
| NG=F      | 2026-07-31 |
| NVDA      | 2026-07-31 |
| PL=F      | 2026-07-31 |
| SI=F      | 2026-07-31 |
| TSLA      | 2026-07-31 |
| UNH       | 2026-07-31 |
| XOM       | 2026-07-31 |
| ZC=F      | 2026-07-31 |
| ZS=F      | 2026-07-31 |
| ZW=F      | 2026-07-31 |
| ^DJI      | 2026-07-31 |
| ^FCHI     | 2026-07-31 |
| ^FTSE     | 2026-07-31 |
| ^GDAXI    | 2026-07-31 |
| ^GSPC     | 2026-07-31 |
| ^HSI      | 2026-07-31 |
| ^N225     | 2026-07-31 |
| ^NDX      | 2026-07-31 |
| ^RUT      | 2026-07-31 |
| ^STOXX50E | 2026-07-31 |

## Symbol Details

### Microsoft Corporation / MSFT (score 77.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +3.0% |
| ret_5d     | +21.8% |
| ret_20d    | +19.0% |
| ret_60d    | +13.2% |
| ma20_dist  | +17.1% |
| ma50_dist  | +16.4% |
| vol_20d    |  58.6% |
| mdd_60d    |  23.4% |
| rsi_14     |   75.0 |
| zscore_20d |    3.2 |

### FTSE 100 / ^FTSE (score 72.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | +1.2% |
| ret_20d    | +1.8% |
| ret_60d    | +5.8% |
| ma20_dist  | +2.0% |
| ma50_dist  | +3.3% |
| vol_20d    | 10.1% |
| mdd_60d    |  2.6% |
| rsi_14     |  73.6 |
| zscore_20d |   1.5 |

### Amazon.com Inc. / AMZN (score 70.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     | +15.3% |
| ret_5d     | +17.0% |
| ret_20d    | +11.9% |
| ret_60d    |  -0.7% |
| ma20_dist  | +11.4% |
| ma50_dist  | +10.1% |
| vol_20d    |  60.4% |
| mdd_60d    |  17.6% |
| rsi_14     |   64.0 |
| zscore_20d |    2.8 |

### JPMorgan Chase & Co. / JPM (score 70.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.3% |
| ret_5d     |  -0.4% |
| ret_20d    |  +5.7% |
| ret_60d    | +14.2% |
| ma20_dist  |  +2.2% |
| ma50_dist  |  +7.6% |
| vol_20d    |  22.7% |
| mdd_60d    |   6.1% |
| rsi_14     |   64.7 |
| zscore_20d |    1.0 |

### Hang Seng / ^HSI (score 69.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.1% |
| ret_5d     |  +3.7% |
| ret_20d    | +10.9% |
| ret_60d    |  -0.1% |
| ma20_dist  |  +4.4% |
| ma50_dist  |  +5.3% |
| vol_20d    |  18.5% |
| mdd_60d    |  14.9% |
| rsi_14     |   73.5 |
| zscore_20d |    1.6 |

### CAC 40 / ^FCHI (score 68.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +1.6% |
| ret_20d    | +0.0% |
| ret_60d    | +4.9% |
| ma20_dist  | +1.5% |
| ma50_dist  | +2.0% |
| vol_20d    | 12.5% |
| mdd_60d    |  3.0% |
| rsi_14     |  61.9 |
| zscore_20d |   1.9 |

### DAX / ^GDAXI (score 66.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | +2.1% |
| ret_20d    | -0.6% |
| ret_60d    | +5.3% |
| ma20_dist  | +1.7% |
| ma50_dist  | +2.4% |
| vol_20d    | 13.7% |
| mdd_60d    |  4.7% |
| rsi_14     |  63.3 |
| zscore_20d |   1.5 |

### Euro Stoxx 50 / ^STOXX50E (score 63.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | +1.2% |
| ret_20d    | -0.9% |
| ret_60d    | +5.5% |
| ma20_dist  | +1.2% |
| ma50_dist  | +2.3% |
| vol_20d    | 14.0% |
| mdd_60d    |  3.2% |
| rsi_14     |  58.3 |
| zscore_20d |   1.6 |

### Dow Jones Industrial Average / ^DJI (score 59.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | +1.0% |
| ret_20d    | -0.8% |
| ret_60d    | +6.5% |
| ma20_dist  | +0.3% |
| ma50_dist  | +1.5% |
| vol_20d    | 12.3% |
| mdd_60d    |  3.2% |
| rsi_14     |  49.9 |
| zscore_20d |   0.4 |

### S&P 500 / ^GSPC (score 57.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | +1.0% |
| ret_20d    | +0.1% |
| ret_60d    | +3.2% |
| ma20_dist  | +0.1% |
| ma50_dist  | +0.2% |
| vol_20d    | 12.2% |
| mdd_60d    |  4.5% |
| rsi_14     |  48.1 |
| zscore_20d |   0.1 |

### Alphabet Inc. Class A / GOOGL (score 46.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +6.7% |
| ret_5d     | +11.4% |
| ret_20d    |  -1.1% |
| ret_60d    |  -8.3% |
| ma20_dist  |  +2.3% |
| ma50_dist  |  -0.7% |
| vol_20d    |  44.9% |
| mdd_60d    |  21.0% |
| rsi_14     |   51.4 |
| zscore_20d |    0.5 |

### Platinum / PL=F (score 46.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.1% |
| ret_5d     |  +3.6% |
| ret_20d    |  +2.1% |
| ret_60d    | -15.8% |
| ma20_dist  |  +1.9% |
| ma50_dist  |  -3.4% |
| vol_20d    |  30.0% |
| mdd_60d    |  29.1% |
| rsi_14     |   58.0 |
| zscore_20d |    1.4 |

### Brent Crude Oil / BZ=F (score 45.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.2% |
| ret_5d     |  -6.9% |
| ret_20d    | +25.5% |
| ret_60d    | -18.0% |
| ma20_dist  |  +5.0% |
| ma50_dist  |  +4.1% |
| vol_20d    |  68.8% |
| mdd_60d    |  36.2% |
| rsi_14     |   57.6 |
| zscore_20d |    0.6 |

### Russell 2000 / ^RUT (score 43.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | +0.0% |
| ret_20d    | -2.2% |
| ret_60d    | +3.0% |
| ma20_dist  | -1.0% |
| ma50_dist  | -0.4% |
| vol_20d    | 13.2% |
| mdd_60d    |  4.8% |
| rsi_14     |  46.2 |
| zscore_20d |  -1.2 |

### Wheat / ZW=F (score 39.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -3.7% |
| ret_5d     | -5.7% |
| ret_20d    | +8.3% |
| ret_60d    | +3.7% |
| ma20_dist  | -2.2% |
| ma50_dist  | +2.8% |
| vol_20d    | 39.8% |
| mdd_60d    | 14.6% |
| rsi_14     |  53.4 |
| zscore_20d |  -0.5 |

### NVIDIA Corporation / NVDA (score 38.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.9% |
| ret_5d     | -2.9% |
| ret_20d    | +3.0% |
| ret_60d    | +2.2% |
| ma20_dist  | -1.3% |
| ma50_dist  | -2.6% |
| vol_20d    | 41.3% |
| mdd_60d    | 19.4% |
| rsi_14     |  47.7 |
| zscore_20d |  -0.4 |

### NASDAQ 100 / ^NDX (score 37.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | +0.5% |
| ret_20d    | -3.6% |
| ret_60d    | +0.9% |
| ma20_dist  | -1.9% |
| ma50_dist  | -3.8% |
| vol_20d    | 23.1% |
| mdd_60d    | 11.3% |
| rsi_14     |  39.9 |
| zscore_20d |  -0.8 |

### UnitedHealth Group Inc. / UNH (score 37.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.7% |
| ret_5d     |  -1.5% |
| ret_20d    |  -2.6% |
| ret_60d    | +14.5% |
| ma20_dist  |  -2.3% |
| ma50_dist  |  +1.2% |
| vol_20d    |  25.7% |
| mdd_60d    |   6.1% |
| rsi_14     |   41.2 |
| zscore_20d |   -1.9 |

### Gold / GC=F (score 36.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.2% |
| ret_5d     |  -0.5% |
| ret_20d    |  -1.5% |
| ret_60d    | -11.1% |
| ma20_dist  |  -0.4% |
| ma50_dist  |  -3.6% |
| vol_20d    |  21.3% |
| mdd_60d    |  15.6% |
| rsi_14     |   54.4 |
| zscore_20d |   -0.4 |

### Corn / ZC=F (score 35.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.1% |
| ret_5d     | -5.1% |
| ret_20d    | +3.7% |
| ret_60d    | -5.3% |
| ma20_dist  | -1.3% |
| ma50_dist  | +1.3% |
| vol_20d    | 27.3% |
| mdd_60d    | 15.7% |
| rsi_14     |  51.8 |
| zscore_20d |  -0.6 |

### Soybeans / ZS=F (score 33.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -6.1% |
| ret_20d    | +3.6% |
| ret_60d    | -2.0% |
| ma20_dist  | -2.6% |
| ma50_dist  | +0.5% |
| vol_20d    | 25.0% |
| mdd_60d    |  8.8% |
| rsi_14     |  41.0 |
| zscore_20d |  -1.5 |

### Apple Inc. / AAPL (score 29.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -7.4% |
| ret_5d     | -7.2% |
| ret_20d    | +0.1% |
| ret_60d    | +8.8% |
| ma20_dist  | -4.8% |
| ma50_dist  | -0.2% |
| vol_20d    | 35.8% |
| mdd_60d    | 12.7% |
| rsi_14     |  45.1 |
| zscore_20d |  -1.6 |

### Natural Gas / NG=F (score 19.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.4% |
| ret_5d     |  -4.3% |
| ret_20d    | -14.0% |
| ret_60d    |  -1.5% |
| ma20_dist  |  -5.7% |
| ma50_dist  | -10.4% |
| vol_20d    |  34.6% |
| mdd_60d    |  20.4% |
| rsi_14     |   38.1 |
| zscore_20d |   -1.0 |

### Meta Platforms Inc. / META (score 18.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +3.3% |
| ret_5d     |  -6.5% |
| ret_20d    |  -4.5% |
| ret_60d    |  -7.9% |
| ma20_dist  | -10.3% |
| ma50_dist  |  -7.5% |
| vol_20d    |  50.3% |
| mdd_60d    |  20.9% |
| rsi_14     |   22.9 |
| zscore_20d |   -1.7 |

### Silver / SI=F (score 17.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.1% |
| ret_5d     |  -1.8% |
| ret_20d    |  -5.0% |
| ret_60d    | -21.2% |
| ma20_dist  |  -1.5% |
| ma50_dist  | -10.4% |
| vol_20d    |  38.6% |
| mdd_60d    |  37.1% |
| rsi_14     |   49.9 |
| zscore_20d |   -0.6 |

### Tesla Inc. / TSLA (score 14.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.8% |
| ret_5d     |  -0.6% |
| ret_20d    | -20.9% |
| ret_60d    | -20.1% |
| ma20_dist  | -14.5% |
| ma50_dist  | -20.4% |
| vol_20d    |  64.1% |
| mdd_60d    |  33.0% |
| rsi_14     |   18.1 |
| zscore_20d |   -1.3 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Microsoft Corporation / MSFT        |  16.4443 |           3.5% |                 0.17x |       32.8886 |            7.1% |
| FTSE 100 / ^FTSE                    | 117.6930 |           1.1% |                 0.99x |      235.3860 |            2.2% |
| Amazon.com Inc. / AMZN              |   9.2564 |           3.4% |                 0.17x |       18.5129 |            6.8% |
| JPMorgan Chase & Co. / JPM          |   8.1936 |           2.3% |                 0.44x |       16.3871 |            4.7% |
| Hang Seng / ^HSI                    | 438.1293 |           1.7% |                 0.54x |      876.2586 |            3.4% |
| CAC 40 / ^FCHI                      |  98.7450 |           1.2% |                 0.80x |      197.4901 |            2.3% |
| DAX / ^GDAXI                        | 311.8121 |           1.2% |                 0.73x |      623.6242 |            2.4% |
| Euro Stoxx 50 / ^STOXX50E           |  76.9843 |           1.2% |                 0.72x |      153.9686 |            2.4% |
| Dow Jones Industrial Average / ^DJI | 622.1035 |           1.2% |                 0.81x |     1244.2070 |            2.4% |
| S&P 500 / ^GSPC                     |  85.0414 |           1.1% |                 0.82x |      170.0828 |            2.3% |
| Alphabet Inc. Class A / GOOGL       |  13.2486 |           3.7% |                 0.22x |       26.4971 |            7.4% |
| Platinum / PL=F                     |  24.7929 |           1.5% |                 0.33x |       49.5857 |            3.0% |
| Brent Crude Oil / BZ=F              |   5.1807 |           5.7% |                 0.15x |       10.3614 |           11.5% |
| Russell 2000 / ^RUT                 |  37.6564 |           1.3% |                 0.76x |       75.3128 |            2.6% |
| Wheat / ZW=F                        |  25.6786 |           4.0% |                 0.25x |       51.3571 |            8.0% |
| NVIDIA Corporation / NVDA           |   7.6400 |           3.8% |                 0.24x |       15.2800 |            7.6% |
| NASDAQ 100 / ^NDX                   | 606.5142 |           2.1% |                 0.43x |     1213.0285 |            4.3% |
| UnitedHealth Group Inc. / UNH       |  14.1407 |           3.4% |                 0.39x |       28.2814 |            6.8% |
| Gold / GC=F                         |  60.5428 |           1.5% |                 0.47x |      121.0857 |            3.0% |
| Corn / ZC=F                         |  10.5357 |           2.4% |                 0.37x |       21.0714 |            4.8% |
| Soybeans / ZS=F                     |  20.4821 |           1.7% |                 0.40x |       40.9643 |            3.5% |
| Apple Inc. / AAPL                   |   9.9021 |           3.2% |                 0.28x |       19.8043 |            6.4% |
| Natural Gas / NG=F                  |   0.1004 |           3.7% |                 0.29x |        0.2007 |            7.3% |
| Meta Platforms Inc. / META          |  24.1357 |           4.3% |                 0.20x |       48.2714 |            8.7% |
| Silver / SI=F                       |   1.4580 |           2.5% |                 0.26x |        2.9160 |            5.1% |
| Tesla Inc. / TSLA                   |  15.8457 |           5.1% |                 0.16x |       31.6914 |           10.2% |

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

Scoring engine version: **1.0.0** | Git commit: **3431bfe**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
