+++
title = "Market Analysis 2026-08-26"
date = "2026-08-26T00:00:00+00:00"
draft = false
summary = "Neutral market: 26 reliable instruments. Top signal: ZC=F (score 82.4)."
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
source_files = ["data/analysis/2026-08-26.json", "data/history/2026-08-26.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "0412a4e"
+++

## Market Regime

**Neutral** — 14 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Corn / ZC=F** — score 82.4, 20d return +19.7%, RSI14=63. 20d up +19.7%; above MA20 by 13.5%; RSI14=63
- **Gold / GC=F** — score 80.3, 20d return +16.5%, RSI14=72. 20d up +16.5%; above MA20 by 7.0%; RSI14=72
- **Wheat / ZW=F** — score 77.9, 20d return +11.6%, RSI14=64. 20d up +11.6%; above MA20 by 7.4%; RSI14=64
- **Soybeans / ZS=F** — score 73.0, 20d return +5.6%, RSI14=67. 20d up +5.6%; above MA20 by 4.3%; RSI14=67
- **Silver / SI=F** — score 69.1, 20d return +20.6%, RSI14=71. 20d up +20.6%; above MA20 by 6.9%; RSI14=71

## Upcoming Events

_No scheduled events for covered instruments in the next 7 days._

## Signal History

Compared with the previous available report (**2026-08-25**).

- **New top-5:** SI=F
- **Persistent top signals:** ZC=F (10 reports), ZW=F (8 reports), GC=F (5 reports), ZS=F (3 reports)
- **Dropped from top-5:** PL=F

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     -1 |    -6.7 |
| 7203.T    |     -1 |    -6.4 |
| 8306.T    |     +2 |    +9.7 |
| AAPL      |     -2 |    -5.2 |
| AMZN      |     -4 |    -7.6 |
| BZ=F      |    -17 |   -43.6 |
| CL=F      |     -2 |   -34.5 |
| GC=F      |     -1 |    +1.8 |
| GOOGL     |     -1 |    -7.3 |
| HG=F      |     +3 |   +13.9 |
| JPM       |     -2 |    -4.5 |
| META      |     +3 |   +13.6 |
| MSFT      |     -2 |    +0.6 |
| NG=F      |     +4 |    +5.8 |
| NVDA      |     +7 |   +13.3 |
| PL=F      |     -1 |    -1.5 |
| SI=F      |     +3 |   +11.8 |
| TSLA      |     +0 |    +7.9 |
| UNH       |     -7 |   -10.9 |
| XOM       |     -1 |   -10.3 |
| ZC=F      |     +1 |    +4.5 |
| ZS=F      |     +0 |    +7.6 |
| ZW=F      |     +0 |   +11.8 |
| ^DJI      |     +1 |    +0.0 |
| ^FCHI     |     +1 |    -2.1 |
| ^FTSE     |     -2 |    +0.0 |
| ^GDAXI    |     +3 |    +6.4 |
| ^GSPC     |     +1 |    +3.0 |
| ^HSI      |     +3 |    +2.4 |
| ^N225     |     +0 |    +4.5 |
| ^NDX      |     +7 |   +11.5 |
| ^RUT      |     +4 |   +11.2 |
| ^STOXX50E |     +1 |    -0.9 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Copper / HG=F** — malformed_input
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Nikkei 225 / ^N225** — missing_bars
- **WTI Crude Oil / CL=F** — malformed_input

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|    1 | Corn / ZC=F            |  82.4 |   Yes    | —               | 20d up +19.7%; above MA20 by 13.5%; RSI14=63 |
|    2 | Gold / GC=F            |  80.3 |   Yes    | —               | 20d up +16.5%; above MA20 by 7.0%; RSI14=72  |
|    3 | Wheat / ZW=F           |  77.9 |   Yes    | —               | 20d up +11.6%; above MA20 by 7.4%; RSI14=64  |
|    4 | Soybeans / ZS=F        |  73.0 |   Yes    | —               | 20d up +5.6%; above MA20 by 4.3%; RSI14=67   |
|    5 | Silver / SI=F          |  69.1 |   Yes    | —               | 20d up +20.6%; above MA20 by 6.9%; RSI14=71  |
|    6 | Platinum / PL=F        |  63.3 |   Yes    | —               | 20d up +14.3%; above MA20 by 6.2%; RSI14=67  |
|   10 | Natural Gas / NG=F     |  52.7 |   Yes    | —               | 20d up +4.0%; above MA20 by 4.1%; RSI14=60   |
|   26 | Brent Crude Oil / BZ=F |  12.1 |   Yes    | —               | 20d down -5.4%; below MA20 by 2.8%; RSI14=52 |
|   27 | Copper / HG=F          |  70.6 |    No    | malformed_input | Suppressed: malformed_input                  |
|   33 | WTI Crude Oil / CL=F   |  15.4 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    9 | Microsoft Corporation / MSFT                                                   |  60.0 |   Yes    | —                             | 20d up +25.2%; above MA20 by 2.0%; RSI14=54  |
|   13 | JPMorgan Chase & Co. / JPM                                                     |  49.4 |   Yes    | —                             | 20d down -0.2%; below MA20 by 0.1%; RSI14=46 |
|   16 | Tesla Inc. / TSLA                                                              |  47.3 |   Yes    | —                             | 20d up +13.9%; above MA20 by 5.4%; RSI14=65  |
|   18 | NVIDIA Corporation / NVDA                                                      |  39.4 |   Yes    | —                             | 20d up +8.1%; below MA20 by 0.7%; RSI14=42   |
|   21 | Amazon.com Inc. / AMZN                                                         |  31.5 |   Yes    | —                             | 20d up +13.1%; below MA20 by 1.3%; RSI14=36  |
|   22 | Apple Inc. / AAPL                                                              |  31.2 |   Yes    | —                             | 20d down -8.8%; below MA20 by 0.5%; RSI14=49 |
|   23 | Meta Platforms Inc. / META                                                     |  30.6 |   Yes    | —                             | 20d down -3.9%; below MA20 by 0.6%; RSI14=43 |
|   24 | Alphabet Inc. Class A / GOOGL                                                  |  26.4 |   Yes    | —                             | 20d up +4.0%; below MA20 by 0.9%; RSI14=32   |
|   25 | UnitedHealth Group Inc. / UNH                                                  |  26.4 |   Yes    | —                             | 20d down -7.5%; below MA20 by 1.7%; RSI14=38 |
|   28 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  60.3 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   29 | Exxon Mobil Corporation / XOM                                                  |  56.7 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   30 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  54.5 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   31 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  39.4 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    7 | DAX / ^GDAXI                        |  61.5 |   Yes    | —            | 20d up +3.2%; above MA20 by 0.6%; RSI14=55   |
|    8 | FTSE 100 / ^FTSE                    |  60.3 |   Yes    | —            | 20d up +0.1%; above MA20 by 0.5%; RSI14=50   |
|   11 | Dow Jones Industrial Average / ^DJI |  52.4 |   Yes    | —            | 20d up +1.6%; above MA20 by 0.3%; RSI14=38   |
|   12 | Euro Stoxx 50 / ^STOXX50E           |  50.0 |   Yes    | —            | 20d up +2.6%; below MA20 by 0.1%; RSI14=46   |
|   14 | S&P 500 / ^GSPC                     |  49.1 |   Yes    | —            | 20d up +3.3%; above MA20 by 0.1%; RSI14=45   |
|   15 | Russell 2000 / ^RUT                 |  48.2 |   Yes    | —            | 20d up +1.9%; above MA20 by 0.0%; RSI14=48   |
|   17 | NASDAQ 100 / ^NDX                   |  39.7 |   Yes    | —            | 20d up +5.2%; below MA20 by 0.2%; RSI14=45   |
|   19 | Hang Seng / ^HSI                    |  37.6 |   Yes    | —            | 20d up +0.8%; below MA20 by 0.6%; RSI14=43   |
|   20 | CAC 40 / ^FCHI                      |  33.0 |   Yes    | —            | 20d down -0.2%; below MA20 by 1.6%; RSI14=22 |
|   32 | Nikkei 225 / ^N225                  |  38.2 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-08-25 |
| 7203.T    | 2026-08-25 |
| 8306.T    | 2026-08-25 |
| AAPL      | 2026-08-25 |
| AMZN      | 2026-08-25 |
| BZ=F      | 2026-08-25 |
| CL=F      | 2026-08-25 |
| GC=F      | 2026-08-25 |
| GOOGL     | 2026-08-25 |
| HG=F      | 2026-08-25 |
| JPM       | 2026-08-25 |
| META      | 2026-08-25 |
| MSFT      | 2026-08-25 |
| NG=F      | 2026-08-25 |
| NVDA      | 2026-08-25 |
| PL=F      | 2026-08-25 |
| SI=F      | 2026-08-25 |
| TSLA      | 2026-08-25 |
| UNH       | 2026-08-25 |
| XOM       | 2026-08-25 |
| ZC=F      | 2026-08-25 |
| ZS=F      | 2026-08-25 |
| ZW=F      | 2026-08-25 |
| ^DJI      | 2026-08-25 |
| ^FCHI     | 2026-08-25 |
| ^FTSE     | 2026-08-25 |
| ^GDAXI    | 2026-08-25 |
| ^GSPC     | 2026-08-25 |
| ^HSI      | 2026-08-25 |
| ^N225     | 2026-08-25 |
| ^NDX      | 2026-08-25 |
| ^RUT      | 2026-08-25 |
| ^STOXX50E | 2026-08-25 |

## Symbol Details

### Corn / ZC=F (score 82.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +7.4% |
| ret_5d     | +11.6% |
| ret_20d    | +19.7% |
| ret_60d    | +22.3% |
| ma20_dist  | +13.5% |
| ma50_dist  | +18.0% |
| vol_20d    |  60.0% |
| mdd_60d    |   6.0% |
| rsi_14     |   63.3 |
| zscore_20d |    2.4 |

### Gold / GC=F (score 80.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.7% |
| ret_5d     |  +5.1% |
| ret_20d    | +16.5% |
| ret_60d    |  +6.3% |
| ma20_dist  |  +7.0% |
| ma50_dist  | +12.1% |
| vol_20d    |  22.0% |
| mdd_60d    |  11.0% |
| rsi_14     |   72.2 |
| zscore_20d |    1.8 |

### Wheat / ZW=F (score 77.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +4.6% |
| ret_5d     |  +4.9% |
| ret_20d    | +11.6% |
| ret_60d    | +21.5% |
| ma20_dist  |  +7.4% |
| ma50_dist  | +10.6% |
| vol_20d    |  38.7% |
| mdd_60d    |  10.7% |
| rsi_14     |   64.1 |
| zscore_20d |    2.0 |

### Soybeans / ZS=F (score 73.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.7% |
| ret_5d     | +1.2% |
| ret_20d    | +5.6% |
| ret_60d    | +7.2% |
| ma20_dist  | +4.3% |
| ma50_dist  | +4.8% |
| vol_20d    | 17.7% |
| mdd_60d    |  8.1% |
| rsi_14     |  66.9 |
| zscore_20d |   1.7 |

### Silver / SI=F (score 69.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.3% |
| ret_5d     |  +5.6% |
| ret_20d    | +20.6% |
| ret_60d    |  -5.5% |
| ma20_dist  |  +6.9% |
| ma50_dist  | +12.9% |
| vol_20d    |  29.8% |
| mdd_60d    |  24.2% |
| rsi_14     |   70.9 |
| zscore_20d |    1.5 |

### Platinum / PL=F (score 63.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.3% |
| ret_5d     |  +4.6% |
| ret_20d    | +14.3% |
| ret_60d    |  +0.9% |
| ma20_dist  |  +6.2% |
| ma50_dist  | +12.1% |
| vol_20d    |  37.4% |
| mdd_60d    |  18.2% |
| rsi_14     |   67.4 |
| zscore_20d |    1.6 |

### DAX / ^GDAXI (score 61.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | +0.5% |
| ret_20d    | +3.2% |
| ret_60d    | +4.5% |
| ma20_dist  | +0.6% |
| ma50_dist  | +3.0% |
| vol_20d    |  8.1% |
| mdd_60d    |  4.1% |
| rsi_14     |  55.4 |
| zscore_20d |   0.6 |

### FTSE 100 / ^FTSE (score 60.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +1.5% |
| ret_20d    | +0.1% |
| ret_60d    | +4.9% |
| ma20_dist  | +0.5% |
| ma50_dist  | +2.0% |
| vol_20d    |  4.5% |
| mdd_60d    |  1.9% |
| rsi_14     |  49.7 |
| zscore_20d |   0.9 |

### Microsoft Corporation / MSFT (score 60.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.9% |
| ret_5d     |  +2.3% |
| ret_20d    | +25.2% |
| ret_60d    |  +9.2% |
| ma20_dist  |  +2.0% |
| ma50_dist  | +16.1% |
| vol_20d    |  58.7% |
| mdd_60d    |  23.4% |
| rsi_14     |   53.7 |
| zscore_20d |    0.4 |

### Natural Gas / NG=F (score 52.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.7% |
| ret_5d     |  +1.5% |
| ret_20d    |  +4.0% |
| ret_60d    | -11.1% |
| ma20_dist  |  +4.1% |
| ma50_dist  |  -1.8% |
| vol_20d    |  31.0% |
| mdd_60d    |  21.0% |
| rsi_14     |   59.9 |
| zscore_20d |    2.0 |

### Dow Jones Industrial Average / ^DJI (score 52.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +0.4% |
| ret_20d    | +1.6% |
| ret_60d    | +5.0% |
| ma20_dist  | +0.3% |
| ma50_dist  | +1.7% |
| vol_20d    | 13.9% |
| mdd_60d    |  3.2% |
| rsi_14     |  37.5 |
| zscore_20d |   0.2 |

### Euro Stoxx 50 / ^STOXX50E (score 50.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | -0.2% |
| ret_20d    | +2.6% |
| ret_60d    | +5.7% |
| ma20_dist  | -0.1% |
| ma50_dist  | +1.6% |
| vol_20d    |  9.1% |
| mdd_60d    |  3.2% |
| rsi_14     |  46.3 |
| zscore_20d |  -0.1 |

### JPMorgan Chase & Co. / JPM (score 49.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.1% |
| ret_5d     |  -1.8% |
| ret_20d    |  -0.2% |
| ret_60d    | +19.7% |
| ma20_dist  |  -0.1% |
| ma50_dist  |  +3.3% |
| vol_20d    |  18.9% |
| mdd_60d    |   3.7% |
| rsi_14     |   46.4 |
| zscore_20d |   -0.1 |

### S&P 500 / ^GSPC (score 49.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | -0.2% |
| ret_20d    | +3.3% |
| ret_60d    | +1.3% |
| ma20_dist  | +0.1% |
| ma50_dist  | +1.7% |
| vol_20d    | 13.0% |
| mdd_60d    |  4.5% |
| rsi_14     |  44.6 |
| zscore_20d |   0.1 |

### Russell 2000 / ^RUT (score 48.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | -0.3% |
| ret_20d    | +1.9% |
| ret_60d    | +3.1% |
| ma20_dist  | +0.0% |
| ma50_dist  | +0.7% |
| vol_20d    | 15.6% |
| mdd_60d    |  3.9% |
| rsi_14     |  48.4 |
| zscore_20d |   0.0 |

### Tesla Inc. / TSLA (score 47.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.4% |
| ret_5d     |  +4.0% |
| ret_20d    | +13.9% |
| ret_60d    | -19.6% |
| ma20_dist  |  +5.4% |
| ma50_dist  |  -3.7% |
| vol_20d    |  39.0% |
| mdd_60d    |  29.9% |
| rsi_14     |   65.3 |
| zscore_20d |    1.2 |

### NASDAQ 100 / ^NDX (score 39.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | -1.0% |
| ret_20d    | +5.2% |
| ret_60d    | -3.7% |
| ma20_dist  | -0.2% |
| ma50_dist  | -0.3% |
| vol_20d    | 21.9% |
| mdd_60d    | 11.3% |
| rsi_14     |  44.8 |
| zscore_20d |  -0.1 |

### NVIDIA Corporation / NVDA (score 39.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.2% |
| ret_5d     | -3.0% |
| ret_20d    | +8.1% |
| ret_60d    | +0.9% |
| ma20_dist  | -0.7% |
| ma50_dist  | +2.5% |
| vol_20d    | 34.7% |
| mdd_60d    | 15.3% |
| rsi_14     |  42.4 |
| zscore_20d |  -0.2 |

### Hang Seng / ^HSI (score 37.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.0% |
| ret_5d     | +0.2% |
| ret_20d    | +0.8% |
| ret_60d    | +1.3% |
| ma20_dist  | -0.6% |
| ma50_dist  | +3.1% |
| vol_20d    | 15.4% |
| mdd_60d    | 12.9% |
| rsi_14     |  43.3 |
| zscore_20d |  -0.6 |

### CAC 40 / ^FCHI (score 33.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | -0.8% |
| ret_20d    | -0.2% |
| ret_60d    | +2.8% |
| ma20_dist  | -1.6% |
| ma50_dist  | -0.3% |
| vol_20d    |  8.3% |
| mdd_60d    |  3.3% |
| rsi_14     |  21.7 |
| zscore_20d |  -1.3 |

### Amazon.com Inc. / AMZN (score 31.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.4% |
| ret_5d     |  +0.6% |
| ret_20d    | +13.1% |
| ret_60d    |  -3.5% |
| ma20_dist  |  -1.3% |
| ma50_dist  |  +4.2% |
| vol_20d    |  61.3% |
| mdd_60d    |  13.2% |
| rsi_14     |   36.5 |
| zscore_20d |   -0.3 |

### Apple Inc. / AAPL (score 31.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | -0.0% |
| ret_20d    | -8.8% |
| ret_60d    | -0.7% |
| ma20_dist  | -0.5% |
| ma50_dist  | -0.3% |
| vol_20d    | 30.9% |
| mdd_60d    | 12.7% |
| rsi_14     |  48.9 |
| zscore_20d |  -0.2 |

### Meta Platforms Inc. / META (score 30.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.0% |
| ret_5d     | +4.9% |
| ret_20d    | -3.9% |
| ret_60d    | -9.8% |
| ma20_dist  | -0.6% |
| ma50_dist  | -3.8% |
| vol_20d    | 46.6% |
| mdd_60d    | 20.9% |
| rsi_14     |  42.5 |
| zscore_20d |  -0.2 |

### Alphabet Inc. Class A / GOOGL (score 26.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | +0.8% |
| ret_20d    | +4.0% |
| ret_60d    | -8.7% |
| ma20_dist  | -0.9% |
| ma50_dist  | -1.2% |
| vol_20d    | 37.3% |
| mdd_60d    | 15.5% |
| rsi_14     |  32.3 |
| zscore_20d |  -0.3 |

### UnitedHealth Group Inc. / UNH (score 26.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | +0.7% |
| ret_20d    | -7.5% |
| ret_60d    | +4.9% |
| ma20_dist  | -1.7% |
| ma50_dist  | -4.1% |
| vol_20d    | 20.3% |
| mdd_60d    | 11.8% |
| rsi_14     |  37.7 |
| zscore_20d |  -0.7 |

### Brent Crude Oil / BZ=F (score 12.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -7.5% |
| ret_5d     |  -6.9% |
| ret_20d    |  -5.4% |
| ret_60d    | -12.8% |
| ma20_dist  |  -2.8% |
| ma50_dist  |  +1.1% |
| vol_20d    |  48.9% |
| mdd_60d    |  24.7% |
| rsi_14     |   52.1 |
| zscore_20d |   -0.6 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Corn / ZC=F                         |  19.9643 |           3.8% |                 0.17x |       39.9286 |            7.6% |
| Gold / GC=F                         |  84.5358 |           1.8% |                 0.45x |      169.0716 |            3.6% |
| Wheat / ZW=F                        |  23.3571 |           3.3% |                 0.26x |       46.7143 |            6.5% |
| Soybeans / ZS=F                     |  17.9286 |           1.4% |                 0.56x |       35.8571 |            2.9% |
| Silver / SI=F                       |   1.5529 |           2.2% |                 0.34x |        3.1057 |            4.5% |
| Platinum / PL=F                     |  29.9000 |           1.6% |                 0.27x |       59.8000 |            3.2% |
| DAX / ^GDAXI                        | 199.8828 |           0.8% |                 1.23x |      399.7656 |            1.5% |
| FTSE 100 / ^FTSE                    |  75.7143 |           0.7% |                 2.21x |      151.4286 |            1.4% |
| Microsoft Corporation / MSFT        |   9.3802 |           1.9% |                 0.17x |       18.7604 |            3.8% |
| Natural Gas / NG=F                  |   0.0852 |           3.0% |                 0.32x |        0.1704 |            6.0% |
| Dow Jones Industrial Average / ^DJI | 378.6574 |           0.7% |                 0.72x |      757.3147 |            1.4% |
| Euro Stoxx 50 / ^STOXX50E           |  45.3221 |           0.7% |                 1.10x |       90.6442 |            1.4% |
| JPMorgan Chase & Co. / JPM          |   5.4265 |           1.5% |                 0.53x |       10.8530 |            3.0% |
| S&P 500 / ^GSPC                     |  47.7965 |           0.6% |                 0.77x |       95.5929 |            1.2% |
| Russell 2000 / ^RUT                 |  26.8674 |           0.9% |                 0.64x |       53.7348 |            1.8% |
| Tesla Inc. / TSLA                   |  12.0214 |           3.4% |                 0.26x |       24.0429 |            6.9% |
| NASDAQ 100 / ^NDX                   | 341.3947 |           1.2% |                 0.46x |      682.7893 |            2.3% |
| NVIDIA Corporation / NVDA           |   5.5999 |           2.6% |                 0.29x |       11.1999 |            5.3% |
| Hang Seng / ^HSI                    | 346.0508 |           1.4% |                 0.65x |      692.1016 |            2.7% |
| CAC 40 / ^FCHI                      |  56.7842 |           0.7% |                 1.21x |      113.5684 |            1.3% |
| Amazon.com Inc. / AMZN              |   5.5637 |           2.1% |                 0.16x |       11.1274 |            4.3% |
| Apple Inc. / AAPL                   |   5.9757 |           1.9% |                 0.32x |       11.9515 |            3.9% |
| Meta Platforms Inc. / META          |  16.4121 |           2.9% |                 0.21x |       32.8243 |            5.8% |
| Alphabet Inc. Class A / GOOGL       |   6.3586 |           1.8% |                 0.27x |       12.7171 |            3.7% |
| UnitedHealth Group Inc. / UNH       |   8.4850 |           2.1% |                 0.49x |       16.9700 |            4.3% |
| Brent Crude Oil / BZ=F              |   2.8764 |           3.4% |                 0.20x |        5.7529 |            6.7% |

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

Scoring engine version: **1.0.0** | Git commit: **0412a4e**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
