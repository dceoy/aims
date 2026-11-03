+++
title = "Market Analysis 2026-11-03"
date = "2026-11-03T00:00:00+00:00"
draft = false
summary = "Bearish market: 25 reliable instruments. Top signal: TSLA (score 82.4)."
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
source_files = ["data/analysis/2026-11-03.json", "data/history/2026-11-03.json"]
market_regime = "Bearish"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "8db0dfc"
+++

## Market Regime

**Bearish** — 8 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Tesla Inc. / TSLA** — score 82.4, 20d return +6.6%, RSI14=63. 20d up +6.6%; above MA20 by 5.7%; RSI14=63
- **DAX / ^GDAXI** — score 80.3, 20d return +2.9%, RSI14=63. 20d up +2.9%; above MA20 by 2.2%; RSI14=63
- **CAC 40 / ^FCHI** — score 74.8, 20d return +2.7%, RSI14=65. 20d up +2.7%; above MA20 by 2.2%; RSI14=65
- **FTSE 100 / ^FTSE** — score 74.5, 20d return +2.5%, RSI14=58. 20d up +2.5%; above MA20 by 0.7%; RSI14=58
- **JPMorgan Chase & Co. / JPM** — score 73.3, 20d return +3.0%, RSI14=60. 20d up +3.0%; above MA20 by 1.6%; RSI14=60

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                   | Applies To |
| ---------- | ----------------------- | ---------- |
| 2026-11-05 | 6758.T earnings release | 6758.T     |
| 2026-11-05 | 7203.T earnings release | 7203.T     |

## Signal History

Compared with the previous available report (**2026-11-02**).

