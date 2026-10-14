+++
title = "Market Analysis 2026-10-14"
date = "2026-10-14T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: MSFT (score 85.2)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-10-14.json", "data/history/2026-10-14.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "714eb72"
+++

## Market Regime

**Neutral** — 13 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Microsoft Corporation / MSFT** — score 85.2, 20d return +9.3%, RSI14=78. 20d up +9.3%; above MA20 by 5.7%; RSI14=78
- **Meta Platforms Inc. / META** — score 70.0, 20d return +13.9%, RSI14=54. 20d up +13.9%; above MA20 by 4.8%; RSI14=54
- **S&P 500 / ^GSPC** — score 69.4, 20d return +2.9%, RSI14=62. 20d up +2.9%; above MA20 by 1.0%; RSI14=62
- **Apple Inc. / AAPL** — score 67.9, 20d return +3.0%, RSI14=55. 20d up +3.0%; above MA20 by 1.5%; RSI14=55
- **Alphabet Inc. Class A / GOOGL** — score 62.1, 20d return +2.6%, RSI14=71. 20d up +2.6%; above MA20 by 2.1%; RSI14=71

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                 | Applies To |
| ---------- | --------------------- | ---------- |
| 2026-10-21 | TSLA earnings release | TSLA       |

## Signal History

Compared with the previous available report (**2026-10-13**).

