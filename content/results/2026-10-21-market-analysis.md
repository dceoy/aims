+++
title = "Market Analysis 2026-10-21"
date = "2026-10-21T00:00:00+00:00"
draft = false
summary = "Neutral market: 25 reliable instruments. Top signal: ^DJI (score 78.2)."
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
source_files = ["data/analysis/2026-10-21.json", "data/history/2026-10-21.json"]
market_regime = "Neutral"
data_source = "yfinance"
scoring_version = "1.0.0"
git_commit = "b86e327"
+++

## Market Regime

**Neutral** — 10 of 25 reliable instrument(s) with MA20 data trade above their 20-day moving average (33 instruments in universe).

## Top Opportunities

- **Dow Jones Industrial Average / ^DJI** — score 78.2, 20d return +1.2%, RSI14=75. 20d up +1.2%; above MA20 by 1.8%; RSI14=75 ⚠️ Upcoming: FOMC rate decision (2026-10-28)
- **UnitedHealth Group Inc. / UNH** — score 75.8, 20d return +12.4%, RSI14=81. 20d up +12.4%; above MA20 by 9.7%; RSI14=81 ⚠️ Upcoming: FOMC rate decision (2026-10-28)
- **Brent Crude Oil / BZ=F** — score 71.2, 20d return +9.6%, RSI14=66. 20d up +9.6%; above MA20 by 4.0%; RSI14=66 ⚠️ Upcoming: FOMC rate decision (2026-10-28)
- **Microsoft Corporation / MSFT** — score 69.4, 20d return +6.8%, RSI14=62. 20d up +6.8%; above MA20 by 1.6%; RSI14=62 ⚠️ Upcoming: FOMC rate decision (2026-10-28); MSFT earnings release (2026-10-28)
- **FTSE 100 / ^FTSE** — score 66.4, 20d return +0.2%, RSI14=56. 20d up +0.2%; above MA20 by 0.9%; RSI14=56 ⚠️ Upcoming: FOMC rate decision (2026-10-28)

## Upcoming Events

Scheduled events within the next 7 days for covered instruments (from `data/calendars/`).

| Date       | Event                  | Applies To                      |
| ---------- | ---------------------- | ------------------------------- |
| 2026-10-28 | FOMC rate decision     | Commodity, Equity, Equity Index |
| 2026-10-28 | GOOGL earnings release | GOOGL                           |
| 2026-10-28 | MSFT earnings release  | MSFT                            |

## Signal History

Compared with the previous available report (**2026-10-20**).

- **New top-5:** ^DJI, ^FTSE
- **Persistent top signals:** MSFT (18 reports), BZ=F (3 reports), UNH (2 reports)
- **Dropped from top-5:** AAPL, AMZN

| Symbol    | Rank Δ | Score Δ |
| --------- | -----: | ------: |
| 6758.T    |     +1 |    +1.2 |
| 7203.T    |     +1 |    +1.2 |
| 8306.T    |     -1 |   -27.6 |
| AAPL      |     -6 |    -9.4 |
| AMZN      |     -4 |    -2.1 |
| BZ=F      |     -1 |    +0.0 |
| CL=F      |     -2 |   -11.8 |
| GC=F      |     -1 |    -0.9 |
| GOOGL     |     -6 |   -14.2 |
| HG=F      |     +0 |    +4.8 |
| JPM       |     +6 |   +18.2 |
| META      |     -3 |    -5.2 |
| MSFT      |     -3 |    -4.2 |
| NG=F      |     +0 |   -10.9 |
| NVDA      |     +1 |    -1.2 |
| PL=F      |     +1 |    +4.8 |
| SI=F      |     +2 |   +13.6 |
| TSLA      |     +3 |    +7.3 |
| UNH       |     +2 |    +8.8 |
| XOM       |     +0 |    +0.9 |
| ZC=F      |     +0 |    +0.9 |
| ZS=F      |     +2 |    +3.0 |
| ZW=F      |     -2 |    -4.5 |
| ^DJI      |     +5 |   +13.3 |
| ^FCHI     |     +1 |    +2.4 |
| ^FTSE     |     +2 |    +1.8 |
| ^GDAXI    |     +0 |    +5.2 |
| ^GSPC     |     +0 |    +3.3 |
| ^HSI      |     -8 |   -14.8 |
| ^N225     |     +1 |    -3.6 |
| ^NDX      |     +0 |    -0.3 |
| ^RUT      |     +9 |   +17.3 |
| ^STOXX50E |     +0 |    +2.4 |

