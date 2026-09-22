+++
title = "Market Analysis 2026-09-22"
date = "2026-09-22T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: ZC=F (score 81.8)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-09-22.json", "data/history/2026-09-22.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "8cfac97"
+++

## Market Regime

**Neutral** — 12 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Corn / ZC=F** — score 81.8, 20d return +4.3%, RSI14=68. 20d up +4.3%; above MA20 by 5.1%; RSI14=68
- **Meta Platforms Inc. / META** — score 77.6, 20d return +34.9%, RSI14=87. 20d up +34.9%; above MA20 by 18.8%; RSI14=87
- **Soybeans / ZS=F** — score 74.5, 20d return +7.6%, RSI14=63. 20d up +7.6%; above MA20 by 3.0%; RSI14=63
- **NASDAQ 100 / ^NDX** — score 73.0, 20d return +4.0%, RSI14=65. 20d up +4.0%; above MA20 by 3.8%; RSI14=65
- **Apple Inc. / AAPL** — score 70.0, 20d return +9.6%, RSI14=71. 20d up +9.6%; above MA20 by 4.6%; RSI14=71

## Upcoming Events

_No scheduled events for covered instruments in the next 7 days._

## Signal History

Compared with the previous available report (**2026-09-21**).

- **New top-5:** None
- **Persistent top signals:** AAPL (8 reports), META (7 reports), ZC=F (5 reports), ZS=F (2 reports), ^NDX (2 reports)
- **Dropped from top-5:** None

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +2 |    -3.3 |
| 7203.T    |     +2 |    -7.6 |
| 8306.T    |     +2 |    -6.1 |
| AAPL      |     -3 |    -0.3 |
| AMZN      |     +8 |   +17.6 |
| BZ=F      |     -7 |   -11.2 |
| CL=F      |     -1 |   -13.6 |
| GC=F      |     -8 |   -11.5 |
| GOOGL     |     -3 |    -2.1 |
| HG=F      |     +1 |    +2.7 |
| JPM       |     -1 |    +4.5 |
| META      |     +2 |   +10.9 |
| MSFT      |     +3 |    +8.5 |
| NG=F      |     -4 |   -30.6 |
| NVDA      |     +1 |    +6.1 |
| PL=F      |     -7 |   -10.0 |
| SI=F      |     -9 |   -14.2 |
| TSLA      |     +4 |   +10.9 |
| UNH       |     -2 |   -11.2 |
| XOM       |     -4 |   -28.5 |
| ZC=F      |     +0 |    +7.9 |
| ZS=F      |     +0 |    +6.1 |
| ZW=F      |     +5 |   +12.7 |
| ^DJI      |     -2 |    +0.9 |
| ^FCHI     |     +2 |    +9.4 |
| ^FTSE     |     +2 |    +5.2 |
| ^GDAXI    |     +1 |   +10.6 |
| ^GSPC     |     +4 |   +10.3 |
| ^HSI      |     +3 |    +7.9 |
| ^N225     |     +2 |    -7.6 |
| ^NDX      |     +1 |    +9.4 |
| ^RUT      |     +0 |    +0.0 |
| ^STOXX50E |     +6 |   +16.4 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Copper / HG=F** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Nikkei 225 / ^N225** — missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Natural Gas / NG=F** — malformed_input

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|    1 | Corn / ZC=F            |  81.8 |   Yes    | —               | 20d up +4.3%; above MA20 by 5.1%; RSI14=68   |
|    3 | Soybeans / ZS=F        |  74.5 |   Yes    | —               | 20d up +7.6%; above MA20 by 3.0%; RSI14=63   |
|   12 | Wheat / ZW=F           |  53.6 |   Yes    | —               | 20d up +2.0%; below MA20 by 0.0%; RSI14=41   |
|   14 | Brent Crude Oil / BZ=F |  50.6 |   Yes    | —               | 20d up +8.9%; above MA20 by 2.1%; RSI14=60   |
|   18 | Silver / SI=F          |  43.9 |   Yes    | —               | 20d down -4.0%; below MA20 by 0.3%; RSI14=54 |
|   19 | Platinum / PL=F        |  43.0 |   Yes    | —               | 20d down -4.3%; below MA20 by 0.8%; RSI14=55 |
|   21 | Gold / GC=F            |  36.1 |   Yes    | —               | 20d down -6.7%; below MA20 by 1.8%; RSI14=49 |
|   26 | Copper / HG=F          |  61.5 |    No    | malformed_input | Suppressed: malformed_input                  |
|   27 | WTI Crude Oil / CL=F   |  50.9 |    No    | malformed_input | Suppressed: malformed_input                  |
|   33 | Natural Gas / NG=F     |  22.1 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    2 | Meta Platforms Inc. / META                                                     |  77.6 |   Yes    | —                             | 20d up +34.9%; above MA20 by 18.8%; RSI14=87 |
|    5 | Apple Inc. / AAPL                                                              |  70.0 |   Yes    | —                             | 20d up +9.6%; above MA20 by 4.6%; RSI14=71   |
|    7 | NVIDIA Corporation / NVDA                                                      |  67.6 |   Yes    | —                             | 20d up +6.0%; above MA20 by 3.7%; RSI14=57   |
|    8 | Microsoft Corporation / MSFT                                                   |  64.5 |   Yes    | —                             | 20d up +3.8%; above MA20 by 0.6%; RSI14=47   |
|    9 | Alphabet Inc. Class A / GOOGL                                                  |  60.3 |   Yes    | —                             | 20d up +3.0%; above MA20 by 3.7%; RSI14=63   |
|   10 | Tesla Inc. / TSLA                                                              |  57.6 |   Yes    | —                             | 20d up +3.4%; above MA20 by 4.2%; RSI14=53   |
|   11 | Amazon.com Inc. / AMZN                                                         |  55.1 |   Yes    | —                             | 20d down -0.1%; above MA20 by 0.9%; RSI14=49 |
|   17 | JPMorgan Chase & Co. / JPM                                                     |  45.8 |   Yes    | —                             | 20d up +0.1%; below MA20 by 0.7%; RSI14=45   |
|   25 | UnitedHealth Group Inc. / UNH                                                  |  17.9 |   Yes    | —                             | 20d down -2.6%; below MA20 by 2.7%; RSI14=42 |
|   28 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  40.9 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   30 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  31.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   31 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  28.5 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   32 | Exxon Mobil Corporation / XOM                                                  |  28.2 |    No    | malformed_input               | Suppressed: malformed_input                  |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    4 | NASDAQ 100 / ^NDX                   |  73.0 |   Yes    | —            | 20d up +4.0%; above MA20 by 3.8%; RSI14=65   |
|    6 | S&P 500 / ^GSPC                     |  68.5 |   Yes    | —            | 20d up +1.2%; above MA20 by 1.3%; RSI14=56   |
|   13 | FTSE 100 / ^FTSE                    |  51.2 |   Yes    | —            | 20d down -0.7%; below MA20 by 0.2%; RSI14=47 |
|   15 | Hang Seng / ^HSI                    |  47.3 |   Yes    | —            | 20d down -1.9%; below MA20 by 0.6%; RSI14=44 |
|   16 | Euro Stoxx 50 / ^STOXX50E           |  46.7 |   Yes    | —            | 20d down -2.0%; below MA20 by 0.6%; RSI14=46 |
|   20 | DAX / ^GDAXI                        |  41.8 |   Yes    | —            | 20d down -2.0%; below MA20 by 1.1%; RSI14=42 |
|   22 | Dow Jones Industrial Average / ^DJI |  33.6 |   Yes    | —            | 20d down -2.3%; below MA20 by 1.3%; RSI14=39 |
|   23 | CAC 40 / ^FCHI                      |  29.7 |   Yes    | —            | 20d down -3.7%; below MA20 by 1.3%; RSI14=39 |
|   24 | Russell 2000 / ^RUT                 |  25.4 |   Yes    | —            | 20d down -4.7%; below MA20 by 2.0%; RSI14=36 |
|   29 | Nikkei 225 / ^N225                  |  39.4 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-09-18 |
| 7203.T    | 2026-09-18 |
| 8306.T    | 2026-09-18 |
| AAPL      | 2026-09-21 |
| AMZN      | 2026-09-21 |
| BZ=F      | 2026-09-21 |
| CL=F      | 2026-09-21 |
| GC=F      | 2026-09-21 |
| GOOGL     | 2026-09-21 |
| HG=F      | 2026-09-21 |
| JPM       | 2026-09-21 |
| META      | 2026-09-21 |
| MSFT      | 2026-09-21 |
| NG=F      | 2026-09-21 |
| NVDA      | 2026-09-21 |
| PL=F      | 2026-09-21 |
| SI=F      | 2026-09-21 |
| TSLA      | 2026-09-21 |
| UNH       | 2026-09-21 |
| XOM       | 2026-09-21 |
| ZC=F      | 2026-09-21 |
| ZS=F      | 2026-09-21 |
| ZW=F      | 2026-09-21 |
| ^DJI      | 2026-09-21 |
| ^FCHI     | 2026-09-21 |
| ^FTSE     | 2026-09-21 |
| ^GDAXI    | 2026-09-21 |
| ^GSPC     | 2026-09-21 |
| ^HSI      | 2026-09-21 |
| ^N225     | 2026-09-18 |
| ^NDX      | 2026-09-21 |
| ^RUT      | 2026-09-21 |
| ^STOXX50E | 2026-09-21 |

