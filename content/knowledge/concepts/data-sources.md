---
description: Authoritative market and instrument data sources used by AIMS and the boundaries for durable knowledge updates.
id: okf/concepts/data-sources
params:
  okf_type: concept
resource:
  path: okf/concepts/data-sources.md
  source: repository
tags:
  - data-sources
  - market-analysis
timestamp: 2026-06-16T00:00:00Z
title: Data Sources
type: knowledge
---

# Data Sources

Authoritative market and instrument data sources used by AIMS and the boundaries for durable knowledge updates.

## Source-of-truth boundary

AIMS keeps numeric market facts, scores, ranks, dates, risk gates, and data availability in `data/analysis/*.json` and generated daily reports in `content/results/`. This OKF concept captures durable repository knowledge only and must not invent or override generated numeric facts.

## AIMS notes

This concept is seeded from repository documentation, operations guidance, tests, workflows, and issue dceoy/aims#57. Update it through the OKF authoring and curation workflow when durable architecture or operational knowledge changes.

## Related concepts

- [Related: instrument-master](./instrument-master.md)
- [Related: scoring-methodology](./scoring-methodology.md)
