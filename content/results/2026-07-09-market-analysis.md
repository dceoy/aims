+++
title = "Market Analysis 2026-07-09"
date = "2026-07-09T00:00:00+00:00"
draft = false
summary = "Neutral market: 26 reliable instruments. Top signal: ZS=F (score 80.6)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-07-09.json", "data/history/2026-07-09.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "a790620"
+++

## Market Regime

**Neutral** — 15 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Soybeans / ZS=F** — score 80.6, 20d return +7.1%, RSI14=71. 20d up +7.1%; above MA20 by 5.6%; RSI14=71
- **Apple Inc. / AAPL** — score 79.1, 20d return +3.9%, RSI14=59. 20d up +3.9%; above MA20 by 6.0%; RSI14=59
- **UnitedHealth Group Inc. / UNH** — score 79.1, 20d return +5.3%, RSI14=60. 20d up +5.3%; above MA20 by 2.9%; RSI14=60 ⚠️ Upcoming: UNH earnings release (2026-07-16)
- **Dow Jones Industrial Average / ^DJI** — score 69.7, 20d return +3.1%, RSI14=56. 20d up +3.1%; above MA20 by 1.0%; RSI14=56
- **S&P 500 / ^GSPC** — score 62.1, 20d return +1.0%, RSI14=48. 20d up +1.0%; above MA20 by 0.6%; RSI14=48

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                | Applies To |
| ---------- | -------------------- | ---------- |
| 2026-07-14 | JPM earnings release | JPM        |
| 2026-07-16 | UNH earnings release | UNH        |

## Signal History

