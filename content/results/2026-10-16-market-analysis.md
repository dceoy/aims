+++
title = "Market Analysis 2026-10-16"
date = "2026-10-16T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: MSFT (score 80.9)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-10-16.json", "data/history/2026-10-16.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "64cf559"
+++

## Market Regime

**Neutral** — 12 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Microsoft Corporation / MSFT** — score 80.9, 20d return +8.4%, RSI14=66. 20d up +8.4%; above MA20 by 4.0%; RSI14=66
- **FTSE 100 / ^FTSE** — score 74.2, 20d return +0.2%, RSI14=58. 20d up +0.2%; above MA20 by 2.1%; RSI14=58
- **UnitedHealth Group Inc. / UNH** — score 70.3, 20d return +8.4%, RSI14=70. 20d up +8.4%; above MA20 by 7.8%; RSI14=70
- **Dow Jones Industrial Average / ^DJI** — score 69.1, 20d return +0.8%, RSI14=55. 20d up +0.8%; above MA20 by 1.3%; RSI14=55
- **S&P 500 / ^GSPC** — score 62.1, 20d return +1.4%, RSI14=50. 20d up +1.4%; above MA20 by 0.1%; RSI14=50

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                 | Applies To |
| ---------- | --------------------- | ---------- |
| 2026-10-21 | TSLA earnings release | TSLA       |

## Signal History

Compared with the previous available report (**2026-10-15**).

