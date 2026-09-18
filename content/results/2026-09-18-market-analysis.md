+++
title = "Market Analysis 2026-09-18"
date = "2026-09-18T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: META (score 76.7)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-09-18.json", "data/history/2026-09-18.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "de970f7"
+++

## Market Regime

**Neutral** — 12 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Meta Platforms Inc. / META** — score 76.7, 20d return +25.0%, RSI14=88. 20d up +25.0%; above MA20 by 12.1%; RSI14=88
- **Apple Inc. / AAPL** — score 74.2, 20d return +6.4%, RSI14=69. 20d up +6.4%; above MA20 by 4.9%; RSI14=69
- **Corn / ZC=F** — score 70.3, 20d return +10.8%, RSI14=65. 20d up +10.8%; above MA20 by 3.3%; RSI14=65
- **Microsoft Corporation / MSFT** — score 68.2, 20d return +3.0%, RSI14=46. 20d up +3.0%; above MA20 by 0.2%; RSI14=46
- **FTSE 100 / ^FTSE** — score 67.6, 20d return +0.7%, RSI14=52. 20d up +0.7%; above MA20 by 0.4%; RSI14=52

## Upcoming Events

_No scheduled events for covered instruments in the next 7 days._

## Signal History

Compared with the previous available report (**2026-09-17**).

