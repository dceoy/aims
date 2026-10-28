+++
title = "Market Analysis 2026-10-28"
date = "2026-10-28T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: AAPL (score 81.8)."
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
source_files = ["data/analysis/2026-10-28.json", "data/history/2026-10-28.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "d19ca3f"
+++

## Market Regime

**Neutral** — 11 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Apple Inc. / AAPL** — score 81.8, 20d return +5.4%, RSI14=64. 20d up +5.4%; above MA20 by 2.1%; RSI14=64 ⚠️ Upcoming: AAPL earnings release (2026-11-02)
- **Tesla Inc. / TSLA** — score 81.8, 20d return +15.5%, RSI14=62. 20d up +15.5%; above MA20 by 8.9%; RSI14=62
- **Brent Crude Oil / BZ=F** — score 75.8, 20d return +11.0%, RSI14=79. 20d up +11.0%; above MA20 by 6.5%; RSI14=79
- **DAX / ^GDAXI** — score 68.8, 20d return +0.8%, RSI14=59. 20d up +0.8%; above MA20 by 1.2%; RSI14=59 ⚠️ Upcoming: ECB monetary policy decision (2026-10-29)
- **Dow Jones Industrial Average / ^DJI** — score 67.0, 20d return +2.0%, RSI14=68. 20d up +2.0%; above MA20 by 1.1%; RSI14=68

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                        | Applies To                    |
| ---------- | ---------------------------- | ----------------------------- |
| 2026-10-29 | AMZN earnings release        | AMZN                          |
| 2026-10-29 | ECB monetary policy decision | ^FCHI, ^GDAXI, ^STOXX50E      |
| 2026-10-30 | BOJ monetary policy decision | 6758.T, 7203.T, 8306.T, ^N225 |
| 2026-10-30 | XOM earnings release         | XOM                           |
| 2026-11-02 | AAPL earnings release        | AAPL                          |

## Signal History

Compared with the previous available report (**2026-10-27**).

- **New top-5:** AAPL, ^GDAXI
- **Persistent top signals:** BZ=F (8 reports), ^DJI (6 reports), TSLA (2 reports)
- **Dropped from top-5:** MSFT, ^FTSE

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +1 |    -4.8 |
| 7203.T    |     +0 |    -3.9 |
| 8306.T    |     +1 |   +12.4 |
| AAPL      |     +5 |   +11.5 |
| AMZN      |     +1 |    +3.3 |
| BZ=F      |     -1 |    -2.1 |
| CL=F      |     -1 |    -3.0 |
| GC=F      |     +0 |    -0.3 |
| GOOGL     |     +3 |    +8.5 |
| HG=F      |     +1 |   +11.5 |
| JPM       |     +0 |    -0.9 |
| META      |     -2 |    -3.0 |
| MSFT      |     -3 |   -10.9 |
| NG=F      |     +0 |   +13.0 |
| NVDA      |     +0 |    -1.2 |
| PL=F      |     +3 |    +2.4 |
| SI=F      |     -3 |    -2.7 |
| TSLA      |     -1 |    +3.6 |
| UNH       |     +0 |    -1.2 |
| XOM       |     -1 |   -12.4 |
| ZC=F      |     -1 |    -6.4 |
| ZS=F      |     -1 |    -5.5 |
| ZW=F      |     +1 |    -1.2 |
| ^DJI      |     -2 |    -5.5 |
| ^FCHI     |     -2 |    -1.5 |
| ^FTSE     |     -6 |   -13.6 |
| ^GDAXI    |     +3 |    +1.5 |
| ^GSPC     |     +2 |    -1.2 |
| ^HSI      |     -1 |    -8.2 |
| ^N225     |     -1 |   +10.0 |
| ^NDX      |     +2 |    +4.2 |
| ^RUT      |     +3 |    +6.7 |
| ^STOXX50E |     +0 |    +0.9 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Nikkei 225 / ^N225** — missing_bars
- **Natural Gas / NG=F** — malformed_input

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|    3 | Brent Crude Oil / BZ=F |  75.8 |   Yes    | —               | 20d up +11.0%; above MA20 by 6.5%; RSI14=79   |
|   17 | Soybeans / ZS=F        |  39.1 |   Yes    | —               | 20d down -5.3%; below MA20 by 3.3%; RSI14=16  |
|   18 | Gold / GC=F            |  37.9 |   Yes    | —               | 20d down -2.5%; below MA20 by 1.7%; RSI14=44  |
|   21 | Corn / ZC=F            |  20.0 |   Yes    | —               | 20d down -14.0%; below MA20 by 6.5%; RSI14=7  |
|   22 | Platinum / PL=F        |  17.6 |   Yes    | —               | 20d down -8.6%; below MA20 by 6.1%; RSI14=33  |
|   23 | Wheat / ZW=F           |  14.8 |   Yes    | —               | 20d down -11.9%; below MA20 by 7.7%; RSI14=6  |
|   24 | Silver / SI=F          |  14.6 |   Yes    | —               | 20d down -10.5%; below MA20 by 6.4%; RSI14=30 |
|   29 | Copper / HG=F          |  66.4 |    No    | malformed_input | Suppressed: malformed_input                   |
|   30 | WTI Crude Oil / CL=F   |  56.4 |    No    | malformed_input | Suppressed: malformed_input                   |
|   33 | Natural Gas / NG=F     |  22.4 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                    |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | ---------------------------------------------- |
|    1 | Apple Inc. / AAPL                                                              |  81.8 |   Yes    | —                             | 20d up +5.4%; above MA20 by 2.1%; RSI14=64     |
|    2 | Tesla Inc. / TSLA                                                              |  81.8 |   Yes    | —                             | 20d up +15.5%; above MA20 by 8.9%; RSI14=62    |
|    7 | Microsoft Corporation / MSFT                                                   |  61.2 |   Yes    | —                             | 20d up +4.4%; above MA20 by 0.4%; RSI14=51     |
|    9 | UnitedHealth Group Inc. / UNH                                                  |  59.1 |   Yes    | —                             | 20d up +9.5%; above MA20 by 4.5%; RSI14=69     |
|   10 | JPMorgan Chase & Co. / JPM                                                     |  58.2 |   Yes    | —                             | 20d up +0.7%; above MA20 by 0.8%; RSI14=59     |
|   15 | NVIDIA Corporation / NVDA                                                      |  44.2 |   Yes    | —                             | 20d down -4.1%; below MA20 by 2.9%; RSI14=32   |
|   16 | Amazon.com Inc. / AMZN                                                         |  42.7 |   Yes    | —                             | 20d up +2.6%; below MA20 by 0.7%; RSI14=44     |
|   19 | Alphabet Inc. Class A / GOOGL                                                  |  25.1 |   Yes    | —                             | 20d down -6.0%; below MA20 by 5.9%; RSI14=25   |
|   25 | Meta Platforms Inc. / META                                                     |  13.0 |   Yes    | —                             | 20d down -16.1%; below MA20 by 12.3%; RSI14=24 |
|   26 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  75.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   27 | Exxon Mobil Corporation / XOM                                                  |  73.0 |    No    | malformed_input               | Suppressed: malformed_input                    |
|   28 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  66.7 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   31 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  37.0 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    4 | DAX / ^GDAXI                        |  68.8 |   Yes    | —            | 20d up +0.8%; above MA20 by 1.2%; RSI14=59   |
|    5 | Dow Jones Industrial Average / ^DJI |  67.0 |   Yes    | —            | 20d up +2.0%; above MA20 by 1.1%; RSI14=68   |
|    6 | S&P 500 / ^GSPC                     |  62.4 |   Yes    | —            | 20d up +0.7%; below MA20 by 0.1%; RSI14=44   |
|    8 | Russell 2000 / ^RUT                 |  60.3 |   Yes    | —            | 20d up +0.4%; above MA20 by 1.1%; RSI14=54   |
|   11 | FTSE 100 / ^FTSE                    |  57.9 |   Yes    | —            | 20d up +0.5%; above MA20 by 0.4%; RSI14=63   |
|   12 | NASDAQ 100 / ^NDX                   |  54.2 |   Yes    | —            | 20d down -2.3%; below MA20 by 1.6%; RSI14=33 |
|   13 | Euro Stoxx 50 / ^STOXX50E           |  52.7 |   Yes    | —            | 20d down -2.5%; below MA20 by 0.2%; RSI14=49 |
|   14 | CAC 40 / ^FCHI                      |  51.5 |   Yes    | —            | 20d down -1.9%; above MA20 by 0.4%; RSI14=58 |
|   20 | Hang Seng / ^HSI                    |  25.1 |   Yes    | —            | 20d down -6.0%; below MA20 by 3.8%; RSI14=30 |
|   32 | Nikkei 225 / ^N225                  |  36.1 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-10-27 |
| 7203.T    | 2026-10-27 |
| 8306.T    | 2026-10-27 |
| AAPL      | 2026-10-27 |
| AMZN      | 2026-10-27 |
| BZ=F      | 2026-10-27 |
| CL=F      | 2026-10-27 |
| GC=F      | 2026-10-27 |
| GOOGL     | 2026-10-27 |
| HG=F      | 2026-10-27 |
| JPM       | 2026-10-27 |
| META      | 2026-10-27 |
| MSFT      | 2026-10-27 |
| NG=F      | 2026-10-27 |
| NVDA      | 2026-10-27 |
| PL=F      | 2026-10-27 |
| SI=F      | 2026-10-27 |
| TSLA      | 2026-10-27 |
| UNH       | 2026-10-27 |
| XOM       | 2026-10-27 |
| ZC=F      | 2026-10-27 |
| ZS=F      | 2026-10-27 |
| ZW=F      | 2026-10-27 |
| ^DJI      | 2026-10-27 |
| ^FCHI     | 2026-10-27 |
| ^FTSE     | 2026-10-27 |
| ^GDAXI    | 2026-10-27 |
| ^GSPC     | 2026-10-27 |
| ^HSI      | 2026-10-27 |
| ^N225     | 2026-10-27 |
| ^NDX      | 2026-10-27 |
| ^RUT      | 2026-10-27 |
| ^STOXX50E | 2026-10-27 |

## Symbol Details

### Apple Inc. / AAPL (score 81.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.9% |
| ret_5d     |  +2.2% |
| ret_20d    |  +5.4% |
| ret_60d    | +14.5% |
| ma20_dist  |  +2.1% |
| ma50_dist  |  +4.8% |
| vol_20d    |  13.0% |
| mdd_60d    |   3.9% |
| rsi_14     |   64.3 |
| zscore_20d |    1.4 |

### Tesla Inc. / TSLA (score 81.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +4.0% |
| ret_5d     |  +9.0% |
| ret_20d    | +15.5% |
| ret_60d    | +26.5% |
| ma20_dist  |  +8.9% |
| ma50_dist  | +11.3% |
| vol_20d    |  38.2% |
| mdd_60d    |   7.3% |
| rsi_14     |   62.4 |
| zscore_20d |    2.7 |

### Brent Crude Oil / BZ=F (score 75.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.7% |
| ret_5d     |  +4.7% |
| ret_20d    | +11.0% |
| ret_60d    | +36.3% |
| ma20_dist  |  +6.5% |
| ma50_dist  | +11.7% |
| vol_20d    |  28.6% |
| mdd_60d    |   8.7% |
| rsi_14     |   78.9 |
| zscore_20d |    1.4 |

### DAX / ^GDAXI (score 68.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | +1.1% |
| ret_20d    | +0.8% |
| ret_60d    | -2.3% |
| ma20_dist  | +1.2% |
| ma50_dist  | -0.0% |
| vol_20d    | 14.2% |
| mdd_60d    |  6.6% |
| rsi_14     |  59.1 |
| zscore_20d |   1.5 |

### Dow Jones Industrial Average / ^DJI (score 67.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.0% |
| ret_5d     | -0.2% |
| ret_20d    | +2.0% |
| ret_60d    | -1.5% |
| ma20_dist  | +1.1% |
| ma50_dist  | +0.2% |
| vol_20d    |  9.3% |
| mdd_60d    |  6.3% |
| rsi_14     |  67.7 |
| zscore_20d |   1.0 |

### S&P 500 / ^GSPC (score 62.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | +0.1% |
| ret_20d    | +0.7% |
| ret_60d    | +1.6% |
| ma20_dist  | -0.1% |
| ma50_dist  | +0.3% |
| vol_20d    |  9.8% |
| mdd_60d    |  3.2% |
| rsi_14     |  43.6 |
| zscore_20d |  -0.1 |

### Microsoft Corporation / MSFT (score 61.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | -0.1% |
| ret_20d    | +4.4% |
| ret_60d    | +9.2% |
| ma20_dist  | +0.4% |
| ma50_dist  | +4.2% |
| vol_20d    | 19.1% |
| mdd_60d    |  5.1% |
| rsi_14     |  50.9 |
| zscore_20d |   0.3 |

### Russell 2000 / ^RUT (score 60.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.2% |
| ret_5d     | +1.6% |
| ret_20d    | +0.4% |
| ret_60d    | -5.5% |
| ma20_dist  | +1.1% |
| ma50_dist  | -1.8% |
| vol_20d    | 14.6% |
| mdd_60d    | 11.3% |
| rsi_14     |  54.4 |
| zscore_20d |   1.0 |

### UnitedHealth Group Inc. / UNH (score 59.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | -2.1% |
| ret_20d    | +9.5% |
| ret_60d    | -1.2% |
| ma20_dist  | +4.5% |
| ma50_dist  | +5.7% |
| vol_20d    | 29.0% |
| mdd_60d    | 11.5% |
| rsi_14     |  68.8 |
| zscore_20d |   0.9 |

### JPMorgan Chase & Co. / JPM (score 58.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | +0.2% |
| ret_20d    | +0.7% |
| ret_60d    | -4.8% |
| ma20_dist  | +0.8% |
| ma50_dist  | -2.3% |
| vol_20d    | 13.0% |
| mdd_60d    |  9.9% |
| rsi_14     |  59.0 |
| zscore_20d |   1.0 |

### FTSE 100 / ^FTSE (score 57.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | -0.4% |
| ret_20d    | +0.5% |
| ret_60d    | -1.6% |
| ma20_dist  | +0.4% |
| ma50_dist  | -0.2% |
| vol_20d    | 11.4% |
| mdd_60d    |  4.3% |
| rsi_14     |  63.3 |
| zscore_20d |   0.3 |

### NASDAQ 100 / ^NDX (score 54.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.3% |
| ret_5d     | +0.5% |
| ret_20d    | -2.3% |
| ret_60d    | +3.0% |
| ma20_dist  | -1.6% |
| ma50_dist  | -0.5% |
| vol_20d    | 19.1% |
| mdd_60d    |  7.3% |
| rsi_14     |  33.5 |
| zscore_20d |  -0.7 |

### Euro Stoxx 50 / ^STOXX50E (score 52.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.8% |
| ret_5d     | +0.7% |
| ret_20d    | -2.5% |
| ret_60d    | -5.0% |
| ma20_dist  | -0.2% |
| ma50_dist  | -1.9% |
| vol_20d    | 14.5% |
| mdd_60d    |  7.4% |
| rsi_14     |  48.8 |
| zscore_20d |  -0.2 |

### CAC 40 / ^FCHI (score 51.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | +0.6% |
| ret_20d    | -1.9% |
| ret_60d    | -9.0% |
| ma20_dist  | +0.4% |
| ma50_dist  | -2.5% |
| vol_20d    | 13.3% |
| mdd_60d    | 11.4% |
| rsi_14     |  58.2 |
| zscore_20d |   0.6 |

### NVIDIA Corporation / NVDA (score 44.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | +0.7% |
| ret_20d    | -4.1% |
| ret_60d    | +5.5% |
| ma20_dist  | -2.9% |
| ma50_dist  | -1.9% |
| vol_20d    | 29.5% |
| mdd_60d    | 11.8% |
| rsi_14     |  32.2 |
| zscore_20d |  -0.7 |

### Amazon.com Inc. / AMZN (score 42.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.6% |
| ret_5d     |  -3.6% |
| ret_20d    |  +2.6% |
| ret_60d    | -10.9% |
| ma20_dist  |  -0.7% |
| ma50_dist  |  -0.8% |
| vol_20d    |  32.0% |
| mdd_60d    |  11.6% |
| rsi_14     |   44.4 |
| zscore_20d |   -0.4 |

### Soybeans / ZS=F (score 39.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | -1.5% |
| ret_20d    | -5.3% |
| ret_60d    | +6.2% |
| ma20_dist  | -3.3% |
| ma50_dist  | -3.9% |
| vol_20d    | 10.4% |
| mdd_60d    |  7.4% |
| rsi_14     |  15.8 |
| zscore_20d |  -2.0 |

### Gold / GC=F (score 37.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | -1.6% |
| ret_20d    | -2.5% |
| ret_60d    | -6.1% |
| ma20_dist  | -1.7% |
| ma50_dist  | -5.9% |
| vol_20d    | 15.3% |
| mdd_60d    | 14.8% |
| rsi_14     |  43.5 |
| zscore_20d |  -1.2 |

### Alphabet Inc. Class A / GOOGL (score 25.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.2% |
| ret_5d     |  -5.8% |
| ret_20d    |  -6.0% |
| ret_60d    | -14.2% |
| ma20_dist  |  -5.9% |
| ma50_dist  |  -6.2% |
| vol_20d    |  21.2% |
| mdd_60d    |  16.1% |
| rsi_14     |   24.6 |
| zscore_20d |   -1.8 |

### Hang Seng / ^HSI (score 25.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.7% |
| ret_5d     |  -3.5% |
| ret_20d    |  -6.0% |
| ret_60d    | -11.0% |
| ma20_dist  |  -3.8% |
| ma50_dist  |  -6.8% |
| vol_20d    |  18.4% |
| mdd_60d    |  11.8% |
| rsi_14     |   30.4 |
| zscore_20d |   -1.8 |

### Corn / ZC=F (score 20.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.4% |
| ret_5d     |  -2.9% |
| ret_20d    | -14.0% |
| ret_60d    |  +2.2% |
| ma20_dist  |  -6.5% |
| ma50_dist  | -10.5% |
| vol_20d    |  21.8% |
| mdd_60d    |  17.4% |
| rsi_14     |    7.2 |
| zscore_20d |   -1.7 |

### Platinum / PL=F (score 17.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.1% |
| ret_5d     |  -6.8% |
| ret_20d    |  -8.6% |
| ret_60d    | -12.3% |
| ma20_dist  |  -6.1% |
| ma50_dist  | -11.7% |
| vol_20d    |  26.9% |
| mdd_60d    |  19.8% |
| rsi_14     |   33.4 |
| zscore_20d |   -1.9 |

### Wheat / ZW=F (score 14.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.9% |
| ret_5d     |  -5.1% |
| ret_20d    | -11.9% |
| ret_60d    |  -3.3% |
| ma20_dist  |  -7.7% |
| ma50_dist  | -12.2% |
| vol_20d    |  19.3% |
| mdd_60d    |  20.4% |
| rsi_14     |    6.3 |
| zscore_20d |   -1.9 |

### Silver / SI=F (score 14.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.3% |
| ret_5d     |  -5.9% |
| ret_20d    | -10.5% |
| ret_60d    | -14.3% |
| ma20_dist  |  -6.4% |
| ma50_dist  | -13.4% |
| vol_20d    |  33.2% |
| mdd_60d    |  22.7% |
| rsi_14     |   30.4 |
| zscore_20d |   -1.5 |

### Meta Platforms Inc. / META (score 13.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.6% |
| ret_5d     | -10.7% |
| ret_20d    | -16.1% |
| ret_60d    |  +5.1% |
| ma20_dist  | -12.3% |
| ma50_dist  |  -6.8% |
| vol_20d    |  35.6% |
| mdd_60d    |  20.2% |
| rsi_14     |   24.1 |
| zscore_20d |   -2.2 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Apple Inc. / AAPL                   |   6.3593 |           1.8% |                 0.77x |       12.7186 |            3.7% |
| Tesla Inc. / TSLA                   |  13.7836 |           3.4% |                 0.26x |       27.5671 |            6.8% |
| Brent Crude Oil / BZ=F              |   3.9686 |           3.5% |                 0.35x |        7.9371 |            7.0% |
| DAX / ^GDAXI                        | 318.9669 |           1.2% |                 0.70x |      637.9339 |            2.5% |
| Dow Jones Industrial Average / ^DJI | 507.9235 |           1.0% |                 1.08x |     1015.8471 |            1.9% |
| S&P 500 / ^GSPC                     |  73.0336 |           0.9% |                 1.02x |      146.0672 |            1.9% |
| Microsoft Corporation / MSFT        |  11.0679 |           2.1% |                 0.52x |       22.1357 |            4.2% |
| Russell 2000 / ^RUT                 |  33.3543 |           1.2% |                 0.69x |       66.7085 |            2.4% |
| UnitedHealth Group Inc. / UNH       |  13.0629 |           3.2% |                 0.34x |       26.1257 |            6.4% |
| JPMorgan Chase & Co. / JPM          |   6.3079 |           1.9% |                 0.77x |       12.6157 |            3.8% |
| FTSE 100 / ^FTSE                    | 113.4643 |           1.1% |                 0.88x |      226.9286 |            2.1% |
| NASDAQ 100 / ^NDX                   | 519.0904 |           1.8% |                 0.52x |     1038.1808 |            3.5% |
| Euro Stoxx 50 / ^STOXX50E           |  75.6536 |           1.2% |                 0.69x |      151.3073 |            2.5% |
| CAC 40 / ^FCHI                      |  88.2386 |           1.1% |                 0.75x |      176.4773 |            2.2% |
| NVIDIA Corporation / NVDA           |   6.2007 |           2.8% |                 0.34x |       12.4014 |            5.7% |
| Amazon.com Inc. / AMZN              |   6.8679 |           2.7% |                 0.31x |       13.7357 |            5.4% |
| Soybeans / ZS=F                     |  18.0179 |           1.5% |                 0.96x |       36.0357 |            2.9% |
| Gold / GC=F                         |  67.7928 |           1.7% |                 0.65x |      135.5856 |            3.3% |
| Alphabet Inc. Class A / GOOGL       |   8.3750 |           2.6% |                 0.47x |       16.7500 |            5.2% |
| Hang Seng / ^HSI                    | 387.3331 |           1.7% |                 0.54x |      774.6663 |            3.4% |
| Corn / ZC=F                         |   9.4286 |           2.1% |                 0.46x |       18.8571 |            4.2% |
| Platinum / PL=F                     |  26.9143 |           1.8% |                 0.37x |       53.8286 |            3.5% |
| Wheat / ZW=F                        |  14.2857 |           2.3% |                 0.52x |       28.5714 |            4.7% |
| Silver / SI=F                       |   1.1520 |           2.1% |                 0.30x |        2.3040 |            4.2% |
| Meta Platforms Inc. / META          |  25.3979 |           4.1% |                 0.28x |       50.7957 |            8.2% |

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

Scoring engine version: **1.0.0** | Git commit: **d19ca3f**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
