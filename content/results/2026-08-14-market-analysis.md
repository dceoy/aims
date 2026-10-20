+++
title = "Market Analysis 2026-08-14"
date = "2026-08-14T00:00:00+00:00"
draft = false
summary = "Bullish market: 26 reliable instruments. Top signal: ^GSPC (score 70.0)."
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
source_files = ["data/analysis/2026-08-14.json", "data/history/2026-08-14.json"]
market_regime = "Bullish"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "959fcb2"
+++

## Market Regime

**Bullish** — 17 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **S&P 500 / ^GSPC** — score 70.0, 20d return +3.5%, RSI14=77. 20d up +3.5%; above MA20 by 3.0%; RSI14=77
- **Euro Stoxx 50 / ^STOXX50E** — score 69.7, 20d return +4.2%, RSI14=83. 20d up +4.2%; above MA20 by 2.5%; RSI14=83
- **Corn / ZC=F** — score 69.4, 20d return +6.5%, RSI14=58. 20d up +6.5%; above MA20 by 5.1%; RSI14=58
- **JPMorgan Chase & Co. / JPM** — score 68.5, 20d return +5.8%, RSI14=61. 20d up +5.8%; above MA20 by 2.7%; RSI14=61
- **DAX / ^GDAXI** — score 67.3, 20d return +5.6%, RSI14=89. 20d up +5.6%; above MA20 by 2.5%; RSI14=89

## Upcoming Events

_No scheduled events for covered instruments in the next 7 days._

## Signal History

Compared with the previous available report (**2026-08-13**).