- **New top-5:** MSFT, ^FTSE
- **Persistent top signals:** AAPL (6 reports), META (5 reports), ZC=F (3 reports)
- **Dropped from top-5:** BZ=F, ZS=F

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +0 |    -0.6 |
| 7203.T    |     -3 |    -7.3 |
| 8306.T    |     -3 |   -11.5 |
| AAPL      |     +2 |    +2.4 |
| AMZN      |     +3 |   +13.6 |
| BZ=F      |     -4 |    -9.4 |
| CL=F      |     +0 |    -7.0 |
| GC=F      |     -6 |    -9.1 |
| GOOGL     |     +3 |    +7.9 |
| HG=F      |     +5 |   +17.6 |
| JPM       |     +2 |    -3.0 |
| META      |     +1 |    +1.8 |
| MSFT      |     +3 |    +7.3 |
| NG=F      |     +1 |    +1.2 |
| NVDA      |     +6 |   +10.9 |
| PL=F      |     -3 |    -6.4 |
| SI=F      |     +6 |   +12.4 |
| TSLA      |     +5 |    +9.4 |
| UNH       |     +0 |    -2.4 |
| XOM       |     +0 |    -4.8 |
| ZC=F      |     -2 |    -4.8 |
| ZS=F      |     -3 |    -7.3 |
| ZW=F      |     -7 |   -14.6 |
| ^DJI      |     +0 |    +3.6 |
| ^FCHI     |     -2 |    -5.5 |
| ^FTSE     |     +3 |   +10.3 |
| ^GDAXI    |     -5 |    -3.3 |
| ^GSPC     |     +1 |    +7.3 |
| ^HSI      |     -4 |   -12.1 |
| ^N225     |     +0 |   -10.6 |
| ^NDX      |     +5 |   +13.3 |
| ^RUT      |     +0 |    +0.9 |
| ^STOXX50E |     -4 |    -0.3 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **WTI Crude Oil / CL=F** — malformed_input
- **Copper / HG=F** — malformed_input
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Natural Gas / NG=F** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Nikkei 225 / ^N225** — missing_bars

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|    3 | Corn / ZC=F            |  70.3 |   Yes    | —               | 20d up +10.8%; above MA20 by 3.3%; RSI14=65  |
|    6 | Soybeans / ZS=F        |  66.4 |   Yes    | —               | 20d up +8.1%; above MA20 by 3.1%; RSI14=67   |
|    9 | Brent Crude Oil / BZ=F |  56.7 |   Yes    | —               | 20d up +11.0%; above MA20 by 7.8%; RSI14=76  |
|   13 | Wheat / ZW=F           |  50.0 |   Yes    | —               | 20d up +6.5%; above MA20 by 0.3%; RSI14=46   |
|   15 | Silver / SI=F          |  47.9 |   Yes    | —               | 20d down -5.8%; below MA20 by 1.2%; RSI14=45 |
|   18 | Platinum / PL=F        |  37.3 |   Yes    | —               | 20d down -5.1%; below MA20 by 1.6%; RSI14=43 |
|   20 | Gold / GC=F            |  34.5 |   Yes    | —               | 20d down -6.0%; below MA20 by 2.1%; RSI14=39 |
|   26 | WTI Crude Oil / CL=F   |  62.1 |    No    | malformed_input | Suppressed: malformed_input                  |
|   27 | Copper / HG=F          |  61.8 |    No    | malformed_input | Suppressed: malformed_input                  |
|   29 | Natural Gas / NG=F     |  51.8 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    1 | Meta Platforms Inc. / META                                                     |  76.7 |   Yes    | —                             | 20d up +25.0%; above MA20 by 12.1%; RSI14=88 |
|    2 | Apple Inc. / AAPL                                                              |  74.2 |   Yes    | —                             | 20d up +6.4%; above MA20 by 4.9%; RSI14=69   |
|    4 | Microsoft Corporation / MSFT                                                   |  68.2 |   Yes    | —                             | 20d up +3.0%; above MA20 by 0.2%; RSI14=46   |
|    7 | Alphabet Inc. Class A / GOOGL                                                  |  58.8 |   Yes    | —                             | 20d up +0.8%; above MA20 by 1.8%; RSI14=55   |
|   11 | Tesla Inc. / TSLA                                                              |  52.7 |   Yes    | —                             | 20d up +4.3%; above MA20 by 2.1%; RSI14=55   |
|   12 | NVIDIA Corporation / NVDA                                                      |  52.1 |   Yes    | —                             | 20d up +0.9%; above MA20 by 0.4%; RSI14=43   |
|   17 | JPMorgan Chase & Co. / JPM                                                     |  37.6 |   Yes    | —                             | 20d down -2.2%; below MA20 by 1.5%; RSI14=44 |
|   21 | Amazon.com Inc. / AMZN                                                         |  32.7 |   Yes    | —                             | 20d down -5.5%; below MA20 by 2.1%; RSI14=45 |
|   25 | UnitedHealth Group Inc. / UNH                                                  |  15.8 |   Yes    | —                             | 20d down -2.9%; below MA20 by 3.5%; RSI14=36 |
|   28 | Exxon Mobil Corporation / XOM                                                  |  53.0 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   30 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  50.3 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   31 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  48.5 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   32 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  43.6 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    5 | FTSE 100 / ^FTSE                    |  67.6 |   Yes    | —            | 20d up +0.7%; above MA20 by 0.4%; RSI14=52   |
|    8 | NASDAQ 100 / ^NDX                   |  57.6 |   Yes    | —            | 20d up +0.1%; above MA20 by 0.6%; RSI14=46   |
|   10 | S&P 500 / ^GSPC                     |  53.9 |   Yes    | —            | 20d down -0.9%; below MA20 by 0.3%; RSI14=43 |
|   14 | DAX / ^GDAXI                        |  48.8 |   Yes    | —            | 20d down -1.0%; below MA20 by 0.8%; RSI14=32 |
|   16 | Euro Stoxx 50 / ^STOXX50E           |  46.4 |   Yes    | —            | 20d down -1.5%; below MA20 by 0.8%; RSI14=35 |
|   19 | CAC 40 / ^FCHI                      |  37.0 |   Yes    | —            | 20d down -3.1%; below MA20 by 1.2%; RSI14=33 |
|   22 | Dow Jones Industrial Average / ^DJI |  32.4 |   Yes    | —            | 20d down -3.2%; below MA20 by 2.1%; RSI14=33 |
|   23 | Russell 2000 / ^RUT                 |  25.4 |   Yes    | —            | 20d down -5.2%; below MA20 by 2.5%; RSI14=27 |
|   24 | Hang Seng / ^HSI                    |  24.9 |   Yes    | —            | 20d down -4.3%; below MA20 by 2.7%; RSI14=27 |
|   33 | Nikkei 225 / ^N225                  |  23.0 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-09-17 |
| 7203.T    | 2026-09-17 |
| 8306.T    | 2026-09-17 |
| AAPL      | 2026-09-17 |
| AMZN      | 2026-09-17 |
| BZ=F      | 2026-09-17 |
| CL=F      | 2026-09-17 |
| GC=F      | 2026-09-17 |
| GOOGL     | 2026-09-17 |
| HG=F      | 2026-09-17 |
| JPM       | 2026-09-17 |
| META      | 2026-09-17 |
| MSFT      | 2026-09-17 |
| NG=F      | 2026-09-17 |
| NVDA      | 2026-09-17 |
| PL=F      | 2026-09-17 |
| SI=F      | 2026-09-17 |
| TSLA      | 2026-09-17 |
| UNH       | 2026-09-17 |
| XOM       | 2026-09-17 |
| ZC=F      | 2026-09-17 |
| ZS=F      | 2026-09-17 |
| ZW=F      | 2026-09-17 |
| ^DJI      | 2026-09-17 |
| ^FCHI     | 2026-09-17 |
| ^FTSE     | 2026-09-17 |
| ^GDAXI    | 2026-09-17 |
| ^GSPC     | 2026-09-17 |
| ^HSI      | 2026-09-17 |
| ^N225     | 2026-09-17 |
| ^NDX      | 2026-09-17 |
| ^RUT      | 2026-09-17 |
| ^STOXX50E | 2026-09-17 |

