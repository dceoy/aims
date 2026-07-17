+++
title = "Market Analysis 2026-07-17"
date = "2026-07-17T00:00:00+00:00"
draft = false
summary = "Neutral market: 26 reliable instruments. Top signal: AAPL (score 82.4)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-07-17.json", "data/history/2026-07-17.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "383bacf"
+++

## Market Regime

**Neutral** — 16 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Apple Inc. / AAPL** — score 82.4, 20d return +11.4%, RSI14=90. 20d up +11.4%; above MA20 by 9.8%; RSI14=90
- **Wheat / ZW=F** — score 77.9, 20d return +13.2%, RSI14=75. 20d up +13.2%; above MA20 by 11.0%; RSI14=75
- **Hang Seng / ^HSI** — score 67.3, 20d return +2.1%, RSI14=77. 20d up +2.1%; above MA20 by 5.4%; RSI14=77
- **JPMorgan Chase & Co. / JPM** — score 64.8, 20d return +4.1%, RSI14=59. 20d up +4.1%; above MA20 by 2.8%; RSI14=59
- **Soybeans / ZS=F** — score 63.0, 20d return +5.8%, RSI14=71. 20d up +5.8%; above MA20 by 3.5%; RSI14=71

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                        | Applies To               |
| ---------- | ---------------------------- | ------------------------ |
| 2026-07-22 | TSLA earnings release        | TSLA                     |
| 2026-07-23 | ECB monetary policy decision | ^FCHI, ^GDAXI, ^STOXX50E |
| 2026-07-23 | GOOGL earnings release       | GOOGL                    |

## Signal History