- **New top-5:** JPM, ^FCHI
- **Persistent top signals:** TSLA (6 reports), ^GDAXI (5 reports), ^FTSE (2 reports)
- **Dropped from top-5:** AAPL, BZ=F

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +3 |    +5.5 |
| 7203.T    |     +0 |    -1.2 |
| 8306.T    |     -2 |   -10.9 |
| AAPL      |     -3 |   -10.9 |
| AMZN      |     +5 |   +17.0 |
| BZ=F      |    -12 |   -39.4 |
| CL=F      |     -3 |   -24.6 |
| GC=F      |     +4 |   +17.0 |
| GOOGL     |     -1 |    +0.9 |
| HG=F      |     +2 |   +15.2 |
| JPM       |     +4 |   +13.9 |
| META      |     +0 |    -0.9 |
| MSFT      |     -6 |   -17.9 |
| NG=F      |     -1 |    -4.8 |
| NVDA      |     -1 |    +0.0 |
| PL=F      |     +1 |   +10.6 |
| SI=F      |     +1 |   +13.3 |
| TSLA      |     +1 |    +7.0 |
| UNH       |     -2 |    -6.1 |
| XOM       |     -1 |   -16.4 |
| ZC=F      |     -2 |    +0.9 |
| ZS=F      |     -1 |    -9.7 |
| ZW=F      |     -1 |    +5.5 |
| ^DJI      |     +2 |    +6.1 |
| ^FCHI     |     +3 |    +6.7 |
| ^FTSE     |     +0 |    +2.4 |
| ^GDAXI    |     +1 |    +5.5 |
| ^GSPC     |     +2 |    -2.4 |
| ^HSI      |     +3 |    +4.2 |
| ^N225     |     +2 |    +5.2 |
| ^NDX      |     -3 |    -3.6 |
| ^RUT      |     +0 |    +2.4 |
| ^STOXX50E |     +5 |    +9.7 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Natural Gas / NG=F** — malformed_input

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|   13 | Brent Crude Oil / BZ=F |  43.9 |   Yes    | —               | 20d up +4.4%; below MA20 by 4.0%; RSI14=49    |
|   15 | Soybeans / ZS=F        |  40.3 |   Yes    | —               | 20d down -5.9%; below MA20 by 4.2%; RSI14=13  |
|   16 | Gold / GC=F            |  39.1 |   Yes    | —               | 20d down -4.5%; below MA20 by 3.3%; RSI14=34  |
|   18 | Corn / ZC=F            |  35.5 |   Yes    | —               | 20d down -9.9%; below MA20 by 4.6%; RSI14=11  |
|   19 | Wheat / ZW=F           |  32.4 |   Yes    | —               | 20d down -12.4%; below MA20 by 6.0%; RSI14=14 |
|   22 | Platinum / PL=F        |  20.3 |   Yes    | —               | 20d down -14.5%; below MA20 by 8.4%; RSI14=22 |
|   24 | Silver / SI=F          |  17.9 |   Yes    | —               | 20d down -16.7%; below MA20 by 9.7%; RSI14=25 |
|   29 | Copper / HG=F          |  63.9 |    No    | malformed_input | Suppressed: malformed_input                   |
|   30 | WTI Crude Oil / CL=F   |  49.4 |    No    | malformed_input | Suppressed: malformed_input                   |
|   33 | Natural Gas / NG=F     |  38.5 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                    |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | ---------------------------------------------- |
|    1 | Tesla Inc. / TSLA                                                              |  82.4 |   Yes    | —                             | 20d up +6.6%; above MA20 by 5.7%; RSI14=63     |
|    5 | JPMorgan Chase & Co. / JPM                                                     |  73.3 |   Yes    | —                             | 20d up +3.0%; above MA20 by 1.6%; RSI14=60     |
|    8 | Apple Inc. / AAPL                                                              |  60.6 |   Yes    | —                             | 20d up +1.6%; below MA20 by 1.2%; RSI14=47     |
|    9 | UnitedHealth Group Inc. / UNH                                                  |  58.5 |   Yes    | —                             | 20d up +5.8%; above MA20 by 0.2%; RSI14=62     |
|   14 | Amazon.com Inc. / AMZN                                                         |  42.1 |   Yes    | —                             | 20d down -2.3%; below MA20 by 3.3%; RSI14=40   |
|   17 | Microsoft Corporation / MSFT                                                   |  37.0 |   Yes    | —                             | 20d down -3.4%; below MA20 by 4.3%; RSI14=28   |
|   21 | Meta Platforms Inc. / META                                                     |  20.9 |   Yes    | —                             | 20d down -18.2%; below MA20 by 11.3%; RSI14=8  |
|   23 | NVIDIA Corporation / NVDA                                                      |  19.7 |   Yes    | —                             | 20d down -15.4%; below MA20 by 8.0%; RSI14=27  |
|   25 | Alphabet Inc. Class A / GOOGL                                                  |   8.5 |   Yes    | —                             | 20d down -19.5%; below MA20 by 15.6%; RSI14=13 |
|   26 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  70.0 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   27 | Exxon Mobil Corporation / XOM                                                  |  69.4 |    No    | malformed_input               | Suppressed: malformed_input                    |
|   28 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  67.9 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |
|   32 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  41.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars      |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    2 | DAX / ^GDAXI                        |  80.3 |   Yes    | —            | 20d up +2.9%; above MA20 by 2.2%; RSI14=63   |
|    3 | CAC 40 / ^FCHI                      |  74.8 |   Yes    | —            | 20d up +2.7%; above MA20 by 2.2%; RSI14=65   |
|    4 | FTSE 100 / ^FTSE                    |  74.5 |   Yes    | —            | 20d up +2.5%; above MA20 by 0.7%; RSI14=58   |
|    6 | Dow Jones Industrial Average / ^DJI |  67.0 |   Yes    | —            | 20d up +1.4%; below MA20 by 0.1%; RSI14=54   |
|    7 | Euro Stoxx 50 / ^STOXX50E           |  64.5 |   Yes    | —            | 20d down -1.1%; above MA20 by 0.2%; RSI14=51 |
|   10 | Russell 2000 / ^RUT                 |  58.2 |   Yes    | —            | 20d down -1.4%; above MA20 by 0.6%; RSI14=53 |
|   11 | S&P 500 / ^GSPC                     |  48.8 |   Yes    | —            | 20d down -3.0%; below MA20 by 2.3%; RSI14=32 |
|   12 | Hang Seng / ^HSI                    |  48.8 |   Yes    | —            | 20d down -2.4%; below MA20 by 1.3%; RSI14=34 |
|   20 | NASDAQ 100 / ^NDX                   |  27.9 |   Yes    | —            | 20d down -9.9%; below MA20 by 6.0%; RSI14=27 |
|   31 | Nikkei 225 / ^N225                  |  42.4 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-11-02 |
| 7203.T    | 2026-11-02 |
| 8306.T    | 2026-11-02 |
| AAPL      | 2026-11-02 |
| AMZN      | 2026-11-02 |
| BZ=F      | 2026-11-02 |
| CL=F      | 2026-11-02 |
| GC=F      | 2026-11-02 |
| GOOGL     | 2026-11-02 |
| HG=F      | 2026-11-02 |
| JPM       | 2026-11-02 |
| META      | 2026-11-02 |
| MSFT      | 2026-11-02 |
| NG=F      | 2026-11-02 |
| NVDA      | 2026-11-02 |
| PL=F      | 2026-11-02 |
| SI=F      | 2026-11-02 |
| TSLA      | 2026-11-02 |
| UNH       | 2026-11-02 |
| XOM       | 2026-11-02 |
| ZC=F      | 2026-11-02 |
| ZS=F      | 2026-11-02 |
| ZW=F      | 2026-11-02 |
| ^DJI      | 2026-11-02 |
| ^FCHI     | 2026-11-02 |
| ^FTSE     | 2026-11-02 |
| ^GDAXI    | 2026-11-02 |
| ^GSPC     | 2026-11-02 |
| ^HSI      | 2026-11-02 |
| ^N225     | 2026-11-02 |
| ^NDX      | 2026-11-02 |
| ^RUT      | 2026-11-02 |
| ^STOXX50E | 2026-11-02 |

