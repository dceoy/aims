+++
title = "Market Analysis 2026-10-23"
date = "2026-10-23T00:00:00+00:00"
draft = false
summary = "Bearish market: 25 reliable instruments. Top signal: BZ=F (score 85.2)."
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
source_files = ["data/analysis/2026-10-23.json", "data/history/2026-10-23.json"]
market_regime = "Bearish"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "e0c0558"
+++

## Market Regime

**Bearish** — 8 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Brent Crude Oil / BZ=F** — score 85.2, 20d return +6.2%, RSI14=77. 20d up +6.2%; above MA20 by 7.5%; RSI14=77 ⚠️ Upcoming: FOMC rate decision (2026-10-28)
- **Dow Jones Industrial Average / ^DJI** — score 77.0, 20d return +3.0%, RSI14=76. 20d up +3.0%; above MA20 by 2.3%; RSI14=76 ⚠️ Upcoming: FOMC rate decision (2026-10-28)
- **UnitedHealth Group Inc. / UNH** — score 76.7, 20d return +13.3%, RSI14=81. 20d up +13.3%; above MA20 by 9.8%; RSI14=81 ⚠️ Upcoming: FOMC rate decision (2026-10-28)
- **Apple Inc. / AAPL** — score 76.1, 20d return +3.7%, RSI14=72. 20d up +3.7%; above MA20 by 2.8%; RSI14=72 ⚠️ Upcoming: FOMC rate decision (2026-10-28)
- **FTSE 100 / ^FTSE** — score 69.4, 20d return +0.4%, RSI14=66. 20d up +0.4%; above MA20 by 0.8%; RSI14=66 ⚠️ Upcoming: FOMC rate decision (2026-10-28)

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

## Signal History

Compared with the previous available report (**2026-10-22**).