Compared with the previous available report (**2026-07-16**).
- **New top-5:** ZS=F, ^HSI
- **Persistent top signals:** ZW=F (7 reports), AAPL (2 reports), JPM (2 reports)
- **Dropped from top-5:** META, ZC=F

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +4 |   +17.9 |
| 7203.T    |     +1 |   +13.3 |
| 8306.T    |     +0 |    -7.0 |
| AAPL      |     +1 |    +6.7 |
| AMZN      |    -11 |   -17.9 |
| BZ=F      |     +0 |    +0.0 |
| CL=F      |     +0 |    +1.5 |
| GC=F      |     +0 |    +0.6 |
| GOOGL     |    -11 |   -28.5 |
| HG=F      |     -2 |    +5.5 |
| JPM       |     -1 |    -9.1 |
| META      |     -7 |   -12.4 |
| MSFT      |    +10 |   +15.2 |
| NG=F      |     -3 |    -5.8 |
| NVDA      |     -6 |   -12.7 |
| PL=F      |     +1 |    +3.0 |
| SI=F      |     +0 |    +1.2 |
| TSLA      |     +2 |    +3.3 |
| UNH       |     +5 |    +8.8 |
| XOM       |     +0 |   +13.0 |
| ZC=F      |     -8 |   -10.9 |
| ZS=F      |     +3 |    +2.1 |
| ZW=F      |     -1 |    -5.8 |
| ^DJI      |     +3 |    +0.9 |
| ^FCHI     |     +1 |    +3.3 |
| ^FTSE     |    +11 |   +13.0 |
| ^GDAXI    |     +2 |    +3.0 |
| ^GSPC     |     -1 |    -5.2 |
| ^HSI      |     +9 |   +16.7 |
| ^N225     |     -3 |   -16.1 |
| ^NDX      |     +1 |    -5.2 |
| ^RUT      |     -5 |    -0.9 |
| ^STOXX50E |     +5 |    +8.2 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|    2 | Wheat / ZW=F           |  77.9 |   Yes    | —               | 20d up +13.2%; above MA20 by 11.0%; RSI14=75  |
|    5 | Soybeans / ZS=F        |  63.0 |   Yes    | —               | 20d up +5.8%; above MA20 by 3.5%; RSI14=71    |
|   13 | Corn / ZC=F            |  53.6 |   Yes    | —               | 20d up +6.7%; above MA20 by 3.9%; RSI14=63    |
|   14 | Brent Crude Oil / BZ=F |  50.0 |   Yes    | —               | 20d up +6.7%; above MA20 by 9.5%; RSI14=69    |
|   22 | Platinum / PL=F        |  26.1 |   Yes    | —               | 20d down -9.7%; above MA20 by 0.4%; RSI14=54  |
|   24 | Gold / GC=F            |  20.0 |   Yes    | —               | 20d down -8.0%; below MA20 by 2.7%; RSI14=47  |
|   25 | Natural Gas / NG=F     |  17.3 |   Yes    | —               | 20d down -11.8%; below MA20 by 8.8%; RSI14=22 |
|   26 | Silver / SI=F          |   5.8 |   Yes    | —               | 20d down -20.0%; below MA20 by 7.5%; RSI14=43 |
|   31 | Copper / HG=F          |  51.8 |    No    | malformed_input | Suppressed: malformed_input                   |
|   32 | WTI Crude Oil / CL=F   |  45.5 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    1 | Apple Inc. / AAPL                                                              |  82.4 |   Yes    | —                             | 20d up +11.4%; above MA20 by 9.8%; RSI14=90  |
|    4 | JPMorgan Chase & Co. / JPM                                                     |  64.8 |   Yes    | —                             | 20d up +4.1%; above MA20 by 2.8%; RSI14=59   |
|    9 | Microsoft Corporation / MSFT                                                   |  57.3 |   Yes    | —                             | 20d up +1.8%; above MA20 by 5.4%; RSI14=78   |
|   10 | UnitedHealth Group Inc. / UNH                                                  |  57.3 |   Yes    | —                             | 20d up +3.9%; above MA20 by 1.1%; RSI14=54   |
|   11 | Meta Platforms Inc. / META                                                     |  56.4 |   Yes    | —                             | 20d up +10.7%; above MA20 by 10.5%; RSI14=73 |
|   17 | Amazon.com Inc. / AMZN                                                         |  45.8 |   Yes    | —                             | 20d up +1.6%; above MA20 by 3.4%; RSI14=76   |
|   19 | NVIDIA Corporation / NVDA                                                      |  37.6 |   Yes    | —                             | 20d down -0.0%; above MA20 by 2.6%; RSI14=60 |
|   21 | Alphabet Inc. Class A / GOOGL                                                  |  27.0 |   Yes    | —                             | 20d down -5.0%; below MA20 by 0.6%; RSI14=56 |
|   23 | Tesla Inc. / TSLA                                                              |  21.8 |   Yes    | —                             | 20d down -3.4%; below MA20 by 1.9%; RSI14=55 |
|   27 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  78.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   28 | Exxon Mobil Corporation / XOM                                                  |  60.6 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   29 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  59.1 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   30 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  57.6 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    3 | Hang Seng / ^HSI                    |  67.3 |   Yes    | —            | 20d up +2.1%; above MA20 by 5.4%; RSI14=77   |
|    6 | Dow Jones Industrial Average / ^DJI |  60.9 |   Yes    | —            | 20d up +1.1%; above MA20 by 0.5%; RSI14=62   |
|    7 | FTSE 100 / ^FTSE                    |  58.5 |   Yes    | —            | 20d up +1.7%; above MA20 by 0.5%; RSI14=55   |
|    8 | S&P 500 / ^GSPC                     |  57.6 |   Yes    | —            | 20d up +0.3%; above MA20 by 0.8%; RSI14=67   |
|   12 | Euro Stoxx 50 / ^STOXX50E           |  54.2 |   Yes    | —            | 20d down -0.6%; below MA20 by 0.0%; RSI14=55 |
|   15 | CAC 40 / ^FCHI                      |  50.0 |   Yes    | —            | 20d down -1.1%; below MA20 by 0.1%; RSI14=49 |
|   16 | Russell 2000 / ^RUT                 |  50.0 |   Yes    | —            | 20d up +1.2%; below MA20 by 0.4%; RSI14=42   |
|   18 | DAX / ^GDAXI                        |  43.3 |   Yes    | —            | 20d down -0.4%; below MA20 by 0.7%; RSI14=54 |
|   20 | NASDAQ 100 / ^NDX                   |  32.7 |   Yes    | —            | 20d down -3.1%; below MA20 by 1.9%; RSI14=46 |
|   33 | Nikkei 225 / ^N225                  |  28.8 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-07-16 |
| 7203.T    | 2026-07-16 |
| 8306.T    | 2026-07-16 |
| AAPL      | 2026-07-16 |
| AMZN      | 2026-07-16 |
| BZ=F      | 2026-07-16 |
| CL=F      | 2026-07-16 |
| GC=F      | 2026-07-16 |
| GOOGL     | 2026-07-16 |
| HG=F      | 2026-07-16 |
| JPM       | 2026-07-16 |
| META      | 2026-07-16 |
| MSFT      | 2026-07-16 |
| NG=F      | 2026-07-16 |
| NVDA      | 2026-07-16 |
| PL=F      | 2026-07-16 |
| SI=F      | 2026-07-16 |
| TSLA      | 2026-07-16 |
| UNH       | 2026-07-16 |
| XOM       | 2026-07-16 |
| ZC=F      | 2026-07-16 |
| ZS=F      | 2026-07-16 |
| ZW=F      | 2026-07-16 |
| ^DJI      | 2026-07-16 |
| ^FCHI     | 2026-07-16 |
| ^FTSE     | 2026-07-16 |
| ^GDAXI    | 2026-07-16 |
| ^GSPC     | 2026-07-16 |
| ^HSI      | 2026-07-16 |
| ^N225     | 2026-07-16 |
| ^NDX      | 2026-07-16 |
| ^RUT      | 2026-07-16 |
| ^STOXX50E | 2026-07-16 |

