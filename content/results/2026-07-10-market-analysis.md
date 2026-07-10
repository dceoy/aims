+++
title = "Market Analysis 2026-07-10"
date = "2026-07-10T00:00:00+00:00"
draft = false
summary = "Bullish market: 26 reliable instruments. Top signal: UNH (score 80.9)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-07-10.json", "data/history/2026-07-10.json"]
market_regime = "Bullish"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "dd0f942"
+++

## Market Regime

**Bullish** — 19 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **UnitedHealth Group Inc. / UNH** — score 80.9, 20d return +5.1%, RSI14=69. 20d up +5.1%; above MA20 by 4.1%; RSI14=69 ⚠️ Upcoming: UNH earnings release (2026-07-16)
- **Apple Inc. / AAPL** — score 79.1, 20d return +8.8%, RSI14=64. 20d up +8.8%; above MA20 by 6.5%; RSI14=64
- **Soybeans / ZS=F** — score 70.3, 20d return +5.9%, RSI14=64. 20d up +5.9%; above MA20 by 4.0%; RSI14=64
- **JPMorgan Chase & Co. / JPM** — score 70.0, 20d return +7.8%, RSI14=53. 20d up +7.8%; above MA20 by 2.3%; RSI14=53 ⚠️ Upcoming: JPM earnings release (2026-07-14)
- **Dow Jones Industrial Average / ^DJI** — score 69.7, 20d return +3.2%, RSI14=69. 20d up +3.2%; above MA20 by 1.1%; RSI14=69

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                | Applies To |
| ---------- | -------------------- | ---------- |
| 2026-07-14 | JPM earnings release | JPM        |
| 2026-07-16 | UNH earnings release | UNH        |

## Signal History

