+++
title = "Market Analysis 2026-09-10"
date = "2026-09-10T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: BZ=F (score 78.2)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-09-10.json", "data/history/2026-09-10.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "92eec55"
+++

## Market Regime

**Neutral** — 9 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Brent Crude Oil / BZ=F** — score 78.2, 20d return +14.3%, RSI14=66. 20d up +14.3%; above MA20 by 8.9%; RSI14=66 ⚠️ Upcoming: FOMC rate decision (2026-09-16)
- **Meta Platforms Inc. / META** — score 75.8, 20d return +9.1%, RSI14=90. 20d up +9.1%; above MA20 by 12.6%; RSI14=90 ⚠️ Upcoming: FOMC rate decision (2026-09-16)
- **Platinum / PL=F** — score 75.8, 20d return +9.4%, RSI14=54. 20d up +9.4%; above MA20 by 4.9%; RSI14=54 ⚠️ Upcoming: FOMC rate decision (2026-09-16)
- **Soybeans / ZS=F** — score 70.0, 20d return +10.9%, RSI14=73. 20d up +10.9%; above MA20 by 3.7%; RSI14=73 ⚠️ Upcoming: FOMC rate decision (2026-09-16)
- **Corn / ZC=F** — score 62.7, 20d return +13.3%, RSI14=62. 20d up +13.3%; above MA20 by 2.0%; RSI14=62 ⚠️ Upcoming: FOMC rate decision (2026-09-16)

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event              | Applies To                      |
| ---------- | ------------------ | ------------------------------- |
| 2026-09-16 | FOMC rate decision | Commodity, Equity, Equity Index |

## Signal History

Compared with the previous available report (**2026-09-09**).