## Symbol Details

### Corn / ZC=F (score 81.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.9% |
| ret_5d     |  +6.1% |
| ret_20d    |  +4.3% |
| ret_60d    | +31.6% |
| ma20_dist  |  +5.1% |
| ma50_dist  | +12.9% |
| vol_20d    |  31.4% |
| mdd_60d    |   6.0% |
| rsi_14     |   67.6 |
| zscore_20d |    2.2 |

### Meta Platforms Inc. / META (score 77.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     | +11.4% |
| ret_5d     | +11.5% |
| ret_20d    | +34.9% |
| ret_60d    | +36.5% |
| ma20_dist  | +18.8% |
| ma50_dist  | +21.8% |
| vol_20d    |  46.6% |
| mdd_60d    |  20.9% |
| rsi_14     |   87.2 |
| zscore_20d |    2.4 |

### Soybeans / ZS=F (score 74.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.9% |
| ret_5d     |  +3.3% |
| ret_20d    |  +7.6% |
| ret_60d    | +18.9% |
| ma20_dist  |  +3.0% |
| ma50_dist  |  +7.8% |
| vol_20d    |  21.7% |
| mdd_60d    |   8.1% |
| rsi_14     |   62.7 |
| zscore_20d |    1.3 |

### NASDAQ 100 / ^NDX (score 73.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.8% |
| ret_5d     | +4.7% |
| ret_20d    | +4.0% |
| ret_60d    | +3.5% |
| ma20_dist  | +3.8% |
| ma50_dist  | +4.4% |
| vol_20d    | 16.2% |
| mdd_60d    | 10.2% |
| rsi_14     |  64.5 |
| zscore_20d |   3.3 |

