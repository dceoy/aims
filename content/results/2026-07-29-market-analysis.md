+++
title = "Market Analysis 2026-07-29"
date = "2026-07-29T00:00:00+00:00"
draft = false
summary = "Neutral market: 26 reliable instruments. Top signal: AAPL (score 82.4)."
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
source_files = ["data/analysis/2026-07-29.json", "data/history/2026-07-29.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "85db1ab"
+++

## Market Regime

**Neutral** — 14 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Apple Inc. / AAPL** — score 82.4, 20d return +20.7%, RSI14=72. 20d up +20.7%; above MA20 by 6.3%; RSI14=72 ⚠️ Upcoming: AAPL earnings release (2026-07-30)
- **JPMorgan Chase & Co. / JPM** — score 81.8, 20d return +9.0%, RSI14=79. 20d up +9.0%; above MA20 by 4.7%; RSI14=79
- **FTSE 100 / ^FTSE** — score 79.1, 20d return +3.6%, RSI14=76. 20d up +3.6%; above MA20 by 2.5%; RSI14=76
- **CAC 40 / ^FCHI** — score 68.5, 20d return +0.7%, RSI14=68. 20d up +0.7%; above MA20 by 0.9%; RSI14=68
- **Corn / ZC=F** — score 67.6, 20d return +14.1%, RSI14=64. 20d up +14.1%; above MA20 by 3.6%; RSI14=64

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                        | Applies To                    |
| ---------- | ---------------------------- | ----------------------------- |
| 2026-07-30 | AAPL earnings release        | AAPL                          |
| 2026-07-30 | AMZN earnings release        | AMZN                          |
| 2026-07-31 | 6758.T earnings release      | 6758.T                        |
| 2026-07-31 | BOJ monetary policy decision | 6758.T, 7203.T, 8306.T, ^N225 |
| 2026-07-31 | XOM earnings release         | XOM                           |
| 2026-08-03 | 8306.T earnings release      | 8306.T                        |
| 2026-08-04 | 7203.T earnings release      | 7203.T                        |

## Signal History

Compared with the previous available report (**2026-07-28**).

- **New top-5:** ZC=F, ^FCHI
- **Persistent top signals:** ^FTSE (5 reports), AAPL (3 reports), JPM (3 reports)
- **Dropped from top-5:** ^GDAXI, ^HSI

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +1 |    +2.1 |
| 7203.T    |     +1 |    +0.3 |
| 8306.T    |     -1 |   -16.4 |
| AAPL      |     +1 |    +3.0 |
| AMZN      |     +1 |    +2.7 |
| BZ=F      |     -2 |   -11.5 |
| CL=F      |     +0 |   -11.2 |
| GC=F      |     +0 |    -6.7 |
| GOOGL     |     +1 |    +4.2 |
| HG=F      |     +0 |    -6.4 |
| JPM       |     -1 |    +0.3 |
| META      |     +2 |    +0.0 |
| MSFT      |     +0 |    +5.2 |
| NG=F      |     +0 |    -6.4 |
| NVDA      |     +1 |    +2.7 |
| PL=F      |     +1 |    -5.5 |
| SI=F      |     -3 |    -8.5 |
| TSLA      |     +0 |    +1.2 |
| UNH       |     +5 |   +19.1 |
| XOM       |     -1 |    -6.4 |
| ZC=F      |     +6 |   +15.5 |
| ZS=F      |     -1 |    +5.8 |
| ZW=F      |     +0 |    +9.1 |
| ^DJI      |     +2 |   +10.6 |
| ^FCHI     |     +3 |   +10.3 |
| ^FTSE     |     +0 |    +6.7 |
| ^GDAXI    |     -3 |    +0.3 |
| ^GSPC     |     -2 |    +0.9 |
| ^HSI      |     -3 |    +0.3 |
| ^N225     |     +0 |   -17.0 |
| ^NDX      |     -1 |    -2.1 |
| ^RUT      |     -1 |    -1.5 |
| ^STOXX50E |     -6 |    -0.9 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Copper / HG=F** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                    |
| ---: | ---------------------- | ----: | :------: | --------------- | ---------------------------------------------- |
|    5 | Corn / ZC=F            |  67.6 |   Yes    | —               | 20d up +14.1%; above MA20 by 3.6%; RSI14=64    |
|    9 | Wheat / ZW=F           |  62.7 |   Yes    | —               | 20d up +16.3%; above MA20 by 3.0%; RSI14=67    |
|   11 | Soybeans / ZS=F        |  58.8 |   Yes    | —               | 20d up +9.3%; above MA20 by 1.3%; RSI14=55     |
|   16 | Gold / GC=F            |  36.1 |   Yes    | —               | 20d up +0.3%; below MA20 by 0.8%; RSI14=47     |
|   17 | Platinum / PL=F        |  33.6 |   Yes    | —               | 20d up +2.4%; below MA20 by 0.0%; RSI14=57     |
|   19 | Brent Crude Oil / BZ=F |  29.7 |   Yes    | —               | 20d up +15.0%; above MA20 by 1.2%; RSI14=57    |
|   24 | Silver / SI=F          |  18.5 |   Yes    | —               | 20d down -1.5%; below MA20 by 2.5%; RSI14=48   |
|   25 | Natural Gas / NG=F     |  11.5 |   Yes    | —               | 20d down -16.3%; below MA20 by 10.9%; RSI14=17 |
|   31 | Copper / HG=F          |  55.1 |    No    | malformed_input | Suppressed: malformed_input                    |
|   32 | WTI Crude Oil / CL=F   |  31.5 |    No    | malformed_input | Suppressed: malformed_input                    |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                    |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | ---------------------------------------------- |
|    1 | Apple Inc. / AAPL                                                              |  82.4 |   Yes    | —                             | 20d up +20.7%; above MA20 by 6.3%; RSI14=72    |
|    2 | JPMorgan Chase & Co. / JPM                                                     |  81.8 |   Yes    | —                             | 20d up +9.0%; above MA20 by 4.7%; RSI14=79     |
|   10 | UnitedHealth Group Inc. / UNH                                                  |  62.4 |   Yes    | —                             | 20d up +2.1%; above MA20 by 0.9%; RSI14=52     |
|   14 | Microsoft Corporation / MSFT                                                   |  48.5 |   Yes    | —                             | 20d up +6.7%; above MA20 by 1.1%; RSI14=56     |
|   18 | Meta Platforms Inc. / META                                                     |  30.0 |   Yes    | —                             | 20d up +5.5%; below MA20 by 5.0%; RSI14=47     |
|   21 | NVIDIA Corporation / NVDA                                                      |  27.9 |   Yes    | —                             | 20d up +1.0%; below MA20 by 3.3%; RSI14=44     |
|   22 | Alphabet Inc. Class A / GOOGL                                                  |  24.9 |   Yes    | —                             | 20d down -5.6%; below MA20 by 4.8%; RSI14=37   |
|   23 | Amazon.com Inc. / AMZN                                                         |  21.8 |   Yes    | —                             | 20d down -3.9%; below MA20 by 5.1%; RSI14=36   |
|   26 | Tesla Inc. / TSLA                                                              |   6.1 |   Yes    | —                             | 20d down -25.3%; below MA20 by 19.1%; RSI14=18 |
|   27 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  78.8 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   28 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  69.4 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   29 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  67.0 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   30 | Exxon Mobil Corporation / XOM                                                  |  62.4 |    No    | malformed_input               | Suppressed: malformed_input                    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    3 | FTSE 100 / ^FTSE                    |  79.1 |   Yes    | —            | 20d up +3.6%; above MA20 by 2.5%; RSI14=76   |
|    4 | CAC 40 / ^FCHI                      |  68.5 |   Yes    | —            | 20d up +0.7%; above MA20 by 0.9%; RSI14=68   |
|    6 | Dow Jones Industrial Average / ^DJI |  67.0 |   Yes    | —            | 20d up +1.1%; above MA20 by 0.6%; RSI14=56   |
|    7 | DAX / ^GDAXI                        |  66.7 |   Yes    | —            | 20d up +1.9%; above MA20 by 1.2%; RSI14=64   |
|    8 | Hang Seng / ^HSI                    |  66.4 |   Yes    | —            | 20d up +9.9%; above MA20 by 3.8%; RSI14=67   |
|   12 | Euro Stoxx 50 / ^STOXX50E           |  57.9 |   Yes    | —            | 20d down -0.6%; above MA20 by 0.0%; RSI14=59 |
|   13 | Russell 2000 / ^RUT                 |  49.7 |   Yes    | —            | 20d down -1.9%; below MA20 by 0.6%; RSI14=49 |
|   15 | S&P 500 / ^GSPC                     |  47.3 |   Yes    | —            | 20d down -0.2%; below MA20 by 0.8%; RSI14=45 |
|   20 | NASDAQ 100 / ^NDX                   |  29.1 |   Yes    | —            | 20d down -6.8%; below MA20 by 4.6%; RSI14=33 |
|   33 | Nikkei 225 / ^N225                  |  20.0 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-07-28 |
| 7203.T    | 2026-07-28 |
| 8306.T    | 2026-07-28 |
| AAPL      | 2026-07-28 |
| AMZN      | 2026-07-28 |
| BZ=F      | 2026-07-28 |
| CL=F      | 2026-07-28 |
| GC=F      | 2026-07-28 |
| GOOGL     | 2026-07-28 |
| HG=F      | 2026-07-28 |
| JPM       | 2026-07-28 |
| META      | 2026-07-28 |
| MSFT      | 2026-07-28 |
| NG=F      | 2026-07-28 |
| NVDA      | 2026-07-28 |
| PL=F      | 2026-07-28 |
| SI=F      | 2026-07-28 |
| TSLA      | 2026-07-28 |
| UNH       | 2026-07-28 |
| XOM       | 2026-07-28 |
| ZC=F      | 2026-07-28 |
| ZS=F      | 2026-07-28 |
| ZW=F      | 2026-07-28 |
| ^DJI      | 2026-07-28 |
| ^FCHI     | 2026-07-28 |
| ^FTSE     | 2026-07-28 |
| ^GDAXI    | 2026-07-28 |
| ^GSPC     | 2026-07-28 |
| ^HSI      | 2026-07-28 |
| ^N225     | 2026-07-28 |
| ^NDX      | 2026-07-28 |
| ^RUT      | 2026-07-28 |
| ^STOXX50E | 2026-07-28 |

## Symbol Details

### Apple Inc. / AAPL (score 82.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.9% |
| ret_5d     |  +3.8% |
| ret_20d    | +20.7% |
| ret_60d    | +25.4% |
| ma20_dist  |  +6.3% |
| ma50_dist  | +10.5% |
| vol_20d    |  27.7% |
| mdd_60d    |  12.7% |
| rsi_14     |   72.3 |
| zscore_20d |    1.5 |

### JPMorgan Chase & Co. / JPM (score 81.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.3% |
| ret_5d     |  +3.5% |
| ret_20d    |  +9.0% |
| ret_60d    | +14.6% |
| ma20_dist  |  +4.7% |
| ma50_dist  | +10.4% |
| vol_20d    |  18.7% |
| mdd_60d    |   6.1% |
| rsi_14     |   78.6 |
| zscore_20d |    1.9 |

### FTSE 100 / ^FTSE (score 79.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.8% |
| ret_5d     | +2.7% |
| ret_20d    | +3.6% |
| ret_60d    | +4.9% |
| ma20_dist  | +2.5% |
| ma50_dist  | +3.6% |
| vol_20d    | 11.3% |
| mdd_60d    |  2.6% |
| rsi_14     |  75.5 |
| zscore_20d |   2.4 |

### CAC 40 / ^FCHI (score 68.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | +1.1% |
| ret_20d    | +0.7% |
| ret_60d    | +4.9% |
| ma20_dist  | +0.9% |
| ma50_dist  | +1.7% |
| vol_20d    | 13.6% |
| mdd_60d    |  4.2% |
| rsi_14     |  68.1 |
| zscore_20d |   1.2 |

### Corn / ZC=F (score 67.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.5% |
| ret_5d     |  +1.3% |
| ret_20d    | +14.1% |
| ret_60d    |  -1.3% |
| ma20_dist  |  +3.6% |
| ma50_dist  |  +5.0% |
| vol_20d    |  26.8% |
| mdd_60d    |  15.7% |
| rsi_14     |   64.3 |
| zscore_20d |    1.1 |

### Dow Jones Industrial Average / ^DJI (score 67.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.0% |
| ret_5d     | +1.0% |
| ret_20d    | +1.1% |
| ret_60d    | +6.2% |
| ma20_dist  | +0.6% |
| ma50_dist  | +2.3% |
| vol_20d    |  9.4% |
| mdd_60d    |  3.2% |
| rsi_14     |  56.0 |
| zscore_20d |   1.0 |

### DAX / ^GDAXI (score 66.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | +1.8% |
| ret_20d    | +1.9% |
| ret_60d    | +4.4% |
| ma20_dist  | +1.2% |
| ma50_dist  | +1.9% |
| vol_20d    | 15.8% |
| mdd_60d    |  4.7% |
| rsi_14     |  63.6 |
| zscore_20d |   1.0 |

### Hang Seng / ^HSI (score 66.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | +0.7% |
| ret_20d    | +9.9% |
| ret_60d    | -3.1% |
| ma20_dist  | +3.8% |
| ma50_dist  | +2.9% |
| vol_20d    | 18.4% |
| mdd_60d    | 14.9% |
| rsi_14     |  66.6 |
| zscore_20d |   1.3 |

### Wheat / ZW=F (score 62.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.4% |
| ret_5d     |  -2.3% |
| ret_20d    | +16.3% |
| ret_60d    |  +6.2% |
| ma20_dist  |  +3.0% |
| ma50_dist  |  +6.6% |
| vol_20d    |  37.5% |
| mdd_60d    |  14.6% |
| rsi_14     |   66.8 |
| zscore_20d |    0.5 |

### UnitedHealth Group Inc. / UNH (score 62.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.7% |
| ret_5d     |  -1.7% |
| ret_20d    |  +2.1% |
| ret_60d    | +16.4% |
| ma20_dist  |  +0.9% |
| ma50_dist  |  +5.2% |
| vol_20d    |  26.1% |
| mdd_60d    |   6.1% |
| rsi_14     |   51.9 |
| zscore_20d |    0.8 |

### Soybeans / ZS=F (score 58.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | -0.6% |
| ret_20d    | +9.3% |
| ret_60d    | +2.5% |
| ma20_dist  | +1.3% |
| ma50_dist  | +3.8% |
| vol_20d    | 22.3% |
| mdd_60d    |  8.8% |
| rsi_14     |  55.2 |
| zscore_20d |   0.5 |

### Euro Stoxx 50 / ^STOXX50E (score 57.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | +0.1% |
| ret_20d    | -0.6% |
| ret_60d    | +6.9% |
| ma20_dist  | +0.0% |
| ma50_dist  | +1.5% |
| vol_20d    | 13.9% |
| mdd_60d    |  3.6% |
| rsi_14     |  59.0 |
| zscore_20d |   0.0 |

### Russell 2000 / ^RUT (score 49.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | -1.1% |
| ret_20d    | -1.9% |
| ret_60d    | +5.5% |
| ma20_dist  | -0.6% |
| ma50_dist  | +0.7% |
| vol_20d    | 11.1% |
| mdd_60d    |  4.8% |
| rsi_14     |  49.5 |
| zscore_20d |  -0.7 |

### Microsoft Corporation / MSFT (score 48.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | -1.1% |
| ret_20d    | +6.7% |
| ret_60d    | -3.3% |
| ma20_dist  | +1.1% |
| ma50_dist  | -1.3% |
| vol_20d    | 25.4% |
| mdd_60d    | 23.4% |
| rsi_14     |  56.4 |
| zscore_20d |   0.6 |

### S&P 500 / ^GSPC (score 47.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | -1.1% |
| ret_20d    | -0.2% |
| ret_60d    | +3.0% |
| ma20_dist  | -0.8% |
| ma50_dist  | -0.6% |
| vol_20d    |  9.3% |
| mdd_60d    |  4.5% |
| rsi_14     |  44.9 |
| zscore_20d |  -1.3 |

### Gold / GC=F (score 36.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.9% |
| ret_5d     |  -0.9% |
| ret_20d    |  +0.3% |
| ret_60d    | -12.5% |
| ma20_dist  |  -0.8% |
| ma50_dist  |  -4.6% |
| vol_20d    |  20.8% |
| mdd_60d    |  15.6% |
| rsi_14     |   47.4 |
| zscore_20d |   -0.6 |

### Platinum / PL=F (score 33.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.5% |
| ret_5d     |  -0.9% |
| ret_20d    |  +2.4% |
| ret_60d    | -18.5% |
| ma20_dist  |  -0.0% |
| ma50_dist  |  -6.7% |
| vol_20d    |  28.8% |
| mdd_60d    |  29.1% |
| rsi_14     |   56.6 |
| zscore_20d |   -0.0 |

### Meta Platforms Inc. / META (score 30.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | -7.8% |
| ret_20d    | +5.5% |
| ret_60d    | -2.9% |
| ma20_dist  | -5.0% |
| ma50_dist  | -1.9% |
| vol_20d    | 53.3% |
| mdd_60d    | 14.5% |
| rsi_14     |  47.5 |
| zscore_20d |  -1.0 |

### Brent Crude Oil / BZ=F (score 29.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -4.8% |
| ret_5d     |  -7.6% |
| ret_20d    | +15.0% |
| ret_60d    | -26.2% |
| ma20_dist  |  +1.2% |
| ma50_dist  |  -4.2% |
| vol_20d    |  64.5% |
| mdd_60d    |  37.5% |
| rsi_14     |   56.8 |
| zscore_20d |    0.1 |

### NASDAQ 100 / ^NDX (score 29.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | -4.8% |
| ret_20d    | -6.8% |
| ret_60d    | +1.1% |
| ma20_dist  | -4.6% |
| ma50_dist  | -5.8% |
| vol_20d    | 20.3% |
| mdd_60d    |  9.5% |
| rsi_14     |  33.1 |
| zscore_20d |  -2.1 |

### NVIDIA Corporation / NVDA (score 27.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | -5.0% |
| ret_20d    | +1.0% |
| ret_60d    | -1.3% |
| ma20_dist  | -3.3% |
| ma50_dist  | -5.2% |
| vol_20d    | 38.6% |
| mdd_60d    | 18.3% |
| rsi_14     |  44.2 |
| zscore_20d |  -1.1 |

### Alphabet Inc. Class A / GOOGL (score 24.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.2% |
| ret_5d     |  -3.9% |
| ret_20d    |  -5.6% |
| ret_60d    | -13.2% |
| ma20_dist  |  -4.8% |
| ma50_dist  |  -7.8% |
| vol_20d    |  37.9% |
| mdd_60d    |  21.0% |
| rsi_14     |   36.9 |
| zscore_20d |   -1.1 |

### Amazon.com Inc. / AMZN (score 21.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.2% |
| ret_5d     |  -6.7% |
| ret_20d    |  -3.9% |
| ret_60d    | -12.9% |
| ma20_dist  |  -5.1% |
| ma50_dist  |  -6.8% |
| vol_20d    |  24.1% |
| mdd_60d    |  17.4% |
| rsi_14     |   35.6 |
| zscore_20d |   -1.9 |

### Silver / SI=F (score 18.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.0% |
| ret_5d     |  -2.6% |
| ret_20d    |  -1.5% |
| ret_60d    | -22.1% |
| ma20_dist  |  -2.5% |
| ma50_dist  | -12.4% |
| vol_20d    |  38.6% |
| mdd_60d    |  37.1% |
| rsi_14     |   47.5 |
| zscore_20d |   -0.9 |

### Natural Gas / NG=F (score 11.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -3.8% |
| ret_5d     |  -7.1% |
| ret_20d    | -16.3% |
| ret_60d    |  -3.8% |
| ma20_dist  | -10.9% |
| ma50_dist  | -13.7% |
| vol_20d    |  34.7% |
| mdd_60d    |  20.4% |
| rsi_14     |   17.3 |
| zscore_20d |   -1.8 |

### Tesla Inc. / TSLA (score 6.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.6% |
| ret_5d     | -18.9% |
| ret_20d    | -25.3% |
| ret_60d    | -19.4% |
| ma20_dist  | -19.1% |
| ma50_dist  | -22.6% |
| vol_20d    |  66.7% |
| mdd_60d    |  31.0% |
| rsi_14     |   18.1 |
| zscore_20d |   -2.0 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Apple Inc. / AAPL                   |   7.9014 |           2.3% |                 0.36x |       15.8029 |            4.6% |
| JPMorgan Chase & Co. / JPM          |   7.4379 |           2.1% |                 0.53x |       14.8757 |            4.2% |
| FTSE 100 / ^FTSE                    | 110.4645 |           1.0% |                 0.88x |      220.9290 |            2.0% |
| CAC 40 / ^FCHI                      |  90.7829 |           1.1% |                 0.74x |      181.5657 |            2.1% |
| Corn / ZC=F                         |  10.3750 |           2.3% |                 0.37x |       20.7500 |            4.5% |
| Dow Jones Industrial Average / ^DJI | 534.1401 |           1.0% |                 1.07x |     1068.2801 |            2.0% |
| DAX / ^GDAXI                        | 296.4149 |           1.2% |                 0.63x |      592.8298 |            2.3% |
| Hang Seng / ^HSI                    | 449.0771 |           1.8% |                 0.54x |      898.1543 |            3.5% |
| Wheat / ZW=F                        |  23.5536 |           3.6% |                 0.27x |       47.1071 |            7.1% |
| UnitedHealth Group Inc. / UNH       |  13.4829 |           3.1% |                 0.38x |       26.9657 |            6.3% |
| Soybeans / ZS=F                     |  18.6786 |           1.5% |                 0.45x |       37.3571 |            3.1% |
| Euro Stoxx 50 / ^STOXX50E           |  69.7599 |           1.1% |                 0.72x |      139.5199 |            2.2% |
| Russell 2000 / ^RUT                 |  34.9335 |           1.2% |                 0.90x |       69.8671 |            2.4% |
| Microsoft Corporation / MSFT        |  11.6614 |           3.0% |                 0.39x |       23.3229 |            5.9% |
| S&P 500 / ^GSPC                     |  72.4828 |           1.0% |                 1.08x |      144.9657 |            2.0% |
| Gold / GC=F                         |  63.1286 |           1.6% |                 0.48x |      126.2571 |            3.1% |
| Platinum / PL=F                     |  22.9857 |           1.4% |                 0.35x |       45.9714 |            2.9% |
| Meta Platforms Inc. / META          |  26.0521 |           4.4% |                 0.19x |       52.1043 |            8.8% |
| Brent Crude Oil / BZ=F              |   5.1129 |           6.1% |                 0.16x |       10.2257 |           12.2% |
| NASDAQ 100 / ^NDX                   | 543.7998 |           2.0% |                 0.49x |     1087.5996 |            3.9% |
| NVIDIA Corporation / NVDA           |   7.7343 |           3.9% |                 0.26x |       15.4686 |            7.9% |
| Alphabet Inc. Class A / GOOGL       |  11.9050 |           3.6% |                 0.26x |       23.8100 |            7.1% |
| Amazon.com Inc. / AMZN              |   6.6693 |           2.9% |                 0.42x |       13.3386 |            5.8% |
| Silver / SI=F                       |   1.5181 |           2.6% |                 0.26x |        3.0361 |            5.3% |
| Natural Gas / NG=F                  |   0.1125 |           4.2% |                 0.29x |        0.2250 |            8.5% |
| Tesla Inc. / TSLA                   |  16.2729 |           5.3% |                 0.15x |       32.5457 |           10.6% |

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

Scoring engine version: **1.0.0** | Git commit: **85db1ab**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
