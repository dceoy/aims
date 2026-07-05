# AIMS OKF Log

## 2026-07-04

- Added the deterministic qualitative theme curation pass (#96): `curate_themes.py` proposes promotions of recurring themes from `data/qualitative/*.json` into `qualitative-theme`-tagged concepts, with monthly cadence, ≥3-dates/≥14-day promotion criteria, and 60-day retirement criteria documented in the `aims-okf-curator` skill. Ran the first pass: zero qualitative artifacts have accumulated on `main` yet (shadow mode has not produced committed artifacts), so this is a recorded empty pass with no promotions — the first real promotion PR follows once artifacts accumulate.
- Seeded the Qualitative Analysis concept documenting the AI qualitative layer design (roadmap #98, design issue #89): artifact contract with machine-checkable claims, grounding rules, deterministic gates, fail-open policy, and shadow-mode rollout. Operational contract recorded in `OPERATIONS.md` §10 and `data/schema/qualitative.schema.json`.

## 2026-06-16

- Established `okf/` as the canonical OKF v0.1 knowledge source for durable AIMS concepts.
- Added generated `content/knowledge/` shadow content as Hugo publication output, not a canonical authoring location.
- Seeded initial concepts for architecture, data sources, instrument master data, scoring methodology, report generation, publication, recovery, and Agent Skills.