## Instruments to Avoid

These instruments have quality or risk issues and are excluded from ranking:

- **Exxon Mobil Corporation / XOM** — malformed_input
- **Sony Group Corporation / 6758.T** — malformed_input, missing_bars
- **Toyota Motor Corporation / 7203.T** — malformed_input, missing_bars
- **WTI Crude Oil / CL=F** — malformed_input
- **Copper / HG=F** — malformed_input
- **Natural Gas / NG=F** — malformed_input
- **Nikkei 225 / ^N225** — missing_bars
- **Mitsubishi UFJ Financial Group Inc. / 8306.T** — malformed_input, missing_bars

## Key Risks

- **malformed_input** (7 instrument(s)): Malformed input: price data quality issues detected.
- **missing_bars** (4 instrument(s)): Missing bars: data gaps detected in price history.

## Instrument Scores

### Commodity

| Rank | Instrument             | Score | Reliable | Risk Gates      | Explanation                                   |
| ---: | ---------------------- | ----: | :------: | --------------- | --------------------------------------------- |
|    3 | Brent Crude Oil / BZ=F |  71.2 |   Yes    | —               | 20d up +9.6%; above MA20 by 4.0%; RSI14=66    |
|   16 | Soybeans / ZS=F        |  39.7 |   Yes    | —               | 20d down -5.8%; below MA20 by 3.0%; RSI14=28  |
|   18 | Gold / GC=F            |  36.7 |   Yes    | —               | 20d down -5.3%; below MA20 by 1.2%; RSI14=45  |
|   21 | Platinum / PL=F        |  31.8 |   Yes    | —               | 20d down -9.7%; below MA20 by 1.9%; RSI14=41  |
|   23 | Silver / SI=F          |  26.1 |   Yes    | —               | 20d down -12.5%; below MA20 by 3.8%; RSI14=41 |
|   24 | Corn / ZC=F            |  16.4 |   Yes    | —               | 20d down -13.9%; below MA20 by 7.1%; RSI14=22 |
|   25 | Wheat / ZW=F           |  13.0 |   Yes    | —               | 20d down -10.3%; below MA20 by 5.6%; RSI14=34 |
|   29 | WTI Crude Oil / CL=F   |  65.5 |    No    | malformed_input | Suppressed: malformed_input                   |
|   30 | Copper / HG=F          |  55.5 |    No    | malformed_input | Suppressed: malformed_input                   |
|   31 | Natural Gas / NG=F     |  33.3 |    No    | malformed_input | Suppressed: malformed_input                   |

### Equity

