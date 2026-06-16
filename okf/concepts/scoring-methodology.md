---
id: okf/concepts/scoring-methodology
title: Scoring Methodology
description: How AIMS treats analysis artifacts, score semantics, ranking outputs, and risk gates as generated numeric facts.
type: concept
tags: [scoring, market-analysis]
timestamp: 2026-06-16T00:00:00Z
resource:
  path: okf/concepts/scoring-methodology.md
  source: repository
status: seeded
---

# Scoring Methodology

How AIMS treats analysis artifacts, score semantics, ranking outputs, and risk gates as generated numeric facts.

## Repository facts

AIMS computes cross-sectional rankings from daily OHLCV-derived features and produces a composite score from percentile ranks. Risk gates mark unreliable instruments, which remain in output but are ranked below reliable instruments.

OKF concepts may summarize durable methodology, but numeric market facts, scores, ranks, dates, risk gates, and availability remain authoritative only in generated analysis artifacts and validated report outputs.

## Source-of-truth boundary

AIMS keeps numeric market facts, scores, ranks, dates, risk gates, and data availability in generated artifacts and validated reports. This OKF concept captures durable repository knowledge only.

## Related concepts

- [Data Sources](/concepts/data-sources.md)
- [Report Generation](/concepts/report-generation.md)

# Citations

- `OPERATIONS.md`
- `data/schema/analysis.schema.json`
- `AGENTS.md`
