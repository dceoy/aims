+++
title = "Market Analysis 2026-10-19"
date = "2026-10-19T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: BZ=F (score 74.8)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-10-19.json", "data/history/2026-10-19.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "95e2d80"
+++

## Market Regime

**Neutral** — 9 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Brent Crude Oil / BZ=F** — score 74.8, 20d return +5.8%, RSI14=62. 20d up +5.8%; above MA20 by 5.9%; RSI14=62
- **FTSE 100 / ^FTSE** — score 73.3, 20d return +2.1%, RSI14=61. 20d up +2.1%; above MA20 by 2.4%; RSI14=61
- **Microsoft Corporation / MSFT** — score 68.5, 20d return +7.1%, RSI14=63. 20d up +7.1%; above MA20 by 1.7%; RSI14=63
- **Apple Inc. / AAPL** — score 67.9, 20d return +2.2%, RSI14=56. 20d up +2.2%; above MA20 by 1.8%; RSI14=56
- **DAX / ^GDAXI** — score 67.3, 20d return +1.3%, RSI14=55. 20d up +1.3%; above MA20 by 1.3%; RSI14=55

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                 | Applies To |
| ---------- | --------------------- | ---------- |
| 2026-10-21 | TSLA earnings release | TSLA       |

## Signal History

Compared with the previous available report (**2026-10-16**).