- **New top-5:** ^GDAXI, ^GSPC
- **Persistent top signals:** ^STOXX50E (10 reports), JPM (4 reports), ZC=F (2 reports)
- **Dropped from top-5:** GC=F, SI=F

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     -2 |   -10.0 |
| 7203.T    |     -1 |    -7.0 |
| 8306.T    |     +2 |   +11.5 |
| AAPL      |     +2 |    +7.6 |
| AMZN      |     +0 |    +0.6 |
| BZ=F      |     -3 |    -7.9 |
| CL=F      |     +0 |    -7.6 |
| GC=F      |     -8 |   -13.3 |
| GOOGL     |     +0 |    +5.5 |
| HG=F      |     +2 |    +3.3 |
| JPM       |     -3 |    -7.3 |
| META      |     +5 |   +15.2 |
| MSFT      |     +0 |    +4.8 |
| NG=F      |     -6 |   -12.4 |
| NVDA      |     +1 |    +2.4 |
| PL=F      |     -8 |   -20.9 |
| SI=F      |    -10 |   -16.7 |
| TSLA      |     +6 |   +21.8 |
| UNH       |     -3 |    -7.9 |
| XOM       |     -3 |   -10.3 |
| ZC=F      |     +0 |    +0.9 |
| ZS=F      |     +1 |    +3.0 |
| ZW=F      |     +4 |   +13.3 |
| ^DJI      |     +1 |    +2.7 |
| ^FCHI     |     -1 |    -1.2 |
| ^FTSE     |     -1 |   -11.2 |
| ^GDAXI    |     +1 |    +0.9 |
| ^GSPC     |    +10 |   +10.0 |
| ^HSI      |     +1 |    +2.4 |
| ^N225     |     +2 |    +4.8 |
| ^NDX      |     +8 |   +15.2 |
| ^RUT      |     +0 |    +5.2 |
| ^STOXX50E |     +3 |    +2.4 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Nikkei 225 / ^N225** — missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **WTI Crude Oil / CL=F** — malformed_input

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|    3 | Corn / ZC=F            |  69.4 |   Yes    | —               | 20d up +6.5%; above MA20 by 5.1%; RSI14=58   |
|   10 | Gold / GC=F            |  61.5 |   Yes    | —               | 20d up +9.0%; above MA20 by 4.8%; RSI14=74   |
|   13 | Wheat / ZW=F           |  53.0 |   Yes    | —               | 20d down -1.6%; above MA20 by 2.0%; RSI14=54 |
|   14 | Silver / SI=F          |  50.6 |   Yes    | —               | 20d up +14.4%; above MA20 by 6.0%; RSI14=68  |
|   17 | Soybeans / ZS=F        |  41.8 |   Yes    | —               | 20d down -1.5%; below MA20 by 0.0%; RSI14=43 |
|   20 | Platinum / PL=F        |  34.5 |   Yes    | —               | 20d up +6.9%; above MA20 by 2.5%; RSI14=63   |
|   25 | Brent Crude Oil / BZ=F |  23.6 |   Yes    | —               | 20d down -1.1%; below MA20 by 1.0%; RSI14=48 |
|   26 | Natural Gas / NG=F     |  21.8 |   Yes    | —               | 20d down -5.8%; below MA20 by 1.0%; RSI14=48 |
|   30 | Copper / HG=F          |  52.7 |    No    | malformed_input | Suppressed: malformed_input                  |
|   33 | WTI Crude Oil / CL=F   |  18.8 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                   |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | --------------------------------------------- |
|    4 | JPMorgan Chase & Co. / JPM                                                     |  68.5 |   Yes    | —                             | 20d up +5.8%; above MA20 by 2.7%; RSI14=61    |
|    6 | NVIDIA Corporation / NVDA                                                      |  66.1 |   Yes    | —                             | 20d up +8.6%; above MA20 by 7.7%; RSI14=64    |
|    9 | Microsoft Corporation / MSFT                                                   |  64.8 |   Yes    | —                             | 20d up +23.9%; above MA20 by 11.6%; RSI14=86  |
|   16 | Amazon.com Inc. / AMZN                                                         |  43.3 |   Yes    | —                             | 20d up +6.1%; above MA20 by 3.7%; RSI14=68    |
|   19 | Tesla Inc. / TSLA                                                              |  37.0 |   Yes    | —                             | 20d down -13.1%; above MA20 by 2.7%; RSI14=66 |
|   21 | Meta Platforms Inc. / META                                                     |  27.0 |   Yes    | —                             | 20d down -10.5%; below MA20 by 0.4%; RSI14=50 |
|   22 | Apple Inc. / AAPL                                                              |  26.1 |   Yes    | —                             | 20d down -8.3%; below MA20 by 4.5%; RSI14=30  |
|   23 | Alphabet Inc. Class A / GOOGL                                                  |  25.1 |   Yes    | —                             | 20d down -2.3%; below MA20 by 0.0%; RSI14=62  |
|   24 | UnitedHealth Group Inc. / UNH                                                  |  24.2 |   Yes    | —                             | 20d down -5.7%; below MA20 by 4.1%; RSI14=35  |
|   27 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  63.6 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars     |
|   29 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  55.8 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars     |
|   31 | Exxon Mobil Corporation / XOM                                                  |  52.1 |    No    | malformed_input               | Suppressed: malformed_input                   |
|   32 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  44.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars     |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                |
| ---: | ----------------------------------- | ----: | :------: | ------------ | ------------------------------------------ |
|    1 | S&P 500 / ^GSPC                     |  70.0 |   Yes    | —            | 20d up +3.5%; above MA20 by 3.0%; RSI14=77 |
|    2 | Euro Stoxx 50 / ^STOXX50E           |  69.7 |   Yes    | —            | 20d up +4.2%; above MA20 by 2.5%; RSI14=83 |
|    5 | DAX / ^GDAXI                        |  67.3 |   Yes    | —            | 20d up +5.6%; above MA20 by 2.5%; RSI14=89 |
|    7 | NASDAQ 100 / ^NDX                   |  66.1 |   Yes    | —            | 20d up +3.6%; above MA20 by 4.2%; RSI14=70 |
|    8 | Russell 2000 / ^RUT                 |  65.5 |   Yes    | —            | 20d up +2.6%; above MA20 by 2.4%; RSI14=67 |
|   11 | CAC 40 / ^FCHI                      |  58.8 |   Yes    | —            | 20d up +3.3%; above MA20 by 1.4%; RSI14=76 |
|   12 | Dow Jones Industrial Average / ^DJI |  57.9 |   Yes    | —            | 20d up +2.4%; above MA20 by 1.8%; RSI14=67 |
|   15 | FTSE 100 / ^FTSE                    |  43.6 |   Yes    | —            | 20d up +1.9%; below MA20 by 0.2%; RSI14=54 |
|   18 | Hang Seng / ^HSI                    |  38.5 |   Yes    | —            | 20d up +1.6%; below MA20 by 0.3%; RSI14=58 |
|   28 | Nikkei 225 / ^N225                  |  57.0 |    No    | missing_bars | Suppressed: missing_bars                   |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-08-13 |
| 7203.T    | 2026-08-13 |
| 8306.T    | 2026-08-13 |
| AAPL      | 2026-08-13 |
| AMZN      | 2026-08-13 |
| BZ=F      | 2026-08-13 |
| CL=F      | 2026-08-13 |
| GC=F      | 2026-08-13 |
| GOOGL     | 2026-08-13 |
| HG=F      | 2026-08-13 |
| JPM       | 2026-08-13 |
| META      | 2026-08-13 |
| MSFT      | 2026-08-13 |
| NG=F      | 2026-08-13 |
| NVDA      | 2026-08-13 |
| PL=F      | 2026-08-13 |
| SI=F      | 2026-08-13 |
| TSLA      | 2026-08-13 |
| UNH       | 2026-08-13 |
| XOM       | 2026-08-13 |
| ZC=F      | 2026-08-13 |
| ZS=F      | 2026-08-13 |
| ZW=F      | 2026-08-13 |
| ^DJI      | 2026-08-13 |
| ^FCHI     | 2026-08-13 |
| ^FTSE     | 2026-08-13 |
| ^GDAXI    | 2026-08-13 |
| ^GSPC     | 2026-08-13 |
| ^HSI      | 2026-08-13 |
| ^N225     | 2026-08-13 |
| ^NDX      | 2026-08-13 |
| ^RUT      | 2026-08-13 |
| ^STOXX50E | 2026-08-13 |