## Symbol Details

### Tesla Inc. / TSLA (score 82.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.0% |
| ret_5d     |  +3.1% |
| ret_20d    |  +6.6% |
| ret_60d    | +22.9% |
| ma20_dist  |  +5.7% |
| ma50_dist  |  +9.0% |
| vol_20d    |  35.5% |
| mdd_60d    |   7.3% |
| rsi_14     |   62.6 |
| zscore_20d |    1.5 |

### DAX / ^GDAXI (score 80.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.6% |
| ret_5d     | +2.2% |
| ret_20d    | +2.9% |
| ret_60d    | -1.3% |
| ma20_dist  | +2.2% |
| ma50_dist  | +1.6% |
| vol_20d    | 14.0% |
| mdd_60d    |  6.6% |
| rsi_14     |  63.2 |
| zscore_20d |   1.8 |

### CAC 40 / ^FCHI (score 74.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.0% |
| ret_5d     | +2.6% |
| ret_20d    | +2.7% |
| ret_60d    | -7.8% |
| ma20_dist  | +2.2% |
| ma50_dist  | -0.0% |
| vol_20d    | 11.9% |
| mdd_60d    | 11.3% |
| rsi_14     |  65.0 |
| zscore_20d |   2.3 |

### FTSE 100 / ^FTSE (score 74.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | -0.1% |
| ret_20d    | +2.5% |
| ret_60d    | -1.3% |
| ma20_dist  | +0.7% |
| ma50_dist  | +0.5% |
| vol_20d    |  9.5% |
| mdd_60d    |  4.2% |
| rsi_14     |  58.0 |
| zscore_20d |   0.7 |