- **New top-5:** AAPL, BZ=F, ^GDAXI
- **Persistent top signals:** MSFT (16 reports), ^FTSE (3 reports)
- **Dropped from top-5:** UNH, ^DJI, ^GSPC

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     -1 |    +4.8 |
| 7203.T    |     +0 |    +2.4 |
| 8306.T    |     +0 |   +18.5 |
| AAPL      |     +2 |    +6.1 |
| AMZN      |     -5 |   -14.2 |
| BZ=F      |     +6 |   +15.2 |
| CL=F      |     +1 |    +7.3 |
| GC=F      |     +1 |    +2.4 |
| GOOGL     |     -7 |   -16.7 |
| HG=F      |     +0 |   +10.6 |
| JPM       |     +7 |   +13.9 |
| META      |     -4 |   -12.7 |
| MSFT      |     -2 |   -12.4 |
| NG=F      |     -1 |   -18.2 |
| NVDA      |     -3 |    -9.1 |
| PL=F      |     +1 |    +4.2 |
| SI=F      |     +0 |    -1.8 |
| TSLA      |     +1 |    -2.4 |
| UNH       |     -4 |   -12.4 |
| XOM       |     +1 |   +10.6 |
| ZC=F      |     +3 |    +2.4 |
| ZS=F      |     +3 |    +6.4 |
| ZW=F      |     +0 |    -0.9 |
| ^DJI      |     -2 |    -5.8 |
| ^FCHI     |     +2 |    +0.0 |
| ^FTSE     |     +0 |    -0.9 |
| ^GDAXI    |     +3 |    +8.8 |
| ^GSPC     |     -5 |    -8.5 |
| ^HSI      |     +6 |    +8.5 |
| ^N225     |     +0 |   +13.6 |
| ^NDX      |     -7 |   -19.1 |
| ^RUT      |     -1 |   -11.2 |
| ^STOXX50E |     +5 |   +10.6 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Exxon Mobil Corporation / XOM** — malformed_input
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **WTI Crude Oil / CL=F** — malformed_input
- **Natural Gas / NG=F** — malformed_input
- **Copper / HG=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|    1 | Brent Crude Oil / BZ=F |  74.8 |   Yes    | —               | 20d up +5.8%; above MA20 by 5.9%; RSI14=62    |
|   14 | Soybeans / ZS=F        |  44.5 |   Yes    | —               | 20d down -3.2%; below MA20 by 2.5%; RSI14=37  |
|   15 | Gold / GC=F            |  42.4 |   Yes    | —               | 20d down -5.5%; below MA20 by 0.8%; RSI14=52  |
|   20 | Corn / ZC=F            |  23.6 |   Yes    | —               | 20d down -10.1%; below MA20 by 6.1%; RSI14=19 |
|   22 | Wheat / ZW=F           |  23.0 |   Yes    | —               | 20d down -7.5%; below MA20 by 4.1%; RSI14=36  |
|   23 | Platinum / PL=F        |  22.7 |   Yes    | —               | 20d down -10.0%; below MA20 by 4.2%; RSI14=36 |
|   25 | Silver / SI=F          |  13.6 |   Yes    | —               | 20d down -14.4%; below MA20 by 6.3%; RSI14=35 |
|   29 | WTI Crude Oil / CL=F   |  73.6 |    No    | malformed_input | Suppressed: malformed_input                   |
|   30 | Natural Gas / NG=F     |  52.4 |    No    | malformed_input | Suppressed: malformed_input                   |
|   31 | Copper / HG=F          |  51.8 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    3 | Microsoft Corporation / MSFT                                                   |  68.5 |   Yes    | —                             | 20d up +7.1%; above MA20 by 1.7%; RSI14=63   |
|    4 | Apple Inc. / AAPL                                                              |  67.9 |   Yes    | —                             | 20d up +2.2%; above MA20 by 1.8%; RSI14=56   |
|    7 | UnitedHealth Group Inc. / UNH                                                  |  57.9 |   Yes    | —                             | 20d up +6.5%; above MA20 by 6.0%; RSI14=65   |
|    8 | JPMorgan Chase & Co. / JPM                                                     |  56.4 |   Yes    | —                             | 20d down -2.4%; above MA20 by 1.5%; RSI14=59 |
|   13 | Meta Platforms Inc. / META                                                     |  45.5 |   Yes    | —                             | 20d up +6.6%; below MA20 by 3.6%; RSI14=48   |
|   16 | Amazon.com Inc. / AMZN                                                         |  37.6 |   Yes    | —                             | 20d down -1.5%; below MA20 by 1.3%; RSI14=54 |
|   17 | Alphabet Inc. Class A / GOOGL                                                  |  37.3 |   Yes    | —                             | 20d down -2.6%; below MA20 by 1.7%; RSI14=48 |
|   18 | Tesla Inc. / TSLA                                                              |  33.3 |   Yes    | —                             | 20d down -2.6%; below MA20 by 4.2%; RSI14=48 |
|   24 | NVIDIA Corporation / NVDA                                                      |  20.0 |   Yes    | —                             | 20d down -3.7%; below MA20 by 6.2%; RSI14=33 |
|   26 | Exxon Mobil Corporation / XOM                                                  |  85.2 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   27 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  79.7 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   28 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  74.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   33 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  33.6 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    2 | FTSE 100 / ^FTSE                    |  73.3 |   Yes    | —            | 20d up +2.1%; above MA20 by 2.4%; RSI14=61   |
|    5 | DAX / ^GDAXI                        |  67.3 |   Yes    | —            | 20d up +1.3%; above MA20 by 1.3%; RSI14=55   |
|    6 | Dow Jones Industrial Average / ^DJI |  63.3 |   Yes    | —            | 20d up +0.6%; above MA20 by 0.9%; RSI14=58   |
|    9 | Euro Stoxx 50 / ^STOXX50E           |  54.9 |   Yes    | —            | 20d down -0.5%; below MA20 by 0.5%; RSI14=42 |
|   10 | S&P 500 / ^GSPC                     |  53.6 |   Yes    | —            | 20d up +0.1%; below MA20 by 1.0%; RSI14=48   |
|   11 | CAC 40 / ^FCHI                      |  46.7 |   Yes    | —            | 20d down -1.3%; above MA20 by 0.2%; RSI14=42 |
|   12 | Hang Seng / ^HSI                    |  46.4 |   Yes    | —            | 20d down -1.7%; below MA20 by 0.9%; RSI14=44 |
|   19 | NASDAQ 100 / ^NDX                   |  28.8 |   Yes    | —            | 20d down -1.5%; below MA20 by 4.4%; RSI14=33 |
|   21 | Russell 2000 / ^RUT                 |  23.3 |   Yes    | —            | 20d down -4.9%; below MA20 by 3.2%; RSI14=34 |
|   32 | Nikkei 225 / ^N225                  |  42.7 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-10-16 |
| 7203.T    | 2026-10-16 |
| 8306.T    | 2026-10-16 |
| AAPL      | 2026-10-16 |
| AMZN      | 2026-10-16 |
| BZ=F      | 2026-10-16 |
| CL=F      | 2026-10-16 |
| GC=F      | 2026-10-16 |
| GOOGL     | 2026-10-16 |
| HG=F      | 2026-10-16 |
| JPM       | 2026-10-16 |
| META      | 2026-10-16 |
| MSFT      | 2026-10-16 |
| NG=F      | 2026-10-16 |
| NVDA      | 2026-10-16 |
| PL=F      | 2026-10-16 |
| SI=F      | 2026-10-16 |
| TSLA      | 2026-10-16 |
| UNH       | 2026-10-16 |
| XOM       | 2026-10-16 |
| ZC=F      | 2026-10-16 |
| ZS=F      | 2026-10-16 |
| ZW=F      | 2026-10-16 |
| ^DJI      | 2026-10-16 |
| ^FCHI     | 2026-10-16 |
| ^FTSE     | 2026-10-16 |
| ^GDAXI    | 2026-10-16 |
| ^GSPC     | 2026-10-16 |
| ^HSI      | 2026-10-16 |
| ^N225     | 2026-10-16 |
| ^NDX      | 2026-10-16 |
| ^RUT      | 2026-10-16 |
| ^STOXX50E | 2026-10-16 |