## Symbol Details

### S&P 500 / ^GSPC (score 70.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | +1.2% |
| ret_20d    | +3.5% |
| ret_60d    | +5.3% |
| ma20_dist  | +3.0% |
| ma50_dist  | +3.9% |
| vol_20d    | 13.6% |
| mdd_60d    |  4.5% |
| rsi_14     |  76.7 |
| zscore_20d |   1.5 |

### Euro Stoxx 50 / ^STOXX50E (score 69.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | +0.7% |
| ret_20d    | +4.2% |
| ret_60d    | +9.5% |
| ma20_dist  | +2.5% |
| ma50_dist  | +3.9% |
| vol_20d    | 11.5% |
| mdd_60d    |  3.2% |
| rsi_14     |  83.1 |
| zscore_20d |   1.3 |

### Corn / ZC=F (score 69.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +3.7% |
| ret_5d     | +7.9% |
| ret_20d    | +6.5% |
| ret_60d    | -0.3% |
| ma20_dist  | +5.1% |
| ma50_dist  | +9.1% |
| vol_20d    | 40.1% |
| mdd_60d    | 13.7% |
| rsi_14     |  58.0 |
| zscore_20d |   2.1 |

### JPMorgan Chase & Co. / JPM (score 68.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.6% |
| ret_5d     |  +1.9% |
| ret_20d    |  +5.8% |
| ret_60d    | +21.3% |
| ma20_dist  |  +2.7% |
| ma50_dist  |  +7.6% |
| vol_20d    |  18.1% |
| mdd_60d    |   3.5% |
| rsi_14     |   61.0 |
| zscore_20d |    1.4 |

### DAX / ^GDAXI (score 67.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | +0.6% |
| ret_20d    | +5.6% |
| ret_60d    | +6.9% |
| ma20_dist  | +2.5% |
| ma50_dist  | +4.2% |
| vol_20d    | 10.5% |
| mdd_60d    |  4.7% |
| rsi_14     |  88.9 |
| zscore_20d |   1.1 |

