+++
title = "Market Analysis 2026-10-26"
date = "2026-10-26T00:00:00+00:00"
draft = false
summary = "Bearish market: 25 reliable instruments. Top signal: BZ=F (score 85.5)."
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
source_files = ["data/analysis/2026-10-26.json", "data/history/2026-10-26.json"]
market_regime = "Bearish"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "5b93153"
+++

## Market Regime

**Bearish** — 6 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Brent Crude Oil / BZ=F** — score 85.5, 20d return +11.9%, RSI14=88. 20d up +11.9%; above MA20 by 10.3%; RSI14=88 ⚠️ Upcoming: FOMC rate decision (2026-10-28)
- **Apple Inc. / AAPL** — score 77.6, 20d return +2.0%, RSI14=72. 20d up +2.0%; above MA20 by 2.6%; RSI14=72 ⚠️ Upcoming: FOMC rate decision (2026-10-28); AAPL earnings release (2026-11-02)
- **Microsoft Corporation / MSFT** — score 69.4, 20d return +1.6%, RSI14=50. 20d up +1.6%; below MA20 by 0.4%; RSI14=50 ⚠️ Upcoming: FOMC rate decision (2026-10-28); MSFT earnings release (2026-10-28)
- **Dow Jones Industrial Average / ^DJI** — score 69.4, 20d return +0.7%, RSI14=62. 20d up +0.7%; above MA20 by 1.0%; RSI14=62 ⚠️ Upcoming: FOMC rate decision (2026-10-28)
- **FTSE 100 / ^FTSE** — score 67.6, 20d return -0.0%, RSI14=62. 20d down -0.0%; above MA20 by 0.5%; RSI14=62 ⚠️ Upcoming: FOMC rate decision (2026-10-28)

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

Compared with the previous available report (**2026-10-23**).