## Symbol Details

### Apple Inc. / AAPL (score 82.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.8% |
| ret_5d     |  +5.4% |
| ret_20d    | +11.4% |
| ret_60d    | +22.2% |
| ma20_dist  |  +9.8% |
| ma50_dist  | +10.5% |
| vol_20d    |  35.8% |
| mdd_60d    |  12.7% |
| rsi_14     |   89.9 |
| zscore_20d |    2.0 |

### Wheat / ZW=F (score 77.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.4% |
| ret_5d     | +10.4% |
| ret_20d    | +13.2% |
| ret_60d    | +13.0% |
| ma20_dist  | +11.0% |
| ma50_dist  | +10.0% |
| vol_20d    |  35.8% |
| mdd_60d    |  14.6% |
| rsi_14     |   75.4 |
| zscore_20d |    2.4 |

### Hang Seng / ^HSI (score 67.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.3% |
| ret_5d     | +4.1% |
| ret_20d    | +2.1% |
| ret_60d    | -4.4% |
| ma20_dist  | +5.4% |
| ma50_dist  | +0.9% |
| vol_20d    | 20.2% |
| mdd_60d    | 14.9% |
| rsi_14     |  76.8 |
| zscore_20d |   2.1 |

### JPMorgan Chase & Co. / JPM (score 64.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.1% |
| ret_5d     | +2.3% |
| ret_20d    | +4.1% |
| ret_60d    | +8.7% |
| ma20_dist  | +2.8% |
| ma50_dist  | +8.4% |
| vol_20d    | 22.0% |
| mdd_60d    |  6.1% |
| rsi_14     |  58.8 |
| zscore_20d |   1.6 |

### Soybeans / ZS=F (score 63.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | +1.3% |
| ret_20d    | +5.8% |
| ret_60d    | +2.5% |
| ma20_dist  | +3.5% |
| ma50_dist  | +2.7% |
| vol_20d    | 20.3% |
| mdd_60d    |  8.8% |
| rsi_14     |  70.6 |
| zscore_20d |   1.1 |

