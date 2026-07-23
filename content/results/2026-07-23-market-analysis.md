+++
title = "Market Analysis 2026-07-23"
date = "2026-07-23T00:00:00+00:00"
draft = false
summary = "Bullish market: 26 reliable instruments. Top signal: ZW=F (score 80.3)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-07-23.json", "data/history/2026-07-23.json"]
market_regime = "Bullish"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "93a857a"
+++

## Market Regime

**Bullish** — 20 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Wheat / ZW=F** — score 80.3, 20d return +20.3%, RSI14=84. 20d up +20.3%; above MA20 by 12.9%; RSI14=84 ⚠️ Upcoming: FOMC rate decision (2026-07-29)
- **Soybeans / ZS=F** — score 70.9, 20d return +10.4%, RSI14=80. 20d up +10.4%; above MA20 by 5.0%; RSI14=80 ⚠️ Upcoming: FOMC rate decision (2026-07-29)
- **Corn / ZC=F** — score 67.9, 20d return +12.8%, RSI14=73. 20d up +12.8%; above MA20 by 6.8%; RSI14=73 ⚠️ Upcoming: FOMC rate decision (2026-07-29)
- **Brent Crude Oil / BZ=F** — score 67.6, 20d return +22.0%, RSI14=90. 20d up +22.0%; above MA20 by 18.6%; RSI14=90 ⚠️ Upcoming: FOMC rate decision (2026-07-29)
- **JPMorgan Chase & Co. / JPM** — score 66.7, 20d return +4.7%, RSI14=65. 20d up +4.7%; above MA20 by 3.4%; RSI14=65 ⚠️ Upcoming: FOMC rate decision (2026-07-29)

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                 | Applies To                      |
| ---------- | --------------------- | ------------------------------- |
| 2026-07-29 | FOMC rate decision    | Commodity, Equity, Equity Index |
| 2026-07-29 | META earnings release | META                            |
| 2026-07-29 | MSFT earnings release | MSFT                            |
| 2026-07-30 | AAPL earnings release | AAPL                            |
| 2026-07-30 | AMZN earnings release | AMZN                            |

## Signal History