| Rank | Instrument                                                                     | Score | Reliable | Risk Gates                    | Explanation                                  |
| ---: | ------------------------------------------------------------------------------ | ----: | :------: | ----------------------------- | -------------------------------------------- |
|    2 | UnitedHealth Group Inc. / UNH                                                  |  75.8 |   Yes    | —                             | 20d up +12.4%; above MA20 by 9.7%; RSI14=81  |
|    4 | Microsoft Corporation / MSFT                                                   |  69.4 |   Yes    | —                             | 20d up +6.8%; above MA20 by 1.6%; RSI14=62   |
|    6 | Tesla Inc. / TSLA                                                              |  65.2 |   Yes    | —                             | 20d down -1.4%; above MA20 by 1.1%; RSI14=61 |
|    7 | Amazon.com Inc. / AMZN                                                         |  64.8 |   Yes    | —                             | 20d up +3.0%; above MA20 by 3.5%; RSI14=63   |
|    9 | JPMorgan Chase & Co. / JPM                                                     |  57.6 |   Yes    | —                             | 20d down -0.9%; above MA20 by 0.5%; RSI14=60 |
|   11 | Apple Inc. / AAPL                                                              |  56.4 |   Yes    | —                             | 20d down -0.1%; above MA20 by 0.6%; RSI14=60 |
|   17 | Alphabet Inc. Class A / GOOGL                                                  |  37.6 |   Yes    | —                             | 20d down -3.1%; below MA20 by 1.5%; RSI14=46 |
|   19 | NVIDIA Corporation / NVDA                                                      |  32.7 |   Yes    | —                             | 20d down -5.4%; below MA20 by 4.7%; RSI14=36 |
|   22 | Meta Platforms Inc. / META                                                     |  29.7 |   Yes    | —                             | 20d down -5.7%; below MA20 by 5.1%; RSI14=40 |
|   26 | Exxon Mobil Corporation / XOM                                                  |  81.2 |    No    | malformed_input               | Suppressed: malformed_input                  |
|   27 | Sony Group Corporation / 6758.T _(informational — no broker CFD)_              |  75.5 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   28 | Toyota Motor Corporation / 7203.T _(informational — no broker CFD)_            |  72.1 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |
|   33 | Mitsubishi UFJ Financial Group Inc. / 8306.T _(informational — no broker CFD)_ |   9.7 |    No    | malformed_input, missing_bars | Suppressed: malformed_input, missing_bars    |

### Equity Index

| Rank | Instrument                          | Score | Reliable | Risk Gates   | Explanation                                  |
| ---: | ----------------------------------- | ----: | :------: | ------------ | -------------------------------------------- |
|    1 | Dow Jones Industrial Average / ^DJI |  78.2 |   Yes    | —            | 20d up +1.2%; above MA20 by 1.8%; RSI14=75   |
|    5 | FTSE 100 / ^FTSE                    |  66.4 |   Yes    | —            | 20d up +0.2%; above MA20 by 0.9%; RSI14=56   |
|    8 | S&P 500 / ^GSPC                     |  64.5 |   Yes    | —            | 20d down -0.7%; below MA20 by 0.3%; RSI14=56 |
|   10 | DAX / ^GDAXI                        |  57.3 |   Yes    | —            | 20d down -1.1%; above MA20 by 0.1%; RSI14=52 |
|   12 | Russell 2000 / ^RUT                 |  46.7 |   Yes    | —            | 20d down -4.0%; below MA20 by 0.8%; RSI14=46 |
|   13 | NASDAQ 100 / ^NDX                   |  42.7 |   Yes    | —            | 20d down -4.0%; below MA20 by 3.0%; RSI14=37 |
|   14 | Euro Stoxx 50 / ^STOXX50E           |  42.4 |   Yes    | —            | 20d down -3.2%; below MA20 by 1.6%; RSI14=38 |
|   15 | CAC 40 / ^FCHI                      |  40.9 |   Yes    | —            | 20d down -3.9%; below MA20 by 0.9%; RSI14=42 |
|   20 | Hang Seng / ^HSI                    |  32.1 |   Yes    | —            | 20d down -3.6%; below MA20 by 2.1%; RSI14=37 |
|   32 | Nikkei 225 / ^N225                  |  31.8 |    No    | missing_bars | Suppressed: missing_bars                     |

## Data Freshness

Data source: **yfinance**

