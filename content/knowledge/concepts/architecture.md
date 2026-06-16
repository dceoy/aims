---
description: Repository-level architecture for the AIMS analysis pipeline, static site, OKF source, and generated knowledge pages.
id: okf/concepts/architecture
params:
  okf_type: concept
resource:
  path: okf/concepts/architecture.md
  source: repository
tags:
  - architecture
  - okf
  - hugo
timestamp: 2026-06-16T00:00:00Z
title: AIMS Architecture
type: knowledge
---

# AIMS Architecture

Repository-level architecture for the AIMS analysis pipeline, static site, OKF source, and generated knowledge pages.

## Source-of-truth boundary

AIMS keeps numeric market facts, scores, ranks, dates, risk gates, and data availability in `data/analysis/*.json` and generated daily reports in `content/results/`. This OKF concept captures durable repository knowledge only and must not invent or override generated numeric facts.

## AIMS notes

This concept is seeded from repository documentation, operations guidance, tests, workflows, and issue dceoy/aims#57. Update it through the OKF authoring and curation workflow when durable architecture or operational knowledge changes.

## Related concepts

- [Related: data-sources](./data-sources.md)
- [Related: report-generation](./report-generation.md)
- [Related: publication-workflow](./publication-workflow.md)