- **New top-5:** MSFT
- **Persistent top signals:** BZ=F (6 reports), ^DJI (4 reports), AAPL (2 reports), ^FTSE (2 reports)
- **Dropped from top-5:** UNH

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     -1 |    +0.6 |
| 7203.T    |     -1 |    +4.5 |
| 8306.T    |     -1 |   -11.2 |
| AAPL      |     +2 |    +1.5 |
| AMZN      |     +0 |    +1.5 |
| BZ=F      |     +0 |    +0.3 |
| CL=F      |     +1 |    +5.8 |
| GC=F      |     -3 |    -9.1 |
| GOOGL     |     -3 |    -2.7 |
| HG=F      |     +0 |   +16.4 |
| JPM       |     -6 |   -16.1 |
| META      |     +1 |    +3.6 |
| MSFT      |     +8 |    +8.8 |
| NG=F      |     +0 |   -14.2 |
| NVDA      |     +0 |    +2.7 |
| PL=F      |     +0 |    +0.9 |
| SI=F      |     +0 |    -3.6 |
| TSLA      |     +3 |    +3.3 |
| UNH       |     -4 |   -12.7 |
| XOM       |     +1 |    +2.7 |
| ZC=F      |     +0 |    +0.3 |
| ZS=F      |     +2 |    +1.8 |
| ZW=F      |     +2 |    +4.5 |
| ^DJI      |     -2 |    -7.6 |
| ^FCHI     |     +1 |    +1.2 |
| ^FTSE     |     +0 |    -1.8 |
| ^GDAXI    |     -3 |    -4.5 |
| ^GSPC     |     -3 |    -3.9 |
| ^HSI      |     +3 |   +13.0 |
| ^N225     |     +1 |    +5.2 |
| ^NDX      |     +3 |    +8.5 |
| ^RUT      |     +1 |    +1.2 |
| ^STOXX50E |     -2 |    -0.9 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Exxon Mobil Corporation / XOM** — malformed_input
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **WTI Crude Oil / CL=F** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
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
|    1 | Brent Crude Oil / BZ=F |  85.5 |   Yes    | —               | 20d up +11.9%; above MA20 by 10.3%; RSI14=88  |
|    8 | Soybeans / ZS=F        |  62.7 |   Yes    | —               | 20d down -4.7%; below MA20 by 1.6%; RSI14=38  |
|   19 | Corn / ZC=F            |  26.4 |   Yes    | —               | 20d down -13.7%; below MA20 by 6.4%; RSI14=21 |
|   20 | Wheat / ZW=F           |  23.6 |   Yes    | —               | 20d down -11.1%; below MA20 by 6.6%; RSI14=17 |
|   21 | Gold / GC=F            |  23.3 |   Yes    | —               | 20d down -7.3%; below MA20 by 3.5%; RSI14=36  |
|   24 | Platinum / PL=F        |  17.6 |   Yes    | —               | 20d down -12.4%; below MA20 by 5.9%; RSI14=28 |
|   25 | Silver / SI=F          |   7.3 |   Yes    | —               | 20d down -16.4%; below MA20 by 8.5%; RSI14=27 |
|   28 | WTI Crude Oil / CL=F   |  74.5 |    No    | malformed_input | Suppressed: malformed_input                   |
|   30 | Copper / HG=F          |  56.7 |    No    | malformed_input | Suppressed: malformed_input                   |
|   33 | Natural Gas / NG=F     |   9.4 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                    |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | ---------------------------------------------- |
|    2 | Apple Inc. / AAPL                                                              |  77.6 |   Yes    | —                             | 20d up +2.0%; above MA20 by 2.6%; RSI14=72     |
|    3 | Microsoft Corporation / MSFT                                                   |  69.4 |   Yes    | —                             | 20d up +1.6%; below MA20 by 0.4%; RSI14=50     |
|    6 | Tesla Inc. / TSLA                                                              |  64.8 |   Yes    | —                             | 20d up +0.0%; above MA20 by 0.6%; RSI14=46     |
|    7 | UnitedHealth Group Inc. / UNH                                                  |  63.9 |   Yes    | —                             | 20d up +11.0%; above MA20 by 7.4%; RSI14=73    |
|   14 | JPMorgan Chase & Co. / JPM                                                     |  47.6 |   Yes    | —                             | 20d down -2.9%; below MA20 by 0.5%; RSI14=51   |
|   15 | Amazon.com Inc. / AMZN                                                         |  46.4 |   Yes    | —                             | 20d down -0.7%; below MA20 by 2.5%; RSI14=47   |
|   17 | NVIDIA Corporation / NVDA                                                      |  35.8 |   Yes    | —                             | 20d down -6.3%; below MA20 by 6.5%; RSI14=22   |
|   22 | Meta Platforms Inc. / META                                                     |  20.9 |   Yes    | —                             | 20d down -14.5%; below MA20 by 10.5%; RSI14=24 |
|   23 | Alphabet Inc. Class A / GOOGL                                                  |  19.4 |   Yes    | —                             | 20d down -6.9%; below MA20 by 6.7%; RSI14=26   |
|   26 | Exxon Mobil Corporation / XOM                                                  |  86.1 |    No    | malformed_input               | Suppressed: malformed_input                    |
|   27 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  84.8 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   29 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  73.9 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   32 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  19.1 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    4 | Dow Jones Industrial Average / ^DJI |  69.4 |   Yes    | —            | 20d up +0.7%; above MA20 by 1.0%; RSI14=62   |
|    5 | FTSE 100 / ^FTSE                    |  67.6 |   Yes    | —            | 20d down -0.0%; above MA20 by 0.5%; RSI14=62 |
|    9 | S&P 500 / ^GSPC                     |  60.9 |   Yes    | —            | 20d down -1.5%; below MA20 by 1.3%; RSI14=37 |
|   10 | DAX / ^GDAXI                        |  59.7 |   Yes    | —            | 20d down -0.9%; below MA20 by 0.4%; RSI14=49 |
|   11 | Russell 2000 / ^RUT                 |  55.8 |   Yes    | —            | 20d down -2.2%; below MA20 by 0.5%; RSI14=38 |
|   12 | CAC 40 / ^FCHI                      |  47.9 |   Yes    | —            | 20d down -3.7%; below MA20 by 1.1%; RSI14=47 |
|   13 | NASDAQ 100 / ^NDX                   |  47.9 |   Yes    | —            | 20d down -5.4%; below MA20 by 4.2%; RSI14=24 |
|   16 | Euro Stoxx 50 / ^STOXX50E           |  45.8 |   Yes    | —            | 20d down -3.7%; below MA20 by 2.0%; RSI14=37 |
|   18 | Hang Seng / ^HSI                    |  33.6 |   Yes    | —            | 20d down -7.0%; below MA20 by 4.2%; RSI14=36 |
|   31 | Nikkei 225 / ^N225                  |  34.9 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-10-23 |
| 7203.T    | 2026-10-23 |
| 8306.T    | 2026-10-23 |
| AAPL      | 2026-10-23 |
| AMZN      | 2026-10-23 |
| BZ=F      | 2026-10-23 |
| CL=F      | 2026-10-23 |
| GC=F      | 2026-10-23 |
| GOOGL     | 2026-10-23 |
| HG=F      | 2026-10-23 |
| JPM       | 2026-10-23 |
| META      | 2026-10-23 |
| MSFT      | 2026-10-23 |
| NG=F      | 2026-10-23 |
| NVDA      | 2026-10-23 |
| PL=F      | 2026-10-23 |
| SI=F      | 2026-10-23 |
| TSLA      | 2026-10-23 |
| UNH       | 2026-10-23 |
| XOM       | 2026-10-23 |
| ZC=F      | 2026-10-23 |
| ZS=F      | 2026-10-23 |
| ZW=F      | 2026-10-23 |
| ^DJI      | 2026-10-23 |
| ^FCHI     | 2026-10-23 |
| ^FTSE     | 2026-10-23 |
| ^GDAXI    | 2026-10-23 |
| ^GSPC     | 2026-10-23 |
| ^HSI      | 2026-10-23 |
| ^N225     | 2026-10-23 |
| ^NDX      | 2026-10-23 |
| ^RUT      | 2026-10-23 |
| ^STOXX50E | 2026-10-23 |

