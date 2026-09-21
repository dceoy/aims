+++
title = "Market Analysis 2026-09-21"
date = "2026-09-21T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: ZC=F (score 73.9)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-09-21.json", "data/history/2026-09-21.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "f6d90b1"
+++

## Market Regime

**Neutral** — 10 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Corn / ZC=F** — score 73.9, 20d return +9.0%, RSI14=62. 20d up +9.0%; above MA20 by 2.3%; RSI14=62
- **Apple Inc. / AAPL** — score 70.3, 20d return +8.0%, RSI14=65. 20d up +8.0%; above MA20 by 4.2%; RSI14=65
- **Soybeans / ZS=F** — score 68.5, 20d return +6.4%, RSI14=57. 20d up +6.4%; above MA20 by 1.5%; RSI14=57
- **Meta Platforms Inc. / META** — score 66.7, 20d return +22.0%, RSI14=78. 20d up +22.0%; above MA20 by 8.3%; RSI14=78
- **NASDAQ 100 / ^NDX** — score 63.6, 20d return +1.5%, RSI14=54. 20d up +1.5%; above MA20 by 1.2%; RSI14=54

## Upcoming Events

_No scheduled events for covered instruments in the next 7 days._

## Signal History

Compared with the previous available report (**2026-09-18**).

- **New top-5:** ZS=F, ^NDX
- **Persistent top signals:** AAPL (7 reports), META (6 reports), ZC=F (4 reports)
- **Dropped from top-5:** MSFT, ^FTSE

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     -2 |   -16.7 |
| 7203.T    |     +0 |    -4.8 |
| 8306.T    |     +0 |    -3.3 |
| AAPL      |     +0 |    -3.9 |
| AMZN      |     +2 |    +4.8 |
| BZ=F      |     +2 |    +5.2 |
| CL=F      |     +0 |    +2.4 |
| GC=F      |     +7 |   +13.0 |
| GOOGL     |     +1 |    +3.6 |
| HG=F      |     +0 |    -3.0 |
| JPM       |     +1 |    +3.6 |
| META      |     -3 |   -10.0 |
| MSFT      |     -7 |   -12.1 |
| NG=F      |     +0 |    +0.9 |
| NVDA      |     +4 |    +9.4 |
| PL=F      |     +6 |   +15.8 |
| SI=F      |     +6 |   +10.3 |
| TSLA      |     -3 |    -6.1 |
| UNH       |     +2 |   +13.3 |
| XOM       |     +0 |    +3.6 |
| ZC=F      |     +2 |    +3.6 |
| ZS=F      |     +3 |    +2.1 |
| ZW=F      |     -4 |    -9.1 |
| ^DJI      |     +2 |    +0.3 |
| ^FCHI     |     -6 |   -16.7 |
| ^FTSE     |    -10 |   -21.5 |
| ^GDAXI    |     -7 |   -17.6 |
| ^GSPC     |     +0 |    +4.2 |
| ^HSI      |     +6 |   +14.5 |
| ^N225     |     +2 |   +23.9 |
| ^NDX      |     +3 |    +6.1 |
| ^RUT      |     -1 |    +0.0 |
| ^STOXX50E |     -6 |   -16.1 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **WTI Crude Oil / CL=F** — malformed_input
- **Copper / HG=F** — malformed_input
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Natural Gas / NG=F** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Nikkei 225 / ^N225** — missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|    1 | Corn / ZC=F            |  73.9 |   Yes    | —               | 20d up +9.0%; above MA20 by 2.3%; RSI14=62   |
|    3 | Soybeans / ZS=F        |  68.5 |   Yes    | —               | 20d up +6.4%; above MA20 by 1.5%; RSI14=57   |
|    7 | Brent Crude Oil / BZ=F |  61.8 |   Yes    | —               | 20d up +12.1%; above MA20 by 6.2%; RSI14=73  |
|    9 | Silver / SI=F          |  58.2 |   Yes    | —               | 20d down -3.9%; above MA20 by 0.6%; RSI14=51 |
|   12 | Platinum / PL=F        |  53.0 |   Yes    | —               | 20d down -4.8%; below MA20 by 0.7%; RSI14=52 |
|   13 | Gold / GC=F            |  47.6 |   Yes    | —               | 20d down -6.0%; below MA20 by 1.3%; RSI14=45 |
|   17 | Wheat / ZW=F           |  40.9 |   Yes    | —               | 20d up +4.8%; below MA20 by 1.7%; RSI14=34   |
|   26 | WTI Crude Oil / CL=F   |  64.5 |    No    | malformed_input | Suppressed: malformed_input                  |
|   27 | Copper / HG=F          |  58.8 |    No    | malformed_input | Suppressed: malformed_input                  |
|   29 | Natural Gas / NG=F     |  52.7 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    2 | Apple Inc. / AAPL                                                              |  70.3 |   Yes    | —                             | 20d up +8.0%; above MA20 by 4.2%; RSI14=65   |
|    4 | Meta Platforms Inc. / META                                                     |  66.7 |   Yes    | —                             | 20d up +22.0%; above MA20 by 8.3%; RSI14=78  |
|    6 | Alphabet Inc. Class A / GOOGL                                                  |  62.4 |   Yes    | —                             | 20d up +2.7%; above MA20 by 2.3%; RSI14=53   |
|    8 | NVIDIA Corporation / NVDA                                                      |  61.5 |   Yes    | —                             | 20d up +2.6%; above MA20 by 1.6%; RSI14=55   |
|   11 | Microsoft Corporation / MSFT                                                   |  56.1 |   Yes    | —                             | 20d up +2.6%; below MA20 by 0.7%; RSI14=39   |
|   14 | Tesla Inc. / TSLA                                                              |  46.7 |   Yes    | —                             | 20d up +5.5%; above MA20 by 1.3%; RSI14=57   |
|   16 | JPMorgan Chase & Co. / JPM                                                     |  41.2 |   Yes    | —                             | 20d down -0.5%; below MA20 by 1.4%; RSI14=39 |
|   19 | Amazon.com Inc. / AMZN                                                         |  37.6 |   Yes    | —                             | 20d down -2.5%; below MA20 by 0.9%; RSI14=36 |
|   23 | UnitedHealth Group Inc. / UNH                                                  |  29.1 |   Yes    | —                             | 20d down -1.5%; below MA20 by 3.0%; RSI14=39 |
|   28 | Exxon Mobil Corporation / XOM                                                  |  56.7 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   30 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  47.0 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   32 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  38.8 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   33 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  31.8 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    5 | NASDAQ 100 / ^NDX                   |  63.6 |   Yes    | —            | 20d up +1.5%; above MA20 by 1.2%; RSI14=54   |
|   10 | S&P 500 / ^GSPC                     |  58.2 |   Yes    | —            | 20d up +0.1%; below MA20 by 0.1%; RSI14=45   |
|   15 | FTSE 100 / ^FTSE                    |  46.1 |   Yes    | —            | 20d down -0.8%; below MA20 by 1.0%; RSI14=40 |
|   18 | Hang Seng / ^HSI                    |  39.4 |   Yes    | —            | 20d down -4.8%; below MA20 by 1.8%; RSI14=32 |
|   20 | Dow Jones Industrial Average / ^DJI |  32.7 |   Yes    | —            | 20d down -2.0%; below MA20 by 2.1%; RSI14=33 |
|   21 | DAX / ^GDAXI                        |  31.2 |   Yes    | —            | 20d down -3.2%; below MA20 by 2.2%; RSI14=30 |
|   22 | Euro Stoxx 50 / ^STOXX50E           |  30.3 |   Yes    | —            | 20d down -3.5%; below MA20 by 2.0%; RSI14=34 |
|   24 | Russell 2000 / ^RUT                 |  25.4 |   Yes    | —            | 20d down -4.4%; below MA20 by 2.7%; RSI14=30 |
|   25 | CAC 40 / ^FCHI                      |  20.3 |   Yes    | —            | 20d down -4.9%; below MA20 by 2.4%; RSI14=30 |
|   31 | Nikkei 225 / ^N225                  |  47.0 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-09-18 |
| 7203.T    | 2026-09-18 |
| 8306.T    | 2026-09-18 |
| AAPL      | 2026-09-18 |
| AMZN      | 2026-09-18 |
| BZ=F      | 2026-09-18 |
| CL=F      | 2026-09-18 |
| GC=F      | 2026-09-18 |
| GOOGL     | 2026-09-18 |
| HG=F      | 2026-09-18 |
| JPM       | 2026-09-18 |
| META      | 2026-09-18 |
| MSFT      | 2026-09-18 |
| NG=F      | 2026-09-18 |
| NVDA      | 2026-09-18 |
| PL=F      | 2026-09-18 |
| SI=F      | 2026-09-18 |
| TSLA      | 2026-09-18 |
| UNH       | 2026-09-18 |
| XOM       | 2026-09-18 |
| ZC=F      | 2026-09-18 |
| ZS=F      | 2026-09-18 |
| ZW=F      | 2026-09-18 |
| ^DJI      | 2026-09-18 |
| ^FCHI     | 2026-09-18 |
| ^FTSE     | 2026-09-18 |
| ^GDAXI    | 2026-09-18 |
| ^GSPC     | 2026-09-18 |
| ^HSI      | 2026-09-18 |
| ^N225     | 2026-09-18 |
| ^NDX      | 2026-09-18 |
| ^RUT      | 2026-09-18 |
| ^STOXX50E | 2026-09-18 |

