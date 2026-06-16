---
id: okf/concepts/agent-skills
title: Agent Skills
description: Repository-local Agent Skills that guide AIMS automation, OKF curation, site generation, and PR review.
type: concept
tags: [agents, skills, okf]
timestamp: 2026-06-16T00:00:00Z
resource:
  path: okf/concepts/agent-skills.md
  source: repository
status: seeded
---

# Agent Skills

Repository-local Agent Skills that guide AIMS automation, OKF curation, site generation, and PR review.

## Repository facts

Repository-local Agent Skills describe repeatable workflows for market analysis, CFD instrument updates, local QA, PR feedback triage, and OKF maintenance. The OKF author, curator, site, and PR-review skills point agents at canonical `okf/` edits and generated `content/knowledge/` validation.

Agent workflows must keep generated knowledge separate from canonical OKF and must not invent numeric market facts.

## Source-of-truth boundary

AIMS keeps numeric market facts, scores, ranks, dates, risk gates, and data availability in generated artifacts and validated reports. This OKF concept captures durable repository knowledge only.

## Related concepts

- [Architecture](/concepts/architecture.md)
- [Operational Recovery](/concepts/operational-recovery.md)

# Citations

- `.agents/skills/local-qa/SKILL.md`
- `.agents/skills/market-analysis/SKILL.md`
- `.agents/skills/update-cfd-instruments/SKILL.md`
- `.agents/skills/aims-okf-author/SKILL.md`
