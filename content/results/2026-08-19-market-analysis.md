+++
title = "Market Analysis 2026-08-19"
date = "2026-08-19T00:00:00+00:00"
draft = false
summary = "Bullish market: 26 reliable instruments. Top signal: JPM (score 76.7)."
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
source_files = ["data/analysis/2026-08-19.json", "data/history/2026-08-19.json"]
market_regime = "Bullish"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "3dfe925"
+++

## Market Regime

**Bullish** — 20 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **JPMorgan Chase & Co. / JPM** — score 76.7, 20d return +5.2%, RSI14=78. 20d up +5.2%; above MA20 by 1.9%; RSI14=78
- **Corn / ZC=F** — score 74.2, 20d return +5.4%, RSI14=63. 20d up +5.4%; above MA20 by 8.0%; RSI14=63
- **Euro Stoxx 50 / ^STOXX50E** — score 70.3, 20d return +4.9%, RSI14=80. 20d up +4.9%; above MA20 by 1.8%; RSI14=80
- **DAX / ^GDAXI** — score 69.1, 20d return +6.0%, RSI14=81. 20d up +6.0%; above MA20 by 2.0%; RSI14=81
- **Wheat / ZW=F** — score 68.5, 20d return -2.0%, RSI14=63. 20d down -2.0%; above MA20 by 4.0%; RSI14=63

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                 | Applies To |
| ---------- | --------------------- | ---------- |
| 2026-08-26 | NVDA earnings release | NVDA       |

## Signal History

Compared with the previous available report (**2026-08-18**).

