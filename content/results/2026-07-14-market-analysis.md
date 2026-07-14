+++
title = "Market Analysis 2026-07-14"
date = "2026-07-14T00:00:00+00:00"
draft = false
summary = "Neutral market: 26 reliable instruments. Top signal: UNH (score 77.9)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-07-14.json", "data/history/2026-07-14.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "b1e00d6"
+++

## Market Regime

**Neutral** — 15 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **UnitedHealth Group Inc. / UNH** — score 77.9, 20d return +6.4%, RSI14=62. 20d up +6.4%; above MA20 by 3.0%; RSI14=62 ⚠️ Upcoming: UNH earnings release (2026-07-16)
- **Soybeans / ZS=F** — score 77.6, 20d return +7.8%, RSI14=75. 20d up +7.8%; above MA20 by 5.2%; RSI14=75
- **Apple Inc. / AAPL** — score 73.6, 20d return +7.3%, RSI14=64. 20d up +7.3%; above MA20 by 6.1%; RSI14=64
- **Dow Jones Industrial Average / ^DJI** — score 70.9, 20d return +3.2%, RSI14=65. 20d up +3.2%; above MA20 by 0.7%; RSI14=65
- **Wheat / ZW=F** — score 67.6, 20d return +6.9%, RSI14=61. 20d up +6.9%; above MA20 by 5.0%; RSI14=61

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                | Applies To |
| ---------- | -------------------- | ---------- |
| 2026-07-16 | UNH earnings release | UNH        |

## Signal History