- **New top-5:** AAPL, UNH, ^FTSE
- **Persistent top signals:** BZ=F (5 reports), ^DJI (3 reports)
- **Dropped from top-5:** MSFT, TSLA, ^GDAXI

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +0 |    +3.6 |
| 7203.T    |     +0 |    +3.3 |
| 8306.T    |     +1 |    +4.5 |
| AAPL      |     +3 |   +10.3 |
| AMZN      |     -5 |   -16.7 |
| BZ=F      |     +2 |   +13.9 |
| CL=F      |     +0 |   +14.6 |
| GC=F      |     -1 |    -8.2 |
| GOOGL     |     +0 |    -7.3 |
| HG=F      |     +0 |    -5.5 |
| JPM       |     +7 |   +17.9 |
| META      |     -4 |   -17.6 |
| MSFT      |     -6 |    -6.7 |
| NG=F      |     +0 |   +12.7 |
| NVDA      |     -4 |   -15.4 |
| PL=F      |     -3 |    -9.4 |
| SI=F      |     -2 |   -11.5 |
| TSLA      |     -8 |   -14.8 |
| UNH       |     +5 |   +10.9 |
| XOM       |     +0 |    +5.8 |
| ZC=F      |     +5 |    +4.2 |
| ZS=F      |     +8 |   +21.2 |
| ZW=F      |     +3 |    +9.7 |
| ^DJI      |     +0 |    +1.2 |
| ^FCHI     |     +1 |    -1.8 |
| ^FTSE     |     +4 |    +7.6 |
| ^GDAXI    |     -3 |    -4.8 |
| ^GSPC     |     +0 |    -1.2 |
| ^HSI      |     +1 |    -5.2 |
| ^N225     |     -1 |    -5.5 |
| ^NDX      |     -4 |   -11.2 |
| ^RUT      |     +4 |    +9.7 |
| ^STOXX50E |     -3 |    -8.5 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **WTI Crude Oil / CL=F** — malformed_input
- **Copper / HG=F** — malformed_input
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
|    1 | Brent Crude Oil / BZ=F |  85.2 |   Yes    | —               | 20d up +6.2%; above MA20 by 7.5%; RSI14=77    |
|   10 | Soybeans / ZS=F        |  60.9 |   Yes    | —               | 20d down -4.9%; below MA20 by 2.1%; RSI14=37  |
|   18 | Gold / GC=F            |  32.4 |   Yes    | —               | 20d down -5.5%; below MA20 by 2.7%; RSI14=39  |
|   19 | Corn / ZC=F            |  26.1 |   Yes    | —               | 20d down -12.7%; below MA20 by 6.1%; RSI14=23 |
|   22 | Wheat / ZW=F           |  19.1 |   Yes    | —               | 20d down -11.6%; below MA20 by 7.2%; RSI14=24 |
|   24 | Platinum / PL=F        |  16.7 |   Yes    | —               | 20d down -10.4%; below MA20 by 5.7%; RSI14=34 |
|   25 | Silver / SI=F          |  10.9 |   Yes    | —               | 20d down -13.7%; below MA20 by 7.5%; RSI14=33 |
|   29 | WTI Crude Oil / CL=F   |  68.8 |    No    | malformed_input | Suppressed: malformed_input                   |
|   30 | Copper / HG=F          |  40.3 |    No    | malformed_input | Suppressed: malformed_input                   |
|   33 | Natural Gas / NG=F     |  23.6 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                    |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | ---------------------------------------------- |
|    3 | UnitedHealth Group Inc. / UNH                                                  |  76.7 |   Yes    | —                             | 20d up +13.3%; above MA20 by 9.8%; RSI14=81    |
|    4 | Apple Inc. / AAPL                                                              |  76.1 |   Yes    | —                             | 20d up +3.7%; above MA20 by 2.8%; RSI14=72     |
|    8 | JPMorgan Chase & Co. / JPM                                                     |  63.6 |   Yes    | —                             | 20d down -0.1%; above MA20 by 0.9%; RSI14=61   |
|    9 | Tesla Inc. / TSLA                                                              |  61.5 |   Yes    | —                             | 20d down -0.9%; above MA20 by 1.3%; RSI14=52   |
|   11 | Microsoft Corporation / MSFT                                                   |  60.6 |   Yes    | —                             | 20d up +4.6%; below MA20 by 1.0%; RSI14=52     |
|   15 | Amazon.com Inc. / AMZN                                                         |  44.9 |   Yes    | —                             | 20d up +0.4%; below MA20 by 1.6%; RSI14=49     |
|   17 | NVIDIA Corporation / NVDA                                                      |  33.0 |   Yes    | —                             | 20d down -5.5%; below MA20 by 6.2%; RSI14=30   |
|   20 | Alphabet Inc. Class A / GOOGL                                                  |  22.1 |   Yes    | —                             | 20d down -5.3%; below MA20 by 5.8%; RSI14=32   |
|   23 | Meta Platforms Inc. / META                                                     |  17.3 |   Yes    | —                             | 20d down -16.6%; below MA20 by 10.3%; RSI14=30 |
|   26 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  84.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   27 | Exxon Mobil Corporation / XOM                                                  |  83.3 |    No    | malformed_input               | Suppressed: malformed_input                    |
|   28 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  69.4 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   31 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  30.3 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    2 | Dow Jones Industrial Average / ^DJI |  77.0 |   Yes    | —            | 20d up +3.0%; above MA20 by 2.3%; RSI14=76   |
|    5 | FTSE 100 / ^FTSE                    |  69.4 |   Yes    | —            | 20d up +0.4%; above MA20 by 0.8%; RSI14=66   |
|    6 | S&P 500 / ^GSPC                     |  64.8 |   Yes    | —            | 20d down -0.5%; below MA20 by 0.9%; RSI14=45 |
|    7 | DAX / ^GDAXI                        |  64.2 |   Yes    | —            | 20d up +0.4%; above MA20 by 0.3%; RSI14=53   |
|   12 | Russell 2000 / ^RUT                 |  54.5 |   Yes    | —            | 20d down -1.8%; below MA20 by 0.3%; RSI14=42 |
|   13 | CAC 40 / ^FCHI                      |  46.7 |   Yes    | —            | 20d down -3.3%; below MA20 by 1.0%; RSI14=44 |
|   14 | Euro Stoxx 50 / ^STOXX50E           |  46.7 |   Yes    | —            | 20d down -3.0%; below MA20 by 1.9%; RSI14=38 |
|   16 | NASDAQ 100 / ^NDX                   |  39.4 |   Yes    | —            | 20d down -5.0%; below MA20 by 4.4%; RSI14=29 |
|   21 | Hang Seng / ^HSI                    |  20.6 |   Yes    | —            | 20d down -8.6%; below MA20 by 5.2%; RSI14=27 |
|   32 | Nikkei 225 / ^N225                  |  29.7 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-10-22 |
| 7203.T    | 2026-10-22 |
| 8306.T    | 2026-10-22 |
| AAPL      | 2026-10-22 |
| AMZN      | 2026-10-22 |
| BZ=F      | 2026-10-22 |
| CL=F      | 2026-10-22 |
| GC=F      | 2026-10-22 |
| GOOGL     | 2026-10-22 |
| HG=F      | 2026-10-22 |
| JPM       | 2026-10-22 |
| META      | 2026-10-22 |
| MSFT      | 2026-10-22 |
| NG=F      | 2026-10-22 |
| NVDA      | 2026-10-22 |
| PL=F      | 2026-10-22 |
| SI=F      | 2026-10-22 |
| TSLA      | 2026-10-22 |
| UNH       | 2026-10-22 |
| XOM       | 2026-10-22 |
| ZC=F      | 2026-10-22 |
| ZS=F      | 2026-10-22 |
| ZW=F      | 2026-10-22 |
| ^DJI      | 2026-10-22 |
| ^FCHI     | 2026-10-22 |
| ^FTSE     | 2026-10-22 |
| ^GDAXI    | 2026-10-22 |
| ^GSPC     | 2026-10-22 |
| ^HSI      | 2026-10-22 |
| ^N225     | 2026-10-22 |
| ^NDX      | 2026-10-22 |
| ^RUT      | 2026-10-22 |
| ^STOXX50E | 2026-10-22 |

