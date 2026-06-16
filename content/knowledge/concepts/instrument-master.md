---
description: Canonical CFD instrument reference data and validation responsibilities in AIMS.
id: okf/concepts/instrument-master
params:
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

## Source-of-truth boundary

AIMS keeps numeric market facts, scores, ranks, dates, risk gates, and data availability in `data/analysis/*.json` and generated daily reports in `content/results/`. This OKF concept captures durable repository knowledge only and must not invent or override generated numeric facts.

## AIMS notes

This concept is seeded from repository documentation, operations guidance, tests, workflows, and issue dceoy/aims#57. Update it through the OKF authoring and curation workflow when durable architecture or operational knowledge changes.

## Related concepts

- [Related: data-sources](./data-sources.md)
- [Related: scoring-methodology](./scoring-methodology.md)