- **New top-5:** GOOGL
- **Persistent top signals:** MSFT (13 reports), ^GSPC (11 reports), AAPL (2 reports), META (2 reports)
- **Dropped from top-5:** BZ=F

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     -1 |    -1.8 |
| 7203.T    |     +2 |   +17.3 |
| 8306.T    |     +0 |   +19.4 |
| AAPL      |     -2 |    +0.0 |
| AMZN      |     +0 |    -2.7 |
| BZ=F      |     -6 |   -12.1 |
| CL=F      |     +1 |    +3.6 |
| GC=F      |     +0 |    -0.9 |
| GOOGL     |     +2 |    +3.6 |
| HG=F      |     -2 |    -7.0 |
| JPM       |     -1 |    -8.5 |
| META      |     +3 |    +6.4 |
| MSFT      |     +0 |    -0.6 |
| NG=F      |     +2 |   +14.6 |
| NVDA      |     +5 |   +10.3 |
| PL=F      |     -1 |    -5.5 |
| SI=F      |     -1 |    -6.4 |
| TSLA      |     +0 |    -0.3 |
| UNH       |     +3 |    +4.2 |
| XOM       |     +0 |    -0.6 |
| ZC=F      |     +1 |    -1.5 |
| ZS=F      |     -3 |    -1.8 |
| ZW=F      |     +1 |    -2.7 |
| ^DJI      |     -3 |    -4.8 |
| ^FCHI     |     -1 |    +0.3 |
| ^FTSE     |     -2 |    -3.0 |
| ^GDAXI    |     -1 |    -4.5 |
| ^GSPC     |     +1 |    +2.7 |
| ^HSI      |     +4 |    +3.3 |
| ^N225     |     -2 |   -14.2 |
| ^NDX      |     +3 |    -0.6 |
| ^RUT      |     +1 |    +1.8 |
| ^STOXX50E |     -3 |    -7.9 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Exxon Mobil Corporation / XOM** — malformed_input
- **Natural Gas / NG=F** — malformed_input
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|    9 | Brent Crude Oil / BZ=F |  55.1 |   Yes    | —               | 20d down -2.8%; above MA20 by 2.3%; RSI14=56 |
|   16 | Soybeans / ZS=F        |  42.1 |   Yes    | —               | 20d down -2.7%; below MA20 by 1.3%; RSI14=35 |
|   19 | Gold / GC=F            |  30.0 |   Yes    | —               | 20d down -3.6%; below MA20 by 1.8%; RSI14=35 |
|   22 | Corn / ZC=F            |  20.3 |   Yes    | —               | 20d down -9.9%; below MA20 by 5.9%; RSI14=21 |
|   23 | Platinum / PL=F        |  17.6 |   Yes    | —               | 20d down -6.5%; below MA20 by 3.7%; RSI14=37 |
|   24 | Wheat / ZW=F           |  14.8 |   Yes    | —               | 20d down -8.1%; below MA20 by 4.0%; RSI14=32 |
|   25 | Silver / SI=F          |  12.1 |   Yes    | —               | 20d down -6.4%; below MA20 by 4.9%; RSI14=31 |
|   27 | Natural Gas / NG=F     |  79.7 |    No    | malformed_input | Suppressed: malformed_input                  |
|   30 | Copper / HG=F          |  61.2 |    No    | malformed_input | Suppressed: malformed_input                  |
|   31 | WTI Crude Oil / CL=F   |  48.5 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    1 | Microsoft Corporation / MSFT                                                   |  85.2 |   Yes    | —                             | 20d up +9.3%; above MA20 by 5.7%; RSI14=78   |
|    2 | Meta Platforms Inc. / META                                                     |  70.0 |   Yes    | —                             | 20d up +13.9%; above MA20 by 4.8%; RSI14=54  |
|    4 | Apple Inc. / AAPL                                                              |  67.9 |   Yes    | —                             | 20d up +3.0%; above MA20 by 1.5%; RSI14=55   |
|    5 | Alphabet Inc. Class A / GOOGL                                                  |  62.1 |   Yes    | —                             | 20d up +2.6%; above MA20 by 2.1%; RSI14=71   |
|    7 | NVIDIA Corporation / NVDA                                                      |  56.4 |   Yes    | —                             | 20d up +7.7%; above MA20 by 0.1%; RSI14=54   |
|   10 | Amazon.com Inc. / AMZN                                                         |  54.5 |   Yes    | —                             | 20d up +4.1%; above MA20 by 2.3%; RSI14=62   |
|   13 | UnitedHealth Group Inc. / UNH                                                  |  44.5 |   Yes    | —                             | 20d up +0.5%; above MA20 by 0.8%; RSI14=56   |
|   15 | Tesla Inc. / TSLA                                                              |  42.1 |   Yes    | —                             | 20d up +5.2%; above MA20 by 1.3%; RSI14=47   |
|   18 | JPMorgan Chase & Co. / JPM                                                     |  30.9 |   Yes    | —                             | 20d down -5.5%; below MA20 by 1.5%; RSI14=43 |
|   26 | Exxon Mobil Corporation / XOM                                                  |  83.0 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   28 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  70.0 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   29 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  63.9 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   33 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  39.4 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    3 | S&P 500 / ^GSPC                     |  69.4 |   Yes    | —            | 20d up +2.9%; above MA20 by 1.0%; RSI14=62   |
|    6 | NASDAQ 100 / ^NDX                   |  57.3 |   Yes    | —            | 20d up +5.6%; above MA20 by 0.3%; RSI14=52   |
|    8 | FTSE 100 / ^FTSE                    |  56.4 |   Yes    | —            | 20d down -0.1%; above MA20 by 0.3%; RSI14=46 |
|   11 | Dow Jones Industrial Average / ^DJI |  53.0 |   Yes    | —            | 20d down -0.8%; above MA20 by 0.4%; RSI14=52 |
|   12 | DAX / ^GDAXI                        |  47.3 |   Yes    | —            | 20d down -0.6%; below MA20 by 0.2%; RSI14=47 |
|   14 | Hang Seng / ^HSI                    |  42.7 |   Yes    | —            | 20d down -2.3%; below MA20 by 0.6%; RSI14=37 |
|   17 | Euro Stoxx 50 / ^STOXX50E           |  36.1 |   Yes    | —            | 20d down -1.1%; below MA20 by 1.3%; RSI14=38 |
|   20 | Russell 2000 / ^RUT                 |  29.4 |   Yes    | —            | 20d down -3.0%; below MA20 by 1.6%; RSI14=35 |
|   21 | CAC 40 / ^FCHI                      |  28.5 |   Yes    | —            | 20d down -3.2%; below MA20 by 1.8%; RSI14=29 |
|   32 | Nikkei 225 / ^N225                  |  48.5 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-10-13 |
| 7203.T    | 2026-10-13 |
| 8306.T    | 2026-10-13 |
| AAPL      | 2026-10-13 |
| AMZN      | 2026-10-13 |
| BZ=F      | 2026-10-13 |
| CL=F      | 2026-10-13 |
| GC=F      | 2026-10-13 |
| GOOGL     | 2026-10-13 |
| HG=F      | 2026-10-13 |
| JPM       | 2026-10-13 |
| META      | 2026-10-13 |
| MSFT      | 2026-10-13 |
| NG=F      | 2026-10-13 |
| NVDA      | 2026-10-13 |
| PL=F      | 2026-10-13 |
| SI=F      | 2026-10-13 |
| TSLA      | 2026-10-13 |
| UNH       | 2026-10-13 |
| XOM       | 2026-10-13 |
| ZC=F      | 2026-10-13 |
| ZS=F      | 2026-10-13 |
| ZW=F      | 2026-10-13 |
| ^DJI      | 2026-10-13 |
| ^FCHI     | 2026-10-13 |
| ^FTSE     | 2026-10-13 |
| ^GDAXI    | 2026-10-13 |
| ^GSPC     | 2026-10-13 |
| ^HSI      | 2026-10-13 |
| ^N225     | 2026-10-13 |
| ^NDX      | 2026-10-13 |
| ^RUT      | 2026-10-13 |
| ^STOXX50E | 2026-10-13 |