Compared with the previous available report (**2026-07-08**).
- **New top-5:** AAPL, ^GSPC
- **Persistent top signals:** ZS=F (3 reports), UNH (2 reports), ^DJI (2 reports)
- **Dropped from top-5:** JPM, ZC=F

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +0 |    +0.6 |
| 7203.T    |     +0 |    -7.6 |
| 8306.T    |     +0 |    -0.6 |
| AAPL      |     +6 |   +16.4 |
| AMZN      |     +0 |    +0.9 |
| BZ=F      |     +3 |   +16.4 |
| CL=F      |     +0 |   +13.3 |
| GC=F      |     -2 |    -5.8 |
| GOOGL     |     -2 |    -2.1 |
| HG=F      |     +0 |    -7.3 |
| JPM       |     -4 |   -11.8 |
| META      |     -2 |    -6.7 |
| MSFT      |     -3 |    -1.5 |
| NG=F      |     -3 |    -7.3 |
| NVDA      |     +9 |   +21.8 |
| PL=F      |     -2 |   -14.2 |
| SI=F      |     +0 |    -8.8 |
| TSLA      |     -4 |    -6.4 |
| UNH       |     -1 |    +2.1 |
| XOM       |     +0 |    +0.0 |
| ZC=F      |     -1 |    -6.4 |
| ZS=F      |     +0 |    +3.3 |
| ZW=F      |     -2 |    -3.3 |
| ^DJI      |     +0 |    +0.6 |
| ^FCHI     |     -5 |   -11.2 |
| ^FTSE     |     -4 |    -5.8 |
| ^GDAXI    |     -4 |   -10.3 |
| ^GSPC     |     +9 |   +10.0 |
| ^HSI      |    +10 |   +24.2 |
| ^N225     |     +0 |    -3.9 |
| ^NDX      |     +1 |   +12.4 |
| ^RUT      |     +5 |    +5.8 |
| ^STOXX50E |     -4 |    -7.0 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars
- **Copper / HG=F** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|    1 | Soybeans / ZS=F        |  80.6 |   Yes    | —               | 20d up +7.1%; above MA20 by 5.6%; RSI14=71    |
|    6 | Corn / ZC=F            |  61.5 |   Yes    | —               | 20d up +3.8%; above MA20 by 3.9%; RSI14=62    |
|    9 | Wheat / ZW=F           |  59.7 |   Yes    | —               | 20d up +2.8%; above MA20 by 1.3%; RSI14=51    |
|   12 | Natural Gas / NG=F     |  53.0 |   Yes    | —               | 20d up +2.1%; above MA20 by 0.2%; RSI14=49    |
|   22 | Brent Crude Oil / BZ=F |  33.0 |   Yes    | —               | 20d down -17.2%; below MA20 by 0.8%; RSI14=48 |
|   24 | Gold / GC=F            |  23.3 |   Yes    | —               | 20d down -6.1%; below MA20 by 1.8%; RSI14=33  |
|   25 | Platinum / PL=F        |  12.4 |   Yes    | —               | 20d down -9.9%; below MA20 by 5.0%; RSI14=28  |
|   26 | Silver / SI=F          |   4.5 |   Yes    | —               | 20d down -15.0%; below MA20 by 7.7%; RSI14=25 |
|   32 | Copper / HG=F          |  28.8 |    No    | malformed_input | Suppressed: malformed_input                   |
|   33 | WTI Crude Oil / CL=F   |  26.4 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    2 | Apple Inc. / AAPL                                                              |  79.1 |   Yes    | —                             | 20d up +3.9%; above MA20 by 6.0%; RSI14=59   |
|    3 | UnitedHealth Group Inc. / UNH                                                  |  79.1 |   Yes    | —                             | 20d up +5.3%; above MA20 by 2.9%; RSI14=60   |
|    7 | JPMorgan Chase & Co. / JPM                                                     |  61.2 |   Yes    | —                             | 20d up +6.7%; above MA20 by 1.2%; RSI14=51   |
|   13 | Meta Platforms Inc. / META                                                     |  51.2 |   Yes    | —                             | 20d up +3.1%; above MA20 by 4.5%; RSI14=51   |
|   15 | NVIDIA Corporation / NVDA                                                      |  48.2 |   Yes    | —                             | 20d down -2.2%; above MA20 by 1.2%; RSI14=47 |
|   17 | Amazon.com Inc. / AMZN                                                         |  46.4 |   Yes    | —                             | 20d down -0.7%; above MA20 by 1.6%; RSI14=48 |
|   18 | Alphabet Inc. Class A / GOOGL                                                  |  45.1 |   Yes    | —                             | 20d down -0.4%; above MA20 by 1.1%; RSI14=43 |
|   21 | Microsoft Corporation / MSFT                                                   |  34.5 |   Yes    | —                             | 20d down -6.9%; above MA20 by 0.3%; RSI14=45 |
|   23 | Tesla Inc. / TSLA                                                              |  26.4 |   Yes    | —                             | 20d down -3.6%; below MA20 by 1.3%; RSI14=47 |
|   27 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  81.8 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   28 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  68.8 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   29 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  53.0 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   30 | Exxon Mobil Corporation / XOM                                                  |  42.4 |    No    | malformed_input               | Suppressed: malformed_input                  |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    4 | Dow Jones Industrial Average / ^DJI |  69.7 |   Yes    | —            | 20d up +3.1%; above MA20 by 1.0%; RSI14=56   |
|    5 | S&P 500 / ^GSPC                     |  62.1 |   Yes    | —            | 20d up +1.0%; above MA20 by 0.6%; RSI14=48   |
|    8 | Russell 2000 / ^RUT                 |  60.6 |   Yes    | —            | 20d up +3.5%; below MA20 by 0.4%; RSI14=53   |
|   10 | FTSE 100 / ^FTSE                    |  57.6 |   Yes    | —            | 20d up +2.3%; below MA20 by 0.1%; RSI14=56   |
|   11 | Hang Seng / ^HSI                    |  53.6 |   Yes    | —            | 20d down -1.9%; above MA20 by 1.8%; RSI14=46 |
|   14 | DAX / ^GDAXI                        |  49.1 |   Yes    | —            | 20d up +2.9%; below MA20 by 0.5%; RSI14=48   |
|   16 | Euro Stoxx 50 / ^STOXX50E           |  48.2 |   Yes    | —            | 20d up +3.2%; below MA20 by 1.1%; RSI14=42   |
|   19 | NASDAQ 100 / ^NDX                   |  43.9 |   Yes    | —            | 20d down -0.5%; below MA20 by 1.2%; RSI14=44 |
|   20 | CAC 40 / ^FCHI                      |  37.3 |   Yes    | —            | 20d up +1.1%; below MA20 by 1.7%; RSI14=37   |
|   31 | Nikkei 225 / ^N225                  |  37.3 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-07-08 |
| 7203.T    | 2026-07-08 |
| 8306.T    | 2026-07-08 |
| AAPL      | 2026-07-08 |
| AMZN      | 2026-07-08 |
| BZ=F      | 2026-07-08 |
| CL=F      | 2026-07-08 |
| GC=F      | 2026-07-08 |
| GOOGL     | 2026-07-08 |
| HG=F      | 2026-07-08 |
| JPM       | 2026-07-08 |
| META      | 2026-07-08 |
| MSFT      | 2026-07-08 |
| NG=F      | 2026-07-08 |
| NVDA      | 2026-07-08 |
| PL=F      | 2026-07-08 |
| SI=F      | 2026-07-08 |
| TSLA      | 2026-07-08 |
| UNH       | 2026-07-08 |
| XOM       | 2026-07-08 |
| ZC=F      | 2026-07-08 |
| ZS=F      | 2026-07-08 |
| ZW=F      | 2026-07-08 |
| ^DJI      | 2026-07-08 |
| ^FCHI     | 2026-07-08 |
| ^FTSE     | 2026-07-08 |
| ^GDAXI    | 2026-07-08 |
| ^GSPC     | 2026-07-08 |
| ^HSI      | 2026-07-08 |
| ^N225     | 2026-07-08 |
| ^NDX      | 2026-07-08 |
| ^RUT      | 2026-07-08 |
| ^STOXX50E | 2026-07-08 |