| Symbol    | Latest Bar |
| --------- | ---------- |
| 6758.T    | 2026-10-20 |
| 7203.T    | 2026-10-20 |
| 8306.T    | 2026-10-20 |
| AAPL      | 2026-10-20 |
| AMZN      | 2026-10-20 |
| BZ=F      | 2026-10-20 |
| CL=F      | 2026-10-20 |
| GC=F      | 2026-10-20 |
| GOOGL     | 2026-10-20 |
| HG=F      | 2026-10-20 |
| JPM       | 2026-10-20 |
| META      | 2026-10-20 |
| MSFT      | 2026-10-20 |
| NG=F      | 2026-10-20 |
| NVDA      | 2026-10-20 |
| PL=F      | 2026-10-20 |
| SI=F      | 2026-10-20 |
| TSLA      | 2026-10-20 |
| UNH       | 2026-10-20 |
| XOM       | 2026-10-20 |
| ZC=F      | 2026-10-20 |
| ZS=F      | 2026-10-20 |
| ZW=F      | 2026-10-20 |
| ^DJI      | 2026-10-20 |
| ^FCHI     | 2026-10-20 |
| ^FTSE     | 2026-10-20 |
| ^GDAXI    | 2026-10-20 |
| ^GSPC     | 2026-10-20 |
| ^HSI      | 2026-10-20 |
| ^N225     | 2026-10-20 |
| ^NDX      | 2026-10-20 |
| ^RUT      | 2026-10-20 |
| ^STOXX50E | 2026-10-20 |

## Symbol Details

### Dow Jones Industrial Average / ^DJI (score 78.2)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.0% |
| ret_5d     | +1.6% |
| ret_20d    | +1.2% |
| ret_60d    | +0.5% |
| ma20_dist  | +1.8% |
| ma50_dist  | +0.2% |
| vol_20d    |  9.3% |
| mdd_60d    |  6.3% |
| rsi_14     |  75.2 |
| zscore_20d |   2.3 |

### UnitedHealth Group Inc. / UNH (score 75.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +3.0% |
| ret_5d     | +11.0% |
| ret_20d    | +12.4% |
| ret_60d    |  +0.4% |
| ma20_dist  |  +9.7% |
| ma50_dist  |  +8.5% |
| vol_20d    |  26.6% |
| mdd_60d    |  14.8% |
| rsi_14     |   80.8 |
| zscore_20d |    2.5 |

### Brent Crude Oil / BZ=F (score 71.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.7% |
| ret_5d     |  +2.9% |
| ret_20d    |  +9.6% |
| ret_60d    | +20.7% |
| ma20_dist  |  +4.0% |
| ma50_dist  |  +9.2% |
| vol_20d    |  30.8% |
| mdd_60d    |   8.7% |
| rsi_14     |   65.7 |
| zscore_20d |    1.5 |

### Microsoft Corporation / MSFT (score 69.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.3% |
| ret_5d     |  -2.1% |
| ret_20d    |  +6.8% |
| ret_60d    | +36.9% |
| ma20_dist  |  +1.6% |
| ma50_dist  |  +5.0% |
| vol_20d    |  21.2% |
| mdd_60d    |   5.1% |
| rsi_14     |   62.3 |
| zscore_20d |    0.6 |

### FTSE 100 / ^FTSE (score 66.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.3% |
| ret_5d     | +0.8% |
| ret_20d    | +0.2% |
| ret_60d    | -0.5% |
| ma20_dist  | +0.9% |
| ma50_dist  | +0.2% |
| vol_20d    | 10.9% |
| mdd_60d    |  4.4% |
| rsi_14     |  56.4 |
| zscore_20d |   0.8 |

### Tesla Inc. / TSLA (score 65.2)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.5% |
| ret_5d     |  -0.4% |
| ret_20d    |  -1.4% |
| ret_60d    | +20.9% |
| ma20_dist  |  +1.1% |
| ma50_dist  |  +3.5% |
| vol_20d    |  32.1% |
| mdd_60d    |   7.3% |
| rsi_14     |   60.8 |
| zscore_20d |    0.4 |