Compared with the previous available report (**2026-07-13**).
- **New top-5:** AAPL, UNH
- **Persistent top signals:** ZS=F (8 reports), ZW=F (4 reports), ^DJI (2 reports)
- **Dropped from top-5:** JPM, META

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     -1 |    +2.4 |
| 7203.T    |     -1 |    -5.5 |
| 8306.T    |     +0 |    +4.5 |
| AAPL      |     +4 |    +3.9 |
| AMZN      |     +8 |   +14.8 |
| BZ=F      |     +5 |   +27.0 |
| CL=F      |     +2 |   +28.2 |
| GC=F      |     -2 |    -9.4 |
| GOOGL     |     -1 |    -3.9 |
| HG=F      |     -1 |    +1.2 |
| JPM       |     -3 |    -9.4 |
| META      |     -3 |   -10.0 |
| MSFT      |     +4 |   +15.4 |
| NG=F      |     +1 |    +1.8 |
| NVDA      |    -11 |   -26.1 |
| PL=F      |     +0 |    -1.8 |
| SI=F      |     +0 |    -3.6 |
| TSLA      |    -10 |   -32.4 |
| UNH       |     +7 |   +10.9 |
| XOM       |     +4 |   +21.5 |
| ZC=F      |     +1 |    -3.0 |
| ZS=F      |     -1 |    -0.9 |
| ZW=F      |     -3 |    -9.7 |
| ^DJI      |     +1 |    -1.5 |
| ^FCHI     |     +4 |   +11.2 |
| ^FTSE     |     +4 |    +4.5 |
| ^GDAXI    |     +3 |    +5.8 |
| ^GSPC     |     -2 |   -10.3 |
| ^HSI      |     +0 |    +0.0 |
| ^N225     |     -3 |   -10.9 |
| ^NDX      |     -8 |   -18.5 |
| ^RUT      |     -3 |    -5.5 |
| ^STOXX50E |     +5 |    +9.1 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Nikkei 225 / ^N225** — missing_bars

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|    2 | Soybeans / ZS=F        |  77.6 |   Yes    | —               | 20d up +7.8%; above MA20 by 5.2%; RSI14=75   |
|    5 | Wheat / ZW=F           |  67.6 |   Yes    | —               | 20d up +6.9%; above MA20 by 5.0%; RSI14=61   |
|    9 | Corn / ZC=F            |  59.1 |   Yes    | —               | 20d up +6.3%; above MA20 by 4.0%; RSI14=64   |
|   18 | Brent Crude Oil / BZ=F |  47.3 |   Yes    | —               | 20d down -7.8%; above MA20 by 8.6%; RSI14=60 |
|   23 | Natural Gas / NG=F     |  20.6 |   Yes    | —               | 20d down -6.2%; below MA20 by 8.8%; RSI14=33 |
|   24 | Gold / GC=F            |  15.8 |   Yes    | —               | 20d down -2.3%; below MA20 by 3.3%; RSI14=38 |
|   25 | Platinum / PL=F        |  15.8 |   Yes    | —               | 20d down -3.6%; below MA20 by 2.8%; RSI14=43 |
|   26 | Silver / SI=F          |   4.2 |   Yes    | —               | 20d down -9.8%; below MA20 by 7.4%; RSI14=32 |
|   30 | Copper / HG=F          |  47.0 |    No    | malformed_input | Suppressed: malformed_input                  |
|   31 | WTI Crude Oil / CL=F   |  43.3 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    1 | UnitedHealth Group Inc. / UNH                                                  |  77.9 |   Yes    | —                             | 20d up +6.4%; above MA20 by 3.0%; RSI14=62   |
|    3 | Apple Inc. / AAPL                                                              |  73.6 |   Yes    | —                             | 20d up +7.3%; above MA20 by 6.1%; RSI14=64   |
|    6 | JPMorgan Chase & Co. / JPM                                                     |  64.2 |   Yes    | —                             | 20d up +7.2%; above MA20 by 1.2%; RSI14=55   |
|    7 | Meta Platforms Inc. / META                                                     |  63.6 |   Yes    | —                             | 20d up +15.6%; above MA20 by 11.5%; RSI14=69 |
|   10 | Amazon.com Inc. / AMZN                                                         |  57.3 |   Yes    | —                             | 20d up +2.4%; above MA20 by 2.8%; RSI14=68   |
|   17 | Microsoft Corporation / MSFT                                                   |  48.2 |   Yes    | —                             | 20d up +0.2%; above MA20 by 2.7%; RSI14=63   |
|   20 | NVIDIA Corporation / NVDA                                                      |  36.7 |   Yes    | —                             | 20d down -0.7%; above MA20 by 0.8%; RSI14=45 |
|   21 | Alphabet Inc. Class A / GOOGL                                                  |  29.4 |   Yes    | —                             | 20d down -1.5%; below MA20 by 1.4%; RSI14=52 |
|   22 | Tesla Inc. / TSLA                                                              |  21.8 |   Yes    | —                             | 20d down -1.1%; below MA20 by 1.5%; RSI14=47 |
|   27 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  88.5 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   28 | Exxon Mobil Corporation / XOM                                                  |  57.9 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   29 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  48.5 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   32 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  34.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    4 | Dow Jones Industrial Average / ^DJI |  70.9 |   Yes    | —            | 20d up +3.2%; above MA20 by 0.7%; RSI14=65   |
|    8 | S&P 500 / ^GSPC                     |  60.6 |   Yes    | —            | 20d up +1.6%; above MA20 by 0.6%; RSI14=54   |
|   11 | FTSE 100 / ^FTSE                    |  54.9 |   Yes    | —            | 20d up +0.6%; below MA20 by 0.1%; RSI14=55   |
|   12 | Euro Stoxx 50 / ^STOXX50E           |  54.9 |   Yes    | —            | 20d up +0.7%; below MA20 by 0.3%; RSI14=53   |
|   13 | DAX / ^GDAXI                        |  53.9 |   Yes    | —            | 20d up +0.9%; above MA20 by 0.1%; RSI14=53   |
|   14 | Hang Seng / ^HSI                    |  52.7 |   Yes    | —            | 20d down -0.1%; above MA20 by 2.0%; RSI14=56 |
|   15 | CAC 40 / ^FCHI                      |  51.8 |   Yes    | —            | 20d down -0.2%; below MA20 by 0.4%; RSI14=52 |
|   16 | Russell 2000 / ^RUT                 |  48.5 |   Yes    | —            | 20d up +1.1%; below MA20 by 1.0%; RSI14=40   |
|   19 | NASDAQ 100 / ^NDX                   |  38.5 |   Yes    | —            | 20d down -0.6%; below MA20 by 1.4%; RSI14=41 |
|   33 | Nikkei 225 / ^N225                  |  33.3 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-07-13 |
| 7203.T    | 2026-07-13 |
| 8306.T    | 2026-07-13 |
| AAPL      | 2026-07-13 |
| AMZN      | 2026-07-13 |
| BZ=F      | 2026-07-13 |
| CL=F      | 2026-07-13 |
| GC=F      | 2026-07-13 |
| GOOGL     | 2026-07-13 |
| HG=F      | 2026-07-13 |
| JPM       | 2026-07-13 |
| META      | 2026-07-13 |
| MSFT      | 2026-07-13 |
| NG=F      | 2026-07-13 |
| NVDA      | 2026-07-13 |
| PL=F      | 2026-07-13 |
| SI=F      | 2026-07-13 |
| TSLA      | 2026-07-13 |
| UNH       | 2026-07-13 |
| XOM       | 2026-07-13 |
| ZC=F      | 2026-07-13 |
| ZS=F      | 2026-07-13 |
| ZW=F      | 2026-07-13 |
| ^DJI      | 2026-07-13 |
| ^FCHI     | 2026-07-13 |
| ^FTSE     | 2026-07-13 |
| ^GDAXI    | 2026-07-13 |
| ^GSPC     | 2026-07-13 |
| ^HSI      | 2026-07-13 |
| ^N225     | 2026-07-13 |
| ^NDX      | 2026-07-13 |
| ^RUT      | 2026-07-13 |
| ^STOXX50E | 2026-07-13 |