### JPMorgan Chase & Co. / JPM (score 73.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | +2.0% |
| ret_20d    | +3.0% |
| ret_60d    | -4.7% |
| ma20_dist  | +1.6% |
| ma50_dist  | -0.5% |
| vol_20d    | 15.2% |
| mdd_60d    |  9.9% |
| rsi_14     |  60.2 |
| zscore_20d |   1.6 |

### Dow Jones Industrial Average / ^DJI (score 67.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | -0.7% |
| ret_20d    | +1.4% |
| ret_60d    | -3.8% |
| ma20_dist  | -0.1% |
| ma50_dist  | -0.4% |
| vol_20d    |  9.7% |
| mdd_60d    |  5.7% |
| rsi_14     |  54.4 |
| zscore_20d |  -0.1 |

### Euro Stoxx 50 / ^STOXX50E (score 64.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | +1.0% |
| ret_20d    | -1.1% |
| ret_60d    | -5.5% |
| ma20_dist  | +0.2% |
| ma50_dist  | -1.4% |
| vol_20d    | 13.9% |
| mdd_60d    |  7.4% |
| rsi_14     |  50.7 |
| zscore_20d |   0.3 |

### Apple Inc. / AAPL (score 60.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.8% |
| ret_5d     | -1.6% |
| ret_20d    | +1.6% |
| ret_60d    | +8.1% |
| ma20_dist  | -1.2% |
| ma50_dist  | +1.4% |
| vol_20d    | 15.7% |
| mdd_60d    |  3.9% |
| rsi_14     |  46.6 |
| zscore_20d |  -1.0 |

### UnitedHealth Group Inc. / UNH (score 58.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.6% |
| ret_5d     | -2.5% |
| ret_20d    | +5.8% |
| ret_60d    | -1.6% |
| ma20_dist  | +0.2% |
| ma50_dist  | +2.7% |
| vol_20d    | 28.2% |
| mdd_60d    | 10.7% |
| rsi_14     |  62.0 |
| zscore_20d |   0.0 |

### Russell 2000 / ^RUT (score 58.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | +0.7% |
| ret_20d    | -1.4% |
| ret_60d    | -7.5% |
| ma20_dist  | +0.6% |
| ma50_dist  | -1.7% |
| vol_20d    | 15.6% |
| mdd_60d    | 11.3% |
| rsi_14     |  53.3 |
| zscore_20d |   0.5 |

### S&P 500 / ^GSPC (score 48.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.5% |
| ret_5d     | -1.8% |
| ret_20d    | -3.0% |
| ret_60d    | -2.8% |
| ma20_dist  | -2.3% |
| ma50_dist  | -2.0% |
| vol_20d    | 11.2% |
| mdd_60d    |  3.5% |
| rsi_14     |  32.4 |
| zscore_20d |  -2.3 |

### Hang Seng / ^HSI (score 48.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | +0.8% |
| ret_20d    | -2.4% |
| ret_60d    | -8.4% |
| ma20_dist  | -1.3% |
| ma50_dist  | -4.6% |
| vol_20d    | 17.3% |
| mdd_60d    | 11.8% |
| rsi_14     |  34.4 |
| zscore_20d |  -0.6 |

### Brent Crude Oil / BZ=F (score 43.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     | -10.9% |
| ret_5d     |  -9.5% |
| ret_20d    |  +4.4% |
| ret_60d    | +17.7% |
| ma20_dist  |  -4.0% |
| ma50_dist  |  +1.2% |
| vol_20d    |  49.0% |
| mdd_60d    |  10.9% |
| rsi_14     |   48.6 |
| zscore_20d |   -0.8 |

### Amazon.com Inc. / AMZN (score 42.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.2% |
| ret_5d     |  -1.4% |
| ret_20d    |  -2.3% |
| ret_60d    | -10.5% |
| ma20_dist  |  -3.3% |
| ma50_dist  |  -3.3% |
| vol_20d    |  36.2% |
| mdd_60d    |  13.6% |
| rsi_14     |   39.8 |
| zscore_20d |   -1.3 |