Compared with the previous available report (**2026-07-09**).
- **New top-5:** JPM
- **Persistent top signals:** ZS=F (4 reports), UNH (3 reports), ^DJI (3 reports), AAPL (2 reports)
- **Dropped from top-5:** ^GSPC

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +0 |   -12.1 |
| 7203.T    |     -2 |   -13.3 |
| 8306.T    |     +0 |    -3.0 |
| AAPL      |     +0 |    +0.0 |
| AMZN      |     +5 |    +7.0 |
| BZ=F      |     -3 |   -14.2 |
| CL=F      |     +0 |   -10.6 |
| GC=F      |     +2 |    +8.5 |
| GOOGL     |     -2 |    -9.4 |
| HG=F      |     +3 |   +16.4 |
| JPM       |     +3 |    +8.8 |
| META      |     +7 |   +17.3 |
| MSFT      |     +0 |    -0.9 |
| NG=F      |    -11 |   -28.8 |
| NVDA      |     -4 |    -8.2 |
| PL=F      |     +1 |   +11.5 |
| SI=F      |     +0 |   +14.2 |
| TSLA      |     +9 |   +23.6 |
| UNH       |     +2 |    +1.8 |
| XOM       |     -2 |   -20.9 |
| ZC=F      |     -9 |   -13.0 |
| ZS=F      |     -2 |   -10.3 |
| ZW=F      |     +1 |    +7.0 |
| ^DJI      |     -1 |    +0.0 |
| ^FCHI     |     +2 |    +5.2 |
| ^FTSE     |     -6 |    -9.1 |
| ^GDAXI    |     +1 |    +3.9 |
| ^GSPC     |     -2 |    +5.2 |
| ^HSI      |     -6 |    -7.9 |
| ^N225     |     +1 |    +7.0 |
| ^NDX      |     +8 |   +11.5 |
| ^RUT      |     -1 |    +4.8 |
| ^STOXX50E |     +6 |    +8.2 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|    3 | Soybeans / ZS=F        |  70.3 |   Yes    | —               | 20d up +5.9%; above MA20 by 4.0%; RSI14=64    |
|    8 | Wheat / ZW=F           |  66.7 |   Yes    | —               | 20d up +4.4%; above MA20 by 3.1%; RSI14=49    |
|   15 | Corn / ZC=F            |  48.5 |   Yes    | —               | 20d up +2.0%; above MA20 by 2.2%; RSI14=54    |
|   22 | Gold / GC=F            |  31.8 |   Yes    | —               | 20d down -3.0%; below MA20 by 0.2%; RSI14=36  |
|   23 | Natural Gas / NG=F     |  24.2 |   Yes    | —               | 20d down -4.1%; below MA20 by 5.8%; RSI14=44  |
|   24 | Platinum / PL=F        |  23.9 |   Yes    | —               | 20d down -5.3%; below MA20 by 2.2%; RSI14=35  |
|   25 | Brent Crude Oil / BZ=F |  18.8 |   Yes    | —               | 20d down -16.6%; below MA20 by 2.1%; RSI14=43 |
|   26 | Silver / SI=F          |  18.8 |   Yes    | —               | 20d down -7.2%; below MA20 by 3.9%; RSI14=29  |
|   29 | Copper / HG=F          |  45.1 |    No    | malformed_input | Suppressed: malformed_input                   |
|   33 | WTI Crude Oil / CL=F   |  15.8 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    1 | UnitedHealth Group Inc. / UNH                                                  |  80.9 |   Yes    | —                             | 20d up +5.1%; above MA20 by 4.1%; RSI14=69   |
|    2 | Apple Inc. / AAPL                                                              |  79.1 |   Yes    | —                             | 20d up +8.8%; above MA20 by 6.5%; RSI14=64   |
|    4 | JPMorgan Chase & Co. / JPM                                                     |  70.0 |   Yes    | —                             | 20d up +7.8%; above MA20 by 2.3%; RSI14=53   |
|    6 | Meta Platforms Inc. / META                                                     |  68.5 |   Yes    | —                             | 20d up +8.1%; above MA20 by 8.9%; RSI14=65   |
|   12 | Amazon.com Inc. / AMZN                                                         |  53.3 |   Yes    | —                             | 20d up +1.2%; above MA20 by 3.0%; RSI14=59   |
|   14 | Tesla Inc. / TSLA                                                              |  50.0 |   Yes    | —                             | 20d up +2.5%; above MA20 by 1.7%; RSI14=53   |
|   19 | NVIDIA Corporation / NVDA                                                      |  40.0 |   Yes    | —                             | 20d down -2.6%; above MA20 by 0.7%; RSI14=48 |
|   20 | Alphabet Inc. Class A / GOOGL                                                  |  35.8 |   Yes    | —                             | 20d down -1.5%; above MA20 by 0.3%; RSI14=47 |
|   21 | Microsoft Corporation / MSFT                                                   |  33.6 |   Yes    | —                             | 20d down -4.7%; above MA20 by 0.8%; RSI14=53 |
|   27 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  78.8 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   28 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  56.7 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   31 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  39.7 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   32 | Exxon Mobil Corporation / XOM                                                  |  21.5 |    No    | malformed_input               | Suppressed: malformed_input                  |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    5 | Dow Jones Industrial Average / ^DJI |  69.7 |   Yes    | —            | 20d up +3.2%; above MA20 by 1.1%; RSI14=69   |
|    7 | S&P 500 / ^GSPC                     |  67.3 |   Yes    | —            | 20d up +2.1%; above MA20 by 1.3%; RSI14=61   |
|    9 | Russell 2000 / ^RUT                 |  65.5 |   Yes    | —            | 20d up +4.4%; above MA20 by 0.6%; RSI14=63   |
|   10 | Euro Stoxx 50 / ^STOXX50E           |  56.4 |   Yes    | —            | 20d up +3.8%; above MA20 by 0.0%; RSI14=49   |
|   11 | NASDAQ 100 / ^NDX                   |  55.5 |   Yes    | —            | 20d up +2.2%; above MA20 by 0.3%; RSI14=50   |
|   13 | DAX / ^GDAXI                        |  53.0 |   Yes    | —            | 20d up +3.8%; above MA20 by 0.2%; RSI14=52   |
|   16 | FTSE 100 / ^FTSE                    |  48.5 |   Yes    | —            | 20d up +1.6%; below MA20 by 0.3%; RSI14=58   |
|   17 | Hang Seng / ^HSI                    |  45.8 |   Yes    | —            | 20d down -2.2%; above MA20 by 1.2%; RSI14=46 |
|   18 | CAC 40 / ^FCHI                      |  42.4 |   Yes    | —            | 20d up +1.5%; below MA20 by 0.9%; RSI14=44   |
|   30 | Nikkei 225 / ^N225                  |  44.2 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-07-09 |
| 7203.T    | 2026-07-09 |
| 8306.T    | 2026-07-09 |
| AAPL      | 2026-07-09 |
| AMZN      | 2026-07-09 |
| BZ=F      | 2026-07-09 |
| CL=F      | 2026-07-09 |
| GC=F      | 2026-07-09 |
| GOOGL     | 2026-07-09 |
| HG=F      | 2026-07-09 |
| JPM       | 2026-07-09 |
| META      | 2026-07-09 |
| MSFT      | 2026-07-09 |
| NG=F      | 2026-07-09 |
| NVDA      | 2026-07-09 |
| PL=F      | 2026-07-09 |
| SI=F      | 2026-07-09 |
| TSLA      | 2026-07-09 |
| UNH       | 2026-07-09 |
| XOM       | 2026-07-09 |
| ZC=F      | 2026-07-09 |
| ZS=F      | 2026-07-09 |
| ZW=F      | 2026-07-09 |
| ^DJI      | 2026-07-09 |
| ^FCHI     | 2026-07-09 |
| ^FTSE     | 2026-07-09 |
| ^GDAXI    | 2026-07-09 |
| ^GSPC     | 2026-07-09 |
| ^HSI      | 2026-07-09 |
| ^N225     | 2026-07-09 |
| ^NDX      | 2026-07-09 |
| ^RUT      | 2026-07-09 |
| ^STOXX50E | 2026-07-09 |