## Symbol Details

### Brent Crude Oil / BZ=F (score 74.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +3.7% |
| ret_5d     |  +4.9% |
| ret_20d    |  +5.8% |
| ret_60d    | +21.1% |
| ma20_dist  |  +5.9% |
| ma50_dist  | +11.2% |
| vol_20d    |  33.7% |
| mdd_60d    |  11.9% |
| rsi_14     |   61.8 |
| zscore_20d |    2.3 |

### FTSE 100 / ^FTSE (score 73.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | +3.1% |
| ret_20d    | +2.1% |
| ret_60d    | +2.3% |
| ma20_dist  | +2.4% |
| ma50_dist  | +1.5% |
| vol_20d    | 10.4% |
| mdd_60d    |  4.4% |
| rsi_14     |  60.7 |
| zscore_20d |   2.0 |

### Microsoft Corporation / MSFT (score 68.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.9% |
| ret_5d     |  -1.1% |
| ret_20d    |  +7.1% |
| ret_60d    | +38.9% |
| ma20_dist  |  +1.7% |
| ma50_dist  |  +4.7% |
| vol_20d    |  21.8% |
| mdd_60d    |   5.1% |
| rsi_14     |   63.2 |
| zscore_20d |    0.6 |

### Apple Inc. / AAPL (score 67.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | +2.0% |
| ret_20d    | +2.2% |
| ret_60d    | +6.9% |
| ma20_dist  | +1.8% |
| ma50_dist  | +5.5% |
| vol_20d    | 15.8% |
| mdd_60d    | 11.0% |
| rsi_14     |  56.4 |
| zscore_20d |   1.5 |

### DAX / ^GDAXI (score 67.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | +2.1% |
| ret_20d    | +1.3% |
| ret_60d    | +2.1% |
| ma20_dist  | +1.3% |
| ma50_dist  | -0.4% |
| vol_20d    | 12.3% |
| mdd_60d    |  6.6% |
| rsi_14     |  55.0 |
| zscore_20d |   1.6 |

### Dow Jones Industrial Average / ^DJI (score 63.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | +0.7% |
| ret_20d    | +0.6% |
| ret_60d    | +0.6% |
| ma20_dist  | +0.9% |
| ma50_dist  | -0.9% |
| vol_20d    |  9.0% |
| mdd_60d    |  6.3% |
| rsi_14     |  58.2 |
| zscore_20d |   1.3 |

### UnitedHealth Group Inc. / UNH (score 57.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.3% |
| ret_5d     | +5.8% |
| ret_20d    | +6.5% |
| ret_60d    | -5.2% |
| ma20_dist  | +6.0% |
| ma50_dist  | +3.9% |
| vol_20d    | 25.5% |
| mdd_60d    | 14.8% |
| rsi_14     |  65.2 |
| zscore_20d |   2.2 |

### JPMorgan Chase & Co. / JPM (score 56.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.2% |
| ret_5d     | +2.0% |
| ret_20d    | -2.4% |
| ret_60d    | -2.9% |
| ma20_dist  | +1.5% |
| ma50_dist  | -2.2% |
| vol_20d    | 17.7% |
| mdd_60d    |  9.9% |
| rsi_14     |  58.9 |
| zscore_20d |   1.0 |

### Euro Stoxx 50 / ^STOXX50E (score 54.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | +0.5% |
| ret_20d    | -0.5% |
| ret_60d    | -1.2% |
| ma20_dist  | -0.5% |
| ma50_dist  | -2.2% |
| vol_20d    | 11.9% |
| mdd_60d    |  6.5% |
| rsi_14     |  41.9 |
| zscore_20d |  -0.5 |

### S&P 500 / ^GSPC (score 53.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.1% |
| ret_5d     | -1.9% |
| ret_20d    | +0.1% |
| ret_60d    | +3.4% |
| ma20_dist  | -1.0% |
| ma50_dist  | -0.6% |
| vol_20d    | 10.2% |
| mdd_60d    |  3.2% |
| rsi_14     |  47.6 |
| zscore_20d |  -1.5 |

