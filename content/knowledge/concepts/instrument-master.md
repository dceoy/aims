---
description: Canonical CFD instrument reference data and validation responsibilities
  in AIMS.
params:
  okf_extra:
    id: okf/concepts/instrument-master
    status: seeded
  okf_type: concept
resource:
  path: okf/concepts/instrument-master.md
  source: repository
tags:
- cfd
- data
- instrument-master
timestamp: 2026-06-16T00:00:00Z
title: Instrument Master
type: knowledge
---

# Instrument Master

Canonical CFD instrument reference data and validation responsibilities in AIMS.

## Repository facts

The CFD instrument master is stored in `data/cfd_instruments.csv` and sourced from GMO Click Securities and Rakuten Securities CFD lineup pages. Broker ticker symbols are maintained separately from Stooq symbols, with mappings in `data/mappings/cfd_ticker_mappings.csv`.

The master CSV is validated against `data/schema/cfd_instruments.schema.json` after updates and before daily analysis.

## Source-of-truth boundary

AIMS keeps numeric market facts, scores, ranks, dates, risk gates, and data availability in generated artifacts and validated reports. This OKF concept captures durable repository knowledge only.

## Related concepts

- [Data Sources](../data-sources/)
- [Scoring Methodology](../scoring-methodology/)

# Citations

- `OPERATIONS.md`
- `data/schema/cfd_instruments.schema.json`
- `.agents/skills/update-cfd-instruments/SKILL.md`