## Symbol Details

### Brent Crude Oil / BZ=F (score 85.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +3.1% |
| ret_5d     |  +6.2% |
| ret_20d    | +11.9% |
| ret_60d    | +46.9% |
| ma20_dist  | +10.3% |
| ma50_dist  | +15.5% |
| vol_20d    |  29.3% |
| mdd_60d    |   8.7% |
| rsi_14     |   88.1 |
| zscore_20d |    2.6 |

### Apple Inc. / AAPL (score 77.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | +1.2% |
| ret_20d    | +2.0% |
| ret_60d    | +4.4% |
| ma20_dist  | +2.6% |
| ma50_dist  | +5.5% |
| vol_20d    | 16.0% |
| mdd_60d    |  3.9% |
| rsi_14     |  72.3 |
| zscore_20d |   1.7 |

### Microsoft Corporation / MSFT (score 69.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.7% |
| ret_5d     |  -0.9% |
| ret_20d    |  +1.6% |
| ret_60d    | +16.5% |
| ma20_dist  |  -0.4% |
| ma50_dist  |  +3.2% |
| vol_20d    |  19.2% |
| mdd_60d    |   5.1% |
| rsi_14     |   49.6 |
| zscore_20d |   -0.2 |

### Dow Jones Industrial Average / ^DJI (score 69.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.2% |
| ret_5d     | +0.4% |
| ret_20d    | +0.7% |
| ret_60d    | +0.0% |
| ma20_dist  | +1.0% |
| ma50_dist  | -0.2% |
| vol_20d    |  9.7% |
| mdd_60d    |  6.3% |
| rsi_14     |  62.4 |
| zscore_20d |   0.9 |