- **New top-5:** ^DJI, ^GSPC
- **Persistent top signals:** MSFT (15 reports), UNH (2 reports), ^FTSE (2 reports)
- **Dropped from top-5:** AAPL, BZ=F

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +1 |    -2.1 |
| 7203.T    |     +0 |    +2.7 |
| 8306.T    |     +0 |    -8.8 |
| AAPL      |     -4 |   -10.0 |
| AMZN      |     +2 |    +5.2 |
| BZ=F      |     -2 |    -4.5 |
| CL=F      |     +0 |    +8.2 |
| GC=F      |     +5 |   +10.9 |
| GOOGL     |     +0 |    +4.5 |
| HG=F      |     +1 |   -13.0 |
| JPM       |     -4 |    -6.7 |
| META      |     +0 |    +5.8 |
| MSFT      |     +0 |    +5.5 |
| NG=F      |     +0 |    +9.7 |
| NVDA      |     -3 |    -7.6 |
| PL=F      |     +0 |    +6.7 |
| SI=F      |     +0 |   +12.4 |
| TSLA      |     +0 |    +3.3 |
| UNH       |     +1 |    +3.3 |
| XOM       |     -1 |   -13.6 |
| ZC=F      |     -1 |    -1.2 |
| ZS=F      |     -3 |    -7.6 |
| ZW=F      |     -2 |    -7.3 |
| ^DJI      |     +2 |    +8.5 |
| ^FCHI     |     +4 |    +6.7 |
| ^FTSE     |     +1 |    +3.9 |
| ^GDAXI    |     +0 |    +3.0 |
| ^GSPC     |     +2 |    +3.6 |
| ^HSI      |     -2 |    -5.5 |
| ^N225     |     -1 |   -27.6 |
| ^NDX      |     +3 |    +2.7 |
| ^RUT      |     +3 |   +12.1 |
| ^STOXX50E |     -2 |    -3.3 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Natural Gas / NG=F** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input
- **Copper / HG=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|    7 | Brent Crude Oil / BZ=F |  59.7 |   Yes    | —               | 20d up +1.0%; above MA20 by 2.4%; RSI14=55    |
|   16 | Gold / GC=F            |  40.0 |   Yes    | —               | 20d down -5.2%; below MA20 by 1.3%; RSI14=36  |
|   17 | Soybeans / ZS=F        |  38.2 |   Yes    | —               | 20d down -4.3%; below MA20 by 2.6%; RSI14=29  |
|   22 | Wheat / ZW=F           |  23.9 |   Yes    | —               | 20d down -7.8%; below MA20 by 3.1%; RSI14=35  |
|   23 | Corn / ZC=F            |  21.2 |   Yes    | —               | 20d down -9.9%; below MA20 by 5.8%; RSI14=19  |
|   24 | Platinum / PL=F        |  18.5 |   Yes    | —               | 20d down -10.1%; below MA20 by 5.5%; RSI14=29 |
|   25 | Silver / SI=F          |  15.4 |   Yes    | —               | 20d down -13.2%; below MA20 by 7.3%; RSI14=28 |
|   29 | Natural Gas / NG=F     |  70.6 |    No    | malformed_input | Suppressed: malformed_input                   |
|   30 | WTI Crude Oil / CL=F   |  66.4 |    No    | malformed_input | Suppressed: malformed_input                   |
|   31 | Copper / HG=F          |  41.2 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    1 | Microsoft Corporation / MSFT                                                   |  80.9 |   Yes    | —                             | 20d up +8.4%; above MA20 by 4.0%; RSI14=66   |
|    3 | UnitedHealth Group Inc. / UNH                                                  |  70.3 |   Yes    | —                             | 20d up +8.4%; above MA20 by 7.8%; RSI14=70   |
|    6 | Apple Inc. / AAPL                                                              |  61.8 |   Yes    | —                             | 20d up +1.5%; above MA20 by 1.5%; RSI14=51   |
|    9 | Meta Platforms Inc. / META                                                     |  58.2 |   Yes    | —                             | 20d up +8.1%; above MA20 by 0.4%; RSI14=46   |
|   10 | Alphabet Inc. Class A / GOOGL                                                  |  53.9 |   Yes    | —                             | 20d up +0.5%; above MA20 by 0.7%; RSI14=57   |
|   11 | Amazon.com Inc. / AMZN                                                         |  51.8 |   Yes    | —                             | 20d up +1.4%; above MA20 by 0.5%; RSI14=56   |
|   15 | JPMorgan Chase & Co. / JPM                                                     |  42.4 |   Yes    | —                             | 20d down -3.5%; above MA20 by 0.1%; RSI14=40 |
|   19 | Tesla Inc. / TSLA                                                              |  35.8 |   Yes    | —                             | 20d down -1.0%; below MA20 by 2.3%; RSI14=44 |
|   21 | NVIDIA Corporation / NVDA                                                      |  29.1 |   Yes    | —                             | 20d down -1.0%; below MA20 by 5.0%; RSI14=41 |
|   26 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  74.8 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   27 | Exxon Mobil Corporation / XOM                                                  |  74.5 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   28 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  71.8 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   33 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  15.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    2 | FTSE 100 / ^FTSE                    |  74.2 |   Yes    | —            | 20d up +0.2%; above MA20 by 2.1%; RSI14=58   |
|    4 | Dow Jones Industrial Average / ^DJI |  69.1 |   Yes    | —            | 20d up +0.8%; above MA20 by 1.3%; RSI14=55   |
|    5 | S&P 500 / ^GSPC                     |  62.1 |   Yes    | —            | 20d up +1.4%; above MA20 by 0.1%; RSI14=50   |
|    8 | DAX / ^GDAXI                        |  58.5 |   Yes    | —            | 20d down -1.3%; above MA20 by 0.4%; RSI14=49 |
|   12 | NASDAQ 100 / ^NDX                   |  47.9 |   Yes    | —            | 20d up +1.7%; below MA20 by 2.0%; RSI14=38   |
|   13 | CAC 40 / ^FCHI                      |  46.7 |   Yes    | —            | 20d down -3.1%; below MA20 by 0.1%; RSI14=40 |
|   14 | Euro Stoxx 50 / ^STOXX50E           |  44.2 |   Yes    | —            | 20d down -2.4%; below MA20 by 1.1%; RSI14=38 |
|   18 | Hang Seng / ^HSI                    |  37.9 |   Yes    | —            | 20d down -2.6%; below MA20 by 1.5%; RSI14=38 |
|   20 | Russell 2000 / ^RUT                 |  34.5 |   Yes    | —            | 20d down -3.7%; below MA20 by 1.8%; RSI14=37 |
|   32 | Nikkei 225 / ^N225                  |  29.1 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-10-15 |
| 7203.T    | 2026-10-15 |
| 8306.T    | 2026-10-15 |
| AAPL      | 2026-10-15 |
| AMZN      | 2026-10-15 |
| BZ=F      | 2026-10-15 |
| CL=F      | 2026-10-15 |
| GC=F      | 2026-10-15 |
| GOOGL     | 2026-10-15 |
| HG=F      | 2026-10-15 |
| JPM       | 2026-10-15 |
| META      | 2026-10-15 |
| MSFT      | 2026-10-15 |
| NG=F      | 2026-10-15 |
| NVDA      | 2026-10-15 |
| PL=F      | 2026-10-15 |
| SI=F      | 2026-10-15 |
| TSLA      | 2026-10-15 |
| UNH       | 2026-10-15 |
| XOM       | 2026-10-15 |
| ZC=F      | 2026-10-15 |
| ZS=F      | 2026-10-15 |
| ZW=F      | 2026-10-15 |
| ^DJI      | 2026-10-15 |
| ^FCHI     | 2026-10-15 |
| ^FTSE     | 2026-10-15 |
| ^GDAXI    | 2026-10-15 |
| ^GSPC     | 2026-10-15 |
| ^HSI      | 2026-10-15 |
| ^N225     | 2026-10-15 |
| ^NDX      | 2026-10-15 |
| ^RUT      | 2026-10-15 |
| ^STOXX50E | 2026-10-15 |