- **New top-5:** JPM
- **Persistent top signals:** ZC=F (5 reports), ^GDAXI (4 reports), ZW=F (3 reports), ^STOXX50E (2 reports)
- **Dropped from top-5:** GC=F

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     -2 |    -8.8 |
| 7203.T    |     +3 |    +8.5 |
| 8306.T    |     +1 |   +12.7 |
| AAPL      |     +2 |    +9.4 |
| AMZN      |     -2 |    -1.8 |
| BZ=F      |     +5 |    +6.7 |
| CL=F      |     -1 |    +1.5 |
| GC=F      |     -4 |    -4.5 |
| GOOGL     |     +1 |   +10.9 |
| HG=F      |     -1 |    -8.8 |
| JPM       |     +8 |   +17.9 |
| META      |     +0 |    -2.7 |
| MSFT      |     +7 |    +7.0 |
| NG=F      |     +7 |   +15.8 |
| NVDA      |     -4 |   -13.3 |
| PL=F      |     -6 |   -21.2 |
| SI=F      |     -6 |   -18.5 |
| TSLA      |     +0 |    +2.7 |
| UNH       |     -2 |    +4.8 |
| XOM       |     +0 |    +7.9 |
| ZC=F      |     -1 |    +0.9 |
| ZS=F      |     +1 |    +3.3 |
| ZW=F      |     +0 |    +2.1 |
| ^DJI      |     +5 |    +5.5 |
| ^FCHI     |     -4 |    -8.5 |
| ^FTSE     |     +2 |    -0.3 |
| ^GDAXI    |     -2 |    -1.8 |
| ^GSPC     |     +5 |    -0.3 |
| ^HSI      |     -4 |    -7.9 |
| ^N225     |     +0 |    +3.0 |
| ^NDX      |     -4 |   -12.4 |
| ^RUT      |     -5 |   -11.8 |
| ^STOXX50E |     +1 |    +2.1 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Exxon Mobil Corporation / XOM** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **WTI Crude Oil / CL=F** — malformed_input
- **Copper / HG=F** — malformed_input

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|    2 | Corn / ZC=F            |  74.2 |   Yes    | —               | 20d up +5.4%; above MA20 by 8.0%; RSI14=63   |
|    5 | Wheat / ZW=F           |  68.5 |   Yes    | —               | 20d down -2.0%; above MA20 by 4.0%; RSI14=63 |
|    6 | Soybeans / ZS=F        |  67.3 |   Yes    | —               | 20d down -1.2%; above MA20 by 3.6%; RSI14=66 |
|    7 | Gold / GC=F            |  64.8 |   Yes    | —               | 20d up +8.9%; above MA20 by 3.9%; RSI14=80   |
|   12 | Brent Crude Oil / BZ=F |  49.7 |   Yes    | —               | 20d down -8.7%; above MA20 by 5.4%; RSI14=53 |
|   17 | Natural Gas / NG=F     |  38.2 |   Yes    | —               | 20d down -4.5%; above MA20 by 1.8%; RSI14=53 |
|   18 | Silver / SI=F          |  37.9 |   Yes    | —               | 20d up +9.4%; above MA20 by 2.2%; RSI14=69   |
|   19 | Platinum / PL=F        |  34.5 |   Yes    | —               | 20d up +8.1%; above MA20 by 1.5%; RSI14=60   |
|   32 | WTI Crude Oil / CL=F   |  44.2 |    No    | malformed_input | Suppressed: malformed_input                  |
|   33 | Copper / HG=F          |  32.7 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                   |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | --------------------------------------------- |
|    1 | JPMorgan Chase & Co. / JPM                                                     |  76.7 |   Yes    | —                             | 20d up +5.2%; above MA20 by 1.9%; RSI14=78    |
|    8 | Microsoft Corporation / MSFT                                                   |  60.0 |   Yes    | —                             | 20d up +21.1%; above MA20 by 5.1%; RSI14=78   |
|   10 | NVIDIA Corporation / NVDA                                                      |  52.7 |   Yes    | —                             | 20d up +6.0%; above MA20 by 3.6%; RSI14=77    |
|   20 | Apple Inc. / AAPL                                                              |  34.2 |   Yes    | —                             | 20d down -5.3%; below MA20 by 2.0%; RSI14=28  |
|   21 | Tesla Inc. / TSLA                                                              |  31.8 |   Yes    | —                             | 20d down -11.1%; above MA20 by 3.5%; RSI14=75 |
|   22 | Amazon.com Inc. / AMZN                                                         |  31.5 |   Yes    | —                             | 20d up +4.8%; above MA20 by 0.7%; RSI14=68    |
|   24 | Alphabet Inc. Class A / GOOGL                                                  |  28.8 |   Yes    | —                             | 20d down -0.8%; below MA20 by 0.5%; RSI14=54  |
|   25 | UnitedHealth Group Inc. / UNH                                                  |  27.9 |   Yes    | —                             | 20d down -9.7%; below MA20 by 4.3%; RSI14=29  |
|   26 | Meta Platforms Inc. / META                                                     |   6.7 |   Yes    | —                             | 20d down -15.6%; below MA20 by 7.2%; RSI14=39 |
|   27 | Exxon Mobil Corporation / XOM                                                  |  80.3 |    No    | malformed_input               | Suppressed: malformed_input                   |
|   29 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  57.9 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars     |
|   30 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  48.2 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars     |
|   31 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  46.1 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars     |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                |
| ---: | ----------------------------------- | ----: | :------: | ------------ | ------------------------------------------ |
|    3 | Euro Stoxx 50 / ^STOXX50E           |  70.3 |   Yes    | —            | 20d up +4.9%; above MA20 by 1.8%; RSI14=80 |
|    4 | DAX / ^GDAXI                        |  69.1 |   Yes    | —            | 20d up +6.0%; above MA20 by 2.0%; RSI14=81 |
|    9 | S&P 500 / ^GSPC                     |  55.1 |   Yes    | —            | 20d up +2.4%; above MA20 by 1.1%; RSI14=77 |
|   11 | Dow Jones Industrial Average / ^DJI |  52.7 |   Yes    | —            | 20d up +2.1%; above MA20 by 0.4%; RSI14=71 |
|   13 | Russell 2000 / ^RUT                 |  49.4 |   Yes    | —            | 20d up +1.0%; above MA20 by 0.8%; RSI14=66 |
|   14 | CAC 40 / ^FCHI                      |  48.8 |   Yes    | —            | 20d up +2.9%; above MA20 by 0.3%; RSI14=62 |
|   15 | NASDAQ 100 / ^NDX                   |  44.2 |   Yes    | —            | 20d up +1.2%; above MA20 by 1.6%; RSI14=75 |
|   16 | FTSE 100 / ^FTSE                    |  40.9 |   Yes    | —            | 20d up +1.9%; below MA20 by 0.8%; RSI14=29 |
|   23 | Hang Seng / ^HSI                    |  30.6 |   Yes    | —            | 20d up +0.5%; below MA20 by 1.0%; RSI14=39 |
|   28 | Nikkei 225 / ^N225                  |  63.9 |    No    | missing_bars | Suppressed: missing_bars                   |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-08-18 |
| 7203.T    | 2026-08-18 |
| 8306.T    | 2026-08-18 |
| AAPL      | 2026-08-18 |
| AMZN      | 2026-08-18 |
| BZ=F      | 2026-08-18 |
| CL=F      | 2026-08-18 |
| GC=F      | 2026-08-18 |
| GOOGL     | 2026-08-18 |
| HG=F      | 2026-08-18 |
| JPM       | 2026-08-18 |
| META      | 2026-08-18 |
| MSFT      | 2026-08-18 |
| NG=F      | 2026-08-18 |
| NVDA      | 2026-08-18 |
| PL=F      | 2026-08-18 |
| SI=F      | 2026-08-18 |
| TSLA      | 2026-08-18 |
| UNH       | 2026-08-18 |
| XOM       | 2026-08-18 |
| ZC=F      | 2026-08-18 |
| ZS=F      | 2026-08-18 |
| ZW=F      | 2026-08-18 |
| ^DJI      | 2026-08-18 |
| ^FCHI     | 2026-08-17 |
| ^FTSE     | 2026-08-17 |
| ^GDAXI    | 2026-08-17 |
| ^GSPC     | 2026-08-18 |
| ^HSI      | 2026-08-18 |
| ^N225     | 2026-08-18 |
| ^NDX      | 2026-08-18 |
| ^RUT      | 2026-08-18 |
| ^STOXX50E | 2026-08-17 |

