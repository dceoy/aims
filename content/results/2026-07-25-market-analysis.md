+++
title = "Market Analysis 2026-07-25"
date = "2026-07-25T00:00:00+00:00"
draft = false
summary = "Bearish market: 26 reliable instruments. Top signal: JPM (score 79.1)."
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
source_files = ["data/analysis/2026-07-25.json", "data/history/2026-07-25.json"]
market_regime = "Bearish"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "0bc26f0"
+++

## Market Regime

**Bearish** — 9 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **JPMorgan Chase & Co. / JPM** — score 79.1, 20d return +5.9%, RSI14=65. 20d up +5.9%; above MA20 by 4.3%; RSI14=65 ⚠️ Upcoming: FOMC rate decision (2026-07-29)
- **Soybeans / ZS=F** — score 77.0, 20d return +10.7%, RSI14=74. 20d up +10.7%; above MA20 by 5.2%; RSI14=74 ⚠️ Upcoming: FOMC rate decision (2026-07-29)
- **Apple Inc. / AAPL** — score 74.2, 20d return +21.0%, RSI14=68. 20d up +21.0%; above MA20 by 5.9%; RSI14=68 ⚠️ Upcoming: FOMC rate decision (2026-07-29); AAPL earnings release (2026-07-30)
- **FTSE 100 / ^FTSE** — score 71.8, 20d return +2.2%, RSI14=55. 20d up +2.2%; above MA20 by 1.5%; RSI14=55 ⚠️ Upcoming: FOMC rate decision (2026-07-29)
- **Corn / ZC=F** — score 65.8, 20d return +11.9%, RSI14=66. 20d up +11.9%; above MA20 by 6.1%; RSI14=66 ⚠️ Upcoming: FOMC rate decision (2026-07-29)

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                        | Applies To                      |
| ---------- | ---------------------------- | ------------------------------- |
| 2026-07-29 | FOMC rate decision           | Commodity, Equity, Equity Index |
| 2026-07-29 | META earnings release        | META                            |
| 2026-07-29 | MSFT earnings release        | MSFT                            |
| 2026-07-30 | AAPL earnings release        | AAPL                            |
| 2026-07-30 | AMZN earnings release        | AMZN                            |
| 2026-07-31 | 6758.T earnings release      | 6758.T                          |
| 2026-07-31 | BOJ monetary policy decision | 6758.T, 7203.T, 8306.T, ^N225   |
| 2026-07-31 | XOM earnings release         | XOM                             |

## Signal History

Compared with the previous available report (**2026-07-24**).

