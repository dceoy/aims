+++
title = "Market Analysis 2026-08-20"
date = "2026-08-20T00:00:00+00:00"
draft = false
summary = "Bullish market: 26 reliable instruments. Top signal: ZC=F (score 76.1)."
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
source_files = ["data/analysis/2026-08-20.json", "data/history/2026-08-20.json"]
market_regime = "Bullish"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "7e9ccc3"
+++

## Market Regime

**Bullish** — 20 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Corn / ZC=F** — score 76.1, 20d return +7.6%, RSI14=63. 20d up +7.6%; above MA20 by 10.2%; RSI14=63
- **Gold / GC=F** — score 75.2, 20d return +11.9%, RSI14=82. 20d up +11.9%; above MA20 by 6.7%; RSI14=82
- **Wheat / ZW=F** — score 74.2, 20d return +2.7%, RSI14=62. 20d up +2.7%; above MA20 by 6.2%; RSI14=62
- **Soybeans / ZS=F** — score 70.9, 20d return -0.9%, RSI14=70. 20d down -0.9%; above MA20 by 4.9%; RSI14=70
- **Silver / SI=F** — score 66.7, 20d return +14.7%, RSI14=78. 20d up +14.7%; above MA20 by 7.9%; RSI14=78

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                 | Applies To |
| ---------- | --------------------- | ---------- |
| 2026-08-26 | NVDA earnings release | NVDA       |

## Signal History

Compared with the previous available report (**2026-08-19**).