### FTSE 100 / ^FTSE (score 67.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | -1.8% |
| ret_20d    | -0.0% |
| ret_60d    | -1.9% |
| ma20_dist  | +0.5% |
| ma50_dist  | -0.1% |
| vol_20d    | 10.9% |
| mdd_60d    |  4.3% |
| rsi_14     |  61.6 |
| zscore_20d |   0.4 |

### Tesla Inc. / TSLA (score 64.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.6% |
| ret_5d     |  +4.9% |
| ret_20d    |  +0.0% |
| ret_60d    | +20.5% |
| ma20_dist  |  +0.6% |
| ma50_dist  |  +2.3% |
| vol_20d    |  35.6% |
| mdd_60d    |   7.3% |
| rsi_14     |   46.4 |
| zscore_20d |    0.2 |

### UnitedHealth Group Inc. / UNH (score 63.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.6% |
| ret_5d     |  +4.2% |
| ret_20d    | +11.0% |
| ret_60d    |  -0.8% |
| ma20_dist  |  +7.4% |
| ma50_dist  |  +7.9% |
| vol_20d    |  28.2% |
| mdd_60d    |  12.1% |
| rsi_14     |   72.8 |
| zscore_20d |    1.5 |

### Soybeans / ZS=F (score 62.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | -0.4% |
| ret_20d    | -4.7% |
| ret_60d    | +8.8% |
| ma20_dist  | -1.6% |
| ma50_dist  | -1.7% |
| vol_20d    | 12.5% |
| mdd_60d    |  6.2% |
| rsi_14     |  37.9 |
| zscore_20d |  -1.1 |

### S&P 500 / ^GSPC (score 60.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | -0.5% |
| ret_20d    | -1.5% |
| ret_60d    | +2.5% |
| ma20_dist  | -1.3% |
| ma50_dist  | -1.0% |
| vol_20d    |  9.6% |
| mdd_60d    |  3.2% |
| rsi_14     |  37.0 |
| zscore_20d |  -1.7 |

### DAX / ^GDAXI (score 59.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | -1.7% |
| ret_20d    | -0.9% |
| ret_60d    | -1.7% |
| ma20_dist  | -0.4% |
| ma50_dist  | -1.7% |
| vol_20d    | 13.6% |
| mdd_60d    |  6.6% |
| rsi_14     |  48.7 |
| zscore_20d |  -0.5 |

### Russell 2000 / ^RUT (score 55.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | +2.0% |
| ret_20d    | -2.2% |
| ret_60d    | -5.8% |
| ma20_dist  | -0.5% |
| ma50_dist  | -3.6% |
| vol_20d    | 14.1% |
| mdd_60d    | 11.3% |
| rsi_14     |  38.1 |
| zscore_20d |  -0.4 |

### CAC 40 / ^FCHI (score 47.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -2.2% |
| ret_20d    | -3.7% |
| ret_60d    | -8.5% |
| ma20_dist  | -1.1% |
| ma50_dist  | -4.1% |
| vol_20d    | 12.7% |
| mdd_60d    | 11.4% |
| rsi_14     |  46.6 |
| zscore_20d |  -1.1 |

### NASDAQ 100 / ^NDX (score 47.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.0% |
| ret_5d     | -0.8% |
| ret_20d    | -5.4% |
| ret_60d    | +3.0% |
| ma20_dist  | -4.2% |
| ma50_dist  | -2.9% |
| vol_20d    | 18.1% |
| mdd_60d    |  7.3% |
| rsi_14     |  24.0 |
| zscore_20d |  -1.8 |

### JPMorgan Chase & Co. / JPM (score 47.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.5% |
| ret_5d     | -2.4% |
| ret_20d    | -2.9% |
| ret_60d    | -5.5% |
| ma20_dist  | -0.5% |
| ma50_dist  | -3.8% |
| vol_20d    | 14.2% |
| mdd_60d    |  9.9% |
| rsi_14     |  51.3 |
| zscore_20d |  -0.6 |