## Symbol Details

### Brent Crude Oil / BZ=F (score 85.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +4.0% |
| ret_5d     |  +6.8% |
| ret_20d    |  +6.2% |
| ret_60d    | +42.6% |
| ma20_dist  |  +7.5% |
| ma50_dist  | +12.6% |
| vol_20d    |  29.1% |
| mdd_60d    |   8.7% |
| rsi_14     |   77.5 |
| zscore_20d |    2.3 |

### Dow Jones Industrial Average / ^DJI (score 77.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.0% |
| ret_5d     | +1.3% |
| ret_20d    | +3.0% |
| ret_60d    | +2.5% |
| ma20_dist  | +2.3% |
| ma50_dist  | +1.0% |
| vol_20d    |  9.0% |
| mdd_60d    |  6.3% |
| rsi_14     |  76.0 |
| zscore_20d |   2.1 |

### UnitedHealth Group Inc. / UNH (score 76.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.9% |
| ret_5d     |  +4.5% |
| ret_20d    | +13.3% |
| ret_60d    |  +1.0% |
| ma20_dist  |  +9.8% |
| ma50_dist  |  +9.8% |
| vol_20d    |  27.0% |
| mdd_60d    |  13.4% |
| rsi_14     |   80.7 |
| zscore_20d |    2.1 |

### Apple Inc. / AAPL (score 76.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.2% |
| ret_5d     | +1.8% |
| ret_20d    | +3.7% |
| ret_60d    | +3.1% |
| ma20_dist  | +2.8% |
| ma50_dist  | +6.0% |
| vol_20d    | 16.7% |
| mdd_60d    |  9.3% |
| rsi_14     |  71.7 |
| zscore_20d |   1.9 |