### Apple Inc. / AAPL (score 70.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.8% |
| ret_5d     |  +1.8% |
| ret_20d    |  +9.6% |
| ret_60d    | +23.2% |
| ma20_dist  |  +4.6% |
| ma50_dist  |  +5.8% |
| vol_20d    |  21.0% |
| mdd_60d    |  11.0% |
| rsi_14     |   70.7 |
| zscore_20d |    1.6 |

### S&P 500 / ^GSPC (score 68.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.5% |
| ret_5d     | +1.9% |
| ret_20d    | +1.2% |
| ret_60d    | +5.5% |
| ma20_dist  | +1.3% |
| ma50_dist  | +1.9% |
| vol_20d    | 10.4% |
| mdd_60d    |  3.4% |
| rsi_14     |  55.5 |
| zscore_20d |   1.9 |

### NVIDIA Corporation / NVDA (score 67.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.3% |
| ret_5d     |  +7.8% |
| ret_20d    |  +6.0% |
| ret_60d    | +16.2% |
| ma20_dist  |  +3.7% |
| ma50_dist  |  +6.0% |
| vol_20d    |  45.6% |
| mdd_60d    |  10.6% |
| rsi_14     |   56.6 |
| zscore_20d |    1.2 |

### Microsoft Corporation / MSFT (score 64.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.6% |
| ret_5d     |  -0.8% |
| ret_20d    |  +3.8% |
| ret_60d    | +42.2% |
| ma20_dist  |  +0.6% |
| ma50_dist  |  +7.5% |
| vol_20d    |  22.0% |
| mdd_60d    |   5.1% |
| rsi_14     |   46.9 |
| zscore_20d |    0.5 |

### Alphabet Inc. Class A / GOOGL (score 60.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.6% |
| ret_5d     | +1.6% |
| ret_20d    | +3.0% |
| ret_60d    | +3.3% |
| ma20_dist  | +3.7% |
| ma50_dist  | +2.8% |
| vol_20d    | 22.8% |
| mdd_60d    | 14.4% |
| rsi_14     |  63.0 |
| zscore_20d |   2.1 |

### Tesla Inc. / TSLA (score 57.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +3.0% |
| ret_5d     | +4.5% |
| ret_20d    | +3.4% |
| ret_60d    | +0.0% |
| ma20_dist  | +4.2% |
| ma50_dist  | +7.4% |
| vol_20d    | 45.8% |
| mdd_60d    | 29.9% |
| rsi_14     |  53.5 |
| zscore_20d |   1.8 |