### Dow Jones Industrial Average / ^DJI (score 60.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | +0.1% |
| ret_20d    | +1.1% |
| ret_60d    | +6.3% |
| ma20_dist  | +0.5% |
| ma50_dist  | +2.7% |
| vol_20d    |  7.6% |
| mdd_60d    |  3.2% |
| rsi_14     |  61.9 |
| zscore_20d |   0.6 |

### FTSE 100 / ^FTSE (score 58.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | +1.0% |
| ret_20d    | +1.7% |
| ret_60d    | +0.7% |
| ma20_dist  | +0.5% |
| ma50_dist  | +1.4% |
| vol_20d    |  9.6% |
| mdd_60d    |  2.7% |
| rsi_14     |  55.2 |
| zscore_20d |   0.6 |

### S&P 500 / ^GSPC (score 57.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | -0.1% |
| ret_20d    | +0.3% |
| ret_60d    | +6.0% |
| ma20_dist  | +0.8% |
| ma50_dist  | +1.0% |
| vol_20d    | 11.1% |
| mdd_60d    |  4.5% |
| rsi_14     |  66.9 |
| zscore_20d |   0.8 |

### Microsoft Corporation / MSFT (score 57.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.4% |
| ret_5d     | +4.4% |
| ret_20d    | +1.8% |
| ret_60d    | -3.9% |
| ma20_dist  | +5.4% |
| ma50_dist  | -0.1% |
| vol_20d    | 37.1% |
| mdd_60d    | 23.4% |
| rsi_14     |  77.5 |
| zscore_20d |   1.8 |

### UnitedHealth Group Inc. / UNH (score 57.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.2% |
| ret_5d     |  -1.9% |
| ret_20d    |  +3.9% |
| ret_60d    | +31.6% |
| ma20_dist  |  +1.1% |
| ma50_dist  |  +5.7% |
| vol_20d    |  25.7% |
| mdd_60d    |   6.1% |
| rsi_14     |   54.4 |
| zscore_20d |    0.5 |

### Meta Platforms Inc. / META (score 56.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.5% |
| ret_5d     |  +5.2% |
| ret_20d    | +10.7% |
| ret_60d    |  -0.9% |
| ma20_dist  | +10.5% |
| ma50_dist  | +10.1% |
| vol_20d    |  55.5% |
| mdd_60d    |  19.9% |
| rsi_14     |   72.9 |
| zscore_20d |    1.4 |

### Euro Stoxx 50 / ^STOXX50E (score 54.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | -0.0% |
| ret_20d    | -0.6% |
| ret_60d    | +5.0% |
| ma20_dist  | -0.0% |
| ma50_dist  | +2.4% |
| vol_20d    | 13.8% |
| mdd_60d    |  3.6% |
| rsi_14     |  55.0 |
| zscore_20d |  -0.1 |

### Corn / ZC=F (score 53.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.3% |
| ret_5d     | +3.2% |
| ret_20d    | +6.7% |
| ret_60d    | -2.3% |
| ma20_dist  | +3.9% |
| ma50_dist  | +1.0% |
| vol_20d    | 28.6% |
| mdd_60d    | 15.7% |
| rsi_14     |  63.1 |
| zscore_20d |   1.2 |

### Brent Crude Oil / BZ=F (score 50.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.8% |
| ret_5d     | +10.4% |
| ret_20d    |  +6.7% |
| ret_60d    | -11.8% |
| ma20_dist  |  +9.5% |
| ma50_dist  |  -6.3% |
| vol_20d    |  48.9% |
| mdd_60d    |  39.4% |
| rsi_14     |   68.6 |
| zscore_20d |    1.6 |

### CAC 40 / ^FCHI (score 50.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | +0.6% |
| ret_20d    | -1.1% |
| ret_60d    | +2.7% |
| ma20_dist  | -0.1% |
| ma50_dist  | +1.4% |
| vol_20d    | 12.1% |
| mdd_60d    |  4.2% |
| rsi_14     |  49.5 |
| zscore_20d |  -0.2 |