- **New top-5:** None
- **Persistent top signals:** ZC=F (21 reports), ZS=F (14 reports), BZ=F (4 reports), META (4 reports), PL=F (2 reports)
- **Dropped from top-5:** None

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +0 |    +3.6 |
| 7203.T    |     +0 |    +7.3 |
| 8306.T    |     -1 |    -5.2 |
| AAPL      |     +1 |    +1.8 |
| AMZN      |     +0 |    -6.1 |
| BZ=F      |     +1 |    +2.4 |
| CL=F      |     +0 |    +1.5 |
| GC=F      |     +5 |   +11.8 |
| GOOGL     |     +0 |    -9.1 |
| HG=F      |     +0 |    -1.2 |
| JPM       |    +11 |   +18.2 |
| META      |     +2 |   +11.8 |
| MSFT      |     +7 |    +6.1 |
| NG=F      |     -2 |   -17.3 |
| NVDA      |     +0 |    -0.9 |
| PL=F      |     +2 |   +12.1 |
| SI=F      |    +13 |   +21.8 |
| TSLA      |     -1 |    +0.3 |
| UNH       |     -8 |   -16.1 |
| XOM       |     +1 |   +15.2 |
| ZC=F      |     -2 |    -2.7 |
| ZS=F      |     -3 |    -8.8 |
| ZW=F      |     -8 |   -14.8 |
| ^DJI      |     +5 |    +4.2 |
| ^FCHI     |     -2 |   -12.4 |
| ^FTSE     |    -10 |   -15.8 |
| ^GDAXI    |    -10 |   -16.4 |
| ^GSPC     |     +1 |    +3.0 |
| ^HSI      |     +1 |    +6.4 |
| ^N225     |     +2 |   +12.1 |
| ^NDX      |     +3 |    +4.8 |
| ^RUT      |     +0 |    -2.7 |
| ^STOXX50E |     -8 |   -15.2 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **WTI Crude Oil / CL=F** — malformed_input
- **Copper / HG=F** — malformed_input
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Nikkei 225 / ^N225** — missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Natural Gas / NG=F** — malformed_input
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                 |
| ---: | ---------------------- | ----: | :------: | --------------- | ------------------------------------------- |
|    1 | Brent Crude Oil / BZ=F |  78.2 |   Yes    | —               | 20d up +14.3%; above MA20 by 8.9%; RSI14=66 |
|    3 | Platinum / PL=F        |  75.8 |   Yes    | —               | 20d up +9.4%; above MA20 by 4.9%; RSI14=54  |
|    4 | Soybeans / ZS=F        |  70.0 |   Yes    | —               | 20d up +10.9%; above MA20 by 3.7%; RSI14=73 |
|    5 | Corn / ZC=F            |  62.7 |   Yes    | —               | 20d up +13.3%; above MA20 by 2.0%; RSI14=62 |
|    6 | Silver / SI=F          |  59.4 |   Yes    | —               | 20d up +4.5%; above MA20 by 1.4%; RSI14=45  |
|   14 | Wheat / ZW=F           |  48.5 |   Yes    | —               | 20d up +9.0%; below MA20 by 0.1%; RSI14=56  |
|   15 | Gold / GC=F            |  48.2 |   Yes    | —               | 20d up +0.8%; below MA20 by 1.7%; RSI14=37  |
|   26 | WTI Crude Oil / CL=F   |  78.5 |    No    | malformed_input | Suppressed: malformed_input                 |
|   27 | Copper / HG=F          |  73.0 |    No    | malformed_input | Suppressed: malformed_input                 |
|   32 | Natural Gas / NG=F     |  31.5 |    No    | malformed_input | Suppressed: malformed_input                 |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    2 | Meta Platforms Inc. / META                                                     |  75.8 |   Yes    | —                             | 20d up +9.1%; above MA20 by 12.6%; RSI14=90  |
|    7 | JPMorgan Chase & Co. / JPM                                                     |  57.3 |   Yes    | —                             | 20d down -2.0%; below MA20 by 0.8%; RSI14=46 |
|    8 | NVIDIA Corporation / NVDA                                                      |  54.9 |   Yes    | —                             | 20d up +2.8%; above MA20 by 1.3%; RSI14=54   |
|    9 | Microsoft Corporation / MSFT                                                   |  54.2 |   Yes    | —                             | 20d down -2.2%; below MA20 by 0.5%; RSI14=55 |
|   10 | Tesla Inc. / TSLA                                                              |  53.9 |   Yes    | —                             | 20d up +10.5%; above MA20 by 4.5%; RSI14=56  |
|   13 | Apple Inc. / AAPL                                                              |  50.3 |   Yes    | —                             | 20d up +3.4%; above MA20 by 0.4%; RSI14=48   |
|   21 | UnitedHealth Group Inc. / UNH                                                  |  33.3 |   Yes    | —                             | 20d down -2.3%; below MA20 by 0.8%; RSI14=54 |
|   24 | Amazon.com Inc. / AMZN                                                         |  23.3 |   Yes    | —                             | 20d down -7.3%; below MA20 by 3.0%; RSI14=36 |
|   25 | Alphabet Inc. Class A / GOOGL                                                  |  14.8 |   Yes    | —                             | 20d down -3.8%; below MA20 by 3.3%; RSI14=38 |
|   28 | Exxon Mobil Corporation / XOM                                                  |  67.9 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   29 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  48.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   31 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  33.3 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   33 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  25.1 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|   11 | S&P 500 / ^GSPC                     |  53.6 |   Yes    | —            | 20d down -1.2%; below MA20 by 0.8%; RSI14=43 |
|   12 | NASDAQ 100 / ^NDX                   |  53.3 |   Yes    | —            | 20d down -0.4%; below MA20 by 0.2%; RSI14=50 |
|   16 | Hang Seng / ^HSI                    |  48.2 |   Yes    | —            | 20d down -0.6%; below MA20 by 0.8%; RSI14=41 |
|   17 | FTSE 100 / ^FTSE                    |  44.5 |   Yes    | —            | 20d down -1.6%; below MA20 by 1.1%; RSI14=44 |
|   18 | Dow Jones Industrial Average / ^DJI |  39.7 |   Yes    | —            | 20d down -2.6%; below MA20 by 1.8%; RSI14=39 |
|   19 | Euro Stoxx 50 / ^STOXX50E           |  35.8 |   Yes    | —            | 20d down -3.4%; below MA20 by 2.0%; RSI14=38 |
|   20 | DAX / ^GDAXI                        |  35.5 |   Yes    | —            | 20d down -2.9%; below MA20 by 2.1%; RSI14=40 |
|   22 | Russell 2000 / ^RUT                 |  33.3 |   Yes    | —            | 20d down -3.5%; below MA20 by 2.5%; RSI14=33 |
|   23 | CAC 40 / ^FCHI                      |  23.9 |   Yes    | —            | 20d down -6.0%; below MA20 by 3.0%; RSI14=27 |
|   30 | Nikkei 225 / ^N225                  |  33.9 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-09-09 |
| 7203.T    | 2026-09-09 |
| 8306.T    | 2026-09-09 |
| AAPL      | 2026-09-09 |
| AMZN      | 2026-09-09 |
| BZ=F      | 2026-09-09 |
| CL=F      | 2026-09-09 |
| GC=F      | 2026-09-09 |
| GOOGL     | 2026-09-09 |
| HG=F      | 2026-09-09 |
| JPM       | 2026-09-09 |
| META      | 2026-09-09 |
| MSFT      | 2026-09-09 |
| NG=F      | 2026-09-09 |
| NVDA      | 2026-09-09 |
| PL=F      | 2026-09-09 |
| SI=F      | 2026-09-09 |
| TSLA      | 2026-09-09 |
| UNH       | 2026-09-09 |
| XOM       | 2026-09-09 |
| ZC=F      | 2026-09-09 |
| ZS=F      | 2026-09-09 |
| ZW=F      | 2026-09-09 |
| ^DJI      | 2026-09-09 |
| ^FCHI     | 2026-09-09 |
| ^FTSE     | 2026-09-09 |
| ^GDAXI    | 2026-09-09 |
| ^GSPC     | 2026-09-09 |
| ^HSI      | 2026-09-09 |
| ^N225     | 2026-09-09 |
| ^NDX      | 2026-09-09 |
| ^RUT      | 2026-09-09 |
| ^STOXX50E | 2026-09-09 |