## Symbol Details

### Microsoft Corporation / MSFT (score 85.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.4% |
| ret_5d     |  +2.7% |
| ret_20d    |  +9.3% |
| ret_60d    | +35.3% |
| ma20_dist  |  +5.7% |
| ma50_dist  |  +8.1% |
| vol_20d    |  20.3% |
| mdd_60d    |   5.1% |
| rsi_14     |   77.8 |
| zscore_20d |    1.9 |

### Meta Platforms Inc. / META (score 70.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.6% |
| ret_5d     |  +3.2% |
| ret_20d    | +13.9% |
| ret_60d    | +18.1% |
| ma20_dist  |  +4.8% |
| ma50_dist  | +17.9% |
| vol_20d    |  53.4% |
| mdd_60d    |  16.3% |
| rsi_14     |   54.3 |
| zscore_20d |    1.3 |

### S&P 500 / ^GSPC (score 69.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.0% |
| ret_5d     | -0.2% |
| ret_20d    | +2.9% |
| ret_60d    | +4.9% |
| ma20_dist  | +1.0% |
| ma50_dist  | +1.3% |
| vol_20d    |  9.3% |
| mdd_60d    |  3.2% |
| rsi_14     |  62.2 |
| zscore_20d |   1.1 |

### Apple Inc. / AAPL (score 67.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | +2.3% |
| ret_20d    | +3.0% |
| ret_60d    | +4.6% |
| ma20_dist  | +1.5% |
| ma50_dist  | +5.4% |
| vol_20d    | 16.3% |
| mdd_60d    | 11.0% |
| rsi_14     |  54.8 |
| zscore_20d |   1.4 |

### Alphabet Inc. Class A / GOOGL (score 62.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +1.8% |
| ret_20d    | +2.6% |
| ret_60d    | +0.5% |
| ma20_dist  | +2.1% |
| ma50_dist  | +2.3% |
| vol_20d    | 20.0% |
| mdd_60d    | 12.4% |
| rsi_14     |  71.0 |
| zscore_20d |   1.5 |

### NASDAQ 100 / ^NDX (score 57.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | -2.1% |
| ret_20d    | +5.6% |
| ret_60d    | +6.9% |
| ma20_dist  | +0.3% |
| ma50_dist  | +2.4% |
| vol_20d    | 14.9% |
| mdd_60d    |  6.7% |
| rsi_14     |  52.1 |
| zscore_20d |   0.2 |

### NVIDIA Corporation / NVDA (score 56.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.0% |
| ret_5d     |  -4.5% |
| ret_20d    |  +7.7% |
| ret_60d    | +12.4% |
| ma20_dist  |  +0.1% |
| ma50_dist  |  +2.5% |
| vol_20d    |  21.7% |
| mdd_60d    |  10.4% |
| rsi_14     |   54.4 |
| zscore_20d |    0.0 |

### FTSE 100 / ^FTSE (score 56.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | +1.0% |
| ret_20d    | -0.1% |
| ret_60d    | +1.2% |
| ma20_dist  | +0.3% |
| ma50_dist  | -0.7% |
| vol_20d    | 11.5% |
| mdd_60d    |  4.4% |
| rsi_14     |  46.3 |
| zscore_20d |   0.3 |

### Brent Crude Oil / BZ=F (score 55.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.9% |
| ret_5d     | +5.1% |
| ret_20d    | -2.8% |
| ret_60d    | +9.2% |
| ma20_dist  | +2.3% |
| ma50_dist  | +8.3% |
| vol_20d    | 33.1% |
| mdd_60d    | 12.5% |
| rsi_14     |  56.0 |
| zscore_20d |   1.1 |

### Amazon.com Inc. / AMZN (score 54.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | +0.9% |
| ret_20d    | +4.1% |
| ret_60d    | +3.4% |
| ma20_dist  | +2.3% |
| ma50_dist  | +0.1% |
| vol_20d    | 23.5% |
| mdd_60d    | 13.4% |
| rsi_14     |  62.3 |
| zscore_20d |   1.2 |