### Soybeans / ZS=F (score 40.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.4% |
| ret_5d     | -2.9% |
| ret_20d    | -5.9% |
| ret_60d    | +5.0% |
| ma20_dist  | -4.2% |
| ma50_dist  | -5.8% |
| vol_20d    | 11.0% |
| mdd_60d    |  9.3% |
| rsi_14     |  12.9 |
| zscore_20d |  -1.9 |

### Gold / GC=F (score 39.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.8% |
| ret_5d     |  -1.7% |
| ret_20d    |  -4.5% |
| ret_60d    | -10.0% |
| ma20_dist  |  -3.3% |
| ma50_dist  |  -7.2% |
| vol_20d    |  19.9% |
| mdd_60d    |  17.2% |
| rsi_14     |   33.9 |
| zscore_20d |   -1.6 |

### Microsoft Corporation / MSFT (score 37.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.8% |
| ret_5d     | -4.8% |
| ret_20d    | -3.4% |
| ret_60d    | +1.6% |
| ma20_dist  | -4.3% |
| ma50_dist  | -1.2% |
| vol_20d    | 21.4% |
| mdd_60d    |  6.7% |
| rsi_14     |  27.8 |
| zscore_20d |  -2.9 |

### Corn / ZC=F (score 35.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.1% |
| ret_5d     |  -1.5% |
| ret_20d    |  -9.9% |
| ret_60d    |  +2.6% |
| ma20_dist  |  -4.6% |
| ma50_dist  | -10.0% |
| vol_20d    |  18.5% |
| mdd_60d    |  17.5% |
| rsi_14     |   10.8 |
| zscore_20d |   -1.2 |

### Wheat / ZW=F (score 32.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.5% |
| ret_5d     |  -1.5% |
| ret_20d    | -12.4% |
| ret_60d    |  -3.8% |
| ma20_dist  |  -6.0% |
| ma50_dist  | -11.8% |
| vol_20d    |  17.4% |
| mdd_60d    |  21.9% |
| rsi_14     |   13.8 |
| zscore_20d |   -1.2 |

### NASDAQ 100 / ^NDX (score 27.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.4% |
| ret_5d     | -4.4% |
| ret_20d    | -9.9% |
| ret_60d    | -5.8% |
| ma20_dist  | -6.0% |
| ma50_dist  | -6.0% |
| vol_20d    | 21.9% |
| mdd_60d    | 10.4% |
| rsi_14     |  27.1 |
| zscore_20d |  -2.1 |

### Meta Platforms Inc. / META (score 20.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.3% |
| ret_5d     |  -3.8% |
| ret_20d    | -18.2% |
| ret_60d    |  +2.5% |
| ma20_dist  | -11.3% |
| ma50_dist  |  -9.6% |
| vol_20d    |  35.2% |
| mdd_60d    |  22.0% |
| rsi_14     |    8.2 |
| zscore_20d |   -1.5 |

### Platinum / PL=F (score 20.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.5% |
| ret_5d     |  -5.1% |
| ret_20d    | -14.5% |
| ret_60d    | -17.2% |
| ma20_dist  |  -8.4% |
| ma50_dist  | -14.6% |
| vol_20d    |  30.4% |
| mdd_60d    |  24.9% |
| rsi_14     |   22.2 |
| zscore_20d |   -1.9 |

### NVIDIA Corporation / NVDA (score 19.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.3% |
| ret_5d     |  -6.5% |
| ret_20d    | -15.4% |
| ret_60d    |  -9.8% |
| ma20_dist  |  -8.0% |
| ma50_dist  |  -8.8% |
| vol_20d    |  29.8% |
| mdd_60d    |  15.5% |
| rsi_14     |   26.9 |
| zscore_20d |   -1.8 |

### Silver / SI=F (score 17.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +3.3% |
| ret_5d     |  -6.3% |
| ret_20d    | -16.7% |
| ret_60d    | -22.6% |
| ma20_dist  |  -9.7% |
| ma50_dist  | -17.3% |
| vol_20d    |  39.9% |
| mdd_60d    |  29.3% |
| rsi_14     |   25.5 |
| zscore_20d |   -1.7 |