- **New top-5:** GC=F, SI=F, ZS=F
- **Persistent top signals:** ZC=F (6 reports), ZW=F (4 reports)
- **Dropped from top-5:** JPM, ^GDAXI, ^STOXX50E

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +2 |    -5.5 |
| 7203.T    |     -3 |   -24.9 |
| 8306.T    |     -2 |   -28.2 |
| AAPL      |     +1 |    +9.7 |
| AMZN      |     +9 |   +20.9 |
| BZ=F      |     +0 |    +3.3 |
| CL=F      |     +2 |    -4.5 |
| GC=F      |     +5 |   +10.3 |
| GOOGL     |     +0 |    +1.5 |
| HG=F      |     +5 |    +8.2 |
| JPM       |    -14 |   -26.4 |
| META      |     +0 |    +7.3 |
| MSFT      |     -1 |    +0.0 |
| NG=F      |     -6 |    -1.2 |
| NVDA      |     -8 |    -7.3 |
| PL=F      |    +13 |   +30.6 |
| SI=F      |    +13 |   +28.8 |
| TSLA      |     +5 |   +15.2 |
| UNH       |     +0 |    -8.2 |
| XOM       |     +0 |   -11.2 |
| ZC=F      |     +1 |    +1.8 |
| ZS=F      |     +2 |    +3.6 |
| ZW=F      |     +2 |    +5.8 |
| ^DJI      |     +1 |    +6.4 |
| ^FCHI     |     -6 |    -6.1 |
| ^FTSE     |     -5 |    +1.5 |
| ^GDAXI    |     -7 |   -10.6 |
| ^GSPC     |     +2 |    +9.1 |
| ^HSI      |     +1 |   +11.5 |
| ^N225     |     -4 |   -36.7 |
| ^NDX      |     -2 |    +1.8 |
| ^RUT      |     +5 |   +11.8 |
| ^STOXX50E |    -11 |   -18.5 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Exxon Mobil Corporation / XOM** — malformed_input
- **Copper / HG=F** — malformed_input
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **WTI Crude Oil / CL=F** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Nikkei 225 / ^N225** — missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|    1 | Corn / ZC=F            |  76.1 |   Yes    | —               | 20d up +7.6%; above MA20 by 10.2%; RSI14=63  |
|    2 | Gold / GC=F            |  75.2 |   Yes    | —               | 20d up +11.9%; above MA20 by 6.7%; RSI14=82  |
|    3 | Wheat / ZW=F           |  74.2 |   Yes    | —               | 20d up +2.7%; above MA20 by 6.2%; RSI14=62   |
|    4 | Soybeans / ZS=F        |  70.9 |   Yes    | —               | 20d down -0.9%; above MA20 by 4.9%; RSI14=70 |
|    5 | Silver / SI=F          |  66.7 |   Yes    | —               | 20d up +14.7%; above MA20 by 7.9%; RSI14=78  |
|    6 | Platinum / PL=F        |  65.2 |   Yes    | —               | 20d up +13.8%; above MA20 by 5.8%; RSI14=72  |
|   12 | Brent Crude Oil / BZ=F |  53.0 |   Yes    | —               | 20d down -4.8%; above MA20 by 5.9%; RSI14=70 |
|   23 | Natural Gas / NG=F     |  37.0 |   Yes    | —               | 20d down -3.0%; above MA20 by 2.0%; RSI14=50 |
|   28 | Copper / HG=F          |  40.9 |    No    | malformed_input | Suppressed: malformed_input                  |
|   30 | WTI Crude Oil / CL=F   |  39.7 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                   |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | --------------------------------------------- |
|    9 | Microsoft Corporation / MSFT                                                   |  60.0 |   Yes    | —                             | 20d up +24.1%; above MA20 by 4.6%; RSI14=66   |
|   13 | Amazon.com Inc. / AMZN                                                         |  52.4 |   Yes    | —                             | 20d up +8.6%; above MA20 by 2.7%; RSI14=67    |
|   15 | JPMorgan Chase & Co. / JPM                                                     |  50.3 |   Yes    | —                             | 20d up +2.6%; above MA20 by 0.1%; RSI14=60    |
|   16 | Tesla Inc. / TSLA                                                              |  47.0 |   Yes    | —                             | 20d down -6.1%; above MA20 by 8.2%; RSI14=77  |
|   18 | NVIDIA Corporation / NVDA                                                      |  45.5 |   Yes    | —                             | 20d up +2.6%; above MA20 by 2.4%; RSI14=72    |
|   19 | Apple Inc. / AAPL                                                              |  43.9 |   Yes    | —                             | 20d down -2.7%; above MA20 by 0.3%; RSI14=38  |
|   24 | Alphabet Inc. Class A / GOOGL                                                  |  30.3 |   Yes    | —                             | 20d up +0.8%; below MA20 by 0.4%; RSI14=56    |
|   25 | UnitedHealth Group Inc. / UNH                                                  |  19.7 |   Yes    | —                             | 20d down -9.9%; below MA20 by 5.1%; RSI14=25  |
|   26 | Meta Platforms Inc. / META                                                     |  13.9 |   Yes    | —                             | 20d down -12.9%; below MA20 by 6.1%; RSI14=52 |
|   27 | Exxon Mobil Corporation / XOM                                                  |  69.1 |    No    | malformed_input               | Suppressed: malformed_input                   |
|   29 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  40.6 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars     |
|   31 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  29.7 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars     |
|   33 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  23.3 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars     |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                |
| ---: | ----------------------------------- | ----: | :------: | ------------ | ------------------------------------------ |
|    7 | S&P 500 / ^GSPC                     |  64.2 |   Yes    | —            | 20d up +2.8%; above MA20 by 1.2%; RSI14=73 |
|    8 | Russell 2000 / ^RUT                 |  61.2 |   Yes    | —            | 20d up +2.5%; above MA20 by 1.2%; RSI14=63 |
|   10 | Dow Jones Industrial Average / ^DJI |  59.1 |   Yes    | —            | 20d up +2.4%; above MA20 by 0.5%; RSI14=67 |
|   11 | DAX / ^GDAXI                        |  58.5 |   Yes    | —            | 20d up +3.7%; above MA20 by 0.6%; RSI14=66 |
|   14 | Euro Stoxx 50 / ^STOXX50E           |  51.8 |   Yes    | —            | 20d up +2.0%; above MA20 by 0.2%; RSI14=64 |
|   17 | NASDAQ 100 / ^NDX                   |  46.1 |   Yes    | —            | 20d up +1.5%; above MA20 by 1.3%; RSI14=68 |
|   20 | CAC 40 / ^FCHI                      |  42.7 |   Yes    | —            | 20d up +0.8%; below MA20 by 0.7%; RSI14=52 |
|   21 | FTSE 100 / ^FTSE                    |  42.4 |   Yes    | —            | 20d up +0.2%; below MA20 by 0.7%; RSI14=27 |
|   22 | Hang Seng / ^HSI                    |  42.1 |   Yes    | —            | 20d up +2.4%; below MA20 by 0.3%; RSI14=42 |
|   32 | Nikkei 225 / ^N225                  |  27.3 |    No    | missing_bars | Suppressed: missing_bars                   |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-08-19 |
| 7203.T    | 2026-08-19 |
| 8306.T    | 2026-08-19 |
| AAPL      | 2026-08-19 |
| AMZN      | 2026-08-19 |
| BZ=F      | 2026-08-19 |
| CL=F      | 2026-08-19 |
| GC=F      | 2026-08-19 |
| GOOGL     | 2026-08-19 |
| HG=F      | 2026-08-19 |
| JPM       | 2026-08-19 |
| META      | 2026-08-19 |
| MSFT      | 2026-08-19 |
| NG=F      | 2026-08-19 |
| NVDA      | 2026-08-19 |
| PL=F      | 2026-08-19 |
| SI=F      | 2026-08-19 |
| TSLA      | 2026-08-19 |
| UNH       | 2026-08-19 |
| XOM       | 2026-08-19 |
| ZC=F      | 2026-08-19 |
| ZS=F      | 2026-08-19 |
| ZW=F      | 2026-08-19 |
| ^DJI      | 2026-08-19 |
| ^FCHI     | 2026-08-19 |
| ^FTSE     | 2026-08-19 |
| ^GDAXI    | 2026-08-19 |
| ^GSPC     | 2026-08-19 |
| ^HSI      | 2026-08-19 |
| ^N225     | 2026-08-19 |
| ^NDX      | 2026-08-19 |
| ^RUT      | 2026-08-19 |
| ^STOXX50E | 2026-08-19 |

