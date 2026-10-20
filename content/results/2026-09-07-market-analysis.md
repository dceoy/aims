+++
title = "Market Analysis 2026-09-07"
date = "2026-09-07T00:00:00+00:00"
draft = false
summary = "Bullish market: 26 reliable instruments. Top signal: ZS=F (score 74.2)."
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
source_files = ["data/analysis/2026-09-07.json", "data/history/2026-09-07.json"]
market_regime = "Bullish"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "980c5a8"
+++

## Market Regime

**Bullish** — 17 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Soybeans / ZS=F** — score 74.2, 20d return +12.7%, RSI14=77. 20d up +12.7%; above MA20 by 4.7%; RSI14=77
- **Brent Crude Oil / BZ=F** — score 71.8, 20d return +8.3%, RSI14=64. 20d up +8.3%; above MA20 by 5.3%; RSI14=64
- **Corn / ZC=F** — score 68.2, 20d return +17.2%, RSI14=68. 20d up +17.2%; above MA20 by 4.0%; RSI14=68
- **Meta Platforms Inc. / META** — score 67.3, 20d return +4.2%, RSI14=70. 20d up +4.2%; above MA20 by 6.9%; RSI14=70
- **NVIDIA Corporation / NVDA** — score 65.2, 20d return +2.9%, RSI14=54. 20d up +2.9%; above MA20 by 4.7%; RSI14=54

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                        | Applies To               |
| ---------- | ---------------------------- | ------------------------ |
| 2026-09-10 | ECB monetary policy decision | ^FCHI, ^GDAXI, ^STOXX50E |

## Signal History

Compared with the previous available report (**2026-09-04**).

