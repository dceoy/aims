---
id: okf/concepts/qualitative-analysis
title: Qualitative Analysis
description: How the AI qualitative layer adds grounded, citation-bound interpretation around the quantitative signal without becoming a source of numeric truth.
type: concept
tags: [qualitative, market-analysis]
timestamp: 2026-07-04T00:00:00Z
resource:
  path: okf/concepts/qualitative-analysis.md
  source: repository
status: seeded
---

# Qualitative Analysis

How the AI qualitative layer adds grounded, citation-bound interpretation around the quantitative signal without becoming a source of numeric truth.

## Repository facts

AIMS plans a qualitative layer in which a single daily LLM call reads the day's analysis artifact, committed evidence bundle, and event calendar, and writes a schema-validated `data/qualitative/` artifact. The call is the pipeline's only non-deterministic step; validation, deterministic gates, report rendering, and the Hugo build stay deterministic, and reports without a qualitative artifact are byte-identical to today's.

Claims are machine-checkable by contract: stances and confidence are closed enums, drivers carry structured direction and numeric claims, and every driver cites evidence IDs from the committed bundle. Deterministic gates cross-examine those structured claims against the quantitative features and withhold entries that fail; a stance that merely disagrees with the quantitative signal is legitimate output and is never gated for the disagreement.

The layer is fail-open and staged: without an `ANTHROPIC_API_KEY` secret or on any qualitative failure, the quantitative report publishes unchanged; because analysis pull requests auto-merge without human review, rendering is enabled only after a shadow period meets recorded exit criteria.

## Source-of-truth boundary

AIMS keeps numeric market facts, scores, ranks, dates, risk gates, and data availability in generated artifacts and validated reports. Qualitative artifacts may reference those numbers but never restate them authoritatively and never modify them. This OKF concept captures durable design knowledge only; the operational contract lives in `OPERATIONS.md` §10 and `data/schema/qualitative.schema.json`.

## Related concepts

- [Scoring Methodology](/concepts/scoring-methodology.md)
- [Report Generation](/concepts/report-generation.md)
- [Publication Workflow](/concepts/publication-workflow.md)

# Citations

- `OPERATIONS.md`
- `data/schema/qualitative.schema.json`