## Symbol Details

### JPMorgan Chase & Co. / JPM (score 76.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.6% |
| ret_5d     |  +0.3% |
| ret_20d    |  +5.2% |
| ret_60d    | +20.4% |
| ma20_dist  |  +1.9% |
| ma50_dist  |  +6.6% |
| vol_20d    |  16.9% |
| mdd_60d    |   3.5% |
| rsi_14     |   78.2 |
| zscore_20d |    1.2 |

### Corn / ZC=F (score 74.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +5.2% |
| ret_5d     |  +7.1% |
| ret_20d    |  +5.4% |
| ret_60d    |  +6.9% |
| ma20_dist  |  +8.0% |
| ma50_dist  | +11.7% |
| vol_20d    |  49.4% |
| mdd_60d    |  11.8% |
| rsi_14     |   63.0 |
| zscore_20d |    2.5 |

### Euro Stoxx 50 / ^STOXX50E (score 70.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | -0.1% |
| ret_20d    | +4.9% |
| ret_60d    | +8.5% |
| ma20_dist  | +1.8% |
| ma50_dist  | +3.4% |
| vol_20d    | 10.9% |
| mdd_60d    |  3.2% |
| rsi_14     |  79.7 |
| zscore_20d |   1.0 |

### DAX / ^GDAXI (score 69.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | +0.1% |
| ret_20d    | +6.0% |
| ret_60d    | +3.7% |
| ma20_dist  | +2.0% |
| ma50_dist  | +4.1% |
| vol_20d    | 10.5% |
| mdd_60d    |  4.1% |
| rsi_14     |  80.8 |
| zscore_20d |   1.0 |

### Wheat / ZW=F (score 68.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | +4.5% |
| ret_20d    | -2.0% |
| ret_60d    | +7.4% |
| ma20_dist  | +4.0% |
| ma50_dist  | +7.8% |
| vol_20d    | 32.7% |
| mdd_60d    | 10.7% |
| rsi_14     |  63.1 |
| zscore_20d |   1.5 |