Compared with the previous available report (**2026-07-22**).
- **New top-5:** BZ=F, ZC=F
- **Persistent top signals:** ZW=F (13 reports), ZS=F (7 reports), JPM (2 reports)
- **Dropped from top-5:** AAPL, UNH

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +0 |    -3.0 |
| 7203.T    |     -1 |    -3.3 |
| 8306.T    |     +0 |    +3.9 |
| AAPL      |     -3 |    -7.9 |
| AMZN      |     -5 |    -7.3 |
| BZ=F      |     +2 |    +4.5 |
| CL=F      |     +2 |    +3.9 |
| GC=F      |     +6 |   +12.1 |
| GOOGL     |     +0 |    -3.3 |
| HG=F      |     -1 |    -8.2 |
| JPM       |     -2 |    -2.1 |
| META      |     -5 |   -10.6 |
| MSFT      |    -10 |   -16.1 |
| NG=F      |     +2 |   +10.0 |
| NVDA      |     +8 |   +15.8 |
| PL=F      |     +4 |    +3.9 |
| SI=F      |     +2 |    +8.2 |
| TSLA      |     +0 |    -7.3 |
| UNH       |     -6 |   -13.9 |
| XOM       |     +0 |    +1.5 |
| ZC=F      |     +4 |    +6.1 |
| ZS=F      |     +3 |    +7.6 |
| ZW=F      |     +0 |    +7.0 |
| ^DJI      |     +0 |    -0.9 |
| ^FCHI     |     +4 |    +8.8 |
| ^FTSE     |     +3 |   +12.7 |
| ^GDAXI    |     +1 |    +3.9 |
| ^GSPC     |     -3 |    -4.2 |
| ^HSI      |     -2 |    -5.5 |
| ^N225     |     +0 |    -5.5 |
| ^NDX      |     +2 |    -1.5 |
| ^RUT      |     -6 |   -11.8 |
| ^STOXX50E |     +1 |    +2.4 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input
- **Copper / HG=F** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Nikkei 225 / ^N225** — missing_bars

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|    1 | Wheat / ZW=F           |  80.3 |   Yes    | —               | 20d up +20.3%; above MA20 by 12.9%; RSI14=84 |
|    2 | Soybeans / ZS=F        |  70.9 |   Yes    | —               | 20d up +10.4%; above MA20 by 5.0%; RSI14=80  |
|    3 | Corn / ZC=F            |  67.9 |   Yes    | —               | 20d up +12.8%; above MA20 by 6.8%; RSI14=73  |
|    4 | Brent Crude Oil / BZ=F |  67.6 |   Yes    | —               | 20d up +22.0%; above MA20 by 18.6%; RSI14=90 |
|   14 | Gold / GC=F            |  47.0 |   Yes    | —               | 20d up +0.4%; above MA20 by 2.1%; RSI14=56   |
|   18 | Platinum / PL=F        |  33.9 |   Yes    | —               | 20d down -1.1%; above MA20 by 2.0%; RSI14=58 |
|   21 | Silver / SI=F          |  31.2 |   Yes    | —               | 20d down -3.2%; above MA20 by 2.0%; RSI14=50 |
|   22 | Natural Gas / NG=F     |  30.3 |   Yes    | —               | 20d down -7.1%; below MA20 by 4.9%; RSI14=30 |
|   29 | WTI Crude Oil / CL=F   |  63.9 |    No    | malformed_input | Suppressed: malformed_input                  |
|   30 | Copper / HG=F          |  60.6 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    5 | JPMorgan Chase & Co. / JPM                                                     |  66.7 |   Yes    | —                             | 20d up +4.7%; above MA20 by 3.4%; RSI14=65   |
|    7 | Apple Inc. / AAPL                                                              |  60.3 |   Yes    | —                             | 20d up +10.7%; above MA20 by 5.1%; RSI14=76  |
|    8 | UnitedHealth Group Inc. / UNH                                                  |  57.9 |   Yes    | —                             | 20d up +5.4%; above MA20 by 1.8%; RSI14=53   |
|   11 | NVIDIA Corporation / NVDA                                                      |  51.8 |   Yes    | —                             | 20d up +6.0%; above MA20 by 4.8%; RSI14=63   |
|   20 | Meta Platforms Inc. / META                                                     |  31.5 |   Yes    | —                             | 20d up +11.6%; above MA20 by 1.8%; RSI14=53  |
|   23 | Amazon.com Inc. / AMZN                                                         |  29.4 |   Yes    | —                             | 20d up +4.6%; above MA20 by 0.5%; RSI14=54   |
|   24 | Microsoft Corporation / MSFT                                                   |  26.7 |   Yes    | —                             | 20d up +4.4%; above MA20 by 1.5%; RSI14=54   |
|   25 | Alphabet Inc. Class A / GOOGL                                                  |  15.2 |   Yes    | —                             | 20d down -1.2%; below MA20 by 3.6%; RSI14=38 |
|   26 | Tesla Inc. / TSLA                                                              |  10.0 |   Yes    | —                             | 20d down -2.0%; below MA20 by 5.2%; RSI14=33 |
|   27 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  77.9 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   28 | Exxon Mobil Corporation / XOM                                                  |  71.5 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   31 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  57.3 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   32 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  50.3 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    6 | FTSE 100 / ^FTSE                    |  65.8 |   Yes    | —            | 20d up +2.4%; above MA20 by 1.5%; RSI14=55   |
|    9 | Euro Stoxx 50 / ^STOXX50E           |  53.9 |   Yes    | —            | 20d up +1.6%; above MA20 by 0.5%; RSI14=46   |
|   10 | Hang Seng / ^HSI                    |  52.4 |   Yes    | —            | 20d up +6.7%; above MA20 by 3.9%; RSI14=74   |
|   12 | CAC 40 / ^FCHI                      |  50.9 |   Yes    | —            | 20d up +0.6%; above MA20 by 0.6%; RSI14=47   |
|   13 | Dow Jones Industrial Average / ^DJI |  47.3 |   Yes    | —            | 20d up +1.1%; below MA20 by 0.3%; RSI14=49   |
|   15 | S&P 500 / ^GSPC                     |  45.5 |   Yes    | —            | 20d up +1.8%; above MA20 by 0.2%; RSI14=52   |
|   16 | DAX / ^GDAXI                        |  45.1 |   Yes    | —            | 20d up +1.7%; above MA20 by 0.2%; RSI14=40   |
|   17 | Russell 2000 / ^RUT                 |  39.4 |   Yes    | —            | 20d down -0.5%; below MA20 by 0.8%; RSI14=41 |
|   19 | NASDAQ 100 / ^NDX                   |  33.3 |   Yes    | —            | 20d down -1.2%; below MA20 by 1.3%; RSI14=41 |
|   33 | Nikkei 225 / ^N225                  |  26.4 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-07-22 |
| 7203.T    | 2026-07-22 |
| 8306.T    | 2026-07-22 |
| AAPL      | 2026-07-22 |
| AMZN      | 2026-07-22 |
| BZ=F      | 2026-07-22 |
| CL=F      | 2026-07-22 |
| GC=F      | 2026-07-22 |
| GOOGL     | 2026-07-22 |
| HG=F      | 2026-07-22 |
| JPM       | 2026-07-22 |
| META      | 2026-07-22 |
| MSFT      | 2026-07-22 |
| NG=F      | 2026-07-22 |
| NVDA      | 2026-07-22 |
| PL=F      | 2026-07-22 |
| SI=F      | 2026-07-22 |
| TSLA      | 2026-07-22 |
| UNH       | 2026-07-22 |
| XOM       | 2026-07-22 |
| ZC=F      | 2026-07-22 |
| ZS=F      | 2026-07-22 |
| ZW=F      | 2026-07-22 |
| ^DJI      | 2026-07-22 |
| ^FCHI     | 2026-07-22 |
| ^FTSE     | 2026-07-22 |
| ^GDAXI    | 2026-07-22 |
| ^GSPC     | 2026-07-22 |
| ^HSI      | 2026-07-22 |
| ^N225     | 2026-07-22 |
| ^NDX      | 2026-07-22 |
| ^RUT      | 2026-07-22 |
| ^STOXX50E | 2026-07-22 |