## Symbol Details

### UnitedHealth Group Inc. / UNH (score 80.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.4% |
| ret_5d     |  +1.2% |
| ret_20d    |  +5.1% |
| ret_60d    | +38.7% |
| ma20_dist  |  +4.1% |
| ma50_dist  |  +9.4% |
| vol_20d    |  24.6% |
| mdd_60d    |   6.1% |
| rsi_14     |   68.7 |
| zscore_20d |    1.7 |

### Apple Inc. / AAPL (score 79.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.9% |
| ret_5d     |  +7.4% |
| ret_20d    |  +8.8% |
| ret_60d    | +22.1% |
| ma20_dist  |  +6.5% |
| ma50_dist  |  +6.5% |
| vol_20d    |  34.2% |
| mdd_60d    |  12.7% |
| rsi_14     |   63.7 |
| zscore_20d |    1.8 |

### Soybeans / ZS=F (score 70.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.3% |
| ret_5d     | +4.8% |
| ret_20d    | +5.9% |
| ret_60d    | +1.5% |
| ma20_dist  | +4.0% |
| ma50_dist  | +1.5% |
| vol_20d    | 20.1% |
| mdd_60d    |  8.8% |
| rsi_14     |  64.2 |
| zscore_20d |   1.6 |

### JPMorgan Chase & Co. / JPM (score 70.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.5% |
| ret_5d     | +0.9% |
| ret_20d    | +7.8% |
| ret_60d    | +7.4% |
| ma20_dist  | +2.3% |
| ma50_dist  | +7.1% |
| vol_20d    | 24.9% |
| mdd_60d    |  6.7% |
| rsi_14     |  53.2 |
| zscore_20d |   0.9 |

### Dow Jones Industrial Average / ^DJI (score 69.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +0.3% |
| ret_20d    | +3.2% |
| ret_60d    | +8.9% |
| ma20_dist  | +1.1% |
| ma50_dist  | +3.3% |
| vol_20d    | 12.6% |
| mdd_60d    |  3.2% |
| rsi_14     |  69.0 |
| zscore_20d |   0.8 |

