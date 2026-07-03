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
10. [AI qualitative analysis](#10-ai-qualitative-analysis)

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

**Isolated missing symbols:** When coverage policy passes, the workflow still generates an artifact and marks affected instruments with the `missing_data` risk gate. One missing symbol out of five configured symbols (80% success ratio) is within policy.

**Systemic data-source failure:** When coverage policy fails (too many missing symbols, success ratio below threshold, empty symbol universe, or all symbols failed), the `generate` step may write a diagnostic JSON artifact with `metadata.coverage.passed: false`, then exits with a non-zero status. The automated workflow stops before artifact validation, Hugo report generation, pull-request creation, and Slack success notification. Diagnostic artifacts are for local inspection only — do not validate or publish them manually. The failure Slack notification still links to the GitHub Actions run.

**Artifact validation contract:** `validate_analysis.py` accepts `metadata.coverage.passed: false` as structurally valid JSON. Publication safety comes from the workflow gate: `generate` must exit `0` before validation, report generation, or PR creation run. Only artifacts with `coverage.passed: true` reach the public pipeline.

Override coverage gates locally or in manual workflow runs via `market_analysis.py generate --min-success-ratio` and `--max-missing-symbols`, or through the `workflow_dispatch` inputs of the same name (defaults: `0.8` and `1`).

**Current-run fetch status:** The daily workflow initializes `data/prices/fetch_status_<interval>.json` before fetching, records per-symbol success or failure during each `fetch` call, and passes that file to `generate --fetch-status`. Coverage gates use this fetch-status file as the source of truth, not merely the presence of pre-existing local price CSVs. A stale on-disk price file cannot mask a failed fetch in the current run. `generate` rejects fetch-status files whose `interval` or `analysis_date` do not match the current run.

### Market regime

The market regime label is derived from breadth: the share of reliable instruments whose latest close is above their 20-day moving average. Percentile-based composite scores are relative by construction — their median stays near 50 for any universe of meaningful size regardless of market direction — so breadth is used as an absolute directional measure instead. Reliable instruments without MA20 data are excluded from the ratio.

| Label       | Share above MA20                       |
| ----------- | -------------------------------------- |
| Bullish     | ≥ 65%                                  |
| Neutral     | > 35% and < 65%                        |
| Bearish     | ≤ 35%                                  |
| Unavailable | No reliable instruments with MA20 data |

### Scoring version

`SCORING_VERSION = "1.0.0"` in `src/aims/market_analysis.py`. Increment this when the feature set or scoring logic changes in a way that makes old and new scores incomparable.

### Assumptions and limitations

- Scores are cross-sectional: they reflect relative, not absolute, performance. A score of 80 in a falling market still means that instrument fell less than most others.
- Volatility and drawdown are historical. They do not predict future risk.
- Missing or stale data can distort percentile ranks when the universe is small.
- Short history (< 60 bars) triggers the `insufficient_history` gate and excludes an instrument from reliable rankings.
- Score/rank deltas in `data/history/` and the Signal History report section compare each instrument only against the most recent prior report. If the analyzed instrument universe changes between reports (e.g. a mapping addition or removal), deltas reflect both genuine market moves and the change in cross-sectional population, and should be interpreted with care until the universe is stable across both dates.

---

## 4. Report generation

### Script

```sh
uv run .agents/skills/market-analysis/scripts/generate_report.py \
    --input data/analysis/YYYY-MM-DD.json \
    --output content/results/
```

The script reads the JSON artifact produced by `market_analysis.py generate` and writes a Hugo-compatible Markdown file to `content/results/YYYY-MM-DD-market-analysis.md`.

Before report generation, `generate_history.py` reads the current and all earlier
available `data/analysis/YYYY-MM-DD.json` files and writes the deterministic,
versioned `data/history/YYYY-MM-DD.json` artifact. Version 1.0.0 records previous
rank/score, deltas (positive rank delta means improvement), new and dropped top-5
signals, consecutive reliable and top-5 available-report counts, and added/removed
risk gates. Missing calendar dates are intentionally ignored. The format reference
is `data/schema/history.schema.json`; candidates with a different configured bar
interval are excluded, and numeric history remains separate from OKF.

### Output format

The report includes:

- TOML front matter: title, date, draft status, summary, ticker symbols, market regime, scoring metadata
- Market regime section
- Top opportunities (up to 5 reliable instruments)
- Changes versus the previous available report and persistent top signals
- Instruments to avoid (unreliable instruments)
- Key risks (triggered risk gates)
- Full instrument scores table
- Data freshness table (per-symbol latest bar date)
- Methodology summary
- Financial disclaimer

### Determinism

The generator is fully deterministic: identical input JSON always produces identical Markdown output. It does not call `datetime.now()` and uses only the `generated_at` timestamp from the artifact.

### Draft status

`draft = false` is set in all generated reports. Draft reports can be created manually using `hugo new results/YYYY-MM-DD-description.md`.

---

## 5. Publication workflow

### Daily schedule

`.github/workflows/daily-market-analysis.yml` runs at **01:00 UTC** every day.

Pipeline order:

1. Validate CFD instrument master
2. Set analysis date (default: today UTC)
3. Load symbols from `data/mappings/canonical_instrument_mappings.csv` for the configured `--provider`/`--interval` (the mapping file is the single source of truth; there is no separate `data/*_symbols.txt` file to keep in sync)
4. Initialize `data/prices/fetch_status_<interval>.json` and fetch market data from the configured provider (1-year lookback), recording per-symbol outcomes in fetch status
5. Generate JSON analysis artifact (`data/analysis/YYYY-MM-DD.json`) using `--mapping` and `--fetch-status`; fail if coverage gates are violated. Each instrument entry is enriched with `canonical_id`, `display_name`, and `asset_class` from the mapping.
6. Validate artifact
7. Generate score history (`data/history/YYYY-MM-DD.json`)
8. Generate Hugo Markdown report (`content/results/YYYY-MM-DD-market-analysis.md`), grouped by asset class when the artifact carries more than one
9. Build Hugo site (validation only — catches template or content errors before commit)
10. Create (or update) a pull-request branch `generated/analysis-YYYY-MM-DD` with both artifacts and the report, then enable GitHub auto-merge (squash, delete branch on merge) on that PR
11. A Slack notification summarizes new/persistent signals and risk-gate changes and links to the analysis PR.

### Auto-merge and CI approval

Step 10 calls `gh pr merge --auto --squash --delete-branch`, which merges the PR automatically once its required status checks pass — it does not bypass branch protection or required reviews. This requires **"Allow auto-merge"** to be enabled in **Settings → General → Pull Requests**; if it is not enabled, the step logs a warning and the PR falls back to manual merge exactly as before.

**Known gotcha — PRs stuck in `action_required`:** pull-request-triggered `ci.yml` runs on `generated/analysis-*` branches can be gated with conclusion `action_required` and zero jobs executed, even though the PR was opened by `github-actions[bot]` pushing to a branch in the same repository (not a fork). When this happens, `gh pr merge --auto` waits indefinitely because the required checks never run. A repository maintainer must approve the pending workflow run (Actions tab → the run → **Approve and run**) or re-run it; only an authorized human/maintainer token can do this, the workflow's own `GITHUB_TOKEN` cannot self-approve. If this recurs daily, check **Settings → Actions → General** for an approval requirement (e.g. "Require approval for all outside collaborators") that is being applied to `github-actions[bot]`-authored pull requests, and relax it only if the operational risk is acceptable.

### Manual dispatch

The workflow supports `workflow_dispatch` with optional inputs:

| Input                 | Default    | Description                                                                                       |
| --------------------- | ---------- | ------------------------------------------------------------------------------------------------- |
| `analysis_date`       | Today UTC  | Override the analysis date (YYYY-MM-DD)                                                           |
| `interval`            | `d`        | Price bar interval: `d` (daily), `w` (weekly), `m` (monthly)                                      |
| `dry_run`             | `false`    | When `true`, skips PR creation, auto-merge, and Slack success notification                        |
| `min_success_ratio`   | `0.8`      | Minimum symbol fetch success ratio for coverage gate                                              |
| `max_missing_symbols` | `4`        | Maximum allowed missing symbols for coverage gate (scaled for the ~20-instrument mapped universe) |
| `provider`            | `yfinance` | Market data provider: `yfinance` or `stooq`                                                       |

### Deployment gate

GitHub Pages deployment is handled by `ci.yml` (`hugo-deploy-to-gh-pages` job), which runs only after Python linting, type checking, and tests all pass. The daily analysis workflow commits only content files (JSON and Markdown), not Python source, so existing tests remain stable.

### Rollback

If a published report or artifact needs to be removed, see [Delete a published report](#delete-a-published-report) in Manual recovery. Reverting a bad _code_ change (as opposed to a bad daily _report_) is a normal `git revert` on `main`, gated by the same CI checks as any other change.

---

## 6. GitHub Actions secrets

| Secret              | Required | Description                                                                                                                                      |
| ------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `SLACK_WEBHOOK_URL` | Optional | Slack incoming webhook URL for success and failure notifications. If not set, the workflow skips Slack notification steps.                       |
| `ANTHROPIC_API_KEY` | Optional | Claude API key for the AI qualitative analysis step. If not set, the qualitative steps are skipped and the pipeline behaves exactly as before.   |
| `GITHUB_TOKEN`      | Built-in | Used automatically by `gh` and `git push` in the `update-cfd-instruments` and `daily-market-analysis` workflows. No manual configuration needed. |

**How to add `SLACK_WEBHOOK_URL`:** Go to the repository → Settings → Secrets and variables → Actions → New repository secret. Name: `SLACK_WEBHOOK_URL`. Value: the `https://hooks.slack.com/services/…` URL from your Slack app's Incoming Webhooks configuration.

**Never commit secret values.** The `notify_slack.py` script reads `SLACK_WEBHOOK_URL` only from the environment.

---

## 7. Required permissions

The `daily-market-analysis.yml` workflow uses:

| Permission             | Scope                  | Reason                                      |
| ---------------------- | ---------------------- | ------------------------------------------- |
| `contents: write`      | `analyze` job          | Create and push to analysis branch; open PR |
| `pull-requests: write` | `analyze` job          | Create analysis pull requests               |
| `contents: read`       | Workflow-level default | Checkout                                    |

The `ci.yml` workflow adds:

| Permission        | Scope                         | Reason                          |
| ----------------- | ----------------------------- | ------------------------------- |
| `id-token: write` | `hugo-deploy-to-gh-pages` job | OIDC token for Pages deployment |
| `pages: write`    | `hugo-deploy-to-gh-pages` job | Deploy to GitHub Pages          |

---

## 8. Troubleshooting

### Fetch failed for symbol

```
ERROR: fetch failed for ^SPX
```

The data provider may be temporarily unavailable or the symbol may be invalid. Per-symbol fetch failures are non-fatal — a `WARNING` is logged and the fetch loop continues. The symbol is passed to the `generate` step which marks it as `missing_data` in the artifact and report when coverage policy still passes. The workflow fails before publishing when coverage gates detect a systemic data-source failure (too many missing symbols or success ratio below threshold). It also fails when no symbols at all can be fetched.

**Fix:** Check `data/mappings/canonical_instrument_mappings.csv` for typos in `provider_symbol`. Verify the symbol on the provider's site (e.g. https://finance.yahoo.com or https://stooq.com). Remove permanently unavailable rows to keep the analysis clean. Re-run the workflow after the data source recovers.

### Artifact validation failure

```
ERROR: instrument[0] missing required key: 'symbol'
```

The generated JSON does not match the expected schema. This usually means a bug in `src/aims/market_analysis.py`.

**Fix:** Run the generate step locally, then run `validate_analysis.py` with `--input` to reproduce the error.

### Hugo build failure

```
Error: ... template: ...
```

A generated Markdown file has invalid front matter or content that causes Hugo to fail.

**Fix:** Run `hugo --gc --minify` locally with the failing content file, fix the generator, and regenerate.

### Mapping validation errors

```
ERROR: row 5: unknown provider 'bloomberg'; known: csv, stooq
WARNING: CFD instrument ('TestBroker', 'US30') has no canonical mapping entry
```

Run `validate_instrument_mappings.py` locally to see all errors before committing. Common causes:

- **Unknown provider:** only `stooq` and `csv` are registered. Add the provider to `_PROVIDER_REGISTRY` before using it in a mapping.
- **Broker/instrument not found in cfd_instruments.csv:** the CFD product has not been fetched yet. Run `update-cfd-instruments` first, or leave the broker columns blank to skip the reference check.
- **Duplicate provider mapping:** two different `canonical_id` values claim the same `(provider, provider_symbol, provider_interval)` triple. Each provider symbol/interval combination must map to exactly one canonical instrument.
- **Unmapped tradable CFD warning:** a tradable entry in `cfd_instruments.csv` has no row in `canonical_instrument_mappings.csv`. Add a mapping row or accept the warning as informational.

### Stale data warning

Reports include a freshness table. Symbols with `n/a` in the freshness column had no data returned from Stooq. Symbols with old dates may be delisted or have restricted access.

### 100% test coverage requirement

All implementation modules under `src/aims/` are included in the pytest coverage check. If you add new code paths to `src/aims/`, add corresponding tests.

---

## 9. Manual recovery

### Re-run the daily workflow

Trigger it from **Actions → Daily market analysis → Run workflow** with the desired `analysis_date`. Use `dry_run = true` to test fetch, scoring, and artifact generation without opening a pull request or sending a success Slack notification.

### Recover from a coverage gate failure

1. Inspect the failed GitHub Actions run log for `ERROR: coverage gate failed` messages and the saved artifact (if generated locally).
2. Verify data-provider availability and symbol validity in `data/mappings/canonical_instrument_mappings.csv`.
3. Re-run the workflow manually once the data source has recovered.
4. For temporary outages affecting multiple symbols, wait for recovery rather than lowering coverage thresholds in automation.

### Re-fetch data for a symbol

```sh
uv run .agents/skills/market-analysis/scripts/market_analysis.py \
    fetch --symbol ^SPX --start 2023-01-01 --end 2024-12-31
```

### Regenerate an artifact from saved data (explicit symbols)

```sh
uv run .agents/skills/market-analysis/scripts/market_analysis.py \
    generate --symbols "^SPX,^DJI,^NDX" --output data/analysis/ \
    --analysis-date YYYY-MM-DD
```

### Regenerate an artifact using canonical mapping

```sh
uv run .agents/skills/market-analysis/scripts/market_analysis.py \
    generate --mapping data/mappings/canonical_instrument_mappings.csv \
    --provider stooq --interval d --output data/analysis/ \
    --analysis-date YYYY-MM-DD
```

`--mapping` and `--symbols` are mutually exclusive. With `--mapping`, the symbol list is derived from the mapping file for the given `--provider` and `--interval`, and each instrument entry in the artifact is enriched with `canonical_id` and `display_name`. Reports render these as "Display Name / symbol" (e.g. "S&P 500 / ^SPX").

### Regenerate a report from an existing artifact

```sh
uv run .agents/skills/market-analysis/scripts/generate_report.py \
    --input data/analysis/2024-01-01.json \
    --output content/results/
```

### Send a test Slack notification

```sh
SLACK_WEBHOOK_URL="https://hooks.slack.com/services/..." \
uv run .agents/skills/market-analysis/scripts/notify_slack.py \
    --artifact data/analysis/2024-01-01.json \
    --report-url https://dceoy.github.io/aims/results/2024-01-01-market-analysis/
```

### Delete a published report

1. Delete `content/results/YYYY-MM-DD-market-analysis.md` and `data/analysis/YYYY-MM-DD.json`.
2. Commit and push to `main`.
3. CI will rebuild and redeploy without the deleted report.

### Refresh CFD instruments manually

Trigger **Actions → Update CFD instruments → Run workflow**.

---

## 10. AI qualitative analysis

The qualitative layer enriches daily reports with grounded AI analysis of news, earnings, disclosures, and macro events. The quantitative pipeline (sections 1–5) remains the sole source of deterministic market scores; the AI never modifies scores, ranks, risk gates, or the market regime.

### Design contract

- **Artifacts, not prose.** The Claude API call in `src/aims/qualitative.py` is the single non-deterministic step in the pipeline. It writes `data/qualitative/YYYY-MM-DD.json` (schema reference: `data/schema/qualitative.schema.json`); validation, gating, and report rendering are deterministic given that file. Artifacts record the model id, `PROMPT_VERSION`, and SHA-256 hashes of the analysis artifact and evidence bundle they were produced from.
- **Evidence-first grounding.** The model may cite only from the committed evidence bundle — no browsing at analysis time. Fabricated citation ids are dropped at assembly and instruments outside the analysis universe are discarded, so hallucinated references become gated content instead of published claims.
- **Fail-open.** When `ANTHROPIC_API_KEY` is absent, `skip_qualitative` is set, or any qualitative step fails, the daily workflow logs a warning, removes partial outputs, and publishes the quantitative-only report unchanged. Quantitative coverage gates are never affected.
- **Repository policy.** No vector databases, embeddings pipelines, external RAG services, or server-side runtimes.

### Evidence bundles

`.agents/skills/qualitative-analysis/scripts/fetch_evidence.py fetch` collects per-instrument news via `yfinance` for every mapped instrument plus curated institutional feeds listed in `data/mappings/evidence_sources.csv` (columns: `name,url,category`), and writes `data/evidence/YYYY-MM-DD.json` (schema: `data/schema/evidence.schema.json`).

- Evidence ids are the first 16 hex characters of the SHA-256 of `<url>|<published_at>`, stable across runs.
- Items are markup-stripped, capped (titles 300 chars, summaries 500 chars, 10 items per symbol, 20 per feed), deduplicated, and recency-filtered (`--max-age-days`, default 7).
- Per-source fetch outcomes are recorded in `metadata.coverage`, mirroring the price fetch-status pattern, so a dead feed is visible rather than silently shrinking the bundle.
- **Trust boundary:** the feed list is a curated allowlist of official institutional sources. Evidence text is untrusted data — stored and cited, never interpreted as instructions. To add a feed, append a row to `evidence_sources.csv` (RSS 2.0 and Atom are supported) and keep the list limited to official sources.
- Items without a parseable publication timestamp are dropped; recency gating needs real timestamps.
- **Retention:** `data/evidence/` accumulates one file per analysis date alongside `data/analysis/`. Prune old bundles together with their analysis artifacts if repository size becomes a concern; evaluation only needs the qualitative artifacts and prices.

### Event calendars

`data/calendars/` holds known-in-advance events (schema: `data/schema/calendar.schema.json`):

- `macro_events.json` — curated from officially published schedules (FOMC etc.). Update it by hand from the sources recorded in each entry's `source_url`; use the decision/announcement day for multi-day meetings.
- `earnings.json` — generated by `update_calendars.py fetch-earnings` from `yfinance` for `asset_class=equity` mapping rows (default horizon 120 days). The daily workflow refreshes it before report generation; refresh failures fall back to the committed file.

The report renders an "Upcoming Events" section (default window: 7 days from the analysis date) and flags top opportunities with imminent events; the Slack notification lists events affecting top-5 signals. A wrong date is corrected by editing the calendar file and regenerating the report. If any calendar file fails validation, the workflow omits the Upcoming Events section for that run instead of failing.

### Qualitative artifact and grounding gates

`generate_qualitative.py` builds a structured prompt (quantitative artifact + evidence bundle + upcoming events, each delimited as data), forces a schema-constrained tool response at temperature 0, and assembles the artifact. Contract validation (`validate_qualitative.py`) rejects unknown instruments, out-of-enum stances/confidences, over-length texts, and citations missing from the bundle; one retry is attempted before the step fails (fail-open in the workflow).

Deterministic grounding gates then cross-examine the surviving content and are recorded per entry (mirroring `risk_gates`):

| Gate                     | Trigger                                                                                         |
| ------------------------ | ----------------------------------------------------------------------------------------------- |
| `uncited_claims`         | A driver, theme, or the narrative has no surviving citations                                    |
| `stale_evidence`         | Every cited item is older than the freshness window (default 5 days, aligned with `stale_days`) |
| `numeric_claim_mismatch` | A percentage claim matches neither the instrument's features nor any cited evidence text        |
| `direction_conflict`     | Direction words (rallied/fell/…) contradict the sign of `ret_5d` and `ret_20d`                  |

Gated entries are excluded from rendering while the rest of the artifact still publishes; a fully gated narrative renders as "withheld by grounding gates" with the gate names. Gate outcomes are summarized in `metadata.gates`.

### Report and Slack rendering

`generate_report.py --qualitative … --calendar-dir …` renders the "AI Market Commentary" section: explicitly labeled AI-generated, showing model id and prompt version, with numbered citations linking to sources. Without these inputs the report output is byte-identical to the quantitative-only generator. The front matter gains `ai_commentary = true/false` when a qualitative artifact is supplied. `notify_slack.py --qualitative … --calendar-dir …` adds one bounded stance-summary line and an upcoming-events line.

### Workflow behavior and cost

The daily workflow runs the qualitative steps only when the `ANTHROPIC_API_KEY` repository secret is configured and the `skip_qualitative` dispatch input is not set. A typical run sends roughly 10–40k input tokens (universe of ~20 instruments plus a capped evidence bundle) and receives up to 3,072 output tokens — on the order of a few US cents per day with the default model; verify against current pricing at https://docs.anthropic.com/en/docs/about-claude/pricing when changing models. Cost controls: capped evidence bundle, `--max-tokens`, request timeout, and a single retry.

### Evaluation and prompt changes

- `evaluate_qualitative.py evaluate` deterministically joins ungated stances with realized forward returns from `data/prices/` (hit = supportive entries at/above the cross-sectional median forward return of evaluated entries, conflicting below it; neutral excluded) and writes `data/performance/qualitative_evaluation.json` with per-horizon hit rates and confidence calibration. This measures informational association, not an executable track record.
- `evaluate_qualitative.py check-links` samples cited URLs from the latest bundle and warns (never fails) on link rot.
- Any change to the system prompt or tool schema must bump `PROMPT_VERSION` in `src/aims/qualitative.py` and pass the prompt regression tests (`tests/test_qualitative_prompt_regression.py`) before adoption.

### Troubleshooting and manual recovery

- **Qualitative step failed in the daily run:** the run log shows the failing sub-step (evidence fetch, evidence validation, generation, or artifact validation). The report for that day is quantitative-only; no action is required. To backfill, regenerate manually (below) and open a PR.
- **Regenerate a qualitative artifact for a past date:**

  ```sh
  DATE=2026-07-02
  uv run .agents/skills/qualitative-analysis/scripts/fetch_evidence.py \
      fetch --mapping data/mappings/canonical_instrument_mappings.csv \
      --provider yfinance --interval d \
      --sources data/mappings/evidence_sources.csv \
      --analysis-date "$DATE" --output data/evidence/
  ANTHROPIC_API_KEY=... \
  uv run .agents/skills/qualitative-analysis/scripts/generate_qualitative.py \
      --analysis "data/analysis/${DATE}.json" \
      --evidence "data/evidence/${DATE}.json" \
      --calendar-dir data/calendars --output data/qualitative/
  uv run .agents/skills/market-analysis/scripts/generate_report.py \
      --input "data/analysis/${DATE}.json" \
      --history "data/history/${DATE}.json" \
      --qualitative "data/qualitative/${DATE}.json" \
      --calendar-dir data/calendars --output content/results/
  ```

  Note that news fetched after the fact may differ from what was available on the original date; the artifact records its own input hashes and retrieval timestamps.

- **API errors (401/429/5xx):** check the key, Anthropic status, and rate limits; the step retries once. Persistent failures only suppress the AI section — never the report.
- **Everything withheld by gates:** inspect `metadata.gates` in the artifact and the cited evidence; frequent `numeric_claim_mismatch` or `direction_conflict` gates on honest content may indicate the prompt drifted from the artifact features — re-run the prompt regression tests.
- **Delete published qualitative content:** remove `data/qualitative/YYYY-MM-DD.json` (and optionally `data/evidence/YYYY-MM-DD.json`), regenerate the report without `--qualitative`, commit, and push — same flow as deleting a published report.

Durable market themes distilled from qualitative artifacts are curated into the OKF layer via human-reviewed PRs only; see `.agents/skills/aims-okf-curator/SKILL.md`.
