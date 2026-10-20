+++
title = "Market Analysis 2026-09-09"
date = "2026-09-09T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: ZS=F (score 78.8)."
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
source_files = ["data/analysis/2026-09-09.json", "data/history/2026-09-09.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "950c500"
+++

## Market Regime

**Neutral** — 12 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Soybeans / ZS=F** — score 78.8, 20d return +11.8%, RSI14=76. 20d up +11.8%; above MA20 by 4.8%; RSI14=76 ⚠️ Upcoming: FOMC rate decision (2026-09-16)
- **Brent Crude Oil / BZ=F** — score 75.8, 20d return +12.5%, RSI14=61. 20d up +12.5%; above MA20 by 6.1%; RSI14=61 ⚠️ Upcoming: FOMC rate decision (2026-09-16)
- **Corn / ZC=F** — score 65.5, 20d return +11.8%, RSI14=65. 20d up +11.8%; above MA20 by 3.3%; RSI14=65 ⚠️ Upcoming: FOMC rate decision (2026-09-16)
- **Meta Platforms Inc. / META** — score 63.9, 20d return +3.1%, RSI14=86. 20d up +3.1%; above MA20 by 6.2%; RSI14=86 ⚠️ Upcoming: FOMC rate decision (2026-09-16)
- **Platinum / PL=F** — score 63.6, 20d return +7.1%, RSI14=53. 20d up +7.1%; above MA20 by 1.7%; RSI14=53 ⚠️ Upcoming: FOMC rate decision (2026-09-16)

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                        | Applies To                      |
| ---------- | ---------------------------- | ------------------------------- |
| 2026-09-10 | ECB monetary policy decision | ^FCHI, ^GDAXI, ^STOXX50E        |
| 2026-09-16 | FOMC rate decision           | Commodity, Equity, Equity Index |

## Signal History

Compared with the previous available report (**2026-09-08**).

- **New top-5:** PL=F
- **Persistent top signals:** ZC=F (20 reports), ZS=F (13 reports), BZ=F (3 reports), META (3 reports)
- **Dropped from top-5:** NVDA

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +0 |   -13.6 |
| 7203.T    |     -1 |   -28.8 |
| 8306.T    |     +0 |    -5.8 |
| AAPL      |     -6 |    -4.8 |
| AMZN      |     +0 |    +0.3 |
| BZ=F      |     +0 |    +6.7 |
| CL=F      |     +0 |    +3.6 |
| GC=F      |     -7 |   -13.6 |
| GOOGL     |     +0 |    +8.5 |
| HG=F      |     +0 |   +10.3 |
| JPM       |     -8 |   -12.7 |
| META      |     -1 |    -4.5 |
| MSFT      |     -9 |    -5.8 |
| NG=F      |     -1 |    -8.5 |
| NVDA      |     -3 |   -11.5 |
| PL=F      |     +4 |   +11.5 |
| SI=F      |     -4 |    -6.7 |
| TSLA      |     +9 |   +16.1 |
| UNH       |     +9 |   +16.4 |
| XOM       |     +2 |    +7.0 |
| ZC=F      |     +1 |    -2.1 |
| ZS=F      |     +0 |    +4.2 |
| ZW=F      |     +6 |   +13.0 |
| ^DJI      |     -9 |    -9.4 |
| ^FCHI     |     +2 |    +7.0 |
| ^FTSE     |     -1 |    +6.1 |
| ^GDAXI    |     +9 |   +14.6 |
| ^GSPC     |     -1 |    -1.2 |
| ^HSI      |     +4 |    +6.4 |
| ^N225     |     +0 |   -17.0 |
| ^NDX      |     +1 |    +4.2 |
| ^RUT      |     -5 |    -2.4 |
| ^STOXX50E |     +9 |   +13.6 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **WTI Crude Oil / CL=F** — malformed_input
- **Copper / HG=F** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Natural Gas / NG=F** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Nikkei 225 / ^N225** — missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                 |
| ---: | ---------------------- | ----: | :------: | --------------- | ------------------------------------------- |
|    1 | Soybeans / ZS=F        |  78.8 |   Yes    | —               | 20d up +11.8%; above MA20 by 4.8%; RSI14=76 |
|    2 | Brent Crude Oil / BZ=F |  75.8 |   Yes    | —               | 20d up +12.5%; above MA20 by 6.1%; RSI14=61 |
|    3 | Corn / ZC=F            |  65.5 |   Yes    | —               | 20d up +11.8%; above MA20 by 3.3%; RSI14=65 |
|    5 | Platinum / PL=F        |  63.6 |   Yes    | —               | 20d up +7.1%; above MA20 by 1.7%; RSI14=53  |
|    6 | Wheat / ZW=F           |  63.3 |   Yes    | —               | 20d up +11.9%; above MA20 by 3.0%; RSI14=61 |
|   19 | Silver / SI=F          |  37.6 |   Yes    | —               | 20d up +2.2%; below MA20 by 0.8%; RSI14=44  |
|   20 | Gold / GC=F            |  36.4 |   Yes    | —               | 20d up +0.7%; below MA20 by 2.2%; RSI14=43  |
|   26 | WTI Crude Oil / CL=F   |  77.0 |    No    | malformed_input | Suppressed: malformed_input                 |
|   27 | Copper / HG=F          |  74.2 |    No    | malformed_input | Suppressed: malformed_input                 |
|   30 | Natural Gas / NG=F     |  48.8 |    No    | malformed_input | Suppressed: malformed_input                 |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    4 | Meta Platforms Inc. / META                                                     |  63.9 |   Yes    | —                             | 20d up +3.1%; above MA20 by 6.2%; RSI14=86   |
|    8 | NVIDIA Corporation / NVDA                                                      |  55.8 |   Yes    | —                             | 20d up +3.8%; above MA20 by 2.4%; RSI14=54   |
|    9 | Tesla Inc. / TSLA                                                              |  53.6 |   Yes    | —                             | 20d up +11.3%; above MA20 by 5.1%; RSI14=60  |
|   13 | UnitedHealth Group Inc. / UNH                                                  |  49.4 |   Yes    | —                             | 20d down -1.9%; above MA20 by 1.1%; RSI14=56 |
|   14 | Apple Inc. / AAPL                                                              |  48.5 |   Yes    | —                             | 20d up +2.6%; above MA20 by 0.9%; RSI14=56   |
|   16 | Microsoft Corporation / MSFT                                                   |  48.2 |   Yes    | —                             | 20d down -2.2%; below MA20 by 0.2%; RSI14=58 |
|   18 | JPMorgan Chase & Co. / JPM                                                     |  39.1 |   Yes    | —                             | 20d down -1.7%; below MA20 by 1.3%; RSI14=38 |
|   24 | Amazon.com Inc. / AMZN                                                         |  29.4 |   Yes    | —                             | 20d down -7.6%; below MA20 by 1.6%; RSI14=48 |
|   25 | Alphabet Inc. Class A / GOOGL                                                  |  23.9 |   Yes    | —                             | 20d down -5.3%; below MA20 by 1.2%; RSI14=44 |
|   28 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  53.3 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   29 | Exxon Mobil Corporation / XOM                                                  |  52.7 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   31 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  26.1 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   33 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  21.5 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    7 | FTSE 100 / ^FTSE                    |  60.3 |   Yes    | —            | 20d down -0.5%; above MA20 by 0.1%; RSI14=59 |
|   10 | DAX / ^GDAXI                        |  51.8 |   Yes    | —            | 20d down -1.5%; below MA20 by 0.6%; RSI14=48 |
|   11 | Euro Stoxx 50 / ^STOXX50E           |  50.9 |   Yes    | —            | 20d down -2.1%; below MA20 by 0.6%; RSI14=46 |
|   12 | S&P 500 / ^GSPC                     |  50.6 |   Yes    | —            | 20d down -1.0%; below MA20 by 0.4%; RSI14=48 |
|   15 | NASDAQ 100 / ^NDX                   |  48.5 |   Yes    | —            | 20d down -0.4%; above MA20 by 0.1%; RSI14=50 |
|   17 | Hang Seng / ^HSI                    |  41.8 |   Yes    | —            | 20d down -1.3%; below MA20 by 0.7%; RSI14=46 |
|   21 | CAC 40 / ^FCHI                      |  36.4 |   Yes    | —            | 20d down -4.6%; below MA20 by 1.4%; RSI14=33 |
|   22 | Russell 2000 / ^RUT                 |  36.1 |   Yes    | —            | 20d down -1.9%; below MA20 by 1.4%; RSI14=40 |
|   23 | Dow Jones Industrial Average / ^DJI |  35.5 |   Yes    | —            | 20d down -2.2%; below MA20 by 1.1%; RSI14=44 |
|   32 | Nikkei 225 / ^N225                  |  21.8 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-09-08 |
| 7203.T    | 2026-09-08 |
| 8306.T    | 2026-09-08 |
| AAPL      | 2026-09-08 |
| AMZN      | 2026-09-08 |
| BZ=F      | 2026-09-08 |
| CL=F      | 2026-09-08 |
| GC=F      | 2026-09-08 |
| GOOGL     | 2026-09-08 |
| HG=F      | 2026-09-08 |
| JPM       | 2026-09-08 |
| META      | 2026-09-08 |
| MSFT      | 2026-09-08 |
| NG=F      | 2026-09-08 |
| NVDA      | 2026-09-08 |
| PL=F      | 2026-09-08 |
| SI=F      | 2026-09-08 |
| TSLA      | 2026-09-08 |
| UNH       | 2026-09-08 |
| XOM       | 2026-09-08 |
| ZC=F      | 2026-09-08 |
| ZS=F      | 2026-09-08 |
| ZW=F      | 2026-09-08 |
| ^DJI      | 2026-09-08 |
| ^FCHI     | 2026-09-08 |
| ^FTSE     | 2026-09-08 |
| ^GDAXI    | 2026-09-08 |
| ^GSPC     | 2026-09-08 |
| ^HSI      | 2026-09-08 |
| ^N225     | 2026-09-08 |
| ^NDX      | 2026-09-08 |
| ^RUT      | 2026-09-08 |
| ^STOXX50E | 2026-09-08 |

## Symbol Details

### Soybeans / ZS=F (score 78.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.7% |
| ret_5d     |  +2.1% |
| ret_20d    | +11.8% |
| ret_60d    | +15.3% |
| ma20_dist  |  +4.8% |
| ma50_dist  |  +7.6% |
| vol_20d    |  15.5% |
| mdd_60d    |   8.1% |
| rsi_14     |   75.5 |
| zscore_20d |    1.4 |

### Brent Crude Oil / BZ=F (score 75.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.7% |
| ret_5d     |  +3.5% |
| ret_20d    | +12.5% |
| ret_60d    | +23.1% |
| ma20_dist  |  +6.1% |
| ma50_dist  | +11.1% |
| vol_20d    |  27.0% |
| mdd_60d    |  21.2% |
| rsi_14     |   61.3 |
| zscore_20d |    1.9 |

### Corn / ZC=F (score 65.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.2% |
| ret_5d     |  -0.8% |
| ret_20d    | +11.8% |
| ret_60d    | +23.5% |
| ma20_dist  |  +3.3% |
| ma50_dist  |  +9.9% |
| vol_20d    |  45.2% |
| mdd_60d    |   6.0% |
| rsi_14     |   65.2 |
| zscore_20d |    0.7 |

### Meta Platforms Inc. / META (score 63.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | +7.2% |
| ret_20d    | +3.1% |
| ret_60d    | +8.0% |
| ma20_dist  | +6.2% |
| ma50_dist  | +2.8% |
| vol_20d    | 32.0% |
| mdd_60d    | 20.9% |
| rsi_14     |  85.5 |
| zscore_20d |   1.6 |

### Platinum / PL=F (score 63.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.2% |
| ret_5d     | +4.9% |
| ret_20d    | +7.1% |
| ret_60d    | +3.2% |
| ma20_dist  | +1.7% |
| ma50_dist  | +7.4% |
| vol_20d    | 30.8% |
| mdd_60d    |  9.1% |
| rsi_14     |  52.7 |
| zscore_20d |   0.7 |

### Wheat / ZW=F (score 63.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.0% |
| ret_5d     |  -3.5% |
| ret_20d    | +11.9% |
| ret_60d    | +22.5% |
| ma20_dist  |  +3.0% |
| ma50_dist  |  +8.6% |
| vol_20d    |  42.4% |
| mdd_60d    |  10.7% |
| rsi_14     |   60.8 |
| zscore_20d |    0.6 |

### FTSE 100 / ^FTSE (score 60.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | +0.2% |
| ret_20d    | -0.5% |
| ret_60d    | +3.7% |
| ma20_dist  | +0.1% |
| ma50_dist  | +0.7% |
| vol_20d    |  5.6% |
| mdd_60d    |  1.9% |
| rsi_14     |  59.4 |
| zscore_20d |   0.2 |

### NVIDIA Corporation / NVDA (score 55.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.0% |
| ret_5d     |  +2.2% |
| ret_20d    |  +3.8% |
| ret_60d    | +10.2% |
| ma20_dist  |  +2.4% |
| ma50_dist  |  +6.9% |
| vol_20d    |  43.7% |
| mdd_60d    |  10.6% |
| rsi_14     |   54.2 |
| zscore_20d |    0.9 |

### Tesla Inc. / TSLA (score 53.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +4.0% |
| ret_5d     |  +0.1% |
| ret_20d    | +11.3% |
| ret_60d    |  -7.8% |
| ma20_dist  |  +5.1% |
| ma50_dist  |  +2.9% |
| vol_20d    |  51.0% |
| mdd_60d    |  29.9% |
| rsi_14     |   59.8 |
| zscore_20d |    1.5 |

### DAX / ^GDAXI (score 51.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.0% |
| ret_5d     | +0.1% |
| ret_20d    | -1.5% |
| ret_60d    | +4.4% |
| ma20_dist  | -0.6% |
| ma50_dist  | +1.0% |
| vol_20d    |  8.7% |
| mdd_60d    |  4.1% |
| rsi_14     |  47.6 |
| zscore_20d |  -0.9 |

### Euro Stoxx 50 / ^STOXX50E (score 50.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | +0.7% |
| ret_20d    | -2.1% |
| ret_60d    | +2.5% |
| ma20_dist  | -0.6% |
| ma50_dist  | +0.5% |
| vol_20d    |  7.8% |
| mdd_60d    |  3.2% |
| rsi_14     |  45.9 |
| zscore_20d |  -0.6 |

### S&P 500 / ^GSPC (score 50.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | -0.2% |
| ret_20d    | -1.0% |
| ret_60d    | +3.8% |
| ma20_dist  | -0.4% |
| ma50_dist  | +1.0% |
| vol_20d    |  8.3% |
| mdd_60d    |  3.4% |
| rsi_14     |  48.2 |
| zscore_20d |  -0.7 |

### UnitedHealth Group Inc. / UNH (score 49.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | +2.9% |
| ret_20d    | -1.9% |
| ret_60d    | -0.6% |
| ma20_dist  | +1.1% |
| ma50_dist  | -2.5% |
| vol_20d    | 19.0% |
| mdd_60d    | 11.8% |
| rsi_14     |  55.7 |
| zscore_20d |   0.8 |

### Apple Inc. / AAPL (score 48.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.2% |
| ret_5d     | -0.2% |
| ret_20d    | +2.6% |
| ret_60d    | +7.0% |
| ma20_dist  | +0.9% |
| ma50_dist  | +0.2% |
| vol_20d    | 20.5% |
| mdd_60d    | 11.0% |
| rsi_14     |  55.9 |
| zscore_20d |   0.4 |

### NASDAQ 100 / ^NDX (score 48.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | +0.2% |
| ret_20d    | -0.4% |
| ret_60d    | +0.2% |
| ma20_dist  | +0.1% |
| ma50_dist  | +0.9% |
| vol_20d    | 12.6% |
| mdd_60d    | 11.0% |
| rsi_14     |  50.3 |
| zscore_20d |   0.1 |

### Microsoft Corporation / MSFT (score 48.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.2% |
| ret_5d     |  -2.6% |
| ret_20d    |  -2.2% |
| ret_60d    | +26.5% |
| ma20_dist  |  -0.2% |
| ma50_dist  | +10.7% |
| vol_20d    |  22.6% |
| mdd_60d    |  11.7% |
| rsi_14     |   57.9 |
| zscore_20d |   -0.1 |

### Hang Seng / ^HSI (score 41.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -0.0% |
| ret_20d    | -1.3% |
| ret_60d    | +2.4% |
| ma20_dist  | -0.7% |
| ma50_dist  | +0.8% |
| vol_20d    | 13.7% |
| mdd_60d    |  8.7% |
| rsi_14     |  46.3 |
| zscore_20d |  -0.9 |

### JPMorgan Chase & Co. / JPM (score 39.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.4% |
| ret_5d     |  -0.7% |
| ret_20d    |  -1.7% |
| ret_60d    | +13.3% |
| ma20_dist  |  -1.3% |
| ma50_dist  |  +1.0% |
| vol_20d    |  14.4% |
| mdd_60d    |   3.7% |
| rsi_14     |   38.1 |
| zscore_20d |   -1.1 |

### Silver / SI=F (score 37.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | +2.6% |
| ret_20d    | +2.2% |
| ret_60d    | -6.2% |
| ma20_dist  | -0.8% |
| ma50_dist  | +5.8% |
| vol_20d    | 31.5% |
| mdd_60d    | 15.6% |
| rsi_14     |  43.7 |
| zscore_20d |  -0.3 |

### Gold / GC=F (score 36.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.8% |
| ret_5d     | +1.1% |
| ret_20d    | +0.7% |
| ret_60d    | +0.8% |
| ma20_dist  | -2.2% |
| ma50_dist  | +2.6% |
| vol_20d    | 25.6% |
| mdd_60d    |  7.6% |
| rsi_14     |  43.3 |
| zscore_20d |  -0.9 |

### CAC 40 / ^FCHI (score 36.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | +0.2% |
| ret_20d    | -4.6% |
| ret_60d    | -1.5% |
| ma20_dist  | -1.4% |
| ma50_dist  | -1.6% |
| vol_20d    |  8.6% |
| mdd_60d    |  5.1% |
| rsi_14     |  33.1 |
| zscore_20d |  -0.9 |

### Russell 2000 / ^RUT (score 36.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | +0.1% |
| ret_20d    | -1.9% |
| ret_60d    | +1.3% |
| ma20_dist  | -1.4% |
| ma50_dist  | -0.9% |
| vol_20d    | 12.1% |
| mdd_60d    |  4.8% |
| rsi_14     |  40.3 |
| zscore_20d |  -1.1 |

### Dow Jones Industrial Average / ^DJI (score 35.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.2% |
| ret_5d     | -0.8% |
| ret_20d    | -2.2% |
| ret_60d    | +3.8% |
| ma20_dist  | -1.1% |
| ma50_dist  | -0.3% |
| vol_20d    |  9.8% |
| mdd_60d    |  2.9% |
| rsi_14     |  43.8 |
| zscore_20d |  -1.9 |

### Amazon.com Inc. / AMZN (score 29.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | -1.1% |
| ret_20d    | -7.6% |
| ret_60d    | +6.4% |
| ma20_dist  | -1.6% |
| ma50_dist  | +1.0% |
| vol_20d    | 25.3% |
| mdd_60d    | 11.1% |
| rsi_14     |  47.5 |
| zscore_20d |  -1.0 |

### Alphabet Inc. Class A / GOOGL (score 23.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.0% |
| ret_5d     | -0.2% |
| ret_20d    | -5.3% |
| ret_60d    | -5.4% |
| ma20_dist  | -1.2% |
| ma50_dist  | -2.9% |
| vol_20d    | 20.6% |
| mdd_60d    | 14.9% |
| rsi_14     |  44.2 |
| zscore_20d |  -1.2 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Soybeans / ZS=F                     |  19.3036 |           1.5% |                 0.65x |       38.6071 |            3.0% |
| Brent Crude Oil / BZ=F              |   3.2207 |           3.3% |                 0.37x |        6.4414 |            6.6% |
| Corn / ZC=F                         |  14.5536 |           2.8% |                 0.22x |       29.1071 |            5.7% |
| Meta Platforms Inc. / META          |  17.9336 |           2.9% |                 0.31x |       35.8672 |            5.8% |
| Platinum / PL=F                     |  29.5214 |           1.6% |                 0.32x |       59.0428 |            3.2% |
| Wheat / ZW=F                        |  25.5000 |           3.5% |                 0.24x |       51.0000 |            7.0% |
| FTSE 100 / ^FTSE                    |  81.7357 |           0.8% |                 1.78x |      163.4714 |            1.5% |
| NVIDIA Corporation / NVDA           |   7.8007 |           3.5% |                 0.23x |       15.6014 |            6.9% |
| Tesla Inc. / TSLA                   |  15.8021 |           4.3% |                 0.20x |       31.6043 |            8.6% |
| DAX / ^GDAXI                        | 224.1779 |           0.9% |                 1.16x |      448.3557 |            1.7% |
| Euro Stoxx 50 / ^STOXX50E           |  51.2756 |           0.8% |                 1.28x |      102.5513 |            1.6% |
| S&P 500 / ^GSPC                     |  55.3670 |           0.7% |                 1.20x |      110.7341 |            1.4% |
| UnitedHealth Group Inc. / UNH       |   8.1964 |           2.0% |                 0.53x |       16.3929 |            4.1% |
| Apple Inc. / AAPL                   |   7.4243 |           2.3% |                 0.49x |       14.8486 |            4.7% |
| NASDAQ 100 / ^NDX                   | 315.2027 |           1.1% |                 0.80x |      630.4054 |            2.1% |
| Microsoft Corporation / MSFT        |  10.2558 |           2.1% |                 0.44x |       20.5116 |            4.2% |
| Hang Seng / ^HSI                    | 340.4630 |           1.3% |                 0.73x |      680.9261 |            2.7% |
| JPMorgan Chase & Co. / JPM          |   5.8057 |           1.6% |                 0.69x |       11.6114 |            3.3% |
| Silver / SI=F                       |   1.7899 |           2.7% |                 0.32x |        3.5797 |            5.4% |
| Gold / GC=F                         |  80.0215 |           1.8% |                 0.39x |      160.0430 |            3.6% |
| CAC 40 / ^FCHI                      |  72.9750 |           0.9% |                 1.16x |      145.9501 |            1.8% |
| Russell 2000 / ^RUT                 |  28.6079 |           1.0% |                 0.82x |       57.2157 |            1.9% |
| Dow Jones Industrial Average / ^DJI | 451.7344 |           0.9% |                 1.02x |      903.4688 |            1.7% |
| Amazon.com Inc. / AMZN              |   5.8150 |           2.3% |                 0.40x |       11.6300 |            4.5% |
| Alphabet Inc. Class A / GOOGL       |   6.7241 |           2.0% |                 0.49x |       13.4483 |            4.0% |

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

Scoring engine version: **1.0.0** | Git commit: **950c500**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