### Amazon.com Inc. / AMZN (score 64.8)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +0.1% |
| ret_5d     |  +1.6% |
| ret_20d    |  +3.0% |
| ret_60d    | +13.5% |
| ma20_dist  |  +3.5% |
| ma50_dist  |  +2.4% |
| vol_20d    |  28.4% |
| mdd_60d    |  13.4% |
| rsi_14     |   62.6 |
| zscore_20d |    1.6 |

### S&P 500 / ^GSPC (score 64.5)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.3% |
| ret_5d     | -1.2% |
| ret_20d    | -0.7% |
| ret_60d    | +4.0% |
| ma20_dist  | -0.3% |
| ma50_dist  | +0.1% |
| vol_20d    |  8.9% |
| mdd_60d    |  3.2% |
| rsi_14     |  55.8 |
| zscore_20d |  -0.4 |

### JPMorgan Chase & Co. / JPM (score 57.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | +1.2% |
| ret_20d    | -0.9% |
| ret_60d    | -5.9% |
| ma20_dist  | +0.5% |
| ma50_dist  | -3.2% |
| vol_20d    | 14.4% |
| mdd_60d    |  9.9% |
| rsi_14     |  60.4 |
| zscore_20d |   0.5 |

### DAX / ^GDAXI (score 57.3)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | +0.2% |
| ret_20d    | -1.1% |
| ret_60d    | -0.6% |
| ma20_dist  | +0.1% |
| ma50_dist  | -1.5% |
| vol_20d    | 12.4% |
| mdd_60d    |  6.6% |
| rsi_14     |  52.0 |
| zscore_20d |   0.2 |

### Apple Inc. / AAPL (score 56.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.0% |
| ret_5d     | -0.5% |
| ret_20d    | -0.1% |
| ret_60d    | +0.9% |
| ma20_dist  | +0.6% |
| ma50_dist  | +3.8% |
| vol_20d    | 16.0% |
| mdd_60d    | 11.0% |
| rsi_14     |  60.5 |
| zscore_20d |   0.4 |

### Russell 2000 / ^RUT (score 46.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +1.7% |
| ret_5d     | -0.4% |
| ret_20d    | -4.0% |
| ret_60d    | -5.9% |
| ma20_dist  | -0.8% |
| ma50_dist  | -4.2% |
| vol_20d    | 15.1% |
| mdd_60d    | 11.3% |
| rsi_14     |  46.5 |
| zscore_20d |  -0.6 |

### NASDAQ 100 / ^NDX (score 42.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.1% |
| ret_5d     | -3.5% |
| ret_20d    | -4.0% |
| ret_60d    | +5.2% |
| ma20_dist  | -3.0% |
| ma50_dist  | -1.2% |
| vol_20d    | 15.1% |
| mdd_60d    |  6.5% |
| rsi_14     |  37.1 |
| zscore_20d |  -1.7 |

### Euro Stoxx 50 / ^STOXX50E (score 42.4)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -0.7% |
| ret_20d    | -3.2% |
| ret_60d    | -2.7% |
| ma20_dist  | -1.6% |
| ma50_dist  | -3.2% |
| vol_20d    | 11.2% |
| mdd_60d    |  6.6% |
| rsi_14     |  37.9 |
| zscore_20d |  -1.6 |

### CAC 40 / ^FCHI (score 40.9)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | +0.1% |
| ret_20d    | -3.9% |
| ret_60d    | -7.3% |
| ma20_dist  | -0.9% |
| ma50_dist  | -4.0% |
| vol_20d    | 11.2% |
| mdd_60d    | 11.4% |
| rsi_14     |  41.9 |
| zscore_20d |  -0.7 |

### Soybeans / ZS=F (score 39.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -2.8% |
| ret_20d    | -5.8% |
| ret_60d    | +6.0% |
| ma20_dist  | -3.0% |
| ma50_dist  | -2.0% |
| vol_20d    | 12.1% |
| mdd_60d    |  6.0% |
| rsi_14     |  28.3 |
| zscore_20d |  -2.0 |

