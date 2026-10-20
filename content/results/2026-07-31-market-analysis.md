+++
title = "Market Analysis 2026-07-31"
date = "2026-07-31T00:00:00+00:00"
draft = false
summary = "Neutral market: 26 reliable instruments. Top signal: MSFT (score 77.3)."
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
source_files = ["data/analysis/2026-07-31.json", "data/history/2026-07-31.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "9e92ef0"
+++

## Market Regime

**Neutral** — 14 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Microsoft Corporation / MSFT** — score 77.3, 20d return +17.4%, RSI14=74. 20d up +17.4%; above MA20 by 14.7%; RSI14=74
- **FTSE 100 / ^FTSE** — score 73.0, 20d return +2.3%, RSI14=76. 20d up +2.3%; above MA20 by 2.4%; RSI14=76
- **JPMorgan Chase & Co. / JPM** — score 70.3, 20d return +5.5%, RSI14=62. 20d up +5.5%; above MA20 by 2.2%; RSI14=62
- **Hang Seng / ^HSI** — score 67.9, 20d return +12.2%, RSI14=74. 20d up +12.2%; above MA20 by 4.9%; RSI14=74
- **Apple Inc. / AAPL** — score 67.3, 20d return +13.3%, RSI14=64. 20d up +13.3%; above MA20 by 2.8%; RSI14=64

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                   | Applies To |
| ---------- | ----------------------- | ---------- |
| 2026-08-03 | 8306.T earnings release | 8306.T     |
| 2026-08-04 | 7203.T earnings release | 7203.T     |

## Signal History

Compared with the previous available report (**2026-07-30**).

- **New top-5:** JPM, MSFT
- **Persistent top signals:** ^FTSE (7 reports), AAPL (5 reports), ^HSI (2 reports)
- **Dropped from top-5:** ^FCHI, ^GDAXI

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +1 |    -3.6 |
| 7203.T    |     -2 |   -14.2 |
| 8306.T    |     -1 |   -23.0 |
| AAPL      |     -3 |    -8.8 |
| AMZN      |     +4 |   +14.8 |
| BZ=F      |     -8 |   -16.7 |
| CL=F      |     -1 |   -15.4 |
| GC=F      |     +2 |    +6.1 |
| GOOGL     |     -5 |    -6.4 |
| HG=F      |     +4 |   +16.4 |
| JPM       |     +3 |    +8.5 |
| META      |     -6 |   -22.4 |
| MSFT      |    +11 |   +29.1 |
| NG=F      |     -1 |    -1.5 |
| NVDA      |     +3 |   +10.3 |
| PL=F      |     +8 |   +20.9 |
| SI=F      |     +0 |    +4.5 |
| TSLA      |     +1 |   +10.3 |
| UNH       |     -4 |    -1.8 |
| XOM       |     -1 |   -11.2 |
| ZC=F      |     -5 |    -7.9 |
| ZS=F      |     -4 |    -5.8 |
| ZW=F      |     -3 |    -5.8 |
| ^DJI      |     +4 |    +7.6 |
| ^FCHI     |     -2 |    +2.4 |
| ^FTSE     |     -1 |    -8.8 |
| ^GDAXI    |     -2 |    -2.7 |
| ^GSPC     |     +5 |    +9.4 |
| ^HSI      |     -1 |    -6.7 |
| ^N225     |     +0 |    +0.9 |
| ^NDX      |     +3 |   +10.3 |
| ^RUT      |     +1 |    +6.4 |
| ^STOXX50E |     +0 |    +4.8 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **WTI Crude Oil / CL=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|   10 | Wheat / ZW=F           |  53.6 |   Yes    | —               | 20d up +12.1%; above MA20 by 1.9%; RSI14=60   |
|   11 | Platinum / PL=F        |  51.8 |   Yes    | —               | 20d up +4.0%; above MA20 by 2.1%; RSI14=55    |
|   13 | Gold / GC=F            |  49.4 |   Yes    | —               | 20d up +0.8%; above MA20 by 0.7%; RSI14=50    |
|   16 | Corn / ZC=F            |  42.1 |   Yes    | —               | 20d up +5.9%; above MA20 by 0.0%; RSI14=55    |
|   17 | Brent Crude Oil / BZ=F |  38.5 |   Yes    | —               | 20d up +24.4%; above MA20 by 4.9%; RSI14=63   |
|   18 | Soybeans / ZS=F        |  38.2 |   Yes    | —               | 20d up +4.5%; below MA20 by 2.0%; RSI14=44    |
|   21 | Silver / SI=F          |  32.4 |   Yes    | —               | 20d down -2.1%; above MA20 by 0.4%; RSI14=47  |
|   24 | Natural Gas / NG=F     |  21.2 |   Yes    | —               | 20d down -14.3%; below MA20 by 6.1%; RSI14=36 |
|   28 | Copper / HG=F          |  69.4 |    No    | malformed_input | Suppressed: malformed_input                   |
|   32 | WTI Crude Oil / CL=F   |  40.0 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                    |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | ---------------------------------------------- |
|    1 | Microsoft Corporation / MSFT                                                   |  77.3 |   Yes    | —                             | 20d up +17.4%; above MA20 by 14.7%; RSI14=74   |
|    3 | JPMorgan Chase & Co. / JPM                                                     |  70.3 |   Yes    | —                             | 20d up +5.5%; above MA20 by 2.2%; RSI14=62     |
|    5 | Apple Inc. / AAPL                                                              |  67.3 |   Yes    | —                             | 20d up +13.3%; above MA20 by 2.8%; RSI14=64    |
|   14 | UnitedHealth Group Inc. / UNH                                                  |  49.4 |   Yes    | —                             | 20d down -1.2%; below MA20 by 0.8%; RSI14=48   |
|   20 | Amazon.com Inc. / AMZN                                                         |  34.9 |   Yes    | —                             | 20d down -2.6%; below MA20 by 2.9%; RSI14=41   |
|   22 | NVIDIA Corporation / NVDA                                                      |  26.1 |   Yes    | —                             | 20d down -1.3%; below MA20 by 3.9%; RSI14=37   |
|   23 | Alphabet Inc. Class A / GOOGL                                                  |  24.9 |   Yes    | —                             | 20d down -7.6%; below MA20 by 4.2%; RSI14=39   |
|   25 | Tesla Inc. / TSLA                                                              |  15.2 |   Yes    | —                             | 20d down -27.4%; below MA20 by 16.1%; RSI14=15 |
|   26 | Meta Platforms Inc. / META                                                     |   7.9 |   Yes    | —                             | 20d down -12.1%; below MA20 by 13.4%; RSI14=14 |
|   27 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  77.6 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   29 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  68.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   30 | Exxon Mobil Corporation / XOM                                                  |  63.3 |    No    | malformed_input               | Suppressed: malformed_input                    |
|   31 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  48.5 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    2 | FTSE 100 / ^FTSE                    |  73.0 |   Yes    | —            | 20d up +2.3%; above MA20 by 2.4%; RSI14=76   |
|    4 | Hang Seng / ^HSI                    |  67.9 |   Yes    | —            | 20d up +12.2%; above MA20 by 4.9%; RSI14=74  |
|    6 | DAX / ^GDAXI                        |  65.8 |   Yes    | —            | 20d up +0.1%; above MA20 by 1.7%; RSI14=64   |
|    7 | CAC 40 / ^FCHI                      |  65.5 |   Yes    | —            | 20d up +0.1%; above MA20 by 1.2%; RSI14=62   |
|    8 | Euro Stoxx 50 / ^STOXX50E           |  63.6 |   Yes    | —            | 20d down -0.3%; above MA20 by 0.9%; RSI14=57 |
|    9 | Dow Jones Industrial Average / ^DJI |  55.8 |   Yes    | —            | 20d down -0.2%; below MA20 by 0.3%; RSI14=46 |
|   12 | S&P 500 / ^GSPC                     |  50.9 |   Yes    | —            | 20d down -0.6%; below MA20 by 0.6%; RSI14=40 |
|   15 | Russell 2000 / ^RUT                 |  49.4 |   Yes    | —            | 20d down -2.2%; below MA20 by 0.6%; RSI14=45 |
|   19 | NASDAQ 100 / ^NDX                   |  37.3 |   Yes    | —            | 20d down -5.7%; below MA20 by 2.6%; RSI14=34 |
|   33 | Nikkei 225 / ^N225                  |  23.6 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-07-30 |
| 7203.T    | 2026-07-30 |
| 8306.T    | 2026-07-30 |
| AAPL      | 2026-07-30 |
| AMZN      | 2026-07-30 |
| BZ=F      | 2026-07-30 |
| CL=F      | 2026-07-30 |
| GC=F      | 2026-07-30 |
| GOOGL     | 2026-07-30 |
| HG=F      | 2026-07-30 |
| JPM       | 2026-07-30 |
| META      | 2026-07-30 |
| MSFT      | 2026-07-30 |
| NG=F      | 2026-07-30 |
| NVDA      | 2026-07-30 |
| PL=F      | 2026-07-30 |
| SI=F      | 2026-07-30 |
| TSLA      | 2026-07-30 |
| UNH       | 2026-07-30 |
| XOM       | 2026-07-30 |
| ZC=F      | 2026-07-30 |
| ZS=F      | 2026-07-30 |
| ZW=F      | 2026-07-30 |
| ^DJI      | 2026-07-30 |
| ^FCHI     | 2026-07-30 |
| ^FTSE     | 2026-07-30 |
| ^GDAXI    | 2026-07-30 |
| ^GSPC     | 2026-07-30 |
| ^HSI      | 2026-07-30 |
| ^N225     | 2026-07-30 |
| ^NDX      | 2026-07-30 |
| ^RUT      | 2026-07-30 |
| ^STOXX50E | 2026-07-30 |

## Symbol Details

### Microsoft Corporation / MSFT (score 77.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     | +15.5% |
| ret_5d     | +18.2% |
| ret_20d    | +17.4% |
| ret_60d    |  +9.3% |
| ma20_dist  | +14.7% |
| ma50_dist  | +13.2% |
| vol_20d    |  58.2% |
| mdd_60d    |  23.4% |
| rsi_14     |   73.6 |
| zscore_20d |    4.0 |

### FTSE 100 / ^FTSE (score 73.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | +2.4% |
| ret_20d    | +2.3% |
| ret_60d    | +4.4% |
| ma20_dist  | +2.4% |
| ma50_dist  | +3.7% |
| vol_20d    | 10.0% |
| mdd_60d    |  2.6% |
| rsi_14     |  76.5 |
| zscore_20d |   1.9 |

### JPMorgan Chase & Co. / JPM (score 70.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.8% |
| ret_5d     |  +0.3% |
| ret_20d    |  +5.5% |
| ret_60d    | +14.6% |
| ma20_dist  |  +2.2% |
| ma50_dist  |  +7.7% |
| vol_20d    |  22.8% |
| mdd_60d    |   6.1% |
| rsi_14     |   62.1 |
| zscore_20d |    1.0 |

### Hang Seng / ^HSI (score 67.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.2% |
| ret_5d     |  +2.6% |
| ret_20d    | +12.2% |
| ret_60d    |  -0.9% |
| ma20_dist  |  +4.9% |
| ma50_dist  |  +5.2% |
| vol_20d    |  18.6% |
| mdd_60d    |  14.9% |
| rsi_14     |   73.6 |
| zscore_20d |    1.7 |

### Apple Inc. / AAPL (score 67.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.4% |
| ret_5d     |  +3.7% |
| ret_20d    | +13.3% |
| ret_60d    | +20.6% |
| ma20_dist  |  +2.8% |
| ma50_dist  |  +7.8% |
| vol_20d    |  28.2% |
| mdd_60d    |  12.7% |
| rsi_14     |   64.4 |
| zscore_20d |    0.9 |

### DAX / ^GDAXI (score 65.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | +3.4% |
| ret_20d    | +0.1% |
| ret_60d    | +3.8% |
| ma20_dist  | +1.7% |
| ma50_dist  | +2.4% |
| vol_20d    | 14.0% |
| mdd_60d    |  4.7% |
| rsi_14     |  63.8 |
| zscore_20d |   1.4 |

### CAC 40 / ^FCHI (score 65.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | +2.2% |
| ret_20d    | +0.1% |
| ret_60d    | +3.5% |
| ma20_dist  | +1.2% |
| ma50_dist  | +1.8% |
| vol_20d    | 12.6% |
| mdd_60d    |  3.0% |
| rsi_14     |  62.0 |
| zscore_20d |   1.5 |

### Euro Stoxx 50 / ^STOXX50E (score 63.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.5% |
| ret_5d     | +2.2% |
| ret_20d    | -0.3% |
| ret_60d    | +8.1% |
| ma20_dist  | +0.9% |
| ma50_dist  | +2.2% |
| vol_20d    | 14.3% |
| mdd_60d    |  3.6% |
| rsi_14     |  57.3 |
| zscore_20d |   1.1 |

### Dow Jones Industrial Average / ^DJI (score 55.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.2% |
| ret_5d     | +1.0% |
| ret_20d    | -0.2% |
| ret_60d    | +6.7% |
| ma20_dist  | -0.3% |
| ma50_dist  | +1.1% |
| vol_20d    | 12.9% |
| mdd_60d    |  3.2% |
| rsi_14     |  45.5 |
| zscore_20d |  -0.4 |

### Wheat / ZW=F (score 53.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.4% |
| ret_5d     |  -4.7% |
| ret_20d    | +12.1% |
| ret_60d    |  +5.4% |
| ma20_dist  |  +1.9% |
| ma50_dist  |  +6.6% |
| vol_20d    |  37.1% |
| mdd_60d    |  14.6% |
| rsi_14     |   59.9 |
| zscore_20d |    0.4 |

### Platinum / PL=F (score 51.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +3.9% |
| ret_5d     |  +3.3% |
| ret_20d    |  +4.0% |
| ret_60d    | -15.2% |
| ma20_dist  |  +2.1% |
| ma50_dist  |  -3.6% |
| vol_20d    |  30.5% |
| mdd_60d    |  29.1% |
| rsi_14     |   55.4 |
| zscore_20d |    1.7 |

### S&P 500 / ^GSPC (score 50.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.7% |
| ret_5d     | +0.4% |
| ret_20d    | -0.6% |
| ret_60d    | +3.3% |
| ma20_dist  | -0.6% |
| ma50_dist  | -0.4% |
| vol_20d    | 11.9% |
| mdd_60d    |  4.5% |
| rsi_14     |  39.7 |
| zscore_20d |  -0.7 |

### Gold / GC=F (score 49.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.6% |
| ret_5d     | +1.3% |
| ret_20d    | +0.8% |
| ret_60d    | -9.3% |
| ma20_dist  | +0.7% |
| ma50_dist  | -2.6% |
| vol_20d    | 21.2% |
| mdd_60d    | 15.6% |
| rsi_14     |  49.7 |
| zscore_20d |   0.6 |

### UnitedHealth Group Inc. / UNH (score 49.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.2% |
| ret_5d     |  -0.5% |
| ret_20d    |  -1.2% |
| ret_60d    | +14.3% |
| ma20_dist  |  -0.8% |
| ma50_dist  |  +3.1% |
| vol_20d    |  25.1% |
| mdd_60d    |   6.1% |
| rsi_14     |   48.1 |
| zscore_20d |   -0.7 |

### Russell 2000 / ^RUT (score 49.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.4% |
| ret_5d     | +0.2% |
| ret_20d    | -2.2% |
| ret_60d    | +5.4% |
| ma20_dist  | -0.6% |
| ma50_dist  | +0.2% |
| vol_20d    | 13.2% |
| mdd_60d    |  4.8% |
| rsi_14     |  44.6 |
| zscore_20d |  -0.7 |

### Corn / ZC=F (score 42.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | -3.9% |
| ret_20d    | +5.9% |
| ret_60d    | -5.9% |
| ma20_dist  | +0.0% |
| ma50_dist  | +2.3% |
| vol_20d    | 27.0% |
| mdd_60d    | 15.7% |
| rsi_14     |  54.9 |
| zscore_20d |   0.0 |

### Brent Crude Oil / BZ=F (score 38.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.9% |
| ret_5d     | -11.6% |
| ret_20d    | +24.4% |
| ret_60d    | -22.2% |
| ma20_dist  |  +4.9% |
| ma50_dist  |  +2.4% |
| vol_20d    |  68.9% |
| mdd_60d    |  36.2% |
| rsi_14     |   62.7 |
| zscore_20d |    0.5 |

### Soybeans / ZS=F (score 38.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | -4.9% |
| ret_20d    | +4.5% |
| ret_60d    | -2.5% |
| ma20_dist  | -2.0% |
| ma50_dist  | +0.8% |
| vol_20d    | 24.9% |
| mdd_60d    |  8.8% |
| rsi_14     |  44.2 |
| zscore_20d |  -1.0 |

### NASDAQ 100 / ^NDX (score 37.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +3.4% |
| ret_5d     | -1.2% |
| ret_20d    | -5.7% |
| ret_60d    | +1.6% |
| ma20_dist  | -2.6% |
| ma50_dist  | -4.4% |
| vol_20d    | 23.4% |
| mdd_60d    | 11.3% |
| rsi_14     |  33.8 |
| zscore_20d |  -1.1 |

### Amazon.com Inc. / AMZN (score 34.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +3.9% |
| ret_5d     |  +0.8% |
| ret_20d    |  -2.6% |
| ret_60d    | -13.4% |
| ma20_dist  |  -2.9% |
| ma50_dist  |  -4.4% |
| vol_20d    |  28.1% |
| mdd_60d    |  17.6% |
| rsi_14     |   40.6 |
| zscore_20d |   -0.9 |

### Silver / SI=F (score 32.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.6% |
| ret_5d     |  +1.8% |
| ret_20d    |  -2.1% |
| ret_60d    | -19.5% |
| ma20_dist  |  +0.4% |
| ma50_dist  |  -9.0% |
| vol_20d    |  38.2% |
| mdd_60d    |  37.1% |
| rsi_14     |   46.9 |
| zscore_20d |    0.1 |

### NVIDIA Corporation / NVDA (score 26.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.6% |
| ret_5d     | -6.6% |
| ret_20d    | -1.3% |
| ret_60d    | -1.7% |
| ma20_dist  | -3.9% |
| ma50_dist  | -5.6% |
| vol_20d    | 40.4% |
| mdd_60d    | 19.4% |
| rsi_14     |  37.4 |
| zscore_20d |  -1.2 |

### Alphabet Inc. Class A / GOOGL (score 24.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.9% |
| ret_5d     |  +5.0% |
| ret_20d    |  -7.6% |
| ret_60d    | -12.9% |
| ma20_dist  |  -4.2% |
| ma50_dist  |  -7.1% |
| vol_20d    |  37.6% |
| mdd_60d    |  21.0% |
| rsi_14     |   39.2 |
| zscore_20d |   -0.9 |

### Natural Gas / NG=F (score 21.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.2% |
| ret_5d     |  -5.4% |
| ret_20d    | -14.3% |
| ret_60d    |  -3.8% |
| ma20_dist  |  -6.1% |
| ma50_dist  | -10.3% |
| vol_20d    |  34.6% |
| mdd_60d    |  20.4% |
| rsi_14     |   36.3 |
| zscore_20d |   -1.1 |

### Tesla Inc. / TSLA (score 15.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +3.5% |
| ret_5d     |  -3.4% |
| ret_20d    | -27.4% |
| ret_60d    | -21.3% |
| ma20_dist  | -16.1% |
| ma50_dist  | -21.3% |
| vol_20d    |  67.4% |
| mdd_60d    |  33.0% |
| rsi_14     |   15.1 |
| zscore_20d |   -1.5 |

### Meta Platforms Inc. / META (score 7.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -8.0% |
| ret_5d     | -11.1% |
| ret_20d    | -12.1% |
| ret_60d    | -11.6% |
| ma20_dist  | -13.4% |
| ma50_dist  | -10.6% |
| vol_20d    |  51.2% |
| mdd_60d    |  20.9% |
| rsi_14     |   13.7 |
| zscore_20d |   -2.3 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Microsoft Corporation / MSFT        |  15.8721 |           3.5% |                 0.17x |       31.7443 |            7.0% |
| FTSE 100 / ^FTSE                    | 111.0430 |           1.0% |                 1.00x |      222.0859 |            2.0% |
| JPMorgan Chase & Co. / JPM          |   8.2707 |           2.4% |                 0.44x |       16.5414 |            4.7% |
| Hang Seng / ^HSI                    | 442.3979 |           1.7% |                 0.54x |      884.7958 |            3.4% |
| Apple Inc. / AAPL                   |   8.0950 |           2.4% |                 0.36x |       16.1900 |            4.9% |
| DAX / ^GDAXI                        | 301.0120 |           1.2% |                 0.71x |      602.0240 |            2.4% |
| CAC 40 / ^FCHI                      |  96.9872 |           1.1% |                 0.80x |      193.9745 |            2.3% |
| Euro Stoxx 50 / ^STOXX50E           |  73.5207 |           1.2% |                 0.70x |      147.0414 |            2.3% |
| Dow Jones Industrial Average / ^DJI | 612.7157 |           1.2% |                 0.78x |     1225.4314 |            2.3% |
| Wheat / ZW=F                        |  24.0357 |           3.6% |                 0.27x |       48.0714 |            7.2% |
| Platinum / PL=F                     |  25.8143 |           1.6% |                 0.33x |       51.6286 |            3.1% |
| S&P 500 / ^GSPC                     |  81.9535 |           1.1% |                 0.84x |      163.9071 |            2.2% |
| Gold / GC=F                         |  63.2714 |           1.5% |                 0.47x |      126.5429 |            3.1% |
| UnitedHealth Group Inc. / UNH       |  14.0107 |           3.3% |                 0.40x |       28.0214 |            6.6% |
| Russell 2000 / ^RUT                 |  36.0285 |           1.2% |                 0.76x |       72.0571 |            2.4% |
| Corn / ZC=F                         |  10.6071 |           2.4% |                 0.37x |       21.2143 |            4.8% |
| Brent Crude Oil / BZ=F              |   5.4857 |           6.2% |                 0.15x |       10.9714 |           12.3% |
| Soybeans / ZS=F                     |  20.2857 |           1.7% |                 0.40x |       40.5714 |            3.4% |
| NASDAQ 100 / ^NDX                   | 605.3256 |           2.2% |                 0.43x |     1210.6512 |            4.3% |
| Amazon.com Inc. / AMZN              |   6.9521 |           3.0% |                 0.36x |       13.9043 |            5.9% |
| Silver / SI=F                       |   1.4894 |           2.5% |                 0.26x |        2.9787 |            5.1% |
| NVIDIA Corporation / NVDA           |   7.7050 |           4.0% |                 0.25x |       15.4100 |            7.9% |
| Alphabet Inc. Class A / GOOGL       |  11.9243 |           3.6% |                 0.27x |       23.8486 |            7.1% |
| Natural Gas / NG=F                  |   0.1015 |           3.7% |                 0.29x |        0.2030 |            7.4% |
| Tesla Inc. / TSLA                   |  16.0500 |           5.2% |                 0.15x |       32.1000 |           10.4% |
| Meta Platforms Inc. / META          |  24.3586 |           4.5% |                 0.20x |       48.7171 |            9.0% |

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

Scoring engine version: **1.0.0** | Git commit: **9e92ef0**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
