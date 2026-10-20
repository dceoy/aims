+++
title = "Market Analysis 2026-07-28"
date = "2026-07-28T00:00:00+00:00"
draft = false
summary = "Neutral market: 26 reliable instruments. Top signal: JPM (score 81.5)."
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
source_files = ["data/analysis/2026-07-28.json", "data/history/2026-07-28.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "eaeac01"
+++

## Market Regime

**Neutral** — 13 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **JPMorgan Chase & Co. / JPM** — score 81.5, 20d return +8.7%, RSI14=66. 20d up +8.7%; above MA20 by 4.8%; RSI14=66 ⚠️ Upcoming: FOMC rate decision (2026-07-29)
- **Apple Inc. / AAPL** — score 79.4, 20d return +18.7%, RSI14=72. 20d up +18.7%; above MA20 by 6.3%; RSI14=72 ⚠️ Upcoming: FOMC rate decision (2026-07-29); AAPL earnings release (2026-07-30)
- **FTSE 100 / ^FTSE** — score 72.4, 20d return +2.8%, RSI14=57. 20d up +2.8%; above MA20 by 1.8%; RSI14=57 ⚠️ Upcoming: FOMC rate decision (2026-07-29)
- **DAX / ^GDAXI** — score 66.4, 20d return +3.0%, RSI14=48. 20d up +3.0%; above MA20 by 0.8%; RSI14=48 ⚠️ Upcoming: FOMC rate decision (2026-07-29)
- **Hang Seng / ^HSI** — score 66.1, 20d return +11.2%, RSI14=72. 20d up +11.2%; above MA20 by 3.9%; RSI14=72 ⚠️ Upcoming: FOMC rate decision (2026-07-29)

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
| 2026-08-03 | 8306.T earnings release      | 8306.T                          |
| 2026-08-04 | 7203.T earnings release      | 7203.T                          |

## Signal History

Compared with the previous available report (**2026-07-27**).

- **New top-5:** ^GDAXI, ^HSI
- **Persistent top signals:** ^FTSE (4 reports), AAPL (2 reports), JPM (2 reports)
- **Dropped from top-5:** ZC=F, ZS=F

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +4 |   +27.0 |
| 7203.T    |     +1 |   +16.1 |
| 8306.T    |     +0 |    +6.4 |
| AAPL      |     +1 |    +5.2 |
| AMZN      |     +0 |    -6.1 |
| BZ=F      |     -9 |   -16.7 |
| CL=F      |     -2 |   -15.2 |
| GC=F      |     +0 |    -2.4 |
| GOOGL     |     +2 |    +3.9 |
| HG=F      |     -2 |    +0.6 |
| JPM       |     +0 |    +2.4 |
| META      |     +1 |    +3.6 |
| MSFT      |     +5 |   +10.0 |
| NG=F      |     -2 |    -7.6 |
| NVDA      |     -8 |   -22.1 |
| PL=F      |     +4 |   +13.0 |
| SI=F      |     -3 |    -8.5 |
| TSLA      |     +0 |    +1.5 |
| UNH       |     -2 |    -6.7 |
| XOM       |     -1 |    -4.8 |
| ZC=F      |     -6 |   -13.6 |
| ZS=F      |     -8 |   -23.9 |
| ZW=F      |     +0 |    -3.9 |
| ^DJI      |     +4 |    +4.5 |
| ^FCHI     |     +4 |    +3.0 |
| ^FTSE     |     +1 |    +0.6 |
| ^GDAXI    |     +6 |    +9.4 |
| ^GSPC     |     +2 |    -0.6 |
| ^HSI      |     +2 |    +6.7 |
| ^N225     |     +0 |   +10.6 |
| ^NDX      |     +1 |    +1.8 |
| ^RUT      |     +5 |    +8.2 |
| ^STOXX50E |     +0 |    -2.4 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|    9 | Wheat / ZW=F           |  53.6 |   Yes    | —               | 20d up +14.1%; above MA20 by 3.3%; RSI14=63   |
|   10 | Soybeans / ZS=F        |  53.0 |   Yes    | —               | 20d up +7.3%; above MA20 by 1.5%; RSI14=54    |
|   11 | Corn / ZC=F            |  52.1 |   Yes    | —               | 20d up +9.4%; above MA20 by 2.7%; RSI14=55    |
|   16 | Gold / GC=F            |  42.7 |   Yes    | —               | 20d down -0.1%; above MA20 by 0.2%; RSI14=45  |
|   17 | Brent Crude Oil / BZ=F |  41.2 |   Yes    | —               | 20d up +22.7%; above MA20 by 7.0%; RSI14=66   |
|   18 | Platinum / PL=F        |  39.1 |   Yes    | —               | 20d down -0.6%; above MA20 by 0.6%; RSI14=45  |
|   21 | Silver / SI=F          |  27.0 |   Yes    | —               | 20d down -1.3%; below MA20 by 0.5%; RSI14=44  |
|   25 | Natural Gas / NG=F     |  17.9 |   Yes    | —               | 20d down -14.4%; below MA20 by 8.1%; RSI14=18 |
|   31 | Copper / HG=F          |  61.5 |    No    | malformed_input | Suppressed: malformed_input                   |
|   32 | WTI Crude Oil / CL=F   |  42.7 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                    |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | ---------------------------------------------- |
|    1 | JPMorgan Chase & Co. / JPM                                                     |  81.5 |   Yes    | —                             | 20d up +8.7%; above MA20 by 4.8%; RSI14=66     |
|    2 | Apple Inc. / AAPL                                                              |  79.4 |   Yes    | —                             | 20d up +18.7%; above MA20 by 6.3%; RSI14=72    |
|   14 | Microsoft Corporation / MSFT                                                   |  43.3 |   Yes    | —                             | 20d up +4.3%; above MA20 by 0.4%; RSI14=50     |
|   15 | UnitedHealth Group Inc. / UNH                                                  |  43.3 |   Yes    | —                             | 20d down -2.4%; below MA20 by 1.6%; RSI14=43   |
|   20 | Meta Platforms Inc. / META                                                     |  30.0 |   Yes    | —                             | 20d up +7.9%; below MA20 by 4.7%; RSI14=45     |
|   22 | NVIDIA Corporation / NVDA                                                      |  25.1 |   Yes    | —                             | 20d up +2.1%; below MA20 by 3.4%; RSI14=50     |
|   23 | Alphabet Inc. Class A / GOOGL                                                  |  20.6 |   Yes    | —                             | 20d down -3.2%; below MA20 by 7.1%; RSI14=31   |
|   24 | Amazon.com Inc. / AMZN                                                         |  19.1 |   Yes    | —                             | 20d down -0.6%; below MA20 by 5.1%; RSI14=34   |
|   26 | Tesla Inc. / TSLA                                                              |   4.8 |   Yes    | —                             | 20d down -18.6%; below MA20 by 19.7%; RSI14=17 |
|   27 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  85.8 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   28 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  76.7 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   29 | Exxon Mobil Corporation / XOM                                                  |  68.8 |    No    | malformed_input               | Suppressed: malformed_input                    |
|   30 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  66.7 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    3 | FTSE 100 / ^FTSE                    |  72.4 |   Yes    | —            | 20d up +2.8%; above MA20 by 1.8%; RSI14=57   |
|    4 | DAX / ^GDAXI                        |  66.4 |   Yes    | —            | 20d up +3.0%; above MA20 by 0.8%; RSI14=48   |
|    5 | Hang Seng / ^HSI                    |  66.1 |   Yes    | —            | 20d up +11.2%; above MA20 by 3.9%; RSI14=72  |
|    6 | Euro Stoxx 50 / ^STOXX50E           |  58.8 |   Yes    | —            | 20d up +0.8%; below MA20 by 0.1%; RSI14=47   |
|    7 | CAC 40 / ^FCHI                      |  58.2 |   Yes    | —            | 20d up +0.5%; above MA20 by 0.3%; RSI14=48   |
|    8 | Dow Jones Industrial Average / ^DJI |  56.4 |   Yes    | —            | 20d up +0.6%; below MA20 by 0.3%; RSI14=39   |
|   12 | Russell 2000 / ^RUT                 |  51.2 |   Yes    | —            | 20d down -2.1%; below MA20 by 0.9%; RSI14=44 |
|   13 | S&P 500 / ^GSPC                     |  46.4 |   Yes    | —            | 20d up +0.8%; below MA20 by 1.1%; RSI14=41   |
|   19 | NASDAQ 100 / ^NDX                   |  31.2 |   Yes    | —            | 20d down -3.7%; below MA20 by 4.0%; RSI14=37 |
|   33 | Nikkei 225 / ^N225                  |  37.0 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-07-27 |
| 7203.T    | 2026-07-27 |
| 8306.T    | 2026-07-27 |
| AAPL      | 2026-07-27 |
| AMZN      | 2026-07-27 |
| BZ=F      | 2026-07-27 |
| CL=F      | 2026-07-27 |
| GC=F      | 2026-07-27 |
| GOOGL     | 2026-07-27 |
| HG=F      | 2026-07-27 |
| JPM       | 2026-07-27 |
| META      | 2026-07-27 |
| MSFT      | 2026-07-27 |
| NG=F      | 2026-07-27 |
| NVDA      | 2026-07-27 |
| PL=F      | 2026-07-27 |
| SI=F      | 2026-07-27 |
| TSLA      | 2026-07-27 |
| UNH       | 2026-07-27 |
| XOM       | 2026-07-27 |
| ZC=F      | 2026-07-27 |
| ZS=F      | 2026-07-27 |
| ZW=F      | 2026-07-27 |
| ^DJI      | 2026-07-27 |
| ^FCHI     | 2026-07-27 |
| ^FTSE     | 2026-07-27 |
| ^GDAXI    | 2026-07-27 |
| ^GSPC     | 2026-07-27 |
| ^HSI      | 2026-07-27 |
| ^N225     | 2026-07-27 |
| ^NDX      | 2026-07-27 |
| ^RUT      | 2026-07-27 |
| ^STOXX50E | 2026-07-27 |

## Symbol Details

### JPMorgan Chase & Co. / JPM (score 81.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.8% |
| ret_5d     |  +5.1% |
| ret_20d    |  +8.7% |
| ret_60d    | +15.7% |
| ma20_dist  |  +4.8% |
| ma50_dist  | +10.4% |
| vol_20d    |  18.8% |
| mdd_60d    |   6.1% |
| rsi_14     |   65.7 |
| zscore_20d |    2.0 |

### Apple Inc. / AAPL (score 79.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.2% |
| ret_5d     |  +3.2% |
| ret_20d    | +18.7% |
| ret_60d    | +24.8% |
| ma20_dist  |  +6.3% |
| ma50_dist  |  +9.7% |
| vol_20d    |  28.3% |
| mdd_60d    |  12.7% |
| rsi_14     |   72.1 |
| zscore_20d |    1.4 |

### FTSE 100 / ^FTSE (score 72.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | +2.4% |
| ret_20d    | +2.8% |
| ret_60d    | +3.9% |
| ma20_dist  | +1.8% |
| ma50_dist  | +2.9% |
| vol_20d    | 11.1% |
| mdd_60d    |  2.6% |
| rsi_14     |  56.9 |
| zscore_20d |   2.1 |

### DAX / ^GDAXI (score 66.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.0% |
| ret_5d     | +2.1% |
| ret_20d    | +3.0% |
| ret_60d    | +5.7% |
| ma20_dist  | +0.8% |
| ma50_dist  | +1.6% |
| vol_20d    | 16.5% |
| mdd_60d    |  4.7% |
| rsi_14     |  48.0 |
| zscore_20d |   0.7 |

### Hang Seng / ^HSI (score 66.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.0% |
| ret_5d     |  +0.3% |
| ret_20d    | +11.2% |
| ret_60d    |  -1.8% |
| ma20_dist  |  +3.9% |
| ma50_dist  |  +2.4% |
| vol_20d    |  18.7% |
| mdd_60d    |  14.9% |
| rsi_14     |   71.7 |
| zscore_20d |    1.2 |

### Euro Stoxx 50 / ^STOXX50E (score 58.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.0% |
| ret_5d     | +0.9% |
| ret_20d    | +0.8% |
| ret_60d    | +8.0% |
| ma20_dist  | -0.1% |
| ma50_dist  | +1.6% |
| vol_20d    | 15.0% |
| mdd_60d    |  3.6% |
| rsi_14     |  46.7 |
| zscore_20d |  -0.1 |

### CAC 40 / ^FCHI (score 58.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | +0.8% |
| ret_20d    | +0.5% |
| ret_60d    | +5.4% |
| ma20_dist  | +0.3% |
| ma50_dist  | +1.2% |
| vol_20d    | 13.5% |
| mdd_60d    |  4.2% |
| rsi_14     |  47.8 |
| zscore_20d |   0.4 |

### Dow Jones Industrial Average / ^DJI (score 56.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | +0.7% |
| ret_20d    | +0.6% |
| ret_60d    | +6.9% |
| ma20_dist  | -0.3% |
| ma50_dist  | +1.4% |
| vol_20d    |  8.9% |
| mdd_60d    |  3.2% |
| rsi_14     |  39.4 |
| zscore_20d |  -0.5 |

### Wheat / ZW=F (score 53.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.7% |
| ret_5d     |  -2.1% |
| ret_20d    | +14.1% |
| ret_60d    |  +2.8% |
| ma20_dist  |  +3.3% |
| ma50_dist  |  +6.2% |
| vol_20d    |  38.3% |
| mdd_60d    |  14.6% |
| rsi_14     |   63.0 |
| zscore_20d |    0.5 |

### Soybeans / ZS=F (score 53.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -3.2% |
| ret_5d     | -1.4% |
| ret_20d    | +7.3% |
| ret_60d    | +2.2% |
| ma20_dist  | +1.5% |
| ma50_dist  | +3.5% |
| vol_20d    | 23.4% |
| mdd_60d    |  8.8% |
| rsi_14     |  53.6 |
| zscore_20d |   0.5 |

### Corn / ZC=F (score 52.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.7% |
| ret_5d     | +0.5% |
| ret_20d    | +9.4% |
| ret_60d    | -3.2% |
| ma20_dist  | +2.7% |
| ma50_dist  | +3.5% |
| vol_20d    | 28.9% |
| mdd_60d    | 15.7% |
| rsi_14     |  55.5 |
| zscore_20d |   0.8 |

### Russell 2000 / ^RUT (score 51.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | +0.2% |
| ret_20d    | -2.1% |
| ret_60d    | +7.6% |
| ma20_dist  | -0.9% |
| ma50_dist  | +0.5% |
| vol_20d    | 11.1% |
| mdd_60d    |  4.8% |
| rsi_14     |  43.8 |
| zscore_20d |  -1.0 |

### S&P 500 / ^GSPC (score 46.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.0% |
| ret_5d     | -0.4% |
| ret_20d    | +0.8% |
| ret_60d    | +3.9% |
| ma20_dist  | -1.1% |
| ma50_dist  | -0.8% |
| vol_20d    | 10.1% |
| mdd_60d    |  4.5% |
| rsi_14     |  41.5 |
| zscore_20d |  -1.6 |

### Microsoft Corporation / MSFT (score 43.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.9% |
| ret_5d     | -3.3% |
| ret_20d    | +4.3% |
| ret_60d    | -8.1% |
| ma20_dist  | +0.4% |
| ma50_dist  | -2.4% |
| vol_20d    | 25.8% |
| mdd_60d    | 23.4% |
| rsi_14     |  50.2 |
| zscore_20d |   0.2 |

### UnitedHealth Group Inc. / UNH (score 43.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.7% |
| ret_5d     |  -0.9% |
| ret_20d    |  -2.4% |
| ret_60d    | +13.3% |
| ma20_dist  |  -1.6% |
| ma50_dist  |  +2.6% |
| vol_20d    |  25.2% |
| mdd_60d    |   6.1% |
| rsi_14     |   43.1 |
| zscore_20d |   -1.3 |

### Gold / GC=F (score 42.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.2% |
| ret_5d     |  +1.6% |
| ret_20d    |  -0.1% |
| ret_60d    | -10.4% |
| ma20_dist  |  +0.2% |
| ma50_dist  |  -4.0% |
| vol_20d    |  21.1% |
| mdd_60d    |  15.6% |
| rsi_14     |   45.0 |
| zscore_20d |    0.1 |

### Brent Crude Oil / BZ=F (score 41.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -8.7% |
| ret_5d     |  -1.0% |
| ret_20d    | +22.7% |
| ret_60d    | -25.1% |
| ma20_dist  |  +7.0% |
| ma50_dist  |  +0.1% |
| vol_20d    |  61.2% |
| mdd_60d    |  37.5% |
| rsi_14     |   66.0 |
| zscore_20d |    0.7 |

### Platinum / PL=F (score 39.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.7% |
| ret_5d     |  +1.8% |
| ret_20d    |  -0.6% |
| ret_60d    | -14.0% |
| ma20_dist  |  +0.6% |
| ma50_dist  |  -6.7% |
| vol_20d    |  31.3% |
| mdd_60d    |  29.1% |
| rsi_14     |   45.5 |
| zscore_20d |    0.4 |

### NASDAQ 100 / ^NDX (score 31.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | -2.0% |
| ret_20d    | -3.7% |
| ret_60d    | +3.1% |
| ma20_dist  | -4.0% |
| ma50_dist  | -4.9% |
| vol_20d    | 22.0% |
| mdd_60d    |  8.5% |
| rsi_14     |  36.5 |
| zscore_20d |  -2.0 |

### Meta Platforms Inc. / META (score 30.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.2% |
| ret_5d     |  -8.0% |
| ret_20d    |  +7.9% |
| ret_60d    | -11.2% |
| ma20_dist  |  -4.7% |
| ma50_dist  |  -1.9% |
| vol_20d    |  53.7% |
| mdd_60d    |  14.5% |
| rsi_14     |   44.7 |
| zscore_20d |   -0.9 |

### Silver / SI=F (score 27.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.3% |
| ret_5d     |  +2.9% |
| ret_20d    |  -1.3% |
| ret_60d    | -18.3% |
| ma20_dist  |  -0.5% |
| ma50_dist  | -11.3% |
| vol_20d    |  38.5% |
| mdd_60d    |  37.1% |
| rsi_14     |   43.6 |
| zscore_20d |   -0.2 |

### NVIDIA Corporation / NVDA (score 25.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -5.0% |
| ret_5d     | -3.3% |
| ret_20d    | +2.1% |
| ret_60d    | -6.1% |
| ma20_dist  | -3.4% |
| ma50_dist  | -5.8% |
| vol_20d    | 38.8% |
| mdd_60d    | 18.3% |
| rsi_14     |  49.7 |
| zscore_20d |  -1.2 |

### Alphabet Inc. Class A / GOOGL (score 20.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.1% |
| ret_5d     |  -7.2% |
| ret_20d    |  -3.2% |
| ret_60d    |  -6.6% |
| ma20_dist  |  -7.1% |
| ma50_dist  | -10.1% |
| vol_20d    |  41.0% |
| mdd_60d    |  21.0% |
| rsi_14     |   30.8 |
| zscore_20d |   -1.7 |

### Amazon.com Inc. / AMZN (score 19.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.3% |
| ret_5d     |  -7.4% |
| ret_20d    |  -0.6% |
| ret_60d    | -12.0% |
| ma20_dist  |  -5.1% |
| ma50_dist  |  -6.9% |
| vol_20d    |  26.8% |
| mdd_60d    |  17.4% |
| rsi_14     |   34.2 |
| zscore_20d |   -2.1 |

### Natural Gas / NG=F (score 17.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -3.6% |
| ret_5d     |  -3.3% |
| ret_20d    | -14.4% |
| ret_60d    |  +4.5% |
| ma20_dist  |  -8.1% |
| ma50_dist  | -10.4% |
| vol_20d    |  33.2% |
| mdd_60d    |  17.2% |
| rsi_14     |   18.4 |
| zscore_20d |   -1.5 |

### Tesla Inc. / TSLA (score 4.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.2% |
| ret_5d     | -16.3% |
| ret_20d    | -18.6% |
| ret_60d    | -17.1% |
| ma20_dist  | -19.7% |
| ma50_dist  | -22.7% |
| vol_20d    |  74.8% |
| mdd_60d    |  30.6% |
| rsi_14     |   17.2 |
| zscore_20d |   -2.3 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| JPMorgan Chase & Co. / JPM          |   7.7193 |           2.2% |                 0.53x |       15.4386 |            4.3% |
| Apple Inc. / AAPL                   |   7.9357 |           2.4% |                 0.35x |       15.8714 |            4.7% |
| FTSE 100 / ^FTSE                    | 116.5430 |           1.1% |                 0.90x |      233.0861 |            2.2% |
| DAX / ^GDAXI                        | 324.1848 |           1.3% |                 0.61x |      648.3697 |            2.6% |
| Hang Seng / ^HSI                    | 480.7342 |           1.9% |                 0.53x |      961.4685 |            3.8% |
| Euro Stoxx 50 / ^STOXX50E           |  75.3500 |           1.2% |                 0.67x |      150.6999 |            2.4% |
| CAC 40 / ^FCHI                      |  99.9551 |           1.2% |                 0.74x |      199.9102 |            2.4% |
| Dow Jones Industrial Average / ^DJI | 545.8175 |           1.0% |                 1.12x |     1091.6350 |            2.1% |
| Wheat / ZW=F                        |  23.4821 |           3.6% |                 0.26x |       46.9643 |            7.1% |
| Soybeans / ZS=F                     |  18.6071 |           1.5% |                 0.43x |       37.2143 |            3.1% |
| Corn / ZC=F                         |  10.2857 |           2.3% |                 0.35x |       20.5714 |            4.6% |
| Russell 2000 / ^RUT                 |  36.5935 |           1.2% |                 0.90x |       73.1871 |            2.5% |
| S&P 500 / ^GSPC                     |  73.4036 |           1.0% |                 0.99x |      146.8072 |            2.0% |
| Microsoft Corporation / MSFT        |  11.3964 |           2.9% |                 0.39x |       22.7929 |            5.9% |
| UnitedHealth Group Inc. / UNH       |  12.8821 |           3.1% |                 0.40x |       25.7643 |            6.2% |
| Gold / GC=F                         |  66.2357 |           1.6% |                 0.47x |      132.4714 |            3.3% |
| Brent Crude Oil / BZ=F              |   5.1529 |           5.8% |                 0.16x |       10.3057 |           11.7% |
| Platinum / PL=F                     |  27.0571 |           1.7% |                 0.32x |       54.1143 |            3.3% |
| NASDAQ 100 / ^NDX                   | 535.2104 |           1.9% |                 0.45x |     1070.4208 |            3.8% |
| Meta Platforms Inc. / META          |  26.3371 |           4.4% |                 0.19x |       52.6743 |            8.9% |
| Silver / SI=F                       |   1.6606 |           2.8% |                 0.26x |        3.3211 |            5.7% |
| NVIDIA Corporation / NVDA           |   8.0300 |           4.1% |                 0.26x |       16.0600 |            8.2% |
| Alphabet Inc. Class A / GOOGL       |  11.7893 |           3.6% |                 0.24x |       23.5786 |            7.2% |
| Amazon.com Inc. / AMZN              |   6.7014 |           2.9% |                 0.37x |       13.4029 |            5.8% |
| Natural Gas / NG=F                  |   0.1139 |           4.1% |                 0.30x |        0.2279 |            8.2% |
| Tesla Inc. / TSLA                   |  16.4100 |           5.3% |                 0.13x |       32.8200 |           10.6% |

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

Scoring engine version: **1.0.0** | Git commit: **eaeac01**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