## Symbol Details

### Meta Platforms Inc. / META (score 76.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.3% |
| ret_5d     |  +5.9% |
| ret_20d    | +25.0% |
| ret_60d    | +21.4% |
| ma20_dist  | +12.1% |
| ma50_dist  | +12.5% |
| vol_20d    |  27.2% |
| mdd_60d    |  20.9% |
| rsi_14     |   87.6 |
| zscore_20d |    1.7 |

### Apple Inc. / AAPL (score 74.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.4% |
| ret_5d     |  +3.2% |
| ret_20d    |  +6.4% |
| ret_60d    | +14.5% |
| ma20_dist  |  +4.9% |
| ma50_dist  |  +5.4% |
| vol_20d    |  22.5% |
| mdd_60d    |  11.0% |
| rsi_14     |   69.4 |
| zscore_20d |    1.8 |

### Corn / ZC=F (score 70.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.7% |
| ret_5d     |  +3.2% |
| ret_20d    | +10.8% |
| ret_60d    | +28.5% |
| ma20_dist  |  +3.3% |
| ma50_dist  | +11.2% |
| vol_20d    |  39.6% |
| mdd_60d    |   6.0% |
| rsi_14     |   65.4 |
| zscore_20d |    1.4 |

### Microsoft Corporation / MSFT (score 68.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.5% |
| ret_5d     |  +1.1% |
| ret_20d    |  +3.0% |
| ret_60d    | +33.1% |
| ma20_dist  |  +0.2% |
| ma50_dist  |  +7.7% |
| vol_20d    |  21.3% |
| mdd_60d    |   5.1% |
| rsi_14     |   46.1 |
| zscore_20d |    0.1 |

### FTSE 100 / ^FTSE (score 67.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.2% |
| ret_5d     | +2.0% |
| ret_20d    | +0.7% |
| ret_60d    | +3.4% |
| ma20_dist  | +0.4% |
| ma50_dist  | +0.7% |
| vol_20d    |  8.7% |
| mdd_60d    |  2.7% |
| rsi_14     |  51.7 |
| zscore_20d |   0.6 |

### Soybeans / ZS=F (score 66.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.1% |
| ret_5d     |  +0.3% |
| ret_20d    |  +8.1% |
| ret_60d    | +17.2% |
| ma20_dist  |  +3.1% |
| ma50_dist  |  +7.6% |
| vol_20d    |  20.3% |
| mdd_60d    |   8.1% |
| rsi_14     |   66.8 |
| zscore_20d |    1.2 |

### Alphabet Inc. Class A / GOOGL (score 58.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.3% |
| ret_5d     | +4.4% |
| ret_20d    | +0.8% |
| ret_60d    | +0.3% |
| ma20_dist  | +1.8% |
| ma50_dist  | +0.5% |
| vol_20d    | 23.0% |
| mdd_60d    | 14.4% |
| rsi_14     |  55.2 |
| zscore_20d |   1.2 |

### NASDAQ 100 / ^NDX (score 57.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.7% |
| ret_5d     | +1.2% |
| ret_20d    | +0.1% |
| ret_60d    | +0.3% |
| ma20_dist  | +0.6% |
| ma50_dist  | +0.9% |
| vol_20d    | 13.2% |
| mdd_60d    | 10.2% |
| rsi_14     |  46.4 |
| zscore_20d |   0.8 |

### Brent Crude Oil / BZ=F (score 56.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.0% |
| ret_5d     |  -2.6% |
| ret_20d    | +11.0% |
| ret_60d    | +43.3% |
| ma20_dist  |  +7.8% |
| ma50_dist  | +13.9% |
| vol_20d    |  39.3% |
| mdd_60d    |  21.2% |
| rsi_14     |   76.2 |
| zscore_20d |    1.1 |

### S&P 500 / ^GSPC (score 53.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | +0.6% |
| ret_20d    | -0.9% |
| ret_60d    | +3.7% |
| ma20_dist  | -0.3% |
| ma50_dist  | +0.3% |
| vol_20d    |  9.6% |
| mdd_60d    |  3.4% |
| rsi_14     |  42.6 |
| zscore_20d |  -0.4 |

