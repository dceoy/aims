---
id: okf/concepts/publication-workflow
title: Publication Workflow
description: How CI/CD, pull requests, and GitHub Pages publish AIMS reports and generated OKF shadow content.
type: concept
tags:
  - ci
  - hugo
  - publication
timestamp: 2026-06-16T00:00:00Z
resource:
  path: okf/concepts/publication-workflow.md
  source: repository
---

# Publication Workflow

How CI/CD, pull requests, and GitHub Pages publish AIMS reports and generated OKF shadow content.

## Source-of-truth boundary

AIMS keeps numeric market facts, scores, ranks, dates, risk gates, and data availability in `data/analysis/*.json` and generated daily reports in `content/results/`. This OKF concept captures durable repository knowledge only and must not invent or override generated numeric facts.

## AIMS notes

This concept is seeded from repository documentation, operations guidance, tests, workflows, and issue dceoy/aims#57. Update it through the OKF authoring and curation workflow when durable architecture or operational knowledge changes.

## Related concepts

- [Related: architecture](./architecture.md)
- [Related: operational-recovery](./operational-recovery.md)
