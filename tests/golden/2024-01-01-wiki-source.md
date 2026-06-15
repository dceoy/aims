<!-- generated-by: market-wiki/render_wiki_source.py -->
<!-- source-sha256: e0cf55e5218f7da1a65d48d86cdbdf90ae262496a8c98cf5cc041bd6d85dab89 -->

# Market Analysis Source: 2024-01-01

## Metadata

- Analysis date: 2024-01-01
- Generated at: 2024-01-01T01:00:00+00:00
- Artifact version: 1.0.0
- Data source: stooq
- Scoring version: 1.0.0
- Git commit: abc1234
- Source artifact: tests/fixtures/analysis_2024-01-01.json
- Renderer schema: 1

## Market snapshot

- Instruments analyzed: 3
- Reliable instruments: 2
- Unreliable instruments: 1

## Top-ranked instruments

<!-- prettier-ignore-start -->
| Rank | Symbol | Score | Reliable | Risk gates | Explanation |
| ---: | --- | ---: | --- | --- | --- |
| 1 | ^SPX | 72.5 | true | none | 20d up +5.3%; above MA20 by 2.1%; RSI14=62 |
| 2 | ^DJI | 58.3 | true | none | 20d up +2.1%; above MA20 by 0.8%; RSI14=55 |
| 3 | ^NDX | 31.7 | false | insufficient_history | Suppressed: insufficient_history |
<!-- prettier-ignore-end -->

## Unreliable instruments

- ^NDX: insufficient_history

## Risk gates

- insufficient_history: 1

## Notable feature values

- ^SPX: ma20_dist=0.021, ma50_dist=0.018, mdd_60d=0.031, ret_1d=0.012, ret_20d=0.053, ret_5d=0.031, ret_60d=0.089, rsi_14=62, vol_20d=0.127, zscore_20d=1.2
- ^DJI: ma20_dist=0.008, ma50_dist=0.012, mdd_60d=0.018, ret_1d=0.005, ret_20d=0.021, ret_5d=0.015, ret_60d=0.042, rsi_14=55, vol_20d=0.089, zscore_20d=0.7
- ^NDX: ma20_dist=n/a, ma50_dist=n/a, mdd_60d=n/a, ret_1d=n/a, ret_20d=n/a, ret_5d=n/a, ret_60d=n/a, rsi_14=n/a, vol_20d=n/a, zscore_20d=n/a

## Data freshness

- ^DJI: 2023-12-29
- ^NDX: n/a
- ^SPX: 2024-01-01