### Tesla Inc. / TSLA (score 52.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.3% |
| ret_5d     | +0.7% |
| ret_20d    | +4.3% |
| ret_60d    | -4.0% |
| ma20_dist  | +2.1% |
| ma50_dist  | +4.3% |
| vol_20d    | 48.4% |
| mdd_60d    | 29.9% |
| rsi_14     |  54.8 |
| zscore_20d |   0.9 |

### NVIDIA Corporation / NVDA (score 52.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.5% |
| ret_5d     | +0.4% |
| ret_20d    | +0.9% |
| ret_60d    | +9.6% |
| ma20_dist  | +0.4% |
| ma50_dist  | +2.6% |
| vol_20d    | 45.1% |
| mdd_60d    | 10.6% |
| rsi_14     |  42.7 |
| zscore_20d |   0.1 |

### Wheat / ZW=F (score 50.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.5% |
| ret_5d     |  +0.5% |
| ret_20d    |  +6.5% |
| ret_60d    | +25.7% |
| ma20_dist  |  +0.3% |
| ma50_dist  |  +5.7% |
| vol_20d    |  42.1% |
| mdd_60d    |  10.7% |
| rsi_14     |   45.6 |
| zscore_20d |    0.1 |

### DAX / ^GDAXI (score 48.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | +1.4% |
| ret_20d    | -1.0% |
| ret_60d    | +2.9% |
| ma20_dist  | -0.8% |
| ma50_dist  | -0.2% |
| vol_20d    | 11.1% |
| mdd_60d    |  4.5% |
| rsi_14     |  31.6 |
| zscore_20d |  -0.6 |

### Silver / SI=F (score 47.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.8% |
| ret_5d     |  +1.8% |
| ret_20d    |  -5.8% |
| ret_60d    | +12.5% |
| ma20_dist  |  -1.2% |
| ma50_dist  |  +3.3% |
| vol_20d    |  32.6% |
| mdd_60d    |   9.7% |
| rsi_14     |   45.2 |
| zscore_20d |   -0.4 |

### Euro Stoxx 50 / ^STOXX50E (score 46.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | +0.9% |
| ret_20d    | -1.5% |
| ret_60d    | +0.9% |
| ma20_dist  | -0.8% |
| ma50_dist  | -0.9% |
| vol_20d    | 11.0% |
| mdd_60d    |  4.8% |
| rsi_14     |  35.2 |
| zscore_20d |  -0.7 |

### JPMorgan Chase & Co. / JPM (score 37.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | -1.2% |
| ret_20d    | -2.2% |
| ret_60d    | +5.0% |
| ma20_dist  | -1.5% |
| ma50_dist  | -1.0% |
| vol_20d    | 14.5% |
| mdd_60d    |  4.5% |
| rsi_14     |  43.7 |
| zscore_20d |  -1.6 |

### Platinum / PL=F (score 37.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.5% |
| ret_5d     |  -0.3% |
| ret_20d    |  -5.1% |
| ret_60d    | +13.8% |
| ma20_dist  |  -1.6% |
| ma50_dist  |  +2.6% |
| vol_20d    |  32.6% |
| mdd_60d    |   7.4% |
| rsi_14     |   43.3 |
| zscore_20d |   -0.7 |

### CAC 40 / ^FCHI (score 37.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | +0.9% |
| ret_20d    | -3.1% |
| ret_60d    | -2.9% |
| ma20_dist  | -1.2% |
| ma50_dist  | -2.7% |
| vol_20d    | 11.6% |
| mdd_60d    |  7.3% |
| rsi_14     |  32.8 |
| zscore_20d |  -0.8 |

### Gold / GC=F (score 34.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | -0.2% |
| ret_20d    | -6.0% |
| ret_60d    | +9.4% |
| ma20_dist  | -2.1% |
| ma50_dist  | +1.4% |
| vol_20d    | 18.9% |
| mdd_60d    |  7.9% |
| rsi_14     |  39.1 |
| zscore_20d |  -0.8 |

### Amazon.com Inc. / AMZN (score 32.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.1% |
| ret_5d     | -0.3% |
| ret_20d    | -5.5% |
| ret_60d    | +7.3% |
| ma20_dist  | -2.1% |
| ma50_dist  | -1.8% |
| vol_20d    | 26.2% |
| mdd_60d    | 13.4% |
| rsi_14     |  45.3 |
| zscore_20d |  -1.1 |

### Dow Jones Industrial Average / ^DJI (score 32.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | -0.5% |
| ret_20d    | -3.2% |
| ret_60d    | +0.2% |
| ma20_dist  | -2.1% |
| ma50_dist  | -2.1% |
| vol_20d    | 11.8% |
| mdd_60d    |  5.3% |
| rsi_14     |  33.0 |
| zscore_20d |  -1.7 |

