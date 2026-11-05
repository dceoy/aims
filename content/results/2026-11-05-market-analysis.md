+++
title = "Market Analysis 2026-11-05"
date = "2026-11-05T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: MSFT (score 83.3)."
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
source_files = ["data/analysis/2026-11-05.json", "data/history/2026-11-05.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "a235fe7"
+++

## Market Regime

**Neutral** — 13 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Microsoft Corporation / MSFT** — score 83.3, 20d return +4.9%, RSI14=57. 20d up +4.9%; above MA20 by 4.7%; RSI14=57
- **DAX / ^GDAXI** — score 81.5, 20d return +5.3%, RSI14=66. 20d up +5.3%; above MA20 by 3.6%; RSI14=66
- **JPMorgan Chase & Co. / JPM** — score 78.8, 20d return +6.8%, RSI14=64. 20d up +6.8%; above MA20 by 4.6%; RSI14=64
- **Dow Jones Industrial Average / ^DJI** — score 77.3, 20d return +4.3%, RSI14=63. 20d up +4.3%; above MA20 by 2.3%; RSI14=63
- **Apple Inc. / AAPL** — score 77.0, 20d return +3.8%, RSI14=56. 20d up +3.8%; above MA20 by 1.9%; RSI14=56

## Upcoming Events

_No scheduled events for covered instruments in the next 7 days._

## Signal History

Compared with the previous available report (**2026-11-04**).

- **New top-5:** AAPL, JPM, MSFT, ^DJI
- **Persistent top signals:** ^GDAXI (7 reports)
- **Dropped from top-5:** TSLA, UNH, ^FCHI, ^RUT

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +0 |   -10.9 |
| 7203.T    |     +1 |   -12.1 |
| 8306.T    |     +1 |    -4.5 |
| AAPL      |     +9 |   +30.6 |
| AMZN      |     +6 |   +21.2 |
| BZ=F      |     -7 |   -23.6 |
| CL=F      |     -4 |   -30.3 |
| GC=F      |     +5 |   +14.8 |
| GOOGL     |     -2 |    +2.4 |
| HG=F      |     +4 |    +5.2 |
| JPM       |     +4 |   +13.3 |
| META      |     +0 |    -1.8 |
| MSFT      |     +8 |   +20.6 |
| NG=F      |     +2 |    -0.3 |
| NVDA      |     -5 |   -17.0 |
| PL=F      |     +4 |   +16.1 |
| SI=F      |     +3 |   +15.8 |
| TSLA      |     -9 |   -14.2 |
| UNH       |     -7 |    -6.1 |
| XOM       |     -3 |   -28.5 |
| ZC=F      |     +2 |    +2.1 |
| ZS=F      |     -1 |    -6.1 |
| ZW=F      |     +1 |    -0.6 |
| ^DJI      |     +2 |   +11.5 |
| ^FCHI     |     -3 |    +1.2 |
| ^FTSE     |     +0 |    +6.1 |
| ^GDAXI    |     -1 |    +4.8 |
| ^GSPC     |     -1 |    +3.9 |
| ^HSI      |     -2 |    +0.6 |
| ^N225     |     -1 |   -14.2 |
| ^NDX      |     +0 |    -2.1 |
| ^RUT      |     -6 |    -3.6 |
| ^STOXX50E |     +0 |    +5.8 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Natural Gas / NG=F** — malformed_input
- **Copper / HG=F** — malformed_input
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Nikkei 225 / ^N225** — missing_bars
- **WTI Crude Oil / CL=F** — malformed_input

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|   15 | Gold / GC=F            |  44.5 |   Yes    | —               | 20d down -1.6%; below MA20 by 0.4%; RSI14=43  |
|   16 | Soybeans / ZS=F        |  37.6 |   Yes    | —               | 20d down -8.0%; below MA20 by 4.3%; RSI14=14  |
|   19 | Corn / ZC=F            |  30.9 |   Yes    | —               | 20d down -11.5%; below MA20 by 4.2%; RSI14=14 |
|   20 | Platinum / PL=F        |  27.0 |   Yes    | —               | 20d down -8.1%; below MA20 by 4.6%; RSI14=36  |
|   21 | Wheat / ZW=F           |  24.6 |   Yes    | —               | 20d down -12.8%; below MA20 by 5.8%; RSI14=9  |
|   22 | Silver / SI=F          |  22.1 |   Yes    | —               | 20d down -13.0%; below MA20 by 5.6%; RSI14=35 |
|   23 | Brent Crude Oil / BZ=F |  18.8 |   Yes    | —               | 20d down -5.6%; below MA20 by 13.2%; RSI14=37 |
|   28 | Natural Gas / NG=F     |  49.4 |    No    | malformed_input | Suppressed: malformed_input                   |
|   29 | Copper / HG=F          |  42.1 |    No    | malformed_input | Suppressed: malformed_input                   |
|   33 | WTI Crude Oil / CL=F   |  24.2 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                    |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | ---------------------------------------------- |
|    1 | Microsoft Corporation / MSFT                                                   |  83.3 |   Yes    | —                             | 20d up +4.9%; above MA20 by 4.7%; RSI14=57     |
|    3 | JPMorgan Chase & Co. / JPM                                                     |  78.8 |   Yes    | —                             | 20d up +6.8%; above MA20 by 4.6%; RSI14=64     |
|    5 | Apple Inc. / AAPL                                                              |  77.0 |   Yes    | —                             | 20d up +3.8%; above MA20 by 1.9%; RSI14=56     |
|    7 | Amazon.com Inc. / AMZN                                                         |  71.8 |   Yes    | —                             | 20d up +2.4%; above MA20 by 4.7%; RSI14=57     |
|    9 | UnitedHealth Group Inc. / UNH                                                  |  66.4 |   Yes    | —                             | 20d up +8.9%; above MA20 by 1.6%; RSI14=52     |
|   13 | Tesla Inc. / TSLA                                                              |  56.4 |   Yes    | —                             | 20d up +2.0%; above MA20 by 0.5%; RSI14=60     |
|   18 | Meta Platforms Inc. / META                                                     |  33.6 |   Yes    | —                             | 20d down -12.7%; below MA20 by 6.5%; RSI14=21  |
|   24 | NVIDIA Corporation / NVDA                                                      |  15.2 |   Yes    | —                             | 20d down -15.7%; below MA20 by 7.4%; RSI14=35  |
|   25 | Alphabet Inc. Class A / GOOGL                                                  |  14.6 |   Yes    | —                             | 20d down -17.6%; below MA20 by 10.8%; RSI14=21 |
|   26 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  60.6 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   27 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  56.1 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   30 | Exxon Mobil Corporation / XOM                                                  |  41.2 |    No    | malformed_input               | Suppressed: malformed_input                    |
|   31 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  37.6 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    2 | DAX / ^GDAXI                        |  81.5 |   Yes    | —            | 20d up +5.3%; above MA20 by 3.6%; RSI14=66   |
|    4 | Dow Jones Industrial Average / ^DJI |  77.3 |   Yes    | —            | 20d up +4.3%; above MA20 by 2.3%; RSI14=63   |
|    6 | CAC 40 / ^FCHI                      |  73.3 |   Yes    | —            | 20d up +5.3%; above MA20 by 3.5%; RSI14=65   |
|    8 | FTSE 100 / ^FTSE                    |  70.3 |   Yes    | —            | 20d up +3.5%; above MA20 by 1.1%; RSI14=49   |
|   10 | Euro Stoxx 50 / ^STOXX50E           |  65.2 |   Yes    | —            | 20d up +1.4%; above MA20 by 1.7%; RSI14=56   |
|   11 | Russell 2000 / ^RUT                 |  62.4 |   Yes    | —            | 20d up +2.3%; above MA20 by 2.4%; RSI14=65   |
|   12 | S&P 500 / ^GSPC                     |  60.0 |   Yes    | —            | 20d down -1.5%; below MA20 by 0.1%; RSI14=46 |
|   14 | Hang Seng / ^HSI                    |  52.7 |   Yes    | —            | 20d down -1.5%; above MA20 by 1.1%; RSI14=44 |
|   17 | NASDAQ 100 / ^NDX                   |  34.2 |   Yes    | —            | 20d down -8.7%; below MA20 by 3.6%; RSI14=36 |
|   32 | Nikkei 225 / ^N225                  |  29.4 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-11-04 |
| 7203.T    | 2026-11-04 |
| 8306.T    | 2026-11-04 |
| AAPL      | 2026-11-04 |
| AMZN      | 2026-11-04 |
| BZ=F      | 2026-11-04 |
| CL=F      | 2026-11-04 |
| GC=F      | 2026-11-04 |
| GOOGL     | 2026-11-04 |
| HG=F      | 2026-11-04 |
| JPM       | 2026-11-04 |
| META      | 2026-11-04 |
| MSFT      | 2026-11-04 |
| NG=F      | 2026-11-04 |
| NVDA      | 2026-11-04 |
| PL=F      | 2026-11-04 |
| SI=F      | 2026-11-04 |
| TSLA      | 2026-11-04 |
| UNH       | 2026-11-04 |
| XOM       | 2026-11-04 |
| ZC=F      | 2026-11-04 |
| ZS=F      | 2026-11-04 |
| ZW=F      | 2026-11-04 |
| ^DJI      | 2026-11-04 |
| ^FCHI     | 2026-11-04 |
| ^FTSE     | 2026-11-04 |
| ^GDAXI    | 2026-11-04 |
| ^GSPC     | 2026-11-04 |
| ^HSI      | 2026-11-04 |
| ^N225     | 2026-11-04 |
| ^NDX      | 2026-11-04 |
| ^RUT      | 2026-11-04 |
| ^STOXX50E | 2026-11-04 |

## Symbol Details

### Microsoft Corporation / MSFT (score 83.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +6.7% |
| ret_5d     |  +4.7% |
| ret_20d    |  +4.9% |
| ret_60d    | +10.5% |
| ma20_dist  |  +4.7% |
| ma50_dist  |  +7.9% |
| vol_20d    |  33.1% |
| mdd_60d    |   6.7% |
| rsi_14     |   57.1 |
| zscore_20d |    2.5 |

### DAX / ^GDAXI (score 81.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.2% |
| ret_5d     | +2.9% |
| ret_20d    | +5.3% |
| ret_60d    | +0.4% |
| ma20_dist  | +3.6% |
| ma50_dist  | +3.4% |
| vol_20d    | 14.8% |
| mdd_60d    |  6.6% |
| rsi_14     |  66.0 |
| zscore_20d |   2.5 |

### JPMorgan Chase & Co. / JPM (score 78.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +4.2% |
| ret_5d     | +3.8% |
| ret_20d    | +6.8% |
| ret_60d    | -2.7% |
| ma20_dist  | +4.6% |
| ma50_dist  | +3.0% |
| vol_20d    | 20.8% |
| mdd_60d    |  9.9% |
| rsi_14     |  64.5 |
| zscore_20d |   3.3 |

### Dow Jones Industrial Average / ^DJI (score 77.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +3.0% |
| ret_5d     | +1.7% |
| ret_20d    | +4.3% |
| ret_60d    | -0.8% |
| ma20_dist  | +2.3% |
| ma50_dist  | +2.3% |
| vol_20d    | 13.9% |
| mdd_60d    |  5.4% |
| rsi_14     |  62.5 |
| zscore_20d |   2.4 |

### Apple Inc. / AAPL (score 77.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +5.3% |
| ret_5d     |  +1.7% |
| ret_20d    |  +3.8% |
| ret_60d    | +14.6% |
| ma20_dist  |  +1.9% |
| ma50_dist  |  +4.4% |
| vol_20d    |  25.1% |
| mdd_60d    |   4.9% |
| rsi_14     |   55.8 |
| zscore_20d |    1.6 |

### CAC 40 / ^FCHI (score 73.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.0% |
| ret_5d     | +3.7% |
| ret_20d    | +5.3% |
| ret_60d    | -5.7% |
| ma20_dist  | +3.5% |
| ma50_dist  | +1.8% |
| vol_20d    | 12.6% |
| mdd_60d    | 10.6% |
| rsi_14     |  64.9 |
| zscore_20d |   2.7 |

### Amazon.com Inc. / AMZN (score 71.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +6.1% |
| ret_5d     | +4.5% |
| ret_20d    | +2.4% |
| ret_60d    | -2.3% |
| ma20_dist  | +4.7% |
| ma50_dist  | +4.8% |
| vol_20d    | 42.0% |
| mdd_60d    | 10.1% |
| rsi_14     |  57.2 |
| zscore_20d |   1.7 |

### FTSE 100 / ^FTSE (score 70.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.8% |
| ret_5d     | +1.3% |
| ret_20d    | +3.5% |
| ret_60d    | -0.1% |
| ma20_dist  | +1.1% |
| ma50_dist  | +1.2% |
| vol_20d    | 11.5% |
| mdd_60d    |  4.2% |
| rsi_14     |  49.3 |
| zscore_20d |   1.2 |

### UnitedHealth Group Inc. / UNH (score 66.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.2% |
| ret_5d     | +0.6% |
| ret_20d    | +8.9% |
| ret_60d    | +1.8% |
| ma20_dist  | +1.6% |
| ma50_dist  | +4.9% |
| vol_20d    | 28.2% |
| mdd_60d    |  9.4% |
| rsi_14     |  51.8 |
| zscore_20d |   0.4 |

### Euro Stoxx 50 / ^STOXX50E (score 65.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.0% |
| ret_5d     | +1.6% |
| ret_20d    | +1.4% |
| ret_60d    | -4.1% |
| ma20_dist  | +1.7% |
| ma50_dist  | +0.2% |
| vol_20d    | 14.7% |
| mdd_60d    |  7.3% |
| rsi_14     |  56.4 |
| zscore_20d |   2.3 |

### Russell 2000 / ^RUT (score 62.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.6% |
| ret_5d     | +0.9% |
| ret_20d    | +2.3% |
| ret_60d    | -5.6% |
| ma20_dist  | +2.4% |
| ma50_dist  | +0.3% |
| vol_20d    | 15.8% |
| mdd_60d    | 11.3% |
| rsi_14     |  64.7 |
| zscore_20d |   1.8 |

### S&P 500 / ^GSPC (score 60.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.6% |
| ret_5d     | -0.7% |
| ret_20d    | -1.5% |
| ret_60d    | -0.5% |
| ma20_dist  | -0.1% |
| ma50_dist  | -0.1% |
| vol_20d    | 12.6% |
| mdd_60d    |  3.5% |
| rsi_14     |  46.5 |
| zscore_20d |  -0.2 |

### Tesla Inc. / TSLA (score 56.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -3.3% |
| ret_5d     |  -4.7% |
| ret_20d    |  +2.0% |
| ret_60d    | +15.7% |
| ma20_dist  |  +0.5% |
| ma50_dist  |  +3.5% |
| vol_20d    |  37.9% |
| mdd_60d    |   7.3% |
| rsi_14     |   59.5 |
| zscore_20d |    0.1 |

### Hang Seng / ^HSI (score 52.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.7% |
| ret_5d     | +3.6% |
| ret_20d    | -1.5% |
| ret_60d    | -7.8% |
| ma20_dist  | +1.1% |
| ma50_dist  | -2.2% |
| vol_20d    | 18.1% |
| mdd_60d    | 11.8% |
| rsi_14     |  43.9 |
| zscore_20d |   0.5 |

### Gold / GC=F (score 44.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +3.4% |
| ret_5d     | +0.5% |
| ret_20d    | -1.6% |
| ret_60d    | -7.0% |
| ma20_dist  | -0.4% |
| ma50_dist  | -4.2% |
| vol_20d    | 23.1% |
| mdd_60d    | 17.2% |
| rsi_14     |  42.8 |
| zscore_20d |  -0.2 |

### Soybeans / ZS=F (score 37.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | -2.6% |
| ret_20d    | -8.0% |
| ret_60d    | +2.1% |
| ma20_dist  | -4.3% |
| ma50_dist  | -6.6% |
| vol_20d    |  8.3% |
| mdd_60d    | 10.1% |
| rsi_14     |  14.1 |
| zscore_20d |  -1.9 |

### NASDAQ 100 / ^NDX (score 34.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | -4.6% |
| ret_20d    | -8.7% |
| ret_60d    | -3.7% |
| ma20_dist  | -3.6% |
| ma50_dist  | -4.4% |
| vol_20d    | 22.6% |
| mdd_60d    | 10.4% |
| rsi_14     |  36.3 |
| zscore_20d |  -1.3 |

### Meta Platforms Inc. / META (score 33.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.4% |
| ret_5d     |  +2.9% |
| ret_20d    | -12.7% |
| ret_60d    |  +5.2% |
| ma20_dist  |  -6.5% |
| ma50_dist  |  -6.4% |
| vol_20d    |  37.3% |
| mdd_60d    |  22.0% |
| rsi_14     |   21.0 |
| zscore_20d |   -0.8 |

### Corn / ZC=F (score 30.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.4% |
| ret_5d     |  -1.7% |
| ret_20d    | -11.5% |
| ret_60d    |  -0.8% |
| ma20_dist  |  -4.2% |
| ma50_dist  | -10.4% |
| vol_20d    |  16.2% |
| mdd_60d    |  18.5% |
| rsi_14     |   13.9 |
| zscore_20d |   -1.2 |

### Platinum / PL=F (score 27.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +4.8% |
| ret_5d     |  -3.0% |
| ret_20d    |  -8.1% |
| ret_60d    | -14.2% |
| ma20_dist  |  -4.6% |
| ma50_dist  | -11.3% |
| vol_20d    |  34.6% |
| mdd_60d    |  25.2% |
| rsi_14     |   35.8 |
| zscore_20d |   -0.9 |

### Wheat / ZW=F (score 24.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.2% |
| ret_5d     |  -0.1% |
| ret_20d    | -12.8% |
| ret_60d    |  -8.3% |
| ma20_dist  |  -5.8% |
| ma50_dist  | -12.6% |
| vol_20d    |  13.9% |
| mdd_60d    |  22.0% |
| rsi_14     |    9.1 |
| zscore_20d |   -1.2 |

### Silver / SI=F (score 22.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +5.1% |
| ret_5d     |  -2.5% |
| ret_20d    | -13.0% |
| ret_60d    | -19.8% |
| ma20_dist  |  -5.6% |
| ma50_dist  | -14.0% |
| vol_20d    |  44.9% |
| mdd_60d    |  29.3% |
| rsi_14     |   35.2 |
| zscore_20d |   -0.9 |

### Brent Crude Oil / BZ=F (score 18.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -8.7% |
| ret_5d     | -18.0% |
| ret_20d    |  -5.6% |
| ret_60d    |  +6.9% |
| ma20_dist  | -13.2% |
| ma50_dist  |  -9.0% |
| vol_20d    |  58.0% |
| mdd_60d    |  19.6% |
| rsi_14     |   37.0 |
| zscore_20d |   -2.6 |

### NVIDIA Corporation / NVDA (score 15.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -3.2% |
| ret_5d     |  -7.1% |
| ret_20d    | -15.7% |
| ret_60d    |  -7.9% |
| ma20_dist  |  -7.4% |
| ma50_dist  |  -9.5% |
| vol_20d    |  32.6% |
| mdd_60d    |  16.3% |
| rsi_14     |   35.1 |
| zscore_20d |   -1.9 |

### Alphabet Inc. Class A / GOOGL (score 14.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +3.2% |
| ret_5d     | -11.1% |
| ret_20d    | -17.6% |
| ret_60d    | -15.9% |
| ma20_dist  | -10.8% |
| ma50_dist  | -13.8% |
| vol_20d    |  48.6% |
| mdd_60d    |  21.4% |
| rsi_14     |   20.9 |
| zscore_20d |   -1.3 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Microsoft Corporation / MSFT        |  15.0257 |           2.7% |                 0.30x |       30.0514 |            5.4% |
| DAX / ^GDAXI                        | 359.3507 |           1.4% |                 0.68x |      718.7015 |            2.7% |
| JPMorgan Chase & Co. / JPM          |   6.7371 |           1.9% |                 0.48x |       13.4743 |            3.8% |
| Dow Jones Industrial Average / ^DJI | 599.6038 |           1.1% |                 0.72x |     1199.2076 |            2.2% |
| Apple Inc. / AAPL                   |   8.4764 |           2.4% |                 0.40x |       16.9529 |            4.9% |
| CAC 40 / ^FCHI                      | 100.8358 |           1.2% |                 0.79x |      201.6715 |            2.5% |
| Amazon.com Inc. / AMZN              |   9.3379 |           3.5% |                 0.24x |       18.6757 |            7.0% |
| FTSE 100 / ^FTSE                    | 106.6929 |           1.0% |                 0.87x |      213.3857 |            2.0% |
| UnitedHealth Group Inc. / UNH       |  11.6657 |           2.8% |                 0.35x |       23.3314 |            5.7% |
| Euro Stoxx 50 / ^STOXX50E           |  83.9908 |           1.3% |                 0.68x |      167.9816 |            2.7% |
| Russell 2000 / ^RUT                 |  38.0300 |           1.3% |                 0.63x |       76.0600 |            2.7% |
| S&P 500 / ^GSPC                     |  89.7136 |           1.2% |                 0.80x |      179.4272 |            2.3% |
| Tesla Inc. / TSLA                   |  15.7771 |           4.1% |                 0.26x |       31.5543 |            8.2% |
| Hang Seng / ^HSI                    | 370.5304 |           1.5% |                 0.55x |      741.0608 |            3.1% |
| Gold / GC=F                         |  80.5928 |           2.0% |                 0.43x |      161.1857 |            4.0% |
| Soybeans / ZS=F                     |  15.8571 |           1.3% |                 1.20x |       31.7143 |            2.7% |
| NASDAQ 100 / ^NDX                   | 603.5158 |           2.1% |                 0.44x |     1207.0315 |            4.2% |
| Meta Platforms Inc. / META          |  22.3664 |           3.6% |                 0.27x |       44.7329 |            7.1% |
| Corn / ZC=F                         |   7.1964 |           1.6% |                 0.62x |       14.3929 |            3.2% |
| Platinum / PL=F                     |  34.1071 |           2.3% |                 0.29x |       68.2143 |            4.5% |
| Wheat / ZW=F                        |  13.8393 |           2.3% |                 0.72x |       27.6786 |            4.6% |
| Silver / SI=F                       |   1.3802 |           2.6% |                 0.22x |        2.7604 |            5.3% |
| Brent Crude Oil / BZ=F              |   5.4786 |           5.8% |                 0.17x |       10.9571 |           11.6% |
| NVIDIA Corporation / NVDA           |   6.5114 |           3.3% |                 0.31x |       13.0229 |            6.5% |
| Alphabet Inc. Class A / GOOGL       |  10.6629 |           3.7% |                 0.21x |       21.3257 |            7.4% |

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

Scoring engine version: **1.0.0** | Git commit: **a235fe7**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