## Symbol Details

### Microsoft Corporation / MSFT (score 80.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.1% |
| ret_5d     |  +3.2% |
| ret_20d    |  +8.4% |
| ret_60d    | +38.5% |
| ma20_dist  |  +4.0% |
| ma50_dist  |  +6.9% |
| vol_20d    |  20.6% |
| mdd_60d    |   5.1% |
| rsi_14     |   66.2 |
| zscore_20d |    1.4 |

### FTSE 100 / ^FTSE (score 74.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | +3.8% |
| ret_20d    | +0.2% |
| ret_60d    | +1.2% |
| ma20_dist  | +2.1% |
| ma50_dist  | +1.2% |
| vol_20d    | 11.6% |
| mdd_60d    |  4.4% |
| rsi_14     |  58.1 |
| zscore_20d |   2.0 |

### UnitedHealth Group Inc. / UNH (score 70.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.8% |
| ret_5d     | +9.6% |
| ret_20d    | +8.4% |
| ret_60d    | -5.7% |
| ma20_dist  | +7.8% |
| ma50_dist  | +5.3% |
| vol_20d    | 24.9% |
| mdd_60d    | 14.8% |
| rsi_14     |  70.4 |
| zscore_20d |   3.3 |

### Dow Jones Industrial Average / ^DJI (score 69.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | +1.8% |
| ret_20d    | +0.8% |
| ret_60d    | -0.1% |
| ma20_dist  | +1.3% |
| ma50_dist  | -0.6% |
| vol_20d    |  9.0% |
| mdd_60d    |  6.3% |
| rsi_14     |  55.2 |
| zscore_20d |   2.0 |

### S&P 500 / ^GSPC (score 62.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | -0.3% |
| ret_20d    | +1.4% |
| ret_60d    | +3.3% |
| ma20_dist  | +0.1% |
| ma50_dist  | +0.5% |
| vol_20d    |  9.4% |
| mdd_60d    |  3.2% |
| rsi_14     |  50.1 |
| zscore_20d |   0.1 |

### Apple Inc. / AAPL (score 61.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | +0.5% |
| ret_20d    | +1.5% |
| ret_60d    | +5.0% |
| ma20_dist  | +1.5% |
| ma50_dist  | +5.2% |
| vol_20d    | 15.8% |
| mdd_60d    | 11.0% |
| rsi_14     |  51.1 |
| zscore_20d |   1.3 |

### Brent Crude Oil / BZ=F (score 59.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.1% |
| ret_5d     |  +1.6% |
| ret_20d    |  +1.0% |
| ret_60d    | +26.0% |
| ma20_dist  |  +2.4% |
| ma50_dist  |  +7.7% |
| vol_20d    |  31.6% |
| mdd_60d    |  12.5% |
| rsi_14     |   54.9 |
| zscore_20d |    1.1 |

### DAX / ^GDAXI (score 58.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +2.3% |
| ret_20d    | -1.3% |
| ret_60d    | +2.5% |
| ma20_dist  | +0.4% |
| ma50_dist  | -1.4% |
| vol_20d    | 13.1% |
| mdd_60d    |  6.6% |
| rsi_14     |  49.4 |
| zscore_20d |   0.5 |

### Meta Platforms Inc. / META (score 58.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.1% |
| ret_5d     |  +2.2% |
| ret_20d    |  +8.1% |
| ret_60d    | +17.5% |
| ma20_dist  |  +0.4% |
| ma50_dist  | +12.9% |
| vol_20d    |  55.1% |
| mdd_60d    |  11.1% |
| rsi_14     |   45.9 |
| zscore_20d |    0.1 |

### Alphabet Inc. Class A / GOOGL (score 53.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | +0.3% |
| ret_20d    | +0.5% |
| ret_60d    | +2.1% |
| ma20_dist  | +0.7% |
| ma50_dist  | +1.3% |
| vol_20d    | 20.4% |
| mdd_60d    | 12.4% |
| rsi_14     |  56.7 |
| zscore_20d |   0.5 |

