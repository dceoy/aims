+++
title = "Market Analysis 2026-10-15"
date = "2026-10-15T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: MSFT (score 75.5)."
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
source_files = ["data/analysis/2026-10-15.json", "data/history/2026-10-15.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "21ee21e"
+++

## Market Regime

**Neutral** — 10 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Microsoft Corporation / MSFT** — score 75.5, 20d return +8.8%, RSI14=71. 20d up +8.8%; above MA20 by 3.4%; RSI14=71
- **Apple Inc. / AAPL** — score 71.8, 20d return +3.2%, RSI14=58. 20d up +3.2%; above MA20 by 1.8%; RSI14=58
- **FTSE 100 / ^FTSE** — score 70.3, 20d return +0.3%, RSI14=53. 20d up +0.3%; above MA20 by 1.0%; RSI14=53
- **UnitedHealth Group Inc. / UNH** — score 67.0, 20d return +5.4%, RSI14=66. 20d up +5.4%; above MA20 by 5.3%; RSI14=66
- **Brent Crude Oil / BZ=F** — score 64.2, 20d return +0.2%, RSI14=49. 20d up +0.2%; above MA20 by 2.6%; RSI14=49

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                 | Applies To |
| ---------- | --------------------- | ---------- |
| 2026-10-21 | TSLA earnings release | TSLA       |

## Signal History

Compared with the previous available report (**2026-10-14**).

- **New top-5:** BZ=F, UNH, ^FTSE
- **Persistent top signals:** MSFT (14 reports), AAPL (3 reports)
- **Dropped from top-5:** GOOGL, META, ^GSPC

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +1 |    +7.0 |
| 7203.T    |     +1 |    +5.2 |
| 8306.T    |     +0 |   -15.4 |
| AAPL      |     +2 |    +3.9 |
| AMZN      |     -3 |    -7.9 |
| BZ=F      |     +4 |    +9.1 |
| CL=F      |     +1 |    +9.7 |
| GC=F      |     -2 |    -0.9 |
| GOOGL     |     -5 |   -12.7 |
| HG=F      |     -2 |    -7.0 |
| JPM       |     +7 |   +18.2 |
| META      |     -7 |   -17.6 |
| MSFT      |     +0 |    -9.7 |
| NG=F      |     -2 |   -18.8 |
| NVDA      |    -11 |   -19.7 |
| PL=F      |     -1 |    -5.8 |
| SI=F      |     +0 |    -9.1 |
| TSLA      |     -4 |    -9.7 |
| UNH       |     +9 |   +22.4 |
| XOM       |     +0 |    +5.2 |
| ZC=F      |     +0 |    +2.1 |
| ZS=F      |     +2 |    +3.6 |
| ZW=F      |     +4 |   +16.4 |
| ^DJI      |     +5 |    +7.6 |
| ^FCHI     |     +4 |   +11.5 |
| ^FTSE     |     +5 |   +13.9 |
| ^GDAXI    |     +4 |    +8.2 |
| ^GSPC     |     -4 |   -10.9 |
| ^HSI      |     -2 |    +0.6 |
| ^N225     |     +1 |    +8.2 |
| ^NDX      |     -9 |   -12.1 |
| ^RUT      |     -3 |    -7.0 |
| ^STOXX50E |     +5 |   +11.5 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Exxon Mobil Corporation / XOM** — malformed_input
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Natural Gas / NG=F** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars
- **Copper / HG=F** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                    |
| ---: | ---------------------- | ----: | :------: | --------------- | ---------------------------------------------- |
|    5 | Brent Crude Oil / BZ=F |  64.2 |   Yes    | —               | 20d up +0.2%; above MA20 by 2.6%; RSI14=49     |
|   14 | Soybeans / ZS=F        |  45.8 |   Yes    | —               | 20d down -3.3%; below MA20 by 1.7%; RSI14=33   |
|   20 | Wheat / ZW=F           |  31.2 |   Yes    | —               | 20d down -7.9%; below MA20 by 3.0%; RSI14=35   |
|   21 | Gold / GC=F            |  29.1 |   Yes    | —               | 20d down -6.4%; below MA20 by 3.1%; RSI14=32   |
|   22 | Corn / ZC=F            |  22.4 |   Yes    | —               | 20d down -10.0%; below MA20 by 5.8%; RSI14=21  |
|   24 | Platinum / PL=F        |  11.8 |   Yes    | —               | 20d down -10.2%; below MA20 by 6.5%; RSI14=32  |
|   25 | Silver / SI=F          |   3.0 |   Yes    | —               | 20d down -13.6%; below MA20 by 10.0%; RSI14=26 |
|   29 | Natural Gas / NG=F     |  60.9 |    No    | malformed_input | Suppressed: malformed_input                    |
|   30 | WTI Crude Oil / CL=F   |  58.2 |    No    | malformed_input | Suppressed: malformed_input                    |
|   32 | Copper / HG=F          |  54.2 |    No    | malformed_input | Suppressed: malformed_input                    |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    1 | Microsoft Corporation / MSFT                                                   |  75.5 |   Yes    | —                             | 20d up +8.8%; above MA20 by 3.4%; RSI14=71   |
|    2 | Apple Inc. / AAPL                                                              |  71.8 |   Yes    | —                             | 20d up +3.2%; above MA20 by 1.8%; RSI14=58   |
|    4 | UnitedHealth Group Inc. / UNH                                                  |  67.0 |   Yes    | —                             | 20d up +5.4%; above MA20 by 5.3%; RSI14=66   |
|    9 | Meta Platforms Inc. / META                                                     |  52.4 |   Yes    | —                             | 20d up +9.6%; above MA20 by 0.9%; RSI14=40   |
|   10 | Alphabet Inc. Class A / GOOGL                                                  |  49.4 |   Yes    | —                             | 20d up +1.4%; above MA20 by 0.3%; RSI14=57   |
|   11 | JPMorgan Chase & Co. / JPM                                                     |  49.1 |   Yes    | —                             | 20d down -3.4%; below MA20 by 0.1%; RSI14=48 |
|   13 | Amazon.com Inc. / AMZN                                                         |  46.7 |   Yes    | —                             | 20d up +3.3%; above MA20 by 0.3%; RSI14=56   |
|   18 | NVIDIA Corporation / NVDA                                                      |  36.7 |   Yes    | —                             | 20d up +3.5%; below MA20 by 3.2%; RSI14=46   |
|   19 | Tesla Inc. / TSLA                                                              |  32.4 |   Yes    | —                             | 20d up +2.5%; below MA20 by 1.0%; RSI14=44   |
|   26 | Exxon Mobil Corporation / XOM                                                  |  88.2 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   27 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  77.0 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   28 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  69.1 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   33 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  23.9 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    3 | FTSE 100 / ^FTSE                    |  70.3 |   Yes    | —            | 20d up +0.3%; above MA20 by 1.0%; RSI14=53   |
|    6 | Dow Jones Industrial Average / ^DJI |  60.6 |   Yes    | —            | 20d up +0.3%; above MA20 by 0.2%; RSI14=54   |
|    7 | S&P 500 / ^GSPC                     |  58.5 |   Yes    | —            | 20d up +2.2%; below MA20 by 0.2%; RSI14=52   |
|    8 | DAX / ^GDAXI                        |  55.5 |   Yes    | —            | 20d down -0.9%; above MA20 by 0.0%; RSI14=51 |
|   12 | Euro Stoxx 50 / ^STOXX50E           |  47.6 |   Yes    | —            | 20d down -1.2%; below MA20 by 0.9%; RSI14=43 |
|   15 | NASDAQ 100 / ^NDX                   |  45.1 |   Yes    | —            | 20d up +3.5%; below MA20 by 1.9%; RSI14=41   |
|   16 | Hang Seng / ^HSI                    |  43.3 |   Yes    | —            | 20d down -1.4%; below MA20 by 0.6%; RSI14=40 |
|   17 | CAC 40 / ^FCHI                      |  40.0 |   Yes    | —            | 20d down -3.3%; below MA20 by 1.1%; RSI14=35 |
|   23 | Russell 2000 / ^RUT                 |  22.4 |   Yes    | —            | 20d down -4.5%; below MA20 by 3.3%; RSI14=28 |
|   31 | Nikkei 225 / ^N225                  |  56.7 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-10-14 |
| 7203.T    | 2026-10-14 |
| 8306.T    | 2026-10-14 |
| AAPL      | 2026-10-14 |
| AMZN      | 2026-10-14 |
| BZ=F      | 2026-10-14 |
| CL=F      | 2026-10-14 |
| GC=F      | 2026-10-14 |
| GOOGL     | 2026-10-14 |
| HG=F      | 2026-10-14 |
| JPM       | 2026-10-14 |
| META      | 2026-10-14 |
| MSFT      | 2026-10-14 |
| NG=F      | 2026-10-14 |
| NVDA      | 2026-10-14 |
| PL=F      | 2026-10-14 |
| SI=F      | 2026-10-14 |
| TSLA      | 2026-10-14 |
| UNH       | 2026-10-14 |
| XOM       | 2026-10-14 |
| ZC=F      | 2026-10-14 |
| ZS=F      | 2026-10-14 |
| ZW=F      | 2026-10-14 |
| ^DJI      | 2026-10-14 |
| ^FCHI     | 2026-10-14 |
| ^FTSE     | 2026-10-14 |
| ^GDAXI    | 2026-10-14 |
| ^GSPC     | 2026-10-14 |
| ^HSI      | 2026-10-14 |
| ^N225     | 2026-10-14 |
| ^NDX      | 2026-10-14 |
| ^RUT      | 2026-10-14 |
| ^STOXX50E | 2026-10-14 |

## Symbol Details

### Microsoft Corporation / MSFT (score 75.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.8% |
| ret_5d     |  +0.7% |
| ret_20d    |  +8.8% |
| ret_60d    | +34.4% |
| ma20_dist  |  +3.4% |
| ma50_dist  |  +6.0% |
| vol_20d    |  20.8% |
| mdd_60d    |   5.1% |
| rsi_14     |   71.2 |
| zscore_20d |    1.1 |

### Apple Inc. / AAPL (score 71.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | +1.9% |
| ret_20d    | +3.2% |
| ret_60d    | +4.7% |
| ma20_dist  | +1.8% |
| ma50_dist  | +5.7% |
| vol_20d    | 16.4% |
| mdd_60d    | 11.0% |
| rsi_14     |  57.8 |
| zscore_20d |   1.7 |

### FTSE 100 / ^FTSE (score 70.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | +2.5% |
| ret_20d    | +0.3% |
| ret_60d    | +1.3% |
| ma20_dist  | +1.0% |
| ma50_dist  | +0.1% |
| vol_20d    | 11.8% |
| mdd_60d    |  4.4% |
| rsi_14     |  52.8 |
| zscore_20d |   1.0 |

### UnitedHealth Group Inc. / UNH (score 67.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +4.7% |
| ret_5d     | +5.2% |
| ret_20d    | +5.4% |
| ret_60d    | -9.3% |
| ma20_dist  | +5.3% |
| ma50_dist  | +2.4% |
| vol_20d    | 23.3% |
| mdd_60d    | 15.3% |
| rsi_14     |  66.0 |
| zscore_20d |   3.4 |

### Brent Crude Oil / BZ=F (score 64.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.4% |
| ret_5d     |  +5.8% |
| ret_20d    |  +0.2% |
| ret_60d    | +20.0% |
| ma20_dist  |  +2.6% |
| ma50_dist  |  +8.2% |
| vol_20d    |  31.8% |
| mdd_60d    |  12.5% |
| rsi_14     |   48.5 |
| zscore_20d |    1.2 |

### Dow Jones Industrial Average / ^DJI (score 60.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | +0.9% |
| ret_20d    | +0.3% |
| ret_60d    | -1.2% |
| ma20_dist  | +0.2% |
| ma50_dist  | -1.8% |
| vol_20d    |  8.4% |
| mdd_60d    |  6.3% |
| rsi_14     |  54.2 |
| zscore_20d |   0.4 |

### S&P 500 / ^GSPC (score 58.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.1% |
| ret_5d     | -1.1% |
| ret_20d    | +2.2% |
| ret_60d    | +2.8% |
| ma20_dist  | -0.2% |
| ma50_dist  | +0.2% |
| vol_20d    | 10.1% |
| mdd_60d    |  3.2% |
| rsi_14     |  51.5 |
| zscore_20d |  -0.2 |

### DAX / ^GDAXI (score 55.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | +0.8% |
| ret_20d    | -0.9% |
| ret_60d    | +0.6% |
| ma20_dist  | +0.0% |
| ma50_dist  | -1.8% |
| vol_20d    | 13.3% |
| mdd_60d    |  6.6% |
| rsi_14     |  50.7 |
| zscore_20d |   0.0 |

### Meta Platforms Inc. / META (score 52.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -3.3% |
| ret_5d     |  +2.3% |
| ret_20d    |  +9.6% |
| ret_60d    | +14.6% |
| ma20_dist  |  +0.9% |
| ma50_dist  | +13.5% |
| vol_20d    |  55.1% |
| mdd_60d    |  14.1% |
| rsi_14     |   40.3 |
| zscore_20d |    0.3 |

### Alphabet Inc. Class A / GOOGL (score 49.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.7% |
| ret_5d     | -0.8% |
| ret_20d    | +1.4% |
| ret_60d    | +0.1% |
| ma20_dist  | +0.3% |
| ma50_dist  | +0.7% |
| vol_20d    | 20.9% |
| mdd_60d    | 12.4% |
| rsi_14     |  56.7 |
| zscore_20d |   0.2 |

### JPMorgan Chase & Co. / JPM (score 49.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.2% |
| ret_5d     | +1.7% |
| ret_20d    | -3.4% |
| ret_60d    | -2.9% |
| ma20_dist  | -0.1% |
| ma50_dist  | -3.7% |
| vol_20d    | 17.0% |
| mdd_60d    |  9.9% |
| rsi_14     |  47.6 |
| zscore_20d |  -0.1 |

### Euro Stoxx 50 / ^STOXX50E (score 47.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | +0.2% |
| ret_20d    | -1.2% |
| ret_60d    | -2.0% |
| ma20_dist  | -0.9% |
| ma50_dist  | -2.6% |
| vol_20d    | 13.0% |
| mdd_60d    |  6.5% |
| rsi_14     |  42.8 |
| zscore_20d |  -0.9 |

### Amazon.com Inc. / AMZN (score 46.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.7% |
| ret_5d     | -2.2% |
| ret_20d    | +3.3% |
| ret_60d    | +2.6% |
| ma20_dist  | +0.3% |
| ma50_dist  | -1.5% |
| vol_20d    | 24.2% |
| mdd_60d    | 13.4% |
| rsi_14     |  55.6 |
| zscore_20d |   0.2 |

### Soybeans / ZS=F (score 45.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | -1.6% |
| ret_20d    | -3.3% |
| ret_60d    | +2.3% |
| ma20_dist  | -1.7% |
| ma50_dist  | +0.9% |
| vol_20d    | 14.2% |
| mdd_60d    |  5.3% |
| rsi_14     |  33.3 |
| zscore_20d |  -1.3 |

### NASDAQ 100 / ^NDX (score 45.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.0% |
| ret_5d     | -3.9% |
| ret_20d    | +3.5% |
| ret_60d    | +2.7% |
| ma20_dist  | -1.9% |
| ma50_dist  | +0.3% |
| vol_20d    | 16.9% |
| mdd_60d    |  6.2% |
| rsi_14     |  41.2 |
| zscore_20d |  -1.3 |

### Hang Seng / ^HSI (score 43.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | +0.8% |
| ret_20d    | -1.4% |
| ret_60d    | -3.3% |
| ma20_dist  | -0.6% |
| ma50_dist  | -2.9% |
| vol_20d    | 15.2% |
| mdd_60d    |  8.5% |
| rsi_14     |  40.4 |
| zscore_20d |  -0.5 |

### CAC 40 / ^FCHI (score 40.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | +1.3% |
| ret_20d    | -3.3% |
| ret_60d    | -6.7% |
| ma20_dist  | -1.1% |
| ma50_dist  | -4.3% |
| vol_20d    | 12.1% |
| mdd_60d    | 11.4% |
| rsi_14     |  35.0 |
| zscore_20d |  -0.6 |

### NVIDIA Corporation / NVDA (score 36.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -3.2% |
| ret_5d     | -6.8% |
| ret_20d    | +3.5% |
| ret_60d    | +6.8% |
| ma20_dist  | -3.2% |
| ma50_dist  | -0.8% |
| vol_20d    | 24.8% |
| mdd_60d    | 10.4% |
| rsi_14     |  45.9 |
| zscore_20d |  -1.4 |

### Tesla Inc. / TSLA (score 32.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.2% |
| ret_5d     | -2.8% |
| ret_20d    | +2.5% |
| ret_60d    | -3.1% |
| ma20_dist  | -1.0% |
| ma50_dist  | +2.6% |
| vol_20d    | 30.6% |
| mdd_60d    | 20.2% |
| rsi_14     |  43.5 |
| zscore_20d |  -0.4 |

### Wheat / ZW=F (score 31.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | -1.9% |
| ret_20d    | -7.9% |
| ret_60d    | -0.7% |
| ma20_dist  | -3.0% |
| ma50_dist  | -3.7% |
| vol_20d    | 20.6% |
| mdd_60d    | 12.7% |
| rsi_14     |  34.6 |
| zscore_20d |  -1.1 |

### Gold / GC=F (score 29.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.7% |
| ret_5d     | -0.8% |
| ret_20d    | -6.4% |
| ret_60d    | +0.8% |
| ma20_dist  | -3.1% |
| ma50_dist  | -6.3% |
| vol_20d    | 16.8% |
| mdd_60d    | 12.7% |
| rsi_14     |  31.6 |
| zscore_20d |  -1.4 |

### Corn / ZC=F (score 22.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.4% |
| ret_5d     |  -4.2% |
| ret_20d    | -10.0% |
| ret_60d    |  +3.6% |
| ma20_dist  |  -5.8% |
| ma50_dist  |  -3.9% |
| vol_20d    |  25.0% |
| mdd_60d    |  11.6% |
| rsi_14     |   20.5 |
| zscore_20d |   -1.5 |

### Russell 2000 / ^RUT (score 22.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.9% |
| ret_5d     | -2.3% |
| ret_20d    | -4.5% |
| ret_60d    | -8.6% |
| ma20_dist  | -3.3% |
| ma50_dist  | -6.5% |
| vol_20d    | 12.1% |
| mdd_60d    | 11.0% |
| rsi_14     |  27.7 |
| zscore_20d |  -2.5 |

### Platinum / PL=F (score 11.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -3.4% |
| ret_5d     |  -2.0% |
| ret_20d    | -10.2% |
| ret_60d    |  -1.2% |
| ma20_dist  |  -6.5% |
| ma50_dist  |  -9.4% |
| vol_20d    |  30.7% |
| mdd_60d    |  16.4% |
| rsi_14     |   31.7 |
| zscore_20d |   -1.8 |

### Silver / SI=F (score 3.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -6.1% |
| ret_5d     |  -7.3% |
| ret_20d    | -13.6% |
| ret_60d    |  -5.0% |
| ma20_dist  | -10.0% |
| ma50_dist  | -13.7% |
| vol_20d    |  33.6% |
| mdd_60d    |  20.0% |
| rsi_14     |   25.8 |
| zscore_20d |   -2.2 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Microsoft Corporation / MSFT        |  12.2264 |           2.3% |                 0.48x |       24.4529 |            4.6% |
| Apple Inc. / AAPL                   |   6.5814 |           1.9% |                 0.61x |       13.1629 |            3.8% |
| FTSE 100 / ^FTSE                    | 113.3713 |           1.1% |                 0.85x |      226.7426 |            2.1% |
| UnitedHealth Group Inc. / UNH       |  11.1764 |           2.8% |                 0.43x |       22.3529 |            5.7% |
| Brent Crude Oil / BZ=F              |   3.9971 |           3.8% |                 0.31x |        7.9943 |            7.5% |
| Dow Jones Industrial Average / ^DJI | 491.8019 |           1.0% |                 1.19x |      983.6038 |            1.9% |
| S&P 500 / ^GSPC                     |  64.1286 |           0.8% |                 0.99x |      128.2572 |            1.7% |
| DAX / ^GDAXI                        | 291.8842 |           1.2% |                 0.75x |      583.7684 |            2.3% |
| Meta Platforms Inc. / META          |  22.4964 |           3.1% |                 0.18x |       44.9929 |            6.1% |
| Alphabet Inc. Class A / GOOGL       |   8.0436 |           2.3% |                 0.48x |       16.0871 |            4.6% |
| JPMorgan Chase & Co. / JPM          |   5.9443 |           1.8% |                 0.59x |       11.8887 |            3.5% |
| Euro Stoxx 50 / ^STOXX50E           |  73.5686 |           1.2% |                 0.77x |      147.1372 |            2.4% |
| Amazon.com Inc. / AMZN              |   5.5271 |           2.2% |                 0.41x |       11.0543 |            4.4% |
| Soybeans / ZS=F                     |  22.0714 |           1.7% |                 0.70x |       44.1429 |            3.5% |
| NASDAQ 100 / ^NDX                   | 366.9890 |           1.2% |                 0.59x |      733.9780 |            2.5% |
| Hang Seng / ^HSI                    | 342.1723 |           1.4% |                 0.66x |      684.3446 |            2.8% |
| CAC 40 / ^FCHI                      |  89.3985 |           1.1% |                 0.83x |      178.7970 |            2.3% |
| NVIDIA Corporation / NVDA           |   5.6286 |           2.5% |                 0.40x |       11.2571 |            5.1% |
| Tesla Inc. / TSLA                   |  10.9550 |           3.0% |                 0.33x |       21.9100 |            6.0% |
| Wheat / ZW=F                        |  17.1786 |           2.6% |                 0.49x |       34.3571 |            5.1% |
| Gold / GC=F                         |  79.9785 |           1.9% |                 0.60x |      159.9570 |            3.9% |
| Corn / ZC=F                         |  12.3929 |           2.6% |                 0.40x |       24.7857 |            5.2% |
| Russell 2000 / ^RUT                 |  34.0522 |           1.2% |                 0.83x |       68.1043 |            2.5% |
| Platinum / PL=F                     |  36.1929 |           2.3% |                 0.33x |       72.3857 |            4.5% |
| Silver / SI=F                       |   1.3939 |           2.5% |                 0.30x |        2.7879 |            5.0% |

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

Scoring engine version: **1.0.0** | Git commit: **21ee21e**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