- **New top-5:** BZ=F, META, NVDA
- **Persistent top signals:** ZC=F (18 reports), ZS=F (11 reports)
- **Dropped from top-5:** AAPL, JPM, MSFT

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +1 |    +5.5 |
| 7203.T    |     -2 |    -9.4 |
| 8306.T    |     +0 |    +3.9 |
| AAPL      |     -7 |   -16.4 |
| AMZN      |     -4 |    -5.5 |
| BZ=F      |     +5 |   +10.3 |
| CL=F      |     +0 |    +5.2 |
| GC=F      |     -4 |   -11.2 |
| GOOGL     |     -1 |   -11.8 |
| HG=F      |     +2 |   +13.0 |
| JPM       |     -6 |   -10.0 |
| META      |     +4 |    +7.9 |
| MSFT      |     -7 |   -14.2 |
| NG=F      |    +10 |   +22.7 |
| NVDA      |     +5 |    +8.2 |
| PL=F      |     +0 |    -4.5 |
| SI=F      |     -6 |    -8.2 |
| TSLA      |    -15 |   -27.0 |
| UNH       |     -3 |    -3.9 |
| XOM       |     -1 |    -7.3 |
| ZC=F      |     +1 |    +1.8 |
| ZS=F      |     +0 |    -3.3 |
| ZW=F      |     -4 |    -7.0 |
| ^DJI      |     -4 |    -7.6 |
| ^FCHI     |     +1 |    +0.0 |
| ^FTSE     |     +6 |    +7.3 |
| ^GDAXI    |     +1 |    +2.4 |
| ^GSPC     |     +0 |    -0.9 |
| ^HSI      |    +16 |   +27.3 |
| ^N225     |     +0 |   +11.8 |
| ^NDX      |     +5 |    +9.7 |
| ^RUT      |     +5 |    +9.1 |
| ^STOXX50E |     +2 |    +2.1 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **WTI Crude Oil / CL=F** — malformed_input
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                 |
| ---: | ---------------------- | ----: | :------: | --------------- | ------------------------------------------- |
|    1 | Soybeans / ZS=F        |  74.2 |   Yes    | —               | 20d up +12.7%; above MA20 by 4.7%; RSI14=77 |
|    2 | Brent Crude Oil / BZ=F |  71.8 |   Yes    | —               | 20d up +8.3%; above MA20 by 5.3%; RSI14=64  |
|    3 | Corn / ZC=F            |  68.2 |   Yes    | —               | 20d up +17.2%; above MA20 by 4.0%; RSI14=68 |
|    6 | Natural Gas / NG=F     |  62.7 |   Yes    | —               | 20d up +7.5%; above MA20 by 5.6%; RSI14=67  |
|   13 | Wheat / ZW=F           |  50.6 |   Yes    | —               | 20d up +13.6%; above MA20 by 1.5%; RSI14=61 |
|   14 | Platinum / PL=F        |  45.5 |   Yes    | —               | 20d up +4.3%; above MA20 by 0.8%; RSI14=62  |
|   19 | Gold / GC=F            |  36.7 |   Yes    | —               | 20d up +1.1%; below MA20 by 1.3%; RSI14=53  |
|   23 | Silver / SI=F          |  30.3 |   Yes    | —               | 20d up +2.0%; below MA20 by 1.0%; RSI14=56  |
|   28 | WTI Crude Oil / CL=F   |  73.6 |    No    | malformed_input | Suppressed: malformed_input                 |
|   30 | Copper / HG=F          |  53.6 |    No    | malformed_input | Suppressed: malformed_input                 |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    4 | Meta Platforms Inc. / META                                                     |  67.3 |   Yes    | —                             | 20d up +4.2%; above MA20 by 6.9%; RSI14=70   |
|    5 | NVIDIA Corporation / NVDA                                                      |  65.2 |   Yes    | —                             | 20d up +2.9%; above MA20 by 4.7%; RSI14=54   |
|    9 | Apple Inc. / AAPL                                                              |  53.6 |   Yes    | —                             | 20d up +2.2%; above MA20 by 2.2%; RSI14=64   |
|   10 | Microsoft Corporation / MSFT                                                   |  53.3 |   Yes    | —                             | 20d up +0.1%; above MA20 by 0.9%; RSI14=63   |
|   11 | JPMorgan Chase & Co. / JPM                                                     |  52.7 |   Yes    | —                             | 20d up +0.3%; above MA20 by 0.1%; RSI14=47   |
|   21 | Tesla Inc. / TSLA                                                              |  35.8 |   Yes    | —                             | 20d up +7.8%; above MA20 by 1.6%; RSI14=55   |
|   22 | UnitedHealth Group Inc. / UNH                                                  |  31.8 |   Yes    | —                             | 20d down -2.4%; above MA20 by 0.1%; RSI14=51 |
|   24 | Amazon.com Inc. / AMZN                                                         |  28.8 |   Yes    | —                             | 20d down -5.8%; below MA20 by 1.4%; RSI14=47 |
|   26 | Alphabet Inc. Class A / GOOGL                                                  |  16.4 |   Yes    | —                             | 20d down -4.4%; below MA20 by 1.4%; RSI14=44 |
|   27 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  74.5 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   29 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  58.8 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   31 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  46.4 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   32 | Exxon Mobil Corporation / XOM                                                  |  44.2 |    No    | malformed_input               | Suppressed: malformed_input                  |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    7 | FTSE 100 / ^FTSE                    |  58.5 |   Yes    | —            | 20d down -0.3%; above MA20 by 0.2%; RSI14=59 |
|    8 | Hang Seng / ^HSI                    |  57.6 |   Yes    | —            | 20d down -0.1%; above MA20 by 0.5%; RSI14=55 |
|   12 | S&P 500 / ^GSPC                     |  51.2 |   Yes    | —            | 20d down -0.5%; above MA20 by 0.1%; RSI14=47 |
|   15 | Dow Jones Industrial Average / ^DJI |  44.9 |   Yes    | —            | 20d down -1.2%; below MA20 by 0.1%; RSI14=49 |
|   16 | NASDAQ 100 / ^NDX                   |  43.9 |   Yes    | —            | 20d down -0.6%; above MA20 by 0.2%; RSI14=42 |
|   17 | DAX / ^GDAXI                        |  40.3 |   Yes    | —            | 20d down -1.0%; below MA20 by 0.6%; RSI14=42 |
|   18 | Russell 2000 / ^RUT                 |  40.3 |   Yes    | —            | 20d down -1.9%; below MA20 by 1.0%; RSI14=37 |
|   20 | Euro Stoxx 50 / ^STOXX50E           |  36.1 |   Yes    | —            | 20d down -2.0%; below MA20 by 1.1%; RSI14=35 |
|   25 | CAC 40 / ^FCHI                      |  27.0 |   Yes    | —            | 20d down -5.0%; below MA20 by 2.3%; RSI14=24 |
|   33 | Nikkei 225 / ^N225                  |  24.2 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-09-04 |
| 7203.T    | 2026-09-04 |
| 8306.T    | 2026-09-04 |
| AAPL      | 2026-09-04 |
| AMZN      | 2026-09-04 |
| BZ=F      | 2026-09-04 |
| CL=F      | 2026-09-04 |
| GC=F      | 2026-09-04 |
| GOOGL     | 2026-09-04 |
| HG=F      | 2026-09-04 |
| JPM       | 2026-09-04 |
| META      | 2026-09-04 |
| MSFT      | 2026-09-04 |
| NG=F      | 2026-09-04 |
| NVDA      | 2026-09-04 |
| PL=F      | 2026-09-04 |
| SI=F      | 2026-09-04 |
| TSLA      | 2026-09-04 |
| UNH       | 2026-09-04 |
| XOM       | 2026-09-04 |
| ZC=F      | 2026-09-04 |
| ZS=F      | 2026-09-04 |
| ZW=F      | 2026-09-04 |
| ^DJI      | 2026-09-04 |
| ^FCHI     | 2026-09-04 |
| ^FTSE     | 2026-09-04 |
| ^GDAXI    | 2026-09-04 |
| ^GSPC     | 2026-09-04 |
| ^HSI      | 2026-09-04 |
| ^N225     | 2026-09-04 |
| ^NDX      | 2026-09-04 |
| ^RUT      | 2026-09-04 |
| ^STOXX50E | 2026-09-04 |