## Symbol Details

### Soybeans / ZS=F (score 80.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | +7.0% |
| ret_20d    | +7.1% |
| ret_60d    | +1.6% |
| ma20_dist  | +5.6% |
| ma50_dist  | +2.9% |
| vol_20d    | 19.4% |
| mdd_60d    |  8.8% |
| rsi_14     |  71.0 |
| zscore_20d |   2.4 |

### Apple Inc. / AAPL (score 79.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.9% |
| ret_5d     |  +8.3% |
| ret_20d    |  +3.9% |
| ret_60d    | +20.4% |
| ma20_dist  |  +6.0% |
| ma50_dist  |  +5.9% |
| vol_20d    |  36.9% |
| mdd_60d    |  12.7% |
| rsi_14     |   59.5 |
| zscore_20d |    1.8 |

### UnitedHealth Group Inc. / UNH (score 79.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.6% |
| ret_5d     |  +2.4% |
| ret_20d    |  +5.3% |
| ret_60d    | +40.6% |
| ma20_dist  |  +2.9% |
| ma50_dist  |  +8.3% |
| vol_20d    |  24.7% |
| mdd_60d    |   6.1% |
| rsi_14     |   60.2 |
| zscore_20d |    1.3 |

### Dow Jones Industrial Average / ^DJI (score 69.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.1% |
| ret_5d     | +0.1% |
| ret_20d    | +3.1% |
| ret_60d    | +9.2% |
| ma20_dist  | +1.0% |
| ma50_dist  | +3.1% |
| vol_20d    | 12.6% |
| mdd_60d    |  3.2% |
| rsi_14     |  55.8 |
| zscore_20d |   0.7 |

### S&P 500 / ^GSPC (score 62.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | -0.2% |
| ret_20d    | +1.0% |
| ret_60d    | +9.8% |
| ma20_dist  | +0.6% |
| ma50_dist  | +0.9% |
| vol_20d    | 14.5% |
| mdd_60d    |  4.5% |
| rsi_14     |  47.6 |
| zscore_20d |   0.6 |