- **New top-5:** AAPL, ^FTSE
- **Persistent top signals:** ZS=F (9 reports), JPM (4 reports), ZC=F (3 reports)
- **Dropped from top-5:** BZ=F, ZW=F

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     -1 |   -11.2 |
| 7203.T    |     -1 |   -14.2 |
| 8306.T    |     +0 |    -1.5 |
| AAPL      |     +5 |   +17.3 |
| AMZN      |     +0 |    +5.5 |
| BZ=F      |     -4 |   -13.3 |
| CL=F      |     -1 |   -12.1 |
| GC=F      |     +1 |    +5.2 |
| GOOGL     |     +0 |    +7.9 |
| HG=F      |     +3 |    +8.5 |
| JPM       |     +0 |    +3.6 |
| META      |     +0 |    -3.0 |
| MSFT      |     +1 |    +2.7 |
| NG=F      |     -5 |   -11.2 |
| NVDA      |     -3 |    +0.0 |
| PL=F      |     +0 |    -1.5 |
| SI=F      |     +5 |   +11.8 |
| TSLA      |     +0 |    +0.6 |
| UNH       |     -4 |    -6.4 |
| XOM       |     +0 |    -4.2 |
| ZC=F      |     +0 |    -3.3 |
| ZS=F      |     +0 |    +2.1 |
| ZW=F      |     -6 |   -13.9 |
| ^DJI      |     -2 |    +3.9 |
| ^FCHI     |     +4 |   +11.2 |
| ^FTSE     |     +3 |   +10.3 |
| ^GDAXI    |     +6 |   +16.1 |
| ^GSPC     |     -3 |    -0.3 |
| ^HSI      |     -1 |    -7.0 |
| ^N225     |     +0 |   -12.1 |
| ^NDX      |     -1 |    -2.7 |
| ^RUT      |     -3 |    -3.0 |
| ^STOXX50E |     +7 |   +14.8 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Copper / HG=F** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Nikkei 225 / ^N225** — missing_bars

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|    2 | Soybeans / ZS=F        |  77.0 |   Yes    | —               | 20d up +10.7%; above MA20 by 5.2%; RSI14=74   |
|    5 | Corn / ZC=F            |  65.8 |   Yes    | —               | 20d up +11.9%; above MA20 by 6.1%; RSI14=66   |
|    8 | Brent Crude Oil / BZ=F |  57.9 |   Yes    | —               | 20d up +28.6%; above MA20 by 18.4%; RSI14=83  |
|    9 | Wheat / ZW=F           |  57.6 |   Yes    | —               | 20d up +14.7%; above MA20 by 6.8%; RSI14=70   |
|   16 | Gold / GC=F            |  45.1 |   Yes    | —               | 20d up +0.9%; below MA20 by 0.0%; RSI14=44    |
|   18 | Silver / SI=F          |  35.5 |   Yes    | —               | 20d up +0.5%; below MA20 by 0.3%; RSI14=42    |
|   22 | Platinum / PL=F        |  26.1 |   Yes    | —               | 20d down -0.5%; below MA20 by 1.1%; RSI14=44  |
|   23 | Natural Gas / NG=F     |  25.4 |   Yes    | —               | 20d down -14.1%; below MA20 by 5.4%; RSI14=23 |
|   29 | Copper / HG=F          |  60.9 |    No    | malformed_input | Suppressed: malformed_input                   |
|   30 | WTI Crude Oil / CL=F   |  57.9 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                    |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | ---------------------------------------------- |
|    1 | JPMorgan Chase & Co. / JPM                                                     |  79.1 |   Yes    | —                             | 20d up +5.9%; above MA20 by 4.3%; RSI14=65     |
|    3 | Apple Inc. / AAPL                                                              |  74.2 |   Yes    | —                             | 20d up +21.0%; above MA20 by 5.9%; RSI14=68    |
|   13 | UnitedHealth Group Inc. / UNH                                                  |  50.0 |   Yes    | —                             | 20d up +1.3%; below MA20 by 1.0%; RSI14=52     |
|   14 | NVIDIA Corporation / NVDA                                                      |  47.3 |   Yes    | —                             | 20d up +5.7%; above MA20 by 1.7%; RSI14=60     |
|   19 | Microsoft Corporation / MSFT                                                   |  33.3 |   Yes    | —                             | 20d up +8.2%; below MA20 by 1.3%; RSI14=47     |
|   21 | Meta Platforms Inc. / META                                                     |  26.4 |   Yes    | —                             | 20d up +9.6%; below MA20 by 4.2%; RSI14=49     |
|   24 | Amazon.com Inc. / AMZN                                                         |  25.1 |   Yes    | —                             | 20d up +2.2%; below MA20 by 4.8%; RSI14=37     |
|   25 | Alphabet Inc. Class A / GOOGL                                                  |  16.7 |   Yes    | —                             | 20d down -7.0%; below MA20 by 9.2%; RSI14=26   |
|   26 | Tesla Inc. / TSLA                                                              |   3.3 |   Yes    | —                             | 20d down -16.6%; below MA20 by 19.5%; RSI14=16 |
|   27 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  79.4 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   28 | Exxon Mobil Corporation / XOM                                                  |  73.6 |    No    | malformed_input               | Suppressed: malformed_input                    |
|   31 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  50.6 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   32 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  49.7 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    4 | FTSE 100 / ^FTSE                    |  71.8 |   Yes    | —            | 20d up +2.2%; above MA20 by 1.5%; RSI14=55   |
|    6 | Euro Stoxx 50 / ^STOXX50E           |  61.2 |   Yes    | —            | 20d up +1.0%; below MA20 by 0.1%; RSI14=41   |
|    7 | Hang Seng / ^HSI                    |  59.4 |   Yes    | —            | 20d up +8.2%; above MA20 by 3.4%; RSI14=68   |
|   10 | DAX / ^GDAXI                        |  57.0 |   Yes    | —            | 20d up +1.7%; below MA20 by 0.1%; RSI14=36   |
|   11 | CAC 40 / ^FCHI                      |  55.1 |   Yes    | —            | 20d down -0.2%; below MA20 by 0.1%; RSI14=42 |
|   12 | Dow Jones Industrial Average / ^DJI |  51.8 |   Yes    | —            | 20d up +0.1%; below MA20 by 0.8%; RSI14=33   |
|   15 | S&P 500 / ^GSPC                     |  47.0 |   Yes    | —            | 20d up +0.7%; below MA20 by 1.0%; RSI14=39   |
|   17 | Russell 2000 / ^RUT                 |  43.0 |   Yes    | —            | 20d down -2.6%; below MA20 by 1.6%; RSI14=36 |
|   20 | NASDAQ 100 / ^NDX                   |  29.4 |   Yes    | —            | 20d down -4.5%; below MA20 by 3.9%; RSI14=33 |
|   33 | Nikkei 225 / ^N225                  |  26.4 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-07-24 |
| 7203.T    | 2026-07-24 |
| 8306.T    | 2026-07-24 |
| AAPL      | 2026-07-24 |
| AMZN      | 2026-07-24 |
| BZ=F      | 2026-07-24 |
| CL=F      | 2026-07-24 |
| GC=F      | 2026-07-24 |
| GOOGL     | 2026-07-24 |
| HG=F      | 2026-07-24 |
| JPM       | 2026-07-24 |
| META      | 2026-07-24 |
| MSFT      | 2026-07-24 |
| NG=F      | 2026-07-24 |
| NVDA      | 2026-07-24 |
| PL=F      | 2026-07-24 |
| SI=F      | 2026-07-24 |
| TSLA      | 2026-07-24 |
| UNH       | 2026-07-24 |
| XOM       | 2026-07-24 |
| ZC=F      | 2026-07-24 |
| ZS=F      | 2026-07-24 |
| ZW=F      | 2026-07-24 |
| ^DJI      | 2026-07-24 |
| ^FCHI     | 2026-07-24 |
| ^FTSE     | 2026-07-24 |
| ^GDAXI    | 2026-07-24 |
| ^GSPC     | 2026-07-24 |
| ^HSI      | 2026-07-24 |
| ^N225     | 2026-07-24 |
| ^NDX      | 2026-07-24 |
| ^RUT      | 2026-07-24 |
| ^STOXX50E | 2026-07-24 |