## Symbol Details

### Brent Crude Oil / BZ=F (score 78.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +3.4% |
| ret_5d     |  +5.8% |
| ret_20d    | +14.3% |
| ret_60d    | +26.8% |
| ma20_dist  |  +8.9% |
| ma50_dist  | +14.0% |
| vol_20d    |  28.4% |
| mdd_60d    |  21.2% |
| rsi_14     |   66.3 |
| zscore_20d |    2.4 |

### Meta Platforms Inc. / META (score 75.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +6.6% |
| ret_5d     | +13.0% |
| ret_20d    |  +9.1% |
| ret_60d    | +15.4% |
| ma20_dist  | +12.6% |
| ma50_dist  |  +9.2% |
| vol_20d    |  38.9% |
| mdd_60d    |  20.9% |
| rsi_14     |   89.6 |
| zscore_20d |    2.7 |

### Platinum / PL=F (score 75.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +3.6% |
| ret_5d     |  +8.8% |
| ret_20d    |  +9.4% |
| ret_60d    | +12.3% |
| ma20_dist  |  +4.9% |
| ma50_dist  | +10.9% |
| vol_20d    |  32.6% |
| mdd_60d    |   7.2% |
| rsi_14     |   54.1 |
| zscore_20d |    1.8 |

### Soybeans / ZS=F (score 70.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.6% |
| ret_5d     |  -0.9% |
| ret_20d    | +10.9% |
| ret_60d    | +14.4% |
| ma20_dist  |  +3.7% |
| ma50_dist  |  +6.8% |
| vol_20d    |  16.0% |
| mdd_60d    |   8.1% |
| rsi_14     |   72.9 |
| zscore_20d |    1.1 |