### Alphabet Inc. Class A / GOOGL (score 8.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.3% |
| ret_5d     | -11.9% |
| ret_20d    | -19.5% |
| ret_60d    | -21.2% |
| ma20_dist  | -15.6% |
| ma50_dist  | -17.4% |
| vol_20d    |  46.7% |
| mdd_60d    |  21.9% |
| rsi_14     |   13.1 |
| zscore_20d |   -2.2 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Tesla Inc. / TSLA                   |  15.0893 |           3.7% |                 0.28x |       30.1786 |            7.5% |
| DAX / ^GDAXI                        | 319.3005 |           1.2% |                 0.71x |      638.6010 |            2.5% |
| CAC 40 / ^FCHI                      |  88.9415 |           1.1% |                 0.84x |      177.8830 |            2.2% |
| FTSE 100 / ^FTSE                    | 100.5643 |           0.9% |                 1.06x |      201.1286 |            1.9% |
| JPMorgan Chase & Co. / JPM          |   6.4179 |           1.9% |                 0.66x |       12.8357 |            3.8% |
| Dow Jones Industrial Average / ^DJI | 530.7843 |           1.0% |                 1.04x |     1061.5686 |            2.0% |
| Euro Stoxx 50 / ^STOXX50E           |  75.0265 |           1.2% |                 0.72x |      150.0530 |            2.4% |
| Apple Inc. / AAPL                   |   6.7964 |           2.0% |                 0.64x |       13.5929 |            4.0% |
| UnitedHealth Group Inc. / UNH       |  12.0414 |           3.0% |                 0.35x |       24.0829 |            6.0% |
| Russell 2000 / ^RUT                 |  38.9357 |           1.4% |                 0.64x |       77.8714 |            2.8% |
| S&P 500 / ^GSPC                     |  89.4829 |           1.2% |                 0.89x |      178.9658 |            2.4% |
| Hang Seng / ^HSI                    | 372.7154 |           1.6% |                 0.58x |      745.4308 |            3.2% |
| Brent Crude Oil / BZ=F              |   4.5521 |           4.3% |                 0.20x |        9.1043 |            8.7% |
| Amazon.com Inc. / AMZN              |   8.3607 |           3.4% |                 0.28x |       16.7214 |            6.8% |
| Soybeans / ZS=F                     |  16.4643 |           1.4% |                 0.91x |       32.9286 |            2.7% |
| Gold / GC=F                         |  77.5714 |           2.0% |                 0.50x |      155.1429 |            3.9% |
| Microsoft Corporation / MSFT        |  12.7857 |           2.5% |                 0.47x |       25.5714 |            5.0% |
| Corn / ZC=F                         |   6.8571 |           1.5% |                 0.54x |       13.7143 |            3.1% |
| Wheat / ZW=F                        |  13.6786 |           2.3% |                 0.57x |       27.3571 |            4.5% |
| NASDAQ 100 / ^NDX                   | 626.2407 |           2.2% |                 0.46x |     1252.4813 |            4.5% |
| Meta Platforms Inc. / META          |  23.5400 |           3.9% |                 0.28x |       47.0800 |            7.8% |
| Platinum / PL=F                     |  32.3571 |           2.2% |                 0.33x |       64.7143 |            4.4% |
| NVIDIA Corporation / NVDA           |   6.7357 |           3.3% |                 0.34x |       13.4714 |            6.7% |
| Silver / SI=F                       |   1.3977 |           2.8% |                 0.25x |        2.7954 |            5.5% |
| Alphabet Inc. Class A / GOOGL       |  10.9293 |           3.9% |                 0.21x |       21.8586 |            7.8% |

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

Scoring engine version: **1.0.0** | Git commit: **8db0dfc**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
