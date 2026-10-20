+++
title = "Market Analysis 2026-10-12"
date = "2026-10-12T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: MSFT (score 87.3)."
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
source_files = ["data/analysis/2026-10-12.json", "data/history/2026-10-12.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "5f80ebf"
+++

## Market Regime

**Neutral** — 11 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Microsoft Corporation / MSFT** — score 87.3, 20d return +8.0%, RSI14=72. 20d up +8.0%; above MA20 by 4.9%; RSI14=72
- **S&P 500 / ^GSPC** — score 70.6, 20d return +2.0%, RSI14=55. 20d up +2.0%; above MA20 by 1.4%; RSI14=55
- **NASDAQ 100 / ^NDX** — score 68.5, 20d return +5.2%, RSI14=58. 20d up +5.2%; above MA20 by 1.9%; RSI14=58
- **Amazon.com Inc. / AMZN** — score 68.2, 20d return +2.2%, RSI14=55. 20d up +2.2%; above MA20 by 4.1%; RSI14=55
- **Tesla Inc. / TSLA** — score 60.9, 20d return +4.7%, RSI14=55. 20d up +4.7%; above MA20 by 3.8%; RSI14=55

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                | Applies To |
| ---------- | -------------------- | ---------- |
| 2026-10-13 | JPM earnings release | JPM        |
| 2026-10-13 | UNH earnings release | UNH        |

## Signal History

Compared with the previous available report (**2026-10-09**).

- **New top-5:** AMZN, TSLA
- **Persistent top signals:** MSFT (11 reports), ^NDX (11 reports), ^GSPC (9 reports)
- **Dropped from top-5:** AAPL, BZ=F

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +2 |   +23.6 |
| 7203.T    |     +0 |    +2.7 |
| 8306.T    |     +0 |    -5.8 |
| AAPL      |     -8 |   -23.6 |
| AMZN      |     +8 |   +17.6 |
| BZ=F      |     -2 |    -3.6 |
| CL=F      |     +0 |    -3.6 |
| GC=F      |     +4 |    +5.5 |
| GOOGL     |     +5 |    +2.4 |
| HG=F      |     +0 |   +10.3 |
| JPM       |     -3 |    -9.1 |
| META      |     -6 |   -12.1 |
| MSFT      |     +0 |    +8.8 |
| NG=F      |     +1 |    +4.5 |
| NVDA      |     -3 |    -7.6 |
| PL=F      |     +2 |   +11.2 |
| SI=F      |     +5 |   +16.1 |
| TSLA      |     +4 |    +3.9 |
| UNH       |     +9 |   +15.8 |
| XOM       |     -1 |    -7.6 |
| ZC=F      |    -10 |   -26.7 |
| ZS=F      |     -3 |    -5.5 |
| ZW=F      |     -6 |   -20.6 |
| ^DJI      |     -1 |    -5.5 |
| ^FCHI     |     -1 |    +0.6 |
| ^FTSE     |     +1 |    +1.2 |
| ^GDAXI    |     +1 |    +5.5 |
| ^GSPC     |     +1 |    -3.6 |
| ^HSI      |     +7 |   +17.3 |
| ^N225     |     -2 |    -2.1 |
| ^NDX      |     +1 |    -2.4 |
| ^RUT      |     -4 |    -7.3 |
| ^STOXX50E |     -1 |    -0.3 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Natural Gas / NG=F** — malformed_input
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **WTI Crude Oil / CL=F** — malformed_input
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|    7 | Brent Crude Oil / BZ=F |  57.0 |   Yes    | —               | 20d up +0.1%; above MA20 by 1.2%; RSI14=59   |
|   13 | Soybeans / ZS=F        |  50.0 |   Yes    | —               | 20d up +0.9%; below MA20 by 0.8%; RSI14=35   |
|   17 | Gold / GC=F            |  40.0 |   Yes    | —               | 20d down -4.4%; below MA20 by 1.2%; RSI14=33 |
|   20 | Silver / SI=F          |  30.0 |   Yes    | —               | 20d down -6.0%; below MA20 by 3.0%; RSI14=31 |
|   22 | Platinum / PL=F        |  28.5 |   Yes    | —               | 20d down -6.4%; below MA20 by 3.1%; RSI14=36 |
|   24 | Corn / ZC=F            |  16.7 |   Yes    | —               | 20d down -6.0%; below MA20 by 7.2%; RSI14=15 |
|   25 | Wheat / ZW=F           |  15.4 |   Yes    | —               | 20d down -5.1%; below MA20 by 4.4%; RSI14=27 |
|   26 | Natural Gas / NG=F     |  77.3 |    No    | malformed_input | Suppressed: malformed_input                  |
|   29 | Copper / HG=F          |  63.6 |    No    | malformed_input | Suppressed: malformed_input                  |
|   32 | WTI Crude Oil / CL=F   |  31.5 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    1 | Microsoft Corporation / MSFT                                                   |  87.3 |   Yes    | —                             | 20d up +8.0%; above MA20 by 4.9%; RSI14=72   |
|    4 | Amazon.com Inc. / AMZN                                                         |  68.2 |   Yes    | —                             | 20d up +2.2%; above MA20 by 4.1%; RSI14=55   |
|    5 | Tesla Inc. / TSLA                                                              |  60.9 |   Yes    | —                             | 20d up +4.7%; above MA20 by 3.8%; RSI14=55   |
|    6 | Alphabet Inc. Class A / GOOGL                                                  |  57.3 |   Yes    | —                             | 20d up +3.9%; above MA20 by 1.7%; RSI14=47   |
|    9 | NVIDIA Corporation / NVDA                                                      |  52.4 |   Yes    | —                             | 20d up +5.0%; above MA20 by 1.1%; RSI14=53   |
|   10 | Apple Inc. / AAPL                                                              |  52.1 |   Yes    | —                             | 20d up +1.3%; above MA20 by 0.4%; RSI14=47   |
|   11 | UnitedHealth Group Inc. / UNH                                                  |  51.5 |   Yes    | —                             | 20d up +0.7%; above MA20 by 1.2%; RSI14=52   |
|   14 | Meta Platforms Inc. / META                                                     |  45.8 |   Yes    | —                             | 20d up +11.0%; below MA20 by 0.1%; RSI14=44  |
|   21 | JPMorgan Chase & Co. / JPM                                                     |  28.5 |   Yes    | —                             | 20d down -6.1%; below MA20 by 1.5%; RSI14=29 |
|   27 | Exxon Mobil Corporation / XOM                                                  |  73.9 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   28 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  72.7 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   31 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  46.7 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   33 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  21.8 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    2 | S&P 500 / ^GSPC                     |  70.6 |   Yes    | —            | 20d up +2.0%; above MA20 by 1.4%; RSI14=55   |
|    3 | NASDAQ 100 / ^NDX                   |  68.5 |   Yes    | —            | 20d up +5.2%; above MA20 by 1.9%; RSI14=58   |
|    8 | Dow Jones Industrial Average / ^DJI |  54.2 |   Yes    | —            | 20d down -1.7%; above MA20 by 0.2%; RSI14=44 |
|   12 | FTSE 100 / ^FTSE                    |  51.5 |   Yes    | —            | 20d down -0.9%; below MA20 by 0.6%; RSI14=36 |
|   15 | DAX / ^GDAXI                        |  45.1 |   Yes    | —            | 20d down -1.9%; below MA20 by 0.9%; RSI14=40 |
|   16 | Hang Seng / ^HSI                    |  41.2 |   Yes    | —            | 20d down -3.0%; below MA20 by 1.4%; RSI14=41 |
|   18 | Euro Stoxx 50 / ^STOXX50E           |  39.1 |   Yes    | —            | 20d down -2.4%; below MA20 by 1.3%; RSI14=37 |
|   19 | Russell 2000 / ^RUT                 |  33.3 |   Yes    | —            | 20d down -3.3%; below MA20 by 1.1%; RSI14=35 |
|   23 | CAC 40 / ^FCHI                      |  25.4 |   Yes    | —            | 20d down -4.6%; below MA20 by 2.5%; RSI14=26 |
|   30 | Nikkei 225 / ^N225                  |  61.8 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-10-09 |
| 7203.T    | 2026-10-09 |
| 8306.T    | 2026-10-09 |
| AAPL      | 2026-10-09 |
| AMZN      | 2026-10-09 |
| BZ=F      | 2026-10-09 |
| CL=F      | 2026-10-09 |
| GC=F      | 2026-10-09 |
| GOOGL     | 2026-10-09 |
| HG=F      | 2026-10-09 |
| JPM       | 2026-10-09 |
| META      | 2026-10-09 |
| MSFT      | 2026-10-09 |
| NG=F      | 2026-10-09 |
| NVDA      | 2026-10-09 |
| PL=F      | 2026-10-09 |
| SI=F      | 2026-10-09 |
| TSLA      | 2026-10-09 |
| UNH       | 2026-10-09 |
| XOM       | 2026-10-09 |
| ZC=F      | 2026-10-09 |
| ZS=F      | 2026-10-09 |
| ZW=F      | 2026-10-09 |
| ^DJI      | 2026-10-09 |
| ^FCHI     | 2026-10-09 |
| ^FTSE     | 2026-10-09 |
| ^GDAXI    | 2026-10-09 |
| ^GSPC     | 2026-10-09 |
| ^HSI      | 2026-10-09 |
| ^N225     | 2026-10-09 |
| ^NDX      | 2026-10-09 |
| ^RUT      | 2026-10-09 |
| ^STOXX50E | 2026-10-09 |

## Symbol Details

### Microsoft Corporation / MSFT (score 87.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.4% |
| ret_5d     |  +3.4% |
| ret_20d    |  +8.0% |
| ret_60d    | +33.4% |
| ma20_dist  |  +4.9% |
| ma50_dist  |  +7.0% |
| vol_20d    |  22.1% |
| mdd_60d    |   5.1% |
| rsi_14     |   72.3 |
| zscore_20d |    1.9 |

### S&P 500 / ^GSPC (score 70.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | +1.2% |
| ret_20d    | +2.0% |
| ret_60d    | +3.7% |
| ma20_dist  | +1.4% |
| ma50_dist  | +1.5% |
| vol_20d    |  9.7% |
| mdd_60d    |  3.2% |
| rsi_14     |  55.1 |
| zscore_20d |   1.4 |

### NASDAQ 100 / ^NDX (score 68.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | +0.2% |
| ret_20d    | +5.2% |
| ret_60d    | +6.4% |
| ma20_dist  | +1.9% |
| ma50_dist  | +3.7% |
| vol_20d    | 15.2% |
| mdd_60d    |  6.7% |
| rsi_14     |  57.8 |
| zscore_20d |   0.8 |

### Amazon.com Inc. / AMZN (score 68.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +3.3% |
| ret_5d     | +4.3% |
| ret_20d    | +2.2% |
| ret_60d    | +5.0% |
| ma20_dist  | +4.1% |
| ma50_dist  | +1.3% |
| vol_20d    | 24.8% |
| mdd_60d    | 13.4% |
| rsi_14     |  54.6 |
| zscore_20d |   2.3 |

### Tesla Inc. / TSLA (score 60.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.1% |
| ret_5d     | +3.3% |
| ret_20d    | +4.7% |
| ret_60d    | -2.1% |
| ma20_dist  | +3.8% |
| ma50_dist  | +7.9% |
| vol_20d    | 29.8% |
| mdd_60d    | 21.7% |
| rsi_14     |  55.0 |
| zscore_20d |   1.4 |

### Alphabet Inc. Class A / GOOGL (score 57.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.0% |
| ret_5d     | +2.4% |
| ret_20d    | +3.9% |
| ret_60d    | -0.8% |
| ma20_dist  | +1.7% |
| ma50_dist  | +1.6% |
| vol_20d    | 23.3% |
| mdd_60d    | 12.4% |
| rsi_14     |  46.9 |
| zscore_20d |   1.3 |

### Brent Crude Oil / BZ=F (score 57.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.4% |
| ret_5d     |  +2.4% |
| ret_20d    |  +0.1% |
| ret_60d    | +11.3% |
| ma20_dist  |  +1.2% |
| ma50_dist  |  +8.4% |
| vol_20d    |  34.1% |
| mdd_60d    |  21.2% |
| rsi_14     |   59.2 |
| zscore_20d |    0.5 |

### Dow Jones Industrial Average / ^DJI (score 54.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.8% |
| ret_5d     | +0.9% |
| ret_20d    | -1.7% |
| ret_60d    | -1.7% |
| ma20_dist  | +0.2% |
| ma50_dist  | -1.9% |
| vol_20d    |  9.5% |
| mdd_60d    |  6.3% |
| rsi_14     |  44.4 |
| zscore_20d |   0.3 |

### NVIDIA Corporation / NVDA (score 52.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.5% |
| ret_5d     |  -2.0% |
| ret_20d    |  +5.0% |
| ret_60d    | +10.5% |
| ma20_dist  |  +1.1% |
| ma50_dist  |  +3.3% |
| vol_20d    |  24.6% |
| mdd_60d    |  10.4% |
| rsi_14     |   52.8 |
| zscore_20d |    0.3 |

### Apple Inc. / AAPL (score 52.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.1% |
| ret_5d     | +0.9% |
| ret_20d    | +1.3% |
| ret_60d    | +1.1% |
| ma20_dist  | +0.4% |
| ma50_dist  | +4.4% |
| vol_20d    | 15.9% |
| mdd_60d    | 11.0% |
| rsi_14     |  47.3 |
| zscore_20d |   0.4 |

### UnitedHealth Group Inc. / UNH (score 51.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.3% |
| ret_5d     |  +2.0% |
| ret_20d    |  +0.7% |
| ret_60d    | -10.4% |
| ma20_dist  |  +1.2% |
| ma50_dist  |  -2.3% |
| vol_20d    |  19.3% |
| mdd_60d    |  16.3% |
| rsi_14     |   51.6 |
| zscore_20d |    1.1 |

### FTSE 100 / ^FTSE (score 51.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | +0.9% |
| ret_20d    | -0.9% |
| ret_60d    | -0.2% |
| ma20_dist  | -0.6% |
| ma50_dist  | -1.6% |
| vol_20d    | 11.2% |
| mdd_60d    |  4.4% |
| rsi_14     |  36.0 |
| zscore_20d |  -0.6 |

### Soybeans / ZS=F (score 50.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +1.1% |
| ret_20d    | +0.9% |
| ret_60d    | +5.9% |
| ma20_dist  | -0.8% |
| ma50_dist  | +2.7% |
| vol_20d    | 17.1% |
| mdd_60d    |  8.1% |
| rsi_14     |  34.5 |
| zscore_20d |  -0.7 |

### Meta Platforms Inc. / META (score 45.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.3% |
| ret_5d     |  -1.3% |
| ret_20d    | +11.0% |
| ret_60d    |  +8.1% |
| ma20_dist  |  -0.1% |
| ma50_dist  | +12.4% |
| vol_20d    |  52.5% |
| mdd_60d    |  16.6% |
| rsi_14     |   43.9 |
| zscore_20d |   -0.0 |

### DAX / ^GDAXI (score 45.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | -0.6% |
| ret_20d    | -1.9% |
| ret_60d    | +1.0% |
| ma20_dist  | -0.9% |
| ma50_dist  | -2.8% |
| vol_20d    | 13.2% |
| mdd_60d    |  6.6% |
| rsi_14     |  39.9 |
| zscore_20d |  -1.1 |

### Hang Seng / ^HSI (score 41.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.8% |
| ret_5d     | +1.0% |
| ret_20d    | -3.0% |
| ret_60d    | -3.2% |
| ma20_dist  | -1.4% |
| ma50_dist  | -3.7% |
| vol_20d    | 15.6% |
| mdd_60d    |  8.5% |
| rsi_14     |  41.4 |
| zscore_20d |  -0.9 |

### Gold / GC=F (score 40.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.4% |
| ret_5d     | +1.3% |
| ret_20d    | -4.4% |
| ret_60d    | +1.7% |
| ma20_dist  | -1.2% |
| ma50_dist  | -4.1% |
| vol_20d    | 17.3% |
| mdd_60d    | 12.0% |
| rsi_14     |  33.0 |
| zscore_20d |  -0.5 |

### Euro Stoxx 50 / ^STOXX50E (score 39.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.8% |
| ret_5d     | -1.0% |
| ret_20d    | -2.4% |
| ret_60d    | -0.9% |
| ma20_dist  | -1.3% |
| ma50_dist  | -3.1% |
| vol_20d    | 13.2% |
| mdd_60d    |  6.5% |
| rsi_14     |  36.7 |
| zscore_20d |  -1.5 |

### Russell 2000 / ^RUT (score 33.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | -0.9% |
| ret_20d    | -3.3% |
| ret_60d    | -5.6% |
| ma20_dist  | -1.1% |
| ma50_dist  | -4.2% |
| vol_20d    | 10.6% |
| mdd_60d    |  9.0% |
| rsi_14     |  35.1 |
| zscore_20d |  -1.0 |

### Silver / SI=F (score 30.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.7% |
| ret_5d     | +1.2% |
| ret_20d    | -6.0% |
| ret_60d    | +1.1% |
| ma20_dist  | -3.0% |
| ma50_dist  | -6.2% |
| vol_20d    | 28.2% |
| mdd_60d    | 15.0% |
| rsi_14     |  31.3 |
| zscore_20d |  -0.8 |

### JPMorgan Chase & Co. / JPM (score 28.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | +0.7% |
| ret_20d    | -6.1% |
| ret_60d    | -3.0% |
| ma20_dist  | -1.5% |
| ma50_dist  | -4.7% |
| vol_20d    | 17.3% |
| mdd_60d    |  9.9% |
| rsi_14     |  28.9 |
| zscore_20d |  -0.7 |

### Platinum / PL=F (score 28.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +3.3% |
| ret_5d     | -0.2% |
| ret_20d    | -6.4% |
| ret_60d    | +2.2% |
| ma20_dist  | -3.1% |
| ma50_dist  | -5.3% |
| vol_20d    | 28.9% |
| mdd_60d    | 15.1% |
| rsi_14     |  36.2 |
| zscore_20d |  -0.9 |

### CAC 40 / ^FCHI (score 25.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.0% |
| ret_5d     | -1.2% |
| ret_20d    | -4.6% |
| ret_60d    | -6.4% |
| ma20_dist  | -2.5% |
| ma50_dist  | -5.7% |
| vol_20d    | 12.1% |
| mdd_60d    | 11.4% |
| rsi_14     |  26.1 |
| zscore_20d |  -1.4 |

### Corn / ZC=F (score 16.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -4.1% |
| ret_5d     | -3.6% |
| ret_20d    | -6.0% |
| ret_60d    | +6.0% |
| ma20_dist  | -7.2% |
| ma50_dist  | -3.6% |
| vol_20d    | 30.6% |
| mdd_60d    | 11.6% |
| rsi_14     |  14.6 |
| zscore_20d |  -2.2 |

### Wheat / ZW=F (score 15.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.8% |
| ret_5d     | -1.8% |
| ret_20d    | -5.1% |
| ret_60d    | -1.0% |
| ma20_dist  | -4.4% |
| ma50_dist  | -3.7% |
| vol_20d    | 23.6% |
| mdd_60d    | 12.5% |
| rsi_14     |  26.9 |
| zscore_20d |  -1.7 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Microsoft Corporation / MSFT        |  12.7193 |           2.4% |                 0.45x |       25.4386 |            4.8% |
| S&P 500 / ^GSPC                     |  63.2150 |           0.8% |                 1.03x |      126.4300 |            1.6% |
| NASDAQ 100 / ^NDX                   | 347.4648 |           1.1% |                 0.66x |      694.9297 |            2.3% |
| Amazon.com Inc. / AMZN              |   5.6293 |           2.1% |                 0.40x |       11.2586 |            4.3% |
| Tesla Inc. / TSLA                   |  11.0286 |           2.9% |                 0.34x |       22.0571 |            5.8% |
| Alphabet Inc. Class A / GOOGL       |   8.6643 |           2.5% |                 0.43x |       17.3286 |            4.9% |
| Brent Crude Oil / BZ=F              |   4.5707 |           4.4% |                 0.29x |        9.1414 |            8.7% |
| Dow Jones Industrial Average / ^DJI | 481.7687 |           0.9% |                 1.05x |      963.5374 |            1.9% |
| NVIDIA Corporation / NVDA           |   5.1993 |           2.3% |                 0.41x |       10.3986 |            4.5% |
| Apple Inc. / AAPL                   |   6.4586 |           1.9% |                 0.63x |       12.9171 |            3.8% |
| UnitedHealth Group Inc. / UNH       |   8.8650 |           2.3% |                 0.52x |       17.7300 |            4.7% |
| FTSE 100 / ^FTSE                    | 106.2641 |           1.0% |                 0.90x |      212.5282 |            2.0% |
| Soybeans / ZS=F                     |  21.4464 |           1.7% |                 0.59x |       42.8929 |            3.3% |
| Meta Platforms Inc. / META          |  22.0086 |           3.1% |                 0.19x |       44.0172 |            6.1% |
| DAX / ^GDAXI                        | 316.4072 |           1.3% |                 0.76x |      632.8145 |            2.5% |
| Hang Seng / ^HSI                    | 325.2694 |           1.3% |                 0.64x |      650.5388 |            2.7% |
| Gold / GC=F                         |  81.7785 |           1.9% |                 0.58x |      163.5571 |            3.9% |
| Euro Stoxx 50 / ^STOXX50E           |  76.4757 |           1.2% |                 0.76x |      152.9514 |            2.5% |
| Russell 2000 / ^RUT                 |  34.5250 |           1.2% |                 0.95x |       69.0500 |            2.5% |
| Silver / SI=F                       |   1.2934 |           2.1% |                 0.36x |        2.5867 |            4.3% |
| JPMorgan Chase & Co. / JPM          |   5.7225 |           1.7% |                 0.58x |       11.4450 |            3.4% |
| Platinum / PL=F                     |  37.5643 |           2.2% |                 0.35x |       75.1286 |            4.5% |
| CAC 40 / ^FCHI                      |  93.8371 |           1.2% |                 0.83x |      187.6742 |            2.4% |
| Corn / ZC=F                         |  12.3214 |           2.6% |                 0.33x |       24.6429 |            5.1% |
| Wheat / ZW=F                        |  17.3393 |           2.6% |                 0.42x |       34.6786 |            5.2% |

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

Scoring engine version: **1.0.0** | Git commit: **5f80ebf**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
