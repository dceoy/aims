---
id: okf/concepts/scoring-methodology
title: Scoring Methodology
description: How AIMS treats analysis artifacts, score semantics, ranking outputs, and risk gates as generated numeric facts.
type: concept
tags:
  - scoring
  - market-analysis
timestamp: 2026-06-16T00:00:00Z
resource:
  path: okf/concepts/scoring-methodology.md
  source: repository
---

# Scoring Methodology

How AIMS treats analysis artifacts, score semantics, ranking outputs, and risk gates as generated numeric facts.

## Source-of-truth boundary

AIMS keeps numeric market facts, scores, ranks, dates, risk gates, and data availability in `data/analysis/*.json` and generated daily reports in `content/results/`. This OKF concept captures durable repository knowledge only and must not invent or override generated numeric facts.

## AIMS notes

This concept is seeded from repository documentation, operations guidance, tests, workflows, and issue dceoy/aims#57. Update it through the OKF authoring and curation workflow when durable architecture or operational knowledge changes.

## Related concepts

- [Related: data-sources](./data-sources.md)
- [Related: report-generation](./report-generation.md)
