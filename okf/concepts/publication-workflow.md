---
id: okf/concepts/publication-workflow
title: Publication Workflow
description: How CI/CD, pull requests, and GitHub Pages publish AIMS reports and generated OKF shadow content.
type: concept
tags: [ci, hugo, publication]
timestamp: 2026-06-16T00:00:00Z
resource:
  path: okf/concepts/publication-workflow.md
  source: repository
status: seeded
---

# Publication Workflow

How CI/CD, pull requests, and GitHub Pages publish AIMS reports and generated OKF shadow content.

## Repository facts

The daily analysis workflow validates the CFD master, generates JSON artifacts, validates the artifact, generates a Hugo report, builds the Hugo site for validation, and opens a pull request for review.

The CI workflow deploys the Hugo site to GitHub Pages after linting, type checking, and tests pass. The OKF validation job checks generated knowledge content drift before deployment.

## Source-of-truth boundary

AIMS keeps numeric market facts, scores, ranks, dates, risk gates, and data availability in generated artifacts and validated reports. This OKF concept captures durable repository knowledge only.

## Related concepts

- [Architecture](/concepts/architecture.md)
- [Operational Recovery](/concepts/operational-recovery.md)

# Citations

- `OPERATIONS.md`
- `.github/workflows/daily-market-analysis.yml`
- `.github/workflows/ci.yml`