## Symbol Details

### UnitedHealth Group Inc. / UNH (score 77.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.1% |
| ret_5d     |  +2.7% |
| ret_20d    |  +6.4% |
| ret_60d    | +37.4% |
| ma20_dist  |  +3.0% |
| ma50_dist  |  +8.0% |
| vol_20d    |  24.9% |
| mdd_60d    |   6.1% |
| rsi_14     |   62.4 |
| zscore_20d |    1.2 |

### Soybeans / ZS=F (score 77.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | +1.7% |
| ret_20d    | +7.8% |
| ret_60d    | +3.0% |
| ma20_dist  | +5.2% |
| ma50_dist  | +3.4% |
| vol_20d    | 20.1% |
| mdd_60d    |  8.8% |
| rsi_14     |  74.7 |
| zscore_20d |   1.8 |

### Apple Inc. / AAPL (score 73.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.6% |
| ret_5d     |  +1.5% |
| ret_20d    |  +7.3% |
| ret_60d    | +19.2% |
| ma20_dist  |  +6.1% |
| ma50_dist  |  +6.2% |
| vol_20d    |  34.1% |
| mdd_60d    |  12.7% |
| rsi_14     |   63.7 |
| zscore_20d |    1.5 |

### Dow Jones Industrial Average / ^DJI (score 70.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | -1.1% |
| ret_20d    | +3.2% |
| ret_60d    | +8.3% |
| ma20_dist  | +0.7% |
| ma50_dist  | +3.0% |
| vol_20d    |  8.5% |
| mdd_60d    |  3.2% |
| rsi_14     |  64.6 |
| zscore_20d |   0.7 |

### Wheat / ZW=F (score 67.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | +3.5% |
| ret_20d    | +6.9% |
| ret_60d    | +5.6% |
| ma20_dist  | +5.0% |
| ma50_dist  | +2.5% |
| vol_20d    | 26.4% |
| mdd_60d    | 14.6% |
| rsi_14     |  61.5 |
| zscore_20d |   1.9 |

