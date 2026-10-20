+++
title = "Market Analysis 2026-08-25"
date = "2026-08-25T00:00:00+00:00"
draft = false
summary = "Neutral market: 26 reliable instruments. Top signal: GC=F (score 78.5)."
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
source_files = ["data/analysis/2026-08-25.json", "data/history/2026-08-25.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "f940031"
+++

## Market Regime

**Neutral** — 13 of 26 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Gold / GC=F** — score 78.5, 20d return +14.6%, RSI14=77. 20d up +14.6%; above MA20 by 7.3%; RSI14=77
- **Corn / ZC=F** — score 77.9, 20d return +16.2%, RSI14=70. 20d up +16.2%; above MA20 by 12.1%; RSI14=70
- **Wheat / ZW=F** — score 66.1, 20d return +5.6%, RSI14=67. 20d up +5.6%; above MA20 by 5.9%; RSI14=67
- **Soybeans / ZS=F** — score 65.5, 20d return +3.9%, RSI14=71. 20d up +3.9%; above MA20 by 3.3%; RSI14=71
- **Platinum / PL=F** — score 64.8, 20d return +13.9%, RSI14=68. 20d up +13.9%; above MA20 by 6.7%; RSI14=68

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                 | Applies To |
| ---------- | --------------------- | ---------- |
| 2026-08-26 | NVDA earnings release | NVDA       |

## Signal History

Compared with the previous available report (**2026-08-24**).

- **New top-5:** None
- **Persistent top signals:** ZC=F (9 reports), ZW=F (7 reports), GC=F (4 reports), PL=F (3 reports), ZS=F (2 reports)
- **Dropped from top-5:** None

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +2 |   +18.5 |
| 7203.T    |     -1 |    -1.8 |
| 8306.T    |     -1 |    -6.4 |
| AAPL      |     +3 |    +6.7 |
| AMZN      |     +7 |   +11.2 |
| BZ=F      |     +7 |   +10.0 |
| CL=F      |     +0 |    +8.8 |
| GC=F      |     +1 |    -2.7 |
| GOOGL     |     -1 |    +2.1 |
| HG=F      |     +0 |   +13.9 |
| JPM       |     +7 |   +13.0 |
| META      |     +0 |    +6.4 |
| MSFT      |     +7 |    +8.5 |
| NG=F      |     +6 |    +8.2 |
| NVDA      |     -4 |   -10.0 |
| PL=F      |     +0 |    +1.2 |
| SI=F      |     -2 |    -4.5 |
| TSLA      |     -8 |   -18.8 |
| UNH       |     +7 |    +9.4 |
| XOM       |     -1 |    +1.5 |
| ZC=F      |     -1 |    -3.9 |
| ZS=F      |     +0 |    -5.8 |
| ZW=F      |     +0 |   -11.8 |
| ^DJI      |     -1 |    +0.3 |
| ^FCHI     |     -2 |    -5.5 |
| ^FTSE     |     +9 |   +11.5 |
| ^GDAXI    |     -1 |    +0.0 |
| ^GSPC     |     -2 |    -5.2 |
| ^HSI      |    -15 |   -24.6 |
| ^N225     |     +1 |    +1.8 |
| ^NDX      |     -7 |   -13.6 |
| ^RUT      |     -7 |   -15.2 |
| ^STOXX50E |     -3 |    -3.3 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars

## Key Risks

- **malformed_input** (6 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                  |
| ---: | ---------------------- | ----: | :------: | --------------- | -------------------------------------------- |
|    1 | Gold / GC=F            |  78.5 |   Yes    | —               | 20d up +14.6%; above MA20 by 7.3%; RSI14=77  |
|    2 | Corn / ZC=F            |  77.9 |   Yes    | —               | 20d up +16.2%; above MA20 by 12.1%; RSI14=70 |
|    3 | Wheat / ZW=F           |  66.1 |   Yes    | —               | 20d up +5.6%; above MA20 by 5.9%; RSI14=67   |
|    4 | Soybeans / ZS=F        |  65.5 |   Yes    | —               | 20d up +3.9%; above MA20 by 3.3%; RSI14=71   |
|    5 | Platinum / PL=F        |  64.8 |   Yes    | —               | 20d up +13.9%; above MA20 by 6.7%; RSI14=68  |
|    8 | Silver / SI=F          |  57.3 |   Yes    | —               | 20d up +16.0%; above MA20 by 5.9%; RSI14=68  |
|    9 | Brent Crude Oil / BZ=F |  55.8 |   Yes    | —               | 20d up +4.2%; above MA20 by 5.4%; RSI14=78   |
|   14 | Natural Gas / NG=F     |  47.0 |   Yes    | —               | 20d up +2.0%; above MA20 by 2.7%; RSI14=61   |
|   30 | Copper / HG=F          |  56.7 |    No    | malformed_input | Suppressed: malformed_input                  |
|   31 | WTI Crude Oil / CL=F   |  50.0 |    No    | malformed_input | Suppressed: malformed_input                  |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    7 | Microsoft Corporation / MSFT                                                   |  59.4 |   Yes    | —                             | 20d up +25.5%; above MA20 by 2.1%; RSI14=47  |
|   11 | JPMorgan Chase & Co. / JPM                                                     |  53.9 |   Yes    | —                             | 20d up +0.1%; below MA20 by 0.2%; RSI14=48   |
|   16 | Tesla Inc. / TSLA                                                              |  39.4 |   Yes    | —                             | 20d up +12.8%; above MA20 by 5.7%; RSI14=61  |
|   17 | Amazon.com Inc. / AMZN                                                         |  39.1 |   Yes    | —                             | 20d up +13.3%; below MA20 by 0.3%; RSI14=34  |
|   18 | UnitedHealth Group Inc. / UNH                                                  |  37.3 |   Yes    | —                             | 20d down -4.5%; below MA20 by 1.6%; RSI14=44 |
|   20 | Apple Inc. / AAPL                                                              |  36.4 |   Yes    | —                             | 20d down -7.8%; below MA20 by 0.8%; RSI14=52 |
|   23 | Alphabet Inc. Class A / GOOGL                                                  |  33.6 |   Yes    | —                             | 20d up +6.6%; below MA20 by 0.4%; RSI14=24   |
|   25 | NVIDIA Corporation / NVDA                                                      |  26.1 |   Yes    | —                             | 20d up +6.1%; below MA20 by 2.5%; RSI14=46   |
|   26 | Meta Platforms Inc. / META                                                     |  17.0 |   Yes    | —                             | 20d down -5.9%; below MA20 by 2.7%; RSI14=37 |
|   27 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  67.0 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   28 | Exxon Mobil Corporation / XOM                                                  |  67.0 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   29 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  60.9 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   33 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  29.7 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                |
| ---: | ----------------------------------- | ----: | :------: | ------------ | ------------------------------------------ |
|    6 | FTSE 100 / ^FTSE                    |  60.3 |   Yes    | —            | 20d up +0.7%; above MA20 by 0.2%; RSI14=47 |
|   10 | DAX / ^GDAXI                        |  55.1 |   Yes    | —            | 20d up +2.9%; above MA20 by 0.1%; RSI14=46 |
|   12 | Dow Jones Industrial Average / ^DJI |  52.4 |   Yes    | —            | 20d up +2.3%; above MA20 by 0.1%; RSI14=40 |
|   13 | Euro Stoxx 50 / ^STOXX50E           |  50.9 |   Yes    | —            | 20d up +2.6%; below MA20 by 0.1%; RSI14=43 |
|   15 | S&P 500 / ^GSPC                     |  46.1 |   Yes    | —            | 20d up +3.2%; below MA20 by 0.0%; RSI14=40 |
|   19 | Russell 2000 / ^RUT                 |  37.0 |   Yes    | —            | 20d up +1.6%; below MA20 by 0.4%; RSI14=43 |
|   21 | CAC 40 / ^FCHI                      |  35.1 |   Yes    | —            | 20d up +0.6%; below MA20 by 1.5%; RSI14=23 |
|   22 | Hang Seng / ^HSI                    |  35.1 |   Yes    | —            | 20d up +1.2%; below MA20 by 0.5%; RSI14=45 |
|   24 | NASDAQ 100 / ^NDX                   |  28.2 |   Yes    | —            | 20d up +3.5%; below MA20 by 0.6%; RSI14=37 |
|   32 | Nikkei 225 / ^N225                  |  33.6 |    No    | missing_bars | Suppressed: missing_bars                   |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-08-24 |
| 7203.T    | 2026-08-24 |
| 8306.T    | 2026-08-24 |
| AAPL      | 2026-08-24 |
| AMZN      | 2026-08-24 |
| BZ=F      | 2026-08-24 |
| CL=F      | 2026-08-24 |
| GC=F      | 2026-08-24 |
| GOOGL     | 2026-08-24 |
| HG=F      | 2026-08-24 |
| JPM       | 2026-08-24 |
| META      | 2026-08-24 |
| MSFT      | 2026-08-24 |
| NG=F      | 2026-08-24 |
| NVDA      | 2026-08-24 |
| PL=F      | 2026-08-24 |
| SI=F      | 2026-08-24 |
| TSLA      | 2026-08-24 |
| UNH       | 2026-08-24 |
| XOM       | 2026-08-24 |
| ZC=F      | 2026-08-24 |
| ZS=F      | 2026-08-24 |
| ZW=F      | 2026-08-24 |
| ^DJI      | 2026-08-24 |
| ^FCHI     | 2026-08-24 |
| ^FTSE     | 2026-08-24 |
| ^GDAXI    | 2026-08-24 |
| ^GSPC     | 2026-08-24 |
| ^HSI      | 2026-08-24 |
| ^N225     | 2026-08-24 |
| ^NDX      | 2026-08-24 |
| ^RUT      | 2026-08-24 |
| ^STOXX50E | 2026-08-24 |

## Symbol Details

### Gold / GC=F (score 78.5)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.2% |
| ret_5d     |  +7.6% |
| ret_20d    | +14.6% |
| ret_60d    |  +4.6% |
| ma20_dist  |  +7.3% |
| ma50_dist  | +11.8% |
| vol_20d    |  21.8% |
| mdd_60d    |  11.0% |
| rsi_14     |   76.7 |
| zscore_20d |    1.8 |

### Corn / ZC=F (score 77.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.6% |
| ret_5d     | +11.8% |
| ret_20d    | +16.2% |
| ret_60d    | +17.5% |
| ma20_dist  | +12.1% |
| ma50_dist  | +16.2% |
| vol_20d    |  51.1% |
| mdd_60d    |   6.8% |
| rsi_14     |   69.6 |
| zscore_20d |    2.3 |

### Wheat / ZW=F (score 66.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.7% |
| ret_5d     |  +5.5% |
| ret_20d    |  +5.6% |
| ret_60d    | +16.2% |
| ma20_dist  |  +5.9% |
| ma50_dist  |  +9.0% |
| vol_20d    |  35.4% |
| mdd_60d    |  10.7% |
| rsi_14     |   66.8 |
| zscore_20d |    1.7 |

### Soybeans / ZS=F (score 65.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.9% |
| ret_5d     | +1.9% |
| ret_20d    | +3.9% |
| ret_60d    | +5.0% |
| ma20_dist  | +3.3% |
| ma50_dist  | +3.8% |
| vol_20d    | 16.4% |
| mdd_60d    |  8.1% |
| rsi_14     |  70.7 |
| zscore_20d |   1.4 |

### Platinum / PL=F (score 64.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.6% |
| ret_5d     |  +9.0% |
| ret_20d    | +13.9% |
| ret_60d    |  -2.8% |
| ma20_dist  |  +6.7% |
| ma50_dist  | +12.1% |
| vol_20d    |  37.5% |
| mdd_60d    |  18.2% |
| rsi_14     |   68.1 |
| zscore_20d |    1.7 |

### FTSE 100 / ^FTSE (score 60.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +1.2% |
| ret_20d    | +0.7% |
| ret_60d    | +5.0% |
| ma20_dist  | +0.2% |
| ma50_dist  | +1.8% |
| vol_20d    |  5.3% |
| mdd_60d    |  1.9% |
| rsi_14     |  46.7 |
| zscore_20d |   0.4 |

### Microsoft Corporation / MSFT (score 59.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.8% |
| ret_5d     |  +1.6% |
| ret_20d    | +25.5% |
| ret_60d    | +14.1% |
| ma20_dist  |  +2.1% |
| ma50_dist  | +15.6% |
| vol_20d    |  58.7% |
| mdd_60d    |  23.4% |
| rsi_14     |   46.8 |
| zscore_20d |    0.3 |

### Silver / SI=F (score 57.3)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.5% |
| ret_5d     |  +6.7% |
| ret_20d    | +16.0% |
| ret_60d    |  -9.4% |
| ma20_dist  |  +5.9% |
| ma50_dist  | +10.8% |
| vol_20d    |  31.9% |
| mdd_60d    |  24.2% |
| rsi_14     |   67.6 |
| zscore_20d |    1.2 |

### Brent Crude Oil / BZ=F (score 55.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.2% |
| ret_5d     |  +1.9% |
| ret_20d    |  +4.2% |
| ret_60d    |  -3.3% |
| ma20_dist  |  +5.4% |
| ma50_dist  | +10.2% |
| vol_20d    |  41.2% |
| mdd_60d    |  26.8% |
| rsi_14     |   77.9 |
| zscore_20d |    1.1 |

### DAX / ^GDAXI (score 55.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | -0.9% |
| ret_20d    | +2.9% |
| ret_60d    | +4.4% |
| ma20_dist  | +0.1% |
| ma50_dist  | +2.5% |
| vol_20d    |  8.0% |
| mdd_60d    |  4.1% |
| rsi_14     |  46.1 |
| zscore_20d |   0.1 |

### JPMorgan Chase & Co. / JPM (score 53.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.4% |
| ret_5d     |  -1.3% |
| ret_20d    |  +0.1% |
| ret_60d    | +20.6% |
| ma20_dist  |  -0.2% |
| ma50_dist  |  +3.5% |
| vol_20d    |  18.9% |
| mdd_60d    |   3.7% |
| rsi_14     |   48.5 |
| zscore_20d |   -0.1 |

### Dow Jones Industrial Average / ^DJI (score 52.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | -0.1% |
| ret_20d    | +2.3% |
| ret_60d    | +5.4% |
| ma20_dist  | +0.1% |
| ma50_dist  | +1.5% |
| vol_20d    | 14.3% |
| mdd_60d    |  3.2% |
| rsi_14     |  39.5 |
| zscore_20d |   0.1 |

### Euro Stoxx 50 / ^STOXX50E (score 50.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.2% |
| ret_5d     | -1.3% |
| ret_20d    | +2.6% |
| ret_60d    | +6.8% |
| ma20_dist  | -0.1% |
| ma50_dist  | +1.5% |
| vol_20d    |  9.1% |
| mdd_60d    |  3.2% |
| rsi_14     |  43.3 |
| zscore_20d |  -0.1 |

### Natural Gas / NG=F (score 47.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.6% |
| ret_5d     |  +1.4% |
| ret_20d    |  +2.0% |
| ret_60d    | -11.1% |
| ma20_dist  |  +2.7% |
| ma50_dist  |  -3.5% |
| vol_20d    |  30.2% |
| mdd_60d    |  21.0% |
| rsi_14     |   61.4 |
| zscore_20d |    1.4 |

### S&P 500 / ^GSPC (score 46.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | -1.2% |
| ret_20d    | +3.2% |
| ret_60d    | +1.2% |
| ma20_dist  | -0.0% |
| ma50_dist  | +1.4% |
| vol_20d    | 13.0% |
| mdd_60d    |  4.5% |
| rsi_14     |  40.0 |
| zscore_20d |  -0.0 |

### Tesla Inc. / TSLA (score 39.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -3.8% |
| ret_5d     |  +2.8% |
| ret_20d    | +12.8% |
| ret_60d    | -21.1% |
| ma20_dist  |  +5.7% |
| ma50_dist  |  -4.4% |
| vol_20d    |  39.2% |
| mdd_60d    |  31.5% |
| rsi_14     |   61.0 |
| zscore_20d |    1.2 |

### Amazon.com Inc. / AMZN (score 39.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.3% |
| ret_5d     |  +0.3% |
| ret_20d    | +13.3% |
| ret_60d    |  -4.4% |
| ma20_dist  |  -0.3% |
| ma50_dist  |  +4.8% |
| vol_20d    |  61.3% |
| mdd_60d    |  16.3% |
| rsi_14     |   33.6 |
| zscore_20d |   -0.1 |

### UnitedHealth Group Inc. / UNH (score 37.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +2.2% |
| ret_5d     | +0.8% |
| ret_20d    | -4.5% |
| ret_60d    | +4.8% |
| ma20_dist  | -1.6% |
| ma50_dist  | -3.6% |
| vol_20d    | 22.9% |
| mdd_60d    | 11.8% |
| rsi_14     |  43.6 |
| zscore_20d |  -0.6 |

### Russell 2000 / ^RUT (score 37.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | -2.0% |
| ret_20d    | +1.6% |
| ret_60d    | +2.0% |
| ma20_dist  | -0.4% |
| ma50_dist  | +0.3% |
| vol_20d    | 15.5% |
| mdd_60d    |  3.9% |
| rsi_14     |  42.8 |
| zscore_20d |  -0.3 |

### Apple Inc. / AAPL (score 36.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | +1.6% |
| ret_20d    | -7.8% |
| ret_60d    | -0.7% |
| ma20_dist  | -0.8% |
| ma50_dist  | -0.0% |
| vol_20d    | 31.3% |
| mdd_60d    | 12.7% |
| rsi_14     |  51.6 |
| zscore_20d |  -0.2 |

### CAC 40 / ^FCHI (score 35.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -1.5% |
| ret_20d    | +0.6% |
| ret_60d    | +3.8% |
| ma20_dist  | -1.5% |
| ma50_dist  | -0.2% |
| vol_20d    |  8.5% |
| mdd_60d    |  3.1% |
| rsi_14     |  23.0 |
| zscore_20d |  -1.2 |

### Hang Seng / ^HSI (score 35.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.9% |
| ret_5d     | +0.3% |
| ret_20d    | +1.2% |
| ret_60d    | +2.0% |
| ma20_dist  | -0.5% |
| ma50_dist  | +3.2% |
| vol_20d    | 15.4% |
| mdd_60d    | 12.9% |
| rsi_14     |  44.5 |
| zscore_20d |  -0.5 |

### Alphabet Inc. Class A / GOOGL (score 33.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.9% |
| ret_5d     |  +1.2% |
| ret_20d    |  +6.6% |
| ret_60d    | -10.7% |
| ma20_dist  |  -0.4% |
| ma50_dist  |  -1.0% |
| vol_20d    |  37.8% |
| mdd_60d    |  16.4% |
| rsi_14     |   24.4 |
| zscore_20d |   -0.1 |

### NASDAQ 100 / ^NDX (score 28.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | -3.2% |
| ret_20d    | +3.5% |
| ret_60d    | -4.0% |
| ma20_dist  | -0.6% |
| ma50_dist  | -1.0% |
| vol_20d    | 22.2% |
| mdd_60d    | 11.3% |
| rsi_14     |  36.9 |
| zscore_20d |  -0.2 |

### NVIDIA Corporation / NVDA (score 26.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -2.9% |
| ret_5d     | -7.3% |
| ret_20d    | +6.1% |
| ret_60d    | -2.7% |
| ma20_dist  | -2.5% |
| ma50_dist  | +0.4% |
| vol_20d    | 34.1% |
| mdd_60d    | 15.3% |
| rsi_14     |  46.0 |
| zscore_20d |  -0.5 |

### Meta Platforms Inc. / META (score 17.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.7% |
| ret_5d     |  -1.7% |
| ret_20d    |  -5.9% |
| ret_60d    | -11.9% |
| ma20_dist  |  -2.7% |
| ma50_dist  |  -5.7% |
| vol_20d    |  45.9% |
| mdd_60d    |  20.9% |
| rsi_14     |   37.4 |
| zscore_20d |   -0.8 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Gold / GC=F                         |  82.3786 |           1.8% |                 0.46x |      164.7573 |            3.5% |
| Corn / ZC=F                         |  17.0714 |           3.3% |                 0.20x |       34.1429 |            6.6% |
| Wheat / ZW=F                        |  20.4464 |           2.9% |                 0.28x |       40.8929 |            5.8% |
| Soybeans / ZS=F                     |  16.9464 |           1.4% |                 0.61x |       33.8929 |            2.8% |
| Platinum / PL=F                     |  30.6071 |           1.6% |                 0.27x |       61.2143 |            3.3% |
| FTSE 100 / ^FTSE                    |  79.5857 |           0.7% |                 1.90x |      159.1713 |            1.5% |
| Microsoft Corporation / MSFT        |   9.6942 |           2.0% |                 0.17x |       19.3885 |            4.0% |
| Silver / SI=F                       |   1.6236 |           2.4% |                 0.31x |        3.2473 |            4.8% |
| Brent Crude Oil / BZ=F              |   2.4036 |           2.6% |                 0.24x |        4.8071 |            5.2% |
| DAX / ^GDAXI                        | 203.1479 |           0.8% |                 1.25x |      406.2958 |            1.6% |
| JPMorgan Chase & Co. / JPM          |   5.4671 |           1.5% |                 0.53x |       10.9343 |            3.1% |
| Dow Jones Industrial Average / ^DJI | 405.0502 |           0.8% |                 0.70x |      810.1004 |            1.5% |
| Euro Stoxx 50 / ^STOXX50E           |  45.4457 |           0.7% |                 1.10x |       90.8914 |            1.4% |
| Natural Gas / NG=F                  |   0.0799 |           2.8% |                 0.33x |        0.1599 |            5.7% |
| S&P 500 / ^GSPC                     |  50.5336 |           0.7% |                 0.77x |      101.0672 |            1.3% |
| Tesla Inc. / TSLA                   |  11.9514 |           3.4% |                 0.26x |       23.9029 |            6.8% |
| Amazon.com Inc. / AMZN              |   6.1364 |           2.3% |                 0.16x |       12.2729 |            4.7% |
| UnitedHealth Group Inc. / UNH       |   9.5671 |           2.4% |                 0.44x |       19.1343 |            4.8% |
| Russell 2000 / ^RUT                 |  27.8343 |           0.9% |                 0.64x |       55.6687 |            1.9% |
| Apple Inc. / AAPL                   |   6.0232 |           1.9% |                 0.32x |       12.0465 |            3.9% |
| CAC 40 / ^FCHI                      |  54.9877 |           0.7% |                 1.17x |      109.9754 |            1.3% |
| Hang Seng / ^HSI                    | 343.9615 |           1.3% |                 0.65x |      687.9230 |            2.7% |
| Alphabet Inc. Class A / GOOGL       |   8.0121 |           2.3% |                 0.26x |       16.0243 |            4.6% |
| NASDAQ 100 / ^NDX                   | 353.0384 |           1.2% |                 0.45x |      706.0767 |            2.4% |
| NVIDIA Corporation / NVDA           |   5.8793 |           2.8% |                 0.29x |       11.7586 |            5.6% |
| Meta Platforms Inc. / META          |  17.0621 |           3.1% |                 0.22x |       34.1243 |            6.1% |

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

Scoring engine version: **1.0.0** | Git commit: **f940031**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