### Dow Jones Industrial Average / ^DJI (score 53.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | +0.3% |
| ret_20d    | -0.8% |
| ret_60d    | -0.3% |
| ma20_dist  | +0.4% |
| ma50_dist  | -1.8% |
| vol_20d    |  9.4% |
| mdd_60d    |  6.3% |
| rsi_14     |  52.4 |
| zscore_20d |   0.6 |

### DAX / ^GDAXI (score 47.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | -0.7% |
| ret_20d    | -0.6% |
| ret_60d    | +1.0% |
| ma20_dist  | -0.2% |
| ma50_dist  | -2.0% |
| vol_20d    | 13.4% |
| mdd_60d    |  6.6% |
| rsi_14     |  46.9 |
| zscore_20d |  -0.2 |

### UnitedHealth Group Inc. / UNH (score 44.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.2% |
| ret_5d     |  +0.4% |
| ret_20d    |  +0.5% |
| ret_60d    | -10.4% |
| ma20_dist  |  +0.8% |
| ma50_dist  |  -2.3% |
| vol_20d    |  16.8% |
| mdd_60d    |  16.3% |
| rsi_14     |   56.5 |
| zscore_20d |    0.8 |

### Hang Seng / ^HSI (score 42.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +0.3% |
| ret_20d    | -2.3% |
| ret_60d    | -3.2% |
| ma20_dist  | -0.6% |
| ma50_dist  | -2.9% |
| vol_20d    | 15.6% |
| mdd_60d    |  8.5% |
| rsi_14     |  37.3 |
| zscore_20d |  -0.4 |

### Tesla Inc. / TSLA (score 42.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | -1.4% |
| ret_20d    | +5.2% |
| ret_60d    | +1.5% |
| ma20_dist  | +1.3% |
| ma50_dist  | +5.1% |
| vol_20d    | 29.4% |
| mdd_60d    | 21.3% |
| rsi_14     |  46.8 |
| zscore_20d |   0.5 |

### Soybeans / ZS=F (score 42.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | -1.5% |
| ret_20d    | -2.7% |
| ret_60d    | +3.7% |
| ma20_dist  | -1.3% |
| ma50_dist  | +1.6% |
| vol_20d    | 14.2% |
| mdd_60d    |  8.1% |
| rsi_14     |  35.1 |
| zscore_20d |  -1.1 |

### Euro Stoxx 50 / ^STOXX50E (score 36.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | -1.7% |
| ret_20d    | -1.1% |
| ret_60d    | -1.9% |
| ma20_dist  | -1.3% |
| ma50_dist  | -3.0% |
| vol_20d    | 13.0% |
| mdd_60d    |  6.5% |
| rsi_14     |  38.4 |
| zscore_20d |  -1.4 |

### JPMorgan Chase & Co. / JPM (score 30.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.9% |
| ret_5d     | +0.0% |
| ret_20d    | -5.5% |
| ret_60d    | -2.2% |
| ma20_dist  | -1.5% |
| ma50_dist  | -4.9% |
| vol_20d    | 16.5% |
| mdd_60d    |  9.9% |
| rsi_14     |  42.8 |
| zscore_20d |  -0.7 |

### Gold / GC=F (score 30.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | -0.2% |
| ret_20d    | -3.6% |
| ret_60d    | +2.7% |
| ma20_dist  | -1.8% |
| ma50_dist  | -4.9% |
| vol_20d    | 16.9% |
| mdd_60d    | 12.0% |
| rsi_14     |  34.9 |
| zscore_20d |  -0.8 |

### Russell 2000 / ^RUT (score 29.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -1.7% |
| ret_20d    | -3.0% |
| ret_60d    | -5.4% |
| ma20_dist  | -1.6% |
| ma50_dist  | -4.8% |
| vol_20d    | 10.4% |
| mdd_60d    |  9.3% |
| rsi_14     |  35.2 |
| zscore_20d |  -1.5 |

### CAC 40 / ^FCHI (score 28.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | -0.5% |
| ret_20d    | -3.2% |
| ret_60d    | -6.4% |
| ma20_dist  | -1.8% |
| ma50_dist  | -5.1% |
| vol_20d    | 12.1% |
| mdd_60d    | 11.4% |
| rsi_14     |  28.5 |
| zscore_20d |  -1.0 |

### Corn / ZC=F (score 20.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | -5.0% |
| ret_20d    | -9.9% |
| ret_60d    | +4.0% |
| ma20_dist  | -5.9% |
| ma50_dist  | -3.3% |
| vol_20d    | 25.1% |
| mdd_60d    | 11.6% |
| rsi_14     |  20.6 |
| zscore_20d |  -1.6 |