### Russell 2000 / ^RUT (score 50.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | -0.6% |
| ret_20d    | +1.2% |
| ret_60d    | +6.5% |
| ma20_dist  | -0.4% |
| ma50_dist  | +1.9% |
| vol_20d    | 12.5% |
| mdd_60d    |  4.8% |
| rsi_14     |  42.1 |
| zscore_20d |  -0.4 |

### Amazon.com Inc. / AMZN (score 45.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.0% |
| ret_5d     | +1.2% |
| ret_20d    | +1.6% |
| ret_60d    | +0.6% |
| ma20_dist  | +3.4% |
| ma50_dist  | -1.1% |
| vol_20d    | 33.6% |
| mdd_60d    | 17.4% |
| rsi_14     |  75.6 |
| zscore_20d |   1.2 |

### DAX / ^GDAXI (score 43.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | -0.8% |
| ret_20d    | -0.4% |
| ret_60d    | +3.0% |
| ma20_dist  | -0.7% |
| ma50_dist  | +0.3% |
| vol_20d    | 16.0% |
| mdd_60d    |  4.7% |
| rsi_14     |  54.5 |
| zscore_20d |  -0.6 |

### NVIDIA Corporation / NVDA (score 37.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.4% |
| ret_5d     | +2.3% |
| ret_20d    | -0.0% |
| ret_60d    | +2.6% |
| ma20_dist  | +2.6% |
| ma50_dist  | -1.1% |
| vol_20d    | 37.5% |
| mdd_60d    | 18.3% |
| rsi_14     |  60.3 |
| zscore_20d |   0.8 |

### NASDAQ 100 / ^NDX (score 32.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.6% |
| ret_5d     | -2.4% |
| ret_20d    | -3.1% |
| ret_60d    | +9.2% |
| ma20_dist  | -1.9% |
| ma50_dist  | -1.7% |
| vol_20d    | 24.4% |
| mdd_60d    |  7.0% |
| rsi_14     |  46.2 |
| zscore_20d |  -1.4 |

### Alphabet Inc. Class A / GOOGL (score 27.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -4.4% |
| ret_5d     | -1.2% |
| ret_20d    | -5.0% |
| ret_60d    | +5.1% |
| ma20_dist  | -0.6% |
| ma50_dist  | -4.5% |
| vol_20d    | 36.1% |
| mdd_60d    | 16.2% |
| rsi_14     |  56.1 |
| zscore_20d |  -0.3 |

### Platinum / PL=F (score 26.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.3% |
| ret_5d     |  +1.0% |
| ret_20d    |  -9.7% |
| ret_60d    | -21.0% |
| ma20_dist  |  +0.4% |
| ma50_dist  |  -9.2% |
| vol_20d    |  37.3% |
| mdd_60d    |  29.1% |
| rsi_14     |   54.5 |
| zscore_20d |    0.1 |

### Tesla Inc. / TSLA (score 21.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.9% |
| ret_5d     | -3.8% |
| ret_20d    | -3.4% |
| ret_60d    | -0.4% |
| ma20_dist  | -1.9% |
| ma50_dist  | -4.6% |
| vol_20d    | 57.7% |
| mdd_60d    | 15.8% |
| rsi_14     |  54.8 |
| zscore_20d |  -0.5 |

### Gold / GC=F (score 20.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.4% |
| ret_5d     |  -3.5% |
| ret_20d    |  -8.0% |
| ret_60d    | -17.1% |
| ma20_dist  |  -2.7% |
| ma50_dist  |  -7.9% |
| vol_20d    |  24.1% |
| mdd_60d    |  15.8% |
| rsi_14     |   46.6 |
| zscore_20d |   -1.2 |

### Natural Gas / NG=F (score 17.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.3% |
| ret_5d     |  -5.1% |
| ret_20d    | -11.8% |
| ret_60d    |  +6.3% |
| ma20_dist  |  -8.8% |
| ma50_dist  |  -7.2% |
| vol_20d    |  39.4% |
| mdd_60d    |  14.5% |
| rsi_14     |   22.0 |
| zscore_20d |   -1.9 |

