---
id: okf/concepts/agent-skills
title: Agent Skills
description: Repository-local Agent Skills that guide AIMS automation, OKF curation, site generation, and PR review.
type: concept
tags:
  - agents
  - skills
  - okf
timestamp: 2026-06-16T00:00:00Z
resource:
  path: okf/concepts/agent-skills.md
  source: repository
---

# Agent Skills

Repository-local Agent Skills that guide AIMS automation, OKF curation, site generation, and PR review.

## Source-of-truth boundary

AIMS keeps numeric market facts, scores, ranks, dates, risk gates, and data availability in `data/analysis/*.json` and generated daily reports in `content/results/`. This OKF concept captures durable repository knowledge only and must not invent or override generated numeric facts.

## AIMS notes

This concept is seeded from repository documentation, operations guidance, tests, workflows, and issue dceoy/aims#57. Update it through the OKF authoring and curation workflow when durable architecture or operational knowledge changes.

## Related concepts

- [Related: architecture](./architecture.md)
- [Related: operational-recovery](./operational-recovery.md)
