---
description: Runbook-oriented knowledge for restoring AIMS analysis, validation, and
  publication workflows.
id: okf/concepts/operational-recovery
params:
  okf_type: concept
resource:
  path: okf/concepts/operational-recovery.md
  source: repository
status: seeded
tags:
- operations
- recovery
timestamp: 2026-06-16 00:00:00+00:00
title: Operational Recovery
type: knowledge
---

# Operational Recovery

Runbook-oriented knowledge for restoring AIMS analysis, validation, and publication workflows.

## Repository facts

Operational recovery starts from the failing workflow step: Stooq fetch warnings are non-fatal per symbol, artifact validation failures should be fixed in the generated JSON or generator inputs, and site build failures should be reproduced locally with Hugo.

Manual recovery uses the documented scripts and validations rather than editing generated outputs by hand.

## Source-of-truth boundary

AIMS keeps numeric market facts, scores, ranks, dates, risk gates, and data availability in generated artifacts and validated reports. This OKF concept captures durable repository knowledge only.

## Related concepts

- [Publication Workflow](/knowledge/concepts/publication-workflow/)
- [Agent Skills](/knowledge/concepts/agent-skills/)

# Citations

- `OPERATIONS.md`
- `.agents/skills/local-qa/SKILL.md`
