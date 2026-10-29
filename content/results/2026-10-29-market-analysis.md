+++
title = "Market Analysis 2026-10-29"
date = "2026-10-29T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: BZ=F (score 83.9)."
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
source_files = ["data/analysis/2026-10-29.json", "data/history/2026-10-29.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "d989f4b"
+++

## Market Regime

**Neutral** — 12 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Brent Crude Oil / BZ=F** — score 83.9, 20d return +11.4%, RSI14=76. 20d up +11.4%; above MA20 by 7.2%; RSI14=76
- **Tesla Inc. / TSLA** — score 73.9, 20d return +13.9%, RSI14=62. 20d up +13.9%; above MA20 by 7.3%; RSI14=62
- **DAX / ^GDAXI** — score 71.2, 20d return +2.0%, RSI14=68. 20d up +2.0%; above MA20 by 1.5%; RSI14=68
- **JPMorgan Chase & Co. / JPM** — score 69.4, 20d return +3.1%, RSI14=61. 20d up +3.1%; above MA20 by 1.7%; RSI14=61
- **Apple Inc. / AAPL** — score 67.6, 20d return +3.2%, RSI14=55. 20d up +3.2%; above MA20 by 0.9%; RSI14=55 ⚠️ Upcoming: AAPL earnings release (2026-11-02)

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                        | Applies To                    |
| ---------- | ---------------------------- | ----------------------------- |
| 2026-10-30 | BOJ monetary policy decision | 6758.T, 7203.T, 8306.T, ^N225 |
| 2026-10-30 | XOM earnings release         | XOM                           |
| 2026-11-02 | AAPL earnings release        | AAPL                          |
| 2026-11-05 | 6758.T earnings release      | 6758.T                        |
| 2026-11-05 | 7203.T earnings release      | 7203.T                        |

## Signal History

Compared with the previous available report (**2026-10-28**).

- **New top-5:** JPM
- **Persistent top signals:** BZ=F (9 reports), TSLA (3 reports), AAPL (2 reports), ^GDAXI (2 reports)
- **Dropped from top-5:** ^DJI

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     -3 |   -17.0 |
| 7203.T    |     -2 |    -9.1 |
| 8306.T    |     -2 |    -6.7 |
| AAPL      |     -4 |   -14.2 |
| AMZN      |     +1 |    -1.8 |
| BZ=F      |     +2 |    +8.2 |
| CL=F      |     +3 |   +19.4 |
| GC=F      |     +1 |    -7.0 |
| GOOGL     |     +1 |    +3.9 |
| HG=F      |     +1 |    +0.3 |
| JPM       |     +6 |   +11.2 |
| META      |     +2 |    +0.0 |
| MSFT      |     +0 |    +1.8 |
| NG=F      |     +1 |   +13.9 |
| NVDA      |     -6 |   -16.4 |
| PL=F      |     +0 |    +4.8 |
| SI=F      |     -1 |    -7.9 |
| TSLA      |     +0 |    -7.9 |
| UNH       |     -2 |    -0.9 |
| XOM       |     +1 |    +9.7 |
| ZC=F      |     +2 |    +8.5 |
| ZS=F      |     +1 |    +1.2 |
| ZW=F      |     -1 |    -3.3 |
| ^DJI      |     -1 |    +0.0 |
| ^FCHI     |     +1 |    +0.3 |
| ^FTSE     |     +2 |    +3.0 |
| ^GDAXI    |     +1 |    +2.4 |
| ^GSPC     |     -2 |    +0.6 |
| ^HSI      |     +0 |    +3.3 |
| ^N225     |     +1 |    +4.2 |
| ^NDX      |     +0 |    -1.5 |
| ^RUT      |     -2 |    -0.3 |
| ^STOXX50E |     -1 |    -3.0 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Exxon Mobil Corporation / XOM** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input
- **Copper / HG=F** — malformed_input
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Nikkei 225 / ^N225** — missing_bars
- **Natural Gas / NG=F** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|    1 | Brent Crude Oil / BZ=F |  83.9 |   Yes    | —               | 20d up +11.4%; above MA20 by 7.2%; RSI14=76   |
|   16 | Soybeans / ZS=F        |  40.3 |   Yes    | —               | 20d down -5.3%; below MA20 by 3.4%; RSI14=17  |
|   17 | Gold / GC=F            |  30.9 |   Yes    | —               | 20d down -3.2%; below MA20 by 2.1%; RSI14=40  |
|   19 | Corn / ZC=F            |  28.5 |   Yes    | —               | 20d down -9.8%; below MA20 by 5.4%; RSI14=12  |
|   22 | Platinum / PL=F        |  22.4 |   Yes    | —               | 20d down -9.1%; below MA20 by 4.9%; RSI14=37  |
|   24 | Wheat / ZW=F           |  11.5 |   Yes    | —               | 20d down -11.4%; below MA20 by 8.9%; RSI14=6  |
|   25 | Silver / SI=F          |   6.7 |   Yes    | —               | 20d down -11.1%; below MA20 by 7.3%; RSI14=30 |
|   27 | WTI Crude Oil / CL=F   |  75.8 |    No    | malformed_input | Suppressed: malformed_input                   |
|   28 | Copper / HG=F          |  66.7 |    No    | malformed_input | Suppressed: malformed_input                   |
|   32 | Natural Gas / NG=F     |  36.4 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                    |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | ---------------------------------------------- |
|    2 | Tesla Inc. / TSLA                                                              |  73.9 |   Yes    | —                             | 20d up +13.9%; above MA20 by 7.3%; RSI14=62    |
|    4 | JPMorgan Chase & Co. / JPM                                                     |  69.4 |   Yes    | —                             | 20d up +3.1%; above MA20 by 1.7%; RSI14=61     |
|    5 | Apple Inc. / AAPL                                                              |  67.6 |   Yes    | —                             | 20d up +3.2%; above MA20 by 0.9%; RSI14=55     |
|    7 | Microsoft Corporation / MSFT                                                   |  63.0 |   Yes    | —                             | 20d up +3.5%; above MA20 by 0.2%; RSI14=55     |
|   11 | UnitedHealth Group Inc. / UNH                                                  |  58.2 |   Yes    | —                             | 20d up +10.9%; above MA20 by 3.2%; RSI14=70    |
|   15 | Amazon.com Inc. / AMZN                                                         |  40.9 |   Yes    | —                             | 20d up +2.2%; below MA20 by 0.2%; RSI14=50     |
|   18 | Alphabet Inc. Class A / GOOGL                                                  |  29.1 |   Yes    | —                             | 20d down -5.6%; below MA20 by 4.4%; RSI14=31   |
|   21 | NVIDIA Corporation / NVDA                                                      |  27.9 |   Yes    | —                             | 20d down -5.7%; below MA20 by 3.8%; RSI14=35   |
|   23 | Meta Platforms Inc. / META                                                     |  13.0 |   Yes    | —                             | 20d down -15.5%; below MA20 by 12.7%; RSI14=23 |
|   26 | Exxon Mobil Corporation / XOM                                                  |  82.7 |    No    | malformed_input               | Suppressed: malformed_input                    |
|   29 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  58.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   30 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  57.6 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   33 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  30.3 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    3 | DAX / ^GDAXI                        |  71.2 |   Yes    | —            | 20d up +2.0%; above MA20 by 1.5%; RSI14=68   |
|    6 | Dow Jones Industrial Average / ^DJI |  67.0 |   Yes    | —            | 20d up +3.1%; above MA20 by 1.1%; RSI14=68   |
|    8 | S&P 500 / ^GSPC                     |  63.0 |   Yes    | —            | 20d up +1.2%; above MA20 by 0.1%; RSI14=48   |
|    9 | FTSE 100 / ^FTSE                    |  60.9 |   Yes    | —            | 20d up +0.8%; above MA20 by 0.4%; RSI14=65   |
|   10 | Russell 2000 / ^RUT                 |  60.0 |   Yes    | —            | 20d up +1.2%; above MA20 by 1.5%; RSI14=56   |
|   12 | NASDAQ 100 / ^NDX                   |  52.7 |   Yes    | —            | 20d down -2.0%; below MA20 by 1.0%; RSI14=39 |
|   13 | CAC 40 / ^FCHI                      |  51.8 |   Yes    | —            | 20d down -1.0%; above MA20 by 0.5%; RSI14=62 |
|   14 | Euro Stoxx 50 / ^STOXX50E           |  49.7 |   Yes    | —            | 20d down -1.6%; below MA20 by 0.0%; RSI14=53 |
|   20 | Hang Seng / ^HSI                    |  28.5 |   Yes    | —            | 20d down -6.3%; below MA20 by 3.3%; RSI14=33 |
|   31 | Nikkei 225 / ^N225                  |  40.3 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-10-28 |
| 7203.T    | 2026-10-28 |
| 8306.T    | 2026-10-28 |
| AAPL      | 2026-10-28 |
| AMZN      | 2026-10-28 |
| BZ=F      | 2026-10-28 |
| CL=F      | 2026-10-28 |
| GC=F      | 2026-10-28 |
| GOOGL     | 2026-10-28 |
| HG=F      | 2026-10-28 |
| JPM       | 2026-10-28 |
| META      | 2026-10-28 |
| MSFT      | 2026-10-28 |
| NG=F      | 2026-10-28 |
| NVDA      | 2026-10-28 |
| PL=F      | 2026-10-28 |
| SI=F      | 2026-10-28 |
| TSLA      | 2026-10-28 |
| UNH       | 2026-10-28 |
| XOM       | 2026-10-28 |
| ZC=F      | 2026-10-28 |
| ZS=F      | 2026-10-28 |
| ZW=F      | 2026-10-28 |
| ^DJI      | 2026-10-28 |
| ^FCHI     | 2026-10-28 |
| ^FTSE     | 2026-10-28 |
| ^GDAXI    | 2026-10-28 |
| ^GSPC     | 2026-10-28 |
| ^HSI      | 2026-10-28 |
| ^N225     | 2026-10-28 |
| ^NDX      | 2026-10-28 |
| ^RUT      | 2026-10-28 |
| ^STOXX50E | 2026-10-28 |

## Symbol Details

### Brent Crude Oil / BZ=F (score 83.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.3% |
| ret_5d     |  +6.0% |
| ret_20d    | +11.4% |
| ret_60d    | +36.8% |
| ma20_dist  |  +7.2% |
| ma50_dist  | +12.6% |
| vol_20d    |  28.7% |
| mdd_60d    |   8.7% |
| rsi_14     |   76.2 |
| zscore_20d |    1.5 |

### Tesla Inc. / TSLA (score 73.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.8% |
| ret_5d     |  +4.6% |
| ret_20d    | +13.9% |
| ret_60d    | +23.5% |
| ma20_dist  |  +7.3% |
| ma50_dist  | +10.0% |
| vol_20d    |  38.5% |
| mdd_60d    |   7.3% |
| rsi_14     |   62.2 |
| zscore_20d |    2.1 |

### DAX / ^GDAXI (score 71.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | +0.2% |
| ret_20d    | +2.0% |
| ret_60d    | -1.6% |
| ma20_dist  | +1.5% |
| ma50_dist  | +0.5% |
| vol_20d    | 13.9% |
| mdd_60d    |  6.6% |
| rsi_14     |  68.0 |
| zscore_20d |   1.8 |

### JPMorgan Chase & Co. / JPM (score 69.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.0% |
| ret_5d     | +1.2% |
| ret_20d    | +3.1% |
| ret_60d    | -5.1% |
| ma20_dist  | +1.7% |
| ma50_dist  | -1.1% |
| vol_20d    | 12.6% |
| mdd_60d    |  9.9% |
| rsi_14     |  60.9 |
| zscore_20d |   2.0 |

### Apple Inc. / AAPL (score 67.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.9% |
| ret_5d     |  -0.0% |
| ret_20d    |  +3.2% |
| ret_60d    | +11.2% |
| ma20_dist  |  +0.9% |
| ma50_dist  |  +3.6% |
| vol_20d    |  13.3% |
| mdd_60d    |   3.9% |
| rsi_14     |   54.7 |
| zscore_20d |    0.6 |

### Dow Jones Industrial Average / ^DJI (score 67.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | -0.7% |
| ret_20d    | +3.1% |
| ret_60d    | -3.0% |
| ma20_dist  | +1.1% |
| ma50_dist  | +0.4% |
| vol_20d    |  8.6% |
| mdd_60d    |  6.3% |
| rsi_14     |  68.1 |
| zscore_20d |   1.0 |

### Microsoft Corporation / MSFT (score 63.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | -0.4% |
| ret_20d    | +3.5% |
| ret_60d    | +8.0% |
| ma20_dist  | +0.2% |
| ma50_dist  | +3.9% |
| vol_20d    | 19.0% |
| mdd_60d    |  5.1% |
| rsi_14     |  55.3 |
| zscore_20d |   0.1 |

### S&P 500 / ^GSPC (score 63.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | -0.2% |
| ret_20d    | +1.2% |
| ret_60d    | +0.1% |
| ma20_dist  | +0.1% |
| ma50_dist  | +0.6% |
| vol_20d    |  9.8% |
| mdd_60d    |  3.2% |
| rsi_14     |  48.2 |
| zscore_20d |   0.2 |

### FTSE 100 / ^FTSE (score 60.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | -0.5% |
| ret_20d    | +0.8% |
| ret_60d    | -1.7% |
| ma20_dist  | +0.4% |
| ma50_dist  | -0.1% |
| vol_20d    | 11.4% |
| mdd_60d    |  4.3% |
| rsi_14     |  64.9 |
| zscore_20d |   0.4 |

### Russell 2000 / ^RUT (score 60.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | +1.8% |
| ret_20d    | +1.2% |
| ret_60d    | -6.8% |
| ma20_dist  | +1.5% |
| ma50_dist  | -1.3% |
| vol_20d    | 14.6% |
| mdd_60d    | 11.3% |
| rsi_14     |  56.1 |
| zscore_20d |   1.2 |

### UnitedHealth Group Inc. / UNH (score 58.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.8% |
| ret_5d     |  -2.4% |
| ret_20d    | +10.9% |
| ret_60d    |  -0.1% |
| ma20_dist  |  +3.2% |
| ma50_dist  |  +4.8% |
| vol_20d    |  27.9% |
| mdd_60d    |  11.5% |
| rsi_14     |   70.1 |
| zscore_20d |    0.7 |

### NASDAQ 100 / ^NDX (score 52.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | -0.0% |
| ret_20d    | -2.0% |
| ret_60d    | +0.3% |
| ma20_dist  | -1.0% |
| ma50_dist  | -0.0% |
| vol_20d    | 19.2% |
| mdd_60d    |  7.3% |
| rsi_14     |  39.4 |
| zscore_20d |  -0.4 |

### CAC 40 / ^FCHI (score 51.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.0% |
| ret_5d     | -0.4% |
| ret_20d    | -1.0% |
| ret_60d    | -9.0% |
| ma20_dist  | +0.5% |
| ma50_dist  | -2.3% |
| vol_20d    | 13.0% |
| mdd_60d    | 11.4% |
| rsi_14     |  61.5 |
| zscore_20d |   0.7 |

### Euro Stoxx 50 / ^STOXX50E (score 49.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | -0.6% |
| ret_20d    | -1.6% |
| ret_60d    | -4.8% |
| ma20_dist  | -0.0% |
| ma50_dist  | -1.8% |
| vol_20d    | 14.3% |
| mdd_60d    |  7.4% |
| rsi_14     |  53.4 |
| zscore_20d |  -0.1 |

### Amazon.com Inc. / AMZN (score 40.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | -3.0% |
| ret_20d    | +2.2% |
| ret_60d    | -8.2% |
| ma20_dist  | -0.2% |
| ma50_dist  | -0.2% |
| vol_20d    | 31.9% |
| mdd_60d    | 11.6% |
| rsi_14     |  50.5 |
| zscore_20d |  -0.1 |

### Soybeans / ZS=F (score 40.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -1.7% |
| ret_20d    | -5.3% |
| ret_60d    | +5.9% |
| ma20_dist  | -3.4% |
| ma50_dist  | -4.3% |
| vol_20d    | 10.4% |
| mdd_60d    |  7.8% |
| rsi_14     |  16.7 |
| zscore_20d |  -1.9 |

### Gold / GC=F (score 30.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | -2.4% |
| ret_20d    | -3.2% |
| ret_60d    | -7.5% |
| ma20_dist  | -2.1% |
| ma50_dist  | -6.2% |
| vol_20d    | 15.3% |
| mdd_60d    | 14.8% |
| rsi_14     |  39.8 |
| zscore_20d |  -1.5 |

### Alphabet Inc. Class A / GOOGL (score 29.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.3% |
| ret_5d     |  -2.9% |
| ret_20d    |  -5.6% |
| ret_60d    | -13.9% |
| ma20_dist  |  -4.4% |
| ma50_dist  |  -4.9% |
| vol_20d    |  21.6% |
| mdd_60d    |  12.5% |
| rsi_14     |   30.8 |
| zscore_20d |   -1.3 |

### Corn / ZC=F (score 28.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | -2.5% |
| ret_20d    | -9.8% |
| ret_60d    | +2.9% |
| ma20_dist  | -5.4% |
| ma50_dist  | -9.8% |
| vol_20d    | 18.6% |
| mdd_60d    | 17.4% |
| rsi_14     |  11.8 |
| zscore_20d |  -1.4 |

### Hang Seng / ^HSI (score 28.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.2% |
| ret_5d     |  -2.4% |
| ret_20d    |  -6.3% |
| ret_60d    | -11.2% |
| ma20_dist  |  -3.3% |
| ma50_dist  |  -6.4% |
| vol_20d    |  18.3% |
| mdd_60d    |  11.8% |
| rsi_14     |   33.1 |
| zscore_20d |   -1.5 |

### NVIDIA Corporation / NVDA (score 27.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.2% |
| ret_5d     | -3.0% |
| ret_20d    | -5.7% |
| ret_60d    | +1.6% |
| ma20_dist  | -3.8% |
| ma50_dist  | -3.0% |
| vol_20d    | 29.6% |
| mdd_60d    | 11.8% |
| rsi_14     |  35.0 |
| zscore_20d |  -0.9 |

### Platinum / PL=F (score 22.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.8% |
| ret_5d     |  -4.8% |
| ret_20d    |  -9.1% |
| ret_60d    | -12.0% |
| ma20_dist  |  -4.9% |
| ma50_dist  | -10.7% |
| vol_20d    |  26.6% |
| mdd_60d    |  19.8% |
| rsi_14     |   37.1 |
| zscore_20d |   -1.5 |

### Meta Platforms Inc. / META (score 13.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.2% |
| ret_5d     | -12.2% |
| ret_20d    | -15.5% |
| ret_60d    |  +4.2% |
| ma20_dist  | -12.7% |
| ma50_dist  |  -8.1% |
| vol_20d    |  35.4% |
| mdd_60d    |  21.2% |
| rsi_14     |   23.2 |
| zscore_20d |   -2.0 |

### Wheat / ZW=F (score 11.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.8% |
| ret_5d     |  -4.7% |
| ret_20d    | -11.4% |
| ret_60d    |  -6.4% |
| ma20_dist  |  -8.9% |
| ma50_dist  | -13.6% |
| vol_20d    |  18.6% |
| mdd_60d    |  21.9% |
| rsi_14     |    5.8 |
| zscore_20d |   -2.0 |

### Silver / SI=F (score 6.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.5% |
| ret_5d     |  -6.9% |
| ret_20d    | -11.1% |
| ret_60d    | -15.9% |
| ma20_dist  |  -7.3% |
| ma50_dist  | -14.4% |
| vol_20d    |  33.4% |
| mdd_60d    |  23.0% |
| rsi_14     |   30.4 |
| zscore_20d |   -1.6 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Brent Crude Oil / BZ=F              |   3.7907 |           3.3% |                 0.35x |        7.5814 |            6.6% |
| Tesla Inc. / TSLA                   |  14.0614 |           3.5% |                 0.26x |       28.1229 |            7.0% |
| DAX / ^GDAXI                        | 309.7412 |           1.2% |                 0.72x |      619.4824 |            2.4% |
| JPMorgan Chase & Co. / JPM          |   6.2386 |           1.8% |                 0.79x |       12.4771 |            3.7% |
| Apple Inc. / AAPL                   |   6.2157 |           1.8% |                 0.75x |       12.4314 |            3.6% |
| Dow Jones Industrial Average / ^DJI | 507.3956 |           1.0% |                 1.16x |     1014.7913 |            1.9% |
| Microsoft Corporation / MSFT        |  10.6493 |           2.0% |                 0.53x |       21.2986 |            4.0% |
| S&P 500 / ^GSPC                     |  70.8586 |           0.9% |                 1.02x |      141.7172 |            1.8% |
| FTSE 100 / ^FTSE                    | 109.7643 |           1.0% |                 0.88x |      219.5286 |            2.1% |
| Russell 2000 / ^RUT                 |  32.4371 |           1.1% |                 0.69x |       64.8743 |            2.3% |
| UnitedHealth Group Inc. / UNH       |  13.2943 |           3.3% |                 0.36x |       26.5886 |            6.5% |
| NASDAQ 100 / ^NDX                   | 492.4198 |           1.7% |                 0.52x |      984.8396 |            3.3% |
| CAC 40 / ^FCHI                      |  85.2486 |           1.1% |                 0.77x |      170.4973 |            2.2% |
| Euro Stoxx 50 / ^STOXX50E           |  72.1386 |           1.2% |                 0.70x |      144.2773 |            2.3% |
| Amazon.com Inc. / AMZN              |   6.6707 |           2.6% |                 0.31x |       13.3414 |            5.2% |
| Soybeans / ZS=F                     |  17.9821 |           1.5% |                 0.96x |       35.9643 |            2.9% |
| Gold / GC=F                         |  69.0571 |           1.7% |                 0.65x |      138.1142 |            3.4% |
| Alphabet Inc. Class A / GOOGL       |   8.0550 |           2.5% |                 0.46x |       16.1100 |            5.0% |
| Corn / ZC=F                         |   9.4286 |           2.1% |                 0.54x |       18.8571 |            4.2% |
| Hang Seng / ^HSI                    | 381.9911 |           1.7% |                 0.55x |      763.9821 |            3.3% |
| NVIDIA Corporation / NVDA           |   6.0507 |           2.8% |                 0.34x |       12.1014 |            5.6% |
| Platinum / PL=F                     |  28.1643 |           1.8% |                 0.38x |       56.3286 |            3.6% |
| Meta Platforms Inc. / META          |  25.5514 |           4.2% |                 0.28x |       51.1028 |            8.3% |
| Wheat / ZW=F                        |  15.1250 |           2.5% |                 0.54x |       30.2500 |            5.1% |
| Silver / SI=F                       |   1.1451 |           2.1% |                 0.30x |        2.2903 |            4.3% |

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

Scoring engine version: **1.0.0** | Git commit: **d989f4b**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
