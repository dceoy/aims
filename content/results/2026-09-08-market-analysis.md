+++
title = "Market Analysis 2026-09-08"
date = "2026-09-08T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: ZS=F (score 74.5)."
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
source_files = ["data/analysis/2026-09-08.json", "data/history/2026-09-08.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "0add368"
+++

## Market Regime

**Neutral** — 15 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Soybeans / ZS=F** — score 74.5, 20d return +12.7%, RSI14=77. 20d up +12.7%; above MA20 by 4.7%; RSI14=77
- **Brent Crude Oil / BZ=F** — score 69.1, 20d return +8.2%, RSI14=62. 20d up +8.2%; above MA20 by 4.9%; RSI14=62
- **Meta Platforms Inc. / META** — score 68.5, 20d return +4.2%, RSI14=70. 20d up +4.2%; above MA20 by 6.9%; RSI14=70
- **Corn / ZC=F** — score 67.6, 20d return +17.2%, RSI14=68. 20d up +17.2%; above MA20 by 4.0%; RSI14=68
- **NVIDIA Corporation / NVDA** — score 67.3, 20d return +2.9%, RSI14=54. 20d up +2.9%; above MA20 by 4.7%; RSI14=54

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                        | Applies To               |
| ---------- | ---------------------------- | ------------------------ |
| 2026-09-10 | ECB monetary policy decision | ^FCHI, ^GDAXI, ^STOXX50E |

## Signal History

Compared with the previous available report (**2026-09-07**).

- **New top-5:** None
- **Persistent top signals:** ZC=F (19 reports), ZS=F (12 reports), BZ=F (2 reports), META (2 reports), NVDA (2 reports)
- **Dropped from top-5:** None
- **NG=F risk gates:** added malformed_input; removed none

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     -4 |   -23.6 |
| 7203.T    |     +1 |    +8.5 |
| 8306.T    |     -1 |   -15.5 |
| AAPL      |     +1 |    -0.3 |
| AMZN      |     +0 |    +0.3 |
| BZ=F      |     +0 |    -2.7 |
| CL=F      |     +2 |    -0.3 |
| GC=F      |     +6 |   +13.3 |
| GOOGL     |     +1 |    -0.9 |
| HG=F      |     +3 |   +10.3 |
| JPM       |     +1 |    -0.9 |
| META      |     +1 |    +1.2 |
| MSFT      |     +3 |    +0.6 |
| NG=F      |    -23 |    -5.5 |
| NVDA      |     +0 |    +2.1 |
| PL=F      |     +5 |    +6.7 |
| SI=F      |     +8 |   +13.9 |
| TSLA      |     +3 |    +1.8 |
| UNH       |     +0 |    +1.2 |
| XOM       |     +1 |    +1.5 |
| ZC=F      |     -1 |    -0.6 |
| ZS=F      |     +0 |    +0.3 |
| ZW=F      |     +1 |    -0.3 |
| ^DJI      |     +1 |    +0.0 |
| ^FCHI     |     +2 |    +2.4 |
| ^FTSE     |     +1 |    -4.2 |
| ^GDAXI    |     -2 |    -3.0 |
| ^GSPC     |     +1 |    +0.6 |
| ^HSI      |    -13 |   -22.1 |
| ^N225     |     +1 |   +14.6 |
| ^NDX      |     +0 |    +0.3 |
| ^RUT      |     +1 |    -1.8 |
| ^STOXX50E |     +0 |    +1.2 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **WTI Crude Oil / CL=F** — malformed_input
- **Copper / HG=F** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Natural Gas / NG=F** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                 |
| ---: | ---------------------- | ----: | :------: | --------------- | ------------------------------------------- |
|    1 | Soybeans / ZS=F        |  74.5 |   Yes    | —               | 20d up +12.7%; above MA20 by 4.7%; RSI14=77 |
|    2 | Brent Crude Oil / BZ=F |  69.1 |   Yes    | —               | 20d up +8.2%; above MA20 by 4.9%; RSI14=62  |
|    4 | Corn / ZC=F            |  67.6 |   Yes    | —               | 20d up +17.2%; above MA20 by 4.0%; RSI14=68 |
|    9 | Platinum / PL=F        |  52.1 |   Yes    | —               | 20d up +3.7%; above MA20 by 0.9%; RSI14=54  |
|   12 | Wheat / ZW=F           |  50.3 |   Yes    | —               | 20d up +13.6%; above MA20 by 1.5%; RSI14=61 |
|   13 | Gold / GC=F            |  50.0 |   Yes    | —               | 20d up +1.5%; below MA20 by 0.3%; RSI14=49  |
|   15 | Silver / SI=F          |  44.2 |   Yes    | —               | 20d up +1.8%; below MA20 by 0.0%; RSI14=53  |
|   26 | WTI Crude Oil / CL=F   |  73.3 |    No    | malformed_input | Suppressed: malformed_input                 |
|   27 | Copper / HG=F          |  63.9 |    No    | malformed_input | Suppressed: malformed_input                 |
|   29 | Natural Gas / NG=F     |  57.3 |    No    | malformed_input | Suppressed: malformed_input                 |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    3 | Meta Platforms Inc. / META                                                     |  68.5 |   Yes    | —                             | 20d up +4.2%; above MA20 by 6.9%; RSI14=70   |
|    5 | NVIDIA Corporation / NVDA                                                      |  67.3 |   Yes    | —                             | 20d up +2.9%; above MA20 by 4.7%; RSI14=54   |
|    7 | Microsoft Corporation / MSFT                                                   |  53.9 |   Yes    | —                             | 20d up +0.1%; above MA20 by 0.9%; RSI14=63   |
|    8 | Apple Inc. / AAPL                                                              |  53.3 |   Yes    | —                             | 20d up +2.2%; above MA20 by 2.2%; RSI14=64   |
|   10 | JPMorgan Chase & Co. / JPM                                                     |  51.8 |   Yes    | —                             | 20d up +0.3%; above MA20 by 0.1%; RSI14=47   |
|   18 | Tesla Inc. / TSLA                                                              |  37.6 |   Yes    | —                             | 20d up +7.8%; above MA20 by 1.6%; RSI14=55   |
|   22 | UnitedHealth Group Inc. / UNH                                                  |  33.0 |   Yes    | —                             | 20d down -2.4%; above MA20 by 0.1%; RSI14=51 |
|   24 | Amazon.com Inc. / AMZN                                                         |  29.1 |   Yes    | —                             | 20d down -5.8%; below MA20 by 1.4%; RSI14=47 |
|   25 | Alphabet Inc. Class A / GOOGL                                                  |  15.4 |   Yes    | —                             | 20d down -4.4%; below MA20 by 1.4%; RSI14=44 |
|   28 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  59.1 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   30 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  54.9 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   31 | Exxon Mobil Corporation / XOM                                                  |  45.8 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   33 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  35.1 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    6 | FTSE 100 / ^FTSE                    |  54.2 |   Yes    | —            | 20d down -0.7%; above MA20 by 0.2%; RSI14=61 |
|   11 | S&P 500 / ^GSPC                     |  51.8 |   Yes    | —            | 20d down -0.5%; above MA20 by 0.1%; RSI14=47 |
|   14 | Dow Jones Industrial Average / ^DJI |  44.9 |   Yes    | —            | 20d down -1.2%; below MA20 by 0.1%; RSI14=49 |
|   16 | NASDAQ 100 / ^NDX                   |  44.2 |   Yes    | —            | 20d down -0.6%; above MA20 by 0.2%; RSI14=42 |
|   17 | Russell 2000 / ^RUT                 |  38.5 |   Yes    | —            | 20d down -1.9%; below MA20 by 1.0%; RSI14=37 |
|   19 | DAX / ^GDAXI                        |  37.3 |   Yes    | —            | 20d down -1.2%; below MA20 by 0.7%; RSI14=47 |
|   20 | Euro Stoxx 50 / ^STOXX50E           |  37.3 |   Yes    | —            | 20d down -2.0%; below MA20 by 0.8%; RSI14=42 |
|   21 | Hang Seng / ^HSI                    |  35.5 |   Yes    | —            | 20d down -2.0%; below MA20 by 0.4%; RSI14=49 |
|   23 | CAC 40 / ^FCHI                      |  29.4 |   Yes    | —            | 20d down -4.8%; below MA20 by 1.7%; RSI14=31 |
|   32 | Nikkei 225 / ^N225                  |  38.8 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-09-07 |
| 7203.T    | 2026-09-07 |
| 8306.T    | 2026-09-07 |
| AAPL      | 2026-09-04 |
| AMZN      | 2026-09-04 |
| BZ=F      | 2026-09-07 |
| CL=F      | 2026-09-07 |
| GC=F      | 2026-09-07 |
| GOOGL     | 2026-09-04 |
| HG=F      | 2026-09-07 |
| JPM       | 2026-09-04 |
| META      | 2026-09-04 |
| MSFT      | 2026-09-04 |
| NG=F      | 2026-09-07 |
| NVDA      | 2026-09-04 |
| PL=F      | 2026-09-07 |
| SI=F      | 2026-09-07 |
| TSLA      | 2026-09-04 |
| UNH       | 2026-09-04 |
| XOM       | 2026-09-04 |
| ZC=F      | 2026-09-04 |
| ZS=F      | 2026-09-04 |
| ZW=F      | 2026-09-04 |
| ^DJI      | 2026-09-04 |
| ^FCHI     | 2026-09-07 |
| ^FTSE     | 2026-09-07 |
| ^GDAXI    | 2026-09-07 |
| ^GSPC     | 2026-09-04 |
| ^HSI      | 2026-09-07 |
| ^N225     | 2026-09-07 |
| ^NDX      | 2026-09-04 |
| ^RUT      | 2026-09-04 |
| ^STOXX50E | 2026-09-07 |

## Symbol Details

### Soybeans / ZS=F (score 74.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.0% |
| ret_5d     |  +1.4% |
| ret_20d    | +12.7% |
| ret_60d    | +15.6% |
| ma20_dist  |  +4.7% |
| ma50_dist  |  +7.2% |
| vol_20d    |  15.8% |
| mdd_60d    |   8.1% |
| rsi_14     |   77.4 |
| zscore_20d |    1.3 |

### Brent Crude Oil / BZ=F (score 69.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.0% |
| ret_5d     |  +6.4% |
| ret_20d    |  +8.2% |
| ret_60d    | +21.9% |
| ma20_dist  |  +4.9% |
| ma50_dist  |  +9.9% |
| vol_20d    |  28.2% |
| mdd_60d    |  21.2% |
| rsi_14     |   62.4 |
| zscore_20d |    1.6 |

### Meta Platforms Inc. / META (score 68.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.0% |
| ret_5d     | +6.7% |
| ret_20d    | +4.2% |
| ret_60d    | +8.1% |
| ma20_dist  | +6.9% |
| ma50_dist  | +3.6% |
| vol_20d    | 32.0% |
| mdd_60d    | 20.9% |
| rsi_14     |  69.9 |
| zscore_20d |   1.9 |

### Corn / ZC=F (score 67.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.6% |
| ret_5d     |  +0.0% |
| ret_20d    | +17.2% |
| ret_60d    | +23.2% |
| ma20_dist  |  +4.0% |
| ma50_dist  | +10.5% |
| vol_20d    |  47.2% |
| mdd_60d    |   6.0% |
| rsi_14     |   68.2 |
| zscore_20d |    0.8 |

### NVIDIA Corporation / NVDA (score 67.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.8% |
| ret_5d     |  +5.9% |
| ret_20d    |  +2.9% |
| ret_60d    | +14.9% |
| ma20_dist  |  +4.7% |
| ma50_dist  |  +9.4% |
| vol_20d    |  44.4% |
| mdd_60d    |  10.6% |
| rsi_14     |   53.7 |
| zscore_20d |    1.7 |

### FTSE 100 / ^FTSE (score 54.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | -0.0% |
| ret_20d    | -0.7% |
| ret_60d    | +3.3% |
| ma20_dist  | +0.2% |
| ma50_dist  | +0.9% |
| vol_20d    |  5.7% |
| mdd_60d    |  1.9% |
| rsi_14     |  61.5 |
| zscore_20d |   0.4 |

### Microsoft Corporation / MSFT (score 53.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.0% |
| ret_5d     |  -2.7% |
| ret_20d    |  +0.1% |
| ret_60d    | +25.8% |
| ma20_dist  |  +0.9% |
| ma50_dist  | +12.6% |
| vol_20d    |  22.7% |
| mdd_60d    |  11.7% |
| rsi_14     |   62.8 |
| zscore_20d |    0.4 |

### Apple Inc. / AAPL (score 53.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.5% |
| ret_5d     | +0.1% |
| ret_20d    | +2.2% |
| ret_60d    | +9.7% |
| ma20_dist  | +2.2% |
| ma50_dist  | +1.6% |
| vol_20d    | 20.9% |
| mdd_60d    | 11.0% |
| rsi_14     |  63.6 |
| zscore_20d |   0.9 |

### Platinum / PL=F (score 52.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +2.1% |
| ret_20d    | +3.7% |
| ret_60d    | +0.8% |
| ma20_dist  | +0.9% |
| ma50_dist  | +6.4% |
| vol_20d    | 31.7% |
| mdd_60d    | 13.4% |
| rsi_14     |  53.5 |
| zscore_20d |   0.3 |

### JPMorgan Chase & Co. / JPM (score 51.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.9% |
| ret_5d     |  +0.3% |
| ret_20d    |  +0.3% |
| ret_60d    | +16.5% |
| ma20_dist  |  +0.1% |
| ma50_dist  |  +2.6% |
| vol_20d    |  13.8% |
| mdd_60d    |   3.7% |
| rsi_14     |   47.0 |
| zscore_20d |    0.1 |

### S&P 500 / ^GSPC (score 51.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | +0.1% |
| ret_20d    | -0.5% |
| ret_60d    | +6.2% |
| ma20_dist  | +0.1% |
| ma50_dist  | +1.7% |
| vol_20d    |  8.1% |
| mdd_60d    |  3.4% |
| rsi_14     |  47.4 |
| zscore_20d |   0.2 |

### Wheat / ZW=F (score 50.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.7% |
| ret_5d     |  -6.6% |
| ret_20d    | +13.6% |
| ret_60d    | +21.4% |
| ma20_dist  |  +1.5% |
| ma50_dist  |  +6.9% |
| vol_20d    |  43.4% |
| mdd_60d    |  10.7% |
| rsi_14     |   61.1 |
| zscore_20d |    0.3 |

### Gold / GC=F (score 50.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | +1.0% |
| ret_20d    | +1.5% |
| ret_60d    | +3.4% |
| ma20_dist  | -0.3% |
| ma50_dist  | +4.7% |
| vol_20d    | 25.0% |
| mdd_60d    |  8.6% |
| rsi_14     |  49.2 |
| zscore_20d |  -0.1 |

### Dow Jones Industrial Average / ^DJI (score 44.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | -0.3% |
| ret_20d    | -1.2% |
| ret_60d    | +7.0% |
| ma20_dist  | -0.1% |
| ma50_dist  | +0.9% |
| vol_20d    |  9.0% |
| mdd_60d    |  2.9% |
| rsi_14     |  49.4 |
| zscore_20d |  -0.1 |

### Silver / SI=F (score 44.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | +0.8% |
| ret_20d    | +1.8% |
| ret_60d    | -4.5% |
| ma20_dist  | -0.0% |
| ma50_dist  | +6.7% |
| vol_20d    | 31.6% |
| mdd_60d    | 20.9% |
| rsi_14     |  53.2 |
| zscore_20d |  -0.0 |

### NASDAQ 100 / ^NDX (score 44.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | +0.4% |
| ret_20d    | -0.6% |
| ret_60d    | +3.6% |
| ma20_dist  | +0.2% |
| ma50_dist  | +1.1% |
| vol_20d    | 12.6% |
| mdd_60d    | 11.0% |
| rsi_14     |  42.1 |
| zscore_20d |   0.2 |

### Russell 2000 / ^RUT (score 38.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | +0.1% |
| ret_20d    | -1.9% |
| ret_60d    | +4.9% |
| ma20_dist  | -1.0% |
| ma50_dist  | -0.4% |
| vol_20d    | 12.2% |
| mdd_60d    |  4.8% |
| rsi_14     |  37.2 |
| zscore_20d |  -0.8 |

### Tesla Inc. / TSLA (score 37.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -5.9% |
| ret_5d     | +1.5% |
| ret_20d    | +7.8% |
| ret_60d    | -7.2% |
| ma20_dist  | +1.6% |
| ma50_dist  | -1.1% |
| vol_20d    | 49.5% |
| mdd_60d    | 29.9% |
| rsi_14     |  55.0 |
| zscore_20d |   0.5 |

### DAX / ^GDAXI (score 37.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | -1.0% |
| ret_20d    | -1.2% |
| ret_60d    | +4.5% |
| ma20_dist  | -0.7% |
| ma50_dist  | +1.1% |
| vol_20d    |  8.7% |
| mdd_60d    |  4.1% |
| rsi_14     |  46.6 |
| zscore_20d |  -1.0 |

### Euro Stoxx 50 / ^STOXX50E (score 37.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | -0.3% |
| ret_20d    | -2.0% |
| ret_60d    | +2.8% |
| ma20_dist  | -0.8% |
| ma50_dist  | +0.3% |
| vol_20d    |  7.8% |
| mdd_60d    |  3.2% |
| rsi_14     |  41.9 |
| zscore_20d |  -0.9 |

### Hang Seng / ^HSI (score 35.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.9% |
| ret_5d     | -0.6% |
| ret_20d    | -2.0% |
| ret_60d    | +4.8% |
| ma20_dist  | -0.4% |
| ma50_dist  | +1.4% |
| vol_20d    | 14.1% |
| mdd_60d    |  8.7% |
| rsi_14     |  48.8 |
| zscore_20d |  -0.5 |

### UnitedHealth Group Inc. / UNH (score 33.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.9% |
| ret_5d     | +1.1% |
| ret_20d    | -2.4% |
| ret_60d    | -2.0% |
| ma20_dist  | +0.1% |
| ma50_dist  | -3.5% |
| vol_20d    | 18.8% |
| mdd_60d    | 11.8% |
| rsi_14     |  51.3 |
| zscore_20d |   0.0 |

### CAC 40 / ^FCHI (score 29.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | -0.3% |
| ret_20d    | -4.8% |
| ret_60d    | -0.9% |
| ma20_dist  | -1.7% |
| ma50_dist  | -1.7% |
| vol_20d    |  8.5% |
| mdd_60d    |  5.1% |
| rsi_14     |  31.2 |
| zscore_20d |  -1.1 |

### Amazon.com Inc. / AMZN (score 29.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | -3.0% |
| ret_20d    | -5.8% |
| ret_60d    | +8.6% |
| ma20_dist  | -1.4% |
| ma50_dist  | +1.8% |
| vol_20d    | 25.9% |
| mdd_60d    | 11.1% |
| rsi_14     |  47.2 |
| zscore_20d |  -0.7 |

### Alphabet Inc. Class A / GOOGL (score 15.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.1% |
| ret_5d     | -2.3% |
| ret_20d    | -4.4% |
| ret_60d    | -5.0% |
| ma20_dist  | -1.4% |
| ma50_dist  | -2.9% |
| vol_20d    | 21.0% |
| mdd_60d    | 14.9% |
| rsi_14     |  44.5 |
| zscore_20d |  -1.1 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Soybeans / ZS=F                     |  20.5536 |           1.6% |                 0.63x |       41.1071 |            3.2% |
| Brent Crude Oil / BZ=F              |   3.2129 |           3.3% |                 0.35x |        6.4257 |            6.7% |
| Meta Platforms Inc. / META          |  18.6979 |           3.0% |                 0.31x |       37.3957 |            6.1% |
| Corn / ZC=F                         |  15.0000 |           2.9% |                 0.21x |       30.0000 |            5.9% |
| NVIDIA Corporation / NVDA           |   7.6193 |           3.3% |                 0.23x |       15.2386 |            6.6% |
| FTSE 100 / ^FTSE                    |  82.1357 |           0.8% |                 1.74x |      164.2713 |            1.5% |
| Microsoft Corporation / MSFT        |  10.0813 |           2.0% |                 0.44x |       20.1626 |            4.0% |
| Apple Inc. / AAPL                   |   7.4314 |           2.3% |                 0.48x |       14.8629 |            4.6% |
| Platinum / PL=F                     |  29.9643 |           1.6% |                 0.32x |       59.9286 |            3.3% |
| JPMorgan Chase & Co. / JPM          |   5.7264 |           1.6% |                 0.73x |       11.4529 |            3.2% |
| S&P 500 / ^GSPC                     |  55.7114 |           0.7% |                 1.24x |      111.4227 |            1.4% |
| Wheat / ZW=F                        |  26.1250 |           3.6% |                 0.23x |       52.2500 |            7.3% |
| Gold / GC=F                         |  76.5786 |           1.7% |                 0.40x |      153.1572 |            3.4% |
| Dow Jones Industrial Average / ^DJI | 418.1482 |           0.8% |                 1.11x |      836.2963 |            1.6% |
| Silver / SI=F                       |   1.9372 |           2.9% |                 0.32x |        3.8744 |            5.8% |
| NASDAQ 100 / ^NDX                   | 337.7213 |           1.1% |                 0.79x |      675.4425 |            2.3% |
| Russell 2000 / ^RUT                 |  30.2507 |           1.0% |                 0.82x |       60.5014 |            2.0% |
| Tesla Inc. / TSLA                   |  15.3371 |           4.3% |                 0.20x |       30.6743 |            8.7% |
| DAX / ^GDAXI                        | 216.8444 |           0.8% |                 1.15x |      433.6889 |            1.7% |
| Euro Stoxx 50 / ^STOXX50E           |  50.9571 |           0.8% |                 1.27x |      101.9142 |            1.6% |
| Hang Seng / ^HSI                    | 342.9230 |           1.3% |                 0.71x |      685.8460 |            2.7% |
| UnitedHealth Group Inc. / UNH       |   7.6129 |           1.9% |                 0.53x |       15.2257 |            3.8% |
| CAC 40 / ^FCHI                      |  72.5364 |           0.9% |                 1.18x |      145.0728 |            1.7% |
| Amazon.com Inc. / AMZN              |   5.8643 |           2.3% |                 0.39x |       11.7286 |            4.5% |
| Alphabet Inc. Class A / GOOGL       |   6.5968 |           1.9% |                 0.48x |       13.1936 |            3.9% |

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

Scoring engine version: **1.0.0** | Git commit: **0add368**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