## Symbol Details

### Corn / ZC=F (score 76.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +7.9% |
| ret_5d     | +11.6% |
| ret_20d    |  +7.6% |
| ret_60d    | +10.4% |
| ma20_dist  | +10.2% |
| ma50_dist  | +13.8% |
| vol_20d    |  53.5% |
| mdd_60d    |  11.8% |
| rsi_14     |   63.2 |
| zscore_20d |    2.9 |

### Gold / GC=F (score 75.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +4.3% |
| ret_5d     |  +4.3% |
| ret_20d    | +11.9% |
| ret_60d    |  +2.4% |
| ma20_dist  |  +6.7% |
| ma50_dist  |  +9.2% |
| vol_20d    |  23.9% |
| mdd_60d    |  12.6% |
| rsi_14     |   81.6 |
| zscore_20d |    1.8 |

### Wheat / ZW=F (score 74.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +4.8% |
| ret_5d     |  +6.7% |
| ret_20d    |  +2.7% |
| ret_60d    | +11.8% |
| ma20_dist  |  +6.2% |
| ma50_dist  |  +9.7% |
| vol_20d    |  35.7% |
| mdd_60d    |  10.7% |
| rsi_14     |   62.1 |
| zscore_20d |    2.3 |

### Soybeans / ZS=F (score 70.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +3.0% |
| ret_5d     | +5.8% |
| ret_20d    | -0.9% |
| ret_60d    | +4.3% |
| ma20_dist  | +4.9% |
| ma50_dist  | +5.7% |
| vol_20d    | 23.6% |
| mdd_60d    |  8.1% |
| rsi_14     |  69.6 |
| zscore_20d |   2.5 |