### Corn / ZC=F (score 61.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.8% |
| ret_5d     | +5.3% |
| ret_20d    | +3.8% |
| ret_60d    | -1.4% |
| ma20_dist  | +3.9% |
| ma50_dist  | -1.3% |
| vol_20d    | 24.9% |
| mdd_60d    | 15.7% |
| rsi_14     |  61.7 |
| zscore_20d |   1.6 |

### JPMorgan Chase & Co. / JPM (score 61.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.5% |
| ret_5d     | +1.5% |
| ret_20d    | +6.7% |
| ret_60d    | +7.2% |
| ma20_dist  | +1.2% |
| ma50_dist  | +5.7% |
| vol_20d    | 24.6% |
| mdd_60d    |  6.7% |
| rsi_14     |  50.9 |
| zscore_20d |   0.4 |

### Russell 2000 / ^RUT (score 60.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.9% |
| ret_5d     |  -2.2% |
| ret_20d    |  +3.5% |
| ret_60d    | +12.4% |
| ma20_dist  |  -0.4% |
| ma50_dist  |  +2.1% |
| vol_20d    |  16.4% |
| mdd_60d    |   4.8% |
| rsi_14     |   53.1 |
| zscore_20d |   -0.2 |

### Wheat / ZW=F (score 59.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.6% |
| ret_5d     | +3.2% |
| ret_20d    | +2.8% |
| ret_60d    | +5.0% |
| ma20_dist  | +1.3% |
| ma50_dist  | -2.1% |
| vol_20d    | 22.9% |
| mdd_60d    | 14.6% |
| rsi_14     |  51.4 |
| zscore_20d |   0.7 |

### FTSE 100 / ^FTSE (score 57.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.7% |
| ret_5d     | +0.1% |
| ret_20d    | +2.3% |
| ret_60d    | -0.9% |
| ma20_dist  | -0.1% |
| ma50_dist  | +0.8% |
| vol_20d    | 11.9% |
| mdd_60d    |  4.4% |
| rsi_14     |  56.2 |
| zscore_20d |  -0.1 |

### Hang Seng / ^HSI (score 53.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +3.0% |
| ret_5d     | +5.8% |
| ret_20d    | -1.9% |
| ret_60d    | -6.0% |
| ma20_dist  | +1.8% |
| ma50_dist  | -3.1% |
| vol_20d    | 20.8% |
| mdd_60d    | 14.9% |
| rsi_14     |  46.3 |
| zscore_20d |   0.7 |

### Natural Gas / NG=F (score 53.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.6% |
| ret_5d     |  -1.9% |
| ret_20d    |  +2.1% |
| ret_60d    | +21.3% |
| ma20_dist  |  +0.2% |
| ma50_dist  |  +5.2% |
| vol_20d    |  35.5% |
| mdd_60d    |   7.5% |
| rsi_14     |   48.6 |
| zscore_20d |    0.1 |

### Meta Platforms Inc. / META (score 51.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.0% |
| ret_5d     | +7.1% |
| ret_20d    | +3.1% |
| ret_60d    | -4.2% |
| ma20_dist  | +4.5% |
| ma50_dist  | +0.3% |
| vol_20d    | 50.5% |
| mdd_60d    | 21.1% |
| rsi_14     |  50.7 |
| zscore_20d |   1.3 |

### DAX / ^GDAXI (score 49.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.2% |
| ret_5d     | -0.6% |
| ret_20d    | +2.9% |
| ret_60d    | +3.5% |
| ma20_dist  | -0.5% |
| ma50_dist  | +0.5% |
| vol_20d    | 17.0% |
| mdd_60d    |  4.7% |
| rsi_14     |  48.1 |
| zscore_20d |  -0.3 |

### NVIDIA Corporation / NVDA (score 48.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +3.7% |
| ret_5d     | +2.0% |
| ret_20d    | -2.2% |
| ret_60d    | +8.2% |
| ma20_dist  | +1.2% |
| ma50_dist  | -2.6% |
| vol_20d    | 35.0% |
| mdd_60d    | 18.3% |
| rsi_14     |  46.6 |
| zscore_20d |   0.4 |

