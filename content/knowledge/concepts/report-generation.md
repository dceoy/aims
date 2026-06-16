---
description: How deterministic JSON analysis artifacts become public Hugo market analysis reports.
id: okf/concepts/report-generation
params:
  okf_type: concept
resource:
  path: okf/concepts/report-generation.md
  source: repository
tags:
  - reports
  - hugo
  - market-analysis
timestamp: 2026-06-16T00:00:00Z
title: Report Generation
type: knowledge
---

# Report Generation

How deterministic JSON analysis artifacts become public Hugo market analysis reports.

## Source-of-truth boundary

AIMS keeps numeric market facts, scores, ranks, dates, risk gates, and data availability in `data/analysis/*.json` and generated daily reports in `content/results/`. This OKF concept captures durable repository knowledge only and must not invent or override generated numeric facts.

## AIMS notes

This concept is seeded from repository documentation, operations guidance, tests, workflows, and issue dceoy/aims#57. Update it through the OKF authoring and curation workflow when durable architecture or operational knowledge changes.

## Related concepts

- [Related: architecture](./architecture.md)
- [Related: publication-workflow](./publication-workflow.md)