## Symbol Details

### Soybeans / ZS=F (score 74.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.0% |
| ret_5d     |  +1.4% |
| ret_20d    | +12.7% |
| ret_60d    | +15.6% |
| ma20_dist  |  +4.7% |
| ma50_dist  |  +7.2% |
| vol_20d    |  15.8% |
| mdd_60d    |   8.1% |
| rsi_14     |   77.4 |
| zscore_20d |    1.3 |

### Brent Crude Oil / BZ=F (score 71.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.8% |
| ret_5d     |  +7.8% |
| ret_20d    |  +8.3% |
| ret_60d    | +15.8% |
| ma20_dist  |  +5.3% |
| ma50_dist  | +10.5% |
| vol_20d    |  28.2% |
| mdd_60d    |  21.2% |
| rsi_14     |   63.6 |
| zscore_20d |    1.8 |

### Corn / ZC=F (score 68.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.6% |
| ret_5d     |  +0.0% |
| ret_20d    | +17.2% |
| ret_60d    | +23.2% |
| ma20_dist  |  +4.0% |
| ma50_dist  | +10.5% |
| vol_20d    |  47.2% |
| mdd_60d    |   6.0% |
| rsi_14     |   68.2 |
| zscore_20d |    0.8 |

### Meta Platforms Inc. / META (score 67.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.0% |
| ret_5d     | +6.7% |
| ret_20d    | +4.2% |
| ret_60d    | +8.1% |
| ma20_dist  | +6.9% |
| ma50_dist  | +3.6% |
| vol_20d    | 32.0% |
| mdd_60d    | 20.9% |
| rsi_14     |  69.9 |
| zscore_20d |   1.9 |

### NVIDIA Corporation / NVDA (score 65.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.8% |
| ret_5d     |  +5.9% |
| ret_20d    |  +2.9% |
| ret_60d    | +14.9% |
| ma20_dist  |  +4.7% |
| ma50_dist  |  +9.4% |
| vol_20d    |  44.4% |
| mdd_60d    |  10.6% |
| rsi_14     |   53.7 |
| zscore_20d |    1.7 |

