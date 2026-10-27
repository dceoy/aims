+++
title = "Market Analysis 2026-10-27"
date = "2026-10-27T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: TSLA (score 78.2)."
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
source_files = ["data/analysis/2026-10-27.json", "data/history/2026-10-27.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "3597f45"
+++

## Market Regime

**Neutral** — 9 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Tesla Inc. / TSLA** — score 78.2, 20d return +9.6%, RSI14=55. 20d up +9.6%; above MA20 by 5.4%; RSI14=55 ⚠️ Upcoming: FOMC rate decision (2026-10-28)
- **Brent Crude Oil / BZ=F** — score 77.9, 20d return +10.0%, RSI14=84. 20d up +10.0%; above MA20 by 8.9%; RSI14=84 ⚠️ Upcoming: FOMC rate decision (2026-10-28)
- **Dow Jones Industrial Average / ^DJI** — score 72.4, 20d return +1.7%, RSI14=61. 20d up +1.7%; above MA20 by 1.2%; RSI14=61 ⚠️ Upcoming: FOMC rate decision (2026-10-28)
- **Microsoft Corporation / MSFT** — score 72.1, 20d return +4.6%, RSI14=52. 20d up +4.6%; above MA20 by 0.9%; RSI14=52 ⚠️ Upcoming: FOMC rate decision (2026-10-28); MSFT earnings release (2026-10-28)
- **FTSE 100 / ^FTSE** — score 71.5, 20d return +0.8%, RSI14=63. 20d up +0.8%; above MA20 by 1.2%; RSI14=63 ⚠️ Upcoming: FOMC rate decision (2026-10-28)

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                        | Applies To                      |
| ---------- | ---------------------------- | ------------------------------- |
| 2026-10-28 | FOMC rate decision           | Commodity, Equity, Equity Index |
| 2026-10-28 | GOOGL earnings release       | GOOGL                           |
| 2026-10-28 | MSFT earnings release        | MSFT                            |
| 2026-10-29 | AMZN earnings release        | AMZN                            |
| 2026-10-29 | ECB monetary policy decision | ^FCHI, ^GDAXI, ^STOXX50E        |
| 2026-10-30 | BOJ monetary policy decision | 6758.T, 7203.T, 8306.T, ^N225   |
| 2026-10-30 | XOM earnings release         | XOM                             |
| 2026-11-02 | AAPL earnings release        | AAPL                            |

## Signal History

Compared with the previous available report (**2026-10-26**).

- **New top-5:** TSLA
- **Persistent top signals:** BZ=F (7 reports), ^DJI (5 reports), ^FTSE (3 reports), MSFT (2 reports)
- **Dropped from top-5:** AAPL

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +0 |    -4.8 |
| 7203.T    |     +1 |    -3.3 |
| 8306.T    |     +0 |    +5.5 |
| AAPL      |     -4 |    -7.3 |
| AMZN      |     -2 |    -7.0 |
| BZ=F      |     -1 |    -7.6 |
| CL=F      |     -1 |   -15.2 |
| GC=F      |     +3 |   +14.8 |
| GOOGL     |     +1 |    -2.7 |
| HG=F      |     +0 |    -1.8 |
| JPM       |     +4 |   +11.5 |
| META      |     -1 |    -4.8 |
| MSFT      |     -1 |    +2.7 |
| NG=F      |     +0 |    +0.0 |
| NVDA      |     +2 |    +9.7 |
| PL=F      |     -1 |    -2.4 |
| SI=F      |     +4 |   +10.0 |
| TSLA      |     +5 |   +13.3 |
| UNH       |     -2 |    -3.6 |
| XOM       |     +0 |    -0.6 |
| ZC=F      |     -1 |    +0.0 |
| ZS=F      |     -8 |   -18.2 |
| ZW=F      |     -4 |    -7.6 |
| ^DJI      |     +1 |    +3.0 |
| ^FCHI     |     +0 |    +5.2 |
| ^FTSE     |     +0 |    +3.9 |
| ^GDAXI    |     +3 |    +7.6 |
| ^GSPC     |     +1 |    +2.7 |
| ^HSI      |     -1 |    -0.3 |
| ^N225     |     +0 |    -8.8 |
| ^NDX      |     -1 |    +2.1 |
| ^RUT      |     +0 |    -2.1 |
| ^STOXX50E |     +3 |    +6.1 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Exxon Mobil Corporation / XOM** — malformed_input
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **WTI Crude Oil / CL=F** — malformed_input
- **Copper / HG=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Natural Gas / NG=F** — malformed_input

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|    2 | Brent Crude Oil / BZ=F |  77.9 |   Yes    | —               | 20d up +10.0%; above MA20 by 8.9%; RSI14=84   |
|   16 | Soybeans / ZS=F        |  44.5 |   Yes    | —               | 20d down -3.6%; below MA20 by 2.6%; RSI14=17  |
|   18 | Gold / GC=F            |  38.2 |   Yes    | —               | 20d down -3.1%; below MA20 by 2.7%; RSI14=36  |
|   20 | Corn / ZC=F            |  26.4 |   Yes    | —               | 20d down -13.0%; below MA20 by 5.9%; RSI14=7  |
|   21 | Silver / SI=F          |  17.3 |   Yes    | —               | 20d down -11.6%; below MA20 by 7.2%; RSI14=27 |
|   24 | Wheat / ZW=F           |  16.1 |   Yes    | —               | 20d down -10.6%; below MA20 by 7.4%; RSI14=6  |
|   25 | Platinum / PL=F        |  15.2 |   Yes    | —               | 20d down -10.7%; below MA20 by 6.4%; RSI14=28 |
|   29 | WTI Crude Oil / CL=F   |  59.4 |    No    | malformed_input | Suppressed: malformed_input                   |
|   30 | Copper / HG=F          |  54.9 |    No    | malformed_input | Suppressed: malformed_input                   |
|   33 | Natural Gas / NG=F     |   9.4 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                    |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | ---------------------------------------------- |
|    1 | Tesla Inc. / TSLA                                                              |  78.2 |   Yes    | —                             | 20d up +9.6%; above MA20 by 5.4%; RSI14=55     |
|    4 | Microsoft Corporation / MSFT                                                   |  72.1 |   Yes    | —                             | 20d up +4.6%; above MA20 by 0.9%; RSI14=52     |
|    6 | Apple Inc. / AAPL                                                              |  70.3 |   Yes    | —                             | 20d up +1.6%; above MA20 by 1.4%; RSI14=64     |
|    9 | UnitedHealth Group Inc. / UNH                                                  |  60.3 |   Yes    | —                             | 20d up +8.7%; above MA20 by 5.1%; RSI14=69     |
|   10 | JPMorgan Chase & Co. / JPM                                                     |  59.1 |   Yes    | —                             | 20d down -0.3%; above MA20 by 0.3%; RSI14=54   |
|   15 | NVIDIA Corporation / NVDA                                                      |  45.5 |   Yes    | —                             | 20d down -5.6%; below MA20 by 4.0%; RSI14=29   |
|   17 | Amazon.com Inc. / AMZN                                                         |  39.4 |   Yes    | —                             | 20d up +1.2%; below MA20 by 2.2%; RSI14=44     |
|   22 | Alphabet Inc. Class A / GOOGL                                                  |  16.7 |   Yes    | —                             | 20d down -7.6%; below MA20 by 7.3%; RSI14=23   |
|   23 | Meta Platforms Inc. / META                                                     |  16.1 |   Yes    | —                             | 20d down -11.9%; below MA20 by 11.6%; RSI14=23 |
|   26 | Exxon Mobil Corporation / XOM                                                  |  85.5 |    No    | malformed_input               | Suppressed: malformed_input                    |
|   27 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  80.0 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   28 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  70.6 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   32 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  24.6 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    3 | Dow Jones Industrial Average / ^DJI |  72.4 |   Yes    | —            | 20d up +1.7%; above MA20 by 1.2%; RSI14=61   |
|    5 | FTSE 100 / ^FTSE                    |  71.5 |   Yes    | —            | 20d up +0.8%; above MA20 by 1.2%; RSI14=63   |
|    7 | DAX / ^GDAXI                        |  67.3 |   Yes    | —            | 20d up +0.1%; above MA20 by 0.5%; RSI14=49   |
|    8 | S&P 500 / ^GSPC                     |  63.6 |   Yes    | —            | 20d down -0.1%; below MA20 by 0.7%; RSI14=38 |
|   11 | Russell 2000 / ^RUT                 |  53.6 |   Yes    | —            | 20d down -1.1%; below MA20 by 0.0%; RSI14=43 |
|   12 | CAC 40 / ^FCHI                      |  53.0 |   Yes    | —            | 20d down -2.9%; below MA20 by 0.2%; RSI14=49 |
|   13 | Euro Stoxx 50 / ^STOXX50E           |  51.8 |   Yes    | —            | 20d down -2.9%; below MA20 by 1.1%; RSI14=39 |
|   14 | NASDAQ 100 / ^NDX                   |  50.0 |   Yes    | —            | 20d down -3.3%; below MA20 by 3.0%; RSI14=27 |
|   19 | Hang Seng / ^HSI                    |  33.3 |   Yes    | —            | 20d down -6.3%; below MA20 by 3.4%; RSI14=37 |
|   31 | Nikkei 225 / ^N225                  |  26.1 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-10-26 |
| 7203.T    | 2026-10-26 |
| 8306.T    | 2026-10-26 |
| AAPL      | 2026-10-26 |
| AMZN      | 2026-10-26 |
| BZ=F      | 2026-10-26 |
| CL=F      | 2026-10-26 |
| GC=F      | 2026-10-26 |
| GOOGL     | 2026-10-26 |
| HG=F      | 2026-10-26 |
| JPM       | 2026-10-26 |
| META      | 2026-10-26 |
| MSFT      | 2026-10-26 |
| NG=F      | 2026-10-26 |
| NVDA      | 2026-10-26 |
| PL=F      | 2026-10-26 |
| SI=F      | 2026-10-26 |
| TSLA      | 2026-10-26 |
| UNH       | 2026-10-26 |
| XOM       | 2026-10-26 |
| ZC=F      | 2026-10-26 |
| ZS=F      | 2026-10-26 |
| ZW=F      | 2026-10-26 |
| ^DJI      | 2026-10-26 |
| ^FCHI     | 2026-10-26 |
| ^FTSE     | 2026-10-26 |
| ^GDAXI    | 2026-10-26 |
| ^GSPC     | 2026-10-26 |
| ^HSI      | 2026-10-26 |
| ^N225     | 2026-10-26 |
| ^NDX      | 2026-10-26 |
| ^RUT      | 2026-10-26 |
| ^STOXX50E | 2026-10-26 |

## Symbol Details

### Tesla Inc. / TSLA (score 78.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +5.2% |
| ret_5d     |  +6.4% |
| ret_20d    |  +9.6% |
| ret_60d    | +25.8% |
| ma20_dist  |  +5.4% |
| ma50_dist  |  +7.4% |
| vol_20d    |  36.8% |
| mdd_60d    |   7.3% |
| rsi_14     |   55.1 |
| zscore_20d |    1.9 |

### Brent Crude Oil / BZ=F (score 77.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.8% |
| ret_5d     |  +5.7% |
| ret_20d    | +10.0% |
| ret_60d    | +40.4% |
| ma20_dist  |  +8.9% |
| ma50_dist  | +14.1% |
| vol_20d    |  29.6% |
| mdd_60d    |   8.7% |
| rsi_14     |   84.4 |
| zscore_20d |    2.0 |

### Dow Jones Industrial Average / ^DJI (score 72.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +0.8% |
| ret_20d    | +1.7% |
| ret_60d    | -0.2% |
| ma20_dist  | +1.2% |
| ma50_dist  | +0.1% |
| vol_20d    |  9.4% |
| mdd_60d    |  6.3% |
| rsi_14     |  61.3 |
| zscore_20d |   1.0 |

### Microsoft Corporation / MSFT (score 72.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.5% |
| ret_5d     |  -0.2% |
| ret_20d    |  +4.6% |
| ret_60d    | +14.8% |
| ma20_dist  |  +0.9% |
| ma50_dist  |  +4.6% |
| vol_20d    |  19.1% |
| mdd_60d    |   5.1% |
| rsi_14     |   51.9 |
| zscore_20d |    0.5 |

### FTSE 100 / ^FTSE (score 71.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | +0.0% |
| ret_20d    | +0.8% |
| ret_60d    | -0.9% |
| ma20_dist  | +1.2% |
| ma50_dist  | +0.6% |
| vol_20d    | 11.2% |
| mdd_60d    |  4.3% |
| rsi_14     |  63.1 |
| zscore_20d |   0.9 |

### Apple Inc. / AAPL (score 70.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.1% |
| ret_5d     |  +0.3% |
| ret_20d    |  +1.6% |
| ret_60d    | +11.4% |
| ma20_dist  |  +1.4% |
| ma50_dist  |  +4.1% |
| vol_20d    |  16.2% |
| mdd_60d    |   3.9% |
| rsi_14     |   64.2 |
| zscore_20d |    0.9 |

### DAX / ^GDAXI (score 67.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | +0.4% |
| ret_20d    | +0.1% |
| ret_60d    | -2.3% |
| ma20_dist  | +0.5% |
| ma50_dist  | -0.7% |
| vol_20d    | 14.0% |
| mdd_60d    |  6.6% |
| rsi_14     |  49.3 |
| zscore_20d |   0.7 |

### S&P 500 / ^GSPC (score 63.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | -0.2% |
| ret_20d    | -0.1% |
| ret_60d    | +2.5% |
| ma20_dist  | -0.7% |
| ma50_dist  | -0.3% |
| vol_20d    |  9.6% |
| mdd_60d    |  3.2% |
| rsi_14     |  37.9 |
| zscore_20d |  -0.8 |

### UnitedHealth Group Inc. / UNH (score 60.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.8% |
| ret_5d     | +0.9% |
| ret_20d    | +8.7% |
| ret_60d    | -0.9% |
| ma20_dist  | +5.1% |
| ma50_dist  | +5.9% |
| vol_20d    | 29.3% |
| mdd_60d    | 12.1% |
| rsi_14     |  68.7 |
| zscore_20d |   1.0 |

### JPMorgan Chase & Co. / JPM (score 59.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | +0.2% |
| ret_20d    | -0.3% |
| ret_60d    | -5.0% |
| ma20_dist  | +0.3% |
| ma50_dist  | -2.9% |
| vol_20d    | 13.0% |
| mdd_60d    |  9.9% |
| rsi_14     |  54.0 |
| zscore_20d |   0.3 |

### Russell 2000 / ^RUT (score 53.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | +2.1% |
| ret_20d    | -1.1% |
| ret_60d    | -4.9% |
| ma20_dist  | -0.0% |
| ma50_dist  | -3.1% |
| vol_20d    | 14.0% |
| mdd_60d    | 11.3% |
| rsi_14     |  42.5 |
| zscore_20d |  -0.0 |

### CAC 40 / ^FCHI (score 53.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.8% |
| ret_5d     | -0.3% |
| ret_20d    | -2.9% |
| ret_60d    | -8.9% |
| ma20_dist  | -0.2% |
| ma50_dist  | -3.1% |
| vol_20d    | 13.2% |
| mdd_60d    | 11.4% |
| rsi_14     |  48.9 |
| zscore_20d |  -0.2 |

### Euro Stoxx 50 / ^STOXX50E (score 51.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.8% |
| ret_5d     | -0.5% |
| ret_20d    | -2.9% |
| ret_60d    | -4.8% |
| ma20_dist  | -1.1% |
| ma50_dist  | -2.8% |
| vol_20d    | 14.2% |
| mdd_60d    |  7.4% |
| rsi_14     |  38.7 |
| zscore_20d |  -1.1 |

### NASDAQ 100 / ^NDX (score 50.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | -0.9% |
| ret_20d    | -3.3% |
| ret_60d    | +3.5% |
| ma20_dist  | -3.0% |
| ma50_dist  | -1.8% |
| vol_20d    | 18.5% |
| mdd_60d    |  7.3% |
| rsi_14     |  27.0 |
| zscore_20d |  -1.2 |

### NVIDIA Corporation / NVDA (score 45.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.4% |
| ret_5d     | -0.5% |
| ret_20d    | -5.6% |
| ret_60d    | +7.6% |
| ma20_dist  | -4.0% |
| ma50_dist  | -2.8% |
| vol_20d    | 29.3% |
| mdd_60d    | 11.8% |
| rsi_14     |  28.7 |
| zscore_20d |  -1.0 |

### Soybeans / ZS=F (score 44.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.2% |
| ret_5d     | -1.0% |
| ret_20d    | -3.6% |
| ret_60d    | +7.8% |
| ma20_dist  | -2.6% |
| ma50_dist  | -2.9% |
| vol_20d    | 10.6% |
| mdd_60d    |  6.5% |
| rsi_14     |  16.9 |
| zscore_20d |  -1.7 |

### Amazon.com Inc. / AMZN (score 39.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | -5.1% |
| ret_20d    | +1.2% |
| ret_60d    | -8.3% |
| ma20_dist  | -2.2% |
| ma50_dist  | -2.5% |
| vol_20d    | 31.6% |
| mdd_60d    | 13.4% |
| rsi_14     |  44.0 |
| zscore_20d |  -1.0 |

### Gold / GC=F (score 38.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.8% |
| ret_5d     | -2.9% |
| ret_20d    | -3.1% |
| ret_60d    | -4.8% |
| ma20_dist  | -2.7% |
| ma50_dist  | -6.9% |
| vol_20d    | 14.9% |
| mdd_60d    | 14.8% |
| rsi_14     |  35.8 |
| zscore_20d |  -2.1 |

### Hang Seng / ^HSI (score 33.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.5% |
| ret_5d     |  -4.0% |
| ret_20d    |  -6.3% |
| ret_60d    | -10.2% |
| ma20_dist  |  -3.4% |
| ma50_dist  |  -6.2% |
| vol_20d    |  18.5% |
| mdd_60d    |  11.8% |
| rsi_14     |   37.2 |
| zscore_20d |   -1.7 |

### Corn / ZC=F (score 26.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.2% |
| ret_5d     |  -2.6% |
| ret_20d    | -13.0% |
| ret_60d    |  +4.2% |
| ma20_dist  |  -5.9% |
| ma50_dist  |  -9.3% |
| vol_20d    |  21.8% |
| mdd_60d    |  16.2% |
| rsi_14     |    7.3 |
| zscore_20d |   -1.5 |

### Silver / SI=F (score 17.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.7% |
| ret_5d     |  -5.0% |
| ret_20d    | -11.6% |
| ret_60d    | -11.9% |
| ma20_dist  |  -7.2% |
| ma50_dist  | -14.0% |
| vol_20d    |  33.1% |
| mdd_60d    |  22.7% |
| rsi_14     |   27.1 |
| zscore_20d |   -1.8 |

### Alphabet Inc. Class A / GOOGL (score 16.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.1% |
| ret_5d     |  -8.0% |
| ret_20d    |  -7.6% |
| ret_60d    | -11.0% |
| ma20_dist  |  -7.3% |
| ma50_dist  |  -7.4% |
| vol_20d    |  20.5% |
| mdd_60d    |  16.1% |
| rsi_14     |   23.3 |
| zscore_20d |   -2.4 |

### Meta Platforms Inc. / META (score 16.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.9% |
| ret_5d     | -10.6% |
| ret_20d    | -11.9% |
| ret_60d    | +13.3% |
| ma20_dist  | -11.6% |
| ma50_dist  |  -5.1% |
| vol_20d    |  38.1% |
| mdd_60d    |  18.9% |
| rsi_14     |   23.3 |
| zscore_20d |   -2.4 |

### Wheat / ZW=F (score 16.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.4% |
| ret_5d     |  -6.0% |
| ret_20d    | -10.6% |
| ret_60d    |  -4.1% |
| ma20_dist  |  -7.4% |
| ma50_dist  | -11.5% |
| vol_20d    |  19.7% |
| mdd_60d    |  19.7% |
| rsi_14     |    5.5 |
| zscore_20d |   -2.0 |

### Platinum / PL=F (score 15.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.1% |
| ret_5d     |  -6.2% |
| ret_20d    | -10.7% |
| ret_60d    | -11.1% |
| ma20_dist  |  -6.4% |
| ma50_dist  | -11.9% |
| vol_20d    |  27.7% |
| mdd_60d    |  19.7% |
| rsi_14     |   28.0 |
| zscore_20d |   -2.1 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Tesla Inc. / TSLA                   |  13.1471 |           3.4% |                 0.27x |       26.2943 |            6.7% |
| Brent Crude Oil / BZ=F              |   3.9257 |           3.4% |                 0.34x |        7.8514 |            6.8% |
| Dow Jones Industrial Average / ^DJI | 533.4799 |           1.0% |                 1.07x |     1066.9598 |            2.0% |
| Microsoft Corporation / MSFT        |  11.1157 |           2.1% |                 0.52x |       22.2314 |            4.2% |
| FTSE 100 / ^FTSE                    | 111.9429 |           1.0% |                 0.89x |      223.8857 |            2.1% |
| Apple Inc. / AAPL                   |   6.3950 |           1.9% |                 0.62x |       12.7900 |            3.7% |
| DAX / ^GDAXI                        | 326.3527 |           1.3% |                 0.71x |      652.7054 |            2.6% |
| S&P 500 / ^GSPC                     |  72.7565 |           0.9% |                 1.04x |      145.5130 |            1.9% |
| UnitedHealth Group Inc. / UNH       |  13.4979 |           3.3% |                 0.34x |       26.9957 |            6.6% |
| JPMorgan Chase & Co. / JPM          |   6.5036 |           1.9% |                 0.77x |       13.0071 |            3.9% |
| Russell 2000 / ^RUT                 |  33.8764 |           1.2% |                 0.71x |       67.7528 |            2.4% |
| CAC 40 / ^FCHI                      |  89.8600 |           1.1% |                 0.76x |      179.7201 |            2.3% |
| Euro Stoxx 50 / ^STOXX50E           |  78.6658 |           1.3% |                 0.71x |      157.3315 |            2.6% |
| NASDAQ 100 / ^NDX                   | 510.0746 |           1.7% |                 0.54x |     1020.1493 |            3.5% |
| NVIDIA Corporation / NVDA           |   6.1436 |           2.8% |                 0.34x |       12.2871 |            5.7% |
| Soybeans / ZS=F                     |  17.5357 |           1.4% |                 0.94x |       35.0714 |            2.8% |
| Amazon.com Inc. / AMZN              |   6.9393 |           2.8% |                 0.32x |       13.8786 |            5.6% |
| Gold / GC=F                         |  69.8500 |           1.7% |                 0.67x |      139.6999 |            3.5% |
| Hang Seng / ^HSI                    | 386.1789 |           1.7% |                 0.54x |      772.3577 |            3.3% |
| Corn / ZC=F                         |   9.6250 |           2.1% |                 0.46x |       19.2500 |            4.2% |
| Silver / SI=F                       |   1.2234 |           2.3% |                 0.30x |        2.4469 |            4.5% |
| Alphabet Inc. Class A / GOOGL       |   8.4214 |           2.7% |                 0.49x |       16.8429 |            5.3% |
| Meta Platforms Inc. / META          |  25.9250 |           4.1% |                 0.26x |       51.8500 |            8.2% |
| Wheat / ZW=F                        |  15.2143 |           2.5% |                 0.51x |       30.4286 |            4.9% |
| Platinum / PL=F                     |  28.1143 |           1.8% |                 0.36x |       56.2286 |            3.7% |

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

Scoring engine version: **1.0.0** | Git commit: **3597f45**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