### JPMorgan Chase & Co. / JPM (score 64.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | -0.9% |
| ret_20d    | +7.2% |
| ret_60d    | +9.8% |
| ma20_dist  | +1.2% |
| ma50_dist  | +6.4% |
| vol_20d    | 24.3% |
| mdd_60d    |  6.7% |
| rsi_14     |  55.3 |
| zscore_20d |   0.7 |

### Meta Platforms Inc. / META (score 63.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.9% |
| ret_5d     |  +9.4% |
| ret_20d    | +15.6% |
| ret_60d    |  -2.1% |
| ma20_dist  | +11.5% |
| ma50_dist  |  +9.5% |
| vol_20d    |  55.7% |
| mdd_60d    |  21.1% |
| rsi_14     |   69.0 |
| zscore_20d |    2.0 |

### S&P 500 / ^GSPC (score 60.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | -0.3% |
| ret_20d    | +1.6% |
| ret_60d    | +7.0% |
| ma20_dist  | +0.6% |
| ma50_dist  | +1.0% |
| vol_20d    | 12.5% |
| mdd_60d    |  4.5% |
| rsi_14     |  53.9 |
| zscore_20d |   0.7 |

### Corn / ZC=F (score 59.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | -0.7% |
| ret_20d    | +6.3% |
| ret_60d    | -3.0% |
| ma20_dist  | +4.0% |
| ma50_dist  | -0.2% |
| vol_20d    | 25.9% |
| mdd_60d    | 15.7% |
| rsi_14     |  64.5 |
| zscore_20d |   1.4 |

### Amazon.com Inc. / AMZN (score 57.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.8% |
| ret_5d     | +1.3% |
| ret_20d    | +2.4% |
| ret_60d    | -0.5% |
| ma20_dist  | +2.8% |
| ma50_dist  | -2.5% |
| vol_20d    | 33.3% |
| mdd_60d    | 17.4% |
| rsi_14     |  67.8 |
| zscore_20d |   1.2 |

### FTSE 100 / ^FTSE (score 54.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.0% |
| ret_5d     | -1.4% |
| ret_20d    | +0.6% |
| ret_60d    | -0.9% |
| ma20_dist  | -0.1% |
| ma50_dist  | +0.8% |
| vol_20d    | 10.4% |
| mdd_60d    |  4.4% |
| rsi_14     |  55.4 |
| zscore_20d |  -0.1 |

### Euro Stoxx 50 / ^STOXX50E (score 54.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.0% |
| ret_5d     | -2.0% |
| ret_20d    | +0.7% |
| ret_60d    | +5.6% |
| ma20_dist  | -0.3% |
| ma50_dist  | +2.7% |
| vol_20d    | 14.1% |
| mdd_60d    |  4.9% |
| rsi_14     |  52.9 |
| zscore_20d |  -0.3 |

### DAX / ^GDAXI (score 53.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | -2.7% |
| ret_20d    | +0.9% |
| ret_60d    | +1.7% |
| ma20_dist  | +0.1% |
| ma50_dist  | +1.1% |
| vol_20d    | 15.8% |
| mdd_60d    |  4.7% |
| rsi_14     |  53.4 |
| zscore_20d |   0.1 |

### Hang Seng / ^HSI (score 52.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | +2.5% |
| ret_20d    | -0.1% |
| ret_60d    | -6.4% |
| ma20_dist  | +2.0% |
| ma50_dist  | -2.6% |
| vol_20d    | 20.8% |
| mdd_60d    | 14.9% |
| rsi_14     |  56.1 |
| zscore_20d |   0.8 |

### CAC 40 / ^FCHI (score 51.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | -1.4% |
| ret_20d    | -0.2% |
| ret_60d    | -0.7% |
| ma20_dist  | -0.4% |
| ma50_dist  | +1.4% |
| vol_20d    | 12.5% |
| mdd_60d    |  4.5% |
| rsi_14     |  51.5 |
| zscore_20d |  -0.6 |