### Natural Gas / NG=F (score 62.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.1% |
| ret_5d     | +3.0% |
| ret_20d    | +7.5% |
| ret_60d    | -5.5% |
| ma20_dist  | +5.6% |
| ma50_dist  | +4.2% |
| vol_20d    | 28.1% |
| mdd_60d    | 21.0% |
| rsi_14     |  67.2 |
| zscore_20d |   1.8 |

### FTSE 100 / ^FTSE (score 58.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.0% |
| ret_5d     | +0.4% |
| ret_20d    | -0.3% |
| ret_60d    | +5.1% |
| ma20_dist  | +0.2% |
| ma50_dist  | +1.0% |
| vol_20d    |  5.9% |
| mdd_60d    |  1.9% |
| rsi_14     |  58.7 |
| zscore_20d |   0.4 |

### Hang Seng / ^HSI (score 57.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.7% |
| ret_5d     | +0.3% |
| ret_20d    | -0.1% |
| ret_60d    | +5.1% |
| ma20_dist  | +0.5% |
| ma50_dist  | +2.6% |
| vol_20d    | 14.3% |
| mdd_60d    |  8.7% |
| rsi_14     |  54.7 |
| zscore_20d |   0.6 |

### Apple Inc. / AAPL (score 53.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.5% |
| ret_5d     | +0.1% |
| ret_20d    | +2.2% |
| ret_60d    | +9.7% |
| ma20_dist  | +2.2% |
| ma50_dist  | +1.6% |
| vol_20d    | 20.9% |
| mdd_60d    | 11.0% |
| rsi_14     |  63.6 |
| zscore_20d |   0.9 |

### Microsoft Corporation / MSFT (score 53.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.0% |
| ret_5d     |  -2.7% |
| ret_20d    |  +0.1% |
| ret_60d    | +25.8% |
| ma20_dist  |  +0.9% |
| ma50_dist  | +12.6% |
| vol_20d    |  22.7% |
| mdd_60d    |  11.7% |
| rsi_14     |   62.8 |
| zscore_20d |    0.4 |

### JPMorgan Chase & Co. / JPM (score 52.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.9% |
| ret_5d     |  +0.3% |
| ret_20d    |  +0.3% |
| ret_60d    | +16.5% |
| ma20_dist  |  +0.1% |
| ma50_dist  |  +2.6% |
| vol_20d    |  13.8% |
| mdd_60d    |   3.7% |
| rsi_14     |   47.0 |
| zscore_20d |    0.1 |

### S&P 500 / ^GSPC (score 51.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | +0.1% |
| ret_20d    | -0.5% |
| ret_60d    | +6.2% |
| ma20_dist  | +0.1% |
| ma50_dist  | +1.7% |
| vol_20d    |  8.1% |
| mdd_60d    |  3.4% |
| rsi_14     |  47.4 |
| zscore_20d |   0.2 |

### Wheat / ZW=F (score 50.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.7% |
| ret_5d     |  -6.6% |
| ret_20d    | +13.6% |
| ret_60d    | +21.4% |
| ma20_dist  |  +1.5% |
| ma50_dist  |  +6.9% |
| vol_20d    |  43.4% |
| mdd_60d    |  10.7% |
| rsi_14     |   61.1 |
| zscore_20d |    0.3 |

### Platinum / PL=F (score 45.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -1.4% |
| ret_20d    | +4.3% |
| ret_60d    | +2.9% |
| ma20_dist  | +0.8% |
| ma50_dist  | +6.4% |
| vol_20d    | 31.8% |
| mdd_60d    | 14.5% |
| rsi_14     |  61.8 |
| zscore_20d |   0.3 |