### Corn / ZC=F (score 62.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.6% |
| ret_5d     |  -2.6% |
| ret_20d    | +13.3% |
| ret_60d    | +20.6% |
| ma20_dist  |  +2.0% |
| ma50_dist  |  +8.8% |
| vol_20d    |  44.5% |
| mdd_60d    |   6.0% |
| rsi_14     |   61.8 |
| zscore_20d |    0.5 |

### Silver / SI=F (score 59.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.5% |
| ret_5d     | +5.0% |
| ret_20d    | +4.5% |
| ret_60d    | +2.5% |
| ma20_dist  | +1.4% |
| ma50_dist  | +8.2% |
| vol_20d    | 32.5% |
| mdd_60d    | 14.7% |
| rsi_14     |  44.6 |
| zscore_20d |   0.6 |

### JPMorgan Chase & Co. / JPM (score 57.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.3% |
| ret_5d     |  -0.1% |
| ret_20d    |  -2.0% |
| ret_60d    | +11.1% |
| ma20_dist  |  -0.8% |
| ma50_dist  |  +1.1% |
| vol_20d    |  14.3% |
| mdd_60d    |   3.7% |
| rsi_14     |   46.5 |
| zscore_20d |   -0.8 |

### NVIDIA Corporation / NVDA (score 54.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.9% |
| ret_5d     | +2.9% |
| ret_20d    | +2.8% |
| ret_60d    | +9.0% |
| ma20_dist  | +1.3% |
| ma50_dist  | +5.6% |
| vol_20d    | 43.9% |
| mdd_60d    | 10.6% |
| rsi_14     |  54.2 |
| zscore_20d |   0.5 |

### Microsoft Corporation / MSFT (score 54.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.5% |
| ret_5d     |  -1.9% |
| ret_20d    |  -2.2% |
| ret_60d    | +25.8% |
| ma20_dist  |  -0.5% |
| ma50_dist  |  +9.6% |
| vol_20d    |  22.6% |
| mdd_60d    |  11.7% |
| rsi_14     |   55.0 |
| zscore_20d |   -0.3 |

### Tesla Inc. / TSLA (score 53.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.1% |
| ret_5d     |  +3.3% |
| ret_20d    | +10.5% |
| ret_60d    |  -9.5% |
| ma20_dist  |  +4.5% |
| ma50_dist  |  +3.1% |
| vol_20d    |  51.1% |
| mdd_60d    |  29.9% |
| rsi_14     |   55.7 |
| zscore_20d |    1.3 |

### S&P 500 / ^GSPC (score 53.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | +0.1% |
| ret_20d    | -1.2% |
| ret_60d    | +2.8% |
| ma20_dist  | -0.8% |
| ma50_dist  | +0.5% |
| vol_20d    |  8.4% |
| mdd_60d    |  3.4% |
| rsi_14     |  43.2 |
| zscore_20d |  -1.4 |

### NASDAQ 100 / ^NDX (score 53.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | +1.2% |
| ret_20d    | -0.4% |
| ret_60d    | -0.7% |
| ma20_dist  | -0.2% |
| ma50_dist  | +0.7% |
| vol_20d    | 12.6% |
| mdd_60d    | 11.0% |
| rsi_14     |  49.9 |
| zscore_20d |  -0.2 |

### Apple Inc. / AAPL (score 50.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | -3.0% |
| ret_20d    | +3.4% |
| ret_60d    | +8.3% |
| ma20_dist  | +0.4% |
| ma50_dist  | -0.3% |
| vol_20d    | 20.1% |
| mdd_60d    | 11.0% |
| rsi_14     |  48.4 |
| zscore_20d |   0.2 |

### Wheat / ZW=F (score 48.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.6% |
| ret_5d     |  -6.9% |
| ret_20d    |  +9.0% |
| ret_60d    | +16.1% |
| ma20_dist  |  -0.1% |
| ma50_dist  |  +5.4% |
| vol_20d    |  43.8% |
| mdd_60d    |  10.7% |
| rsi_14     |   55.7 |
| zscore_20d |   -0.0 |