### FTSE 100 / ^FTSE (score 69.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | -1.1% |
| ret_20d    | +0.4% |
| ret_60d    | -1.7% |
| ma20_dist  | +0.8% |
| ma50_dist  | +0.2% |
| vol_20d    | 10.9% |
| mdd_60d    |  4.3% |
| rsi_14     |  65.9 |
| zscore_20d |   0.7 |

### S&P 500 / ^GSPC (score 64.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.2% |
| ret_5d     | -1.0% |
| ret_20d    | -0.5% |
| ret_60d    | +4.7% |
| ma20_dist  | -0.9% |
| ma50_dist  | -0.5% |
| vol_20d    |  9.7% |
| mdd_60d    |  3.2% |
| rsi_14     |  45.0 |
| zscore_20d |  -1.3 |

### DAX / ^GDAXI (score 64.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.1% |
| ret_5d     | -0.0% |
| ret_20d    | +0.4% |
| ret_60d    | -0.9% |
| ma20_dist  | +0.3% |
| ma50_dist  | -1.1% |
| vol_20d    | 13.5% |
| mdd_60d    |  6.6% |
| rsi_14     |  52.7 |
| zscore_20d |   0.4 |

### JPMorgan Chase & Co. / JPM (score 63.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | +0.3% |
| ret_20d    | -0.1% |
| ret_60d    | -2.4% |
| ma20_dist  | +0.9% |
| ma50_dist  | -2.6% |
| vol_20d    | 14.2% |
| mdd_60d    |  9.9% |
| rsi_14     |  60.6 |
| zscore_20d |   0.9 |

### Tesla Inc. / TSLA (score 61.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -3.1% |
| ret_5d     |  +3.3% |
| ret_20d    |  -0.9% |
| ret_60d    | +25.6% |
| ma20_dist  |  +1.3% |
| ma50_dist  |  +3.2% |
| vol_20d    |  35.9% |
| mdd_60d    |   7.3% |
| rsi_14     |   52.1 |
| zscore_20d |    0.5 |

### Soybeans / ZS=F (score 60.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | -0.8% |
| ret_20d    | -4.9% |
| ret_60d    | +7.2% |
| ma20_dist  | -2.1% |
| ma50_dist  | -1.9% |
| vol_20d    | 12.4% |
| mdd_60d    |  6.2% |
| rsi_14     |  37.3 |
| zscore_20d |  -1.4 |

### Microsoft Corporation / MSFT (score 60.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.2% |
| ret_5d     |  -3.4% |
| ret_20d    |  +4.6% |
| ret_60d    | +33.7% |
| ma20_dist  |  -1.0% |
| ma50_dist  |  +2.6% |
| vol_20d    |  22.8% |
| mdd_60d    |   5.1% |
| rsi_14     |   52.1 |
| zscore_20d |   -0.5 |

### Russell 2000 / ^RUT (score 54.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | +0.6% |
| ret_20d    | -1.8% |
| ret_60d    | -4.2% |
| ma20_dist  | -0.3% |
| ma50_dist  | -3.5% |
| vol_20d    | 14.1% |
| mdd_60d    | 11.3% |
| rsi_14     |  42.0 |
| zscore_20d |  -0.2 |

### CAC 40 / ^FCHI (score 46.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.4% |
| ret_5d     | -1.6% |
| ret_20d    | -3.3% |
| ret_60d    | -7.9% |
| ma20_dist  | -1.0% |
| ma50_dist  | -4.0% |
| vol_20d    | 12.7% |
| mdd_60d    | 11.4% |
| rsi_14     |  44.5 |
| zscore_20d |  -0.8 |

### Euro Stoxx 50 / ^STOXX50E (score 46.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.9% |
| ret_5d     | -1.3% |
| ret_20d    | -3.0% |
| ret_60d    | -4.1% |
| ma20_dist  | -1.9% |
| ma50_dist  | -3.5% |
| vol_20d    | 14.0% |
| mdd_60d    |  7.1% |
| rsi_14     |  38.5 |
| zscore_20d |  -1.9 |

