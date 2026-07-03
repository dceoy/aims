---
name: qualitative-analysis
description: Fetch grounded news/disclosure evidence and event calendars, generate a schema-validated AI qualitative analysis artifact via the Claude API, apply deterministic grounding gates, and evaluate published stances against realized returns.
---

# qualitative-analysis

Enrich AIMS reports with grounded AI analysis of news, earnings, disclosures,
and macro events — while the quantitative pipeline remains the sole source of
deterministic market scores.

> **Disclaimer:** All output is informational only and does not constitute investment advice.

## Design contract

- The LLM call in `generate_qualitative.py` is the **single non-deterministic
  step** in the pipeline. It writes a versioned artifact
  (`data/qualitative/YYYY-MM-DD.json`), never report prose; everything
  downstream (validation, gating, rendering) is deterministic.
- The AI **never modifies** scores, ranks, risk gates, or the market regime.
- Every claim must cite evidence ids from the committed evidence bundle
  (`data/evidence/YYYY-MM-DD.json`). Fabricated citations are dropped at
  assembly and the orphaned claims are gated as `uncited_claims`.
- Evidence text is untrusted: it is markup-stripped, length-capped, delimited
  as quoted data in the prompt, and never interpreted as instructions.
- The whole layer is **fail-open**: when `ANTHROPIC_API_KEY` is absent or any
  qualitative step fails, the quantitative report publishes unchanged.
- No vector databases, embeddings pipelines, external RAG services, or
  server-side runtimes (repository policy).

## Scripts

All scripts are in `.agents/skills/qualitative-analysis/scripts/` and
delegate to `src/aims/`.

| Script                    | Purpose                                                                   |
| ------------------------- | ------------------------------------------------------------------------- |
| `fetch_evidence.py`       | `fetch` news (yfinance) + curated feeds into a bundle; `validate` bundles |
| `update_calendars.py`     | `fetch-earnings` via yfinance; `validate` calendar files                  |
| `generate_qualitative.py` | Call the Claude API and write the gated qualitative artifact              |
| `validate_qualitative.py` | Re-check an artifact against evidence and analysis inputs                 |
| `evaluate_qualitative.py` | `evaluate` stances vs realized returns; `check-links` for link rot        |

## Usage

```sh
DATE=$(date -u +%Y-%m-%d)

# 1. Fetch the evidence bundle (deterministic given fetched inputs)
uv run .agents/skills/qualitative-analysis/scripts/fetch_evidence.py \
    fetch --mapping data/mappings/canonical_instrument_mappings.csv \
    --provider yfinance --interval d \
    --sources data/mappings/evidence_sources.csv \
    --analysis-date "$DATE" --output data/evidence/

# 2. Refresh the earnings calendar (equity mapping rows)
uv run .agents/skills/qualitative-analysis/scripts/update_calendars.py \
    fetch-earnings --mapping data/mappings/canonical_instrument_mappings.csv \
    --provider yfinance --interval d --output data/calendars/earnings.json

# 3. Generate the qualitative artifact (needs ANTHROPIC_API_KEY)
ANTHROPIC_API_KEY=... \
uv run .agents/skills/qualitative-analysis/scripts/generate_qualitative.py \
    --analysis "data/analysis/${DATE}.json" \
    --evidence "data/evidence/${DATE}.json" \
    --calendar-dir data/calendars --output data/qualitative/

# 4. Re-validate the artifact against its inputs
uv run .agents/skills/qualitative-analysis/scripts/validate_qualitative.py \
    --input "data/qualitative/${DATE}.json" \
    --evidence "data/evidence/${DATE}.json" \
    --analysis "data/analysis/${DATE}.json"

# 5. Render the report with commentary and upcoming events
uv run .agents/skills/market-analysis/scripts/generate_report.py \
    --input "data/analysis/${DATE}.json" \
    --history "data/history/${DATE}.json" \
    --qualitative "data/qualitative/${DATE}.json" \
    --calendar-dir data/calendars --output content/results/

# 6. Periodically: evaluate stance quality and citation health
uv run .agents/skills/qualitative-analysis/scripts/evaluate_qualitative.py \
    evaluate --qualitative-dir data/qualitative --prices-dir data/prices \
    --output data/performance/qualitative_evaluation.json
uv run .agents/skills/qualitative-analysis/scripts/evaluate_qualitative.py \
    check-links --evidence-dir data/evidence
```

## Grounding gates

Deterministic cross-checks recorded per entry (see
`src/aims/validate_qualitative.py`); gated entries are excluded from report
rendering while the rest of the artifact still publishes:

| Gate                     | Trigger                                                                 |
| ------------------------ | ----------------------------------------------------------------------- |
| `uncited_claims`         | A driver/theme/narrative block has no surviving citations               |
| `stale_evidence`         | Every cited item is older than the freshness window (default 5 days)    |
| `numeric_claim_mismatch` | A percentage claim matches neither the analysis features nor cited text |
| `direction_conflict`     | Direction words contradict the sign of `ret_5d`/`ret_20d`               |

## Data layout

```
data/
├── evidence/YYYY-MM-DD.json      # Evidence bundle (schema: evidence.schema.json)
├── calendars/macro_events.json   # Curated macro schedule (calendar.schema.json)
├── calendars/earnings.json       # Generated earnings calendar
├── qualitative/YYYY-MM-DD.json   # Gated AI artifact (qualitative.schema.json)
└── performance/qualitative_evaluation.json
```

## Prompt changes

`PROMPT_VERSION` in `src/aims/qualitative.py` must be bumped whenever the
system prompt or tool schema changes, and the prompt regression tests
(`tests/test_qualitative_prompt_regression.py`) must pass before adopting a
prompt or model change. Artifacts record model id, prompt version, and input
hashes for full traceability.
