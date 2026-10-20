+++
title = "Market Analysis 2026-07-26"
date = "2026-07-26T00:00:00+00:00"
draft = false
summary = "Neutral market: 14 reliable instruments. Top signal: ZS=F (score 84.2)."
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
source_files = ["data/analysis/2026-07-26.json", "data/history/2026-07-26.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "47b73d3"
+++

## Market Regime

**Neutral** — 8 of 14 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Soybeans / ZS=F** — score 84.2, 20d return +11.2%, RSI14=75. 20d up +11.2%; above MA20 by 5.6%; RSI14=75 ⚠️ Upcoming: FOMC rate decision (2026-07-29)
- **Corn / ZC=F** — score 83.9, 20d return +17.5%, RSI14=74. 20d up +17.5%; above MA20 by 11.0%; RSI14=74 ⚠️ Upcoming: FOMC rate decision (2026-07-29)
- **FTSE 100 / ^FTSE** — score 80.3, 20d return +2.2%, RSI14=55. 20d up +2.2%; above MA20 by 1.5%; RSI14=55 ⚠️ Upcoming: FOMC rate decision (2026-07-29)
- **Brent Crude Oil / BZ=F** — score 73.6, 20d return +28.6%, RSI14=83. 20d up +28.6%; above MA20 by 18.4%; RSI14=83 ⚠️ Upcoming: FOMC rate decision (2026-07-29)
- **Hang Seng / ^HSI** — score 72.4, 20d return +8.2%, RSI14=68. 20d up +8.2%; above MA20 by 3.4%; RSI14=68 ⚠️ Upcoming: FOMC rate decision (2026-07-29)

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                        | Applies To                      |
| ---------- | ---------------------------- | ------------------------------- |
| 2026-07-29 | FOMC rate decision           | Commodity, Equity, Equity Index |
| 2026-07-29 | META earnings release        | META                            |
| 2026-07-29 | MSFT earnings release        | MSFT                            |
| 2026-07-30 | AAPL earnings release        | AAPL                            |
| 2026-07-30 | AMZN earnings release        | AMZN                            |
| 2026-07-31 | 6758.T earnings release      | 6758.T                          |
| 2026-07-31 | BOJ monetary policy decision | 6758.T, 7203.T, 8306.T, ^N225   |
| 2026-07-31 | XOM earnings release         | XOM                             |

## Signal History

Compared with the previous available report (**2026-07-25**).

- **New top-5:** BZ=F, ^HSI
- **Persistent top signals:** ZS=F (10 reports), ZC=F (4 reports), ^FTSE (2 reports)
- **Dropped from top-5:** AAPL, JPM
- **AAPL risk gates:** added high_volatility, malformed_input; removed none
- **AMZN risk gates:** added high_volatility, malformed_input; removed none
- **GOOGL risk gates:** added high_volatility, malformed_input; removed none
- **JPM risk gates:** added high_volatility, malformed_input; removed none
- **META risk gates:** added high_volatility, malformed_input; removed none
- **MSFT risk gates:** added high_volatility, malformed_input; removed none
- **NVDA risk gates:** added high_volatility, malformed_input; removed none
- **TSLA risk gates:** added high_volatility, malformed_input; removed none
- **UNH risk gates:** added high_volatility, malformed_input; removed none
- **XOM risk gates:** added high_volatility; removed none
- **^DJI risk gates:** added high_volatility, malformed_input; removed none
- **^GSPC risk gates:** added high_volatility, malformed_input; removed none
- **^NDX risk gates:** added high_volatility, malformed_input; removed none

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |    +13 |   +14.2 |
| 7203.T    |    +13 |   +15.4 |
| 8306.T    |    +12 |    +4.5 |
| AAPL      |    -24 |   -64.5 |
| AMZN      |     -5 |   -16.1 |
| BZ=F      |     +4 |   +15.8 |
| CL=F      |    +13 |   +15.4 |
| GC=F      |     +6 |   +17.3 |
| GOOGL     |     +1 |    -6.1 |
| HG=F      |    +13 |   +14.2 |
| JPM       |    -24 |   -69.1 |
| META      |     -1 |   -15.4 |
| MSFT      |     -9 |   -23.6 |
| NG=F      |    +10 |   +28.2 |
| NVDA      |     -9 |   -36.4 |
| PL=F      |     +8 |   +27.6 |
| SI=F      |     +6 |   +23.9 |
| TSLA      |     -5 |    +5.5 |
| UNH       |    -13 |   -40.0 |
| XOM       |     +7 |   -62.1 |
| ZC=F      |     +3 |   +18.2 |
| ZS=F      |     +1 |    +7.3 |
| ZW=F      |     +2 |   +12.1 |
| ^DJI      |    -20 |   -43.9 |
| ^FCHI     |     +2 |   +11.5 |
| ^FTSE     |     +1 |    +8.5 |
| ^GDAXI    |     +2 |   +11.8 |
| ^GSPC     |    -18 |   -39.1 |
| ^HSI      |     +2 |   +13.0 |
| ^N225     |    +13 |   +26.4 |
| ^NDX      |    -10 |   -20.3 |
| ^RUT      |     +6 |   +17.9 |
| ^STOXX50E |     +0 |    +9.7 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **WTI Crude Oil / CL=F** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Nikkei 225 / ^N225** — missing_bars
- **Exxon Mobil Corporation / XOM** — malformed_input, high_volatility
- **Meta Platforms Inc. / META** — malformed_input, high_volatility
- **NVIDIA Corporation / NVDA** — malformed_input, high_volatility
- **Alphabet Inc. Class A / GOOGL** — malformed_input, high_volatility
- **JPMorgan Chase & Co. / JPM** — malformed_input, high_volatility
- **UnitedHealth Group Inc. / UNH** — malformed_input, high_volatility
- **Apple Inc. / AAPL** — malformed_input, high_volatility
- **Microsoft Corporation / MSFT** — malformed_input, high_volatility
- **Amazon.com Inc. / AMZN** — malformed_input, high_volatility
- **NASDAQ 100 / ^NDX** — malformed_input, high_volatility
- **Tesla Inc. / TSLA** — malformed_input, high_volatility
- **Dow Jones Industrial Average / ^DJI** — malformed_input, high_volatility
- **S&P 500 / ^GSPC** — malformed_input, high_volatility

## Key Risks

- **high_volatility** (13 instrument(s)): High volatility: one or more instruments show extreme volatility.
- **malformed_input** (18 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|    1 | Soybeans / ZS=F        |  84.2 |   Yes    | —               | 20d up +11.2%; above MA20 by 5.6%; RSI14=75   |
|    2 | Corn / ZC=F            |  83.9 |   Yes    | —               | 20d up +17.5%; above MA20 by 11.0%; RSI14=74  |
|    4 | Brent Crude Oil / BZ=F |  73.6 |   Yes    | —               | 20d up +28.6%; above MA20 by 18.4%; RSI14=83  |
|    7 | Wheat / ZW=F           |  69.7 |   Yes    | —               | 20d up +14.7%; above MA20 by 6.8%; RSI14=70   |
|   10 | Gold / GC=F            |  62.4 |   Yes    | —               | 20d up +1.0%; above MA20 by 0.1%; RSI14=44    |
|   12 | Silver / SI=F          |  59.4 |   Yes    | —               | 20d up +1.0%; above MA20 by 0.1%; RSI14=43    |
|   13 | Natural Gas / NG=F     |  53.6 |   Yes    | —               | 20d down -13.6%; below MA20 by 4.9%; RSI14=24 |
|   14 | Platinum / PL=F        |  53.6 |   Yes    | —               | 20d up +0.1%; below MA20 by 0.5%; RSI14=46    |
|   16 | Copper / HG=F          |  75.2 |    No    | malformed_input | Suppressed: malformed_input                   |
|   17 | WTI Crude Oil / CL=F   |  73.3 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                       | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | -------------------------------- | -------------------------------------------- |
|   15 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  83.9 |    No    | malformed_input, missing_bars    | Suppressed: malformed_input, missing_bars    |
|   18 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  66.1 |    No    | malformed_input, missing_bars    | Suppressed: malformed_input, missing_bars    |
|   19 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  63.9 |    No    | malformed_input, missing_bars    | Suppressed: malformed_input, missing_bars    |
|   21 | Exxon Mobil Corporation / XOM                                                  |  11.5 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   22 | Meta Platforms Inc. / META                                                     |  10.9 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   23 | NVIDIA Corporation / NVDA                                                      |  10.9 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   24 | Alphabet Inc. Class A / GOOGL                                                  |  10.6 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   25 | JPMorgan Chase & Co. / JPM                                                     |  10.0 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   26 | UnitedHealth Group Inc. / UNH                                                  |  10.0 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   27 | Apple Inc. / AAPL                                                              |   9.7 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   28 | Microsoft Corporation / MSFT                                                   |   9.7 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   29 | Amazon.com Inc. / AMZN                                                         |   9.1 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   31 | Tesla Inc. / TSLA                                                              |   8.8 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates                       | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | -------------------------------- | -------------------------------------------- |
|    3 | FTSE 100 / ^FTSE                    |  80.3 |   Yes    | —                                | 20d up +2.2%; above MA20 by 1.5%; RSI14=55   |
|    5 | Hang Seng / ^HSI                    |  72.4 |   Yes    | —                                | 20d up +8.2%; above MA20 by 3.4%; RSI14=68   |
|    6 | Euro Stoxx 50 / ^STOXX50E           |  70.9 |   Yes    | —                                | 20d up +1.0%; below MA20 by 0.1%; RSI14=41   |
|    8 | DAX / ^GDAXI                        |  68.8 |   Yes    | —                                | 20d up +1.7%; below MA20 by 0.1%; RSI14=36   |
|    9 | CAC 40 / ^FCHI                      |  66.7 |   Yes    | —                                | 20d down -0.2%; below MA20 by 0.1%; RSI14=42 |
|   11 | Russell 2000 / ^RUT                 |  60.9 |   Yes    | —                                | 20d down -2.6%; below MA20 by 1.6%; RSI14=36 |
|   20 | Nikkei 225 / ^N225                  |  52.7 |    No    | missing_bars                     | Suppressed: missing_bars                     |
|   30 | NASDAQ 100 / ^NDX                   |   9.1 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   32 | Dow Jones Industrial Average / ^DJI |   7.9 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   33 | S&P 500 / ^GSPC                     |   7.9 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-07-24 |
| 7203.T    | 2026-07-24 |
| 8306.T    | 2026-07-24 |
| AAPL      | 2026-07-24 |
| AMZN      | 2026-07-24 |
| BZ=F      | 2026-07-24 |
| CL=F      | 2026-07-24 |
| GC=F      | 2026-07-24 |
| GOOGL     | 2026-07-24 |
| HG=F      | 2026-07-24 |
| JPM       | 2026-07-24 |
| META      | 2026-07-24 |
| MSFT      | 2026-07-24 |
| NG=F      | 2026-07-24 |
| NVDA      | 2026-07-24 |
| PL=F      | 2026-07-24 |
| SI=F      | 2026-07-24 |
| TSLA      | 2026-07-24 |
| UNH       | 2026-07-24 |
| XOM       | 2026-07-24 |
| ZC=F      | 2026-07-24 |
| ZS=F      | 2026-07-24 |
| ZW=F      | 2026-07-24 |
| ^DJI      | 2026-07-24 |
| ^FCHI     | 2026-07-24 |
| ^FTSE     | 2026-07-24 |
| ^GDAXI    | 2026-07-24 |
| ^GSPC     | 2026-07-24 |
| ^HSI      | 2026-07-24 |
| ^N225     | 2026-07-24 |
| ^NDX      | 2026-07-24 |
| ^RUT      | 2026-07-24 |
| ^STOXX50E | 2026-07-24 |

## Symbol Details

### Soybeans / ZS=F (score 84.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.3% |
| ret_5d     |  +4.1% |
| ret_20d    | +11.2% |
| ret_60d    |  +6.9% |
| ma20_dist  |  +5.6% |
| ma50_dist  |  +7.4% |
| vol_20d    |  19.8% |
| mdd_60d    |   8.8% |
| rsi_14     |   75.0 |
| zscore_20d |    1.6 |

### Corn / ZC=F (score 83.9)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +5.0% |
| ret_5d     |  +9.6% |
| ret_20d    | +17.5% |
| ret_60d    |  +4.7% |
| ma20_dist  | +11.0% |
| ma50_dist  | +11.5% |
| vol_20d    |  30.7% |
| mdd_60d    |  15.7% |
| rsi_14     |   74.1 |
| zscore_20d |    2.5 |

### FTSE 100 / ^FTSE (score 80.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | +1.3% |
| ret_20d    | +2.2% |
| ret_60d    | +5.1% |
| ma20_dist  | +1.5% |
| ma50_dist  | +2.5% |
| vol_20d    | 11.1% |
| mdd_60d    |  2.6% |
| rsi_14     |  55.2 |
| zscore_20d |   1.9 |

### Brent Crude Oil / BZ=F (score 73.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -3.9% |
| ret_5d     |  +9.9% |
| ret_20d    | +28.6% |
| ret_60d    | -13.0% |
| ma20_dist  | +18.4% |
| ma50_dist  |  +9.3% |
| vol_20d    |  53.8% |
| mdd_60d    |  39.4% |
| rsi_14     |   82.6 |
| zscore_20d |    1.7 |

### Hang Seng / ^HSI (score 72.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | +1.6% |
| ret_20d    | +8.2% |
| ret_60d    | -3.7% |
| ma20_dist  | +3.4% |
| ma50_dist  | +1.3% |
| vol_20d    | 20.3% |
| mdd_60d    | 14.9% |
| rsi_14     |  67.7 |
| zscore_20d |   1.0 |

### Euro Stoxx 50 / ^STOXX50E (score 70.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.1% |
| ret_5d     | +0.8% |
| ret_20d    | +1.0% |
| ret_60d    | +7.6% |
| ma20_dist  | -0.1% |
| ma50_dist  | +1.7% |
| vol_20d    | 15.0% |
| mdd_60d    |  3.6% |
| rsi_14     |  41.0 |
| zscore_20d |  -0.1 |

### Wheat / ZW=F (score 69.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -2.6% |
| ret_5d     |  -0.7% |
| ret_20d    | +14.7% |
| ret_60d    |  +4.5% |
| ma20_dist  |  +6.8% |
| ma50_dist  |  +9.1% |
| vol_20d    |  37.8% |
| mdd_60d    |  14.6% |
| rsi_14     |   70.0 |
| zscore_20d |    1.0 |

### DAX / ^GDAXI (score 68.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.4% |
| ret_5d     | +1.1% |
| ret_20d    | +1.7% |
| ret_60d    | +3.3% |
| ma20_dist  | -0.1% |
| ma50_dist  | +0.6% |
| vol_20d    | 16.2% |
| mdd_60d    |  4.7% |
| rsi_14     |  36.4 |
| zscore_20d |  -0.0 |

### CAC 40 / ^FCHI (score 66.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.9% |
| ret_5d     | +0.4% |
| ret_20d    | -0.2% |
| ret_60d    | +3.2% |
| ma20_dist  | -0.1% |
| ma50_dist  | +0.9% |
| vol_20d    | 13.5% |
| mdd_60d    |  4.2% |
| rsi_14     |  42.4 |
| zscore_20d |  -0.1 |

### Gold / GC=F (score 62.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.6% |
| ret_5d     |  +1.4% |
| ret_20d    |  +1.0% |
| ret_60d    | -11.3% |
| ma20_dist  |  +0.1% |
| ma50_dist  |  -4.3% |
| vol_20d    |  21.5% |
| mdd_60d    |  15.6% |
| rsi_14     |   44.0 |
| zscore_20d |    0.1 |

### Russell 2000 / ^RUT (score 60.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | -1.1% |
| ret_20d    | -2.6% |
| ret_60d    | +6.3% |
| ma20_dist  | -1.6% |
| ma50_dist  | -0.0% |
| vol_20d    | 10.8% |
| mdd_60d    |  4.8% |
| rsi_14     |  36.2 |
| zscore_20d |  -1.8 |

### Silver / SI=F (score 59.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.9% |
| ret_5d     |  +5.1% |
| ret_20d    |  +1.0% |
| ret_60d    | -19.5% |
| ma20_dist  |  +0.1% |
| ma50_dist  | -11.5% |
| vol_20d    |  39.0% |
| mdd_60d    |  37.1% |
| rsi_14     |   42.5 |
| zscore_20d |    0.0 |

### Natural Gas / NG=F (score 53.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.0% |
| ret_5d     |  -0.8% |
| ret_20d    | -13.6% |
| ret_60d    | +12.9% |
| ma20_dist  |  -4.9% |
| ma50_dist  |  -6.6% |
| vol_20d    |  32.8% |
| mdd_60d    |  14.5% |
| rsi_14     |   24.0 |
| zscore_20d |   -0.9 |

### Platinum / PL=F (score 53.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.3% |
| ret_5d     |  -0.1% |
| ret_20d    |  +0.1% |
| ret_60d    | -17.4% |
| ma20_dist  |  -0.5% |
| ma50_dist  |  -8.3% |
| vol_20d    |  31.4% |
| mdd_60d    |  29.1% |
| rsi_14     |   45.8 |
| zscore_20d |   -0.3 |

## Risk Context

| Instrument                |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Soybeans / ZS=F           |  17.1964 |           1.4% |                 0.50x |       34.3929 |            2.7% |
| Corn / ZC=F               |  10.8036 |           2.2% |                 0.33x |       21.6071 |            4.4% |
| FTSE 100 / ^FTSE          | 117.3287 |           1.1% |                 0.90x |      234.6574 |            2.2% |
| Brent Crude Oil / BZ=F    |   4.7979 |           5.0% |                 0.19x |        9.5957 |            9.9% |
| Hang Seng / ^HSI          | 486.7363 |           1.9% |                 0.49x |      973.4727 |            3.9% |
| Euro Stoxx 50 / ^STOXX50E |  74.6049 |           1.2% |                 0.67x |      149.2099 |            2.4% |
| Wheat / ZW=F              |  22.1071 |           3.3% |                 0.26x |       44.2143 |            6.5% |
| DAX / ^GDAXI              | 316.4256 |           1.3% |                 0.62x |      632.8513 |            2.5% |
| CAC 40 / ^FCHI            | 101.2415 |           1.2% |                 0.74x |      202.4830 |            2.4% |
| Gold / GC=F               |  70.4857 |           1.7% |                 0.46x |      140.9714 |            3.5% |
| Russell 2000 / ^RUT       |  36.5914 |           1.2% |                 0.93x |       73.1828 |            2.5% |
| Silver / SI=F             |   1.8465 |           3.1% |                 0.26x |        3.6930 |            6.3% |
| Natural Gas / NG=F        |   0.1143 |           4.0% |                 0.31x |        0.2286 |            7.9% |
| Platinum / PL=F           |  28.8643 |           1.8% |                 0.32x |       57.7286 |            3.6% |

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

Scoring engine version: **1.0.0** | Git commit: **47b73d3**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