### CAC 40 / ^FCHI (score 46.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +2.0% |
| ret_20d    | -1.3% |
| ret_60d    | -5.0% |
| ma20_dist  | +0.2% |
| ma50_dist  | -3.0% |
| vol_20d    | 11.3% |
| mdd_60d    | 11.4% |
| rsi_14     |  42.1 |
| zscore_20d |   0.1 |

### Hang Seng / ^HSI (score 46.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | -0.1% |
| ret_20d    | -1.7% |
| ret_60d    | -4.1% |
| ma20_dist  | -0.9% |
| ma50_dist  | -3.2% |
| vol_20d    | 15.6% |
| mdd_60d    |  8.5% |
| rsi_14     |  44.1 |
| zscore_20d |  -0.7 |

### Meta Platforms Inc. / META (score 45.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -3.7% |
| ret_5d     |  -1.3% |
| ret_20d    |  +6.6% |
| ret_60d    | +17.0% |
| ma20_dist  |  -3.6% |
| ma50_dist  |  +8.3% |
| vol_20d    |  56.1% |
| mdd_60d    |   9.4% |
| rsi_14     |   48.2 |
| zscore_20d |   -1.7 |

### Soybeans / ZS=F (score 44.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | -2.4% |
| ret_20d    | -3.2% |
| ret_60d    | +4.1% |
| ma20_dist  | -2.5% |
| ma50_dist  | -0.7% |
| vol_20d    | 14.1% |
| mdd_60d    |  5.0% |
| rsi_14     |  37.1 |
| zscore_20d |  -1.7 |

### Gold / GC=F (score 42.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | -0.8% |
| ret_20d    | -5.5% |
| ret_60d    | +3.6% |
| ma20_dist  | -0.8% |
| ma50_dist  | -4.5% |
| vol_20d    | 17.7% |
| mdd_60d    | 12.7% |
| rsi_14     |  51.5 |
| zscore_20d |  -0.4 |

### Amazon.com Inc. / AMZN (score 37.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.9% |
| ret_5d     | -4.7% |
| ret_20d    | -1.5% |
| ret_60d    | +7.0% |
| ma20_dist  | -1.3% |
| ma50_dist  | -2.8% |
| vol_20d    | 23.8% |
| mdd_60d    | 13.4% |
| rsi_14     |  54.4 |
| zscore_20d |  -0.7 |

### Alphabet Inc. Class A / GOOGL (score 37.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.5% |
| ret_5d     | -3.1% |
| ret_20d    | -2.6% |
| ret_60d    | +7.2% |
| ma20_dist  | -1.7% |
| ma50_dist  | -1.1% |
| vol_20d    | 22.1% |
| mdd_60d    | 12.4% |
| rsi_14     |  47.7 |
| zscore_20d |  -1.2 |

### Tesla Inc. / TSLA (score 33.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.1% |
| ret_5d     |  -7.3% |
| ret_20d    |  -2.6% |
| ret_60d    | +11.0% |
| ma20_dist  |  -4.2% |
| ma50_dist  |  -1.3% |
| vol_20d    |  30.8% |
| mdd_60d    |   7.3% |
| rsi_14     |   48.2 |
| zscore_20d |   -1.5 |

### NASDAQ 100 / ^NDX (score 28.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.5% |
| ret_5d     | -5.5% |
| ret_20d    | -1.5% |
| ret_60d    | +2.6% |
| ma20_dist  | -4.4% |
| ma50_dist  | -2.3% |
| vol_20d    | 18.1% |
| mdd_60d    |  6.5% |
| rsi_14     |  33.5 |
| zscore_20d |  -3.0 |

### Corn / ZC=F (score 23.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.8% |
| ret_5d     |  -1.1% |
| ret_20d    | -10.1% |
| ret_60d    |  +3.4% |
| ma20_dist  |  -6.1% |
| ma50_dist  |  -5.4% |
| vol_20d    |  25.1% |
| mdd_60d    |  12.7% |
| rsi_14     |   19.4 |
| zscore_20d |   -1.5 |

### Russell 2000 / ^RUT (score 23.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.7% |
| ret_5d     | -3.0% |
| ret_20d    | -4.9% |
| ret_60d    | -7.4% |
| ma20_dist  | -3.2% |
| ma50_dist  | -6.4% |
| vol_20d    | 14.0% |
| mdd_60d    | 11.3% |
| rsi_14     |  33.9 |
| zscore_20d |  -2.2 |

### Wheat / ZW=F (score 23.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.4% |
| ret_5d     | -1.6% |
| ret_20d    | -7.5% |
| ret_60d    | -0.3% |
| ma20_dist  | -4.1% |
| ma50_dist  | -5.6% |
| vol_20d    | 20.3% |
| mdd_60d    | 13.9% |
| rsi_14     |  36.4 |
| zscore_20d |  -1.6 |