### Platinum / PL=F (score 17.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.3% |
| ret_5d     | -2.1% |
| ret_20d    | -6.5% |
| ret_60d    | +4.0% |
| ma20_dist  | -3.7% |
| ma50_dist  | -6.4% |
| vol_20d    | 29.0% |
| mdd_60d    | 15.1% |
| rsi_14     |  37.5 |
| zscore_20d |  -1.1 |

### Wheat / ZW=F (score 14.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -5.0% |
| ret_20d    | -8.1% |
| ret_60d    | -3.9% |
| ma20_dist  | -4.0% |
| ma50_dist  | -4.1% |
| vol_20d    | 20.4% |
| mdd_60d    | 12.7% |
| rsi_14     |  31.6 |
| zscore_20d |  -1.4 |

### Silver / SI=F (score 12.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.6% |
| ret_5d     | -3.3% |
| ret_20d    | -6.4% |
| ret_60d    | +0.9% |
| ma20_dist  | -4.9% |
| ma50_dist  | -8.4% |
| vol_20d    | 28.2% |
| mdd_60d    | 15.0% |
| rsi_14     |  30.9 |
| zscore_20d |  -1.2 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Microsoft Corporation / MSFT        |  11.9521 |           2.2% |                 0.49x |       23.9043 |            4.4% |
| Meta Platforms Inc. / META          |  23.1107 |           3.0% |                 0.19x |       46.2214 |            6.1% |
| S&P 500 / ^GSPC                     |  60.1500 |           0.8% |                 1.08x |      120.3000 |            1.5% |
| Apple Inc. / AAPL                   |   6.4950 |           1.9% |                 0.61x |       12.9900 |            3.8% |
| Alphabet Inc. Class A / GOOGL       |   7.6157 |           2.2% |                 0.50x |       15.2314 |            4.3% |
| NASDAQ 100 / ^NDX                   | 339.6154 |           1.1% |                 0.67x |      679.2307 |            2.2% |
| NVIDIA Corporation / NVDA           |   5.3100 |           2.3% |                 0.46x |       10.6200 |            4.6% |
| FTSE 100 / ^FTSE                    | 112.2356 |           1.1% |                 0.87x |      224.4711 |            2.1% |
| Brent Crude Oil / BZ=F              |   4.3179 |           4.1% |                 0.30x |        8.6357 |            8.2% |
| Amazon.com Inc. / AMZN              |   5.3729 |           2.1% |                 0.42x |       10.7457 |            4.2% |
| Dow Jones Industrial Average / ^DJI | 483.4621 |           0.9% |                 1.06x |      966.9241 |            1.9% |
| DAX / ^GDAXI                        | 296.9686 |           1.2% |                 0.74x |      593.9372 |            2.4% |
| UnitedHealth Group Inc. / UNH       |  10.3264 |           2.7% |                 0.60x |       20.6529 |            5.5% |
| Hang Seng / ^HSI                    | 332.6201 |           1.4% |                 0.64x |      665.2402 |            2.7% |
| Tesla Inc. / TSLA                   |  10.6850 |           2.8% |                 0.34x |       21.3700 |            5.7% |
| Soybeans / ZS=F                     |  21.9643 |           1.7% |                 0.70x |       43.9286 |            3.4% |
| Euro Stoxx 50 / ^STOXX50E           |  73.9979 |           1.2% |                 0.77x |      147.9957 |            2.4% |
| JPMorgan Chase & Co. / JPM          |   5.5350 |           1.7% |                 0.61x |       11.0700 |            3.3% |
| Gold / GC=F                         |  77.2071 |           1.8% |                 0.59x |      154.4142 |            3.7% |
| Russell 2000 / ^RUT                 |  31.5221 |           1.1% |                 0.96x |       63.0443 |            2.3% |
| CAC 40 / ^FCHI                      |  89.9699 |           1.1% |                 0.83x |      179.9399 |            2.3% |
| Corn / ZC=F                         |  12.3393 |           2.6% |                 0.40x |       24.6786 |            5.1% |
| Platinum / PL=F                     |  32.4286 |           2.0% |                 0.34x |       64.8572 |            3.9% |
| Wheat / ZW=F                        |  17.2500 |           2.6% |                 0.49x |       34.5000 |            5.2% |
| Silver / SI=F                       |   1.2311 |           2.1% |                 0.35x |        2.4623 |            4.2% |

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

Scoring engine version: **1.0.0** | Git commit: **714eb72**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