### Gold / GC=F (score 48.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | +1.1% |
| ret_20d    | +0.8% |
| ret_60d    | +4.5% |
| ma20_dist  | -1.7% |
| ma50_dist  | +3.0% |
| vol_20d    | 25.7% |
| mdd_60d    |  7.6% |
| rsi_14     |  37.3 |
| zscore_20d |  -0.8 |

### Hang Seng / ^HSI (score 48.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | -0.1% |
| ret_20d    | -0.6% |
| ret_60d    | +1.7% |
| ma20_dist  | -0.8% |
| ma50_dist  | +0.5% |
| vol_20d    | 13.4% |
| mdd_60d    |  7.4% |
| rsi_14     |  40.6 |
| zscore_20d |  -1.0 |

### FTSE 100 / ^FTSE (score 44.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.3% |
| ret_5d     | -0.8% |
| ret_20d    | -1.6% |
| ret_60d    | +1.7% |
| ma20_dist  | -1.1% |
| ma50_dist  | -0.6% |
| vol_20d    |  7.2% |
| mdd_60d    |  2.2% |
| rsi_14     |  43.6 |
| zscore_20d |  -2.3 |

### Dow Jones Industrial Average / ^DJI (score 39.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | -0.7% |
| ret_20d    | -2.6% |
| ret_60d    | +2.3% |
| ma20_dist  | -1.8% |
| ma50_dist  | -1.1% |
| vol_20d    | 10.1% |
| mdd_60d    |  3.6% |
| rsi_14     |  38.7 |
| zscore_20d |  -2.5 |

### Euro Stoxx 50 / ^STOXX50E (score 35.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.6% |
| ret_5d     | -0.8% |
| ret_20d    | -3.4% |
| ret_60d    | +0.2% |
| ma20_dist  | -2.0% |
| ma50_dist  | -1.1% |
| vol_20d    |  9.3% |
| mdd_60d    |  3.7% |
| rsi_14     |  38.0 |
| zscore_20d |  -2.1 |

### DAX / ^GDAXI (score 35.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.7% |
| ret_5d     | -1.0% |
| ret_20d    | -2.9% |
| ret_60d    | +2.6% |
| ma20_dist  | -2.1% |
| ma50_dist  | -0.7% |
| vol_20d    | 10.2% |
| mdd_60d    |  4.1% |
| rsi_14     |  40.1 |
| zscore_20d |  -2.5 |

### UnitedHealth Group Inc. / UNH (score 33.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.9% |
| ret_5d     | -0.8% |
| ret_20d    | -2.3% |
| ret_60d    | -3.2% |
| ma20_dist  | -0.8% |
| ma50_dist  | -4.3% |
| vol_20d    | 19.4% |
| mdd_60d    | 11.8% |
| rsi_14     |  53.6 |
| zscore_20d |  -0.6 |

### Russell 2000 / ^RUT (score 33.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.3% |
| ret_5d     | +0.0% |
| ret_20d    | -3.5% |
| ret_60d    | -0.8% |
| ma20_dist  | -2.5% |
| ma50_dist  | -2.2% |
| vol_20d    | 12.7% |
| mdd_60d    |  4.8% |
| rsi_14     |  32.6 |
| zscore_20d |  -1.8 |

### CAC 40 / ^FCHI (score 23.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.9% |
| ret_5d     | -1.5% |
| ret_20d    | -6.0% |
| ret_60d    | -3.3% |
| ma20_dist  | -3.0% |
| ma50_dist  | -3.4% |
| vol_20d    | 10.4% |
| mdd_60d    |  6.5% |
| rsi_14     |  27.5 |
| zscore_20d |  -2.0 |