### Russell 2000 / ^RUT (score 48.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | -1.9% |
| ret_20d    | +1.1% |
| ret_60d    | +8.8% |
| ma20_dist  | -1.0% |
| ma50_dist  | +1.5% |
| vol_20d    | 13.3% |
| mdd_60d    |  4.8% |
| rsi_14     |  39.7 |
| zscore_20d |  -1.0 |

### Microsoft Corporation / MSFT (score 48.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.5% |
| ret_5d     | +1.1% |
| ret_20d    | +0.2% |
| ret_60d    | -4.7% |
| ma20_dist  | +2.7% |
| ma50_dist  | -2.9% |
| vol_20d    | 36.4% |
| mdd_60d    | 23.4% |
| rsi_14     |  62.7 |
| zscore_20d |   0.9 |

### Brent Crude Oil / BZ=F (score 47.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +9.6% |
| ret_5d     | +15.7% |
| ret_20d    |  -7.8% |
| ret_60d    | -12.3% |
| ma20_dist  |  +8.6% |
| ma50_dist  |  -9.0% |
| vol_20d    |  55.7% |
| mdd_60d    |  39.4% |
| rsi_14     |   59.8 |
| zscore_20d |    1.5 |

### NASDAQ 100 / ^NDX (score 38.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.9% |
| ret_5d     |  -1.5% |
| ret_20d    |  -0.6% |
| ret_60d    | +11.7% |
| ma20_dist  |  -1.4% |
| ma50_dist  |  -0.6% |
| vol_20d    |  26.9% |
| mdd_60d    |   7.0% |
| rsi_14     |   40.8 |
| zscore_20d |   -1.0 |

### NVIDIA Corporation / NVDA (score 36.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -3.5% |
| ret_5d     | +4.1% |
| ret_20d    | -0.7% |
| ret_60d    | +2.3% |
| ma20_dist  | +0.8% |
| ma50_dist  | -2.7% |
| vol_20d    | 36.8% |
| mdd_60d    | 18.3% |
| rsi_14     |  45.4 |
| zscore_20d |   0.3 |

### Alphabet Inc. Class A / GOOGL (score 29.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.3% |
| ret_5d     | -3.8% |
| ret_20d    | -1.5% |
| ret_60d    | +4.6% |
| ma20_dist  | -1.4% |
| ma50_dist  | -5.4% |
| vol_20d    | 31.6% |
| mdd_60d    | 16.2% |
| rsi_14     |  52.4 |
| zscore_20d |  -0.5 |

### Tesla Inc. / TSLA (score 21.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -3.2% |
| ret_5d     | -6.0% |
| ret_20d    | -1.1% |
| ret_60d    | +0.7% |
| ma20_dist  | -1.5% |
| ma50_dist  | -3.6% |
| vol_20d    | 58.4% |
| mdd_60d    | 15.8% |
| rsi_14     |  47.3 |
| zscore_20d |  -0.4 |

### Natural Gas / NG=F (score 20.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.5% |
| ret_5d     | -10.7% |
| ret_20d    |  -6.2% |
| ret_60d    | +11.0% |
| ma20_dist  |  -8.8% |
| ma50_dist  |  -5.8% |
| vol_20d    |  41.0% |
| mdd_60d    |  13.3% |
| rsi_14     |   33.4 |
| zscore_20d |   -2.6 |

### Gold / GC=F (score 15.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.6% |
| ret_5d     |  -3.8% |
| ret_20d    |  -2.3% |
| ret_60d    | -16.7% |
| ma20_dist  |  -3.3% |
| ma50_dist  |  -8.4% |
| vol_20d    |  27.7% |
| mdd_60d    |  17.9% |
| rsi_14     |   37.6 |
| zscore_20d |   -1.3 |

### Platinum / PL=F (score 15.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.0% |
| ret_5d     |  -1.8% |
| ret_20d    |  -3.6% |
| ret_60d    | -24.2% |
| ma20_dist  |  -2.8% |
| ma50_dist  | -12.1% |
| vol_20d    |  41.6% |
| mdd_60d    |  29.1% |
| rsi_14     |   42.5 |
| zscore_20d |   -0.6 |