### Amazon.com Inc. / AMZN (score 46.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | -0.8% |
| ret_20d    | -0.7% |
| ret_60d    | +5.3% |
| ma20_dist  | -2.5% |
| ma50_dist  | -3.0% |
| vol_20d    | 32.0% |
| mdd_60d    | 13.4% |
| rsi_14     |  47.3 |
| zscore_20d |  -1.1 |

### Euro Stoxx 50 / ^STOXX50E (score 45.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | -2.2% |
| ret_20d    | -3.7% |
| ret_60d    | -4.6% |
| ma20_dist  | -2.0% |
| ma50_dist  | -3.7% |
| vol_20d    | 13.8% |
| mdd_60d    |  7.4% |
| rsi_14     |  37.1 |
| zscore_20d |  -1.9 |

### NVIDIA Corporation / NVDA (score 35.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | -1.5% |
| ret_20d    | -6.3% |
| ret_60d    | +8.2% |
| ma20_dist  | -6.5% |
| ma50_dist  | -5.1% |
| vol_20d    | 28.6% |
| mdd_60d    | 11.8% |
| rsi_14     |  22.0 |
| zscore_20d |  -1.7 |

### Hang Seng / ^HSI (score 33.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.7% |
| ret_5d     |  -4.0% |
| ret_20d    |  -7.0% |
| ret_60d    | -10.5% |
| ma20_dist  |  -4.2% |
| ma50_dist  |  -6.9% |
| vol_20d    |  18.3% |
| mdd_60d    |  11.8% |
| rsi_14     |   36.2 |
| zscore_20d |   -2.2 |

### Corn / ZC=F (score 26.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.0% |
| ret_5d     |  -3.8% |
| ret_20d    | -13.7% |
| ret_60d    |  +3.1% |
| ma20_dist  |  -6.4% |
| ma50_dist  |  -9.1% |
| vol_20d    |  21.7% |
| mdd_60d    |  16.0% |
| rsi_14     |   21.3 |
| zscore_20d |   -1.6 |

### Wheat / ZW=F (score 23.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.0% |
| ret_5d     |  -5.4% |
| ret_20d    | -11.1% |
| ret_60d    |  -2.1% |
| ma20_dist  |  -6.6% |
| ma50_dist  | -10.3% |
| vol_20d    |  20.1% |
| mdd_60d    |  18.5% |
| rsi_14     |   17.1 |
| zscore_20d |   -2.0 |

### Gold / GC=F (score 23.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.3% |
| ret_5d     | -4.1% |
| ret_20d    | -7.3% |
| ret_60d    | -5.6% |
| ma20_dist  | -3.5% |
| ma50_dist  | -7.8% |
| vol_20d    | 18.5% |
| mdd_60d    | 14.8% |
| rsi_14     |  35.7 |
| zscore_20d |  -3.1 |

### Meta Platforms Inc. / META (score 20.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.0% |
| ret_5d     |  -9.4% |
| ret_20d    | -14.5% |
| ret_60d    | +19.2% |
| ma20_dist  | -10.5% |
| ma50_dist  |  -3.2% |
| vol_20d    |  40.6% |
| mdd_60d    |  17.4% |
| rsi_14     |   24.3 |
| zscore_20d |   -2.6 |

### Alphabet Inc. Class A / GOOGL (score 19.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.2% |
| ret_5d     | -6.0% |
| ret_20d    | -6.9% |
| ret_60d    | -4.0% |
| ma20_dist  | -6.7% |
| ma50_dist  | -6.6% |
| vol_20d    | 20.4% |
| mdd_60d    | 15.2% |
| rsi_14     |  26.4 |
| zscore_20d |  -2.7 |