### Amazon.com Inc. / AMZN (score 23.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.8% |
| ret_5d     | -1.0% |
| ret_20d    | -7.3% |
| ret_60d    | +5.8% |
| ma20_dist  | -3.0% |
| ma50_dist  | -0.9% |
| vol_20d    | 25.0% |
| mdd_60d    | 11.1% |
| rsi_14     |  36.2 |
| zscore_20d |  -2.0 |

### Alphabet Inc. Class A / GOOGL (score 14.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.3% |
| ret_5d     | -1.2% |
| ret_20d    | -3.8% |
| ret_60d    | -8.1% |
| ma20_dist  | -3.3% |
| ma50_dist  | -5.0% |
| vol_20d    | 17.7% |
| mdd_60d    | 14.9% |
| rsi_14     |  37.5 |
| zscore_20d |  -2.6 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Brent Crude Oil / BZ=F              |   3.3457 |           3.3% |                 0.35x |        6.6914 |            6.6% |
| Meta Platforms Inc. / META          |  19.9036 |           3.0% |                 0.26x |       39.8072 |            6.1% |
| Platinum / PL=F                     |  30.4000 |           1.6% |                 0.31x |       60.8000 |            3.2% |
| Soybeans / ZS=F                     |  19.4464 |           1.5% |                 0.63x |       38.8929 |            3.0% |
| Corn / ZC=F                         |  14.3571 |           2.8% |                 0.22x |       28.7143 |            5.7% |
| Silver / SI=F                       |   1.7887 |           2.6% |                 0.31x |        3.5774 |            5.3% |
| JPMorgan Chase & Co. / JPM          |   5.8086 |           1.6% |                 0.70x |       11.6171 |            3.3% |
| NVIDIA Corporation / NVDA           |   7.5586 |           3.4% |                 0.23x |       15.1171 |            6.8% |
| Microsoft Corporation / MSFT        |   9.8750 |           2.0% |                 0.44x |       19.7500 |            4.0% |
| Tesla Inc. / TSLA                   |  15.3393 |           4.2% |                 0.20x |       30.6786 |            8.3% |
| S&P 500 / ^GSPC                     |  55.1663 |           0.7% |                 1.19x |      110.3326 |            1.4% |
| NASDAQ 100 / ^NDX                   | 305.6062 |           1.0% |                 0.80x |      611.2123 |            2.1% |
| Apple Inc. / AAPL                   |   7.3936 |           2.3% |                 0.50x |       14.7871 |            4.7% |
| Wheat / ZW=F                        |  25.7500 |           3.6% |                 0.23x |       51.5000 |            7.2% |
| Gold / GC=F                         |  73.9000 |           1.7% |                 0.39x |      147.8001 |            3.3% |
| Hang Seng / ^HSI                    | 328.0352 |           1.3% |                 0.75x |      656.0703 |            2.6% |
| FTSE 100 / ^FTSE                    |  88.5285 |           0.8% |                 1.39x |      177.0571 |            1.7% |
| Dow Jones Industrial Average / ^DJI | 459.2201 |           0.9% |                 0.99x |      918.4403 |            1.8% |
| Euro Stoxx 50 / ^STOXX50E           |  57.9171 |           0.9% |                 1.07x |      115.8342 |            1.8% |
| DAX / ^GDAXI                        | 246.8936 |           1.0% |                 0.98x |      493.7871 |            1.9% |
| UnitedHealth Group Inc. / UNH       |   9.4807 |           2.4% |                 0.52x |       18.9614 |            4.8% |
| Russell 2000 / ^RUT                 |  29.2471 |           1.0% |                 0.78x |       58.4943 |            2.0% |
| CAC 40 / ^FCHI                      |  80.5929 |           1.0% |                 0.96x |      161.1858 |            2.0% |
| Amazon.com Inc. / AMZN              |   5.7079 |           2.3% |                 0.40x |       11.4157 |            4.5% |
| Alphabet Inc. Class A / GOOGL       |   7.0380 |           2.1% |                 0.57x |       14.0760 |            4.3% |

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

Scoring engine version: **1.0.0** | Git commit: **92eec55**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