## Symbol Details

### Corn / ZC=F (score 73.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.6% |
| ret_5d     |  +3.4% |
| ret_20d    |  +9.0% |
| ret_60d    | +31.2% |
| ma20_dist  |  +2.3% |
| ma50_dist  | +10.1% |
| vol_20d    |  39.7% |
| mdd_60d    |   6.0% |
| rsi_14     |   61.6 |
| zscore_20d |    1.1 |

### Apple Inc. / AAPL (score 70.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.3% |
| ret_5d     |  +1.2% |
| ret_20d    |  +8.0% |
| ret_60d    | +14.7% |
| ma20_dist  |  +4.2% |
| ma50_dist  |  +5.0% |
| vol_20d    |  21.3% |
| mdd_60d    |  11.0% |
| rsi_14     |   65.4 |
| zscore_20d |    1.5 |

### Soybeans / ZS=F (score 68.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.2% |
| ret_5d     |  +1.8% |
| ret_20d    |  +6.4% |
| ret_60d    | +17.6% |
| ma20_dist  |  +1.5% |
| ma50_dist  |  +6.1% |
| vol_20d    |  21.1% |
| mdd_60d    |   8.1% |
| rsi_14     |   57.4 |
| zscore_20d |    0.6 |

### Meta Platforms Inc. / META (score 66.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.4% |
| ret_5d     |  +2.7% |
| ret_20d    | +22.0% |
| ret_60d    | +19.4% |
| ma20_dist  |  +8.3% |
| ma50_dist  |  +9.6% |
| vol_20d    |  29.6% |
| mdd_60d    |  20.9% |
| rsi_14     |   77.9 |
| zscore_20d |    1.2 |

