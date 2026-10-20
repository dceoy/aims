+++
title = "Market Analysis 2026-08-07"
date = "2026-08-07T00:00:00+00:00"
draft = false
summary = "Bullish market: 24 reliable instruments. Top signal: MSFT (score 76.7)."
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
source_files = ["data/analysis/2026-08-07.json", "data/history/2026-08-07.json"]
market_regime = "Bullish"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "7d143d4"
+++

## Market Regime

**Bullish** — 17 of 24 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Microsoft Corporation / MSFT** — score 76.7, 20d return +30.0%, RSI14=82. 20d up +30.0%; above MA20 by 19.6%; RSI14=82
- **CAC 40 / ^FCHI** — score 73.9, 20d return +4.5%, RSI14=74. 20d up +4.5%; above MA20 by 3.0%; RSI14=74
- **Euro Stoxx 50 / ^STOXX50E** — score 71.8, 20d return +3.5%, RSI14=73. 20d up +3.5%; above MA20 by 2.9%; RSI14=73
- **DAX / ^GDAXI** — score 70.0, 20d return +4.1%, RSI14=79. 20d up +4.1%; above MA20 by 3.1%; RSI14=79
- **Gold / GC=F** — score 65.2, 20d return +4.6%, RSI14=71. 20d up +4.6%; above MA20 by 6.0%; RSI14=71

## Upcoming Events

_No scheduled events for covered instruments in the next 7 days._

## Signal History

Compared with the previous available report (**2026-08-06**).

- **New top-5:** GC=F, MSFT
- **Persistent top signals:** ^GDAXI (4 reports), ^STOXX50E (3 reports), ^FCHI (2 reports)
- **Dropped from top-5:** JPM, ^DJI
- **BZ=F risk gates:** added malformed_input; removed none
- **JPM risk gates:** added malformed_input; removed none

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +0 |    +3.6 |
| 7203.T    |     +2 |    +9.4 |
| 8306.T    |     +0 |    +1.2 |
| AAPL      |     +1 |    -0.3 |
| AMZN      |     +5 |    +3.9 |
| BZ=F      |     -7 |   +12.7 |
| CL=F      |     +0 |    +9.1 |
| GC=F      |     +4 |    +0.9 |
| GOOGL     |     +1 |    -2.1 |
| HG=F      |     +2 |    -2.4 |
| JPM       |    -24 |   -11.8 |
| META      |     +2 |    +3.6 |
| MSFT      |     +5 |    +7.6 |
| NG=F      |     +1 |   -10.3 |
| NVDA      |     -4 |    -7.3 |
| PL=F      |     +1 |    +2.1 |
| SI=F      |     +2 |    -1.8 |
| TSLA      |     +2 |    -0.6 |
| UNH       |     -2 |   -13.0 |
| XOM       |     +3 |   +12.7 |
| ZC=F      |    +15 |   +35.8 |
| ZS=F      |     +5 |   +14.8 |
| ZW=F      |     -5 |   -20.0 |
| ^DJI      |     -7 |   -15.2 |
| ^FCHI     |     +1 |    +2.1 |
| ^FTSE     |     -2 |    -4.8 |
| ^GDAXI    |     +1 |    +0.6 |
| ^GSPC     |     +1 |    -0.6 |
| ^HSI      |     -4 |   -13.9 |
| ^N225     |     +0 |   -10.9 |
| ^NDX      |     +0 |    -2.1 |
| ^RUT      |     +0 |    -5.2 |
| ^STOXX50E |     +1 |    +2.1 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Copper / HG=F** — malformed_input
- **JPMorgan Chase & Co. / JPM** — malformed_input
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Nikkei 225 / ^N225** — missing_bars
- **Brent Crude Oil / BZ=F** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input

## Key Risks

