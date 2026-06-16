---
description: Repository-level architecture for the AIMS analysis pipeline, Hugo site,
  OKF source, and generated knowledge pages.
id: okf/concepts/architecture
params:
  okf_type: concept
resource:
  path: okf/concepts/architecture.md
  source: repository
status: seeded
tags:
- architecture
- okf
- hugo
timestamp: 2026-06-16 00:00:00+00:00
title: AIMS Architecture
type: knowledge
---

# AIMS Architecture

Repository-level architecture for the AIMS analysis pipeline, Hugo site, OKF source, and generated knowledge pages.

## Repository facts

AIMS combines Python automation with a Hugo static site. Python scripts live under `.agents/skills/`, tests live in `tests/`, schemas live under `data/schema/`, and Hugo source content lives under `content/`. Generated static output is written to the ignored `site/` directory.

The OKF layer adds `okf/` as the durable knowledge source while preserving existing source-of-truth boundaries: daily analysis JSON remains under `data/analysis/`, public reports remain under `content/results/`, and `content/knowledge/` is regenerated from OKF.

## Source-of-truth boundary

AIMS keeps numeric market facts, scores, ranks, dates, risk gates, and data availability in generated artifacts and validated reports. This OKF concept captures durable repository knowledge only.

## Related concepts

- [Data Sources](/knowledge/concepts/data-sources/)
- [Report Generation](/knowledge/concepts/report-generation/)
- [Publication Workflow](/knowledge/concepts/publication-workflow/)

# Citations

- `AGENTS.md`
- `README.md`