### Euro Stoxx 50 / ^STOXX50E (score 48.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.8% |
| ret_5d     | -1.2% |
| ret_20d    | +3.2% |
| ret_60d    | +4.7% |
| ma20_dist  | -1.1% |
| ma50_dist  | +2.0% |
| vol_20d    | 15.6% |
| mdd_60d    |  4.9% |
| rsi_14     |  41.9 |
| zscore_20d |  -0.8 |

### Amazon.com Inc. / AMZN (score 46.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | +2.2% |
| ret_20d    | -0.7% |
| ret_60d    | +2.2% |
| ma20_dist  | +1.6% |
| ma50_dist  | -4.3% |
| vol_20d    | 34.4% |
| mdd_60d    | 17.4% |
| rsi_14     |  48.0 |
| zscore_20d |   0.8 |

### Alphabet Inc. Class A / GOOGL (score 45.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.4% |
| ret_5d     |  +1.3% |
| ret_20d    |  -0.4% |
| ret_60d    | +14.2% |
| ma20_dist  |  +1.1% |
| ma50_dist  |  -2.8% |
| vol_20d    |  32.1% |
| mdd_60d    |  16.2% |
| rsi_14     |   43.1 |
| zscore_20d |    0.4 |

### NASDAQ 100 / ^NDX (score 43.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.3% |
| ret_5d     |  -3.4% |
| ret_20d    |  -0.5% |
| ret_60d    | +16.5% |
| ma20_dist  |  -1.2% |
| ma50_dist  |  -0.1% |
| vol_20d    |  29.1% |
| mdd_60d    |   7.0% |
| rsi_14     |   43.9 |
| zscore_20d |   -0.7 |

### CAC 40 / ^FCHI (score 37.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.2% |
| ret_5d     | -1.0% |
| ret_20d    | +1.1% |
| ret_60d    | -0.9% |
| ma20_dist  | -1.7% |
| ma50_dist  | +0.2% |
| vol_20d    | 13.8% |
| mdd_60d    |  5.6% |
| rsi_14     |  36.7 |
| zscore_20d |  -2.0 |

### Microsoft Corporation / MSFT (score 34.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.4% |
| ret_5d     | +2.8% |
| ret_20d    | -6.9% |
| ret_60d    | +3.6% |
| ma20_dist  | +0.3% |
| ma50_dist  | -5.3% |
| vol_20d    | 37.2% |
| mdd_60d    | 23.4% |
| rsi_14     |  45.4 |
| zscore_20d |   0.1 |

### Brent Crude Oil / BZ=F (score 33.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +5.2% |
| ret_5d     |  +7.0% |
| ret_20d    | -17.2% |
| ret_60d    | -18.0% |
| ma20_dist  |  -0.8% |
| ma50_dist  | -16.6% |
| vol_20d    |  44.4% |
| mdd_60d    |  39.4% |
| rsi_14     |   47.8 |
| zscore_20d |   -0.1 |

### Tesla Inc. / TSLA (score 26.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.2% |
| ret_5d     |  -6.3% |
| ret_20d    |  -3.6% |
| ret_60d    | +12.9% |
| ma20_dist  |  -1.3% |
| ma50_dist  |  -3.4% |
| vol_20d    |  60.9% |
| mdd_60d    |  15.8% |
| rsi_14     |   47.1 |
| zscore_20d |   -0.3 |

### Gold / GC=F (score 23.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.8% |
| ret_5d     |  +1.2% |
| ret_20d    |  -6.1% |
| ret_60d    | -14.5% |
| ma20_dist  |  -1.8% |
| ma50_dist  |  -7.4% |
| vol_20d    |  28.8% |
| mdd_60d    |  17.9% |
| rsi_14     |   32.9 |
| zscore_20d |   -0.7 |

### Platinum / PL=F (score 12.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -4.5% |
| ret_5d     |  +1.7% |
| ret_20d    |  -9.9% |
| ret_60d    | -23.1% |
| ma20_dist  |  -5.0% |
| ma50_dist  | -14.4% |
| vol_20d    |  41.1% |
| mdd_60d    |  29.1% |
| rsi_14     |   28.1 |
| zscore_20d |   -1.1 |

