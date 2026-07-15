+++
title = "Market Analysis 2026-07-15"
date = "2026-07-15T00:00:00+00:00"
draft = false
summary = "Neutral market: 15 reliable instruments. Top signal: ZS=F (score 81.5)."
ticker_symbols = ["6758.T", "7203.T", "8306.T", "AAPL", "AMZN", "BZ=F", "CL=F", "GC=F", "GOOGL", "HG=F", "JPM", "META", "MSFT", "NG=F", "NVDA", "PL=F", "SI=F", "TSLA", "UNH", "XOM", "ZC=F", "ZS=F", "ZW=F", "^DJI", "^FCHI", "^FTSE", "^GDAXI", "^GSPC", "^HSI", "^N225", "^NDX", "^RUT", "^STOXX50E"]
source_files = ["data/analysis/2026-07-15.json", "data/history/2026-07-15.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "5337fdb"
+++

## Market Regime

**Neutral** — 7 of 15 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Soybeans / ZS=F** — score 81.5, 20d return +8.4%, RSI14=75. 20d up +8.4%; above MA20 by 5.2%; RSI14=75
- **Wheat / ZW=F** — score 80.9, 20d return +8.0%, RSI14=68. 20d up +8.0%; above MA20 by 5.3%; RSI14=68
- **Meta Platforms Inc. / META** — score 77.6, 20d return +16.7%, RSI14=70. 20d up +16.7%; above MA20 by 11.3%; RSI14=70
- **FTSE 100 / ^FTSE** — score 70.0, 20d return +0.6%, RSI14=55. 20d up +0.6%; below MA20 by 0.1%; RSI14=55
- **CAC 40 / ^FCHI** — score 69.7, 20d return -0.2%, RSI14=52. 20d down -0.2%; below MA20 by 0.4%; RSI14=52

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                 | Applies To |
| ---------- | --------------------- | ---------- |
| 2026-07-16 | UNH earnings release  | UNH        |
| 2026-07-22 | TSLA earnings release | TSLA       |

## Signal History

Compared with the previous available report (**2026-07-14**).
- **New top-5:** META, ^FCHI, ^FTSE
- **Persistent top signals:** ZS=F (9 reports), ZW=F (5 reports)
- **Dropped from top-5:** AAPL, UNH, ^DJI
- **AAPL risk gates:** added high_volatility, malformed_input; removed none
- **AMZN risk gates:** added high_volatility, malformed_input; removed none
- **GOOGL risk gates:** added high_volatility, malformed_input; removed none
- **JPM risk gates:** added high_volatility, malformed_input; removed none
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
| 6758.T    |    +11 |   +19.7 |
| 7203.T    |    +12 |   +29.4 |
| 8306.T    |    +11 |    +2.1 |
| AAPL      |    -19 |   -63.0 |
| AMZN      |    -19 |   -49.1 |
| BZ=F      |    +10 |   +21.8 |
| CL=F      |    +12 |   +20.6 |
| GC=F      |    +12 |   +39.4 |
| GOOGL     |     -5 |   -20.0 |
| HG=F      |    +13 |   +26.7 |
| JPM       |    -26 |   -57.0 |
| META      |     +4 |   +13.9 |
| MSFT      |     -8 |   -38.2 |
| NG=F      |     +9 |   +30.6 |
| NVDA      |     -3 |   -26.4 |
| PL=F      |    +12 |   +39.4 |
| SI=F      |    +11 |   +42.7 |
| TSLA      |     -2 |   -11.5 |
| UNH       |    -26 |   -68.8 |
| XOM       |     +0 |   -48.8 |
| ZC=F      |     -1 |    +7.0 |
| ZS=F      |     +1 |    +3.9 |
| ZW=F      |     +3 |   +13.3 |
| ^DJI      |    -29 |   -63.9 |
| ^FCHI     |    +10 |   +17.9 |
| ^FTSE     |     +7 |   +15.2 |
| ^GDAXI    |     +7 |   +15.8 |
| ^GSPC     |    -23 |   -52.7 |
| ^HSI      |     +3 |   +11.8 |
| ^N225     |    +12 |   +25.5 |
| ^NDX      |    -11 |   -30.3 |
| ^RUT      |     +7 |   +18.2 |
| ^STOXX50E |     +5 |   +14.8 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars
- **Copper / HG=F** — malformed_input
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **WTI Crude Oil / CL=F** — malformed_input
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **Nikkei 225 / ^N225** — missing_bars
- **Apple Inc. / AAPL** — malformed_input, high_volatility
- **NVIDIA Corporation / NVDA** — malformed_input, high_volatility
- **Tesla Inc. / TSLA** — malformed_input, high_volatility
- **Microsoft Corporation / MSFT** — malformed_input, high_volatility
- **Alphabet Inc. Class A / GOOGL** — malformed_input, high_volatility
- **UnitedHealth Group Inc. / UNH** — malformed_input, high_volatility
- **Exxon Mobil Corporation / XOM** — malformed_input, high_volatility
- **Amazon.com Inc. / AMZN** — malformed_input, high_volatility
- **NASDAQ 100 / ^NDX** — malformed_input, high_volatility
- **S&P 500 / ^GSPC** — malformed_input, high_volatility
- **JPMorgan Chase & Co. / JPM** — malformed_input, high_volatility
- **Dow Jones Industrial Average / ^DJI** — malformed_input, high_volatility

## Key Risks

- **high_volatility** (12 instrument(s)): High volatility: one or more instruments show extreme volatility.
- **malformed_input** (17 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|    1 | Soybeans / ZS=F        |  81.5 |   Yes    | —               | 20d up +8.4%; above MA20 by 5.2%; RSI14=75    |
|    2 | Wheat / ZW=F           |  80.9 |   Yes    | —               | 20d up +8.0%; above MA20 by 5.3%; RSI14=68    |
|    8 | Brent Crude Oil / BZ=F |  69.1 |   Yes    | —               | 20d down -3.0%; above MA20 by 10.7%; RSI14=64 |
|   10 | Corn / ZC=F            |  66.1 |   Yes    | —               | 20d up +5.1%; above MA20 by 2.8%; RSI14=63    |
|   12 | Gold / GC=F            |  55.1 |   Yes    | —               | 20d down -3.7%; below MA20 by 1.6%; RSI14=45  |
|   13 | Platinum / PL=F        |  55.1 |   Yes    | —               | 20d down -4.5%; below MA20 by 0.8%; RSI14=47  |
|   14 | Natural Gas / NG=F     |  51.2 |   Yes    | —               | 20d down -6.9%; below MA20 by 8.3%; RSI14=38  |
|   15 | Silver / SI=F          |  47.0 |   Yes    | —               | 20d down -13.4%; below MA20 by 4.9%; RSI14=42 |
|   17 | Copper / HG=F          |  73.6 |    No    | malformed_input | Suppressed: malformed_input                   |
|   19 | WTI Crude Oil / CL=F   |  63.9 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                       | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | -------------------------------- | -------------------------------------------- |
|    3 | Meta Platforms Inc. / META                                                     |  77.6 |   Yes    | —                                | 20d up +16.7%; above MA20 by 11.3%; RSI14=70 |
|   16 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |  90.6 |    No    | malformed_input, missing_bars    | Suppressed: malformed_input, missing_bars    |
|   18 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  68.2 |    No    | malformed_input, missing_bars    | Suppressed: malformed_input, missing_bars    |
|   20 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  63.6 |    No    | malformed_input, missing_bars    | Suppressed: malformed_input, missing_bars    |
|   22 | Apple Inc. / AAPL                                                              |  10.6 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   23 | NVIDIA Corporation / NVDA                                                      |  10.3 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   24 | Tesla Inc. / TSLA                                                              |  10.3 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   25 | Microsoft Corporation / MSFT                                                   |  10.0 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   26 | Alphabet Inc. Class A / GOOGL                                                  |   9.4 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   27 | UnitedHealth Group Inc. / UNH                                                  |   9.1 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   28 | Exxon Mobil Corporation / XOM                                                  |   9.1 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   29 | Amazon.com Inc. / AMZN                                                         |   8.2 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   32 | JPMorgan Chase & Co. / JPM                                                     |   7.3 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates                       | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | -------------------------------- | -------------------------------------------- |
|    4 | FTSE 100 / ^FTSE                    |  70.0 |   Yes    | —                                | 20d up +0.6%; below MA20 by 0.1%; RSI14=55   |
|    5 | CAC 40 / ^FCHI                      |  69.7 |   Yes    | —                                | 20d down -0.2%; below MA20 by 0.4%; RSI14=52 |
|    6 | DAX / ^GDAXI                        |  69.7 |   Yes    | —                                | 20d up +0.9%; above MA20 by 0.1%; RSI14=53   |
|    7 | Euro Stoxx 50 / ^STOXX50E           |  69.7 |   Yes    | —                                | 20d up +0.7%; below MA20 by 0.3%; RSI14=53   |
|    9 | Russell 2000 / ^RUT                 |  66.7 |   Yes    | —                                | 20d up +1.1%; below MA20 by 1.0%; RSI14=40   |
|   11 | Hang Seng / ^HSI                    |  64.5 |   Yes    | —                                | 20d down -2.7%; above MA20 by 1.5%; RSI14=60 |
|   21 | Nikkei 225 / ^N225                  |  58.8 |    No    | missing_bars                     | Suppressed: missing_bars                     |
|   30 | NASDAQ 100 / ^NDX                   |   8.2 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   31 | S&P 500 / ^GSPC                     |   7.9 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |
|   33 | Dow Jones Industrial Average / ^DJI |   7.0 |    No    | malformed_input, high_volatility | Suppressed: malformed_input, high_volatility |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-07-14 |
| 7203.T    | 2026-07-14 |
| 8306.T    | 2026-07-14 |
| AAPL      | 2026-07-14 |
| AMZN      | 2026-07-14 |
| BZ=F      | 2026-07-14 |
| CL=F      | 2026-07-14 |
| GC=F      | 2026-07-14 |
| GOOGL     | 2026-07-14 |
| HG=F      | 2026-07-14 |
| JPM       | 2026-07-14 |
| META      | 2026-07-14 |
| MSFT      | 2026-07-14 |
| NG=F      | 2026-07-14 |
| NVDA      | 2026-07-14 |
| PL=F      | 2026-07-14 |
| SI=F      | 2026-07-14 |
| TSLA      | 2026-07-14 |
| UNH       | 2026-07-14 |
| XOM       | 2026-07-14 |
| ZC=F      | 2026-07-14 |
| ZS=F      | 2026-07-14 |
| ZW=F      | 2026-07-14 |
| ^DJI      | 2026-07-14 |
| ^FCHI     | 2026-07-13 |
| ^FTSE     | 2026-07-13 |
| ^GDAXI    | 2026-07-13 |
| ^GSPC     | 2026-07-14 |
| ^HSI      | 2026-07-14 |
| ^N225     | 2026-07-14 |
| ^NDX      | 2026-07-14 |
| ^RUT      | 2026-07-13 |
| ^STOXX50E | 2026-07-13 |

## Symbol Details

### Soybeans / ZS=F (score 81.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.4% |
| ret_5d     | +0.9% |
| ret_20d    | +8.4% |
| ret_60d    | +3.7% |
| ma20_dist  | +5.2% |
| ma50_dist  | +3.8% |
| vol_20d    | 20.0% |
| mdd_60d    |  8.8% |
| rsi_14     |  75.3 |
| zscore_20d |   1.7 |

### Wheat / ZW=F (score 80.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.7% |
| ret_5d     | +3.6% |
| ret_20d    | +8.0% |
| ret_60d    | +5.5% |
| ma20_dist  | +5.3% |
| ma50_dist  | +3.2% |
| vol_20d    | 26.3% |
| mdd_60d    | 14.6% |
| rsi_14     |  68.2 |
| zscore_20d |   1.9 |

### Meta Platforms Inc. / META (score 77.6)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.7% |
| ret_5d     |  +7.4% |
| ret_20d    | +16.7% |
| ret_60d    |  -2.2% |
| ma20_dist  | +11.3% |
| ma50_dist  | +10.0% |
| vol_20d    |  55.6% |
| mdd_60d    |  21.1% |
| rsi_14     |   70.0 |
| zscore_20d |    1.8 |

### FTSE 100 / ^FTSE (score 70.0)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.0% |
| ret_5d     | -1.4% |
| ret_20d    | +0.6% |
| ret_60d    | -0.9% |
| ma20_dist  | -0.1% |
| ma50_dist  | +0.8% |
| vol_20d    | 10.4% |
| mdd_60d    |  4.4% |
| rsi_14     |  55.4 |
| zscore_20d |  -0.1 |

### CAC 40 / ^FCHI (score 69.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | -1.4% |
| ret_20d    | -0.2% |
| ret_60d    | -0.7% |
| ma20_dist  | -0.4% |
| ma50_dist  | +1.4% |
| vol_20d    | 12.5% |
| mdd_60d    |  4.5% |
| rsi_14     |  51.5 |
| zscore_20d |  -0.6 |

### DAX / ^GDAXI (score 69.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.2% |
| ret_5d     | -2.7% |
| ret_20d    | +0.9% |
| ret_60d    | +1.7% |
| ma20_dist  | +0.1% |
| ma50_dist  | +1.1% |
| vol_20d    | 15.8% |
| mdd_60d    |  4.7% |
| rsi_14     |  53.4 |
| zscore_20d |   0.1 |

### Euro Stoxx 50 / ^STOXX50E (score 69.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.0% |
| ret_5d     | -2.0% |
| ret_20d    | +0.7% |
| ret_60d    | +5.6% |
| ma20_dist  | -0.3% |
| ma50_dist  | +2.7% |
| vol_20d    | 14.1% |
| mdd_60d    |  4.9% |
| rsi_14     |  52.9 |
| zscore_20d |  -0.3 |

### Brent Crude Oil / BZ=F (score 69.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.7% |
| ret_5d     | +14.3% |
| ret_20d    |  -3.0% |
| ret_60d    | -14.7% |
| ma20_dist  | +10.7% |
| ma50_dist  |  -6.8% |
| vol_20d    |  55.0% |
| mdd_60d    |  39.4% |
| rsi_14     |   63.6 |
| zscore_20d |    2.1 |

### Russell 2000 / ^RUT (score 66.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.8% |
| ret_5d     | -1.9% |
| ret_20d    | +1.1% |
| ret_60d    | +8.8% |
| ma20_dist  | -1.0% |
| ma50_dist  | +1.5% |
| vol_20d    | 13.3% |
| mdd_60d    |  4.8% |
| rsi_14     |  39.7 |
| zscore_20d |  -1.0 |

### Corn / ZC=F (score 66.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.9% |
| ret_5d     | -2.0% |
| ret_20d    | +5.1% |
| ret_60d    | -3.3% |
| ma20_dist  | +2.8% |
| ma50_dist  | -1.0% |
| vol_20d    | 26.2% |
| mdd_60d    | 15.7% |
| rsi_14     |  62.9 |
| zscore_20d |   1.0 |

### Hang Seng / ^HSI (score 64.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.7% |
| ret_5d     | +2.3% |
| ret_20d    | -2.7% |
| ret_60d    | -7.3% |
| ma20_dist  | +1.5% |
| ma50_dist  | -3.2% |
| vol_20d    | 19.7% |
| mdd_60d    | 14.9% |
| rsi_14     |  60.4 |
| zscore_20d |   0.6 |

### Gold / GC=F (score 55.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.6% |
| ret_5d     |  -2.0% |
| ret_20d    |  -3.7% |
| ret_60d    | -15.1% |
| ma20_dist  |  -1.6% |
| ma50_dist  |  -6.7% |
| vol_20d    |  26.0% |
| mdd_60d    |  17.9% |
| rsi_14     |   45.5 |
| zscore_20d |   -0.6 |

### Platinum / PL=F (score 55.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.8% |
| ret_5d     |  -1.2% |
| ret_20d    |  -4.5% |
| ret_60d    | -22.1% |
| ma20_dist  |  -0.8% |
| ma50_dist  | -10.1% |
| vol_20d    |  40.9% |
| mdd_60d    |  29.1% |
| rsi_14     |   46.9 |
| zscore_20d |   -0.2 |

### Natural Gas / NG=F (score 51.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.2% |
| ret_5d     | -11.1% |
| ret_20d    |  -6.9% |
| ret_60d    |  +9.7% |
| ma20_dist  |  -8.3% |
| ma50_dist  |  -5.6% |
| vol_20d    |  40.8% |
| mdd_60d    |  13.3% |
| rsi_14     |   37.5 |
| zscore_20d |   -2.1 |

### Silver / SI=F (score 47.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +2.0% |
| ret_5d     |  -3.5% |
| ret_20d    | -13.4% |
| ret_60d    | -25.2% |
| ma20_dist  |  -4.9% |
| ma50_dist  | -15.9% |
| vol_20d    |  48.4% |
| mdd_60d    |  35.2% |
| rsi_14     |   41.8 |
| zscore_20d |   -0.7 |

## Risk Context

| Instrument                 |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| -------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Soybeans / ZS=F            |  19.3929 |           1.6% |                 0.50x |       38.7857 |            3.2% |
| Wheat / ZW=F               |  13.9821 |           2.2% |                 0.38x |       27.9643 |            4.4% |
| Meta Platforms Inc. / META |  27.6436 |           4.2% |                 0.18x |       55.2871 |            8.4% |
| FTSE 100 / ^FTSE           | 116.4428 |           1.1% |                 0.97x |      232.8856 |            2.2% |
| CAC 40 / ^FCHI             |  90.6993 |           1.1% |                 0.80x |      181.3986 |            2.2% |
| DAX / ^GDAXI               | 336.6177 |           1.3% |                 0.63x |      673.2355 |            2.7% |
| Euro Stoxx 50 / ^STOXX50E  |  73.6470 |           1.2% |                 0.71x |      147.2940 |            2.3% |
| Brent Crude Oil / BZ=F     |   3.5429 |           4.2% |                 0.18x |        7.0857 |            8.4% |
| Russell 2000 / ^RUT        |  42.5522 |           1.4% |                 0.75x |       85.1044 |            2.9% |
| Corn / ZC=F                |  10.0893 |           2.3% |                 0.38x |       20.1786 |            4.7% |
| Hang Seng / ^HSI           | 459.8650 |           1.9% |                 0.51x |      919.7299 |            3.8% |
| Gold / GC=F                |  86.0714 |           2.1% |                 0.38x |      172.1429 |            4.2% |
| Platinum / PL=F            |  40.7072 |           2.5% |                 0.24x |       81.4143 |            5.0% |
| Natural Gas / NG=F         |   0.1389 |           4.8% |                 0.25x |        0.2777 |            9.6% |
| Silver / SI=F              |   2.1775 |           3.7% |                 0.21x |        4.3550 |            7.4% |

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

Scoring engine version: **1.0.0** | Git commit: **5337fdb**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