### Meta Platforms Inc. / META (score 68.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +4.7% |
| ret_5d     | +3.0% |
| ret_20d    | +8.1% |
| ret_60d    | -0.4% |
| ma20_dist  | +8.9% |
| ma50_dist  | +5.2% |
| vol_20d    | 52.8% |
| mdd_60d    | 21.1% |
| rsi_14     |  64.7 |
| zscore_20d |   2.2 |

### S&P 500 / ^GSPC (score 67.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.8% |
| ret_5d     | +0.8% |
| ret_20d    | +2.1% |
| ret_60d    | +9.5% |
| ma20_dist  | +1.3% |
| ma50_dist  | +1.6% |
| vol_20d    | 14.7% |
| mdd_60d    |  4.5% |
| rsi_14     |  61.1 |
| zscore_20d |   1.3 |

### Wheat / ZW=F (score 66.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.0% |
| ret_5d     | +3.3% |
| ret_20d    | +4.4% |
| ret_60d    | +5.0% |
| ma20_dist  | +3.1% |
| ma50_dist  | -0.1% |
| vol_20d    | 23.7% |
| mdd_60d    | 14.6% |
| rsi_14     |  49.4 |
| zscore_20d |   1.6 |

### Russell 2000 / ^RUT (score 65.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.2% |
| ret_5d     |  -0.7% |
| ret_20d    |  +4.4% |
| ret_60d    | +12.1% |
| ma20_dist  |  +0.6% |
| ma50_dist  |  +3.2% |
| vol_20d    |  16.8% |
| mdd_60d    |   4.8% |
| rsi_14     |   62.6 |
| zscore_20d |    0.4 |

### Euro Stoxx 50 / ^STOXX50E (score 56.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.3% |
| ret_5d     | -1.2% |
| ret_20d    | +3.8% |
| ret_60d    | +6.4% |
| ma20_dist  | +0.0% |
| ma50_dist  | +3.2% |
| vol_20d    | 15.9% |
| mdd_60d    |  4.9% |
| rsi_14     |  49.4 |
| zscore_20d |   0.0 |

### NASDAQ 100 / ^NDX (score 55.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.6% |
| ret_5d     |  -0.3% |
| ret_20d    |  +2.2% |
| ret_60d    | +17.1% |
| ma20_dist  |  +0.3% |
| ma50_dist  |  +1.3% |
| vol_20d    |  29.3% |
| mdd_60d    |   7.0% |
| rsi_14     |   50.5 |
| zscore_20d |    0.2 |

### Amazon.com Inc. / AMZN (score 53.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.4% |
| ret_5d     | +2.2% |
| ret_20d    | +1.2% |
| ret_60d    | +3.0% |
| ma20_dist  | +3.0% |
| ma50_dist  | -2.9% |
| vol_20d    | 34.7% |
| mdd_60d    | 17.4% |
| rsi_14     |  58.6 |
| zscore_20d |   1.3 |

### DAX / ^GDAXI (score 53.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | -1.8% |
| ret_20d    | +3.8% |
| ret_60d    | +4.4% |
| ma20_dist  | +0.2% |
| ma50_dist  | +1.3% |
| vol_20d    | 17.1% |
| mdd_60d    |  4.7% |
| rsi_14     |  51.9 |
| zscore_20d |   0.2 |

### Tesla Inc. / TSLA (score 50.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +3.2% |
| ret_5d     |  -4.4% |
| ret_20d    |  +2.5% |
| ret_60d    | +15.4% |
| ma20_dist  |  +1.7% |
| ma50_dist  |  -0.5% |
| vol_20d    |  61.0% |
| mdd_60d    |  15.8% |
| rsi_14     |   52.7 |
| zscore_20d |    0.5 |

### Corn / ZC=F (score 48.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.6% |
| ret_5d     | +1.6% |
| ret_20d    | +2.0% |
| ret_60d    | -2.8% |
| ma20_dist  | +2.2% |
| ma50_dist  | -2.8% |
| vol_20d    | 25.6% |
| mdd_60d    | 15.7% |
| rsi_14     |  53.8 |
| zscore_20d |   0.9 |

