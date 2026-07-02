---
description: Authoritative market and instrument data sources used by AIMS and the
  boundaries for durable knowledge updates.
params:
  okf_extra:
    id: okf/concepts/data-sources
    status: seeded
  okf_type: concept
resource:
  path: okf/concepts/data-sources.md
  source: repository
tags:
- data-sources
- market-analysis
timestamp: '2026-07-02T00:00:00Z'
title: Data Sources
type: knowledge
---

# Data Sources

Authoritative market and instrument data sources used by AIMS and the boundaries for durable knowledge updates.

## Repository facts

AIMS fetches daily OHLCV history from Yahoo Finance (`yfinance` library, default provider) with Stooq registered as a fallback/alternative provider. The daily workflow derives its symbol universe from `data/mappings/canonical_instrument_mappings.csv` for the configured provider and interval — there is no separate provider symbol list file.

Individual stocks are configured the same way as equity indices and commodities: as rows in `canonical_instrument_mappings.csv` with `asset_class=equity`. Adding a stock row with `provider=yfinance` and `provider_interval=d` is sufficient for the daily workflow to fetch and score it — no separate stock symbol list exists.

The CFD instrument master is a separate data source maintained in `data/cfd_instruments.csv`. It is refreshed by the weekly updater workflow and validated before the daily market analysis workflow runs.

## Source-of-truth boundary

AIMS keeps numeric market facts, scores, ranks, dates, risk gates, and data availability in generated artifacts and validated reports. This OKF concept captures durable repository knowledge only.

## Related concepts

- [Instrument Master](../instrument-master/)
- [Scoring Methodology](../scoring-methodology/)

# Citations

- `OPERATIONS.md`
- `.github/workflows/daily-market-analysis.yml`
- `.github/workflows/update-cfd-instruments.yml`