### Amazon.com Inc. / AMZN (score 51.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +0.3% |
| ret_20d    | +1.4% |
| ret_60d    | +4.0% |
| ma20_dist  | +0.5% |
| ma50_dist  | -1.1% |
| vol_20d    | 23.1% |
| mdd_60d    | 13.4% |
| rsi_14     |  56.0 |
| zscore_20d |   0.3 |

### NASDAQ 100 / ^NDX (score 47.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | -2.6% |
| ret_20d    | +1.7% |
| ret_60d    | +3.2% |
| ma20_dist  | -2.0% |
| ma50_dist  | +0.2% |
| vol_20d    | 15.9% |
| mdd_60d    |  4.4% |
| rsi_14     |  38.3 |
| zscore_20d |  -1.6 |

### CAC 40 / ^FCHI (score 46.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.8% |
| ret_5d     | +2.7% |
| ret_20d    | -3.1% |
| ret_60d    | -4.4% |
| ma20_dist  | -0.1% |
| ma50_dist  | -3.4% |
| vol_20d    | 12.3% |
| mdd_60d    | 11.4% |
| rsi_14     |  40.5 |
| zscore_20d |  -0.1 |

### Euro Stoxx 50 / ^STOXX50E (score 44.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | +0.7% |
| ret_20d    | -2.4% |
| ret_60d    | -0.7% |
| ma20_dist  | -1.1% |
| ma50_dist  | -2.8% |
| vol_20d    | 12.5% |
| mdd_60d    |  6.5% |
| rsi_14     |  38.0 |
| zscore_20d |  -1.2 |

### JPMorgan Chase & Co. / JPM (score 42.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.1% |
| ret_5d     | +1.2% |
| ret_20d    | -3.5% |
| ret_60d    | -3.6% |
| ma20_dist  | +0.1% |
| ma50_dist  | -3.5% |
| vol_20d    | 17.0% |
| mdd_60d    |  9.9% |
| rsi_14     |  40.0 |
| zscore_20d |   0.1 |

### Gold / GC=F (score 40.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.5% |
| ret_5d     | +0.3% |
| ret_20d    | -5.2% |
| ret_60d    | +3.3% |
| ma20_dist  | -1.3% |
| ma50_dist  | -4.8% |
| vol_20d    | 17.8% |
| mdd_60d    | 12.7% |
| rsi_14     |  36.4 |
| zscore_20d |  -0.6 |

### Soybeans / ZS=F (score 38.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.1% |
| ret_5d     | -1.9% |
| ret_20d    | -4.3% |
| ret_60d    | +4.5% |
| ma20_dist  | -2.6% |
| ma50_dist  | -0.4% |
| vol_20d    | 14.6% |
| mdd_60d    |  5.3% |
| rsi_14     |  29.0 |
| zscore_20d |  -1.9 |

### Hang Seng / ^HSI (score 37.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | +1.2% |
| ret_20d    | -2.6% |
| ret_60d    | -3.3% |
| ma20_dist  | -1.5% |
| ma50_dist  | -3.8% |
| vol_20d    | 15.5% |
| mdd_60d    |  8.5% |
| rsi_14     |  37.9 |
| zscore_20d |  -1.1 |

### Tesla Inc. / TSLA (score 35.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.3% |
| ret_5d     | -3.3% |
| ret_20d    | -1.0% |
| ret_60d    | -3.1% |
| ma20_dist  | -2.3% |
| ma50_dist  | +1.0% |
| vol_20d    | 29.9% |
| mdd_60d    |  7.2% |
| rsi_14     |  44.1 |
| zscore_20d |  -0.9 |

### Russell 2000 / ^RUT (score 34.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.4% |
| ret_5d     | -1.0% |
| ret_20d    | -3.7% |
| ret_60d    | -6.5% |
| ma20_dist  | -1.8% |
| ma50_dist  | -5.0% |
| vol_20d    | 13.1% |
| mdd_60d    | 11.0% |
| rsi_14     |  37.2 |
| zscore_20d |  -1.4 |

### NVIDIA Corporation / NVDA (score 29.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.8% |
| ret_5d     | -5.7% |
| ret_20d    | -1.0% |
| ret_60d    | +2.4% |
| ma20_dist  | -5.0% |
| ma50_dist  | -2.6% |
| vol_20d    | 24.2% |
| mdd_60d    |  9.2% |
| rsi_14     |  41.1 |
| zscore_20d |  -2.1 |

### Wheat / ZW=F (score 23.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | -1.9% |
| ret_20d    | -7.8% |
| ret_60d    | +1.5% |
| ma20_dist  | -3.1% |
| ma50_dist  | -4.2% |
| vol_20d    | 20.6% |
| mdd_60d    | 12.7% |
| rsi_14     |  34.7 |
| zscore_20d |  -1.2 |