### Dow Jones Industrial Average / ^DJI (score 44.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | -0.3% |
| ret_20d    | -1.2% |
| ret_60d    | +7.0% |
| ma20_dist  | -0.1% |
| ma50_dist  | +0.9% |
| vol_20d    |  9.0% |
| mdd_60d    |  2.9% |
| rsi_14     |  49.4 |
| zscore_20d |  -0.1 |

### NASDAQ 100 / ^NDX (score 43.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | +0.4% |
| ret_20d    | -0.6% |
| ret_60d    | +3.6% |
| ma20_dist  | +0.2% |
| ma50_dist  | +1.1% |
| vol_20d    | 12.6% |
| mdd_60d    | 11.0% |
| rsi_14     |  42.1 |
| zscore_20d |   0.2 |

### DAX / ^GDAXI (score 40.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | -2.0% |
| ret_20d    | -1.0% |
| ret_60d    | +5.7% |
| ma20_dist  | -0.6% |
| ma50_dist  | +1.4% |
| vol_20d    |  8.7% |
| mdd_60d    |  4.1% |
| rsi_14     |  42.5 |
| zscore_20d |  -0.9 |

### Russell 2000 / ^RUT (score 40.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | +0.1% |
| ret_20d    | -1.9% |
| ret_60d    | +4.9% |
| ma20_dist  | -1.0% |
| ma50_dist  | -0.4% |
| vol_20d    | 12.2% |
| mdd_60d    |  4.8% |
| rsi_14     |  37.2 |
| zscore_20d |  -0.8 |

### Gold / GC=F (score 36.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.4% |
| ret_5d     | -1.1% |
| ret_20d    | +1.1% |
| ret_60d    | +2.4% |
| ma20_dist  | -1.3% |
| ma50_dist  | +3.8% |
| vol_20d    | 24.8% |
| mdd_60d    |  8.6% |
| rsi_14     |  53.4 |
| zscore_20d |  -0.5 |

### Euro Stoxx 50 / ^STOXX50E (score 36.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | -1.4% |
| ret_20d    | -2.0% |
| ret_60d    | +3.3% |
| ma20_dist  | -1.1% |
| ma50_dist  | +0.2% |
| vol_20d    |  7.9% |
| mdd_60d    |  3.2% |
| rsi_14     |  34.6 |
| zscore_20d |  -1.2 |

### Tesla Inc. / TSLA (score 35.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -5.9% |
| ret_5d     | +1.5% |
| ret_20d    | +7.8% |
| ret_60d    | -7.2% |
| ma20_dist  | +1.6% |
| ma50_dist  | -1.1% |
| vol_20d    | 49.5% |
| mdd_60d    | 29.9% |
| rsi_14     |  55.0 |
| zscore_20d |   0.5 |

### UnitedHealth Group Inc. / UNH (score 31.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.9% |
| ret_5d     | +1.1% |
| ret_20d    | -2.4% |
| ret_60d    | -2.0% |
| ma20_dist  | +0.1% |
| ma50_dist  | -3.5% |
| vol_20d    | 18.8% |
| mdd_60d    | 11.8% |
| rsi_14     |  51.3 |
| zscore_20d |   0.0 |

### Silver / SI=F (score 30.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.4% |
| ret_5d     | -1.4% |
| ret_20d    | +2.0% |
| ret_60d    | -5.7% |
| ma20_dist  | -1.0% |
| ma50_dist  | +5.8% |
| vol_20d    | 31.7% |
| mdd_60d    | 20.9% |
| rsi_14     |  56.3 |
| zscore_20d |  -0.4 |

### Amazon.com Inc. / AMZN (score 28.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | -3.0% |
| ret_20d    | -5.8% |
| ret_60d    | +8.6% |
| ma20_dist  | -1.4% |
| ma50_dist  | +1.8% |
| vol_20d    | 25.9% |
| mdd_60d    | 11.1% |
| rsi_14     |  47.2 |
| zscore_20d |  -0.7 |

### CAC 40 / ^FCHI (score 27.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | -1.5% |
| ret_20d    | -5.0% |
| ret_60d    | -0.9% |
| ma20_dist  | -2.3% |
| ma50_dist  | -2.1% |
| vol_20d    |  8.3% |
| mdd_60d    |  5.1% |
| rsi_14     |  24.2 |
| zscore_20d |  -1.3 |