### NVIDIA Corporation / NVDA (score 66.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | +2.9% |
| ret_20d    | +8.6% |
| ret_60d    | +1.3% |
| ma20_dist  | +7.7% |
| ma50_dist  | +9.2% |
| vol_20d    | 38.3% |
| mdd_60d    | 15.3% |
| rsi_14     |  63.9 |
| zscore_20d |   1.6 |

### NASDAQ 100 / ^NDX (score 66.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | +2.4% |
| ret_20d    | +3.6% |
| ret_60d    | +3.8% |
| ma20_dist  | +4.2% |
| ma50_dist  | +2.6% |
| vol_20d    | 24.0% |
| mdd_60d    | 11.3% |
| rsi_14     |  69.8 |
| zscore_20d |   1.6 |

### Russell 2000 / ^RUT (score 65.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.2% |
| ret_5d     |  +1.7% |
| ret_20d    |  +2.6% |
| ret_60d    | +10.0% |
| ma20_dist  |  +2.4% |
| ma50_dist  |  +2.9% |
| vol_20d    |  15.2% |
| mdd_60d    |   3.9% |
| rsi_14     |   67.4 |
| zscore_20d |    1.6 |

### Microsoft Corporation / MSFT (score 64.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.9% |
| ret_5d     |  -0.6% |
| ret_20d    | +23.9% |
| ret_60d    | +17.6% |
| ma20_dist  | +11.6% |
| ma50_dist  | +20.8% |
| vol_20d    |  60.2% |
| mdd_60d    |  23.4% |
| rsi_14     |   86.3 |
| zscore_20d |    1.0 |

### Gold / GC=F (score 61.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | +0.8% |
| ret_20d    | +9.0% |
| ret_60d    | -2.9% |
| ma20_dist  | +4.8% |
| ma50_dist  | +5.2% |
| vol_20d    | 21.5% |
| mdd_60d    | 12.6% |
| rsi_14     |  74.2 |
| zscore_20d |   1.4 |

### CAC 40 / ^FCHI (score 58.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | -0.6% |
| ret_20d    | +3.3% |
| ret_60d    | +7.0% |
| ma20_dist  | +1.4% |
| ma50_dist  | +2.6% |
| vol_20d    | 10.2% |
| mdd_60d    |  3.0% |
| rsi_14     |  76.2 |
| zscore_20d |   0.8 |

### Dow Jones Industrial Average / ^DJI (score 57.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | -0.1% |
| ret_20d    | +2.4% |
| ret_60d    | +8.4% |
| ma20_dist  | +1.8% |
| ma50_dist  | +3.0% |
| vol_20d    | 14.2% |
| mdd_60d    |  3.2% |
| rsi_14     |  66.7 |
| zscore_20d |   1.0 |

### Wheat / ZW=F (score 53.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.9% |
| ret_5d     | +5.0% |
| ret_20d    | -1.6% |
| ret_60d    | +0.6% |
| ma20_dist  | +2.0% |
| ma50_dist  | +7.3% |
| vol_20d    | 33.5% |
| mdd_60d    | 13.8% |
| rsi_14     |  53.8 |
| zscore_20d |   0.6 |

### Silver / SI=F (score 50.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.2% |
| ret_5d     |  +1.2% |
| ret_20d    | +14.4% |
| ret_60d    | -14.3% |
| ma20_dist  |  +6.0% |
| ma50_dist  |  +3.8% |
| vol_20d    |  33.5% |
| mdd_60d    |  26.8% |
| rsi_14     |   68.4 |
| zscore_20d |    1.3 |

### FTSE 100 / ^FTSE (score 43.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | -0.9% |
| ret_20d    | +1.9% |
| ret_60d    | +3.3% |
| ma20_dist  | -0.2% |
| ma50_dist  | +1.6% |
| vol_20d    |  8.2% |
| mdd_60d    |  2.6% |
| rsi_14     |  54.2 |
| zscore_20d |  -0.2 |