### Soybeans / ZS=F (score 67.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.8% |
| ret_5d     | +5.0% |
| ret_20d    | -1.2% |
| ret_60d    | +3.1% |
| ma20_dist  | +3.6% |
| ma50_dist  | +4.7% |
| vol_20d    | 22.3% |
| mdd_60d    |  8.1% |
| rsi_14     |  65.7 |
| zscore_20d |   1.7 |

### Gold / GC=F (score 64.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | -0.0% |
| ret_20d    | +8.9% |
| ret_60d    | -2.0% |
| ma20_dist  | +3.9% |
| ma50_dist  | +5.9% |
| vol_20d    | 19.0% |
| mdd_60d    | 12.6% |
| rsi_14     |  79.6 |
| zscore_20d |   1.0 |

### Microsoft Corporation / MSFT (score 60.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.3% |
| ret_5d     |  -4.4% |
| ret_20d    | +21.1% |
| ret_60d    | +14.9% |
| ma20_dist  |  +5.1% |
| ma50_dist  | +16.0% |
| vol_20d    |  60.7% |
| mdd_60d    |  23.4% |
| rsi_14     |   78.1 |
| zscore_20d |    0.5 |

### S&P 500 / ^GSPC (score 55.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | -0.5% |
| ret_20d    | +2.4% |
| ret_60d    | +3.3% |
| ma20_dist  | +1.1% |
| ma50_dist  | +2.3% |
| vol_20d    | 13.3% |
| mdd_60d    |  4.5% |
| rsi_14     |  76.8 |
| zscore_20d |   0.5 |

### NVIDIA Corporation / NVDA (score 52.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.3% |
| ret_5d     | +1.0% |
| ret_20d    | +6.0% |
| ret_60d    | +0.1% |
| ma20_dist  | +3.6% |
| ma50_dist  | +6.2% |
| vol_20d    | 38.1% |
| mdd_60d    | 15.3% |
| rsi_14     |  77.4 |
| zscore_20d |   0.7 |

### Dow Jones Industrial Average / ^DJI (score 52.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | -0.8% |
| ret_20d    | +2.1% |
| ret_60d    | +6.1% |
| ma20_dist  | +0.4% |
| ma50_dist  | +1.7% |
| vol_20d    | 13.7% |
| mdd_60d    |  3.2% |
| rsi_14     |  70.8 |
| zscore_20d |   0.2 |

### Brent Crude Oil / BZ=F (score 49.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.2% |
| ret_5d     |  +3.3% |
| ret_20d    |  -8.7% |
| ret_60d    |  -7.7% |
| ma20_dist  |  +5.4% |
| ma50_dist  | +10.0% |
| vol_20d    |  61.9% |
| mdd_60d    |  26.8% |
| rsi_14     |   53.4 |
| zscore_20d |    1.1 |

### Russell 2000 / ^RUT (score 49.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.3% |
| ret_5d     | -0.3% |
| ret_20d    | +1.0% |
| ret_60d    | +6.1% |
| ma20_dist  | +0.8% |
| ma50_dist  | +1.4% |
| vol_20d    | 14.9% |
| mdd_60d    |  3.9% |
| rsi_14     |  66.1 |
| zscore_20d |   0.5 |

### CAC 40 / ^FCHI (score 48.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | -1.7% |
| ret_20d    | +2.9% |
| ret_60d    | +3.9% |
| ma20_dist  | +0.3% |
| ma50_dist  | +1.6% |
| vol_20d    | 10.4% |
| mdd_60d    |  3.0% |
| rsi_14     |  61.7 |
| zscore_20d |   0.2 |

### NASDAQ 100 / ^NDX (score 44.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.7% |
| ret_5d     | -0.1% |
| ret_20d    | +1.2% |
| ret_60d    | +0.5% |
| ma20_dist  | +1.6% |
| ma50_dist  | +0.6% |
| vol_20d    | 23.4% |
| mdd_60d    | 11.3% |
| rsi_14     |  75.0 |
| zscore_20d |   0.5 |