### Silver / SI=F (score 4.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -3.6% |
| ret_5d     |  -6.9% |
| ret_20d    |  -9.8% |
| ret_60d    | -27.5% |
| ma20_dist  |  -7.4% |
| ma50_dist  | -17.9% |
| vol_20d    |  53.3% |
| mdd_60d    |  35.2% |
| rsi_14     |   32.2 |
| zscore_20d |   -1.1 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| UnitedHealth Group Inc. / UNH       |  10.3550 |           2.4% |                 0.40x |       20.7100 |            4.8% |
| Soybeans / ZS=F                     |  19.5179 |           1.6% |                 0.50x |       39.0357 |            3.2% |
| Apple Inc. / AAPL                   |   9.1229 |           2.9% |                 0.29x |       18.2457 |            5.8% |
| Dow Jones Industrial Average / ^DJI | 548.1367 |           1.0% |                 1.18x |     1096.2734 |            2.1% |
| Wheat / ZW=F                        |  13.9286 |           2.2% |                 0.38x |       27.8571 |            4.4% |
| JPMorgan Chase & Co. / JPM          |   6.7759 |           2.0% |                 0.41x |       13.5518 |            4.1% |
| Meta Platforms Inc. / META          |  27.1957 |           4.1% |                 0.18x |       54.3914 |            8.3% |
| S&P 500 / ^GSPC                     |  84.0472 |           1.1% |                 0.80x |      168.0944 |            2.2% |
| Corn / ZC=F                         |  10.0179 |           2.3% |                 0.39x |       20.0357 |            4.6% |
| Amazon.com Inc. / AMZN              |   7.5750 |           3.1% |                 0.30x |       15.1500 |            6.1% |
| FTSE 100 / ^FTSE                    | 116.4428 |           1.1% |                 0.97x |      232.8856 |            2.2% |
| Euro Stoxx 50 / ^STOXX50E           |  73.6470 |           1.2% |                 0.71x |      147.2940 |            2.3% |
| DAX / ^GDAXI                        | 336.6177 |           1.3% |                 0.63x |      673.2355 |            2.7% |
| Hang Seng / ^HSI                    | 476.1671 |           2.0% |                 0.48x |      952.3343 |            3.9% |
| CAC 40 / ^FCHI                      |  90.6993 |           1.1% |                 0.80x |      181.3986 |            2.2% |
| Russell 2000 / ^RUT                 |  42.5522 |           1.4% |                 0.75x |       85.1044 |            2.9% |
| Microsoft Corporation / MSFT        |  12.3179 |           3.2% |                 0.27x |       24.6357 |            6.3% |
| Brent Crude Oil / BZ=F              |   3.3571 |           4.0% |                 0.18x |        6.7143 |            8.1% |
| NASDAQ 100 / ^NDX                   | 652.7525 |           2.2% |                 0.37x |     1305.5050 |            4.5% |
| NVIDIA Corporation / NVDA           |   6.9229 |           3.4% |                 0.27x |       13.8457 |            6.8% |
| Alphabet Inc. Class A / GOOGL       |  10.0586 |           2.9% |                 0.32x |       20.1171 |            5.7% |
| Tesla Inc. / TSLA                   |  19.8907 |           5.0% |                 0.17x |       39.7814 |           10.1% |
| Natural Gas / NG=F                  |   0.1429 |           4.9% |                 0.24x |        0.2859 |            9.9% |
| Gold / GC=F                         |  83.1214 |           2.1% |                 0.36x |      166.2429 |            4.2% |
| Platinum / PL=F                     |  38.7000 |           2.4% |                 0.24x |       77.4000 |            4.8% |
| Silver / SI=F                       |   2.2837 |           4.0% |                 0.19x |        4.5674 |            7.9% |

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

Scoring engine version: **1.0.0** | Git commit: **b1e00d6**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