- **malformed_input** (8 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|    5 | Gold / GC=F            |  65.2 |   Yes    | —               | 20d up +4.6%; above MA20 by 6.0%; RSI14=71    |
|    6 | Corn / ZC=F            |  65.2 |   Yes    | —               | 20d up +8.5%; above MA20 by 3.5%; RSI14=59    |
|   12 | Platinum / PL=F        |  57.0 |   Yes    | —               | 20d up +8.0%; above MA20 by 6.8%; RSI14=67    |
|   13 | Silver / SI=F          |  52.1 |   Yes    | —               | 20d up +3.6%; above MA20 by 6.9%; RSI14=70    |
|   17 | Soybeans / ZS=F        |  42.7 |   Yes    | —               | 20d up +0.4%; below MA20 by 1.2%; RSI14=45    |
|   22 | Wheat / ZW=F           |  23.3 |   Yes    | —               | 20d up +3.1%; below MA20 by 4.5%; RSI14=33    |
|   23 | Natural Gas / NG=F     |  12.1 |   Yes    | —               | 20d down -12.7%; below MA20 by 6.6%; RSI14=29 |
|   25 | Copper / HG=F          |  76.1 |    No    | malformed_input | Suppressed: malformed_input                   |
|   32 | Brent Crude Oil / BZ=F |  28.5 |    No    | malformed_input | Suppressed: malformed_input                   |
|   33 | WTI Crude Oil / CL=F   |  23.6 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                   |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | --------------------------------------------- |
|    1 | Microsoft Corporation / MSFT                                                   |  76.7 |   Yes    | —                             | 20d up +30.0%; above MA20 by 19.6%; RSI14=82  |
|    7 | Amazon.com Inc. / AMZN                                                         |  61.8 |   Yes    | —                             | 20d up +10.2%; above MA20 by 8.8%; RSI14=63   |
|   11 | NVIDIA Corporation / NVDA                                                      |  58.5 |   Yes    | —                             | 20d up +8.0%; above MA20 by 6.2%; RSI14=63    |
|   18 | Alphabet Inc. Class A / GOOGL                                                  |  33.6 |   Yes    | —                             | 20d down -0.3%; above MA20 by 2.5%; RSI14=54  |
|   19 | Apple Inc. / AAPL                                                              |  32.7 |   Yes    | —                             | 20d down -1.2%; below MA20 by 3.4%; RSI14=36  |
|   20 | UnitedHealth Group Inc. / UNH                                                  |  28.8 |   Yes    | —                             | 20d down -6.4%; below MA20 by 4.1%; RSI14=37  |
|   21 | Meta Platforms Inc. / META                                                     |  27.0 |   Yes    | —                             | 20d down -6.6%; below MA20 by 4.3%; RSI14=33  |
|   24 | Tesla Inc. / TSLA                                                              |  12.1 |   Yes    | —                             | 20d down -21.4%; below MA20 by 8.0%; RSI14=28 |
|   26 | JPMorgan Chase & Co. / JPM                                                     |  63.9 |    No    | malformed_input               | Suppressed: malformed_input                   |
|   27 | Exxon Mobil Corporation / XOM                                                  |  59.1 |    No    | malformed_input               | Suppressed: malformed_input                   |
|   28 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  53.9 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars     |
|   29 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  50.0 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars     |
|   30 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  45.1 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars     |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    2 | CAC 40 / ^FCHI                      |  73.9 |   Yes    | —            | 20d up +4.5%; above MA20 by 3.0%; RSI14=74   |
|    3 | Euro Stoxx 50 / ^STOXX50E           |  71.8 |   Yes    | —            | 20d up +3.5%; above MA20 by 2.9%; RSI14=73   |
|    4 | DAX / ^GDAXI                        |  70.0 |   Yes    | —            | 20d up +4.1%; above MA20 by 3.1%; RSI14=79   |
|    8 | Dow Jones Industrial Average / ^DJI |  60.9 |   Yes    | —            | 20d up +2.7%; above MA20 by 2.5%; RSI14=63   |
|    9 | S&P 500 / ^GSPC                     |  60.3 |   Yes    | —            | 20d up +2.2%; above MA20 by 2.6%; RSI14=67   |
|   10 | FTSE 100 / ^FTSE                    |  59.7 |   Yes    | —            | 20d up +3.8%; above MA20 by 1.5%; RSI14=69   |
|   14 | Russell 2000 / ^RUT                 |  49.1 |   Yes    | —            | 20d up +0.3%; above MA20 by 1.2%; RSI14=55   |
|   15 | Hang Seng / ^HSI                    |  46.7 |   Yes    | —            | 20d up +6.2%; above MA20 by 1.4%; RSI14=66   |
|   16 | NASDAQ 100 / ^NDX                   |  43.6 |   Yes    | —            | 20d down -1.2%; above MA20 by 2.0%; RSI14=57 |
|   31 | Nikkei 225 / ^N225                  |  34.9 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-08-06 |
| 7203.T    | 2026-08-06 |
| 8306.T    | 2026-08-06 |
| AAPL      | 2026-08-06 |
| AMZN      | 2026-08-06 |
| BZ=F      | 2026-08-06 |
| CL=F      | 2026-08-06 |
| GC=F      | 2026-08-06 |
| GOOGL     | 2026-08-06 |
| HG=F      | 2026-08-06 |
| JPM       | 2026-08-06 |
| META      | 2026-08-06 |
| MSFT      | 2026-08-06 |
| NG=F      | 2026-08-06 |
| NVDA      | 2026-08-06 |
| PL=F      | 2026-08-06 |
| SI=F      | 2026-08-06 |
| TSLA      | 2026-08-06 |
| UNH       | 2026-08-06 |
| XOM       | 2026-08-06 |
| ZC=F      | 2026-08-06 |
| ZS=F      | 2026-08-06 |
| ZW=F      | 2026-08-06 |
| ^DJI      | 2026-08-06 |
| ^FCHI     | 2026-08-06 |
| ^FTSE     | 2026-08-06 |
| ^GDAXI    | 2026-08-06 |
| ^GSPC     | 2026-08-06 |
| ^HSI      | 2026-08-06 |
| ^N225     | 2026-08-06 |
| ^NDX      | 2026-08-06 |
| ^RUT      | 2026-08-06 |
| ^STOXX50E | 2026-08-06 |

## Symbol Details

### Microsoft Corporation / MSFT (score 76.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.5% |
| ret_5d     | +10.8% |
| ret_20d    | +30.0% |
| ret_60d    | +21.4% |
| ma20_dist  | +19.6% |
| ma50_dist  | +23.3% |
| vol_20d    |  59.6% |
| mdd_60d    |  23.4% |
| rsi_14     |   82.4 |
| zscore_20d |    1.9 |

### CAC 40 / ^FCHI (score 73.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | +2.5% |
| ret_20d    | +4.5% |
| ret_60d    | +7.6% |
| ma20_dist  | +3.0% |
| ma50_dist  | +3.9% |
| vol_20d    |  9.8% |
| mdd_60d    |  3.0% |
| rsi_14     |  74.4 |
| zscore_20d |   2.1 |

### Euro Stoxx 50 / ^STOXX50E (score 71.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.4% |
| ret_5d     |  +2.5% |
| ret_20d    |  +3.5% |
| ret_60d    | +12.0% |
| ma20_dist  |  +2.9% |
| ma50_dist  |  +4.0% |
| vol_20d    |  11.6% |
| mdd_60d    |   3.2% |
| rsi_14     |   72.9 |
| zscore_20d |    2.2 |

### DAX / ^GDAXI (score 70.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | +2.1% |
| ret_20d    | +4.1% |
| ret_60d    | +6.9% |
| ma20_dist  | +3.1% |
| ma50_dist  | +4.1% |
| vol_20d    | 10.8% |
| mdd_60d    |  4.7% |
| rsi_14     |  79.1 |
| zscore_20d |   1.7 |

### Gold / GC=F (score 65.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.7% |
| ret_5d     | +5.4% |
| ret_20d    | +4.6% |
| ret_60d    | -8.5% |
| ma20_dist  | +6.0% |
| ma50_dist  | +3.5% |
| vol_20d    | 24.4% |
| mdd_60d    | 15.2% |
| rsi_14     |  71.2 |
| zscore_20d |   3.1 |

### Corn / ZC=F (score 65.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +6.3% |
| ret_5d     | +4.2% |
| ret_20d    | +8.5% |
| ret_60d    | +0.8% |
| ma20_dist  | +3.5% |
| ma50_dist  | +7.0% |
| vol_20d    | 32.6% |
| mdd_60d    | 15.7% |
| rsi_14     |  59.3 |
| zscore_20d |   1.6 |

### Amazon.com Inc. / AMZN (score 61.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.1% |
| ret_5d     | +15.6% |
| ret_20d    | +10.2% |
| ret_60d    |  +1.2% |
| ma20_dist  |  +8.8% |
| ma50_dist  | +10.0% |
| vol_20d    |  63.2% |
| mdd_60d    |  17.3% |
| rsi_14     |   63.1 |
| zscore_20d |    1.3 |

### Dow Jones Industrial Average / ^DJI (score 60.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.9% |
| ret_5d     | +3.2% |
| ret_20d    | +2.7% |
| ret_60d    | +8.4% |
| ma20_dist  | +2.5% |
| ma50_dist  | +3.6% |
| vol_20d    | 14.2% |
| mdd_60d    |  3.2% |
| rsi_14     |  63.1 |
| zscore_20d |   1.8 |

### S&P 500 / ^GSPC (score 60.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | +3.7% |
| ret_20d    | +2.2% |
| ret_60d    | +4.0% |
| ma20_dist  | +2.6% |
| ma50_dist  | +2.9% |
| vol_20d    | 14.0% |
| mdd_60d    |  4.5% |
| rsi_14     |  66.6 |
| zscore_20d |   1.8 |

### FTSE 100 / ^FTSE (score 59.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | -0.3% |
| ret_20d    | +3.8% |
| ret_60d    | +5.3% |
| ma20_dist  | +1.5% |
| ma50_dist  | +3.0% |
| vol_20d    |  7.7% |
| mdd_60d    |  2.6% |
| rsi_14     |  68.7 |
| zscore_20d |   1.0 |

### NVIDIA Corporation / NVDA (score 58.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.1% |
| ret_5d     | +12.3% |
| ret_20d    |  +8.0% |
| ret_60d    |  -0.2% |
| ma20_dist  |  +6.2% |
| ma50_dist  |  +6.4% |
| vol_20d    |  42.8% |
| mdd_60d    |  19.4% |
| rsi_14     |   63.1 |
| zscore_20d |    1.7 |

### Platinum / PL=F (score 57.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.7% |
| ret_5d     |  +5.9% |
| ret_20d    |  +8.0% |
| ret_60d    | -17.3% |
| ma20_dist  |  +6.8% |
| ma50_dist  |  +3.5% |
| vol_20d    |  36.7% |
| mdd_60d    |  29.1% |
| rsi_14     |   67.1 |
| zscore_20d |    2.3 |

### Silver / SI=F (score 52.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.7% |
| ret_5d     |  +6.4% |
| ret_20d    |  +3.6% |
| ret_60d    | -26.8% |
| ma20_dist  |  +6.9% |
| ma50_dist  |  -0.8% |
| vol_20d    |  36.5% |
| mdd_60d    |  37.1% |
| rsi_14     |   70.2 |
| zscore_20d |    2.4 |

### Russell 2000 / ^RUT (score 49.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | +1.9% |
| ret_20d    | +0.3% |
| ret_60d    | +4.6% |
| ma20_dist  | +1.2% |
| ma50_dist  | +1.6% |
| vol_20d    | 15.0% |
| mdd_60d    |  4.1% |
| rsi_14     |  55.1 |
| zscore_20d |   1.2 |

### Hang Seng / ^HSI (score 46.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.5% |
| ret_5d     | -1.3% |
| ret_20d    | +6.2% |
| ret_60d    | -3.3% |
| ma20_dist  | +1.4% |
| ma50_dist  | +3.7% |
| vol_20d    | 16.9% |
| mdd_60d    | 14.1% |
| rsi_14     |  65.9 |
| zscore_20d |   0.6 |

### NASDAQ 100 / ^NDX (score 43.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | +4.5% |
| ret_20d    | -1.2% |
| ret_60d    | +0.2% |
| ma20_dist  | +2.0% |
| ma50_dist  | -0.0% |
| vol_20d    | 25.2% |
| mdd_60d    | 11.3% |
| rsi_14     |  57.2 |
| zscore_20d |   0.8 |

### Soybeans / ZS=F (score 42.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.8% |
| ret_5d     | +0.6% |
| ret_20d    | +0.4% |
| ret_60d    | -1.3% |
| ma20_dist  | -1.2% |
| ma50_dist  | +1.7% |
| vol_20d    | 21.5% |
| mdd_60d    |  8.8% |
| rsi_14     |  44.7 |
| zscore_20d |  -0.6 |

### Alphabet Inc. Class A / GOOGL (score 33.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.3% |
| ret_5d     | +7.2% |
| ret_20d    | -0.3% |
| ret_60d    | -7.9% |
| ma20_dist  | +2.5% |
| ma50_dist  | +0.2% |
| vol_20d    | 49.8% |
| mdd_60d    | 21.0% |
| rsi_14     |  54.4 |
| zscore_20d |   0.5 |

### Apple Inc. / AAPL (score 32.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | -6.3% |
| ret_20d    | -1.2% |
| ret_60d    | +6.7% |
| ma20_dist  | -3.4% |
| ma50_dist  | +0.9% |
| vol_20d    | 36.5% |
| mdd_60d    | 12.7% |
| rsi_14     |  36.4 |
| zscore_20d |  -1.0 |

### UnitedHealth Group Inc. / UNH (score 28.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.1% |
| ret_5d     | -4.2% |
| ret_20d    | -6.4% |
| ret_60d    | +5.7% |
| ma20_dist  | -4.1% |
| ma50_dist  | -1.9% |
| vol_20d    | 24.9% |
| mdd_60d    |  7.4% |
| rsi_14     |  37.5 |
| zscore_20d |  -2.2 |

### Meta Platforms Inc. / META (score 27.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | +9.4% |
| ret_20d    | -6.6% |
| ret_60d    | -1.4% |
| ma20_dist  | -4.3% |
| ma50_dist  | -1.8% |
| vol_20d    | 49.5% |
| mdd_60d    | 20.9% |
| rsi_14     |  32.7 |
| zscore_20d |  -0.7 |

### Wheat / ZW=F (score 23.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.8% |
| ret_5d     | -5.0% |
| ret_20d    | +3.1% |
| ret_60d    | +1.3% |
| ma20_dist  | -4.5% |
| ma50_dist  | +1.5% |
| vol_20d    | 39.9% |
| mdd_60d    | 14.6% |
| rsi_14     |  33.4 |
| zscore_20d |  -1.3 |

### Natural Gas / NG=F (score 12.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.2% |
| ret_5d     |  -4.7% |
| ret_20d    | -12.7% |
| ret_60d    |  -9.7% |
| ma20_dist  |  -6.6% |
| ma50_dist  | -13.7% |
| vol_20d    |  30.1% |
| mdd_60d    |  21.4% |
| rsi_14     |   29.4 |
| zscore_20d |   -1.9 |

### Tesla Inc. / TSLA (score 12.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.6% |
| ret_5d     |  +3.5% |
| ret_20d    | -21.4% |
| ret_60d    | -28.2% |
| ma20_dist  |  -8.0% |
| ma50_dist  | -16.5% |
| vol_20d    |  58.0% |
| mdd_60d    |  33.0% |
| rsi_14     |   27.8 |
| zscore_20d |   -0.7 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Microsoft Corporation / MSFT        |  18.0039 |           3.6% |                 0.17x |       36.0079 |            7.2% |
| CAC 40 / ^FCHI                      |  94.0872 |           1.1% |                 1.02x |      188.1744 |            2.2% |
| Euro Stoxx 50 / ^STOXX50E           |  73.8858 |           1.1% |                 0.86x |      147.7716 |            2.3% |
| DAX / ^GDAXI                        | 306.7001 |           1.2% |                 0.92x |      613.4001 |            2.3% |
| Gold / GC=F                         |  66.3071 |           1.5% |                 0.41x |      132.6143 |            3.1% |
| Corn / ZC=F                         |  11.6964 |           2.5% |                 0.31x |       23.3929 |            5.0% |
| Amazon.com Inc. / AMZN              |   9.9561 |           3.7% |                 0.16x |       19.9122 |            7.3% |
| Dow Jones Industrial Average / ^DJI | 689.2294 |           1.3% |                 0.70x |     1378.4587 |            2.6% |
| S&P 500 / ^GSPC                     |  94.0836 |           1.2% |                 0.72x |      188.1671 |            2.4% |
| FTSE 100 / ^FTSE                    | 110.8572 |           1.0% |                 1.30x |      221.7144 |            2.0% |
| NVIDIA Corporation / NVDA           |   7.7884 |           3.6% |                 0.23x |       15.5768 |            7.1% |
| Platinum / PL=F                     |  31.6143 |           1.8% |                 0.27x |       63.2286 |            3.6% |
| Silver / SI=F                       |   1.4544 |           2.3% |                 0.27x |        2.9089 |            4.7% |
| Russell 2000 / ^RUT                 |  41.2447 |           1.4% |                 0.67x |       82.4895 |            2.7% |
| Hang Seng / ^HSI                    | 378.7810 |           1.5% |                 0.59x |      757.5619 |            3.0% |
| NASDAQ 100 / ^NDX                   | 620.8408 |           2.1% |                 0.40x |     1241.6816 |            4.2% |
| Soybeans / ZS=F                     |  21.4821 |           1.8% |                 0.46x |       42.9643 |            3.6% |
| Alphabet Inc. Class A / GOOGL       |  13.7847 |           3.9% |                 0.20x |       27.5694 |            7.7% |
| Apple Inc. / AAPL                   |   9.7800 |           3.1% |                 0.27x |       19.5599 |            6.3% |
| UnitedHealth Group Inc. / UNH       |  12.0057 |           3.0% |                 0.40x |       24.0114 |            5.9% |
| Meta Platforms Inc. / META          |  22.5925 |           3.8% |                 0.20x |       45.1850 |            7.7% |
| Wheat / ZW=F                        |  23.0893 |           3.7% |                 0.25x |       46.1786 |            7.3% |
| Natural Gas / NG=F                  |   0.0978 |           3.7% |                 0.33x |        0.1956 |            7.4% |
| Tesla Inc. / TSLA                   |  15.1550 |           4.7% |                 0.17x |       30.3099 |            9.5% |

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

Scoring engine version: **1.0.0** | Git commit: **7d143d4**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
