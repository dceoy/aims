+++
title = "Market Analysis 2026-08-27"
date = "2026-08-27T00:00:00+00:00"
draft = false
summary = "Neutral market: 26 reliable instruments. Top signal: ZC=F (score 82.7)."
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
source_files = ["data/analysis/2026-08-27.json", "data/history/2026-08-27.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "a58f83f"
+++

## Market Regime

**Neutral** — 13 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Corn / ZC=F** — score 82.7, 20d return +14.4%, RSI14=69. 20d up +14.4%; above MA20 by 10.1%; RSI14=69
- **Soybeans / ZS=F** — score 81.8, 20d return +7.3%, RSI14=81. 20d up +7.3%; above MA20 by 5.4%; RSI14=81
- **Wheat / ZW=F** — score 81.2, 20d return +12.2%, RSI14=70. 20d up +12.2%; above MA20 by 9.5%; RSI14=70
- **Gold / GC=F** — score 67.6, 20d return +14.0%, RSI14=67. 20d up +14.0%; above MA20 by 3.7%; RSI14=67
- **DAX / ^GDAXI** — score 62.7, 20d return +3.2%, RSI14=56. 20d up +3.2%; above MA20 by 0.5%; RSI14=56

## Upcoming Events

_No scheduled events for covered instruments in the next 7 days._

## Signal History

Compared with the previous available report (**2026-08-26**).

- **New top-5:** ^GDAXI
- **Persistent top signals:** ZC=F (11 reports), ZW=F (9 reports), GC=F (6 reports), ZS=F (4 reports)
- **Dropped from top-5:** SI=F

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +1 |   +10.3 |
| 7203.T    |     +1 |    +1.5 |
| 8306.T    |     +3 |   +17.6 |
| AAPL      |     +6 |   +12.1 |
| AMZN      |     -3 |    -1.5 |
| BZ=F      |     +3 |   +18.5 |
| CL=F      |     +0 |   +15.5 |
| GC=F      |     -2 |   -12.7 |
| GOOGL     |     -2 |   -12.7 |
| HG=F      |     -4 |   -26.7 |
| JPM       |     +1 |    +1.5 |
| META      |     +2 |    +5.2 |
| MSFT      |     +3 |    +0.9 |
| NG=F      |     -1 |    -1.5 |
| NVDA      |     -7 |   -17.6 |
| PL=F      |     -3 |   -10.0 |
| SI=F      |     -3 |   -13.9 |
| TSLA      |     -4 |    -9.4 |
| UNH       |     +7 |   +14.6 |
| XOM       |     -3 |   -14.8 |
| ZC=F      |     +0 |    +0.3 |
| ZS=F      |     +2 |    +8.8 |
| ZW=F      |     +0 |    +3.3 |
| ^DJI      |     -3 |    -3.9 |
| ^FCHI     |     +1 |    +5.2 |
| ^FTSE     |     +1 |    -1.2 |
| ^GDAXI    |     +2 |    +1.2 |
| ^GSPC     |     -1 |    -3.9 |
| ^HSI      |     +6 |   +11.8 |
| ^N225     |     +2 |    +8.2 |
| ^NDX      |     -5 |    -4.5 |
| ^RUT      |     -2 |    -4.8 |
| ^STOXX50E |     +2 |    +3.0 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Nikkei 225 / ^N225** — missing_bars
- **Copper / HG=F** — malformed_input
- **Exxon Mobil Corporation / XOM** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|    1 | Corn / ZC=F            |  82.7 |   Yes    | —               | 20d up +14.4%; above MA20 by 10.1%; RSI14=69 |
|    2 | Soybeans / ZS=F        |  81.8 |   Yes    | —               | 20d up +7.3%; above MA20 by 5.4%; RSI14=81   |
|    3 | Wheat / ZW=F           |  81.2 |   Yes    | —               | 20d up +12.2%; above MA20 by 9.5%; RSI14=70  |
|    4 | Gold / GC=F            |  67.6 |   Yes    | —               | 20d up +14.0%; above MA20 by 3.7%; RSI14=67  |
|    8 | Silver / SI=F          |  55.1 |   Yes    | —               | 20d up +17.9%; above MA20 by 3.9%; RSI14=62  |
|    9 | Platinum / PL=F        |  53.3 |   Yes    | —               | 20d up +13.5%; above MA20 by 2.8%; RSI14=62  |
|   11 | Natural Gas / NG=F     |  51.2 |   Yes    | —               | 20d up +2.2%; above MA20 by 3.6%; RSI14=54   |
|   23 | Brent Crude Oil / BZ=F |  30.6 |   Yes    | —               | 20d up +4.9%; below MA20 by 0.3%; RSI14=50   |
|   31 | Copper / HG=F          |  43.9 |    No    | malformed_input | Suppressed: malformed_input                  |
|   33 | WTI Crude Oil / CL=F   |  30.9 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    6 | Microsoft Corporation / MSFT                                                   |  60.9 |   Yes    | —                             | 20d up +27.3%; above MA20 by 1.8%; RSI14=48  |
|   12 | JPMorgan Chase & Co. / JPM                                                     |  50.9 |   Yes    | —                             | 20d up +3.4%; below MA20 by 0.3%; RSI14=50   |
|   16 | Apple Inc. / AAPL                                                              |  43.3 |   Yes    | —                             | 20d down -7.2%; above MA20 by 1.1%; RSI14=52 |
|   18 | UnitedHealth Group Inc. / UNH                                                  |  40.9 |   Yes    | —                             | 20d down -4.7%; below MA20 by 0.4%; RSI14=48 |
|   20 | Tesla Inc. / TSLA                                                              |  37.9 |   Yes    | —                             | 20d up +15.9%; above MA20 by 3.3%; RSI14=64  |
|   21 | Meta Platforms Inc. / META                                                     |  35.8 |   Yes    | —                             | 20d down -1.6%; above MA20 by 0.5%; RSI14=45 |
|   24 | Amazon.com Inc. / AMZN                                                         |  30.0 |   Yes    | —                             | 20d up +14.8%; below MA20 by 2.2%; RSI14=36  |
|   25 | NVIDIA Corporation / NVDA                                                      |  21.8 |   Yes    | —                             | 20d up +10.3%; below MA20 by 2.7%; RSI14=39  |
|   26 | Alphabet Inc. Class A / GOOGL                                                  |  13.6 |   Yes    | —                             | 20d up +1.6%; below MA20 by 2.4%; RSI14=32   |
|   27 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  70.6 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   28 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  57.0 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   29 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  56.1 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   32 | Exxon Mobil Corporation / XOM                                                  |  41.8 |    No    | malformed_input               | Suppressed: malformed_input                  |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    5 | DAX / ^GDAXI                        |  62.7 |   Yes    | —            | 20d up +3.2%; above MA20 by 0.5%; RSI14=56   |
|    7 | FTSE 100 / ^FTSE                    |  59.1 |   Yes    | —            | 20d down -0.3%; above MA20 by 0.4%; RSI14=51 |
|   10 | Euro Stoxx 50 / ^STOXX50E           |  53.0 |   Yes    | —            | 20d up +3.6%; below MA20 by 0.1%; RSI14=44   |
|   13 | Hang Seng / ^HSI                    |  49.4 |   Yes    | —            | 20d down -0.6%; below MA20 by 0.0%; RSI14=52 |
|   14 | Dow Jones Industrial Average / ^DJI |  48.5 |   Yes    | —            | 20d up +3.6%; below MA20 by 0.1%; RSI14=42   |
|   15 | S&P 500 / ^GSPC                     |  45.1 |   Yes    | —            | 20d up +4.9%; below MA20 by 0.1%; RSI14=46   |
|   17 | Russell 2000 / ^RUT                 |  43.3 |   Yes    | —            | 20d up +3.4%; below MA20 by 0.3%; RSI14=51   |
|   19 | CAC 40 / ^FCHI                      |  38.2 |   Yes    | —            | 20d up +0.6%; below MA20 by 1.4%; RSI14=20   |
|   22 | NASDAQ 100 / ^NDX                   |  35.1 |   Yes    | —            | 20d up +7.5%; below MA20 by 0.5%; RSI14=47   |
|   30 | Nikkei 225 / ^N225                  |  46.4 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-08-26 |
| 7203.T    | 2026-08-26 |
| 8306.T    | 2026-08-26 |
| AAPL      | 2026-08-26 |
| AMZN      | 2026-08-26 |
| BZ=F      | 2026-08-26 |
| CL=F      | 2026-08-26 |
| GC=F      | 2026-08-26 |
| GOOGL     | 2026-08-26 |
| HG=F      | 2026-08-26 |
| JPM       | 2026-08-26 |
| META      | 2026-08-26 |
| MSFT      | 2026-08-26 |
| NG=F      | 2026-08-26 |
| NVDA      | 2026-08-26 |
| PL=F      | 2026-08-26 |
| SI=F      | 2026-08-26 |
| TSLA      | 2026-08-26 |
| UNH       | 2026-08-26 |
| XOM       | 2026-08-26 |
| ZC=F      | 2026-08-26 |
| ZS=F      | 2026-08-26 |
| ZW=F      | 2026-08-26 |
| ^DJI      | 2026-08-26 |
| ^FCHI     | 2026-08-26 |
| ^FTSE     | 2026-08-26 |
| ^GDAXI    | 2026-08-26 |
| ^GSPC     | 2026-08-26 |
| ^HSI      | 2026-08-26 |
| ^N225     | 2026-08-26 |
| ^NDX      | 2026-08-26 |
| ^RUT      | 2026-08-26 |
| ^STOXX50E | 2026-08-26 |

## Symbol Details

### Corn / ZC=F (score 82.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.7% |
| ret_5d     |  +7.4% |
| ret_20d    | +14.4% |
| ret_60d    | +21.1% |
| ma20_dist  | +10.1% |
| ma50_dist  | +14.6% |
| vol_20d    |  55.7% |
| mdd_60d    |   6.0% |
| rsi_14     |   69.1 |
| zscore_20d |    1.9 |

### Soybeans / ZS=F (score 81.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.1% |
| ret_5d     |  +2.7% |
| ret_20d    |  +7.3% |
| ret_60d    | +11.0% |
| ma20_dist  |  +5.4% |
| ma50_dist  |  +6.1% |
| vol_20d    |  18.2% |
| mdd_60d    |   8.1% |
| rsi_14     |   80.6 |
| zscore_20d |    2.0 |

### Wheat / ZW=F (score 81.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +6.6% |
| ret_5d     |  +7.0% |
| ret_20d    | +12.2% |
| ret_60d    | +25.6% |
| ma20_dist  |  +9.5% |
| ma50_dist  | +13.0% |
| vol_20d    |  41.5% |
| mdd_60d    |  10.7% |
| rsi_14     |   69.7 |
| zscore_20d |    2.4 |

### Gold / GC=F (score 67.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.9% |
| ret_5d     |  +1.8% |
| ret_20d    | +14.0% |
| ret_60d    |  +2.7% |
| ma20_dist  |  +3.7% |
| ma50_dist  |  +9.1% |
| vol_20d    |  22.3% |
| mdd_60d    |   8.6% |
| rsi_14     |   66.6 |
| zscore_20d |    1.1 |

### DAX / ^GDAXI (score 62.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | +0.7% |
| ret_20d    | +3.2% |
| ret_60d    | +6.0% |
| ma20_dist  | +0.5% |
| ma50_dist  | +3.0% |
| vol_20d    |  8.1% |
| mdd_60d    |  4.1% |
| rsi_14     |  55.6 |
| zscore_20d |   0.6 |

### Microsoft Corporation / MSFT (score 60.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.9% |
| ret_5d     |  +2.7% |
| ret_20d    | +27.3% |
| ret_60d    |  +7.8% |
| ma20_dist  |  +1.8% |
| ma50_dist  | +16.7% |
| vol_20d    |  58.3% |
| mdd_60d    |  20.0% |
| rsi_14     |   47.9 |
| zscore_20d |    0.7 |

### FTSE 100 / ^FTSE (score 59.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | +1.3% |
| ret_20d    | -0.3% |
| ret_60d    | +5.3% |
| ma20_dist  | +0.4% |
| ma50_dist  | +1.9% |
| vol_20d    |  4.4% |
| mdd_60d    |  1.9% |
| rsi_14     |  51.3 |
| zscore_20d |   0.8 |

### Silver / SI=F (score 55.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.9% |
| ret_5d     |  -0.1% |
| ret_20d    | +17.9% |
| ret_60d    |  -7.8% |
| ma20_dist  |  +3.9% |
| ma50_dist  | +10.5% |
| vol_20d    |  30.4% |
| mdd_60d    |  20.9% |
| rsi_14     |   61.6 |
| zscore_20d |    1.0 |

### Platinum / PL=F (score 53.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.9% |
| ret_5d     |  +0.3% |
| ret_20d    | +13.5% |
| ret_60d    |  -3.1% |
| ma20_dist  |  +2.8% |
| ma50_dist  |  +9.0% |
| vol_20d    |  37.4% |
| mdd_60d    |  14.5% |
| rsi_14     |   61.7 |
| zscore_20d |    0.9 |

### Euro Stoxx 50 / ^STOXX50E (score 53.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | +0.4% |
| ret_20d    | +3.6% |
| ret_60d    | +6.9% |
| ma20_dist  | -0.1% |
| ma50_dist  | +1.8% |
| vol_20d    |  8.7% |
| mdd_60d    |  3.2% |
| rsi_14     |  44.3 |
| zscore_20d |  -0.1 |

### Natural Gas / NG=F (score 51.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.6% |
| ret_5d     |  +4.0% |
| ret_20d    |  +2.2% |
| ret_60d    | -14.8% |
| ma20_dist  |  +3.6% |
| ma50_dist  |  -2.0% |
| vol_20d    |  30.8% |
| mdd_60d    |  21.0% |
| rsi_14     |   54.1 |
| zscore_20d |    1.8 |

### JPMorgan Chase & Co. / JPM (score 50.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.1% |
| ret_5d     |  -0.2% |
| ret_20d    |  +3.4% |
| ret_60d    | +20.7% |
| ma20_dist  |  -0.3% |
| ma50_dist  |  +3.1% |
| vol_20d    |  13.9% |
| mdd_60d    |   3.7% |
| rsi_14     |   50.3 |
| zscore_20d |   -0.3 |

### Hang Seng / ^HSI (score 49.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | +0.6% |
| ret_20d    | -0.6% |
| ret_60d    | +1.0% |
| ma20_dist  | -0.0% |
| ma50_dist  | +3.6% |
| vol_20d    | 13.9% |
| mdd_60d    | 12.9% |
| rsi_14     |  52.2 |
| zscore_20d |  -0.0 |

### Dow Jones Industrial Average / ^DJI (score 48.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | +0.0% |
| ret_20d    | +3.6% |
| ret_60d    | +4.7% |
| ma20_dist  | -0.1% |
| ma50_dist  | +1.4% |
| vol_20d    | 11.3% |
| mdd_60d    |  3.2% |
| rsi_14     |  42.3 |
| zscore_20d |  -0.1 |

### S&P 500 / ^GSPC (score 45.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.0% |
| ret_5d     | -0.4% |
| ret_20d    | +4.9% |
| ret_60d    | +1.0% |
| ma20_dist  | -0.1% |
| ma50_dist  | +1.6% |
| vol_20d    | 11.5% |
| mdd_60d    |  4.5% |
| rsi_14     |  45.9 |
| zscore_20d |  -0.1 |

### Apple Inc. / AAPL (score 43.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | -1.1% |
| ret_20d    | -7.2% |
| ret_60d    | +2.3% |
| ma20_dist  | +1.1% |
| ma50_dist  | +0.8% |
| vol_20d    | 31.4% |
| mdd_60d    | 12.7% |
| rsi_14     |  51.7 |
| zscore_20d |   0.5 |

### Russell 2000 / ^RUT (score 43.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | -0.9% |
| ret_20d    | +3.4% |
| ret_60d    | +3.4% |
| ma20_dist  | -0.3% |
| ma50_dist  | +0.5% |
| vol_20d    | 14.3% |
| mdd_60d    |  3.9% |
| rsi_14     |  50.8 |
| zscore_20d |  -0.3 |

### UnitedHealth Group Inc. / UNH (score 40.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | +3.2% |
| ret_20d    | -4.7% |
| ret_60d    | +6.2% |
| ma20_dist  | -0.4% |
| ma50_dist  | -3.0% |
| vol_20d    | 20.1% |
| mdd_60d    | 11.8% |
| rsi_14     |  47.6 |
| zscore_20d |  -0.2 |

### CAC 40 / ^FCHI (score 38.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | -0.5% |
| ret_20d    | +0.6% |
| ret_60d    | +3.8% |
| ma20_dist  | -1.4% |
| ma50_dist  | -0.0% |
| vol_20d    |  8.0% |
| mdd_60d    |  3.3% |
| rsi_14     |  20.3 |
| zscore_20d |  -1.2 |

### Tesla Inc. / TSLA (score 37.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.3% |
| ret_5d     |  -1.5% |
| ret_20d    | +15.9% |
| ret_60d    | -16.8% |
| ma20_dist  |  +3.3% |
| ma50_dist  |  -4.6% |
| vol_20d    |  37.4% |
| mdd_60d    |  29.9% |
| rsi_14     |   63.6 |
| zscore_20d |    0.8 |

### Meta Platforms Inc. / META (score 35.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | +5.5% |
| ret_20d    | -1.6% |
| ret_60d    | -4.0% |
| ma20_dist  | +0.5% |
| ma50_dist  | -2.8% |
| vol_20d    | 46.6% |
| mdd_60d    | 20.9% |
| rsi_14     |  44.7 |
| zscore_20d |   0.2 |

### NASDAQ 100 / ^NDX (score 35.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | -0.7% |
| ret_20d    | +7.5% |
| ret_60d    | -4.2% |
| ma20_dist  | -0.5% |
| ma50_dist  | -0.2% |
| vol_20d    | 20.2% |
| mdd_60d    | 11.3% |
| rsi_14     |  47.1 |
| zscore_20d |  -0.3 |

### Brent Crude Oil / BZ=F (score 30.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | -6.3% |
| ret_20d    | +4.9% |
| ret_60d    | -7.6% |
| ma20_dist  | -0.3% |
| ma50_dist  | +3.9% |
| vol_20d    | 35.4% |
| mdd_60d    | 24.1% |
| rsi_14     |  50.4 |
| zscore_20d |  -0.1 |

### Amazon.com Inc. / AMZN (score 30.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.3% |
| ret_5d     |  -2.1% |
| ret_20d    | +14.8% |
| ret_60d    |  -0.4% |
| ma20_dist  |  -2.2% |
| ma50_dist  |  +3.7% |
| vol_20d    |  60.8% |
| mdd_60d    |  11.6% |
| rsi_14     |   36.2 |
| zscore_20d |   -0.6 |

### NVIDIA Corporation / NVDA (score 21.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.6% |
| ret_5d     |  -3.6% |
| ret_20d    | +10.3% |
| ret_60d    |  -6.6% |
| ma20_dist  |  -2.7% |
| ma50_dist  |  +0.9% |
| vol_20d    |  32.4% |
| mdd_60d    |  14.7% |
| rsi_14     |   39.4 |
| zscore_20d |   -0.7 |

### Alphabet Inc. Class A / GOOGL (score 13.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.4% |
| ret_5d     | -0.8% |
| ret_20d    | +1.6% |
| ret_60d    | -9.1% |
| ma20_dist  | -2.4% |
| ma50_dist  | -2.5% |
| vol_20d    | 37.6% |
| mdd_60d    | 14.9% |
| rsi_14     |  32.1 |
| zscore_20d |  -0.8 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Corn / ZC=F                         |  17.5536 |           3.4% |                 0.18x |       35.1071 |            6.8% |
| Soybeans / ZS=F                     |  18.5893 |           1.5% |                 0.55x |       37.1786 |            3.0% |
| Wheat / ZW=F                        |  24.6607 |           3.4% |                 0.24x |       49.3214 |            6.8% |
| Gold / GC=F                         |  78.1357 |           1.7% |                 0.45x |      156.2715 |            3.4% |
| DAX / ^GDAXI                        | 208.6113 |           0.8% |                 1.23x |      417.2227 |            1.6% |
| Microsoft Corporation / MSFT        |   9.0960 |           1.8% |                 0.17x |       18.1921 |            3.7% |
| FTSE 100 / ^FTSE                    |  74.6715 |           0.7% |                 2.30x |      149.3429 |            1.4% |
| Silver / SI=F                       |   1.5410 |           2.3% |                 0.33x |        3.0820 |            4.5% |
| Platinum / PL=F                     |  30.2357 |           1.6% |                 0.27x |       60.4714 |            3.3% |
| Euro Stoxx 50 / ^STOXX50E           |  44.7849 |           0.7% |                 1.15x |       89.5699 |            1.4% |
| Natural Gas / NG=F                  |   0.0898 |           3.2% |                 0.32x |        0.1796 |            6.3% |
| JPMorgan Chase & Co. / JPM          |   5.1486 |           1.4% |                 0.72x |       10.2971 |            2.9% |
| Hang Seng / ^HSI                    | 329.1023 |           1.3% |                 0.72x |      658.2045 |            2.6% |
| Dow Jones Industrial Average / ^DJI | 349.5502 |           0.7% |                 0.88x |      699.1004 |            1.3% |
| S&P 500 / ^GSPC                     |  46.9836 |           0.6% |                 0.87x |       93.9671 |            1.2% |
| Apple Inc. / AAPL                   |   5.9462 |           1.9% |                 0.32x |       11.8924 |            3.8% |
| Russell 2000 / ^RUT                 |  25.6000 |           0.9% |                 0.70x |       51.2001 |            1.7% |
| UnitedHealth Group Inc. / UNH       |   8.1757 |           2.0% |                 0.50x |       16.3514 |            4.1% |
| CAC 40 / ^FCHI                      |  56.1570 |           0.7% |                 1.25x |      112.3140 |            1.3% |
| Tesla Inc. / TSLA                   |  12.1586 |           3.5% |                 0.27x |       24.3171 |            7.0% |
| Meta Platforms Inc. / META          |  17.9943 |           3.1% |                 0.21x |       35.9886 |            6.2% |
| NASDAQ 100 / ^NDX                   | 323.7909 |           1.1% |                 0.50x |      647.5818 |            2.2% |
| Brent Crude Oil / BZ=F              |   2.8150 |           3.2% |                 0.28x |        5.6300 |            6.4% |
| Amazon.com Inc. / AMZN              |   5.5214 |           2.1% |                 0.16x |       11.0429 |            4.2% |
| NVIDIA Corporation / NVDA           |   5.4386 |           2.6% |                 0.31x |       10.8771 |            5.2% |
| Alphabet Inc. Class A / GOOGL       |   6.3257 |           1.8% |                 0.27x |       12.6514 |            3.7% |

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

Scoring engine version: **1.0.0** | Git commit: **a58f83f**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