### Silver / SI=F (score 5.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.1% |
| ret_5d     |  -7.4% |
| ret_20d    | -20.0% |
| ret_60d    | -30.1% |
| ma20_dist  |  -7.5% |
| ma50_dist  | -19.2% |
| vol_20d    |  46.8% |
| mdd_60d    |  37.1% |
| rsi_14     |   43.3 |
| zscore_20d |   -1.3 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Apple Inc. / AAPL                   |   8.6664 |           2.6% |                 0.28x |       17.3329 |            5.2% |
| Wheat / ZW=F                        |  17.9464 |           2.7% |                 0.28x |       35.8929 |            5.3% |
| Hang Seng / ^HSI                    | 489.3763 |           2.0% |                 0.50x |      978.7525 |            3.9% |
| JPMorgan Chase & Co. / JPM          |   7.6861 |           2.2% |                 0.46x |       15.3722 |            4.5% |
| Soybeans / ZS=F                     |  19.1071 |           1.6% |                 0.49x |       38.2143 |            3.2% |
| Dow Jones Industrial Average / ^DJI | 519.0678 |           1.0% |                 1.32x |     1038.1356 |            2.0% |
| FTSE 100 / ^FTSE                    | 117.1000 |           1.1% |                 1.04x |      234.2001 |            2.2% |
| S&P 500 / ^GSPC                     |  73.6993 |           1.0% |                 0.90x |      147.3986 |            2.0% |
| Microsoft Corporation / MSFT        |  12.3229 |           3.1% |                 0.27x |       24.6457 |            6.1% |
| UnitedHealth Group Inc. / UNH       |  12.6414 |           3.0% |                 0.39x |       25.2829 |            6.0% |
| Meta Platforms Inc. / META          |  29.0850 |           4.4% |                 0.18x |       58.1700 |            8.8% |
| Euro Stoxx 50 / ^STOXX50E           |  72.5399 |           1.2% |                 0.72x |      145.0798 |            2.3% |
| Corn / ZC=F                         |  10.6607 |           2.4% |                 0.35x |       21.3214 |            4.8% |
| Brent Crude Oil / BZ=F              |   3.3900 |           4.0% |                 0.20x |        6.7800 |            8.0% |
| CAC 40 / ^FCHI                      |  94.4407 |           1.1% |                 0.83x |      188.8814 |            2.3% |
| Russell 2000 / ^RUT                 |  38.0972 |           1.3% |                 0.80x |       76.1944 |            2.6% |
| Amazon.com Inc. / AMZN              |   7.6300 |           3.1% |                 0.30x |       15.2600 |            6.1% |
| DAX / ^GDAXI                        | 327.5762 |           1.3% |                 0.63x |      655.1523 |            2.6% |
| NVIDIA Corporation / NVDA           |   6.9964 |           3.4% |                 0.27x |       13.9929 |            6.7% |
| NASDAQ 100 / ^NDX                   | 587.5239 |           2.0% |                 0.41x |     1175.0477 |            4.0% |
| Alphabet Inc. Class A / GOOGL       |  11.2850 |           3.2% |                 0.28x |       22.5700 |            6.4% |
| Platinum / PL=F                     |  35.0929 |           2.1% |                 0.27x |       70.1857 |            4.3% |
| Tesla Inc. / TSLA                   |  19.0307 |           4.9% |                 0.17x |       38.0614 |            9.7% |
| Gold / GC=F                         |  79.7643 |           2.0% |                 0.42x |      159.5286 |            4.0% |
| Natural Gas / NG=F                  |   0.1359 |           4.8% |                 0.25x |        0.2717 |            9.5% |
| Silver / SI=F                       |   2.0333 |           3.6% |                 0.21x |        4.0666 |            7.3% |

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

Scoring engine version: **1.0.0** | Git commit: **383bacf**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
