---
id: okf/concepts/report-generation
title: Report Generation
description: How deterministic JSON analysis artifacts become public Hugo market analysis reports.
type: concept
tags: [reports, hugo, market-analysis]
timestamp: 2026-06-16T00:00:00Z
resource:
  path: okf/concepts/report-generation.md
  source: repository
status: seeded
---

# Report Generation

How deterministic JSON analysis artifacts become public Hugo market analysis reports.

## Repository facts

The report generator reads `data/analysis/YYYY-MM-DD.json` and writes Hugo Markdown reports to `content/results/YYYY-MM-DD-market-analysis.md`. The generator is deterministic: identical JSON input produces identical Markdown output and the report timestamp comes from the artifact.

OKF-generated `content/knowledge/` pages are separate from `content/results/` reports and do not replace daily report generation.

## Source-of-truth boundary

AIMS keeps numeric market facts, scores, ranks, dates, risk gates, and data availability in generated artifacts and validated reports. This OKF concept captures durable repository knowledge only.

## Related concepts

- [Architecture](/concepts/architecture.md)
- [Publication Workflow](/concepts/publication-workflow.md)

# Citations

- `OPERATIONS.md`
- `README.md`
- `tests/golden/2024-01-01-market-analysis.md`