### Amazon.com Inc. / AMZN (score 55.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.9% |
| ret_5d     |  +1.9% |
| ret_20d    |  -0.1% |
| ret_60d    | +13.8% |
| ma20_dist  |  +0.9% |
| ma50_dist  |  +0.9% |
| vol_20d    |  26.4% |
| mdd_60d    |  13.4% |
| rsi_14     |   48.5 |
| zscore_20d |    0.5 |

### Wheat / ZW=F (score 53.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.8% |
| ret_5d     |  +2.8% |
| ret_20d    |  +2.0% |
| ret_60d    | +25.1% |
| ma20_dist  |  -0.0% |
| ma50_dist  |  +5.3% |
| vol_20d    |  40.1% |
| mdd_60d    |  10.7% |
| rsi_14     |   41.2 |
| zscore_20d |   -0.0 |

### FTSE 100 / ^FTSE (score 51.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | +0.4% |
| ret_20d    | -0.7% |
| ret_60d    | +2.2% |
| ma20_dist  | -0.2% |
| ma50_dist  | -0.1% |
| vol_20d    | 10.2% |
| mdd_60d    |  2.7% |
| rsi_14     |  47.1 |
| zscore_20d |  -0.3 |

### Brent Crude Oil / BZ=F (score 50.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -3.4% |
| ret_5d     |  -5.1% |
| ret_20d    |  +8.9% |
| ret_60d    | +40.2% |
| ma20_dist  |  +2.1% |
| ma50_dist  |  +8.2% |
| vol_20d    |  41.0% |
| mdd_60d    |  21.2% |
| rsi_14     |   59.9 |
| zscore_20d |    0.3 |

### Hang Seng / ^HSI (score 47.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.2% |
| ret_5d     |  +0.5% |
| ret_20d    |  -1.9% |
| ret_60d    | +10.5% |
| ma20_dist  |  -0.6% |
| ma50_dist  |  -1.1% |
| vol_20d    |  11.5% |
| mdd_60d    |   5.4% |
| rsi_14     |   43.9 |
| zscore_20d |   -0.4 |

### Euro Stoxx 50 / ^STOXX50E (score 46.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.3% |
| ret_5d     | +0.9% |
| ret_20d    | -2.0% |
| ret_60d    | +1.4% |
| ma20_dist  | -0.6% |
| ma50_dist  | -0.9% |
| vol_20d    | 12.7% |
| mdd_60d    |  4.8% |
| rsi_14     |  45.8 |
| zscore_20d |  -0.5 |

### JPMorgan Chase & Co. / JPM (score 45.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | +0.5% |
| ret_20d    | +0.1% |
| ret_60d    | +5.5% |
| ma20_dist  | -0.7% |
| ma50_dist  | -0.4% |
| vol_20d    | 13.7% |
| mdd_60d    |  4.5% |
| rsi_14     |  44.6 |
| zscore_20d |  -0.7 |

### Silver / SI=F (score 43.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.1% |
| ret_5d     | +3.6% |
| ret_20d    | -4.0% |
| ret_60d    | +9.6% |
| ma20_dist  | -0.3% |
| ma50_dist  | +3.2% |
| vol_20d    | 33.3% |
| mdd_60d    |  9.7% |
| rsi_14     |  53.9 |
| zscore_20d |  -0.1 |

### Platinum / PL=F (score 43.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.3% |
| ret_5d     |  +1.3% |
| ret_20d    |  -4.3% |
| ret_60d    | +13.2% |
| ma20_dist  |  -0.8% |
| ma50_dist  |  +2.6% |
| vol_20d    |  32.6% |
| mdd_60d    |   7.4% |
| rsi_14     |   55.3 |
| zscore_20d |   -0.4 |

### DAX / ^GDAXI (score 41.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | +0.5% |
| ret_20d    | -2.0% |
| ret_60d    | +3.8% |
| ma20_dist  | -1.1% |
| ma50_dist  | -0.8% |
| vol_20d    | 12.8% |
| mdd_60d    |  4.8% |
| rsi_14     |  41.8 |
| zscore_20d |  -0.8 |

### Gold / GC=F (score 36.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.9% |
| ret_5d     | +0.7% |
| ret_20d    | -6.7% |
| ret_60d    | +7.8% |
| ma20_dist  | -1.8% |
| ma50_dist  | +0.7% |
| vol_20d    | 19.1% |
| mdd_60d    |  7.9% |
| rsi_14     |  48.8 |
| zscore_20d |  -0.8 |

### Dow Jones Industrial Average / ^DJI (score 33.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | -0.7% |
| ret_20d    | -2.3% |
| ret_60d    | +0.2% |
| ma20_dist  | -1.3% |
| ma50_dist  | -1.6% |
| vol_20d    | 10.8% |
| mdd_60d    |  5.3% |
| rsi_14     |  39.4 |
| zscore_20d |  -1.0 |