### Alphabet Inc. Class A / GOOGL (score 37.6)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.1% |
| ret_5d     | -3.8% |
| ret_20d    | -3.1% |
| ret_60d    | +4.2% |
| ma20_dist  | -1.5% |
| ma50_dist  | -1.1% |
| vol_20d    | 21.7% |
| mdd_60d    | 12.4% |
| rsi_14     |  46.2 |
| zscore_20d |  -1.1 |

### Gold / GC=F (score 36.7)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -0.4% |
| ret_5d     | -0.8% |
| ret_20d    | -5.3% |
| ret_60d    | +2.3% |
| ma20_dist  | -1.2% |
| ma50_dist  | -5.2% |
| vol_20d    | 17.6% |
| mdd_60d    | 12.7% |
| rsi_14     |  44.9 |
| zscore_20d |  -0.9 |

### NVIDIA Corporation / NVDA (score 32.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -0.3% |
| ret_5d     |  -5.3% |
| ret_20d    |  -5.4% |
| ret_60d    | +10.2% |
| ma20_dist  |  -4.7% |
| ma50_dist  |  -2.8% |
| vol_20d    |  22.9% |
| mdd_60d    |  10.5% |
| rsi_14     |   36.5 |
| zscore_20d |   -1.5 |

### Hang Seng / ^HSI (score 32.1)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | -1.3% |
| ret_5d     | -1.7% |
| ret_20d    | -3.6% |
| ret_60d    | -4.4% |
| ma20_dist  | -2.1% |
| ma50_dist  | -4.3% |
| vol_20d    | 16.0% |
| mdd_60d    |  8.5% |
| rsi_14     |  36.8 |
| zscore_20d |  -1.4 |

### Platinum / PL=F (score 31.8)

| Feature    | Value |
| ---------- | ----: |
| ret_1d     | +0.5% |
| ret_5d     | -0.7% |
| ret_20d    | -9.7% |
| ret_60d    | -0.2% |
| ma20_dist  | -1.9% |
| ma50_dist  | -6.4% |
| vol_20d    | 30.7% |
| mdd_60d    | 16.4% |
| rsi_14     |  40.9 |
| zscore_20d |  -0.7 |

### Meta Platforms Inc. / META (score 29.7)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.6% |
| ret_5d     |  -9.0% |
| ret_20d    |  -5.7% |
| ret_60d    | +16.9% |
| ma20_dist  |  -5.1% |
| ma50_dist  |  +5.3% |
| vol_20d    |  39.4% |
| mdd_60d    |  10.7% |
| rsi_14     |   39.8 |
| zscore_20d |   -2.0 |

### Silver / SI=F (score 26.1)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  +1.3% |
| ret_5d     |  -2.5% |
| ret_20d    | -12.5% |
| ret_60d    |  +0.2% |
| ma20_dist  |  -3.8% |
| ma50_dist  |  -9.5% |
| vol_20d    |  33.9% |
| mdd_60d    |  20.0% |
| rsi_14     |   41.2 |
| zscore_20d |   -1.0 |

### Corn / ZC=F (score 16.4)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.1% |
| ret_5d     |  -4.3% |
| ret_20d    | -13.9% |
| ret_60d    |  +3.6% |
| ma20_dist  |  -7.1% |
| ma50_dist  |  -8.0% |
| vol_20d    |  21.8% |
| mdd_60d    |  14.9% |
| rsi_14     |   22.2 |
| zscore_20d |   -1.7 |

### Wheat / ZW=F (score 13.0)

| Feature    |  Value |
| ---------- | -----: |
| ret_1d     |  -1.8% |
| ret_5d     |  -3.9% |
| ret_20d    | -10.3% |
| ret_60d    |  -3.1% |
| ma20_dist  |  -5.6% |
| ma50_dist  |  -8.1% |
| vol_20d    |  19.2% |
| mdd_60d    |  16.1% |
| rsi_14     |   33.8 |
| zscore_20d |   -2.2 |