### NASDAQ 100 / ^NDX (score 63.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | +0.9% |
| ret_20d    | +1.5% |
| ret_60d    | +1.5% |
| ma20_dist  | +1.2% |
| ma50_dist  | +1.6% |
| vol_20d    | 13.1% |
| mdd_60d    | 10.2% |
| rsi_14     |  53.9 |
| zscore_20d |   1.6 |

### Alphabet Inc. Class A / GOOGL (score 62.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | +3.3% |
| ret_20d    | +2.7% |
| ret_60d    | +1.2% |
| ma20_dist  | +2.3% |
| ma50_dist  | +1.2% |
| vol_20d    | 22.6% |
| mdd_60d    | 14.4% |
| rsi_14     |  52.5 |
| zscore_20d |   1.5 |

### Brent Crude Oil / BZ=F (score 61.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.9% |
| ret_5d     |  -0.7% |
| ret_20d    | +12.1% |
| ret_60d    | +42.4% |
| ma20_dist  |  +6.2% |
| ma50_dist  | +12.4% |
| vol_20d    |  38.7% |
| mdd_60d    |  21.2% |
| rsi_14     |   72.8 |
| zscore_20d |    0.9 |

### NVIDIA Corporation / NVDA (score 61.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.3% |
| ret_5d     |  +1.8% |
| ret_20d    |  +2.6% |
| ret_60d    | +11.7% |
| ma20_dist  |  +1.6% |
| ma50_dist  |  +3.8% |
| vol_20d    |  45.3% |
| mdd_60d    |  10.6% |
| rsi_14     |   55.0 |
| zscore_20d |    0.6 |

### Silver / SI=F (score 58.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.7% |
| ret_5d     |  +3.1% |
| ret_20d    |  -3.9% |
| ret_60d    | +11.9% |
| ma20_dist  |  +0.6% |
| ma50_dist  |  +4.7% |
| vol_20d    |  33.3% |
| mdd_60d    |   9.7% |
| rsi_14     |   51.0 |
| zscore_20d |    0.2 |

### S&P 500 / ^GSPC (score 58.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | -0.1% |
| ret_20d    | +0.1% |
| ret_60d    | +4.0% |
| ma20_dist  | -0.1% |
| ma50_dist  | +0.4% |
| vol_20d    |  9.2% |
| mdd_60d    |  3.4% |
| rsi_14     |  45.1 |
| zscore_20d |  -0.2 |