### Silver / SI=F (score 66.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +5.2% |
| ret_5d     |  +3.7% |
| ret_20d    | +14.7% |
| ret_60d    |  -9.8% |
| ma20_dist  |  +7.9% |
| ma50_dist  |  +9.3% |
| vol_20d    |  33.7% |
| mdd_60d    |  26.1% |
| rsi_14     |   77.7 |
| zscore_20d |    1.5 |

### Platinum / PL=F (score 65.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +5.0% |
| ret_5d     |  +5.1% |
| ret_20d    | +13.8% |
| ret_60d    |  -5.5% |
| ma20_dist  |  +5.8% |
| ma50_dist  |  +8.6% |
| vol_20d    |  39.7% |
| mdd_60d    |  20.0% |
| rsi_14     |   72.1 |
| zscore_20d |    1.6 |

### S&P 500 / ^GSPC (score 64.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | -0.5% |
| ret_20d    | +2.8% |
| ret_60d    | +3.1% |
| ma20_dist  | +1.2% |
| ma50_dist  | +2.4% |
| vol_20d    | 13.2% |
| mdd_60d    |  4.5% |
| rsi_14     |  72.6 |
| zscore_20d |   0.6 |

### Russell 2000 / ^RUT (score 61.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | -0.4% |
| ret_20d    | +2.5% |
| ret_60d    | +5.7% |
| ma20_dist  | +1.2% |
| ma50_dist  | +1.8% |
| vol_20d    | 14.6% |
| mdd_60d    |  3.9% |
| rsi_14     |  63.5 |
| zscore_20d |   0.7 |

### Microsoft Corporation / MSFT (score 60.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.6% |
| ret_5d     |  -1.6% |
| ret_20d    | +24.1% |
| ret_60d    | +15.7% |
| ma20_dist  |  +4.6% |
| ma50_dist  | +16.3% |
| vol_20d    |  59.8% |
| mdd_60d    |  23.4% |
| rsi_14     |   65.9 |
| zscore_20d |    0.5 |

### Dow Jones Industrial Average / ^DJI (score 59.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | -0.6% |
| ret_20d    | +2.4% |
| ret_60d    | +5.7% |
| ma20_dist  | +0.5% |
| ma50_dist  | +1.9% |
| vol_20d    | 13.7% |
| mdd_60d    |  3.2% |
| rsi_14     |  66.9 |
| zscore_20d |   0.3 |

### DAX / ^GDAXI (score 58.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | -0.9% |
| ret_20d    | +3.7% |
| ret_60d    | +3.6% |
| ma20_dist  | +0.6% |
| ma50_dist  | +2.8% |
| vol_20d    | 11.0% |
| mdd_60d    |  4.1% |
| rsi_14     |  65.8 |
| zscore_20d |   0.3 |

### Brent Crude Oil / BZ=F (score 53.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.2% |
| ret_5d     |  +5.8% |
| ret_20d    |  -4.8% |
| ret_60d    |  -2.3% |
| ma20_dist  |  +5.9% |
| ma50_dist  | +10.2% |
| vol_20d    |  60.6% |
| mdd_60d    |  26.8% |
| rsi_14     |   69.9 |
| zscore_20d |    1.4 |

### Amazon.com Inc. / AMZN (score 52.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.5% |
| ret_5d     | -0.5% |
| ret_20d    | +8.6% |
| ret_60d    | -0.2% |
| ma20_dist  | +2.7% |
| ma50_dist  | +6.8% |
| vol_20d    | 63.3% |
| mdd_60d    | 17.3% |
| rsi_14     |  66.6 |
| zscore_20d |   0.4 |

### Euro Stoxx 50 / ^STOXX50E (score 51.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -1.4% |
| ret_20d    | +2.0% |
| ret_60d    | +6.2% |
| ma20_dist  | +0.2% |
| ma50_dist  | +1.7% |
| vol_20d    | 11.4% |
| mdd_60d    |  3.2% |
| rsi_14     |  64.1 |
| zscore_20d |   0.1 |