### FTSE 100 / ^FTSE (score 48.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | -1.7% |
| ret_20d    | +1.6% |
| ret_60d    | -1.3% |
| ma20_dist  | -0.3% |
| ma50_dist  | +0.6% |
| vol_20d    | 11.8% |
| mdd_60d    |  4.4% |
| rsi_14     |  57.8 |
| zscore_20d |  -0.4 |

### Hang Seng / ^HSI (score 45.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | +4.2% |
| ret_20d    | -2.2% |
| ret_60d    | -7.2% |
| ma20_dist  | +1.2% |
| ma50_dist  | -3.6% |
| vol_20d    | 20.9% |
| mdd_60d    | 14.9% |
| rsi_14     |  46.5 |
| zscore_20d |   0.5 |

### CAC 40 / ^FCHI (score 42.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | -1.7% |
| ret_20d    | +1.5% |
| ret_60d    | +0.6% |
| ma20_dist  | -0.9% |
| ma50_dist  | +1.1% |
| vol_20d    | 14.0% |
| mdd_60d    |  5.6% |
| rsi_14     |  44.4 |
| zscore_20d |  -1.2 |

### NVIDIA Corporation / NVDA (score 40.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | +2.6% |
| ret_20d    | -2.6% |
| ret_60d    | +7.1% |
| ma20_dist  | +0.7% |
| ma50_dist  | -3.1% |
| vol_20d    | 35.0% |
| mdd_60d    | 18.3% |
| rsi_14     |  48.0 |
| zscore_20d |   0.2 |

### Alphabet Inc. Class A / GOOGL (score 35.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.8% |
| ret_5d     |  -0.6% |
| ret_20d    |  -1.5% |
| ret_60d    | +11.8% |
| ma20_dist  |  +0.3% |
| ma50_dist  |  -3.6% |
| vol_20d    |  32.2% |
| mdd_60d    |  16.2% |
| rsi_14     |   46.7 |
| zscore_20d |    0.1 |

### Microsoft Corporation / MSFT (score 33.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +0.0% |
| ret_20d    | -4.7% |
| ret_60d    | +0.2% |
| ma20_dist  | +0.8% |
| ma50_dist  | -4.9% |
| vol_20d    | 36.8% |
| mdd_60d    | 23.4% |
| rsi_14     |  52.8 |
| zscore_20d |   0.3 |

### Gold / GC=F (score 31.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.5% |
| ret_5d     |  +1.5% |
| ret_20d    |  -3.0% |
| ret_60d    | -12.9% |
| ma20_dist  |  -0.2% |
| ma50_dist  |  -5.8% |
| vol_20d    |  28.9% |
| mdd_60d    |  17.9% |
| rsi_14     |   35.6 |
| zscore_20d |   -0.1 |

### Natural Gas / NG=F (score 24.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -6.2% |
| ret_5d     |  -6.5% |
| ret_20d    |  -4.1% |
| ret_60d    | +14.7% |
| ma20_dist  |  -5.8% |
| ma50_dist  |  -1.6% |
| vol_20d    |  41.8% |
| mdd_60d    |   9.9% |
| rsi_14     |   43.8 |
| zscore_20d |   -2.6 |

### Platinum / PL=F (score 23.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.7% |
| ret_5d     |  +1.9% |
| ret_20d    |  -5.3% |
| ret_60d    | -21.5% |
| ma20_dist  |  -2.2% |
| ma50_dist  | -11.8% |
| vol_20d    |  41.9% |
| mdd_60d    |  29.1% |
| rsi_14     |   34.6 |
| zscore_20d |   -0.5 |

### Brent Crude Oil / BZ=F (score 18.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.2% |
| ret_5d     |  +6.6% |
| ret_20d    | -16.6% |
| ret_60d    | -23.2% |
| ma20_dist  |  -2.1% |
| ma50_dist  | -17.9% |
| vol_20d    |  44.0% |
| mdd_60d    |  39.4% |
| rsi_14     |   42.7 |
| zscore_20d |   -0.3 |