## Symbol Details

### JPMorgan Chase & Co. / JPM (score 79.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.9% |
| ret_5d     |  +3.6% |
| ret_20d    |  +5.9% |
| ret_60d    | +13.9% |
| ma20_dist  |  +4.3% |
| ma50_dist  |  +9.9% |
| vol_20d    |  20.2% |
| mdd_60d    |   6.1% |
| rsi_14     |   64.7 |
| zscore_20d |    1.9 |

### Soybeans / ZS=F (score 77.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.8% |
| ret_5d     |  +3.6% |
| ret_20d    | +10.7% |
| ret_60d    |  +6.4% |
| ma20_dist  |  +5.2% |
| ma50_dist  |  +6.9% |
| vol_20d    |  19.7% |
| mdd_60d    |   8.8% |
| rsi_14     |   74.0 |
| zscore_20d |    1.5 |

### Apple Inc. / AAPL (score 74.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +3.5% |
| ret_5d     |  -0.2% |
| ret_20d    | +21.0% |
| ret_60d    | +23.1% |
| ma20_dist  |  +5.9% |
| ma50_dist  |  +8.7% |
| vol_20d    |  29.3% |
| mdd_60d    |  12.7% |
| rsi_14     |   67.7 |
| zscore_20d |    1.2 |

### FTSE 100 / ^FTSE (score 71.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | +1.3% |
| ret_20d    | +2.2% |
| ret_60d    | +5.1% |
| ma20_dist  | +1.5% |
| ma50_dist  | +2.5% |
| vol_20d    | 11.1% |
| mdd_60d    |  2.6% |
| rsi_14     |  55.2 |
| zscore_20d |   1.9 |