### Microsoft Corporation / MSFT (score 56.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.8% |
| ret_5d     |  -0.4% |
| ret_20d    |  +2.6% |
| ret_60d    | +35.1% |
| ma20_dist  |  -0.7% |
| ma50_dist  |  +6.4% |
| vol_20d    |  21.5% |
| mdd_60d    |   5.1% |
| rsi_14     |   38.9 |
| zscore_20d |   -0.5 |

### Platinum / PL=F (score 53.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.7% |
| ret_5d     |  +0.6% |
| ret_20d    |  -4.8% |
| ret_60d    | +16.3% |
| ma20_dist  |  -0.7% |
| ma50_dist  |  +3.1% |
| vol_20d    |  32.7% |
| mdd_60d    |   7.4% |
| rsi_14     |   52.0 |
| zscore_20d |   -0.3 |

### Gold / GC=F (score 47.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.6% |
| ret_5d     |  +0.4% |
| ret_20d    |  -6.0% |
| ret_60d    | +10.0% |
| ma20_dist  |  -1.3% |
| ma50_dist  |  +1.8% |
| vol_20d    |  18.9% |
| mdd_60d    |   7.9% |
| rsi_14     |   45.1 |
| zscore_20d |   -0.5 |

### Tesla Inc. / TSLA (score 46.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | -0.3% |
| ret_20d    | +5.5% |
| ret_60d    | -3.0% |
| ma20_dist  | +1.3% |
| ma50_dist  | +4.0% |
| vol_20d    | 47.9% |
| mdd_60d    | 29.9% |
| rsi_14     |  56.8 |
| zscore_20d |   0.6 |

### FTSE 100 / ^FTSE (score 46.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.5% |
| ret_5d     | +0.1% |
| ret_20d    | -0.8% |
| ret_60d    | +1.2% |
| ma20_dist  | -1.0% |
| ma50_dist  | -0.8% |
| vol_20d    | 10.1% |
| mdd_60d    |  2.7% |
| rsi_14     |  39.8 |
| zscore_20d |  -1.3 |

### JPMorgan Chase & Co. / JPM (score 41.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | -1.8% |
| ret_20d    | -0.5% |
| ret_60d    | +5.3% |
| ma20_dist  | -1.4% |
| ma50_dist  | -1.0% |
| vol_20d    | 13.5% |
| mdd_60d    |  4.5% |
| rsi_14     |  39.0 |
| zscore_20d |  -1.4 |

### Wheat / ZW=F (score 40.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.8% |
| ret_5d     |  +1.0% |
| ret_20d    |  +4.8% |
| ret_60d    | +25.4% |
| ma20_dist  |  -1.7% |
| ma50_dist  |  +3.6% |
| vol_20d    |  42.7% |
| mdd_60d    |  10.7% |
| rsi_14     |   34.3 |
| zscore_20d |   -0.5 |

### Hang Seng / ^HSI (score 39.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | -0.2% |
| ret_20d    | -4.8% |
| ret_60d    | +7.3% |
| ma20_dist  | -1.8% |
| ma50_dist  | -2.2% |
| vol_20d    | 12.1% |
| mdd_60d    |  5.4% |
| rsi_14     |  32.3 |
| zscore_20d |  -1.3 |

### Amazon.com Inc. / AMZN (score 37.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.0% |
| ret_5d     | -1.2% |
| ret_20d    | -2.5% |
| ret_60d    | +8.3% |
| ma20_dist  | -0.9% |
| ma50_dist  | -0.8% |
| vol_20d    | 25.6% |
| mdd_60d    | 13.4% |
| rsi_14     |  36.2 |
| zscore_20d |  -0.5 |

### Dow Jones Industrial Average / ^DJI (score 32.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | -1.7% |
| ret_20d    | -2.0% |
| ret_60d    | -0.3% |
| ma20_dist  | -2.1% |
| ma50_dist  | -2.3% |
| vol_20d    | 11.1% |
| mdd_60d    |  5.3% |
| rsi_14     |  32.5 |
| zscore_20d |  -1.6 |

### DAX / ^GDAXI (score 31.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.6% |
| ret_5d     | -1.0% |
| ret_20d    | -3.2% |
| ret_60d    | +2.6% |
| ma20_dist  | -2.2% |
| ma50_dist  | -1.8% |
| vol_20d    | 12.1% |
| mdd_60d    |  4.8% |
| rsi_14     |  30.2 |
| zscore_20d |  -1.6 |

### Euro Stoxx 50 / ^STOXX50E (score 30.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.4% |
| ret_5d     | -1.4% |
| ret_20d    | -3.5% |
| ret_60d    | +0.2% |
| ma20_dist  | -2.0% |
| ma50_dist  | -2.2% |
| vol_20d    | 11.6% |
| mdd_60d    |  4.8% |
| rsi_14     |  33.9 |
| zscore_20d |  -1.6 |

