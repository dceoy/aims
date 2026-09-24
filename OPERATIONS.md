Warning: truncated output (original token count: 20687)
Total output lines: 819

# AIMS — Operations Guide

This document covers data sources, scoring methodology, report generation, the publication workflow, required secrets, troubleshooting, and manual recovery.

> **Disclaimer:** All analysis produced by AIMS is for informational purposes only and does not constitute investment advice, a solicitation, or a recommendation to buy or sell any financial instrument. Past performance is not indicative of future results. Always consult a qualified financial adviser before making investment decisions.

---

## Table of contents

1. [Data sources](#1-data-sources)
2. [Instrument master](#2-instrument-master)
3. [Scoring methodology](#3-scoring-methodology)
4. [Report generation](#4-report-generation)
5. [Publication workflow](#5-publication-workflow)
6. [GitHub Actions secrets](#6-github-actions-secrets)
7. [Required permissions](#7-required-permissions)
8. [Troubleshooting](#8-troubleshooting)
9. [Manual recovery](#9-manual-recovery)
10. [AI qualitative analysis layer (design)](#10-ai-qualitative-analysis-layer-design)
11. [AI qualitative analysis layer (operations)](#11-ai-qualitative-analysis-layer-operations)
12. [Stance evaluation, accountability, and OKF theme curation](#12-stance-evaluation-accountability-and-okf-theme-curation)

---

## 1. Data sources

### Yahoo Finance (primary market data)

AIMS fetches daily OHLCV (open/high/low/close/volume) price history from Yahoo Finance via the `yfinance` library. [Stooq](https://stooq.com) is registered as a fallback/alternative provider using its free CSV download API.

**Symbol format:** Yahoo Finance uses its own symbol convention.
Examples: `^GSPC` (S&P 500), `^DJI` (Dow Jones), `^NDX` (NASDAQ 100), `^N225` (Nikkei 225), `^GDAXI` (DAX), `GC=F` (Gold futures).

**Limitations:**

- Daily, weekly, and monthly bars only — no intraday data.
- Symbol availability and history depth vary; some symbols return no data.
- Network access is required; fetches that fail are logged as `WARNING` and skipped.

**Configured symbols:** The daily workflow derives its symbol list from `data/mappings/canonical_instrument_mappings.csv` (see [Canonical instrument mappings](#canonical-instrument-mappings)) for the configured `--provider`/`--interval`, so the mapping file is the single source of truth for the automated universe. Add or remove instruments by editing the mapping file rather than a separate symbol list.

### Provider registry

AIMS routes market-data fetches through a provider registry defined in `src/aims/market_analysis.py`. Registered providers:

| Provider   | Supported intervals | Notes                                                       |
| ---------- | ------------------- | ----------------------------------------------------------- |
| `yfinance` | `d`, `w`, `m`       | Yahoo Finance via the `yfinance` library; default provider  |
| `stooq`    | `d`, `w`, `m`       | Free CSV download; registered fallback/alternative provider |
| `csv`      | `d`, `w`, `m`       | Reads pre-downloaded CSVs from data dir                     |

Pass `--provider <name>` to `init-fetch-status`, `fetch`, or `generate`. The default is `yfinance`.

**Adding a future provider:** Subclass `MarketDataProvider` in `src/aims/market_analysis.py`, register it in `_PROVIDER_REGISTRY` with a `ProviderMetadata` entry listing its supported intervals and any known limitations, and mirror the entry in `src/aims/mappings.py`'s `_KNOWN_PROVIDERS` and `_PROVIDER_INTERVALS`. Update the `provider` input choices in `.github/workflows/daily-market-analysis.yml`. Add the new provider to the test suite to maintain 100% coverage.

### Persistent price store

The primary provider's daily universe is kept in a persistent, multi-year OHLCV store at `data/store/` (per-symbol CSVs, same layout as `data/prices/`) instead of being refetched from scratch every run. The daily workflow restores it from a GitHub Actions cache (`actions/cache`, key `prices-store-<interval>-v1-<date>` with a prefix restore-key), updates it, and lets the cache action re-save it at the end of the job.

- **First run for a symbol:** `market_analysis.py update-store` fetches a full deep-history window (`deep_fetch_window_days`: ~10 years for daily; weekly/monthly already span years under the regular policy window).
- **Subsequent runs:** it re-fetches only the last `--overlap-days` (default 30) plus new bars, then merges with `merge_price_series`, which keeps the freshly fetched value on any overlapping date and reports **adjustment drift** — a warning when a fresh close differs from the cached one by more than 0.1% — instead of silently absorbing the rewrite (`yfinance`'s `auto_adjust=True` retroactively rewrites past closes on dividend/split events). Drift warnings and a SHA-256 content hash per symbol are written to `metadata.price_history` on the analysis artifact and are visible for any run.
- **Fetch-status contract preserved:** `update-store --fetch-status` records this run's per-symbol success/failure exactly like the old `fetch` loop did, so a symbol whose refresh failed today is reported missing by the coverage gate even though the store still holds an older cached bar for it — a stale on-disk file can never mask a current-run failure.
- **Storage placement rationale:** the store holds derived OHLCV bars only (not redistributed as a bulk dataset, not committed to the repository), matching the "derived artifacts only" policy and each provider's terms; a GitHub Actions cache is ephemeral, scoped to this repository, and not a public redistribution channel.
- **Rebuild from scratch:** delete the `prices-store-<interval>-v1-*` caches (Actions → Caches in the repository settings, or `gh cache delete` via the API) and re-run the workflow; the next run's `update-store` treats every symbol as first-time and re-fetches the full deep-history window.
- **Local backtests over deep history:** point `backtest.py --data-dir` (or `market_analysis.py generate --data-dir`) at a local copy of the store built the same way: `uv run .agents/skills/market-analysis/scripts/market_analysis.py update-store --mapping data/mappings/canonical_instrument_mappings.csv --store-dir <dir>`.

### Provider failover

If the primary provider's fetch fails the coverage gate (`generate` returns non-zero), the daily workflow retries the full fetch-and-generate cycle with the other registered provider (`FALLBACK_PROVIDER`: `stooq` when the primary is `yfinance`, and vice versa) before failing the run. The fallback fetch writes into a separate `data/prices-fallback/` directory so it never mixes with the primary provider's local cache or the persistent store. If both providers fail the coverage gate, the job fails explicitly and the failure Slack notification fires. One provider's data always fills the whole artifact — the two are never mixed for a single run.

### Cross-provider price consistency

Every Monday, the daily workflow additionally fetches the secondary provider's data (into `data/prices-secondary/`, not committed) and runs `market_analysis.py consistency`, which compares the persistent store's closes against it for canonical instruments available from both providers, over their last 5 common bars. Divergence above 0.5% is recorded as a warning; divergence above 2% is escalated. The report feeds into `generate --price-consistency`, which stores it at `metadata.price_consistency` and adds a `provider_divergence` risk gate (marking the instrument unreliable) to any escalated instrument. Escalated instruments are also called out in the Slack success notification. This check is weekly rather than daily to avoid doubling fetch volume on every run.

### CFD instrument master

The canonical list of CFD products available at supported brokers is maintained in `data/cfd_instruments.csv`. It is refreshed weekly by the `update-cfd-instruments` workflow. The daily analysis workflow validates this file before running but does not modify it.

---

## 2. Instrument master

The CFD instrument master (`data/cfd_instruments.csv`) is sourced from:

- **GMO Click Securities** (`クリック証券`) — CFD lineup pages
- **Rakuten Securities** (`楽天証券`) — CFD lineup pages

Ticker symbols in the instrument master follow each broker's own convention and do not map directly to Stooq symbols. `data/mappings/cfd_ticker_mappings.csv` contains the mapping used by the updater.

The master is validated against `data/schema/cfd_instruments.schema.json` after every update.

**Update frequency:** Weekly (Monday 05:00 UTC) via `.github/workflows/update-cfd-instruments.yml`. Changes are submitted as pull requests for review.

### Canonical instrument mappings

`data/mappings/canonical_instrument_mappings.csv` links broker CFD products and provider symbols to a stable canonical identifier and display name shown in reports.

| Column                   | Required | Description                                                  |
| ------------------------ | -------- | ------------------------------------------------------------ |
| `canonical_id`           | Yes      | Stable lowercase identifier, e.g. `spx`                      |
| `display_name`           | Yes      | Human-readable name shown in reports, e.g. `S&P 500`         |
| `asset_class`            | Yes      | `equity_index`, `equity`, `commodity`, etc.                  |
| `broker`                 | No       | Broker name; leave blank if no broker link is needed         |
| `broker_instrument_name` | No       | Broker CFD product name (used for CFD reference validation)  |
| `broker_ticker_symbol`   | No       | Broker's own ticker symbol                                   |
| `provider`               | Yes      | Data provider: `stooq` or `csv`                              |
| `provider_symbol`        | Yes      | Provider symbol, e.g. `^SPX`                                 |
| `provider_interval`      | Yes      | Bar interval: `d`, `w`, or `m`                               |
| `tradable`               | Yes      | `true` if the instrument is currently tradable at the broker |
| `notes`                  | No       | Free-form notes                                              |

Multiple rows may share a `canonical_id` — one per (provider, interval, broker) combination. A `(provider, provider_symbol, provider_interval)` triple must map to exactly one `canonical_id`.

**Validate the mapping file:**

```bash
uv run .agents/skills/market-analysis/scripts/validate_instrument_mappings.py \
    --input data/mappings/canonical_instrument_mappings.csv \
    --cfd-instruments data/cfd_instruments.csv
```

Exits 0 when clean; exits 1 on hard errors (missing columns, unknown provider, unsupported interval, duplicate key). Warnings are printed for tradable CFD entries in `cfd_instruments.csv` that have no mapping row — these are informational and do not block the run.

**Adding a new instrument:**

1. Add one or more rows to `canonical_instrument_mappings.csv` — one per provider/interval combination to analyze, plus one per broker CFD pairing. A row with `provider=yfinance` and `provider_interval=d` is picked up automatically by the daily workflow, which derives its symbol list from this file.
2. Run the validator above to confirm no errors.
3. Run `uv run pytest` to confirm 100% coverage still holds.

**Individual stocks:** Individual stocks are configured the same way as indices and commodities — through rows in `canonical_instrument_mappings.csv` with `asset_class=equity`. There is no separate stock symbol list; the daily workflow's `yfinance`/`d` universe automatically includes any stock row added to this file (e.g. `AAPL`, `MSFT`, `NVDA`). A `broker`/`broker_instrument_name` pairing is optional — leave those columns blank for stocks with no CFD broker backing (e.g. Japanese large caps not offered as CFDs by GMO Click Securities or Rakuten Securities).

**Connecting new CFD entries to canonical mappings:** After `update-cfd-instruments` adds new rows to `data/cfd_instruments.csv`, the mapping validator warns about tradable CFD entries with no mapping row. Add the corresponding canonical mapping rows to clear those warnings.

**`tradable=false` policy (#76):** Rows with no broker CFD offering (e.g. `7203.T`/`6758.T`/`8306.T` — Japanese large-caps analyzed for informational breadth) stay in the daily universe and are scored normally, but are treated as non-actionable everywhere a report or notification presents a _signal_: `generate --mapping` propagates `tradable` onto each artifact instrument (`instrument_display_map`), and both the "Top Opportunities" report section and the Slack top-signal/event lines exclude `tradable=false` instruments even when they score well. The full "Instrument Scores" table still lists them, annotated `(informational — no broker CFD)`, so the universe's breadth stays visible. Signal-persistence tracking (`data/history/`, the "Signal History" report section) is unaffected by this change and may still surface a `tradable=false` instrument's rank/score deltas.

---

## 3. Scoring methodology

AIMS scores and ranks instruments cross-sectionally using ten features computed from daily OHLCV history.

### Walk-forward backtesting

Run the scoring engine historically against saved daily prices without using future
data in each score:

```bash
uv run .agents/skills/market-analysis/scripts/backtest.py \
    --symbols "^SPX,^DJI,^NDX" --horizons 1,5,20,60
```

The deterministic JSON artifact is written to
`data/backtests/START_END_d.json`. It records the configuration, scoring version,
date range, forward-return averages by score bucket (bucket 1 is highest), top-k
average return and hit rate, top-k turnover, and the maximum drawdown of the
equal-weighted one-day top-k return series.

These results measure historical association, not causation or an executable
strategy. They exclude fees, slippage, financing, order timing, survivorship bias,
and market-impact constraints. Overlapping forward horizons are not independent;
small samples and the selected universe can materially distort results. Backtest
output is informational and is not investment advice.

### Features

| Feature             | Window            | Direction        |
| ------------------- | ----------------- | ---------------- |
| Return              | 1 day             | Higher is better |
| Return              | 5 days            | Higher is better |
| Return              | 20 days           | Higher is better |
| Return              | 60 days           | Higher is better |
| Distance from MA    | 20-day            | Higher is better |
| Distance from MA    | 50-day            | Higher is better |
| Realized volatility | 20-day annualised | Lower is better  |
| Maximum drawdown    | 60 days           | Lower is better  |
| RSI                 | 14-day            | Higher is better |
| Z-score             | 20-day            | Higher is better |

### Cross-sectional ranking

Each feature value is converted to a cross-sectional percentile rank across all instruments in the universe for that run. Features where "lower is better" are inverted (100 minus percentile). The composite score is the unweighted mean of all ten feature ranks, ranging from 0 to 100.

### Volatility-targeted sizing and ATR stop context (#83)

Each reliable instrument's artifact entry also carries a `risk_context` block — informational sizing/stop hints computed from the same fetched OHLCV bars, stored separately from `features` and never fed into `score_instruments` or risk-gate suppression:

| Field                   | Formula                                                                                                                                                                                                  |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `atr_14`                | 14-bar Average True Range (Wilder's true range, simple mean, not Wilder's smoothing), in price units                                                                                                     |
| `atr_14_pct`            | `atr_14 / latest_close`                                                                                                                                                                                  |
| `vol_target_multiplier` | `metadata.config.risk_target_annual_vol / features.vol_20d` — a notional scale factor for a configurable per-position annualized-volatility target (default 10%); `null` when `vol_20d` is `null` or `0` |
| `stop_distance`         | `metadata.config.stop_atr_multiple * atr_14` (default multiple: 2.0), in price units                                                                                                                     |
| `stop_distance_pct`     | `stop_distance / latest_close`                                                                                                                                                                           |

All five fields are `null` together when there are fewer than 15 bars (ATR needs 14 true-range observations plus the prior close); `vol_target_multiplier` is independently `null` whenever `vol_20d` is unavailable, even if ATR itself is computable. The two config values are recorded in every artifact's `metadata.config` so a report or downstream reader never has to guess which target/multiple produced a given number. Rendered in the report's "Risk Context" table with the disclaimer that this is not account-level advice, margin-call simulation, or broker integration — it ignores account size, existing exposure, and execution costs. See `data/schema/analysis.schema.json`'s `risk_context` note for the JSON shape.

### Risk gates

Instruments that fail quality checks are included in output but marked `is_reliable: false` and ranked below reliable instruments. They appear in the "Instruments to Avoid" section of the report.

| Gate                   | Trigger                                                       |
| ---------------------- | ------------------------------------------------------------- |
| `stale_data`           | Latest bar older than interval-specific `stale_days`          |
| `insufficient_history` | Fewer than `min_history` bars (default: 60)                   |
| `missing_bars`         | Gap greater than interval-specific `max_gap_days`             |
| `malformed_input`      | Non-positive prices, high < low, or price outside [low, high] |
| `high_volatility`      | 20-day annualised volatility > 100%                           |
| `missing_data`         | No price history returned for the symbol                      |

Interval-specific freshness and missing-bar thresholds are defined in `src/aims/policy.py` and recorded in each artifact under `metadata.config`:

| Interval | `stale_days` | `max_gap_days` | `min_history` |
| -------- | ------------ | -------------- | ------------- |
| `d`      | 5            | 7              | 60            |
| `w`      | 21           | 21             | 60            |
| `m`      | 62           | 62             | 60            |

### Data coverage gates

The daily workflow evaluates systemic data-source health before publishing results. Coverage statistics are stored in `metadata.coverage`; policy defaults live in `metadata.config.coverage_policy`.

| Policy                | Default | Description                                              |
| --------------------- | ------- | -------------------------------------------------------- |
| `min_success_ratio`   | `0.8`   | Minimum fraction of configured symbols with fetched data |
| `max_missing_symbols` | `1`     | Maximum allowed count of symbols with no fetched data    |

**Isolated missing symbols:** When coverage policy passes, the workflow still generates an arti…10687 tokens truncated…TC, mirroring the analysis artifact.

### Grounding rules (#90, #92)

- The model cites only from the day's committed, validated evidence bundle (`data/evidence/`, issue #90) — no browsing, retrieval, vector stores, embeddings, or external RAG services at analysis time (repository policy).
- Every driver, theme, and the market narrative carries at least one citation; citations are evidence IDs that must exist in the referenced bundle.
- Numeric statements must be reproducible from `data/analysis/` or from a cited evidence item.
- Evidence text is untrusted data: it is delimited as quoted content in the prompt, instructions inside it are content to ignore, and the validator whitelists output shape, enums, and citation targets regardless of what the model emits.
- Where evidence coverage for an instrument is thin (per-asset-class coverage accounting from #90), the prompt says so; `neutral` with few drivers is the correct output — absence of evidence must not be filled with plausible narrative.

### Deterministic gates (#93)

Schema validity is not truth. After validation, a deterministic gate pass cross-examines the structured claims against the numbers AIMS already computes, mirroring the `risk_gates` pattern: direction consistency (an `up`/`down` `direction_claim` contradicting the sign of the matching return feature, or a `none` claim contradicted by a non-trivial move in that feature, is gated — stance disagreement is never gated), numeric-claim verification within tolerance, evidence recency (aligned with `stale_days` in `src/aims/policy.py`), and citation coverage. Gated per-instrument entries are excluded from rendering; a gated market narrative withholds the whole artifact. One regeneration retry is allowed before degrading. Gate outcomes are recorded in artifact metadata so the report and Slack can say why commentary is absent. Gates are deterministic code only — no LLM-based verification.

### Runner architecture and Claude Code Action execution (#92/#138)

- **Runner:** an agent skill at `.agents/skills/qualitative-analysis/` whose scripts are thin wrappers delegating to `src/aims/qualitative.py`, the same pattern as `market-analysis/scripts/`. It runs in the daily workflow after the "Validate artifact" step (#95).
- **Model execution:** `anthropics/claude-code-action` is pinned to a full commit SHA and receives `CLAUDE_CODE_OAUTH_TOKEN`. Automation mode uses `--tools ""`, so Claude has no repository read/write, shell, or GitHub mutation tools; all necessary committed inputs are embedded by the deterministic prepare stage. Claude Code's `--json-schema` produces `structured_output`, which is still treated as untrusted and rechecked by the hand-written validator and grounding gates before persistence. Python performs no model network call and has no Anthropic SDK dependency.
- **Model:** `claude-opus-4-8`, pinned in code and recorded in artifact metadata alongside the prompt version. The prompt is a committed file; changing it or the model requires the #97 regression harness once that exists. Current Claude models accept no sampling parameters (`temperature` is rejected), so run-to-run reproducibility rests on committed inputs, structured outputs, deterministic gates, and committing a single validated artifact per date — not on a temperature setting.
- **Caps:** one call per run; input capped by the evidence bundle's per-instrument item caps and length-capped snippets (#90); output capped via `max_tokens`; request timeout and a single retry (which is also the #93 regeneration retry).

### OAuth handling and subscription quota (#95/#138)

`CLAUDE_CODE_OAUTH_TOKEN` is optional and comes from `claude setup-token` under the operator's Claude Pro/Max subscription. When absent, every qualitative step is skipped. Runs consume the subscription's shared usage allowance rather than API credits; limits vary by plan and concurrent Claude usage. A limit failure is fail-open and should be retried only after the allowance resets. Generation, repository-secret setup, rotation, and revocation are documented in §6.

### Rollout: shadow mode before rendering (#95, then #94)

Daily analysis PRs auto-merge with no human review (#75), so schema validation and the #93 gates are the only pre-publication defenses for LLM output. Rendering is therefore staged:

1. **Shadow mode (#95):** evidence and qualitative artifacts are generated, validated, gated, and committed in the daily analysis PR, but `generate_report.py` is not passed `--qualitative`. Published reports stay byte-identical to today's.
2. **Exit criteria** (tracked on #98): at least 10 consecutive scheduled runs with zero schema/validator failures, a market-narrative gate pass rate of at least 80%, and a human spot-review of the committed artifacts recorded on #98.
3. **Enable rendering (#94):** a default-off repository variable (e.g. `AI_COMMENTARY_ENABLED`) flips `--qualitative` on. The flip is a reviewed change recorded against #98's checklist, not a silent default. AI commentary renders in an explicitly labeled section with citations, model/prompt provenance, and the financial disclaimer adjacent.
4. **Go/no-go checkpoint** (tracked on #98): after roughly one quarter of enabled rendering, review stance hit rates and calibration (#97), gate withhold rates, and subscription quota reliability; continue, adjust, or retire the layer.

### Non-goals

No investment advice or trading automation; no vector databases, embeddings pipelines, external RAG services, custom CMS layers, or server-side runtimes; no AI modification of scores, ranks, gates, or regime labels; no LLM-based verification of LLM output.

---

## 11. AI qualitative analysis layer (operations)

Operational reference for the implemented layer (#90–#95). The binding design contract is [§10](#10-ai-qualitative-analysis-layer-design); the runner is the `qualitative-analysis` agent skill (`.agents/skills/qualitative-analysis/`).

### Evidence sources

`data/mappings/evidence_sources.csv` is the curated macro feed list: `source_id`, `name`, `url`, `category`, and pipe-separated `asset_classes` the feed applies to. Per-symbol news comes from yfinance for every instrument in the canonical mapping. Both source classes are normalized into `data/evidence/<stem>.json` (schema: `data/schema/evidence.schema.json`): stable `ev-<hash>` IDs, stripped markup, length-capped titles/snippets, at most 5 items per instrument and 10 per macro feed, all within a 7-day lookback of the analysis date.

**Adding a feed:** append a row to `evidence_sources.csv` with a stable `source_id`, the RSS/Atom URL, a category, and the asset classes it informs; verify it parses with a local `fetch_evidence.py` run. Feeds must be official/primary sources (central banks, statistical agencies, official energy data) — no scraping, no paywalled content. A dead feed is non-fatal: it appears as `status: failed` under `metadata.coverage.sources` in each bundle; remove or fix the row when a feed fails persistently. (BLS is intentionally absent: `bls.gov` blocks non-browser clients.)

**Coverage asymmetry is expected:** equities get direct yfinance news; indices and commodities rely mostly on macro feeds. `metadata.coverage.asset_classes` records the asymmetry per bundle so the #92 prompt can be honest about which instruments have direct evidence.

**Retention policy:** evidence bundles are small (tens of KB) and accumulate one per scheduled run under `data/evidence/`. Keep at least 400 days so the #97 evaluation loop can join stances with realized forward returns. Prune older bundles manually via a reviewed PR (`git rm data/evidence/<old>.json`); never prune `data/qualitative/` artifacts that still reference a bundle you are deleting.

### Calendars

Two schema-validated files under `data/calendars/` (schema: `data/schema/calendar.schema.json`) drive the deterministic "Upcoming Events" report section, the Slack event lines, and the #92 prompt context:

- **`macro_events.json`** — central-bank decision dates (FOMC, ECB, BOJ), refreshed weekly from official institution schedules through a reviewed PR. The updater records each meeting's final day, filters past dates, and fails closed if a source returns too few events. **Correcting a wrong date:** update the parser or source mapping with tests in a reviewed PR; the next refresh uses the official dates.
- **`earnings.json`** — per-equity earnings dates fetched from yfinance, refreshed weekly by `update-calendars.yml` (Mondays 05:30 UTC) through an auto-created PR. Dates are provider estimates and can shift; the weekly refresh converges on the confirmed date.

Events tag instruments via `canonical_ids` and/or `asset_classes`; rendering windows are relative to the analysis date (7 days in reports/Slack by default, 14 days in the qualitative prompt), so output stays deterministic.

### Qualitative gates and degradation policy

`aims.qualitative_gates.apply_gates` runs after `validate_qualitative.py` and records outcomes in the artifact (`metadata.gates`, per-instrument `qualitative_gates`). All gates operate on structured claim fields, never prose:

| Gate                     | Checks                                                                                                    | Threshold                                                                                         |
| ------------------------ | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `direction_inconsistent` | Each `direction_claim` against the sign of the matching return feature (`1d/5d/20d/60d` → `ret_*`)        | `up`: feature > 0; `down`: feature < 0; `none`: abs(feature) ≤ 0.01; missing feature fails        |
| `numeric_claim_mismatch` | Each `numeric_claims` entry against the referenced quantitative feature or cited evidence item's text     | percent units: ±0.5pp on the fraction scale; otherwise ±max(5% relative, 0.01)                    |
| `stale_evidence`         | Entries may not rest solely on evidence older than the staleness cutoff                                   | at least one citation newer than `analysis_date − stale_days` (from `metadata.config`, default 5) |
| `citation_coverage`      | Every driver (and the narrative and each theme) must carry at least one citation resolvable in the bundle | coverage ratio ≥ 1.0                                                                              |

**Degradation policy:** a gated instrument entry is excluded from rendering while the rest of the artifact still renders; a gated market narrative withholds the whole artifact from rendering (the quantitative report publishes unchanged). The runner allows exactly one regeneration retry when the market narrative is gated, then commits the gated artifact for shadow-mode measurement. A `conflicting` stance is never gated for the disagreement itself.

### Shadow mode, rendering switch, and cost

Shadow mode is the default state: with `CLAUDE_CODE_OAUTH_TOKEN` set, the daily PR carries analysis, history, evidence, and qualitative artifacts while the published report stays byte-identical to a quantitative-only run. Rendering is controlled by the `AI_COMMENTARY_ENABLED` repository variable ([§6](#6-github-actions-secrets)) plus the `ai_commentary` dispatch input; the `skip_qualitative` input disables the qualitative steps for a single run.

Quota controls: one Claude Code Action invocation per run, plus at most one regeneration retry; top-K evidence bounds the prompt and `--max-turns 1` prevents open-ended agent loops. The action has no tools. Both invocations use the pinned model and subscription OAuth allowance. Changing the model or committed prompt requires the §12 regression harness.

---

## 12. Stance evaluation, accountability, and OKF theme curation

Phase 4 of the roadmap (#98): measure whether AI commentary adds information, guard prompt/model changes, and promote durable themes into the knowledge layer. Everything here is deterministic, dependency-light, and reuses the existing schema-validator and skill-wrapper patterns. **None of it asserts an investable or executable track record** — outputs frame informational association only, with disclaimers kept prominent.

> **Disclaimer:** Stance-evaluation figures measure whether published AI stances lined up with subsequent price moves in committed data. They are not an investable or executable track record, exclude fees/slippage/financing/order timing, rest on small overlapping samples, and are not investment advice.

### Stance evaluation (#97)

`evaluate_stances.py` (delegating to `src/aims/performance.py`) joins per-instrument stances from committed `data/qualitative/*.json` artifacts with realized forward returns and writes the schema-validated `data/performance/<date>.json` artifact plus the public `content/evaluation/_index.md` page. It runs in the daily workflow after score history (daily interval only).

- **Forward returns without price fetches.** Returns are reconstructed by chaining each symbol's trailing `ret_1d` feature across analysis artifacts, keyed by the per-symbol bar date in `metadata.data_freshness`. Weekend/holiday artifacts that repeat a bar collapse into one entry. The chain self-checks against any later `ret_5d` feature (compounded trailing-five product must match within `return_consistency_tolerance`); a window that fails is skipped as `broken_chain`, never scored with wrong numbers. This keeps the evaluator deterministic and consistent with the quantitative source of truth instead of introducing a parallel price store.
- **Hit definition.** `supportive` hits when the forward return is positive; `conflicting` hits when it is negative (a conflicting stance on a top-ranked instrument predicting underperformance); `neutral` is tracked but never scored directionally. Per horizon (default 1d/5d/20d): stance counts, hit rates, average returns, and confidence calibration (hit rate of directional stances grouped by stated confidence — higher confidence should mean higher hit rate).
- **Gating and empty state.** Stances withheld by the #93 gates are excluded (`excluded_gated`); stances without a matching chained bar are `unmatched`; stances newer than a horizon are `pending` and mature in later runs. With no qualitative artifacts on `main` yet, the artifact and page render a safe empty state with a warning rather than fabricated numbers — the committed `data/performance/2026-07-04.json` and `content/evaluation/_index.md` are exactly that empty state and fill in as artifacts accumulate. Format reference: `data/schema/performance.schema.json`.
- **Trust boundary for the same-run qualitative artifact.** The "Run qualitative analysis (shadow mode)" step is `continue-on-error`, so `data/qualitative/<stem>.json` can exist on disk for today's date even after a failed or unvalidated run — the same condition that already keeps report rendering and Slack notification from trusting it (`steps.qualitative.outcome == 'success'`). `evaluate_stances.py` extends the same boundary: the workflow passes `--exclude-qualitative-date "${DATE}"` whenever `steps.qualitative.outcome != 'success'`, so that date is excluded from the join (recorded as a warning in the artifact) regardless of whether the file is present, while every historical, already-validated qualitative artifact on `main` is still evaluated normally.
- **Slack.** When present, `notify_slack.py --performance` appends a trailing `AI stance hit rate:` line (blended supportive+conflicting per horizon); it is omitted until matured observations exist.

### Prompt/model regression harness (#97)

A prompt edit or model swap can silently change output quality with no code diff. `prompt_regression.py` (in `src/aims/prompt_regression.py`) recomputes the validator and the #93 gates over a `(qualitative, analysis, evidence)` triple and asserts **structural and gate metrics** — validator cleanliness, market-narrative rendering, instrument gate pass rate (≥ 0.6), citation coverage (= 1.0), and stance-distribution sanity — **never exact prose**, so wording changes alone cannot fail it. Results are recorded in `data/performance/prompt_regressions.json` keyed by the prompt file's SHA-256 and the pinned model ID (schema: `data/schema/prompt_regression.schema.json`).

**Before adopting any change to `prompts/qualitative_v1.md`, `PROMPT_VERSION`, or `MODEL_ID`:** run the harness (over freshly generated candidate artifacts, or the committed fixtures without an OAuth run) with `--record data/performance/prompt_regressions.json` and commit the updated file. A CI test (`tests/test_prompt_regression.py::test_committed_prompt_and_model_have_a_recorded_passing_entry`) fails when the committed prompt/model has no recorded passing entry, so an unreviewed prompt change cannot merge. There is **no automatic prompt tuning or optimization loop** — the harness measures and records; adoption stays a reviewed human decision. See the `qualitative-analysis` skill doc for the exact command.

### Citation link-rot sampling (#97)

`check_citation_links.py` (in `src/aims/link_check.py`) probes a bounded, deterministic sample of recent evidence citation URLs over HTTP (HEAD, falling back to GET) so dead sources surface in the workflow log. It is **a warning, not a gate**: it always exits 0, writes no artifact (network results are non-deterministic and stay out of committed data), and runs `continue-on-error` in the daily workflow. Persistent rot on a source means editing or removing its row in `data/mappings/evidence_sources.csv` per [§11](#11-ai-qualitative-analysis-layer-operations).

### OKF theme curation (#96)

Durable themes surfaced by the daily qualitative artifacts belong in the OKF knowledge layer, not the point-in-time reports. `curate_themes.py` (in `src/aims/okf_curation.py`, behind the `aims-okf-curator` skill) runs a **monthly** deterministic pass over `data/qualitative/*.json`: it clusters recurring theme titles by token overlap, prints promotion candidates that recur on **≥3 distinct dates spanning ≥14 days** (with dated artifact and evidence citations plus a ready-to-edit concept skeleton), lists supporting per-instrument stance streaks, and flags retirement candidates among existing `qualitative-theme`-tagged concepts (unseen for **>60 days**).

Its output is a **proposal for human review only** — it never writes to `okf/`. Promotion and retirement follow the standard OKF flow: edit a draft into `okf/concepts/theme-<slug>.md` (carry the `qualitative-theme` tag and a `theme_tokens` front-matter list so future passes assess recurrence; cite dated artifacts; numeric facts stay pointers into `data/analysis/` and are never asserted as truth in prose), record the pass — including "no promotions" — in `okf/logs/log.md`, regenerate shadow content (`tools/okf_hugo_adapter.py --clean` then `--check`), build with `hugo --gc --minify`, and open a reviewed PR. **OKF changes are never auto-merged.** Cadence and criteria are documented in `.agents/skills/aims-okf-curator/SKILL.md`.

**Current state (accumulation limitation):** shadow mode has not yet committed qualitative artifacts to `main`, so both the stance-evaluation artifact and the first curation pass are recorded empty states. The machinery, schemas, fixtures, and tests are complete; the "at least one promoted theme" and populated evaluation-summary milestones fill in once artifacts accumulate. This limitation is recorded rather than worked around.

### Go/no-go checkpoint (#98)

After roughly one quarter of enabled rendering, review this section's stance hit rates and confidence calibration, gate withhold rates, and subscription quota reliability, then record a continue / adjust / retire decision on issue #98. A layer that measures as plausible-sounding noise is retired, not maintained.