### FTSE 100 / ^FTSE (score 40.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | -1.3% |
| ret_20d    | +1.9% |
| ret_60d    | +2.4% |
| ma20_dist  | -0.8% |
| ma50_dist  | +1.0% |
| vol_20d    |  7.9% |
| mdd_60d    |  2.6% |
| rsi_14     |  28.7 |
| zscore_20d |  -1.0 |

### Natural Gas / NG=F (score 38.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +3.5% |
| ret_5d     | -0.7% |
| ret_20d    | -4.5% |
| ret_60d    | -3.8% |
| ma20_dist  | +1.8% |
| ma50_dist  | -5.7% |
| vol_20d    | 34.8% |
| mdd_60d    | 21.0% |
| rsi_14     |  52.7 |
| zscore_20d |   0.9 |

### Silver / SI=F (score 37.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -4.4% |
| ret_5d     |  -3.6% |
| ret_20d    |  +9.4% |
| ret_60d    | -17.1% |
| ma20_dist  |  +2.2% |
| ma50_dist  |  +2.9% |
| vol_20d    |  31.7% |
| mdd_60d    |  26.1% |
| rsi_14     |   69.0 |
| zscore_20d |    0.4 |

### Platinum / PL=F (score 34.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -3.0% |
| ret_5d     |  -1.9% |
| ret_20d    |  +8.1% |
| ret_60d    | -11.0% |
| ma20_dist  |  +1.5% |
| ma50_dist  |  +3.7% |
| vol_20d    |  36.4% |
| mdd_60d    |  20.0% |
| rsi_14     |   60.1 |
| zscore_20d |    0.4 |

### Apple Inc. / AAPL (score 34.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.5% |
| ret_5d     | +1.7% |
| ret_20d    | -5.3% |
| ret_60d    | +1.7% |
| ma20_dist  | -2.0% |
| ma50_dist  | +0.3% |
| vol_20d    | 33.1% |
| mdd_60d    | 12.7% |
| rsi_14     |  28.2 |
| zscore_20d |  -0.5 |

### Tesla Inc. / TSLA (score 31.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.7% |
| ret_5d     |  +1.2% |
| ret_20d    | -11.1% |
| ret_60d    | -19.4% |
| ma20_dist  |  +3.5% |
| ma50_dist  |  -8.6% |
| vol_20d    |  59.5% |
| mdd_60d    |  32.5% |
| rsi_14     |   75.5 |
| zscore_20d |    0.7 |

### Amazon.com Inc. / AMZN (score 31.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | -4.7% |
| ret_20d    | +4.8% |
| ret_60d    | -3.4% |
| ma20_dist  | +0.7% |
| ma50_dist  | +4.4% |
| vol_20d    | 63.1% |
| mdd_60d    | 17.3% |
| rsi_14     |  67.5 |
| zscore_20d |   0.1 |

### Hang Seng / ^HSI (score 30.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | -1.5% |
| ret_20d    | +0.5% |
| ret_60d    | -0.5% |
| ma20_dist  | -1.0% |
| ma50_dist  | +2.5% |
| vol_20d    | 15.2% |
| mdd_60d    | 12.9% |
| rsi_14     |  39.3 |
| zscore_20d |  -0.8 |

### Alphabet Inc. Class A / GOOGL (score 28.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.1% |
| ret_5d     |  +0.1% |
| ret_20d    |  -0.8% |
| ret_60d    | -11.2% |
| ma20_dist  |  -0.5% |
| ma50_dist  |  -2.4% |
| vol_20d    |  46.3% |
| mdd_60d    |  18.5% |
| rsi_14     |   54.0 |
| zscore_20d |   -0.1 |

### UnitedHealth Group Inc. / UNH (score 27.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -2.1% |
| ret_20d    | -9.7% |
| ret_60d    | +3.6% |
| ma20_dist  | -4.3% |
| ma50_dist  | -5.0% |
| vol_20d    | 20.5% |
| mdd_60d    |  9.7% |
| rsi_14     |  28.7 |
| zscore_20d |  -1.7 |

