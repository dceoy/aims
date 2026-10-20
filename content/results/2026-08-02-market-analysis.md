+++
title = "Market Analysis 2026-08-02"
date = "2026-08-02T00:00:00+00:00"
draft = false
summary = "Neutral market: 26 reliable instruments. Top signal: MSFT (score 77.3)."
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
source_files = ["data/analysis/2026-08-02.json", "data/history/2026-08-02.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "f7bb0ea"
+++

## Market Regime

**Neutral** — 15 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Microsoft Corporation / MSFT** — score 77.3, 20d return +19.0%, RSI14=75. 20d up +19.0%; above MA20 by 17.1%; RSI14=75
- **Amazon.com Inc. / AMZN** — score 70.0, 20d return +11.9%, RSI14=64. 20d up +11.9%; above MA20 by 11.4%; RSI14=64
- **FTSE 100 / ^FTSE** — score 69.4, 20d return +1.8%, RSI14=74. 20d up +1.8%; above MA20 by 2.0%; RSI14=74
- **Hang Seng / ^HSI** — score 67.3, 20d return +10.9%, RSI14=73. 20d up +10.9%; above MA20 by 4.4%; RSI14=73
- **JPMorgan Chase & Co. / JPM** — score 66.7, 20d return +5.7%, RSI14=65. 20d up +5.7%; above MA20 by 2.2%; RSI14=65

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                   | Applies To |
| ---------- | ----------------------- | ---------- |
| 2026-08-03 | 8306.T earnings release | 8306.T     |
| 2026-08-04 | 7203.T earnings release | 7203.T     |

## Signal History

Compared with the previous available report (**2026-08-01**).

- **New top-5:** None
- **Persistent top signals:** ^FTSE (9 reports), ^HSI (4 reports), JPM (3 reports), MSFT (3 reports), AMZN (2 reports)
- **Dropped from top-5:** None

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +0 |    -0.6 |
| 7203.T    |     +0 |    -0.6 |
| 8306.T    |     +0 |    -3.0 |
| AAPL      |     +0 |    -0.3 |
| AMZN      |     +1 |    -0.6 |
| BZ=F      |     -2 |    -1.8 |
| CL=F      |     +0 |    -2.4 |
| GC=F      |     +6 |    +8.5 |
| GOOGL     |     -3 |    -1.8 |
| HG=F      |     +0 |    +1.5 |
| JPM       |     -1 |    -3.3 |
| META      |     +1 |    -0.3 |
| MSFT      |     +0 |    -0.3 |
| NG=F      |     -2 |    -2.1 |
| NVDA      |     -3 |    -1.8 |
| PL=F      |     +0 |    +3.0 |
| SI=F      |     +1 |    +0.9 |
| TSLA      |     +0 |    -1.2 |
| UNH       |     -3 |    -1.5 |
| XOM       |     +0 |    -1.5 |
| ZC=F      |    +13 |   +27.3 |
| ZS=F      |     +5 |    +7.9 |
| ZW=F      |     -3 |    -2.1 |
| ^DJI      |     -1 |    -3.0 |
| ^FCHI     |     +0 |    -2.1 |
| ^FTSE     |     -1 |    -2.7 |
| ^GDAXI    |     -1 |    -4.2 |
| ^GSPC     |     -1 |    -1.8 |
| ^HSI      |     +1 |    -2.4 |
| ^N225     |     +0 |    -0.9 |
| ^NDX      |     -3 |    -1.2 |
| ^RUT      |     -3 |    -1.5 |
| ^STOXX50E |     -1 |    -3.6 |

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
|    7 | Corn / ZC=F            |  63.0 |   Yes    | —               | 20d up +9.2%; above MA20 by 3.7%; RSI14=64    |
|   12 | Platinum / PL=F        |  49.1 |   Yes    | —               | 20d up +2.6%; above MA20 by 2.4%; RSI14=59    |
|   13 | Gold / GC=F            |  44.9 |   Yes    | —               | 20d down -0.1%; above MA20 by 0.9%; RSI14=60  |
|   15 | Brent Crude Oil / BZ=F |  43.9 |   Yes    | —               | 20d up +25.5%; above MA20 by 5.0%; RSI14=58   |
|   16 | Soybeans / ZS=F        |  41.5 |   Yes    | —               | 20d up +4.9%; below MA20 by 1.4%; RSI14=46    |
|   18 | Wheat / ZW=F           |  37.3 |   Yes    | —               | 20d up +8.3%; below MA20 by 2.2%; RSI14=53    |
|   24 | Silver / SI=F          |  18.5 |   Yes    | —               | 20d down -4.7%; below MA20 by 1.1%; RSI14=51  |
|   25 | Natural Gas / NG=F     |  17.3 |   Yes    | —               | 20d down -14.0%; below MA20 by 5.7%; RSI14=38 |
|   28 | Copper / HG=F          |  66.7 |    No    | malformed_input | Suppressed: malformed_input                   |
|   32 | WTI Crude Oil / CL=F   |  46.1 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                    |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | ---------------------------------------------- |
|    1 | Microsoft Corporation / MSFT                                                   |  77.3 |   Yes    | —                             | 20d up +19.0%; above MA20 by 17.1%; RSI14=75   |
|    2 | Amazon.com Inc. / AMZN                                                         |  70.0 |   Yes    | —                             | 20d up +11.9%; above MA20 by 11.4%; RSI14=64   |
|    5 | JPMorgan Chase & Co. / JPM                                                     |  66.7 |   Yes    | —                             | 20d up +5.7%; above MA20 by 2.2%; RSI14=65     |
|   14 | Alphabet Inc. Class A / GOOGL                                                  |  44.5 |   Yes    | —                             | 20d down -1.1%; above MA20 by 2.3%; RSI14=51   |
|   19 | NVIDIA Corporation / NVDA                                                      |  36.7 |   Yes    | —                             | 20d up +3.0%; below MA20 by 1.3%; RSI14=48     |
|   21 | UnitedHealth Group Inc. / UNH                                                  |  35.8 |   Yes    | —                             | 20d down -2.6%; below MA20 by 2.3%; RSI14=41   |
|   22 | Apple Inc. / AAPL                                                              |  28.8 |   Yes    | —                             | 20d up +0.1%; below MA20 by 4.8%; RSI14=45     |
|   23 | Meta Platforms Inc. / META                                                     |  18.5 |   Yes    | —                             | 20d down -4.5%; below MA20 by 10.3%; RSI14=23  |
|   26 | Tesla Inc. / TSLA                                                              |  13.0 |   Yes    | —                             | 20d down -20.9%; below MA20 by 14.5%; RSI14=18 |
|   27 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  75.8 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   29 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  61.8 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   30 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  57.6 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   31 | Exxon Mobil Corporation / XOM                                                  |  57.6 |    No    | malformed_input               | Suppressed: malformed_input                    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    3 | FTSE 100 / ^FTSE                    |  69.4 |   Yes    | —            | 20d up +1.8%; above MA20 by 2.0%; RSI14=74   |
|    4 | Hang Seng / ^HSI                    |  67.3 |   Yes    | —            | 20d up +10.9%; above MA20 by 4.4%; RSI14=73  |
|    6 | CAC 40 / ^FCHI                      |  66.1 |   Yes    | —            | 20d up +0.0%; above MA20 by 1.5%; RSI14=62   |
|    8 | DAX / ^GDAXI                        |  62.1 |   Yes    | —            | 20d down -0.6%; above MA20 by 1.7%; RSI14=63 |
|    9 | Euro Stoxx 50 / ^STOXX50E           |  60.3 |   Yes    | —            | 20d down -0.9%; above MA20 by 1.2%; RSI14=58 |
|   10 | Dow Jones Industrial Average / ^DJI |  56.7 |   Yes    | —            | 20d down -0.8%; above MA20 by 0.3%; RSI14=50 |
|   11 | S&P 500 / ^GSPC                     |  55.1 |   Yes    | —            | 20d up +0.1%; above MA20 by 0.1%; RSI14=48   |
|   17 | Russell 2000 / ^RUT                 |  41.5 |   Yes    | —            | 20d down -2.2%; below MA20 by 1.0%; RSI14=46 |
|   20 | NASDAQ 100 / ^NDX                   |  36.7 |   Yes    | —            | 20d down -3.6%; below MA20 by 1.9%; RSI14=40 |
|   33 | Nikkei 225 / ^N225                  |  32.7 |    No    | missing_bars | Suppressed: missing_bars                     |

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

### Microsoft Corporation / MSFT (score 77.3)

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

### Amazon.com Inc. / AMZN (score 70.0)

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

### FTSE 100 / ^FTSE (score 69.4)

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

### Hang Seng / ^HSI (score 67.3)

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

### JPMorgan Chase & Co. / JPM (score 66.7)

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

### CAC 40 / ^FCHI (score 66.1)

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

### Corn / ZC=F (score 63.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +4.1% |
| ret_5d     | -0.1% |
| ret_20d    | +9.2% |
| ret_60d    | -0.3% |
| ma20_dist  | +3.7% |
| ma50_dist  | +6.5% |
| vol_20d    | 30.0% |
| mdd_60d    | 15.7% |
| rsi_14     |  63.6 |
| zscore_20d |   1.6 |

### DAX / ^GDAXI (score 62.1)

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

### Euro Stoxx 50 / ^STOXX50E (score 60.3)

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

### Dow Jones Industrial Average / ^DJI (score 56.7)

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

### S&P 500 / ^GSPC (score 55.1)

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

### Platinum / PL=F (score 49.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.4% |
| ret_5d     |  +4.1% |
| ret_20d    |  +2.6% |
| ret_60d    | -15.4% |
| ma20_dist  |  +2.4% |
| ma50_dist  |  -2.9% |
| vol_20d    |  30.0% |
| mdd_60d    |  29.1% |
| rsi_14     |   59.3 |
| zscore_20d |    1.8 |

### Gold / GC=F (score 44.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | +1.0% |
| ret_20d    | -0.1% |
| ret_60d    | -9.9% |
| ma20_dist  | +0.9% |
| ma50_dist  | -2.3% |
| vol_20d    | 20.8% |
| mdd_60d    | 15.6% |
| rsi_14     |  60.1 |
| zscore_20d |   0.7 |

### Alphabet Inc. Class A / GOOGL (score 44.5)

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

### Brent Crude Oil / BZ=F (score 43.9)

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

### Soybeans / ZS=F (score 41.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | -4.8% |
| ret_20d    | +4.9% |
| ret_60d    | -0.7% |
| ma20_dist  | -1.4% |
| ma50_dist  | +1.8% |
| vol_20d    | 25.0% |
| mdd_60d    |  8.8% |
| rsi_14     |  45.8 |
| zscore_20d |  -0.9 |

### Russell 2000 / ^RUT (score 41.5)

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

### Wheat / ZW=F (score 37.3)

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

### NVIDIA Corporation / NVDA (score 36.7)

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

### NASDAQ 100 / ^NDX (score 36.7)

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

### UnitedHealth Group Inc. / UNH (score 35.8)

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

### Apple Inc. / AAPL (score 28.8)

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

### Meta Platforms Inc. / META (score 18.5)

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

### Silver / SI=F (score 18.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.7% |
| ret_5d     |  -1.5% |
| ret_20d    |  -4.7% |
| ret_60d    | -21.0% |
| ma20_dist  |  -1.1% |
| ma50_dist  | -10.1% |
| vol_20d    |  38.4% |
| mdd_60d    |  37.1% |
| rsi_14     |   50.5 |
| zscore_20d |   -0.4 |

### Natural Gas / NG=F (score 17.3)

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

### Tesla Inc. / TSLA (score 13.0)

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
| Amazon.com Inc. / AMZN              |   9.2564 |           3.4% |                 0.17x |       18.5129 |            6.8% |
| FTSE 100 / ^FTSE                    | 117.6930 |           1.1% |                 0.99x |      235.3860 |            2.2% |
| Hang Seng / ^HSI                    | 438.1293 |           1.7% |                 0.54x |      876.2586 |            3.4% |
| JPMorgan Chase & Co. / JPM          |   8.1936 |           2.3% |                 0.44x |       16.3871 |            4.7% |
| CAC 40 / ^FCHI                      |  98.7450 |           1.2% |                 0.80x |      197.4901 |            2.3% |
| Corn / ZC=F                         |  11.6250 |           2.5% |                 0.33x |       23.2500 |            5.0% |
| DAX / ^GDAXI                        | 311.8121 |           1.2% |                 0.73x |      623.6242 |            2.4% |
| Euro Stoxx 50 / ^STOXX50E           |  76.9843 |           1.2% |                 0.72x |      153.9686 |            2.4% |
| Dow Jones Industrial Average / ^DJI | 622.1035 |           1.2% |                 0.81x |     1244.2070 |            2.4% |
| S&P 500 / ^GSPC                     |  85.0414 |           1.1% |                 0.82x |      170.0828 |            2.3% |
| Platinum / PL=F                     |  27.9143 |           1.7% |                 0.33x |       55.8286 |            3.4% |
| Gold / GC=F                         |  61.5643 |           1.5% |                 0.48x |      123.1286 |            3.0% |
| Alphabet Inc. Class A / GOOGL       |  13.2486 |           3.7% |                 0.22x |       26.4971 |            7.4% |
| Brent Crude Oil / BZ=F              |   5.1807 |           5.7% |                 0.15x |       10.3614 |           11.5% |
| Soybeans / ZS=F                     |  20.8036 |           1.8% |                 0.40x |       41.6071 |            3.5% |
| Russell 2000 / ^RUT                 |  37.6564 |           1.3% |                 0.76x |       75.3128 |            2.6% |
| Wheat / ZW=F                        |  25.6786 |           4.0% |                 0.25x |       51.3571 |            8.0% |
| NVIDIA Corporation / NVDA           |   7.6400 |           3.8% |                 0.24x |       15.2800 |            7.6% |
| NASDAQ 100 / ^NDX                   | 606.5142 |           2.1% |                 0.43x |     1213.0285 |            4.3% |
| UnitedHealth Group Inc. / UNH       |  14.1407 |           3.4% |                 0.39x |       28.2814 |            6.8% |
| Apple Inc. / AAPL                   |   9.9021 |           3.2% |                 0.28x |       19.8043 |            6.4% |
| Meta Platforms Inc. / META          |  24.1357 |           4.3% |                 0.20x |       48.2714 |            8.7% |
| Silver / SI=F                       |   1.4812 |           2.6% |                 0.26x |        2.9624 |            5.1% |
| Natural Gas / NG=F                  |   0.1004 |           3.7% |                 0.29x |        0.2007 |            7.3% |
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

Scoring engine version: **1.0.0** | Git commit: **f7bb0ea**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