### Russell 2000 / ^RUT (score 25.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | -0.6% |
| ret_20d    | -5.2% |
| ret_60d    | -3.4% |
| ma20_dist  | -2.5% |
| ma50_dist  | -3.3% |
| vol_20d    | 12.2% |
| mdd_60d    |  6.8% |
| rsi_14     |  27.3 |
| zscore_20d |  -1.4 |

### Hang Seng / ^HSI (score 24.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -1.4% |
| ret_20d    | -4.3% |
| ret_60d    | +5.1% |
| ma20_dist  | -2.7% |
| ma50_dist  | -2.7% |
| vol_20d    | 12.8% |
| mdd_60d    |  5.4% |
| rsi_14     |  27.4 |
| zscore_20d |  -1.8 |

### UnitedHealth Group Inc. / UNH (score 15.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.0% |
| ret_5d     | -2.8% |
| ret_20d    | -2.9% |
| ret_60d    | -8.3% |
| ma20_dist  | -3.5% |
| ma50_dist  | -7.2% |
| vol_20d    | 21.3% |
| mdd_60d    | 14.0% |
| rsi_14     |  35.8 |
| zscore_20d |  -1.7 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Meta Platforms Inc. / META          |  20.9914 |           3.1% |                 0.37x |       41.9829 |            6.2% |
| Apple Inc. / AAPL                   |   7.8314 |           2.3% |                 0.45x |       15.6629 |            4.6% |
| Corn / ZC=F                         |  10.6429 |           2.0% |                 0.25x |       21.2857 |            4.0% |
| Microsoft Corporation / MSFT        |  10.2472 |           2.1% |                 0.47x |       20.4943 |            4.1% |
| FTSE 100 / ^FTSE                    |  98.4714 |           0.9% |                 1.15x |      196.9428 |            1.8% |
| Soybeans / ZS=F                     |  19.4464 |           1.5% |                 0.49x |       38.8929 |            2.9% |
| Alphabet Inc. Class A / GOOGL       |   7.9311 |           2.3% |                 0.44x |       15.8621 |            4.6% |
| NASDAQ 100 / ^NDX                   | 347.8571 |           1.2% |                 0.76x |      695.7143 |            2.4% |
| Brent Crude Oil / BZ=F              |   4.3329 |           4.1% |                 0.25x |        8.6657 |            8.3% |
| S&P 500 / ^GSPC                     |  67.4863 |           0.9% |                 1.04x |      134.9726 |            1.8% |
| Tesla Inc. / TSLA                   |  14.4550 |           3.9% |                 0.21x |       28.9100 |            7.9% |
| NVIDIA Corporation / NVDA           |   6.4683 |           2.9% |                 0.22x |       12.9365 |            5.9% |
| Wheat / ZW=F                        |  19.3214 |           2.7% |                 0.24x |       38.6429 |            5.3% |
| DAX / ^GDAXI                        | 266.3736 |           1.0% |                 0.90x |      532.7472 |            2.1% |
| Silver / SI=F                       |   1.6993 |           2.6% |                 0.31x |        3.3986 |            5.2% |
| Euro Stoxx 50 / ^STOXX50E           |  65.8092 |           1.0% |                 0.91x |      131.6184 |            2.1% |
| JPMorgan Chase & Co. / JPM          |   6.9900 |           2.0% |                 0.69x |       13.9800 |            4.0% |
| Platinum / PL=F                     |  31.6500 |           1.8% |                 0.31x |       63.3000 |            3.5% |
| CAC 40 / ^FCHI                      |  80.6658 |           1.0% |                 0.86x |      161.3317 |            2.0% |
| Gold / GC=F                         | 109.8427 |           2.5% |                 0.53x |      219.6855 |            5.0% |
| Amazon.com Inc. / AMZN              |   6.0771 |           2.4% |                 0.38x |       12.1543 |            4.8% |
| Dow Jones Industrial Average / ^DJI | 537.1007 |           1.0% |                 0.84x |     1074.2015 |            2.1% |
| Russell 2000 / ^RUT                 |  34.4600 |           1.2% |                 0.82x |       68.9200 |            2.4% |
| Hang Seng / ^HSI                    | 317.3467 |           1.3% |                 0.78x |      634.6934 |            2.6% |
| UnitedHealth Group Inc. / UNH       |  10.1695 |           2.7% |                 0.47x |       20.3391 |            5.4% |

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

Scoring engine version: **1.0.0** | Git commit: **de970f7**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