### Silver / SI=F (score 18.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +3.8% |
| ret_5d     |  +0.5% |
| ret_20d    |  -7.2% |
| ret_60d    | -20.1% |
| ma20_dist  |  -3.9% |
| ma50_dist  | -14.7% |
| vol_20d    |  52.1% |
| mdd_60d    |  34.7% |
| rsi_14     |   29.0 |
| zscore_20d |   -0.6 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| UnitedHealth Group Inc. / UNH       |  10.3129 |           2.4% |                 0.41x |       20.6257 |            4.8% |
| Apple Inc. / AAPL                   |   8.9614 |           2.8% |                 0.29x |       17.9229 |            5.7% |
| Soybeans / ZS=F                     |  19.6964 |           1.7% |                 0.50x |       39.3929 |            3.3% |
| JPMorgan Chase & Co. / JPM          |   7.6626 |           2.3% |                 0.40x |       15.3252 |            4.6% |
| Dow Jones Industrial Average / ^DJI | 537.4967 |           1.0% |                 0.80x |     1074.9933 |            2.0% |
| Meta Platforms Inc. / META          |  24.7479 |           3.9% |                 0.19x |       49.4957 |            7.8% |
| S&P 500 / ^GSPC                     |  85.4915 |           1.1% |                 0.68x |      170.9830 |            2.3% |
| Wheat / ZW=F                        |  14.0893 |           2.3% |                 0.42x |       28.1786 |            4.6% |
| Russell 2000 / ^RUT                 |  44.8858 |           1.5% |                 0.59x |       89.7715 |            3.0% |
| Euro Stoxx 50 / ^STOXX50E           |  78.2156 |           1.2% |                 0.63x |      156.4312 |            2.5% |
| NASDAQ 100 / ^NDX                   | 669.3806 |           2.3% |                 0.34x |     1338.7612 |            4.5% |
| Amazon.com Inc. / AMZN              |   8.2729 |           3.3% |                 0.29x |       16.5457 |            6.7% |
| DAX / ^GDAXI                        | 353.9071 |           1.4% |                 0.58x |      707.8142 |            2.8% |
| Tesla Inc. / TSLA                   |  20.7071 |           5.1% |                 0.16x |       41.4143 |           10.2% |
| Corn / ZC=F                         |   9.5357 |           2.2% |                 0.39x |       19.0714 |            4.5% |
| FTSE 100 / ^FTSE                    | 124.1714 |           1.2% |                 0.84x |      248.3428 |            2.4% |
| Hang Seng / ^HSI                    | 472.7009 |           2.0% |                 0.48x |      945.4018 |            3.9% |
| CAC 40 / ^FCHI                      |  93.7686 |           1.1% |                 0.71x |      187.5371 |            2.3% |
| NVIDIA Corporation / NVDA           |   6.6350 |           3.3% |                 0.29x |       13.2700 |            6.5% |
| Alphabet Inc. Class A / GOOGL       |  11.8157 |           3.3% |                 0.31x |       23.6314 |            6.6% |
| Microsoft Corporation / MSFT        |  12.5136 |           3.3% |                 0.27x |       25.0271 |            6.5% |
| Gold / GC=F                         |  87.8571 |           2.1% |                 0.35x |      175.7143 |            4.3% |
| Natural Gas / NG=F                  |   0.1407 |           4.7% |                 0.24x |        0.2814 |            9.3% |
| Platinum / PL=F                     |  46.1143 |           2.8% |                 0.24x |       92.2286 |            5.7% |
| Brent Crude Oil / BZ=F              |   3.2479 |           4.3% |                 0.23x |        6.4957 |            8.5% |
| Silver / SI=F                       |   2.4417 |           4.0% |                 0.19x |        4.8834 |            8.1% |

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

Scoring engine version: **1.0.0** | Git commit: **dd0f942**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