### Corn / ZC=F (score 65.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.1% |
| ret_5d     |  +4.4% |
| ret_20d    | +11.9% |
| ret_60d    |  -0.2% |
| ma20_dist  |  +6.1% |
| ma50_dist  |  +6.3% |
| vol_20d    |  26.8% |
| mdd_60d    |  15.7% |
| rsi_14     |   66.0 |
| zscore_20d |    1.6 |

### Euro Stoxx 50 / ^STOXX50E (score 61.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | +0.8% |
| ret_20d    | +1.0% |
| ret_60d    | +7.6% |
| ma20_dist  | -0.1% |
| ma50_dist  | +1.7% |
| vol_20d    | 15.0% |
| mdd_60d    |  3.6% |
| rsi_14     |  41.0 |
| zscore_20d |  -0.1 |

### Hang Seng / ^HSI (score 59.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | +1.6% |
| ret_20d    | +8.2% |
| ret_60d    | -3.7% |
| ma20_dist  | +3.4% |
| ma50_dist  | +1.3% |
| vol_20d    | 20.3% |
| mdd_60d    | 14.9% |
| rsi_14     |  67.7 |
| zscore_20d |   1.0 |

### Brent Crude Oil / BZ=F (score 57.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -3.9% |
| ret_5d     |  +9.9% |
| ret_20d    | +28.6% |
| ret_60d    | -13.0% |
| ma20_dist  | +18.4% |
| ma50_dist  |  +9.3% |
| vol_20d    |  53.8% |
| mdd_60d    |  39.4% |
| rsi_14     |   82.6 |
| zscore_20d |    1.7 |

### Wheat / ZW=F (score 57.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.6% |
| ret_5d     |  -0.7% |
| ret_20d    | +14.7% |
| ret_60d    |  +4.5% |
| ma20_dist  |  +6.8% |
| ma50_dist  |  +9.1% |
| vol_20d    |  37.8% |
| mdd_60d    |  14.6% |
| rsi_14     |   70.0 |
| zscore_20d |    1.0 |

### DAX / ^GDAXI (score 57.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.4% |
| ret_5d     | +1.1% |
| ret_20d    | +1.7% |
| ret_60d    | +3.3% |
| ma20_dist  | -0.1% |
| ma50_dist  | +0.6% |
| vol_20d    | 16.2% |
| mdd_60d    |  4.7% |
| rsi_14     |  36.4 |
| zscore_20d |  -0.0 |

### CAC 40 / ^FCHI (score 55.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | +0.4% |
| ret_20d    | -0.2% |
| ret_60d    | +3.2% |
| ma20_dist  | -0.1% |
| ma50_dist  | +0.9% |
| vol_20d    | 13.5% |
| mdd_60d    |  4.2% |
| rsi_14     |  42.4 |
| zscore_20d |  -0.1 |

### Dow Jones Industrial Average / ^DJI (score 51.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | -0.4% |
| ret_20d    | +0.1% |
| ret_60d    | +5.7% |
| ma20_dist  | -0.8% |
| ma50_dist  | +1.0% |
| vol_20d    |  8.7% |
| mdd_60d    |  3.2% |
| rsi_14     |  32.9 |
| zscore_20d |  -1.2 |

### UnitedHealth Group Inc. / UNH (score 50.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.7% |
| ret_5d     |  -1.3% |
| ret_20d    |  +1.3% |
| ret_60d    | +15.4% |
| ma20_dist  |  -1.0% |
| ma50_dist  |  +3.5% |
| vol_20d    |  27.2% |
| mdd_60d    |   6.1% |
| rsi_14     |   51.6 |
| zscore_20d |   -0.8 |

### NVIDIA Corporation / NVDA (score 47.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.9% |
| ret_5d     | +2.0% |
| ret_20d    | +5.7% |
| ret_60d    | -3.0% |
| ma20_dist  | +1.7% |
| ma50_dist  | -1.1% |
| vol_20d    | 34.7% |
| mdd_60d    | 18.3% |
| rsi_14     |  59.6 |
| zscore_20d |   0.6 |

