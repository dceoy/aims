---
description: Runbook-oriented knowledge for restoring AIMS analysis, validation, and publication workflows.
id: okf/concepts/operational-recovery
params:
  okf_type: concept
resource:
  path: okf/concepts/operational-recovery.md
  source: repository
tags:
  - operations
  - recovery
timestamp: 2026-06-16T00:00:00Z
title: Operational Recovery
type: knowledge
---

# Operational Recovery

Runbook-oriented knowledge for restoring AIMS analysis, validation, and publication workflows.

## Source-of-truth boundary

AIMS keeps numeric market facts, scores, ranks, dates, risk gates, and data availability in `data/analysis/*.json` and generated daily reports in `content/results/`. This OKF concept captures durable repository knowledge only and must not invent or override generated numeric facts.

## AIMS notes

This concept is seeded from repository documentation, operations guidance, tests, workflows, and issue dceoy/aims#57. Update it through the OKF authoring and curation workflow when durable architecture or operational knowledge changes.

## Related concepts

- [Related: publication-workflow](./publication-workflow.md)
- [Related: agent-skills](./agent-skills.md)