### Amazon.com Inc. / AMZN (score 43.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | -2.6% |
| ret_20d    | +6.1% |
| ret_60d    | +0.1% |
| ma20_dist  | +3.7% |
| ma50_dist  | +6.9% |
| vol_20d    | 63.2% |
| mdd_60d    | 17.3% |
| rsi_14     |  67.7 |
| zscore_20d |   0.5 |

### Soybeans / ZS=F (score 41.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.9% |
| ret_5d     | +2.6% |
| ret_20d    | -1.5% |
| ret_60d    | -1.9% |
| ma20_dist  | -0.0% |
| ma50_dist  | +2.1% |
| vol_20d    | 22.7% |
| mdd_60d    |  8.1% |
| rsi_14     |  43.5 |
| zscore_20d |  -0.0 |

### Hang Seng / ^HSI (score 38.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | -0.5% |
| ret_20d    | +1.6% |
| ret_60d    | -1.1% |
| ma20_dist  | -0.3% |
| ma50_dist  | +3.1% |
| vol_20d    | 17.2% |
| mdd_60d    | 12.9% |
| rsi_14     |  58.3 |
| zscore_20d |  -0.2 |

### Tesla Inc. / TSLA (score 37.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +3.8% |
| ret_5d     |  +6.4% |
| ret_20d    | -13.1% |
| ret_60d    | -17.1% |
| ma20_dist  |  +2.7% |
| ma50_dist  |  -8.8% |
| vol_20d    |  61.4% |
| mdd_60d    |  32.5% |
| rsi_14     |   66.3 |
| zscore_20d |    0.4 |

### Platinum / PL=F (score 34.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.6% |
| ret_5d     |  -1.9% |
| ret_20d    |  +6.9% |
| ret_60d    | -11.3% |
| ma20_dist  |  +2.5% |
| ma50_dist  |  +2.8% |
| vol_20d    |  37.1% |
| mdd_60d    |  20.7% |
| rsi_14     |   62.6 |
| zscore_20d |    0.6 |

### Meta Platforms Inc. / META (score 27.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.8% |
| ret_5d     |  +0.9% |
| ret_20d    | -10.5% |
| ret_60d    |  -2.6% |
| ma20_dist  |  -0.4% |
| ma50_dist  |  -0.5% |
| vol_20d    |  44.4% |
| mdd_60d    |  20.9% |
| rsi_14     |   49.9 |
| zscore_20d |   -0.1 |

### Apple Inc. / AAPL (score 26.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.0% |
| ret_5d     | -2.2% |
| ret_20d    | -8.3% |
| ret_60d    | +2.5% |
| ma20_dist  | -4.5% |
| ma50_dist  | -1.3% |
| vol_20d    | 33.2% |
| mdd_60d    | 12.7% |
| rsi_14     |  29.6 |
| zscore_20d |  -1.1 |

### Alphabet Inc. Class A / GOOGL (score 25.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.8% |
| ret_5d     |  -3.2% |
| ret_20d    |  -2.3% |
| ret_60d    | -12.7% |
| ma20_dist  |  -0.0% |
| ma50_dist  |  -2.2% |
| vol_20d    |  47.4% |
| mdd_60d    |  18.5% |
| rsi_14     |   62.4 |
| zscore_20d |   -0.0 |

### UnitedHealth Group Inc. / UNH (score 24.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.6% |
| ret_5d     | -1.2% |
| ret_20d    | -5.7% |
| ret_60d    | +2.6% |
| ma20_dist  | -4.1% |
| ma50_dist  | -3.7% |
| vol_20d    | 24.6% |
| mdd_60d    |  8.5% |
| rsi_14     |  35.4 |
| zscore_20d |  -1.7 |

### Brent Crude Oil / BZ=F (score 23.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.1% |
| ret_5d     |  +4.2% |
| ret_20d    |  -1.1% |
| ret_60d    | -21.7% |
| ma20_dist  |  -1.0% |
| ma50_dist  |  +3.9% |
| vol_20d    |  67.9% |
| mdd_60d    |  31.9% |
| rsi_14     |   48.2 |
| zscore_20d |   -0.2 |