### CAC 40 / ^FCHI (score 29.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | +0.3% |
| ret_20d    | -3.7% |
| ret_60d    | -2.7% |
| ma20_dist  | -1.3% |
| ma50_dist  | -3.2% |
| vol_20d    | 12.9% |
| mdd_60d    |  7.6% |
| rsi_14     |  38.7 |
| zscore_20d |  -0.9 |

### Russell 2000 / ^RUT (score 25.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | -0.6% |
| ret_20d    | -4.7% |
| ret_60d    | -4.4% |
| ma20_dist  | -2.0% |
| ma50_dist  | -3.1% |
| vol_20d    | 11.3% |
| mdd_60d    |  6.8% |
| rsi_14     |  35.5 |
| zscore_20d |  -1.1 |

### UnitedHealth Group Inc. / UNH (score 17.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | -1.6% |
| ret_20d    | -2.6% |
| ret_60d    | -9.1% |
| ma20_dist  | -2.7% |
| ma50_dist  | -6.2% |
| vol_20d    | 20.5% |
| mdd_60d    | 14.0% |
| rsi_14     |  41.8 |
| zscore_20d |  -1.2 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Corn / ZC=F                         |  11.0179 |           2.0% |                 0.32x |       22.0357 |            4.1% |
| Meta Platforms Inc. / META          |  27.3601 |           3.7% |                 0.21x |       54.7203 |            7.4% |
| Soybeans / ZS=F                     |  20.3571 |           1.5% |                 0.46x |       40.7143 |            3.1% |
| NASDAQ 100 / ^NDX                   | 393.6293 |           1.3% |                 0.62x |      787.2586 |            2.6% |
| Apple Inc. / AAPL                   |   7.5686 |           2.2% |                 0.48x |       15.1371 |            4.5% |
| S&P 500 / ^GSPC                     |  71.6363 |           0.9% |                 0.96x |      143.2727 |            1.8% |
| NVIDIA Corporation / NVDA           |   6.0482 |           2.7% |                 0.22x |       12.0965 |            5.3% |
| Microsoft Corporation / MSFT        |  10.1071 |           2.0% |                 0.45x |       20.2143 |            4.0% |
| Alphabet Inc. Class A / GOOGL       |   8.0976 |           2.3% |                 0.44x |       16.1952 |            4.6% |
| Tesla Inc. / TSLA                   |  13.6600 |           3.6% |                 0.22x |       27.3200 |            7.3% |
| Amazon.com Inc. / AMZN              |   5.3286 |           2.1% |                 0.38x |       10.6571 |            4.1% |
| Wheat / ZW=F                        |  17.3393 |           2.4% |                 0.25x |       34.6786 |            4.8% |
| FTSE 100 / ^FTSE                    | 105.0213 |           1.0% |                 0.98x |      210.0427 |            2.0% |
| Brent Crude Oil / BZ=F              |   4.4500 |           4.4% |                 0.24x |        8.9000 |            8.9% |
| Hang Seng / ^HSI                    | 313.3175 |           1.3% |                 0.87x |      626.6350 |            2.5% |
| Euro Stoxx 50 / ^STOXX50E           |  69.9357 |           1.1% |                 0.79x |      139.8713 |            2.2% |
| JPMorgan Chase & Co. / JPM          |   7.1314 |           2.0% |                 0.73x |       14.2629 |            4.1% |
| Silver / SI=F                       |   1.5657 |           2.4% |                 0.30x |        3.1314 |            4.8% |
| Platinum / PL=F                     |  26.7214 |           1.5% |                 0.31x |       53.4429 |            3.0% |
| DAX / ^GDAXI                        | 272.3015 |           1.1% |                 0.78x |      544.6030 |            2.1% |
| Gold / GC=F                         | 103.2070 |           2.4% |                 0.52x |      206.4141 |            4.7% |
| Dow Jones Industrial Average / ^DJI | 537.7182 |           1.0% |                 0.93x |     1075.4364 |            2.1% |
| CAC 40 / ^FCHI                      |  83.7731 |           1.0% |                 0.77x |      167.5461 |            2.1% |
| Russell 2000 / ^RUT                 |  32.9093 |           1.1% |                 0.89x |       65.8186 |            2.3% |
| UnitedHealth Group Inc. / UNH       |  10.1986 |           2.7% |                 0.49x |       20.3971 |            5.4% |

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

Scoring engine version: **1.0.0** | Git commit: **8cfac97**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