### Alphabet Inc. Class A / GOOGL (score 16.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.1% |
| ret_5d     | -2.3% |
| ret_20d    | -4.4% |
| ret_60d    | -5.0% |
| ma20_dist  | -1.4% |
| ma50_dist  | -2.9% |
| vol_20d    | 21.0% |
| mdd_60d    | 14.9% |
| rsi_14     |  44.5 |
| zscore_20d |  -1.1 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Soybeans / ZS=F                     |  20.5536 |           1.6% |                 0.63x |       41.1071 |            3.2% |
| Brent Crude Oil / BZ=F              |   3.2907 |           3.4% |                 0.35x |        6.5814 |            6.8% |
| Corn / ZC=F                         |  15.0000 |           2.9% |                 0.21x |       30.0000 |            5.9% |
| Meta Platforms Inc. / META          |  18.6979 |           3.0% |                 0.31x |       37.3957 |            6.1% |
| NVIDIA Corporation / NVDA           |   7.6193 |           3.3% |                 0.23x |       15.2386 |            6.6% |
| Natural Gas / NG=F                  |   0.1012 |           3.4% |                 0.36x |        0.2024 |            6.8% |
| FTSE 100 / ^FTSE                    |  82.2714 |           0.8% |                 1.71x |      164.5428 |            1.5% |
| Hang Seng / ^HSI                    | 341.1666 |           1.3% |                 0.70x |      682.3331 |            2.7% |
| Apple Inc. / AAPL                   |   7.4314 |           2.3% |                 0.48x |       14.8629 |            4.6% |
| Microsoft Corporation / MSFT        |  10.0813 |           2.0% |                 0.44x |       20.1626 |            4.0% |
| JPMorgan Chase & Co. / JPM          |   5.7264 |           1.6% |                 0.73x |       11.4529 |            3.2% |
| S&P 500 / ^GSPC                     |  55.7114 |           0.7% |                 1.24x |      111.4227 |            1.4% |
| Wheat / ZW=F                        |  26.1250 |           3.6% |                 0.23x |       52.2500 |            7.3% |
| Platinum / PL=F                     |  33.3286 |           1.8% |                 0.31x |       66.6571 |            3.7% |
| Dow Jones Industrial Average / ^DJI | 418.1482 |           0.8% |                 1.11x |      836.2963 |            1.6% |
| NASDAQ 100 / ^NDX                   | 337.7213 |           1.1% |                 0.79x |      675.4425 |            2.3% |
| DAX / ^GDAXI                        | 221.7508 |           0.9% |                 1.15x |      443.5017 |            1.7% |
| Russell 2000 / ^RUT                 |  30.2507 |           1.0% |                 0.82x |       60.5014 |            2.0% |
| Gold / GC=F                         |  86.9358 |           2.0% |                 0.40x |      173.8715 |            3.9% |
| Euro Stoxx 50 / ^STOXX50E           |  52.9442 |           0.8% |                 1.27x |      105.8885 |            1.7% |
| Tesla Inc. / TSLA                   |  15.3371 |           4.3% |                 0.20x |       30.6743 |            8.7% |
| UnitedHealth Group Inc. / UNH       |   7.6129 |           1.9% |                 0.53x |       15.2257 |            3.8% |
| Silver / SI=F                       |   2.1324 |           3.2% |                 0.32x |        4.2647 |            6.5% |
| Amazon.com Inc. / AMZN              |   5.8643 |           2.3% |                 0.39x |       11.7286 |            4.5% |
| CAC 40 / ^FCHI                      |  73.1499 |           0.9% |                 1.20x |      146.2998 |            1.8% |
| Alphabet Inc. Class A / GOOGL       |   6.5968 |           1.9% |                 0.48x |       13.1936 |            3.9% |

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

Scoring engine version: **1.0.0** | Git commit: **980c5a8**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