### Platinum / PL=F (score 17.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.8% |
| ret_5d     |  -4.3% |
| ret_20d    | -12.4% |
| ret_60d    | -10.5% |
| ma20_dist  |  -5.9% |
| ma50_dist  | -11.1% |
| vol_20d    |  28.9% |
| mdd_60d    |  18.8% |
| rsi_14     |   28.2 |
| zscore_20d |   -2.1 |

### Silver / SI=F (score 7.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.9% |
| ret_5d     |  -5.8% |
| ret_20d    | -16.4% |
| ret_60d    | -13.5% |
| ma20_dist  |  -8.5% |
| ma50_dist  | -14.9% |
| vol_20d    |  35.6% |
| mdd_60d    |  22.7% |
| rsi_14     |   26.6 |
| zscore_20d |   -2.2 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Brent Crude Oil / BZ=F              |   3.9829 |           3.4% |                 0.34x |        7.9657 |            6.8% |
| Apple Inc. / AAPL                   |   6.1850 |           1.8% |                 0.63x |       12.3700 |            3.6% |
| Microsoft Corporation / MSFT        |  11.0407 |           2.1% |                 0.52x |       22.0814 |            4.2% |
| Dow Jones Industrial Average / ^DJI | 533.4314 |           1.0% |                 1.03x |     1066.8627 |            2.0% |
| FTSE 100 / ^FTSE                    | 113.3786 |           1.1% |                 0.91x |      226.7571 |            2.1% |
| Tesla Inc. / TSLA                   |  11.7014 |           3.1% |                 0.28x |       23.4029 |            6.3% |
| UnitedHealth Group Inc. / UNH       |  13.0836 |           3.1% |                 0.36x |       26.1671 |            6.3% |
| Soybeans / ZS=F                     |  17.3750 |           1.4% |                 0.80x |       34.7500 |            2.8% |
| S&P 500 / ^GSPC                     |  72.1936 |           0.9% |                 1.04x |      144.3873 |            1.9% |
| DAX / ^GDAXI                        | 322.0476 |           1.3% |                 0.74x |      644.0951 |            2.6% |
| Russell 2000 / ^RUT                 |  34.6157 |           1.2% |                 0.71x |       69.2314 |            2.5% |
| CAC 40 / ^FCHI                      |  89.2736 |           1.1% |                 0.79x |      178.5472 |            2.3% |
| NASDAQ 100 / ^NDX                   | 498.5046 |           1.7% |                 0.55x |      997.0092 |            3.4% |
| JPMorgan Chase & Co. / JPM          |   6.3714 |           1.9% |                 0.70x |       12.7429 |            3.8% |
| Amazon.com Inc. / AMZN              |   7.0850 |           2.9% |                 0.31x |       14.1700 |            5.7% |
| Euro Stoxx 50 / ^STOXX50E           |  78.5751 |           1.3% |                 0.73x |      157.1501 |            2.6% |
| NVIDIA Corporation / NVDA           |   5.9779 |           2.8% |                 0.35x |       11.9557 |            5.7% |
| Hang Seng / ^HSI                    | 382.9873 |           1.7% |                 0.55x |      765.9746 |            3.3% |
| Corn / ZC=F                         |  10.1429 |           2.2% |                 0.46x |       20.2857 |            4.4% |
| Wheat / ZW=F                        |  15.2857 |           2.4% |                 0.50x |       30.5714 |            4.9% |
| Gold / GC=F                         |  71.8928 |           1.8% |                 0.54x |      143.7856 |            3.6% |
| Meta Platforms Inc. / META          |  25.2836 |           3.9% |                 0.25x |       50.5671 |            7.9% |
| Alphabet Inc. Class A / GOOGL       |   8.3879 |           2.6% |                 0.49x |       16.7757 |            5.2% |
| Platinum / PL=F                     |  27.5000 |           1.8% |                 0.35x |       55.0000 |            3.5% |
| Silver / SI=F                       |   1.2312 |           2.3% |                 0.28x |        2.4624 |            4.6% |

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

Scoring engine version: **1.0.0** | Git commit: **5b93153**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