### JPMorgan Chase & Co. / JPM (score 50.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.6% |
| ret_5d     |  -2.2% |
| ret_20d    |  +2.6% |
| ret_60d    | +17.1% |
| ma20_dist  |  +0.1% |
| ma50_dist  |  +4.5% |
| vol_20d    |  17.9% |
| mdd_60d    |   3.5% |
| rsi_14     |   59.8 |
| zscore_20d |    0.0 |

### Tesla Inc. / TSLA (score 47.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +4.2% |
| ret_5d     |  +7.2% |
| ret_20d    |  -6.1% |
| ret_60d    | -17.6% |
| ma20_dist  |  +8.2% |
| ma50_dist  |  -4.4% |
| vol_20d    |  61.7% |
| mdd_60d    |  32.5% |
| rsi_14     |   76.6 |
| zscore_20d |    2.0 |

### NASDAQ 100 / ^NDX (score 46.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | -1.1% |
| ret_20d    | +1.5% |
| ret_60d    | -0.2% |
| ma20_dist  | +1.3% |
| ma50_dist  | +0.4% |
| vol_20d    | 23.3% |
| mdd_60d    | 11.3% |
| rsi_14     |  67.6 |
| zscore_20d |   0.4 |

### NVIDIA Corporation / NVDA (score 45.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | -2.9% |
| ret_20d    | +2.6% |
| ret_60d    | +1.0% |
| ma20_dist  | +2.4% |
| ma50_dist  | +5.0% |
| vol_20d    | 37.6% |
| mdd_60d    | 15.3% |
| rsi_14     |  71.9 |
| zscore_20d |   0.5 |

### Apple Inc. / AAPL (score 43.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.2% |
| ret_5d     | +4.8% |
| ret_20d    | -2.7% |
| ret_60d    | +2.6% |
| ma20_dist  | +0.3% |
| ma50_dist  | +2.4% |
| vol_20d    | 34.1% |
| mdd_60d    | 12.7% |
| rsi_14     |  37.6 |
| zscore_20d |   0.1 |

### CAC 40 / ^FCHI (score 42.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | -2.0% |
| ret_20d    | +0.8% |
| ret_60d    | +3.6% |
| ma20_dist  | -0.7% |
| ma50_dist  | +0.5% |
| vol_20d    | 10.5% |
| mdd_60d    |  3.0% |
| rsi_14     |  51.8 |
| zscore_20d |  -0.5 |

### FTSE 100 / ^FTSE (score 42.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | -0.8% |
| ret_20d    | +0.2% |
| ret_60d    | +2.3% |
| ma20_dist  | -0.7% |
| ma50_dist  | +1.0% |
| vol_20d    |  6.4% |
| mdd_60d    |  1.9% |
| rsi_14     |  26.5 |
| zscore_20d |  -1.0 |

### Hang Seng / ^HSI (score 42.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | +0.2% |
| ret_20d    | +2.4% |
| ret_60d    | -0.4% |
| ma20_dist  | -0.3% |
| ma50_dist  | +3.4% |
| vol_20d    | 14.4% |
| mdd_60d    | 12.9% |
| rsi_14     |  42.3 |
| zscore_20d |  -0.2 |

### Natural Gas / NG=F (score 37.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +2.1% |
| ret_20d    | -3.0% |
| ret_60d    | -8.4% |
| ma20_dist  | +2.0% |
| ma50_dist  | -5.4% |
| vol_20d    | 34.1% |
| mdd_60d    | 21.0% |
| rsi_14     |  50.3 |
| zscore_20d |   1.1 |

### Alphabet Inc. Class A / GOOGL (score 30.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | +0.3% |
| ret_20d    | +0.8% |
| ret_60d    | -9.9% |
| ma20_dist  | -0.4% |
| ma50_dist  | -2.2% |
| vol_20d    | 46.0% |
| mdd_60d    | 18.5% |
| rsi_14     |  56.1 |
| zscore_20d |  -0.1 |

### UnitedHealth Group Inc. / UNH (score 19.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.4% |
| ret_5d     | -4.2% |
| ret_20d    | -9.9% |
| ret_60d    | +0.6% |
| ma20_dist  | -5.1% |
| ma50_dist  | -6.2% |
| vol_20d    | 20.6% |
| mdd_60d    | 10.9% |
| rsi_14     |  25.4 |
| zscore_20d |  -2.0 |