### S&P 500 / ^GSPC (score 47.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.0% |
| ret_5d     | -0.6% |
| ret_20d    | +0.7% |
| ret_60d    | +3.8% |
| ma20_dist  | -1.0% |
| ma50_dist  | -0.8% |
| vol_20d    | 10.1% |
| mdd_60d    |  4.5% |
| rsi_14     |  38.9 |
| zscore_20d |  -1.4 |

### Gold / GC=F (score 45.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.5% |
| ret_5d     |  +1.4% |
| ret_20d    |  +0.9% |
| ret_60d    | -11.4% |
| ma20_dist  |  -0.0% |
| ma50_dist  |  -4.4% |
| vol_20d    |  21.5% |
| mdd_60d    |  15.6% |
| rsi_14     |   43.8 |
| zscore_20d |   -0.0 |

### Russell 2000 / ^RUT (score 43.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | -1.1% |
| ret_20d    | -2.6% |
| ret_60d    | +6.3% |
| ma20_dist  | -1.6% |
| ma50_dist  | -0.0% |
| vol_20d    | 10.8% |
| mdd_60d    |  4.8% |
| rsi_14     |  36.2 |
| zscore_20d |  -1.8 |

### Silver / SI=F (score 35.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.5% |
| ret_5d     |  +4.7% |
| ret_20d    |  +0.5% |
| ret_60d    | -19.9% |
| ma20_dist  |  -0.3% |
| ma50_dist  | -11.8% |
| vol_20d    |  38.8% |
| mdd_60d    |  37.1% |
| rsi_14     |   41.8 |
| zscore_20d |   -0.1 |

### Microsoft Corporation / MSFT (score 33.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.0% |
| ret_5d     |  -3.1% |
| ret_20d    |  +8.2% |
| ret_60d    | -10.9% |
| ma20_dist  |  -1.3% |
| ma50_dist  |  -4.4% |
| vol_20d    |  31.6% |
| mdd_60d    |  23.4% |
| rsi_14     |   46.6 |
| zscore_20d |   -0.6 |

### NASDAQ 100 / ^NDX (score 29.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.1% |
| ret_5d     | -1.6% |
| ret_20d    | -4.5% |
| ret_60d    | +4.1% |
| ma20_dist  | -3.9% |
| ma50_dist  | -4.7% |
| vol_20d    | 22.2% |
| mdd_60d    |  8.3% |
| rsi_14     |  33.1 |
| zscore_20d |  -2.2 |

### Meta Platforms Inc. / META (score 26.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.8% |
| ret_5d     |  -7.9% |
| ret_20d    |  +9.6% |
| ret_60d    | -11.3% |
| ma20_dist  |  -4.2% |
| ma50_dist  |  -1.8% |
| vol_20d    |  53.7% |
| mdd_60d    |  18.8% |
| rsi_14     |   48.8 |
| zscore_20d |   -0.7 |

### Platinum / PL=F (score 26.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.4% |
| ret_5d     |  -0.8% |
| ret_20d    |  -0.5% |
| ret_60d    | -18.0% |
| ma20_dist  |  -1.1% |
| ma50_dist  |  -8.9% |
| vol_20d    |  31.4% |
| mdd_60d    |  29.1% |
| rsi_14     |   44.2 |
| zscore_20d |   -0.7 |

### Natural Gas / NG=F (score 25.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.5% |
| ret_5d     |  -1.4% |
| ret_20d    | -14.1% |
| ret_60d    | +12.2% |
| ma20_dist  |  -5.4% |
| ma50_dist  |  -7.1% |
| vol_20d    |  32.9% |
| mdd_60d    |  14.5% |
| rsi_14     |   23.4 |
| zscore_20d |   -1.0 |

### Amazon.com Inc. / AMZN (score 25.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.7% |
| ret_5d     |  -6.1% |
| ret_20d    |  +2.2% |
| ret_60d    | -10.6% |
| ma20_dist  |  -4.8% |
| ma50_dist  |  -6.9% |
| vol_20d    |  28.1% |
| mdd_60d    |  17.4% |
| rsi_14     |   37.3 |
| zscore_20d |   -2.0 |