### Platinum / PL=F (score 22.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.8% |
| ret_5d     |  -3.3% |
| ret_20d    | -10.0% |
| ret_60d    |  +2.1% |
| ma20_dist  |  -4.2% |
| ma50_dist  |  -7.9% |
| vol_20d    |  30.8% |
| mdd_60d    |  16.4% |
| rsi_14     |   35.9 |
| zscore_20d |   -1.2 |

### NVIDIA Corporation / NVDA (score 20.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.4% |
| ret_5d     | -6.6% |
| ret_20d    | -3.7% |
| ret_60d    | +2.6% |
| ma20_dist  | -6.2% |
| ma50_dist  | -4.0% |
| vol_20d    | 24.1% |
| mdd_60d    | 10.5% |
| rsi_14     |  32.9 |
| zscore_20d |  -2.3 |

### Silver / SI=F (score 13.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.3% |
| ret_5d     |  -6.1% |
| ret_20d    | -14.4% |
| ret_60d    |  -1.5% |
| ma20_dist  |  -6.3% |
| ma50_dist  | -11.1% |
| vol_20d    |  33.3% |
| mdd_60d    |  20.0% |
| rsi_14     |   34.9 |
| zscore_20d |   -1.4 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Brent Crude Oil / BZ=F              |   3.9571 |           3.6% |                 0.30x |        7.9143 |            7.2% |
| FTSE 100 / ^FTSE                    | 121.0999 |           1.1% |                 0.96x |      242.1998 |            2.2% |
| Microsoft Corporation / MSFT        |  11.7407 |           2.2% |                 0.46x |       23.4814 |            4.4% |
| Apple Inc. / AAPL                   |   6.6900 |           1.9% |                 0.63x |       13.3800 |            3.9% |
| DAX / ^GDAXI                        | 300.4584 |           1.2% |                 0.82x |      600.9169 |            2.3% |
| Dow Jones Industrial Average / ^DJI | 520.9735 |           1.0% |                 1.11x |     1041.9470 |            2.0% |
| UnitedHealth Group Inc. / UNH       |  12.6714 |           3.2% |                 0.39x |       25.3429 |            6.3% |
| JPMorgan Chase & Co. / JPM          |   6.1177 |           1.8% |                 0.57x |       12.2354 |            3.6% |
| Euro Stoxx 50 / ^STOXX50E           |  73.6679 |           1.2% |                 0.84x |      147.3358 |            2.4% |
| S&P 500 / ^GSPC                     |  69.3971 |           0.9% |                 0.98x |      138.7943 |            1.8% |
| CAC 40 / ^FCHI                      |  89.6078 |           1.1% |                 0.88x |      179.2156 |            2.3% |
| Hang Seng / ^HSI                    | 344.0658 |           1.4% |                 0.64x |      688.1317 |            2.8% |
| Meta Platforms Inc. / META          |  22.1143 |           3.1% |                 0.18x |       44.2286 |            6.2% |
| Soybeans / ZS=F                     |  19.3036 |           1.5% |                 0.71x |       38.6071 |            3.1% |
| Gold / GC=F                         |  72.9928 |           1.7% |                 0.57x |      145.9856 |            3.5% |
| Amazon.com Inc. / AMZN              |   5.9021 |           2.4% |                 0.42x |       11.8043 |            4.7% |
| Alphabet Inc. Class A / GOOGL       |   8.9607 |           2.6% |                 0.45x |       17.9214 |            5.3% |
| Tesla Inc. / TSLA                   |  10.8571 |           3.1% |                 0.33x |       21.7143 |            6.1% |
| NASDAQ 100 / ^NDX                   | 414.0232 |           1.4% |                 0.55x |      828.0463 |            2.8% |
| Corn / ZC=F                         |  11.4821 |           2.4% |                 0.40x |       22.9643 |            4.8% |
| Russell 2000 / ^RUT                 |  37.1665 |           1.4% |                 0.71x |       74.3329 |            2.7% |
| Wheat / ZW=F                        |  16.0357 |           2.4% |                 0.49x |       32.0714 |            4.9% |
| Platinum / PL=F                     |  33.5357 |           2.1% |                 0.32x |       67.0715 |            4.1% |
| NVIDIA Corporation / NVDA           |   5.7614 |           2.7% |                 0.42x |       11.5229 |            5.4% |
| Silver / SI=F                       |   1.2262 |           2.2% |                 0.30x |        2.4524 |            4.3% |

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

Scoring engine version: **1.0.0** | Git commit: **95e2d80**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