### UnitedHealth Group Inc. / UNH (score 29.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | +0.0% |
| ret_20d    | -1.5% |
| ret_60d    | -7.1% |
| ma20_dist  | -3.0% |
| ma50_dist  | -6.5% |
| vol_20d    | 21.2% |
| mdd_60d    | 14.0% |
| rsi_14     |  38.8 |
| zscore_20d |  -1.4 |

### Russell 2000 / ^RUT (score 25.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | -1.5% |
| ret_20d    | -4.4% |
| ret_60d    | -4.2% |
| ma20_dist  | -2.7% |
| ma50_dist  | -3.7% |
| vol_20d    | 11.6% |
| mdd_60d    |  6.8% |
| rsi_14     |  30.1 |
| zscore_20d |  -1.5 |

### CAC 40 / ^FCHI (score 20.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.5% |
| ret_5d     | -1.4% |
| ret_20d    | -4.9% |
| ret_60d    | -3.8% |
| ma20_dist  | -2.4% |
| ma50_dist  | -4.1% |
| vol_20d    | 12.3% |
| mdd_60d    |  7.6% |
| rsi_14     |  30.1 |
| zscore_20d |  -1.6 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Corn / ZC=F                         |  10.4286 |           2.0% |                 0.25x |       20.8571 |            4.0% |
| Apple Inc. / AAPL                   |   7.7007 |           2.3% |                 0.47x |       15.4014 |            4.6% |
| Soybeans / ZS=F                     |  19.4643 |           1.5% |                 0.47x |       38.9286 |            3.0% |
| Meta Platforms Inc. / META          |  21.7886 |           3.3% |                 0.34x |       43.5771 |            6.5% |
| NASDAQ 100 / ^NDX                   | 341.2179 |           1.2% |                 0.76x |      682.4358 |            2.3% |
| Alphabet Inc. Class A / GOOGL       |   8.1629 |           2.3% |                 0.44x |       16.3258 |            4.7% |
| Brent Crude Oil / BZ=F              |   4.3764 |           4.2% |                 0.26x |        8.7529 |            8.4% |
| NVIDIA Corporation / NVDA           |   5.9157 |           2.7% |                 0.22x |       11.8314 |            5.3% |
| Silver / SI=F                       |   1.7089 |           2.6% |                 0.30x |        3.4179 |            5.1% |
| S&P 500 / ^GSPC                     |  65.7777 |           0.9% |                 1.09x |      131.5555 |            1.7% |
| Microsoft Corporation / MSFT        |   9.8643 |           2.0% |                 0.47x |       19.7286 |            4.0% |
| Platinum / PL=F                     |  28.2857 |           1.6% |                 0.31x |       56.5714 |            3.1% |
| Gold / GC=F                         | 108.6499 |           2.5% |                 0.53x |      217.2997 |            4.9% |
| Tesla Inc. / TSLA                   |  14.2086 |           3.9% |                 0.21x |       28.4171 |            7.8% |
| FTSE 100 / ^FTSE                    | 106.5642 |           1.0% |                 0.99x |      213.1285 |            2.0% |
| JPMorgan Chase & Co. / JPM          |   7.0007 |           2.0% |                 0.74x |       14.0014 |            4.0% |
| Wheat / ZW=F                        |  18.0536 |           2.5% |                 0.23x |       36.1071 |            5.1% |
| Hang Seng / ^HSI                    | 314.8175 |           1.3% |                 0.83x |      629.6350 |            2.5% |
| Amazon.com Inc. / AMZN              |   5.5729 |           2.2% |                 0.39x |       11.1457 |            4.4% |
| Dow Jones Industrial Average / ^DJI | 537.0346 |           1.0% |                 0.90x |     1074.0692 |            2.1% |
| DAX / ^GDAXI                        | 274.2600 |           1.1% |                 0.83x |      548.5201 |            2.2% |
| Euro Stoxx 50 / ^STOXX50E           |  68.7100 |           1.1% |                 0.86x |      137.4199 |            2.2% |
| UnitedHealth Group Inc. / UNH       |  10.3135 |           2.7% |                 0.47x |       20.6269 |            5.5% |
| Russell 2000 / ^RUT                 |  33.2643 |           1.2% |                 0.86x |       66.5286 |            2.3% |
| CAC 40 / ^FCHI                      |  84.1152 |           1.0% |                 0.81x |      168.2303 |            2.1% |

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

Scoring engine version: **1.0.0** | Git commit: **f6d90b1**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