## Symbol Details

### Wheat / ZW=F (score 80.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +4.1% |
| ret_5d     |  +4.2% |
| ret_20d    | +20.3% |
| ret_60d    | +16.0% |
| ma20_dist  | +12.9% |
| ma50_dist  | +13.9% |
| vol_20d    |  35.1% |
| mdd_60d    |  14.6% |
| rsi_14     |   83.6 |
| zscore_20d |    2.0 |

### Soybeans / ZS=F (score 70.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.1% |
| ret_5d     |  +2.6% |
| ret_20d    | +10.4% |
| ret_60d    |  +6.0% |
| ma20_dist  |  +5.0% |
| ma50_dist  |  +5.7% |
| vol_20d    |  20.6% |
| mdd_60d    |   8.8% |
| rsi_14     |   79.9 |
| zscore_20d |    1.4 |

### Corn / ZC=F (score 67.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.0% |
| ret_5d     |  +3.2% |
| ret_20d    | +12.8% |
| ret_60d    |  +1.5% |
| ma20_dist  |  +6.8% |
| ma50_dist  |  +5.8% |
| vol_20d    |  27.5% |
| mdd_60d    |  15.7% |
| rsi_14     |   72.5 |
| zscore_20d |    1.8 |

### Brent Crude Oil / BZ=F (score 67.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +3.4% |
| ret_5d     | +10.7% |
| ret_20d    | +22.0% |
| ret_60d    | -10.7% |
| ma20_dist  | +18.6% |
| ma50_dist  |  +5.9% |
| vol_20d    |  50.3% |
| mdd_60d    |  39.4% |
| rsi_14     |   90.2 |
| zscore_20d |    2.1 |