### Silver / SI=F (score 4.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -4.5% |
| ret_5d     |  -2.2% |
| ret_20d    | -15.0% |
| ret_60d    | -23.8% |
| ma20_dist  |  -7.7% |
| ma50_dist  | -18.1% |
| vol_20d    |  52.1% |
| mdd_60d    |  34.7% |
| rsi_14     |   24.7 |
| zscore_20d |   -1.2 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Soybeans / ZS=F                     |  19.3393 |           1.6% |                 0.52x |       38.6786 |            3.2% |
| Apple Inc. / AAPL                   |   8.9143 |           2.8% |                 0.27x |       17.8286 |            5.7% |
| UnitedHealth Group Inc. / UNH       |  10.4407 |           2.5% |                 0.41x |       20.8814 |            4.9% |
| Dow Jones Industrial Average / ^DJI | 577.7227 |           1.1% |                 0.80x |     1155.4453 |            2.2% |
| S&P 500 / ^GSPC                     |  90.0915 |           1.2% |                 0.69x |      180.1830 |            2.4% |
| Corn / ZC=F                         |   9.6964 |           2.2% |                 0.40x |       19.3929 |            4.5% |
| JPMorgan Chase & Co. / JPM          |   7.6783 |           2.3% |                 0.41x |       15.3566 |            4.6% |
| Russell 2000 / ^RUT                 |  46.6257 |           1.6% |                 0.61x |       93.2515 |            3.2% |
| Wheat / ZW=F                        |  14.6964 |           2.5% |                 0.44x |       29.3929 |            4.9% |
| FTSE 100 / ^FTSE                    | 118.7213 |           1.1% |                 0.84x |      237.4427 |            2.3% |
| Hang Seng / ^HSI                    | 482.4750 |           2.0% |                 0.48x |      964.9501 |            4.0% |
| Natural Gas / NG=F                  |   0.1354 |           4.2% |                 0.28x |        0.2707 |            8.4% |
| Meta Platforms Inc. / META          |  23.1636 |           3.8% |                 0.20x |       46.3271 |            7.7% |
| DAX / ^GDAXI                        | 351.1243 |           1.4% |                 0.59x |      702.2486 |            2.8% |
| NVIDIA Corporation / NVDA           |   6.6707 |           3.3% |                 0.29x |       13.3414 |            6.5% |
| Euro Stoxx 50 / ^STOXX50E           |  75.4292 |           1.2% |                 0.64x |      150.8584 |            2.4% |
| Amazon.com Inc. / AMZN              |   8.3264 |           3.4% |                 0.29x |       16.6528 |            6.8% |
| Alphabet Inc. Class A / GOOGL       |  11.8436 |           3.3% |                 0.31x |       23.6871 |            6.5% |
| NASDAQ 100 / ^NDX                   | 675.2970 |           2.3% |                 0.34x |     1350.5940 |            4.6% |
| CAC 40 / ^FCHI                      |  94.1843 |           1.1% |                 0.73x |      188.3686 |            2.3% |
| Microsoft Corporation / MSFT        |  12.8857 |           3.4% |                 0.27x |       25.7714 |            6.7% |
| Brent Crude Oil / BZ=F              |   3.3500 |           4.3% |                 0.23x |        6.7000 |            8.6% |
| Tesla Inc. / TSLA                   |  20.3629 |           5.2% |                 0.16x |       40.7257 |           10.3% |
| Gold / GC=F                         |  88.9000 |           2.2% |                 0.35x |      177.7999 |            4.4% |
| Platinum / PL=F                     |  44.5286 |           2.8% |                 0.24x |       89.0571 |            5.6% |
| Silver / SI=F                       |   2.4313 |           4.2% |                 0.19x |        4.8626 |            8.4% |

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

Scoring engine version: **1.0.0** | Git commit: **a790620**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
