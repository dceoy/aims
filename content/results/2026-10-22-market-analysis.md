+++
title = "Market Analysis 2026-10-22"
date = "2026-10-22T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: TSLA (score 76.4)."
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
source_files = ["data/analysis/2026-10-22.json", "data/history/2026-10-22.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "f104fbe"
+++

## Market Regime

**Neutral** — 12 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Tesla Inc. / TSLA** — score 76.4, 20d return +1.7%, RSI14=66. 20d up +1.7%; above MA20 by 4.4%; RSI14=66 ⚠️ Upcoming: FOMC rate decision (2026-10-28)
- **Dow Jones Industrial Average / ^DJI** — score 75.8, 20d return +2.6%, RSI14=78. 20d up +2.6%; above MA20 by 2.4%; RSI14=78 ⚠️ Upcoming: FOMC rate decision (2026-10-28)
- **Brent Crude Oil / BZ=F** — score 71.2, 20d return +5.6%, RSI14=71. 20d up +5.6%; above MA20 by 3.7%; RSI14=71 ⚠️ Upcoming: FOMC rate decision (2026-10-28)
- **DAX / ^GDAXI** — score 69.1, 20d return +0.9%, RSI14=63. 20d up +0.9%; above MA20 by 1.4%; RSI14=63 ⚠️ Upcoming: FOMC rate decision (2026-10-28); ECB monetary policy decision (2026-10-29)
- **Microsoft Corporation / MSFT** — score 67.3, 20d return +6.5%, RSI14=63. 20d up +6.5%; above MA20 by 1.5%; RSI14=63 ⚠️ Upcoming: FOMC rate decision (2026-10-28); MSFT earnings release (2026-10-28)

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                        | Applies To                      |
| ---------- | ---------------------------- | ------------------------------- |
| 2026-10-28 | FOMC rate decision           | Commodity, Equity, Equity Index |
| 2026-10-28 | GOOGL earnings release       | GOOGL                           |
| 2026-10-28 | MSFT earnings release        | MSFT                            |
| 2026-10-29 | AMZN earnings release        | AMZN                            |
| 2026-10-29 | ECB monetary policy decision | ^FCHI, ^GDAXI, ^STOXX50E        |

## Signal History

Compared with the previous available report (**2026-10-21**).

- **New top-5:** TSLA, ^GDAXI
- **Persistent top signals:** MSFT (19 reports), BZ=F (4 reports), ^DJI (2 reports)
- **Dropped from top-5:** UNH, ^FTSE

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +1 |    +5.2 |
| 7203.T    |     +0 |    -6.1 |
| 8306.T    |     +1 |   +16.1 |
| AAPL      |     +4 |    +9.4 |
| AMZN      |     -3 |    -3.3 |
| BZ=F      |     +0 |    +0.0 |
| CL=F      |     +0 |   -11.2 |
| GC=F      |     +1 |    +3.9 |
| GOOGL     |     -3 |    -8.2 |
| HG=F      |     +0 |    -9.7 |
| JPM       |     -6 |   -11.8 |
| META      |     +3 |    +5.2 |
| MSFT      |     -1 |    -2.1 |
| NG=F      |     -2 |   -22.4 |
| NVDA      |     +6 |   +15.8 |
| PL=F      |     +0 |    -5.8 |
| SI=F      |     +0 |    -3.6 |
| TSLA      |     +5 |   +11.2 |
| UNH       |     -6 |   -10.0 |
| XOM       |     -1 |    -3.6 |
| ZC=F      |     +0 |    +5.5 |
| ZS=F      |     -2 |    +0.0 |
| ZW=F      |     +0 |    -3.6 |
| ^DJI      |     -1 |    -2.4 |
| ^FCHI     |     +1 |    +7.6 |
| ^FTSE     |     -4 |    -4.5 |
| ^GDAXI    |     +6 |   +11.8 |
| ^GSPC     |     +2 |    +1.5 |
| ^HSI      |     -2 |    -6.4 |
| ^N225     |     +1 |    +3.3 |
| ^NDX      |     +1 |    +7.9 |
| ^RUT      |     -4 |    -1.8 |
| ^STOXX50E |     +3 |   +12.7 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
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
|    3 | Brent Crude Oil / BZ=F |  71.2 |   Yes    | —               | 20d up +5.6%; above MA20 by 3.7%; RSI14=71    |
|   17 | Gold / GC=F            |  40.6 |   Yes    | —               | 20d down -3.9%; below MA20 by 0.8%; RSI14=44  |
|   18 | Soybeans / ZS=F        |  39.7 |   Yes    | —               | 20d down -5.5%; below MA20 by 2.9%; RSI14=30  |
|   21 | Platinum / PL=F        |  26.1 |   Yes    | —               | 20d down -6.9%; below MA20 by 2.8%; RSI14=38  |
|   23 | Silver / SI=F          |  22.4 |   Yes    | —               | 20d down -10.8%; below MA20 by 3.7%; RSI14=38 |
|   24 | Corn / ZC=F            |  21.8 |   Yes    | —               | 20d down -12.4%; below MA20 by 6.2%; RSI14=22 |
|   25 | Wheat / ZW=F           |   9.4 |   Yes    | —               | 20d down -11.3%; below MA20 by 7.2%; RSI14=25 |
|   29 | WTI Crude Oil / CL=F   |  54.2 |    No    | malformed_input | Suppressed: malformed_input                   |
|   30 | Copper / HG=F          |  45.8 |    No    | malformed_input | Suppressed: malformed_input                   |
|   33 | Natural Gas / NG=F     |  10.9 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    1 | Tesla Inc. / TSLA                                                              |  76.4 |   Yes    | —                             | 20d up +1.7%; above MA20 by 4.4%; RSI14=66   |
|    5 | Microsoft Corporation / MSFT                                                   |  67.3 |   Yes    | —                             | 20d up +6.5%; above MA20 by 1.5%; RSI14=63   |
|    7 | Apple Inc. / AAPL                                                              |  65.8 |   Yes    | —                             | 20d up +2.1%; above MA20 by 1.8%; RSI14=71   |
|    8 | UnitedHealth Group Inc. / UNH                                                  |  65.8 |   Yes    | —                             | 20d up +12.3%; above MA20 by 8.4%; RSI14=80  |
|   10 | Amazon.com Inc. / AMZN                                                         |  61.5 |   Yes    | —                             | 20d up +5.3%; above MA20 by 3.1%; RSI14=63   |
|   13 | NVIDIA Corporation / NVDA                                                      |  48.5 |   Yes    | —                             | 20d down -1.6%; below MA20 by 2.2%; RSI14=41 |
|   15 | JPMorgan Chase & Co. / JPM                                                     |  45.8 |   Yes    | —                             | 20d down -0.2%; above MA20 by 0.4%; RSI14=57 |
|   19 | Meta Platforms Inc. / META                                                     |  34.9 |   Yes    | —                             | 20d down -6.3%; below MA20 by 4.4%; RSI14=41 |
|   20 | Alphabet Inc. Class A / GOOGL                                                  |  29.4 |   Yes    | —                             | 20d down -0.9%; below MA20 by 3.0%; RSI14=46 |
|   26 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  80.6 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   27 | Exxon Mobil Corporation / XOM                                                  |  77.6 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   28 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  66.1 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   32 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  25.8 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    2 | Dow Jones Industrial Average / ^DJI |  75.8 |   Yes    | —            | 20d up +2.6%; above MA20 by 2.4%; RSI14=78   |
|    4 | DAX / ^GDAXI                        |  69.1 |   Yes    | —            | 20d up +0.9%; above MA20 by 1.4%; RSI14=63   |
|    6 | S&P 500 / ^GSPC                     |  66.1 |   Yes    | —            | 20d up +0.7%; above MA20 by 0.3%; RSI14=58   |
|    9 | FTSE 100 / ^FTSE                    |  61.8 |   Yes    | —            | 20d up +0.4%; above MA20 by 1.1%; RSI14=69   |
|   11 | Euro Stoxx 50 / ^STOXX50E           |  55.1 |   Yes    | —            | 20d down -1.5%; below MA20 by 0.1%; RSI14=53 |
|   12 | NASDAQ 100 / ^NDX                   |  50.6 |   Yes    | —            | 20d down -2.1%; below MA20 by 1.8%; RSI14=41 |
|   14 | CAC 40 / ^FCHI                      |  48.5 |   Yes    | —            | 20d down -2.5%; above MA20 by 0.3%; RSI14=56 |
|   16 | Russell 2000 / ^RUT                 |  44.9 |   Yes    | —            | 20d down -2.0%; below MA20 by 0.5%; RSI14=46 |
|   22 | Hang Seng / ^HSI                    |  25.8 |   Yes    | —            | 20d down -5.6%; below MA20 by 2.7%; RSI14=36 |
|   31 | Nikkei 225 / ^N225                  |  35.1 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-10-21 |
| 7203.T    | 2026-10-21 |
| 8306.T    | 2026-10-21 |
| AAPL      | 2026-10-21 |
| AMZN      | 2026-10-21 |
| BZ=F      | 2026-10-21 |
| CL=F      | 2026-10-21 |
| GC=F      | 2026-10-21 |
| GOOGL     | 2026-10-21 |
| HG=F      | 2026-10-21 |
| JPM       | 2026-10-21 |
| META      | 2026-10-21 |
| MSFT      | 2026-10-21 |
| NG=F      | 2026-10-21 |
| NVDA      | 2026-10-21 |
| PL=F      | 2026-10-21 |
| SI=F      | 2026-10-21 |
| TSLA      | 2026-10-21 |
| UNH       | 2026-10-21 |
| XOM       | 2026-10-21 |
| ZC=F      | 2026-10-21 |
| ZS=F      | 2026-10-21 |
| ZW=F      | 2026-10-21 |
| ^DJI      | 2026-10-21 |
| ^FCHI     | 2026-10-21 |
| ^FTSE     | 2026-10-21 |
| ^GDAXI    | 2026-10-21 |
| ^GSPC     | 2026-10-21 |
| ^HSI      | 2026-10-21 |
| ^N225     | 2026-10-21 |
| ^NDX      | 2026-10-21 |
| ^RUT      | 2026-10-21 |
| ^STOXX50E | 2026-10-21 |

## Symbol Details

### Tesla Inc. / TSLA (score 76.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +3.4% |
| ret_5d     |  +5.3% |
| ret_20d    |  +1.7% |
| ret_60d    | +25.7% |
| ma20_dist  |  +4.4% |
| ma50_dist  |  +6.7% |
| vol_20d    |  34.3% |
| mdd_60d    |   7.3% |
| rsi_14     |   66.2 |
| zscore_20d |    1.6 |

### Dow Jones Industrial Average / ^DJI (score 75.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | +2.4% |
| ret_20d    | +2.6% |
| ret_60d    | +0.2% |
| ma20_dist  | +2.4% |
| ma50_dist  | +0.9% |
| vol_20d    |  9.1% |
| mdd_60d    |  6.3% |
| rsi_14     |  77.6 |
| zscore_20d |   2.5 |

### Brent Crude Oil / BZ=F (score 71.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.0% |
| ret_5d     |  +2.6% |
| ret_20d    |  +5.6% |
| ret_60d    | +29.9% |
| ma20_dist  |  +3.7% |
| ma50_dist  |  +8.8% |
| vol_20d    |  28.3% |
| mdd_60d    |   8.7% |
| rsi_14     |   70.9 |
| zscore_20d |    1.3 |

### DAX / ^GDAXI (score 69.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.3% |
| ret_5d     | +1.4% |
| ret_20d    | +0.9% |
| ret_60d    | +0.7% |
| ma20_dist  | +1.4% |
| ma50_dist  | -0.1% |
| vol_20d    | 13.1% |
| mdd_60d    |  6.6% |
| rsi_14     |  63.3 |
| zscore_20d |   1.9 |

### Microsoft Corporation / MSFT (score 67.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.2% |
| ret_5d     |  -0.1% |
| ret_20d    |  +6.5% |
| ret_60d    | +35.7% |
| ma20_dist  |  +1.5% |
| ma50_dist  |  +5.1% |
| vol_20d    |  21.2% |
| mdd_60d    |   5.1% |
| rsi_14     |   62.9 |
| zscore_20d |    0.6 |

### S&P 500 / ^GSPC (score 66.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | +0.5% |
| ret_20d    | +0.7% |
| ret_60d    | +4.4% |
| ma20_dist  | +0.3% |
| ma50_dist  | +0.7% |
| vol_20d    |  8.7% |
| mdd_60d    |  3.2% |
| rsi_14     |  58.2 |
| zscore_20d |   0.4 |

### Apple Inc. / AAPL (score 65.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.3% |
| ret_5d     | +0.3% |
| ret_20d    | +2.1% |
| ret_60d    | +1.2% |
| ma20_dist  | +1.8% |
| ma50_dist  | +5.0% |
| vol_20d    | 16.3% |
| mdd_60d    | 10.6% |
| rsi_14     |  70.9 |
| zscore_20d |   1.4 |

### UnitedHealth Group Inc. / UNH (score 65.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.5% |
| ret_5d     |  +5.4% |
| ret_20d    | +12.3% |
| ret_60d    |  -2.7% |
| ma20_dist  |  +8.4% |
| ma50_dist  |  +7.8% |
| vol_20d    |  26.7% |
| mdd_60d    |  13.4% |
| rsi_14     |   80.4 |
| zscore_20d |    2.0 |

### FTSE 100 / ^FTSE (score 61.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | +0.3% |
| ret_20d    | +0.4% |
| ret_60d    | -1.1% |
| ma20_dist  | +1.1% |
| ma50_dist  | +0.4% |
| vol_20d    | 10.9% |
| mdd_60d    |  4.4% |
| rsi_14     |  69.4 |
| zscore_20d |   0.9 |

### Amazon.com Inc. / AMZN (score 61.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.1% |
| ret_5d     |  +3.3% |
| ret_20d    |  +5.3% |
| ret_60d    | +13.6% |
| ma20_dist  |  +3.1% |
| ma50_dist  |  +2.4% |
| vol_20d    |  27.0% |
| mdd_60d    |  13.4% |
| rsi_14     |   63.4 |
| zscore_20d |    1.4 |

### Euro Stoxx 50 / ^STOXX50E (score 55.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.4% |
| ret_5d     | +0.3% |
| ret_20d    | -1.5% |
| ret_60d    | -0.7% |
| ma20_dist  | -0.1% |
| ma50_dist  | -1.7% |
| vol_20d    | 12.4% |
| mdd_60d    |  6.6% |
| rsi_14     |  52.7 |
| zscore_20d |  -0.1 |

### NASDAQ 100 / ^NDX (score 50.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | -0.4% |
| ret_20d    | -2.1% |
| ret_60d    | +7.4% |
| ma20_dist  | -1.8% |
| ma50_dist  | -0.2% |
| vol_20d    | 15.5% |
| mdd_60d    |  6.5% |
| rsi_14     |  41.0 |
| zscore_20d |  -1.0 |

### NVIDIA Corporation / NVDA (score 48.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.5% |
| ret_5d     |  +0.3% |
| ret_20d    |  -1.6% |
| ret_60d    | +12.7% |
| ma20_dist  |  -2.2% |
| ma50_dist  |  -0.4% |
| vol_20d    |  24.4% |
| mdd_60d    |  10.5% |
| rsi_14     |   40.5 |
| zscore_20d |   -0.7 |

### CAC 40 / ^FCHI (score 48.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | +0.6% |
| ret_20d    | -2.5% |
| ret_60d    | -5.8% |
| ma20_dist  | +0.3% |
| ma50_dist  | -2.8% |
| vol_20d    | 12.0% |
| mdd_60d    | 11.4% |
| rsi_14     |  55.9 |
| zscore_20d |   0.2 |

### JPMorgan Chase & Co. / JPM (score 45.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.0% |
| ret_5d     | -0.0% |
| ret_20d    | -0.2% |
| ret_60d    | -6.2% |
| ma20_dist  | +0.4% |
| ma50_dist  | -3.1% |
| vol_20d    | 14.2% |
| mdd_60d    |  9.9% |
| rsi_14     |  56.8 |
| zscore_20d |   0.5 |

### Russell 2000 / ^RUT (score 44.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +1.9% |
| ret_20d    | -2.0% |
| ret_60d    | -5.8% |
| ma20_dist  | -0.5% |
| ma50_dist  | -3.8% |
| vol_20d    | 14.1% |
| mdd_60d    | 11.3% |
| rsi_14     |  46.1 |
| zscore_20d |  -0.4 |

### Gold / GC=F (score 40.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | +1.0% |
| ret_20d    | -3.9% |
| ret_60d    | +2.9% |
| ma20_dist  | -0.8% |
| ma50_dist  | -4.9% |
| vol_20d    | 17.2% |
| mdd_60d    | 12.7% |
| rsi_14     |  43.9 |
| zscore_20d |  -0.7 |

### Soybeans / ZS=F (score 39.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | -2.5% |
| ret_20d    | -5.5% |
| ret_60d    | +6.2% |
| ma20_dist  | -2.9% |
| ma50_dist  | -2.3% |
| vol_20d    | 12.0% |
| mdd_60d    |  6.2% |
| rsi_14     |  30.1 |
| zscore_20d |  -1.9 |

### Meta Platforms Inc. / META (score 34.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.5% |
| ret_5d     |  -5.4% |
| ret_20d    |  -6.3% |
| ret_60d    | +17.5% |
| ma20_dist  |  -4.4% |
| ma50_dist  |  +5.5% |
| vol_20d    |  39.2% |
| mdd_60d    |  10.7% |
| rsi_14     |   40.8 |
| zscore_20d |   -1.6 |

### Alphabet Inc. Class A / GOOGL (score 29.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.6% |
| ret_5d     | -3.7% |
| ret_20d    | -0.9% |
| ret_60d    | +0.3% |
| ma20_dist  | -3.0% |
| ma50_dist  | -2.6% |
| vol_20d    | 18.1% |
| mdd_60d    | 12.4% |
| rsi_14     |  46.5 |
| zscore_20d |  -2.1 |

### Platinum / PL=F (score 26.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.3% |
| ret_5d     | +1.5% |
| ret_20d    | -6.9% |
| ret_60d    | +0.5% |
| ma20_dist  | -2.8% |
| ma50_dist  | -7.5% |
| vol_20d    | 27.8% |
| mdd_60d    | 16.4% |
| rsi_14     |  37.7 |
| zscore_20d |  -1.0 |

### Hang Seng / ^HSI (score 25.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.9% |
| ret_5d     | -2.8% |
| ret_20d    | -5.6% |
| ret_60d    | -6.2% |
| ma20_dist  | -2.7% |
| ma50_dist  | -5.0% |
| vol_20d    | 15.4% |
| mdd_60d    |  9.1% |
| rsi_14     |  35.6 |
| zscore_20d |  -1.8 |

### Silver / SI=F (score 22.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.5% |
| ret_5d     |  +3.4% |
| ret_20d    | -10.8% |
| ret_60d    |  -0.4% |
| ma20_dist  |  -3.7% |
| ma50_dist  |  -9.7% |
| vol_20d    |  33.3% |
| mdd_60d    |  20.0% |
| rsi_14     |   37.5 |
| zscore_20d |   -1.0 |

### Corn / ZC=F (score 21.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.3% |
| ret_5d     |  -3.6% |
| ret_20d    | -12.4% |
| ret_60d    |  +5.1% |
| ma20_dist  |  -6.2% |
| ma50_dist  |  -7.8% |
| vol_20d    |  21.9% |
| mdd_60d    |  14.9% |
| rsi_14     |   21.9 |
| zscore_20d |   -1.5 |

### Wheat / ZW=F (score 9.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.3% |
| ret_5d     |  -6.7% |
| ret_20d    | -11.3% |
| ret_60d    |  -1.7% |
| ma20_dist  |  -7.2% |
| ma50_dist  | -10.2% |
| vol_20d    |  20.1% |
| mdd_60d    |  18.1% |
| rsi_14     |   24.8 |
| zscore_20d |   -2.5 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Tesla Inc. / TSLA                   |  12.4136 |           3.2% |                 0.29x |       24.8271 |            6.4% |
| Dow Jones Industrial Average / ^DJI | 516.7134 |           1.0% |                 1.10x |     1033.4269 |            2.0% |
| Brent Crude Oil / BZ=F              |   3.9150 |           3.6% |                 0.35x |        7.8300 |            7.2% |
| DAX / ^GDAXI                        | 312.0918 |           1.2% |                 0.76x |      624.1836 |            2.4% |
| Microsoft Corporation / MSFT        |  11.1229 |           2.1% |                 0.47x |       22.2457 |            4.2% |
| S&P 500 / ^GSPC                     |  71.3850 |           0.9% |                 1.15x |      142.7700 |            1.8% |
| Apple Inc. / AAPL                   |   5.9507 |           1.7% |                 0.61x |       11.9014 |            3.5% |
| UnitedHealth Group Inc. / UNH       |  13.1457 |           3.2% |                 0.37x |       26.2914 |            6.3% |
| FTSE 100 / ^FTSE                    | 110.4285 |           1.0% |                 0.92x |      220.8570 |            2.1% |
| Amazon.com Inc. / AMZN              |   6.4693 |           2.5% |                 0.37x |       12.9386 |            4.9% |
| Euro Stoxx 50 / ^STOXX50E           |  74.0678 |           1.2% |                 0.81x |      148.1357 |            2.4% |
| NASDAQ 100 / ^NDX                   | 465.0889 |           1.6% |                 0.64x |      930.1777 |            3.1% |
| NVIDIA Corporation / NVDA           |   5.8914 |           2.7% |                 0.41x |       11.7829 |            5.3% |
| CAC 40 / ^FCHI                      |  87.7607 |           1.1% |                 0.83x |      175.5214 |            2.2% |
| JPMorgan Chase & Co. / JPM          |   6.1907 |           1.8% |                 0.71x |       12.3815 |            3.7% |
| Russell 2000 / ^RUT                 |  36.7321 |           1.3% |                 0.71x |       73.4643 |            2.6% |
| Gold / GC=F                         |  68.6714 |           1.7% |                 0.58x |      137.3428 |            3.3% |
| Soybeans / ZS=F                     |  17.7500 |           1.4% |                 0.83x |       35.5000 |            2.9% |
| Meta Platforms Inc. / META          |  22.5564 |           3.2% |                 0.25x |       45.1129 |            6.5% |
| Alphabet Inc. Class A / GOOGL       |   8.1100 |           2.4% |                 0.55x |       16.2200 |            4.8% |
| Platinum / PL=F                     |  30.6286 |           1.9% |                 0.36x |       61.2572 |            3.8% |
| Hang Seng / ^HSI                    | 372.4393 |           1.6% |                 0.65x |      744.8786 |            3.1% |
| Silver / SI=F                       |   1.1691 |           2.0% |                 0.30x |        2.3383 |            4.1% |
| Corn / ZC=F                         |  10.2321 |           2.2% |                 0.46x |       20.4643 |            4.4% |
| Wheat / ZW=F                        |  16.1786 |           2.6% |                 0.50x |       32.3571 |            5.2% |

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

Scoring engine version: **1.0.0** | Git commit: **f104fbe**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