### JPMorgan Chase & Co. / JPM (score 66.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.9% |
| ret_5d     |  +0.4% |
| ret_20d    |  +4.7% |
| ret_60d    | +13.5% |
| ma20_dist  |  +3.4% |
| ma50_dist  |  +9.0% |
| vol_20d    |  20.1% |
| mdd_60d    |   6.1% |
| rsi_14     |   64.8 |
| zscore_20d |    1.8 |

### FTSE 100 / ^FTSE (score 65.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.2% |
| ret_5d     | +1.9% |
| ret_20d    | +2.4% |
| ret_60d    | +3.8% |
| ma20_dist  | +1.5% |
| ma50_dist  | +2.5% |
| vol_20d    | 10.6% |
| mdd_60d    |  2.6% |
| rsi_14     |  54.7 |
| zscore_20d |   2.1 |

### Apple Inc. / AAPL (score 60.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.6% |
| ret_5d     |  -0.5% |
| ret_20d    | +10.7% |
| ret_60d    | +20.3% |
| ma20_dist  |  +5.1% |
| ma50_dist  |  +6.9% |
| vol_20d    |  36.4% |
| mdd_60d    |  12.7% |
| rsi_14     |   76.2 |
| zscore_20d |    0.9 |

### UnitedHealth Group Inc. / UNH (score 57.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.2% |
| ret_5d     |  +3.1% |
| ret_20d    |  +5.4% |
| ret_60d    | +22.2% |
| ma20_dist  |  +1.8% |
| ma50_dist  |  +6.4% |
| vol_20d    |  27.6% |
| mdd_60d    |   6.1% |
| rsi_14     |   52.9 |
| zscore_20d |    1.1 |

### Euro Stoxx 50 / ^STOXX50E (score 53.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | +0.8% |
| ret_20d    | +1.6% |
| ret_60d    | +7.4% |
| ma20_dist  | +0.5% |
| ma50_dist  | +2.5% |
| vol_20d    | 13.7% |
| mdd_60d    |  3.6% |
| rsi_14     |  46.0 |
| zscore_20d |   0.5 |

### Hang Seng / ^HSI (score 52.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | +0.9% |
| ret_20d    | +6.7% |
| ret_60d    | -3.9% |
| ma20_dist  | +3.9% |
| ma50_dist  | +0.8% |
| vol_20d    | 20.4% |
| mdd_60d    | 14.9% |
| rsi_14     |  74.1 |
| zscore_20d |   1.2 |

### NVIDIA Corporation / NVDA (score 51.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.3% |
| ret_5d     | -0.2% |
| ret_20d    | +6.0% |
| ret_60d    | +1.8% |
| ma20_dist  | +4.8% |
| ma50_dist  | +1.1% |
| vol_20d    | 34.6% |
| mdd_60d    | 18.3% |
| rsi_14     |  62.7 |
| zscore_20d |   1.6 |

### CAC 40 / ^FCHI (score 50.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | +0.7% |
| ret_20d    | +0.6% |
| ret_60d    | +4.1% |
| ma20_dist  | +0.6% |
| ma50_dist  | +1.8% |
| vol_20d    | 12.0% |
| mdd_60d    |  4.2% |
| rsi_14     |  46.7 |
| zscore_20d |   0.9 |

### Dow Jones Industrial Average / ^DJI (score 47.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.0% |
| ret_5d     | -0.8% |
| ret_20d    | +1.1% |
| ret_60d    | +6.1% |
| ma20_dist  | -0.3% |
| ma50_dist  | +1.7% |
| vol_20d    |  7.9% |
| mdd_60d    |  3.2% |
| rsi_14     |  48.7 |
| zscore_20d |  -0.4 |

### Gold / GC=F (score 47.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.9% |
| ret_5d     |  +2.5% |
| ret_20d    |  +0.4% |
| ret_60d    | -12.2% |
| ma20_dist  |  +2.1% |
| ma50_dist  |  -3.1% |
| vol_20d    |  23.3% |
| mdd_60d    |  15.6% |
| rsi_14     |   55.9 |
| zscore_20d |    1.6 |