### Corn / ZC=F (score 21.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.6% |
| ret_5d     | -4.4% |
| ret_20d    | -9.9% |
| ret_60d    | +5.8% |
| ma20_dist  | -5.8% |
| ma50_dist  | -4.5% |
| vol_20d    | 25.0% |
| mdd_60d    | 12.0% |
| rsi_14     |  19.1 |
| zscore_20d |  -1.5 |

### Platinum / PL=F (score 18.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.6% |
| ret_5d     |  -0.9% |
| ret_20d    | -10.1% |
| ret_60d    |  -0.1% |
| ma20_dist  |  -5.5% |
| ma50_dist  |  -8.8% |
| vol_20d    |  30.7% |
| mdd_60d    |  16.4% |
| rsi_14     |   28.9 |
| zscore_20d |   -1.5 |

### Silver / SI=F (score 15.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.3% |
| ret_5d     |  -3.8% |
| ret_20d    | -13.2% |
| ret_60d    |  -0.8% |
| ma20_dist  |  -7.3% |
| ma50_dist  | -11.5% |
| vol_20d    |  34.1% |
| mdd_60d    |  20.0% |
| rsi_14     |   28.0 |
| zscore_20d |   -1.6 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Microsoft Corporation / MSFT        |  11.3521 |           2.1% |                 0.49x |       22.7043 |            4.2% |
| FTSE 100 / ^FTSE                    | 119.5356 |           1.1% |                 0.86x |      239.0711 |            2.2% |
| UnitedHealth Group Inc. / UNH       |  11.9264 |           2.9% |                 0.40x |       23.8529 |            5.9% |
| Dow Jones Industrial Average / ^DJI | 498.4445 |           1.0% |                 1.11x |      996.8890 |            1.9% |
| S&P 500 / ^GSPC                     |  65.9500 |           0.9% |                 1.07x |      131.9000 |            1.7% |
| Apple Inc. / AAPL                   |   6.5179 |           1.9% |                 0.63x |       13.0357 |            3.8% |
| Brent Crude Oil / BZ=F              |   3.9521 |           3.7% |                 0.32x |        7.9043 |            7.5% |
| DAX / ^GDAXI                        | 293.6062 |           1.2% |                 0.76x |      587.2123 |            2.3% |
| Meta Platforms Inc. / META          |  22.3064 |           3.0% |                 0.18x |       44.6129 |            6.1% |
| Alphabet Inc. Class A / GOOGL       |   8.4450 |           2.4% |                 0.49x |       16.8900 |            4.8% |
| Amazon.com Inc. / AMZN              |   5.7593 |           2.3% |                 0.43x |       11.5186 |            4.5% |
| NASDAQ 100 / ^NDX                   | 390.0774 |           1.3% |                 0.63x |      780.1549 |            2.6% |
| CAC 40 / ^FCHI                      |  89.7378 |           1.1% |                 0.82x |      179.4756 |            2.3% |
| Euro Stoxx 50 / ^STOXX50E           |  73.9508 |           1.2% |                 0.80x |      147.9015 |            2.4% |
| JPMorgan Chase & Co. / JPM          |   5.9646 |           1.8% |                 0.59x |       11.9292 |            3.6% |
| Gold / GC=F                         |  81.9357 |           2.0% |                 0.56x |      163.8713 |            3.9% |
| Soybeans / ZS=F                     |  21.5000 |           1.7% |                 0.68x |       43.0000 |            3.4% |
| Hang Seng / ^HSI                    | 355.2080 |           1.5% |                 0.64x |      710.4160 |            3.0% |
| Tesla Inc. / TSLA                   |  10.4386 |           2.9% |                 0.33x |       20.8771 |            5.8% |
| Russell 2000 / ^RUT                 |  35.3414 |           1.3% |                 0.77x |       70.6829 |            2.6% |
| NVIDIA Corporation / NVDA           |   5.9600 |           2.7% |                 0.41x |       11.9200 |            5.5% |
| Wheat / ZW=F                        |  16.4821 |           2.5% |                 0.49x |       32.9643 |            4.9% |
| Corn / ZC=F                         |  11.7500 |           2.5% |                 0.40x |       23.5000 |            4.9% |
| Platinum / PL=F                     |  35.4143 |           2.2% |                 0.33x |       70.8286 |            4.4% |
| Silver / SI=F                       |   1.4296 |           2.5% |                 0.29x |        2.8591 |            5.0% |

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

Scoring engine version: **1.0.0** | Git commit: **64cf559**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
