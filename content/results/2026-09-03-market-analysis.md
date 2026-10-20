+++
title = "Market Analysis 2026-09-03"
date = "2026-09-03T00:00:00+00:00"
draft = false
summary = "Neutral market: 26 reliable instruments. Top signal: ZS=F (score 76.4)."
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
source_files = ["data/analysis/2026-09-03.json", "data/history/2026-09-03.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "517435d"
+++

## Market Regime

**Neutral** — 11 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Soybeans / ZS=F** — score 76.4, 20d return +10.2%, RSI14=84. 20d up +10.2%; above MA20 by 6.6%; RSI14=84
- **Brent Crude Oil / BZ=F** — score 69.1, 20d return +13.5%, RSI14=66. 20d up +13.5%; above MA20 by 5.5%; RSI14=66
- **Wheat / ZW=F** — score 69.1, 20d return +16.0%, RSI14=64. 20d up +16.0%; above MA20 by 8.4%; RSI14=64
- **Apple Inc. / AAPL** — score 68.8, 20d return +4.6%, RSI14=73. 20d up +4.6%; above MA20 by 4.2%; RSI14=73
- **Corn / ZC=F** — score 67.0, 20d return +11.7%, RSI14=61. 20d up +11.7%; above MA20 by 7.0%; RSI14=61

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                        | Applies To               |
| ---------- | ---------------------------- | ------------------------ |
| 2026-09-10 | ECB monetary policy decision | ^FCHI, ^GDAXI, ^STOXX50E |

## Signal History

Compared with the previous available report (**2026-09-02**).

- **New top-5:** None
- **Persistent top signals:** ZC=F (16 reports), ZW=F (14 reports), ZS=F (9 reports), AAPL (2 reports), BZ=F (2 reports)
- **Dropped from top-5:** None

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     -2 |   -13.6 |
| 7203.T    |     -4 |   -20.3 |
| 8306.T    |     +1 |    -6.1 |
| AAPL      |     +0 |    -3.9 |
| AMZN      |     +1 |    +5.8 |
| BZ=F      |     +3 |    +4.2 |
| CL=F      |     +2 |    +3.3 |
| GC=F      |     +3 |    +4.5 |
| GOOGL     |     +0 |   +10.0 |
| HG=F      |     +1 |    -0.3 |
| JPM       |     +0 |    +4.8 |
| META      |     +4 |   +10.3 |
| MSFT      |     -3 |    -3.3 |
| NG=F      |     +3 |   +12.4 |
| NVDA      |     +4 |   +17.0 |
| PL=F      |     +1 |    +2.4 |
| SI=F      |     +0 |    +3.3 |
| TSLA      |     +5 |    +9.4 |
| UNH       |     -1 |    +2.4 |
| XOM       |     +3 |    -2.4 |
| ZC=F      |     -2 |    -7.9 |
| ZS=F      |     +0 |    -7.0 |
| ZW=F      |     -1 |    -8.8 |
| ^DJI      |     +4 |    +8.5 |
| ^FCHI     |     -3 |    -5.2 |
| ^FTSE     |     -5 |    -5.8 |
| ^GDAXI    |     -8 |    -7.0 |
| ^GSPC     |     +2 |    +8.2 |
| ^HSI      |     -3 |    -1.2 |
| ^N225     |     -1 |   -25.1 |
| ^NDX      |     -1 |    +3.0 |
| ^RUT      |     +3 |   +10.0 |
| ^STOXX50E |     -6 |    -1.8 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **WTI Crude Oil / CL=F** — malformed_input
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|    1 | Soybeans / ZS=F        |  76.4 |   Yes    | —               | 20d up +10.2%; above MA20 by 6.6%; RSI14=84  |
|    2 | Brent Crude Oil / BZ=F |  69.1 |   Yes    | —               | 20d up +13.5%; above MA20 by 5.5%; RSI14=66  |
|    3 | Wheat / ZW=F           |  69.1 |   Yes    | —               | 20d up +16.0%; above MA20 by 8.4%; RSI14=64  |
|    5 | Corn / ZC=F            |  67.0 |   Yes    | —               | 20d up +11.7%; above MA20 by 7.0%; RSI14=61  |
|    6 | Natural Gas / NG=F     |  62.1 |   Yes    | —               | 20d up +8.3%; above MA20 by 5.5%; RSI14=75   |
|   15 | Gold / GC=F            |  42.7 |   Yes    | —               | 20d down -0.3%; below MA20 by 2.5%; RSI14=45 |
|   19 | Platinum / PL=F        |  37.9 |   Yes    | —               | 20d up +0.1%; below MA20 by 2.2%; RSI14=49   |
|   23 | Silver / SI=F          |  31.8 |   Yes    | —               | 20d up +1.9%; below MA20 by 2.7%; RSI14=46   |
|   27 | WTI Crude Oil / CL=F   |  71.2 |    No    | malformed_input | Suppressed: malformed_input                  |
|   32 | Copper / HG=F          |  39.4 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    4 | Apple Inc. / AAPL                                                              |  68.8 |   Yes    | —                             | 20d up +4.6%; above MA20 by 4.2%; RSI14=73   |
|    7 | NVIDIA Corporation / NVDA                                                      |  62.1 |   Yes    | —                             | 20d up +2.4%; above MA20 by 2.3%; RSI14=49   |
|    8 | JPMorgan Chase & Co. / JPM                                                     |  57.9 |   Yes    | —                             | 20d down -0.8%; below MA20 by 0.5%; RSI14=39 |
|    9 | Microsoft Corporation / MSFT                                                   |  56.1 |   Yes    | —                             | 20d up +2.1%; above MA20 by 0.4%; RSI14=51   |
|   11 | Meta Platforms Inc. / META                                                     |  49.4 |   Yes    | —                             | 20d up +0.7%; above MA20 by 3.2%; RSI14=49   |
|   14 | Tesla Inc. / TSLA                                                              |  46.1 |   Yes    | —                             | 20d up +11.0%; above MA20 by 3.7%; RSI14=58  |
|   17 | UnitedHealth Group Inc. / UNH                                                  |  40.9 |   Yes    | —                             | 20d down -3.2%; above MA20 by 0.5%; RSI14=50 |
|   24 | Amazon.com Inc. / AMZN                                                         |  28.5 |   Yes    | —                             | 20d down -6.5%; below MA20 by 3.3%; RSI14=40 |
|   26 | Alphabet Inc. Class A / GOOGL                                                  |  24.9 |   Yes    | —                             | 20d down -7.0%; below MA20 by 2.3%; RSI14=39 |
|   28 | Exxon Mobil Corporation / XOM                                                  |  63.0 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   29 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  59.4 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   30 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  58.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   31 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  57.3 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|   10 | S&P 500 / ^GSPC                     |  52.1 |   Yes    | —            | 20d down -0.7%; below MA20 by 0.5%; RSI14=36 |
|   12 | FTSE 100 / ^FTSE                    |  49.4 |   Yes    | —            | 20d down -1.1%; below MA20 by 0.5%; RSI14=42 |
|   13 | Dow Jones Industrial Average / ^DJI |  47.0 |   Yes    | —            | 20d down -2.4%; below MA20 by 0.8%; RSI14=39 |
|   16 | Hang Seng / ^HSI                    |  41.2 |   Yes    | —            | 20d down -2.3%; below MA20 by 0.9%; RSI14=48 |
|   18 | DAX / ^GDAXI                        |  38.8 |   Yes    | —            | 20d down -1.1%; below MA20 by 1.5%; RSI14=38 |
|   20 | Euro Stoxx 50 / ^STOXX50E           |  37.9 |   Yes    | —            | 20d down -1.8%; below MA20 by 1.7%; RSI14=29 |
|   21 | Russell 2000 / ^RUT                 |  37.0 |   Yes    | —            | 20d down -2.2%; below MA20 by 1.9%; RSI14=35 |
|   22 | NASDAQ 100 / ^NDX                   |  35.1 |   Yes    | —            | 20d down -1.2%; below MA20 by 1.2%; RSI14=32 |
|   25 | CAC 40 / ^FCHI                      |  26.4 |   Yes    | —            | 20d down -4.5%; below MA20 by 2.8%; RSI14=21 |
|   33 | Nikkei 225 / ^N225                  |  16.1 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-09-02 |
| 7203.T    | 2026-09-02 |
| 8306.T    | 2026-09-02 |
| AAPL      | 2026-09-02 |
| AMZN      | 2026-09-02 |
| BZ=F      | 2026-09-02 |
| CL=F      | 2026-09-02 |
| GC=F      | 2026-09-02 |
| GOOGL     | 2026-09-02 |
| HG=F      | 2026-09-02 |
| JPM       | 2026-09-02 |
| META      | 2026-09-02 |
| MSFT      | 2026-09-02 |
| NG=F      | 2026-09-02 |
| NVDA      | 2026-09-02 |
| PL=F      | 2026-09-02 |
| SI=F      | 2026-09-02 |
| TSLA      | 2026-09-02 |
| UNH       | 2026-09-02 |
| XOM       | 2026-09-02 |
| ZC=F      | 2026-09-02 |
| ZS=F      | 2026-09-02 |
| ZW=F      | 2026-09-02 |
| ^DJI      | 2026-09-02 |
| ^FCHI     | 2026-09-02 |
| ^FTSE     | 2026-09-02 |
| ^GDAXI    | 2026-09-02 |
| ^GSPC     | 2026-09-02 |
| ^HSI      | 2026-09-02 |
| ^N225     | 2026-09-02 |
| ^NDX      | 2026-09-02 |
| ^RUT      | 2026-09-02 |
| ^STOXX50E | 2026-09-02 |

## Symbol Details

### Soybeans / ZS=F (score 76.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.4% |
| ret_5d     |  +3.8% |
| ret_20d    | +10.2% |
| ret_60d    | +16.7% |
| ma20_dist  |  +6.6% |
| ma50_dist  |  +8.6% |
| vol_20d    |  18.2% |
| mdd_60d    |   8.1% |
| rsi_14     |   83.7 |
| zscore_20d |    1.8 |

### Brent Crude Oil / BZ=F (score 69.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.0% |
| ret_5d     |  +8.9% |
| ret_20d    | +13.5% |
| ret_60d    |  +5.8% |
| ma20_dist  |  +5.5% |
| ma50_dist  | +10.9% |
| vol_20d    |  30.9% |
| mdd_60d    |  21.2% |
| rsi_14     |   65.8 |
| zscore_20d |    2.0 |

### Wheat / ZW=F (score 69.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.2% |
| ret_5d     |  +3.3% |
| ret_20d    | +16.0% |
| ret_60d    | +28.6% |
| ma20_dist  |  +8.4% |
| ma50_dist  | +13.7% |
| vol_20d    |  41.7% |
| mdd_60d    |  10.7% |
| rsi_14     |   64.4 |
| zscore_20d |    1.4 |

### Apple Inc. / AAPL (score 68.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | +3.7% |
| ret_20d    | +4.6% |
| ret_60d    | +7.8% |
| ma20_dist  | +4.2% |
| ma50_dist  | +3.7% |
| vol_20d    | 18.4% |
| mdd_60d    | 11.0% |
| rsi_14     |  73.3 |
| zscore_20d |   2.1 |

### Corn / ZC=F (score 67.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.5% |
| ret_5d     |  +0.9% |
| ret_20d    | +11.7% |
| ret_60d    | +26.0% |
| ma20_dist  |  +7.0% |
| ma50_dist  | +13.0% |
| vol_20d    |  52.0% |
| mdd_60d    |   6.0% |
| rsi_14     |   61.4 |
| zscore_20d |    1.2 |

### Natural Gas / NG=F (score 62.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.8% |
| ret_5d     | +4.0% |
| ret_20d    | +8.3% |
| ret_60d    | -4.2% |
| ma20_dist  | +5.5% |
| ma50_dist  | +3.1% |
| vol_20d    | 27.9% |
| mdd_60d    | 21.0% |
| rsi_14     |  75.0 |
| zscore_20d |   2.0 |

### NVIDIA Corporation / NVDA (score 62.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +3.2% |
| ret_5d     | +7.0% |
| ret_20d    | +2.4% |
| ret_60d    | +7.6% |
| ma20_dist  | +2.3% |
| ma50_dist  | +7.2% |
| vol_20d    | 44.6% |
| mdd_60d    | 10.6% |
| rsi_14     |  49.3 |
| zscore_20d |   1.0 |

### JPMorgan Chase & Co. / JPM (score 57.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.4% |
| ret_5d     |  -0.1% |
| ret_20d    |  -0.8% |
| ret_60d    | +15.0% |
| ma20_dist  |  -0.5% |
| ma50_dist  |  +2.2% |
| vol_20d    |  12.4% |
| mdd_60d    |   3.7% |
| rsi_14     |   38.9 |
| zscore_20d |   -0.5 |

### Microsoft Corporation / MSFT (score 56.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.8% |
| ret_5d     |  +0.1% |
| ret_20d    |  +2.1% |
| ret_60d    | +20.7% |
| ma20_dist  |  +0.4% |
| ma50_dist  | +13.4% |
| vol_20d    |  21.3% |
| mdd_60d    |  12.5% |
| rsi_14     |   50.6 |
| zscore_20d |    0.2 |

### S&P 500 / ^GSPC (score 52.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | -0.1% |
| ret_20d    | -0.7% |
| ret_60d    | +3.5% |
| ma20_dist  | -0.5% |
| ma50_dist  | +1.2% |
| vol_20d    |  7.4% |
| mdd_60d    |  3.4% |
| rsi_14     |  35.6 |
| zscore_20d |  -0.9 |

### Meta Platforms Inc. / META (score 49.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.5% |
| ret_5d     | +2.9% |
| ret_20d    | +0.7% |
| ret_60d    | +1.4% |
| ma20_dist  | +3.2% |
| ma50_dist  | -0.0% |
| vol_20d    | 30.1% |
| mdd_60d    | 20.9% |
| rsi_14     |  49.1 |
| zscore_20d |   1.0 |

### FTSE 100 / ^FTSE (score 49.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | -1.2% |
| ret_20d    | -1.1% |
| ret_60d    | +5.2% |
| ma20_dist  | -0.5% |
| ma50_dist  | +0.5% |
| vol_20d    |  5.3% |
| mdd_60d    |  1.9% |
| rsi_14     |  41.9 |
| zscore_20d |  -1.0 |

### Dow Jones Industrial Average / ^DJI (score 47.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | -0.8% |
| ret_20d    | -2.4% |
| ret_60d    | +4.5% |
| ma20_dist  | -0.8% |
| ma50_dist  | +0.3% |
| vol_20d    |  8.3% |
| mdd_60d    |  2.9% |
| rsi_14     |  38.7 |
| zscore_20d |  -1.2 |

### Tesla Inc. / TSLA (score 46.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.3% |
| ret_5d     |  +3.2% |
| ret_20d    | +11.0% |
| ret_60d    | -12.7% |
| ma20_dist  |  +3.7% |
| ma50_dist  |  -0.4% |
| vol_20d    |  41.4% |
| mdd_60d    |  29.9% |
| rsi_14     |   57.6 |
| zscore_20d |    1.0 |

### Gold / GC=F (score 42.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | -5.0% |
| ret_20d    | -0.3% |
| ret_60d    | +6.7% |
| ma20_dist  | -2.5% |
| ma50_dist  | +2.7% |
| vol_20d    | 22.3% |
| mdd_60d    |  8.6% |
| rsi_14     |  44.9 |
| zscore_20d |  -1.0 |

### Hang Seng / ^HSI (score 41.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | -1.3% |
| ret_20d    | -2.3% |
| ret_60d    | +2.7% |
| ma20_dist  | -0.9% |
| ma50_dist  | +1.6% |
| vol_20d    | 13.9% |
| mdd_60d    |  8.7% |
| rsi_14     |  48.1 |
| zscore_20d |  -1.2 |

### UnitedHealth Group Inc. / UNH (score 40.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.8% |
| ret_5d     | -0.3% |
| ret_20d    | -3.2% |
| ret_60d    | -1.1% |
| ma20_dist  | +0.5% |
| ma50_dist  | -3.0% |
| vol_20d    | 20.0% |
| mdd_60d    | 11.8% |
| rsi_14     |  50.5 |
| zscore_20d |   0.3 |

### DAX / ^GDAXI (score 38.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | -1.7% |
| ret_20d    | -1.1% |
| ret_60d    | +6.8% |
| ma20_dist  | -1.5% |
| ma50_dist  | +0.7% |
| vol_20d    |  8.7% |
| mdd_60d    |  4.1% |
| rsi_14     |  38.3 |
| zscore_20d |  -2.3 |

### Platinum / PL=F (score 37.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | -4.1% |
| ret_20d    | +0.1% |
| ret_60d    | +5.8% |
| ma20_dist  | -2.2% |
| ma50_dist  | +3.5% |
| vol_20d    | 29.0% |
| mdd_60d    | 14.5% |
| rsi_14     |  49.2 |
| zscore_20d |  -0.7 |

### Euro Stoxx 50 / ^STOXX50E (score 37.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | -1.7% |
| ret_20d    | -1.8% |
| ret_60d    | +5.9% |
| ma20_dist  | -1.7% |
| ma50_dist  | -0.2% |
| vol_20d    |  8.0% |
| mdd_60d    |  3.2% |
| rsi_14     |  28.7 |
| zscore_20d |  -2.0 |

### Russell 2000 / ^RUT (score 37.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | -1.8% |
| ret_20d    | -2.2% |
| ret_60d    | +3.4% |
| ma20_dist  | -1.9% |
| ma50_dist  | -1.2% |
| vol_20d    | 12.8% |
| mdd_60d    |  4.8% |
| rsi_14     |  34.6 |
| zscore_20d |  -1.5 |

### NASDAQ 100 / ^NDX (score 35.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | -0.3% |
| ret_20d    | -1.2% |
| ret_60d    | -0.9% |
| ma20_dist  | -1.2% |
| ma50_dist  | -0.3% |
| vol_20d    | 12.7% |
| mdd_60d    | 11.0% |
| rsi_14     |  31.5 |
| zscore_20d |  -1.1 |

### Silver / SI=F (score 31.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | -4.8% |
| ret_20d    | +1.9% |
| ret_60d    | +1.3% |
| ma20_dist  | -2.7% |
| ma50_dist  | +4.2% |
| vol_20d    | 30.1% |
| mdd_60d    | 20.9% |
| rsi_14     |  46.4 |
| zscore_20d |  -1.0 |

### Amazon.com Inc. / AMZN (score 28.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.0% |
| ret_5d     | -2.0% |
| ret_20d    | -6.5% |
| ret_60d    | +4.0% |
| ma20_dist  | -3.3% |
| ma50_dist  | +0.9% |
| vol_20d    | 25.4% |
| mdd_60d    | 11.1% |
| rsi_14     |  39.9 |
| zscore_20d |  -1.4 |

### CAC 40 / ^FCHI (score 26.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | -2.1% |
| ret_20d    | -4.5% |
| ret_60d    | +1.5% |
| ma20_dist  | -2.8% |
| ma50_dist  | -2.1% |
| vol_20d    |  8.6% |
| mdd_60d    |  5.1% |
| rsi_14     |  21.2 |
| zscore_20d |  -1.6 |

### Alphabet Inc. Class A / GOOGL (score 24.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | -1.4% |
| ret_20d    | -7.0% |
| ret_60d    | -7.2% |
| ma20_dist  | -2.3% |
| ma50_dist  | -3.3% |
| vol_20d    | 20.1% |
| mdd_60d    | 14.9% |
| rsi_14     |  38.9 |
| zscore_20d |  -1.4 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Soybeans / ZS=F                     |  21.2679 |           1.6% |                 0.55x |       42.5357 |            3.3% |
| Brent Crude Oil / BZ=F              |   3.1186 |           3.3% |                 0.32x |        6.2371 |            6.5% |
| Wheat / ZW=F                        |  25.8393 |           3.4% |                 0.24x |       51.6786 |            6.8% |
| Apple Inc. / AAPL                   |   6.7271 |           2.1% |                 0.54x |       13.4543 |            4.1% |
| Corn / ZC=F                         |  15.8571 |           3.1% |                 0.19x |       31.7143 |            6.1% |
| Natural Gas / NG=F                  |   0.0979 |           3.3% |                 0.36x |        0.1957 |            6.6% |
| NVIDIA Corporation / NVDA           |   7.1729 |           3.2% |                 0.22x |       14.3457 |            6.4% |
| JPMorgan Chase & Co. / JPM          |   5.3657 |           1.5% |                 0.81x |       10.7314 |            3.0% |
| Microsoft Corporation / MSFT        |   9.5503 |           1.9% |                 0.47x |       19.1007 |            3.8% |
| S&P 500 / ^GSPC                     |  51.8021 |           0.7% |                 1.35x |      103.6042 |            1.4% |
| Meta Platforms Inc. / META          |  18.6450 |           3.1% |                 0.33x |       37.2900 |            6.3% |
| FTSE 100 / ^FTSE                    |  80.1858 |           0.7% |                 1.89x |      160.3715 |            1.5% |
| Dow Jones Industrial Average / ^DJI | 380.5603 |           0.7% |                 1.21x |      761.1205 |            1.4% |
| Tesla Inc. / TSLA                   |  13.3243 |           3.7% |                 0.24x |       26.6486 |            7.5% |
| Gold / GC=F                         |  84.1857 |           1.9% |                 0.45x |      168.3714 |            3.9% |
| Hang Seng / ^HSI                    | 327.8058 |           1.3% |                 0.72x |      655.6116 |            2.6% |
| UnitedHealth Group Inc. / UNH       |   7.6150 |           1.9% |                 0.50x |       15.2300 |            3.8% |
| DAX / ^GDAXI                        | 219.2016 |           0.8% |                 1.14x |      438.4032 |            1.7% |
| Platinum / PL=F                     |  32.9357 |           1.9% |                 0.34x |       65.8714 |            3.7% |
| Euro Stoxx 50 / ^STOXX50E           |  51.6778 |           0.8% |                 1.25x |      103.3556 |            1.6% |
| Russell 2000 / ^RUT                 |  29.1779 |           1.0% |                 0.78x |       58.3557 |            2.0% |
| NASDAQ 100 / ^NDX                   | 327.6113 |           1.1% |                 0.79x |      655.2227 |            2.2% |
| Silver / SI=F                       |   2.0829 |           3.2% |                 0.33x |        4.1657 |            6.4% |
| Amazon.com Inc. / AMZN              |   5.8964 |           2.3% |                 0.39x |       11.7929 |            4.6% |
| CAC 40 / ^FCHI                      |  73.6898 |           0.9% |                 1.16x |      147.3796 |            1.8% |
| Alphabet Inc. Class A / GOOGL       |   6.4057 |           1.9% |                 0.50x |       12.8114 |            3.8% |

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

Scoring engine version: **1.0.0** | Git commit: **517435d**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