### S&P 500 / ^GSPC (score 45.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | -1.0% |
| ret_20d    | +1.8% |
| ret_60d    | +4.7% |
| ma20_dist  | +0.2% |
| ma50_dist  | +0.4% |
| vol_20d    |  9.1% |
| mdd_60d    |  4.5% |
| rsi_14     |  51.5 |
| zscore_20d |   0.2 |

### DAX / ^GDAXI (score 45.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | +0.6% |
| ret_20d    | +1.7% |
| ret_60d    | +4.7% |
| ma20_dist  | +0.2% |
| ma50_dist  | +1.0% |
| vol_20d    | 15.6% |
| mdd_60d    |  4.7% |
| rsi_14     |  40.1 |
| zscore_20d |   0.2 |

### Russell 2000 / ^RUT (score 39.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.9% |
| ret_5d     | -0.5% |
| ret_20d    | -0.5% |
| ret_60d    | +6.2% |
| ma20_dist  | -0.8% |
| ma50_dist  | +1.1% |
| vol_20d    | 11.0% |
| mdd_60d    |  4.8% |
| rsi_14     |  40.9 |
| zscore_20d |  -1.1 |

### Platinum / PL=F (score 33.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.1% |
| ret_5d     |  +0.7% |
| ret_20d    |  -1.1% |
| ret_60d    | -18.5% |
| ma20_dist  |  +2.0% |
| ma50_dist  |  -7.1% |
| vol_20d    |  34.8% |
| mdd_60d    |  29.1% |
| rsi_14     |   58.4 |
| zscore_20d |    1.3 |

### NASDAQ 100 / ^NDX (score 33.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | -1.7% |
| ret_20d    | -1.2% |
| ret_60d    | +6.2% |
| ma20_dist  | -1.3% |
| ma50_dist  | -1.9% |
| vol_20d    | 21.3% |
| mdd_60d    |  7.0% |
| rsi_14     |  41.2 |
| zscore_20d |  -0.9 |

### Meta Platforms Inc. / META (score 31.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.6% |
| ret_5d     |  -7.9% |
| ret_20d    | +11.6% |
| ret_60d    |  -7.0% |
| ma20_dist  |  +1.8% |
| ma50_dist  |  +3.5% |
| vol_20d    |  52.7% |
| mdd_60d    |  19.9% |
| rsi_14     |   53.1 |
| zscore_20d |    0.3 |

### Silver / SI=F (score 31.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.0% |
| ret_5d     |  +5.1% |
| ret_20d    |  -3.2% |
| ret_60d    | -21.4% |
| ma20_dist  |  +2.0% |
| ma50_dist  | -11.2% |
| vol_20d    |  42.7% |
| mdd_60d    |  37.1% |
| rsi_14     |   49.8 |
| zscore_20d |    0.8 |

### Natural Gas / NG=F (score 30.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.1% |
| ret_5d     |  +0.0% |
| ret_20d    |  -7.1% |
| ret_60d    | +15.9% |
| ma20_dist  |  -4.9% |
| ma50_dist  |  -5.3% |
| vol_20d    |  37.5% |
| mdd_60d    |  14.5% |
| rsi_14     |   29.6 |
| zscore_20d |   -0.9 |

### Amazon.com Inc. / AMZN (score 29.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.1% |
| ret_5d     | -4.0% |
| ret_20d    | +4.6% |
| ret_60d    | -7.3% |
| ma20_dist  | +0.5% |
| ma50_dist  | -2.3% |
| vol_20d    | 25.2% |
| mdd_60d    | 17.4% |
| rsi_14     |  54.3 |
| zscore_20d |   0.2 |

### Microsoft Corporation / MSFT (score 26.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.9% |
| ret_5d     | -1.3% |
| ret_20d    | +4.4% |
| ret_60d    | -7.9% |
| ma20_dist  | +1.5% |
| ma50_dist  | -2.5% |
| vol_20d    | 34.3% |
| mdd_60d    | 23.4% |
| rsi_14     |  54.0 |
| zscore_20d |   0.5 |