### Amazon.com Inc. / AMZN (score 44.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -4.6% |
| ret_5d     |  -1.7% |
| ret_20d    |  +0.4% |
| ret_60d    | +10.5% |
| ma20_dist  |  -1.6% |
| ma50_dist  |  -2.2% |
| vol_20d    |  31.8% |
| mdd_60d    |  13.4% |
| rsi_14     |   49.1 |
| zscore_20d |   -0.8 |

### NASDAQ 100 / ^NDX (score 39.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.9% |
| ret_5d     | -3.3% |
| ret_20d    | -5.0% |
| ret_60d    | +6.5% |
| ma20_dist  | -4.4% |
| ma50_dist  | -3.0% |
| vol_20d    | 18.3% |
| mdd_60d    |  7.3% |
| rsi_14     |  28.7 |
| zscore_20d |  -2.1 |

### NVIDIA Corporation / NVDA (score 33.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -4.4% |
| ret_5d     |  -2.3% |
| ret_20d    |  -5.5% |
| ret_60d    | +11.7% |
| ma20_dist  |  -6.2% |
| ma50_dist  |  -4.7% |
| vol_20d    |  28.6% |
| mdd_60d    |  11.3% |
| rsi_14     |   29.7 |
| zscore_20d |   -1.8 |

### Gold / GC=F (score 32.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.2% |
| ret_5d     | -2.6% |
| ret_20d    | -5.5% |
| ret_60d    | -0.9% |
| ma20_dist  | -2.7% |
| ma50_dist  | -6.8% |
| vol_20d    | 18.5% |
| mdd_60d    | 13.7% |
| rsi_14     |  39.3 |
| zscore_20d |  -2.3 |

### Corn / ZC=F (score 26.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.6% |
| ret_5d     |  -3.7% |
| ret_20d    | -12.7% |
| ret_60d    |  +2.5% |
| ma20_dist  |  -6.1% |
| ma50_dist  |  -8.3% |
| vol_20d    |  21.9% |
| mdd_60d    |  15.2% |
| rsi_14     |   22.5 |
| zscore_20d |   -1.5 |

### Alphabet Inc. Class A / GOOGL (score 22.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -3.1% |
| ret_5d     | -7.2% |
| ret_20d    | -5.3% |
| ret_60d    | -3.7% |
| ma20_dist  | -5.8% |
| ma50_dist  | -5.6% |
| vol_20d    | 20.3% |
| mdd_60d    | 14.1% |
| rsi_14     |  32.3 |
| zscore_20d |  -3.0 |

### Hang Seng / ^HSI (score 20.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -3.0% |
| ret_5d     | -5.7% |
| ret_20d    | -8.6% |
| ret_60d    | -9.4% |
| ma20_dist  | -5.2% |
| ma50_dist  | -7.7% |
| vol_20d    | 18.0% |
| mdd_60d    | 11.8% |
| rsi_14     |  27.1 |
| zscore_20d |  -3.0 |

### Wheat / ZW=F (score 19.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.6% |
| ret_5d     |  -6.8% |
| ret_20d    | -11.6% |
| ret_60d    |  -4.0% |
| ma20_dist  |  -7.2% |
| ma50_dist  | -10.5% |
| vol_20d    |  20.0% |
| mdd_60d    |  18.5% |
| rsi_14     |   23.8 |
| zscore_20d |   -2.3 |

### Meta Platforms Inc. / META (score 17.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -7.0% |
| ret_5d     | -11.9% |
| ret_20d    | -16.6% |
| ret_60d    | +10.8% |
| ma20_dist  | -10.3% |
| ma50_dist  |  -2.1% |
| vol_20d    |  41.6% |
| mdd_60d    |  16.6% |
| rsi_14     |   30.3 |
| zscore_20d |   -3.1 |