### Meta Platforms Inc. / META (score 6.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -4.4% |
| ret_5d     |  -9.3% |
| ret_20d    | -15.6% |
| ret_60d    | -10.4% |
| ma20_dist  |  -7.2% |
| ma50_dist  |  -8.6% |
| vol_20d    |  46.8% |
| mdd_60d    |  20.9% |
| rsi_14     |   39.5 |
| zscore_20d |   -2.1 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| JPMorgan Chase & Co. / JPM          |   5.4857 |           1.5% |                 0.59x |       10.9714 |            3.0% |
| Corn / ZC=F                         |  16.3929 |           3.4% |                 0.20x |       32.7857 |            6.7% |
| Euro Stoxx 50 / ^STOXX50E           |  58.3122 |           0.9% |                 0.91x |      116.6244 |            1.8% |
| DAX / ^GDAXI                        | 260.7812 |           1.0% |                 0.95x |      521.5625 |            2.0% |
| Wheat / ZW=F                        |  20.1250 |           2.9% |                 0.31x |       40.2500 |            5.9% |
| Soybeans / ZS=F                     |  16.0179 |           1.3% |                 0.45x |       32.0357 |            2.6% |
| Gold / GC=F                         |  77.1429 |           1.7% |                 0.53x |      154.2858 |            3.5% |
| Microsoft Corporation / MSFT        |  16.9728 |           3.5% |                 0.16x |       33.9456 |            7.0% |
| S&P 500 / ^GSPC                     |  72.6443 |           0.9% |                 0.75x |      145.2886 |            1.9% |
| NVIDIA Corporation / NVDA           |   6.5814 |           3.0% |                 0.26x |       13.1628 |            6.0% |
| Dow Jones Industrial Average / ^DJI | 492.2369 |           0.9% |                 0.73x |      984.4738 |            1.8% |
| Brent Crude Oil / BZ=F              |   3.4771 |           3.8% |                 0.16x |        6.9543 |            7.6% |
| Russell 2000 / ^RUT                 |  33.5834 |           1.1% |                 0.67x |       67.1669 |            2.2% |
| CAC 40 / ^FCHI                      |  71.3622 |           0.8% |                 0.96x |      142.7245 |            1.7% |
| NASDAQ 100 / ^NDX                   | 493.1568 |           1.7% |                 0.43x |      986.3136 |            3.3% |
| FTSE 100 / ^FTSE                    |  89.2642 |           0.8% |                 1.27x |      178.5285 |            1.7% |
| Natural Gas / NG=F                  |   0.0858 |           3.1% |                 0.29x |        0.1716 |            6.2% |
| Silver / SI=F                       |   1.5049 |           2.4% |                 0.32x |        3.0099 |            4.8% |
| Platinum / PL=F                     |  30.1714 |           1.7% |                 0.27x |       60.3429 |            3.5% |
| Apple Inc. / AAPL                   |   8.2824 |           2.7% |                 0.30x |       16.5647 |            5.3% |
| Tesla Inc. / TSLA                   |  10.8550 |           3.2% |                 0.17x |       21.7100 |            6.4% |
| Amazon.com Inc. / AMZN              |   9.8393 |           3.8% |                 0.16x |       19.6786 |            7.6% |
| Hang Seng / ^HSI                    | 330.3266 |           1.3% |                 0.66x |      660.6532 |            2.6% |
| Alphabet Inc. Class A / GOOGL       |  10.7086 |           3.1% |                 0.22x |       21.4171 |            6.2% |
| UnitedHealth Group Inc. / UNH       |   9.7464 |           2.5% |                 0.49x |       19.4929 |            4.9% |
| Meta Platforms Inc. / META          |  22.9571 |           4.2% |                 0.21x |       45.9143 |            8.4% |

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

Scoring engine version: **1.0.0** | Git commit: **3dfe925**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
