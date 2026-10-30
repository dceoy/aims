+++
title = "Market Analysis 2026-10-30"
date = "2026-10-30T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: AAPL (score 79.1)."
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
source_files = ["data/analysis/2026-10-30.json", "data/history/2026-10-30.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "177e686"
+++

## Market Regime

**Neutral** — 11 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Apple Inc. / AAPL** — score 79.1, 20d return +5.6%, RSI14=66. 20d up +5.6%; above MA20 by 2.2%; RSI14=66 ⚠️ Upcoming: AAPL earnings release (2026-11-02)
- **DAX / ^GDAXI** — score 77.6, 20d return +4.4%, RSI14=69. 20d up +4.4%; above MA20 by 2.7%; RSI14=69
- **Tesla Inc. / TSLA** — score 74.8, 20d return +13.9%, RSI14=59. 20d up +13.9%; above MA20 by 6.3%; RSI14=59
- **Brent Crude Oil / BZ=F** — score 74.2, 20d return +12.3%, RSI14=74. 20d up +12.3%; above MA20 by 6.2%; RSI14=74
- **JPMorgan Chase & Co. / JPM** — score 70.9, 20d return +3.6%, RSI14=64. 20d up +3.6%; above MA20 by 2.7%; RSI14=64

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                   | Applies To |
| ---------- | ----------------------- | ---------- |
| 2026-11-02 | AAPL earnings release   | AAPL       |
| 2026-11-05 | 6758.T earnings release | 6758.T     |
| 2026-11-05 | 7203.T earnings release | 7203.T     |

## Signal History

Compared with the previous available report (**2026-10-29**).

- **New top-5:** None
- **Persistent top signals:** BZ=F (10 reports), TSLA (4 reports), AAPL (3 reports), ^GDAXI (3 reports), JPM (2 reports)
- **Dropped from top-5:** None

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     -1 |    -2.1 |
| 7203.T    |     +3 |    +7.6 |
| 8306.T    |     +1 |   +18.2 |
| AAPL      |     +4 |   +11.5 |
| AMZN      |     -7 |   -20.3 |
| BZ=F      |     -3 |    -9.7 |
| CL=F      |     -1 |   -12.4 |
| GC=F      |     +0 |    -0.9 |
| GOOGL     |     -7 |   -26.1 |
| HG=F      |     -1 |   -10.0 |
| JPM       |     -1 |    +1.5 |
| META      |     +4 |   +14.6 |
| MSFT      |     -2 |    -1.2 |
| NG=F      |     +1 |   +13.3 |
| NVDA      |     +5 |    +2.7 |
| PL=F      |     -1 |   -12.1 |
| SI=F      |     +1 |    +0.9 |
| TSLA      |     -1 |    +0.9 |
| UNH       |     +5 |    +6.7 |
| XOM       |     +0 |    -2.4 |
| ZC=F      |     -1 |    -1.5 |
| ZS=F      |     +1 |    -3.0 |
| ZW=F      |     +3 |   +10.0 |
| ^DJI      |     -5 |    -6.1 |
| ^FCHI     |     +3 |    +9.7 |
| ^FTSE     |     +2 |    +2.7 |
| ^GDAXI    |     +1 |    +6.4 |
| ^GSPC     |     -4 |    -4.2 |
| ^HSI      |     +2 |    +0.6 |
| ^N225     |     -2 |    +6.1 |
| ^NDX      |     -2 |   -10.6 |
| ^RUT      |     +2 |    +3.0 |
| ^STOXX50E |     +1 |    +6.4 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Exxon Mobil Corporation / XOM** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **WTI Crude Oil / CL=F** — malformed_input
- **Copper / HG=F** — malformed_input
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Natural Gas / NG=F** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Nikkei 225 / ^N225** — missing_bars

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|    4 | Brent Crude Oil / BZ=F |  74.2 |   Yes    | —               | 20d up +12.3%; above MA20 by 6.2%; RSI14=74   |
|   15 | Soybeans / ZS=F        |  37.3 |   Yes    | —               | 20d down -5.0%; below MA20 by 3.5%; RSI14=12  |
|   17 | Gold / GC=F            |  30.0 |   Yes    | —               | 20d down -4.1%; below MA20 by 2.3%; RSI14=31  |
|   20 | Corn / ZC=F            |  27.0 |   Yes    | —               | 20d down -10.2%; below MA20 by 5.0%; RSI14=17 |
|   21 | Wheat / ZW=F           |  21.5 |   Yes    | —               | 20d down -11.6%; below MA20 by 7.6%; RSI14=12 |
|   23 | Platinum / PL=F        |  10.3 |   Yes    | —               | 20d down -12.4%; below MA20 by 7.6%; RSI14=19 |
|   24 | Silver / SI=F          |   7.6 |   Yes    | —               | 20d down -14.1%; below MA20 by 8.8%; RSI14=20 |
|   28 | WTI Crude Oil / CL=F   |  63.3 |    No    | malformed_input | Suppressed: malformed_input                   |
|   29 | Copper / HG=F          |  56.7 |    No    | malformed_input | Suppressed: malformed_input                   |
|   31 | Natural Gas / NG=F     |  49.7 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                    |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | ---------------------------------------------- |
|    1 | Apple Inc. / AAPL                                                              |  79.1 |   Yes    | —                             | 20d up +5.6%; above MA20 by 2.2%; RSI14=66     |
|    3 | Tesla Inc. / TSLA                                                              |  74.8 |   Yes    | —                             | 20d up +13.9%; above MA20 by 6.3%; RSI14=59    |
|    5 | JPMorgan Chase & Co. / JPM                                                     |  70.9 |   Yes    | —                             | 20d up +3.6%; above MA20 by 2.7%; RSI14=64     |
|    6 | UnitedHealth Group Inc. / UNH                                                  |  64.8 |   Yes    | —                             | 20d up +12.5%; above MA20 by 3.5%; RSI14=68    |
|    9 | Microsoft Corporation / MSFT                                                   |  61.8 |   Yes    | —                             | 20d up +3.4%; below MA20 by 0.1%; RSI14=46     |
|   16 | NVIDIA Corporation / NVDA                                                      |  30.6 |   Yes    | —                             | 20d down -7.5%; below MA20 by 4.2%; RSI14=35   |
|   19 | Meta Platforms Inc. / META                                                     |  27.6 |   Yes    | —                             | 20d down -14.0%; below MA20 by 10.4%; RSI14=28 |
|   22 | Amazon.com Inc. / AMZN                                                         |  20.6 |   Yes    | —                             | 20d down -1.8%; below MA20 by 4.4%; RSI14=34   |
|   25 | Alphabet Inc. Class A / GOOGL                                                  |   3.0 |   Yes    | —                             | 20d down -16.1%; below MA20 by 15.8%; RSI14=16 |
|   26 | Exxon Mobil Corporation / XOM                                                  |  80.3 |    No    | malformed_input               | Suppressed: malformed_input                    |
|   27 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  65.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   30 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  56.1 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   32 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  48.5 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    2 | DAX / ^GDAXI                        |  77.6 |   Yes    | —            | 20d up +4.4%; above MA20 by 2.7%; RSI14=69   |
|    7 | FTSE 100 / ^FTSE                    |  63.6 |   Yes    | —            | 20d up +2.8%; above MA20 by 0.6%; RSI14=61   |
|    8 | Russell 2000 / ^RUT                 |  63.0 |   Yes    | —            | 20d up +1.9%; above MA20 by 2.4%; RSI14=58   |
|   10 | CAC 40 / ^FCHI                      |  61.5 |   Yes    | —            | 20d up +1.7%; above MA20 by 1.4%; RSI14=62   |
|   11 | Dow Jones Industrial Average / ^DJI |  60.9 |   Yes    | —            | 20d up +2.8%; above MA20 by 0.7%; RSI14=61   |
|   12 | S&P 500 / ^GSPC                     |  58.8 |   Yes    | —            | 20d up +0.7%; below MA20 by 0.2%; RSI14=42   |
|   13 | Euro Stoxx 50 / ^STOXX50E           |  56.1 |   Yes    | —            | 20d up +0.5%; above MA20 by 0.6%; RSI14=53   |
|   14 | NASDAQ 100 / ^NDX                   |  42.1 |   Yes    | —            | 20d down -3.6%; below MA20 by 2.2%; RSI14=34 |
|   18 | Hang Seng / ^HSI                    |  29.1 |   Yes    | —            | 20d down -6.4%; below MA20 by 3.5%; RSI14=36 |
|   33 | Nikkei 225 / ^N225                  |  46.4 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-10-29 |
| 7203.T    | 2026-10-29 |
| 8306.T    | 2026-10-29 |
| AAPL      | 2026-10-29 |
| AMZN      | 2026-10-29 |
| BZ=F      | 2026-10-29 |
| CL=F      | 2026-10-29 |
| GC=F      | 2026-10-29 |
| GOOGL     | 2026-10-29 |
| HG=F      | 2026-10-29 |
| JPM       | 2026-10-29 |
| META      | 2026-10-29 |
| MSFT      | 2026-10-29 |
| NG=F      | 2026-10-29 |
| NVDA      | 2026-10-29 |
| PL=F      | 2026-10-29 |
| SI=F      | 2026-10-29 |
| TSLA      | 2026-10-29 |
| UNH       | 2026-10-29 |
| XOM       | 2026-10-29 |
| ZC=F      | 2026-10-29 |
| ZS=F      | 2026-10-29 |
| ZW=F      | 2026-10-29 |
| ^DJI      | 2026-10-29 |
| ^FCHI     | 2026-10-29 |
| ^FTSE     | 2026-10-29 |
| ^GDAXI    | 2026-10-29 |
| ^GSPC     | 2026-10-29 |
| ^HSI      | 2026-10-29 |
| ^N225     | 2026-10-29 |
| ^NDX      | 2026-10-29 |
| ^RUT      | 2026-10-29 |
| ^STOXX50E | 2026-10-29 |

## Symbol Details

### Apple Inc. / AAPL (score 79.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.5% |
| ret_5d     |  +0.2% |
| ret_20d    |  +5.6% |
| ret_60d    | +12.3% |
| ma20_dist  |  +2.2% |
| ma50_dist  |  +5.0% |
| vol_20d    |  13.5% |
| mdd_60d    |   3.9% |
| rsi_14     |   66.5 |
| zscore_20d |    1.6 |

### DAX / ^GDAXI (score 77.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.3% |
| ret_5d     | +2.6% |
| ret_20d    | +4.4% |
| ret_60d    | -0.4% |
| ma20_dist  | +2.7% |
| ma50_dist  | +1.8% |
| vol_20d    | 13.9% |
| mdd_60d    |  6.6% |
| rsi_14     |  68.7 |
| zscore_20d |   2.6 |

### Tesla Inc. / TSLA (score 74.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.2% |
| ret_5d     |  +7.7% |
| ret_20d    | +13.9% |
| ret_60d    | +25.4% |
| ma20_dist  |  +6.3% |
| ma50_dist  |  +9.4% |
| vol_20d    |  38.5% |
| mdd_60d    |   7.3% |
| rsi_14     |   59.1 |
| zscore_20d |    1.8 |

### Brent Crude Oil / BZ=F (score 74.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.4% |
| ret_5d     |  +1.5% |
| ret_20d    | +12.3% |
| ret_60d    | +31.0% |
| ma20_dist  |  +6.2% |
| ma50_dist  | +11.7% |
| vol_20d    |  28.2% |
| mdd_60d    |   8.7% |
| rsi_14     |   74.1 |
| zscore_20d |    1.3 |

### JPMorgan Chase & Co. / JPM (score 70.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.3% |
| ret_5d     | +2.1% |
| ret_20d    | +3.6% |
| ret_60d    | -4.4% |
| ma20_dist  | +2.7% |
| ma50_dist  | +0.2% |
| vol_20d    | 13.0% |
| mdd_60d    |  9.9% |
| rsi_14     |  63.7 |
| zscore_20d |   2.7 |

### UnitedHealth Group Inc. / UNH (score 64.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.9% |
| ret_5d     |  -3.3% |
| ret_20d    | +12.5% |
| ret_60d    |  -0.4% |
| ma20_dist  |  +3.5% |
| ma50_dist  |  +5.6% |
| vol_20d    |  27.7% |
| mdd_60d    |  10.7% |
| rsi_14     |   68.5 |
| zscore_20d |    0.8 |

### FTSE 100 / ^FTSE (score 63.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | -0.0% |
| ret_20d    | +2.8% |
| ret_60d    | -1.5% |
| ma20_dist  | +0.6% |
| ma50_dist  | +0.2% |
| vol_20d    |  9.5% |
| mdd_60d    |  4.3% |
| rsi_14     |  61.1 |
| zscore_20d |   0.5 |

### Russell 2000 / ^RUT (score 63.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.0% |
| ret_5d     | +2.7% |
| ret_20d    | +1.9% |
| ret_60d    | -5.3% |
| ma20_dist  | +2.4% |
| ma50_dist  | -0.1% |
| vol_20d    | 14.9% |
| mdd_60d    | 11.3% |
| rsi_14     |  58.3 |
| zscore_20d |   1.8 |

### Microsoft Corporation / MSFT (score 61.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | +1.7% |
| ret_20d    | +3.4% |
| ret_60d    | +9.0% |
| ma20_dist  | -0.1% |
| ma50_dist  | +3.5% |
| vol_20d    | 19.1% |
| mdd_60d    |  5.1% |
| rsi_14     |  46.3 |
| zscore_20d |  -0.1 |

### CAC 40 / ^FCHI (score 61.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | +2.0% |
| ret_20d    | +1.7% |
| ret_60d    | -8.4% |
| ma20_dist  | +1.4% |
| ma50_dist  | -1.2% |
| vol_20d    | 12.2% |
| mdd_60d    | 11.4% |
| rsi_14     |  62.0 |
| zscore_20d |   1.9 |

### Dow Jones Industrial Average / ^DJI (score 60.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | -1.0% |
| ret_20d    | +2.8% |
| ret_60d    | -3.7% |
| ma20_dist  | +0.7% |
| ma50_dist  | +0.2% |
| vol_20d    |  8.7% |
| mdd_60d    |  5.8% |
| rsi_14     |  60.9 |
| zscore_20d |   0.7 |

### S&P 500 / ^GSPC (score 58.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | +0.7% |
| ret_20d    | +0.7% |
| ret_60d    | -0.0% |
| ma20_dist  | -0.2% |
| ma50_dist  | +0.3% |
| vol_20d    |  9.9% |
| mdd_60d    |  3.2% |
| rsi_14     |  42.1 |
| zscore_20d |  -0.3 |

### Euro Stoxx 50 / ^STOXX50E (score 56.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | +2.0% |
| ret_20d    | +0.5% |
| ret_60d    | -4.5% |
| ma20_dist  | +0.6% |
| ma50_dist  | -1.1% |
| vol_20d    | 13.5% |
| mdd_60d    |  7.4% |
| rsi_14     |  52.9 |
| zscore_20d |   0.7 |

### NASDAQ 100 / ^NDX (score 42.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.4% |
| ret_5d     | +1.5% |
| ret_20d    | -3.6% |
| ret_60d    | -0.3% |
| ma20_dist  | -2.2% |
| ma50_dist  | -1.4% |
| vol_20d    | 19.7% |
| mdd_60d    |  7.3% |
| rsi_14     |  33.7 |
| zscore_20d |  -0.9 |

### Soybeans / ZS=F (score 37.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -2.7% |
| ret_20d    | -5.0% |
| ret_60d    | +3.2% |
| ma20_dist  | -3.5% |
| ma50_dist  | -4.7% |
| vol_20d    | 10.3% |
| mdd_60d    |  8.2% |
| rsi_14     |  11.9 |
| zscore_20d |  -1.8 |

### NVIDIA Corporation / NVDA (score 30.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | +0.7% |
| ret_20d    | -7.5% |
| ret_60d    | -2.5% |
| ma20_dist  | -4.2% |
| ma50_dist  | -3.7% |
| vol_20d    | 29.2% |
| mdd_60d    | 11.8% |
| rsi_14     |  34.7 |
| zscore_20d |  -1.0 |

### Gold / GC=F (score 30.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | -0.7% |
| ret_20d    | -4.1% |
| ret_60d    | -7.6% |
| ma20_dist  | -2.3% |
| ma50_dist  | -6.4% |
| vol_20d    | 15.2% |
| mdd_60d    | 14.8% |
| rsi_14     |  30.7 |
| zscore_20d |  -1.6 |

### Hang Seng / ^HSI (score 29.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.6% |
| ret_5d     |  +0.1% |
| ret_20d    |  -6.4% |
| ret_60d    | -11.2% |
| ma20_dist  |  -3.5% |
| ma50_dist  |  -6.7% |
| vol_20d    |  18.3% |
| mdd_60d    |  11.8% |
| rsi_14     |   35.5 |
| zscore_20d |   -1.6 |

### Meta Platforms Inc. / META (score 27.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.0% |
| ret_5d     |  -3.7% |
| ret_20d    | -14.0% |
| ret_60d    |  +6.1% |
| ma20_dist  | -10.4% |
| ma50_dist  |  -6.6% |
| vol_20d    |  36.6% |
| mdd_60d    |  21.2% |
| rsi_14     |   27.8 |
| zscore_20d |   -1.5 |

### Corn / ZC=F (score 27.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.1% |
| ret_5d     |  -2.0% |
| ret_20d    | -10.2% |
| ret_60d    |  -2.9% |
| ma20_dist  |  -5.0% |
| ma50_dist  |  -9.8% |
| vol_20d    |  18.5% |
| mdd_60d    |  17.4% |
| rsi_14     |   17.2 |
| zscore_20d |   -1.3 |

### Wheat / ZW=F (score 21.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.8% |
| ret_5d     |  -3.4% |
| ret_20d    | -11.6% |
| ret_60d    |  -7.2% |
| ma20_dist  |  -7.6% |
| ma50_dist  | -12.7% |
| vol_20d    |  18.4% |
| mdd_60d    |  21.9% |
| rsi_14     |   11.7 |
| zscore_20d |   -1.6 |

### Amazon.com Inc. / AMZN (score 20.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -4.2% |
| ret_5d     |  -2.6% |
| ret_20d    |  -1.8% |
| ret_60d    | -10.6% |
| ma20_dist  |  -4.4% |
| ma50_dist  |  -4.3% |
| vol_20d    |  35.3% |
| mdd_60d    |  12.3% |
| rsi_14     |   34.1 |
| zscore_20d |   -2.1 |

### Platinum / PL=F (score 10.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -3.4% |
| ret_5d     |  -4.6% |
| ret_20d    | -12.4% |
| ret_60d    | -14.3% |
| ma20_dist  |  -7.6% |
| ma50_dist  | -13.4% |
| vol_20d    |  28.3% |
| mdd_60d    |  21.9% |
| rsi_14     |   19.4 |
| zscore_20d |   -2.1 |

### Silver / SI=F (score 7.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.4% |
| ret_5d     |  -4.7% |
| ret_20d    | -14.1% |
| ret_60d    | -19.8% |
| ma20_dist  |  -8.8% |
| ma50_dist  | -15.9% |
| vol_20d    |  33.4% |
| mdd_60d    |  24.9% |
| rsi_14     |   19.7 |
| zscore_20d |   -1.8 |

### Alphabet Inc. Class A / GOOGL (score 3.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     | -12.6% |
| ret_5d     | -12.5% |
| ret_20d    | -16.1% |
| ret_60d    | -21.6% |
| ma20_dist  | -15.8% |
| ma50_dist  | -16.6% |
| vol_20d    |  47.9% |
| mdd_60d    |  20.6% |
| rsi_14     |   15.6 |
| zscore_20d |   -3.1 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Apple Inc. / AAPL                   |   6.0643 |           1.7% |                 0.74x |       12.1286 |            3.5% |
| DAX / ^GDAXI                        | 312.9127 |           1.2% |                 0.72x |      625.8253 |            2.4% |
| Tesla Inc. / TSLA                   |  13.5557 |           3.4% |                 0.26x |       27.1114 |            6.7% |
| Brent Crude Oil / BZ=F              |   3.8271 |           3.3% |                 0.35x |        7.6543 |            6.7% |
| JPMorgan Chase & Co. / JPM          |   6.4879 |           1.9% |                 0.77x |       12.9757 |            3.8% |
| UnitedHealth Group Inc. / UNH       |  12.8571 |           3.1% |                 0.36x |       25.7143 |            6.3% |
| FTSE 100 / ^FTSE                    | 105.7572 |           1.0% |                 1.05x |      211.5144 |            2.0% |
| Russell 2000 / ^RUT                 |  33.7214 |           1.2% |                 0.67x |       67.4428 |            2.4% |
| Microsoft Corporation / MSFT        |  11.1579 |           2.1% |                 0.52x |       22.3157 |            4.2% |
| CAC 40 / ^FCHI                      |  86.3565 |           1.1% |                 0.82x |      172.7130 |            2.2% |
| Dow Jones Industrial Average / ^DJI | 497.0745 |           0.9% |                 1.15x |      994.1490 |            1.9% |
| S&P 500 / ^GSPC                     |  70.7036 |           0.9% |                 1.01x |      141.4072 |            1.8% |
| Euro Stoxx 50 / ^STOXX50E           |  71.9744 |           1.2% |                 0.74x |      143.9487 |            2.3% |
| NASDAQ 100 / ^NDX                   | 516.3612 |           1.8% |                 0.51x |     1032.7224 |            3.5% |
| Soybeans / ZS=F                     |  16.7500 |           1.4% |                 0.97x |       33.5000 |            2.7% |
| NVIDIA Corporation / NVDA           |   5.9429 |           2.8% |                 0.34x |       11.8857 |            5.6% |
| Gold / GC=F                         |  68.1857 |           1.7% |                 0.66x |      136.3713 |            3.4% |
| Hang Seng / ^HSI                    | 371.0590 |           1.6% |                 0.55x |      742.1180 |            3.2% |
| Meta Platforms Inc. / META          |  26.2886 |           4.2% |                 0.27x |       52.5771 |            8.4% |
| Corn / ZC=F                         |   7.4464 |           1.7% |                 0.54x |       14.8929 |            3.3% |
| Wheat / ZW=F                        |  14.3214 |           2.4% |                 0.54x |       28.6429 |            4.7% |
| Amazon.com Inc. / AMZN              |   7.0007 |           2.9% |                 0.28x |       14.0014 |            5.7% |
| Platinum / PL=F                     |  28.9929 |           1.9% |                 0.35x |       57.9857 |            3.9% |
| Silver / SI=F                       |   1.1391 |           2.2% |                 0.30x |        2.2783 |            4.4% |
| Alphabet Inc. Class A / GOOGL       |  10.7779 |           3.8% |                 0.21x |       21.5557 |            7.6% |

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

Scoring engine version: **1.0.0** | Git commit: **177e686**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
