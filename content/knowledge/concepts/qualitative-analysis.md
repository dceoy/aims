---
description: Design contract for the grounded AI qualitative layer that enriches AIMS
  reports while the quantitative pipeline remains the source of deterministic market
  scores.
params:
  okf_extra:
    id: okf/concepts/qualitative-analysis
    status: seeded
  okf_type: concept
resource:
  path: okf/concepts/qualitative-analysis.md
  source: repository
tags:
- qualitative-analysis
- market-analysis
- grounding
timestamp: '2026-07-02T00:00:00Z'
title: AI Qualitative Analysis
type: knowledge
---

# AI Qualitative Analysis

Design contract for the grounded AI qualitative layer that enriches AIMS reports while the quantitative pipeline remains the source of deterministic market scores.

## Repository facts

The qualitative layer reads three committed inputs — the day's quantitative analysis artifact (`data/analysis/`), a validated evidence bundle of news and disclosure items (`data/evidence/`), and scheduled-event calendars (`data/calendars/`) — and produces one versioned output, `data/qualitative/YYYY-MM-DD.json`, validated against `data/schema/qualitative.schema.json`.

The LLM call in `src/aims/qualitative.py` is the single non-deterministic step in the pipeline. It writes an artifact, never report prose; validation, grounding gates, and report rendering are deterministic given that artifact. Artifacts record the model id, prompt version, and SHA-256 hashes of their inputs.

Grounding is evidence-first: every driver, theme, and market narrative must cite evidence ids from the committed bundle. Fabricated citations are dropped at assembly, out-of-universe instruments are discarded, and deterministic gates (`uncited_claims`, `stale_evidence`, `numeric_claim_mismatch`, `direction_conflict`) withhold entries from rendering while the rest of the artifact still publishes. Evidence text is untrusted data: markup-stripped, length-capped, delimited as quoted content in the prompt, and never interpreted as instructions.

The layer is fail-open. When `ANTHROPIC_API_KEY` is absent or any qualitative step fails, the daily workflow publishes the quantitative report unchanged. Quantitative coverage gates are never weakened by the qualitative layer.

## Source-of-truth boundary

The quantitative artifact remains authoritative for all scores, ranks, dates, prices, risk gates, and data availability. Qualitative artifacts may reference those facts but never restate them authoritatively and never modify them. LLM-authored prose is never the source of truth for numeric facts, consistent with the wider OKF guardrail.

No vector databases, embeddings pipelines, external RAG services, or server-side runtimes are used, per repository policy.

## Related concepts

- [Data Sources](../data-sources/)
- [Report Generation](../report-generation/)
- [Publication Workflow](../publication-workflow/)
- [Scoring Methodology](../scoring-methodology/)

# Citations

- `OPERATIONS.md`
- `.agents/skills/qualitative-analysis/SKILL.md`
- `data/schema/qualitative.schema.json`