### Meta Platforms Inc. / META (score 13.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.4% |
| ret_5d     |  -5.7% |
| ret_20d    | -12.9% |
| ret_60d    | -10.4% |
| ma20_dist  |  -6.1% |
| ma50_dist  |  -8.1% |
| vol_20d    |  46.5% |
| mdd_60d    |  20.9% |
| rsi_14     |   52.3 |
| zscore_20d |   -1.8 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Corn / ZC=F                         |  16.6071 |           3.3% |                 0.19x |       33.2143 |            6.6% |
| Gold / GC=F                         |  93.1715 |           2.0% |                 0.42x |      186.3429 |            4.1% |
| Wheat / ZW=F                        |  21.8036 |           3.1% |                 0.28x |       43.6071 |            6.3% |
| Soybeans / ZS=F                     |  17.5893 |           1.4% |                 0.42x |       35.1786 |            2.8% |
| Silver / SI=F                       |   1.6560 |           2.5% |                 0.30x |        3.3120 |            4.9% |
| Platinum / PL=F                     |  34.7500 |           1.9% |                 0.25x |       69.5000 |            3.8% |
| S&P 500 / ^GSPC                     |  66.8993 |           0.9% |                 0.76x |      133.7986 |            1.7% |
| Russell 2000 / ^RUT                 |  32.8881 |           1.1% |                 0.69x |       65.7762 |            2.2% |
| Microsoft Corporation / MSFT        |  12.8007 |           2.6% |                 0.17x |       25.6014 |            5.3% |
| Dow Jones Industrial Average / ^DJI | 470.4049 |           0.9% |                 0.73x |      940.8097 |            1.8% |
| DAX / ^GDAXI                        | 243.6678 |           0.9% |                 0.91x |      487.3357 |            1.9% |
| Brent Crude Oil / BZ=F              |   2.9936 |           3.2% |                 0.16x |        5.9871 |            6.5% |
| Amazon.com Inc. / AMZN              |   9.4571 |           3.6% |                 0.16x |       18.9143 |            7.1% |
| Euro Stoxx 50 / ^STOXX50E           |  53.5622 |           0.8% |                 0.88x |      107.1244 |            1.7% |
| JPMorgan Chase & Co. / JPM          |   5.4904 |           1.5% |                 0.56x |       10.9807 |            3.1% |
| Tesla Inc. / TSLA                   |  11.0957 |           3.2% |                 0.16x |       22.1914 |            6.3% |
| NASDAQ 100 / ^NDX                   | 449.4015 |           1.5% |                 0.43x |      898.8030 |            3.1% |
| NVIDIA Corporation / NVDA           |   6.5007 |           3.0% |                 0.27x |       13.0014 |            6.0% |
| Apple Inc. / AAPL                   |   8.3600 |           2.6% |                 0.29x |       16.7201 |            5.3% |
| CAC 40 / ^FCHI                      |  63.9878 |           0.8% |                 0.95x |      127.9756 |            1.5% |
| FTSE 100 / ^FTSE                    |  85.1143 |           0.8% |                 1.57x |      170.2287 |            1.6% |
| Hang Seng / ^HSI                    | 329.5771 |           1.3% |                 0.69x |      659.1543 |            2.6% |
| Natural Gas / NG=F                  |   0.0797 |           2.9% |                 0.29x |        0.1594 |            5.7% |
| Alphabet Inc. Class A / GOOGL       |  10.6871 |           3.1% |                 0.22x |       21.3743 |            6.2% |
| UnitedHealth Group Inc. / UNH       |   9.3471 |           2.4% |                 0.48x |       18.6943 |            4.8% |
| Meta Platforms Inc. / META          |  19.7900 |           3.6% |                 0.21x |       39.5800 |            7.2% |

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

Scoring engine version: **1.0.0** | Git commit: **7e9ccc3**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