### Alphabet Inc. Class A / GOOGL (score 16.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.6% |
| ret_5d     |  -7.8% |
| ret_20d    |  -7.0% |
| ret_60d    |  -8.5% |
| ma20_dist  |  -9.2% |
| ma50_dist  | -12.3% |
| vol_20d    |  40.6% |
| mdd_60d    |  21.0% |
| rsi_14     |   26.5 |
| zscore_20d |   -2.4 |

### Tesla Inc. / TSLA (score 3.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.1% |
| ret_5d     | -17.8% |
| ret_20d    | -16.6% |
| ret_60d    | -16.8% |
| ma20_dist  | -19.5% |
| ma50_dist  | -22.2% |
| vol_20d    |  75.2% |
| mdd_60d    |  29.7% |
| rsi_14     |   15.7 |
| zscore_20d |   -2.7 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| JPMorgan Chase & Co. / JPM          |   7.5650 |           2.1% |                 0.49x |       15.1300 |            4.3% |
| Soybeans / ZS=F                     |  17.1250 |           1.4% |                 0.51x |       34.2500 |            2.7% |
| Apple Inc. / AAPL                   |   7.8486 |           2.4% |                 0.34x |       15.6971 |            4.7% |
| FTSE 100 / ^FTSE                    | 117.3287 |           1.1% |                 0.90x |      234.6574 |            2.2% |
| Corn / ZC=F                         |   9.6964 |           2.1% |                 0.37x |       19.3929 |            4.2% |
| Euro Stoxx 50 / ^STOXX50E           |  74.6049 |           1.2% |                 0.67x |      149.2099 |            2.4% |
| Hang Seng / ^HSI                    | 486.7363 |           1.9% |                 0.49x |      973.4727 |            3.9% |
| Brent Crude Oil / BZ=F              |   4.7979 |           5.0% |                 0.19x |        9.5957 |            9.9% |
| Wheat / ZW=F                        |  22.1071 |           3.3% |                 0.26x |       44.2143 |            6.5% |
| DAX / ^GDAXI                        | 316.4256 |           1.3% |                 0.62x |      632.8513 |            2.5% |
| CAC 40 / ^FCHI                      | 101.2415 |           1.2% |                 0.74x |      202.4830 |            2.4% |
| Dow Jones Industrial Average / ^DJI | 535.4316 |           1.0% |                 1.15x |     1070.8633 |            2.1% |
| UnitedHealth Group Inc. / UNH       |  12.9014 |           3.1% |                 0.37x |       25.8029 |            6.1% |
| NVIDIA Corporation / NVDA           |   7.5986 |           3.7% |                 0.29x |       15.1971 |            7.3% |
| S&P 500 / ^GSPC                     |  70.6158 |           1.0% |                 0.99x |      141.2316 |            1.9% |
| Gold / GC=F                         |  67.6429 |           1.7% |                 0.47x |      135.2857 |            3.3% |
| Russell 2000 / ^RUT                 |  36.5914 |           1.2% |                 0.93x |       73.1828 |            2.5% |
| Silver / SI=F                       |   1.7699 |           3.0% |                 0.26x |        3.5399 |            6.0% |
| Microsoft Corporation / MSFT        |  11.1343 |           2.9% |                 0.32x |       22.2686 |            5.8% |
| NASDAQ 100 / ^NDX                   | 538.7631 |           1.9% |                 0.45x |     1077.5262 |            3.8% |
| Meta Platforms Inc. / META          |  26.8336 |           4.5% |                 0.19x |       53.6671 |            9.0% |
| Platinum / PL=F                     |  26.5071 |           1.7% |                 0.32x |       53.0143 |            3.3% |
| Natural Gas / NG=F                  |   0.1141 |           4.0% |                 0.30x |        0.2281 |            7.9% |
| Amazon.com Inc. / AMZN              |   6.7964 |           2.9% |                 0.36x |       13.5929 |            5.9% |
| Alphabet Inc. Class A / GOOGL       |  11.5736 |           3.6% |                 0.25x |       23.1471 |            7.2% |
| Tesla Inc. / TSLA                   |  16.7793 |           5.4% |                 0.13x |       33.5586 |           10.7% |

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

Scoring engine version: **1.0.0** | Git commit: **0bc26f0**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