## Risk Context

| Instrument                          |  ATR(14) | ATR % of price | Vol-target multiplier | Stop distance | Stop distance % |
| ----------------------------------- | -------: | -------------: | --------------------: | ------------: | --------------: |
| Dow Jones Industrial Average / ^DJI | 528.5287 |           1.0% |                 1.08x |     1057.0575 |            2.0% |
| UnitedHealth Group Inc. / UNH       |  13.3214 |           3.2% |                 0.38x |       26.6429 |            6.4% |
| Brent Crude Oil / BZ=F              |   4.1543 |           3.8% |                 0.32x |        8.3086 |            7.6% |
| Microsoft Corporation / MSFT        |  11.2957 |           2.1% |                 0.47x |       22.5914 |            4.2% |
| FTSE 100 / ^FTSE                    | 120.6999 |           1.1% |                 0.92x |      241.3998 |            2.2% |
| Tesla Inc. / TSLA                   |  11.7607 |           3.1% |                 0.31x |       23.5214 |            6.3% |
| Amazon.com Inc. / AMZN              |   6.5150 |           2.5% |                 0.35x |       13.0300 |            5.0% |
| S&P 500 / ^GSPC                     |  71.8786 |           0.9% |                 1.13x |      143.7572 |            1.9% |
| JPMorgan Chase & Co. / JPM          |   6.4194 |           1.9% |                 0.69x |       12.8389 |            3.8% |
| DAX / ^GDAXI                        | 308.1169 |           1.2% |                 0.81x |      616.2338 |            2.4% |
| Apple Inc. / AAPL                   |   6.0071 |           1.8% |                 0.63x |       12.0143 |            3.5% |
| Russell 2000 / ^RUT                 |  38.5900 |           1.4% |                 0.66x |       77.1800 |            2.8% |
| NASDAQ 100 / ^NDX                   | 458.2002 |           1.6% |                 0.66x |      916.4004 |            3.1% |
| Euro Stoxx 50 / ^STOXX50E           |  74.8243 |           1.2% |                 0.89x |      149.6486 |            2.4% |
| CAC 40 / ^FCHI                      |  91.1928 |           1.2% |                 0.89x |      182.3857 |            2.3% |
| Soybeans / ZS=F                     |  18.3214 |           1.5% |                 0.83x |       36.6429 |            2.9% |
| Alphabet Inc. Class A / GOOGL       |   8.6679 |           2.5% |                 0.46x |       17.3357 |            5.1% |
| Gold / GC=F                         |  69.7499 |           1.7% |                 0.57x |      139.4999 |            3.4% |
| NVIDIA Corporation / NVDA           |   5.7779 |           2.7% |                 0.44x |       11.5557 |            5.3% |
| Hang Seng / ^HSI                    | 349.9736 |           1.5% |                 0.62x |      699.9473 |            2.9% |
| Platinum / PL=F                     |  30.1929 |           1.8% |                 0.33x |       60.3857 |            3.7% |
| Meta Platforms Inc. / META          |  21.9014 |           3.2% |                 0.25x |       43.8029 |            6.3% |
| Silver / SI=F                       |   1.2046 |           2.1% |                 0.29x |        2.4091 |            4.2% |
| Corn / ZC=F                         |  10.1429 |           2.2% |                 0.46x |       20.2857 |            4.4% |
| Wheat / ZW=F                        |  15.5000 |           2.4% |                 0.52x |       31.0000 |            4.8% |

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

Scoring engine version: **1.0.0** | Git commit: **b86e327**

For methodology details, see OPERATIONS.md in the repository root.

## Disclaimer

> This report is generated automatically from publicly available market data for informational purposes only. It does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.