### Platinum / PL=F (score 16.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -3.6% |
| ret_5d     |  -2.7% |
| ret_20d    | -10.4% |
| ret_60d    | -10.3% |
| ma20_dist  |  -5.7% |
| ma50_dist  | -10.6% |
| vol_20d    |  29.8% |
| mdd_60d    |  18.1% |
| rsi_14     |   34.0 |
| zscore_20d |   -2.0 |

### Silver / SI=F (score 10.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -4.6% |
| ret_5d     |  -3.6% |
| ret_20d    | -13.7% |
| ret_60d    |  -8.8% |
| ma20_dist  |  -7.5% |
| ma50_dist  | -13.6% |
| vol_20d    |  36.1% |
| mdd_60d    |  21.2% |
| rsi_14     |   32.8 |
| zscore_20d |   -2.0 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Brent Crude Oil / BZ=F              |   3.9186 |           3.5% |                 0.34x |        7.8371 |            6.9% |
| Dow Jones Industrial Average / ^DJI | 514.0834 |           1.0% |                 1.11x |     1028.1669 |            1.9% |
| UnitedHealth Group Inc. / UNH       |  13.2414 |           3.1% |                 0.37x |       26.4829 |            6.2% |
| Apple Inc. / AAPL                   |   6.0836 |           1.7% |                 0.60x |       12.1671 |            3.5% |
| FTSE 100 / ^FTSE                    | 110.3357 |           1.0% |                 0.92x |      220.6713 |            2.1% |
| S&P 500 / ^GSPC                     |  73.6415 |           1.0% |                 1.03x |      147.2829 |            1.9% |
| DAX / ^GDAXI                        | 309.4210 |           1.2% |                 0.74x |      618.8421 |            2.4% |
| JPMorgan Chase & Co. / JPM          |   6.1575 |           1.8% |                 0.70x |       12.3149 |            3.7% |
| Tesla Inc. / TSLA                   |  12.0321 |           3.2% |                 0.28x |       24.0643 |            6.4% |
| Soybeans / ZS=F                     |  18.1607 |           1.4% |                 0.80x |       36.3214 |            2.9% |
| Microsoft Corporation / MSFT        |  11.3800 |           2.2% |                 0.44x |       22.7600 |            4.4% |
| Russell 2000 / ^RUT                 |  35.0514 |           1.3% |                 0.71x |       70.1028 |            2.5% |
| CAC 40 / ^FCHI                      |  90.4379 |           1.2% |                 0.79x |      180.8758 |            2.3% |
| Euro Stoxx 50 / ^STOXX50E           |  76.8936 |           1.3% |                 0.72x |      153.7872 |            2.5% |
| Amazon.com Inc. / AMZN              |   7.1150 |           2.8% |                 0.31x |       14.2300 |            5.7% |
| NASDAQ 100 / ^NDX                   | 497.3354 |           1.7% |                 0.55x |      994.6708 |            3.4% |
| NVIDIA Corporation / NVDA           |   6.1550 |           2.9% |                 0.35x |       12.3100 |            5.8% |
| Gold / GC=F                         |  70.2642 |           1.7% |                 0.54x |      140.5285 |            3.5% |
| Corn / ZC=F                         |  10.2321 |           2.2% |                 0.46x |       20.4643 |            4.4% |
| Alphabet Inc. Class A / GOOGL       |   8.4836 |           2.6% |                 0.49x |       16.9671 |            5.2% |
| Hang Seng / ^HSI                    | 405.8500 |           1.8% |                 0.56x |      811.7001 |            3.5% |
| Wheat / ZW=F                        |  16.0536 |           2.6% |                 0.50x |       32.1071 |            5.1% |
| Meta Platforms Inc. / META          |  25.5693 |           3.9% |                 0.24x |       51.1386 |            7.9% |
| Platinum / PL=F                     |  30.3929 |           1.9% |                 0.34x |       60.7857 |            3.9% |
| Silver / SI=F                       |   1.2730 |           2.3% |                 0.28x |        2.5460 |            4.6% |

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

Scoring engine version: **1.0.0** | Git commit: **e0c0558**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