### Natural Gas / NG=F (score 21.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.2% |
| ret_5d     |  +3.0% |
| ret_20d    |  -5.8% |
| ret_60d    | -11.9% |
| ma20_dist  |  -1.0% |
| ma50_dist  |  -8.3% |
| vol_20d    |  31.9% |
| mdd_60d    |  21.0% |
| rsi_14     |   48.2 |
| zscore_20d |   -0.3 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| S&P 500 / ^GSPC                     |  84.6414 |           1.1% |                 0.73x |      169.2827 |            2.2% |
| Euro Stoxx 50 / ^STOXX50E           |  63.7536 |           1.0% |                 0.87x |      127.5073 |            1.9% |
| Corn / ZC=F                         |  13.3571 |           2.8% |                 0.25x |       26.7143 |            5.6% |
| JPMorgan Chase & Co. / JPM          |   6.3214 |           1.7% |                 0.55x |       12.6429 |            3.5% |
| DAX / ^GDAXI                        | 283.0106 |           1.1% |                 0.96x |      566.0212 |            2.2% |
| NVIDIA Corporation / NVDA           |   7.5786 |           3.4% |                 0.26x |       15.1571 |            6.7% |
| NASDAQ 100 / ^NDX                   | 564.5527 |           1.9% |                 0.42x |     1129.1055 |            3.8% |
| Russell 2000 / ^RUT                 |  37.0682 |           1.2% |                 0.66x |       74.1365 |            2.4% |
| Microsoft Corporation / MSFT        |  17.4036 |           3.5% |                 0.17x |       34.8071 |            7.0% |
| Gold / GC=F                         |  71.2643 |           1.6% |                 0.47x |      142.5286 |            3.3% |
| CAC 40 / ^FCHI                      |  76.0508 |           0.9% |                 0.98x |      152.1016 |            1.8% |
| Dow Jones Industrial Average / ^DJI | 618.7720 |           1.1% |                 0.70x |     1237.5441 |            2.3% |
| Wheat / ZW=F                        |  20.8571 |           3.1% |                 0.30x |       41.7143 |            6.2% |
| Silver / SI=F                       |   1.5304 |           2.4% |                 0.30x |        3.0607 |            4.8% |
| FTSE 100 / ^FTSE                    |  93.3214 |           0.9% |                 1.22x |      186.6429 |            1.7% |
| Amazon.com Inc. / AMZN              |   9.9339 |           3.7% |                 0.16x |       19.8679 |            7.5% |
| Soybeans / ZS=F                     |  18.0179 |           1.5% |                 0.44x |       36.0357 |            3.0% |
| Hang Seng / ^HSI                    | 347.7031 |           1.4% |                 0.58x |      695.4062 |            2.7% |
| Tesla Inc. / TSLA                   |  10.9664 |           3.2% |                 0.16x |       21.9329 |            6.5% |
| Platinum / PL=F                     |  29.4643 |           1.7% |                 0.27x |       58.9286 |            3.4% |
| Meta Platforms Inc. / META          |  21.9614 |           3.7% |                 0.23x |       43.9228 |            7.4% |
| Apple Inc. / AAPL                   |   8.7989 |           2.9% |                 0.30x |       17.5979 |            5.8% |
| Alphabet Inc. Class A / GOOGL       |  11.9264 |           3.4% |                 0.21x |       23.8529 |            6.9% |
| UnitedHealth Group Inc. / UNH       |  10.8054 |           2.7% |                 0.41x |       21.6107 |            5.4% |
| Brent Crude Oil / BZ=F              |   4.3443 |           5.0% |                 0.15x |        8.6886 |           10.0% |
| Natural Gas / NG=F                  |   0.0946 |           3.4% |                 0.31x |        0.1891 |            6.9% |

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

Scoring engine version: **1.0.0** | Git commit: **959fcb2**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