### Alphabet Inc. Class A / GOOGL (score 15.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.5% |
| ret_5d     | -7.8% |
| ret_20d    | -1.2% |
| ret_60d    | -0.6% |
| ma20_dist  | -3.6% |
| ma50_dist  | -6.9% |
| vol_20d    | 32.1% |
| mdd_60d    | 16.2% |
| rsi_14     |  38.1 |
| zscore_20d |  -1.4 |

### Tesla Inc. / TSLA (score 10.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.3% |
| ret_5d     | -5.2% |
| ret_20d    | -2.0% |
| ret_60d    | -0.6% |
| ma20_dist  | -5.2% |
| ma50_dist  | -8.2% |
| vol_20d    | 55.9% |
| mdd_60d    | 17.0% |
| rsi_14     |  33.2 |
| zscore_20d |  -1.3 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Wheat / ZW=F                        |  18.9107 |           2.7% |                 0.29x |       37.8214 |            5.4% |
| Soybeans / ZS=F                     |  19.5893 |           1.6% |                 0.49x |       39.1786 |            3.2% |
| Corn / ZC=F                         |  10.0179 |           2.2% |                 0.36x |       20.0357 |            4.3% |
| Brent Crude Oil / BZ=F              |   4.0386 |           4.3% |                 0.20x |        8.0771 |            8.6% |
| JPMorgan Chase & Co. / JPM          |   7.8917 |           2.3% |                 0.50x |       15.7833 |            4.5% |
| FTSE 100 / ^FTSE                    | 114.6430 |           1.1% |                 0.95x |      229.2860 |            2.1% |
| Apple Inc. / AAPL                   |   8.1093 |           2.5% |                 0.27x |       16.2186 |            5.0% |
| UnitedHealth Group Inc. / UNH       |  12.8286 |           3.0% |                 0.36x |       25.6571 |            5.9% |
| Euro Stoxx 50 / ^STOXX50E           |  68.8528 |           1.1% |                 0.73x |      137.7056 |            2.2% |
| Hang Seng / ^HSI                    | 496.0205 |           2.0% |                 0.49x |      992.0410 |            4.0% |
| NVIDIA Corporation / NVDA           |   7.4607 |           3.5% |                 0.29x |       14.9214 |            7.0% |
| CAC 40 / ^FCHI                      |  94.5758 |           1.1% |                 0.83x |      189.1515 |            2.2% |
| Dow Jones Industrial Average / ^DJI | 528.1225 |           1.0% |                 1.26x |     1056.2450 |            2.0% |
| Gold / GC=F                         |  70.7429 |           1.7% |                 0.43x |      141.4858 |            3.4% |
| S&P 500 / ^GSPC                     |  70.1772 |           0.9% |                 1.10x |      140.3544 |            1.9% |
| DAX / ^GDAXI                        | 291.5725 |           1.2% |                 0.64x |      583.1451 |            2.3% |
| Russell 2000 / ^RUT                 |  38.8722 |           1.3% |                 0.91x |       77.7443 |            2.6% |
| Platinum / PL=F                     |  29.0929 |           1.8% |                 0.29x |       58.1857 |            3.5% |
| NASDAQ 100 / ^NDX                   | 562.6002 |           1.9% |                 0.47x |     1125.2003 |            3.9% |
| Meta Platforms Inc. / META          |  27.4643 |           4.4% |                 0.19x |       54.9286 |            8.8% |
| Silver / SI=F                       |   1.8434 |           3.1% |                 0.23x |        3.6867 |            6.1% |
| Natural Gas / NG=F                  |   0.1128 |           3.9% |                 0.27x |        0.2256 |            7.7% |
| Amazon.com Inc. / AMZN              |   6.3957 |           2.6% |                 0.40x |       12.7914 |            5.2% |
| Microsoft Corporation / MSFT        |  10.7771 |           2.8% |                 0.29x |       21.5543 |            5.5% |
| Alphabet Inc. Class A / GOOGL       |  10.6657 |           3.1% |                 0.31x |       21.3314 |            6.2% |
| Tesla Inc. / TSLA                   |  16.6243 |           4.4% |                 0.18x |       33.2486 |            8.9% |

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

Scoring engine version: **1.0.0** | Git commit: **93a857a**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
