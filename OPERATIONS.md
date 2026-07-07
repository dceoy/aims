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

**Bar boundary policy:** `generate --analysis-date DATE` scores only bars strictly before `DATE`; any bar dated on or after `DATE` is dropped before scoring. This excludes in-progress intraday bars for markets still open when the scheduled run fires (e.g. `^N225`, `^HSI`, `*.T` — Tokyo/Hong Kong sessions are mid-day at the 01:00 UTC schedule), and rejects look-ahead when backfilling a past `analysis_date` against a `--data-dir` that holds newer bars. The tradeoff is one extra day of reporting lag for markets that had already closed by fetch time, in exchange for every instrument's `data_freshness` being computed the same way and a rerun of a past date reproducing the same artifact.

### Market regime

The market regime label is derived from breadth: the share of reliable instruments whose latest close is above their 20-day moving average. Percentile-based composite scores are relative by construction — their median stays near 50 for any universe of meaningful size regardless of market direction — so breadth is used as an absolute directional measure instead. Reliable instruments without MA20 data are excluded from the ratio.

| Label       | Share above MA20                       |
| ----------- | -------------------------------------- |
| Bullish     | ≥ 65%                                  |
| Neutral     | > 35% and < 65%                        |
| Bearish     | ≤ 35%                                  |
| Unavailable | No reliable instruments with MA20 data |

The label is computed once, at artifact generation time, and stored as `metadata.market_regime` (`{label, positive_count, reliable_count, breadth, thresholds}`) — the authoritative, auditable source for the regime shown in reports and Slack notifications. Both consumers call `regime_from_artifact()` (`src/aims/reports.py`), which reads the stored value and only recomputes it from reliable-instrument MA20 breadth as a fallback for artifacts generated before this field existed (schema version < 1.1.0). This is informational only: it never modifies scores, ranks, or risk gates.

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
2. Validate instrument mappings (`validate_instrument_mappings.py`) — a typo'd `provider`/`provider_interval` value fails the run instead of silently shrinking the symbol universe
3. Set analysis date (default: today UTC) and compute the interval-aware output stem (see below)
4. Load symbols from `data/mappings/canonical_instrument_mappings.csv` for the configured `--provider`/`--interval` (the mapping file is the single source of truth; there is no separate `data/*_symbols.txt` file to keep in sync)
5. Initialize `data/prices/fetch_status_<interval>.json` and fetch market data from the configured provider (lookback window scaled per interval by `aims.policy.fetch_window_days`), recording per-symbol outcomes in fetch status
6. Generate JSON analysis artifact (`data/analysis/<stem>.json`) using `--mapping` and `--fetch-status`; fail if coverage gates are violated. Each instrument entry is enriched with `canonical_id`, `display_name`, and `asset_class` from the mapping. Bars dated on or after `--analysis-date` are dropped before scoring (see "Bar boundary policy" above).
7. Validate artifact
8. Generate score history (`data/history/<stem>.json`)
9. Generate Hugo Markdown report (`content/results/<stem>-market-analysis.md`), grouped by asset class when the artifact carries more than one
10. Build Hugo site (validation only — catches template or content errors before commit)
11. Create (or update) a pull-request branch `generated/analysis-<stem>` with both artifacts and the report, then merge it directly (squash, delete branch)
12. A Slack notification summarizes new/persistent signals and risk-gate changes and links to the analysis PR.

**Interval-aware output stem:** `<stem>` is the analysis date (`YYYY-MM-DD`) for the default `d` interval, and `YYYY-MM-DD-<interval>` for `w`/`m` (see `aims.market_analysis.artifact_interval_suffix`). This keeps existing daily filenames unchanged while preventing a manual `w`/`m` dispatch from overwriting the same date's daily artifact, history, report, or PR branch.

### Merging the analysis PR

Step 11 calls `gh pr merge --squash --delete-branch` directly rather than `--auto`: `main` has no branch protection or required status checks, and GitHub only allows `--auto` to be enabled on a PR whose merge is otherwise blocked by such requirements, so `--auto` fails outright here. All validation (artifact/history schema checks, Hugo build) has already run earlier in the same job, so merging immediately is safe. If the merge fails for any reason, the step fails the job (no error-masking) and the failure Slack notification fires.

**Known gotcha — PRs stuck in `action_required`:** pull-request-triggered `ci.yml` runs on `generated/analysis-*` branches can be gated with conclusion `action_required` and zero jobs executed, even though the PR was opened by `github-actions[bot]` pushing to a branch in the same repository (not a fork). When this happens, the merge step above will fail (and notify) rather than merging. A repository maintainer must approve the pending workflow run (Actions tab → the run → **Approve and run**) or re-run it; only an authorized human/maintainer token can do this, the workflow's own `GITHUB_TOKEN` cannot self-approve. If this recurs daily, check **Settings → Actions → General** for an approval requirement (e.g. "Require approval for all outside collaborators") that is being applied to `github-actions[bot]`-authored pull requests, and relax it only if the operational risk is acceptable.

### Manual dispatch

The workflow supports `workflow_dispatch` with optional inputs:

| Input                 | Default    | Description                                                                                                                                                                                                                    |
| --------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `analysis_date`       | Today UTC  | Override the analysis date (YYYY-MM-DD)                                                                                                                                                                                        |
| `interval`            | `d`        | Price bar interval: `d` (daily), `w` (weekly), `m` (monthly). `w`/`m` currently only cover the mapping rows that exist for those intervals (the five original indices) and write to interval-suffixed output paths (see above) |
| `dry_run`             | `false`    | When `true`, skips PR creation, merge, and Slack success notification                                                                                                                                                          |
| `min_success_ratio`   | `0.8`      | Minimum symbol fetch success ratio for coverage gate                                                                                                                                                                           |
| `max_missing_symbols` | `4`        | Maximum allowed missing symbols for coverage gate (scaled for the ~20-instrument mapped universe)                                                                                                                              |
| `provider`            | `yfinance` | Market data provider: `yfinance` or `stooq`                                                                                                                                                                                    |

### Deployment gate

GitHub Pages deployment is handled by `ci.yml` (`hugo-deploy-to-gh-pages` job), which runs only after Python linting, type checking, and tests all pass. The daily analysis workflow commits only content files (JSON and Markdown), not Python source, so existing tests remain stable.

`ci.yml` runs on three deploy-relevant triggers:

- `push` to `main` (human merges).
- `workflow_run` on "Daily market analysis" completion: bot merges performed with `GITHUB_TOKEN` create no push event, so the daily workflow finishing (successfully) re-runs CI/CD against the head of `main` and deploys it. Deploys are idempotent snapshots of `main`, so a redundant run after a dry run is harmless.
- `workflow_dispatch` (`gh workflow run ci.yml`): manual full CI + deploy of current `main` — the recovery path when a deploy failed or the site is stale.

The deploy job builds the site with Hugo, uploads it as a Pages artifact, and deploys via `actions/deploy-pages`. Pages deployments fail transiently ("Deployment failed, try again later."); the job retries the deploy once in-run. If the job still fails, a Slack failure notification fires when `SLACK_WEBHOOK_URL` is configured — otherwise check the run under the Actions tab and the deployment status via `gh api repos/<owner>/<repo>/deployments?environment=github-pages`.

### Rollback

If a published report or artifact needs to be removed, see [Delete a published report](#delete-a-published-report) in Manual recovery. Reverting a bad _code_ change (as opposed to a bad daily _report_) is a normal `git revert` on `main`, gated by the same CI checks as any other change.

---

## 6. GitHub Actions secrets

| Secret              | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SLACK_WEBHOOK_URL` | Optional | Slack incoming webhook URL for success and failure notifications. If not set, the workflow skips Slack notification steps.                                                                                                                                                                                                                                                                                                                                                       |
| `ANTHROPIC_API_KEY` | Optional | Claude API key for the AI qualitative analysis step (design in [§10](#10-ai-qualitative-analysis-layer-design), operations in [§11](#11-ai-qualitative-analysis-layer-operations)). Consumed by `daily-market-analysis.yml`: when set, the workflow fetches evidence and generates, validates, gates, and commits a qualitative artifact in the analysis PR (shadow mode). When unset, all qualitative steps are skipped and the run is byte-for-byte the quantitative pipeline. |
| `GITHUB_TOKEN`      | Built-in | Used automatically by `gh` and `git push` in the `update-cfd-instruments` and `daily-market-analysis` workflows. No manual configuration needed.                                                                                                                                                                                                                                                                                                                                 |

**How to add `SLACK_WEBHOOK_URL`:** Go to the repository → Settings → Secrets and variables → Actions → New repository secret. Name: `SLACK_WEBHOOK_URL`. Value: the `https://hooks.slack.com/services/…` URL from your Slack app's Incoming Webhooks configuration.

**Never commit secret values.** The `notify_slack.py` script reads `SLACK_WEBHOOK_URL` only from the environment, and `qualitative_analysis.py` reads `ANTHROPIC_API_KEY` only from the environment.

**Repository variables:**

| Variable                | Default   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AI_COMMENTARY_ENABLED` | unset/off | Rendering switch for AI commentary (#94/#95). While unset or not `true`, qualitative artifacts are committed in shadow mode but `generate_report.py` is never passed `--qualitative`, so published reports are unchanged. Flip to `true` only after the shadow-mode exit criteria recorded on issue #98 are met; the flip is a reviewed change, not a silent default. The `ai_commentary` workflow-dispatch input (`on`/`off`) overrides it per run. |

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

### Qualitative step failed

```
WARNING: AI commentary: step failed; quantitative report unaffected
```

The "Run qualitative analysis (shadow mode)" step is `continue-on-error`: evidence fetch problems, Claude API errors (401/429/5xx/timeouts), or an artifact that stays invalid after the single regeneration retry never block quantitative publication. The Slack success message carries the warning above.

**Fix:** Open the step log in the failed run. For API errors, check the `ANTHROPIC_API_KEY` secret and [status.anthropic.com](https://status.anthropic.com), then re-run (or backfill per [§9](#9-manual-recovery)). For validation errors, the log lists each violated rule from `validate_qualitative.py`. Repeated systemic failures can be silenced with the `skip_qualitative` dispatch input while investigating.

### AI commentary absent or withheld by gates

Commentary can be absent for benign reasons: the secret is unset, rendering is off (shadow mode), the evidence bundle was empty, or the #93 gates withheld content. Gate outcomes are recorded in the artifact itself — `metadata.gates` names the market-level gates and per-instrument `qualitative_gates`; the Slack summary shows `withheld by gates (...)`. Gated entries are working as designed: they are excluded from rendering, not retried. A market-narrative gate withholds the whole artifact from rendering while it still merges for shadow-mode measurement.

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

### Regenerate a qualitative artifact for a past date

Requires the committed analysis artifact for that date. Evidence for a past date can be re-fetched, but feeds only serve recent items — re-fetched bundles for old dates may be thin; prefer the originally committed bundle when it exists.

```sh
# 1. (only if the bundle is missing) rebuild the evidence bundle
uv run .agents/skills/qualitative-analysis/scripts/fetch_evidence.py \
    --analysis-date YYYY-MM-DD --output data/evidence/
uv run .agents/skills/qualitative-analysis/scripts/validate_evidence.py \
    --input data/evidence/YYYY-MM-DD.json

# 2. regenerate, validate, and gate the qualitative artifact
ANTHROPIC_API_KEY=... \
uv run .agents/skills/qualitative-analysis/scripts/qualitative_analysis.py \
    --analysis data/analysis/YYYY-MM-DD.json \
    --evidence data/evidence/YYYY-MM-DD.json \
    --calendar data/calendars/macro_events.json \
    --calendar data/calendars/earnings.json \
    --output data/qualitative/
uv run .agents/skills/qualitative-analysis/scripts/validate_qualitative.py \
    --input data/qualitative/YYYY-MM-DD.json \
    --analysis data/analysis/YYYY-MM-DD.json \
    --evidence data/evidence/YYYY-MM-DD.json
```

Commit the artifacts through a reviewed PR.

### Regenerate the stance-evaluation artifact and page

Deterministic; needs only committed analysis and qualitative artifacts (no API key, no price fetch). See [§12](#12-stance-evaluation-accountability-and-okf-theme-curation).

```sh
uv run .agents/skills/qualitative-analysis/scripts/evaluate_stances.py \
    --input data/analysis/YYYY-MM-DD.json \
    --analysis-dir data/analysis \
    --qualitative-dir data/qualitative \
    --output data/performance \
    --page-output content/evaluation/_index.md
uv run .agents/skills/qualitative-analysis/scripts/validate_performance.py \
    --input data/performance/YYYY-MM-DD.json
```

### Run the OKF theme curation pass

```sh
uv run .agents/skills/aims-okf-curator/scripts/curate_themes.py \
    --qualitative-dir data/qualitative --concepts-dir okf/concepts
```

Review the printed proposal, then promote or retire through a reviewed OKF PR (never auto-merged). See [§12](#12-stance-evaluation-accountability-and-okf-theme-curation).

### Refresh event calendars manually

Trigger **Actions → Update event calendars → Run workflow** (earnings only), or run `update_calendars.py` locally. Macro events are hand-maintained — see [§11](#11-ai-qualitative-analysis-layer-operations).

### Refresh CFD instruments manually

Trigger **Actions → Update CFD instruments → Run workflow**.

---

## 10. AI qualitative analysis layer (design)

This section is the design contract for the AI qualitative analysis roadmap (#98). It was written before implementation (#89) so that later issues (#90–#97) implement against agreed rules instead of re-litigating them. Issues #90–#95 are implemented against this contract (evidence ingestion, calendars, the qualitative skill, the deterministic gates, the renderer, and the shadow-mode workflow integration); operational details live in [§11](#11-ai-qualitative-analysis-layer-operations). Rendering stays off until the shadow-mode exit criteria in this section are met and recorded on #98.

### Purpose and boundaries

The quantitative pipeline cannot see _why_ — news, earnings, disclosures, and macro events that explain or contradict the rankings. The qualitative layer adds grounded AI interpretation around the quantitative signal while leaving every existing guarantee intact:

- **The quantitative artifact stays authoritative for all numbers.** The qualitative artifact may reference scores, ranks, features, risk gates, and the market regime; it never restates them authoritatively and never modifies them. This mirrors the OKF guardrail that LLM prose is never the source of truth for numeric facts.
- **The LLM call is the single non-deterministic step.** It produces a committed, schema-validated JSON artifact (`data/qualitative/<stem>.json`). Everything downstream — validation, gating, report rendering, Hugo build — stays deterministic. Report generation without a qualitative artifact remains byte-identical to today's output.
- **Fail-open.** Any qualitative failure (missing API key, API error, timeout, gate withholding) publishes the quantitative report unchanged. Quantitative coverage gates are never weakened. Qualitative-step failures are non-fatal warnings; quantitative failures remain fatal exactly as now.

### Artifact contract (#92)

`data/qualitative/<stem>.json`, versioned by its own `QUALITATIVE_VERSION` (starting at `1.0.0`), validated by a hand-rolled `validate_qualitative.py` following the `validate_analysis.py` pattern. The format reference is `data/schema/qualitative.schema.json`. Key points:

- **Scope:** per-instrument entries cover only the top-K published signals (K=5, matching `history.py`'s `DEFAULT_TOP_K`), plus one market-level narrative and up to five macro themes. One LLM call per day. No commentary on the rest of the universe — cost and review surface stay bounded.
- **Closed enums:** stance is `supportive` / `neutral` / `conflicting` (relative to the quantitative signal); confidence is `low` / `medium` / `high`. A `conflicting` stance — the model disagreeing with the signal on outlook — is legitimate, expected output.
- **Machine-checkable claims:** drivers carry structured fields instead of burying assertions in prose. A `direction_claim` (`up`/`down`/`none` over a `1d`/`5d`/`20d`/`60d` window) states realized price action, including an explicit no-movement claim so "flat" assertions are checkable too instead of living unverified in free text; `numeric_claims` entries (`value`, `unit`, `refers_to`) declare every number used. Free text is display-only and may not contain numeric tokens undeclared in `numeric_claims` (whitelist: feature names, ISO dates, and — when the analysis artifact is supplied for cross-checking — numerals embedded in covered instruments' own names, e.g. the 500 in "S&P 500", so reciting a proper name is never mistaken for an undeclared claim).
- **Provenance metadata:** model ID, prompt version and prompt-file SHA-256, the bar interval (`d`/`w`/`m`, carried from the analysis artifact so a manual weekly/monthly dispatch's qualitative artifact keeps the same `-w`/`-m` filename suffix as its analysis/evidence siblings), and content hashes of the inputs (analysis artifact, evidence bundle, calendar when it exists), so any artifact traces to exactly what produced it. `generated_at` is analysis-date midnight UTC, mirroring the analysis artifact.

### Grounding rules (#90, #92)

- The model cites only from the day's committed, validated evidence bundle (`data/evidence/`, issue #90) — no browsing, retrieval, vector stores, embeddings, or external RAG services at analysis time (repository policy).
- Every driver, theme, and the market narrative carries at least one citation; citations are evidence IDs that must exist in the referenced bundle.
- Numeric statements must be reproducible from `data/analysis/` or from a cited evidence item.
- Evidence text is untrusted data: it is delimited as quoted content in the prompt, instructions inside it are content to ignore, and the validator whitelists output shape, enums, and citation targets regardless of what the model emits.
- Where evidence coverage for an instrument is thin (per-asset-class coverage accounting from #90), the prompt says so; `neutral` with few drivers is the correct output — absence of evidence must not be filled with plausible narrative.

### Deterministic gates (#93)

Schema validity is not truth. After validation, a deterministic gate pass cross-examines the structured claims against the numbers AIMS already computes, mirroring the `risk_gates` pattern: direction consistency (an `up`/`down` `direction_claim` contradicting the sign of the matching return feature, or a `none` claim contradicted by a non-trivial move in that feature, is gated — stance disagreement is never gated), numeric-claim verification within tolerance, evidence recency (aligned with `stale_days` in `src/aims/policy.py`), and citation coverage. Gated per-instrument entries are excluded from rendering; a gated market narrative withholds the whole artifact. One regeneration retry is allowed before degrading. Gate outcomes are recorded in artifact metadata so the report and Slack can say why commentary is absent. Gates are deterministic code only — no LLM-based verification.

### Runner architecture and API access (#92)

- **Runner:** an agent skill at `.agents/skills/qualitative-analysis/` whose scripts are thin wrappers delegating to `src/aims/qualitative.py`, the same pattern as `market-analysis/scripts/`. It runs in the daily workflow after the "Validate artifact" step (#95).
- **API access:** the official `anthropic` Python SDK is added as a runtime dependency. Rationale: schema-constrained structured outputs, typed error classes, and built-in retry/backoff for 429/5xx — hand-rolling those over stdlib `urllib` (the `notify_slack.py` precedent, which was considered) would mean more custom code maintained at 100% branch coverage for no dependency saved in practice. `output_config.format` takes a real JSON Schema (`type`/`properties`/`required`) authored in code at implementation time (#92); `data/schema/qualitative.schema.json` stays a hand-rolled reference for `validate_qualitative.py`, not that request schema. The API-level schema guarantees basic shape and required-key presence; enum values, citation targets, and cross-field rules remain enforced by the validator and the #93 gates. The API-calling boundary in `src/aims/qualitative.py` stays thin and mockable; tests never call the network.
- **Model:** `claude-opus-4-8`, pinned in code and recorded in artifact metadata alongside the prompt version. The prompt is a committed file; changing it or the model requires the #97 regression harness once that exists. Current Claude models accept no sampling parameters (`temperature` is rejected), so run-to-run reproducibility rests on committed inputs, structured outputs, deterministic gates, and committing a single validated artifact per date — not on a temperature setting.
- **Caps:** one call per run; input capped by the evidence bundle's per-instrument item caps and length-capped snippets (#90); output capped via `max_tokens`; request timeout and a single retry (which is also the #93 regeneration retry).

### Secret handling and cost (#95)

`ANTHROPIC_API_KEY` is an optional repository secret read only from the environment, mirroring `SLACK_WEBHOOK_URL` (see [§6](#6-github-actions-secrets)). When absent, every qualitative step is skipped and the pipeline behaves exactly as today. Expected cost, to be re-measured once #92 runs: one daily call with roughly 30–60k input tokens and 2–5k output tokens on `claude-opus-4-8` ($5/$25 per million tokens) is about $0.20–0.45 per run, i.e. roughly $10–20/month. Record measured figures here after the first shadow-mode week.

### Rollout: shadow mode before rendering (#95, then #94)

Daily analysis PRs auto-merge with no human review (#75), so schema validation and the #93 gates are the only pre-publication defenses for LLM output. Rendering is therefore staged:

1. **Shadow mode (#95):** evidence and qualitative artifacts are generated, validated, gated, and committed in the daily analysis PR, but `generate_report.py` is not passed `--qualitative`. Published reports stay byte-identical to today's.
2. **Exit criteria** (tracked on #98): at least 10 consecutive scheduled runs with zero schema/validator failures, a market-narrative gate pass rate of at least 80%, and a human spot-review of the committed artifacts recorded on #98.
3. **Enable rendering (#94):** a default-off repository variable (e.g. `AI_COMMENTARY_ENABLED`) flips `--qualitative` on. The flip is a reviewed change recorded against #98's checklist, not a silent default. AI commentary renders in an explicitly labeled section with citations, model/prompt provenance, and the financial disclaimer adjacent.
4. **Go/no-go checkpoint** (tracked on #98): after roughly one quarter of enabled rendering, review stance hit rates and calibration (#97), gate withhold rates, and realized cost; continue, adjust, or retire the layer.

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

- **`macro_events.json`** — central-bank decision dates (FOMC, ECB, BOJ), hand-maintained from officially published yearly schedules (sources recorded per event). Refresh cadence: when each institution publishes next year's schedule (typically mid-year), extend the file through a reviewed PR and re-run `validate_calendar.py`. **Correcting a wrong date:** edit the event's `date`, keep the `source` URL pointing at the official schedule, and open a reviewed PR — the next daily run picks it up.
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

Shadow mode is the default state: with `ANTHROPIC_API_KEY` set, the daily PR carries analysis, history, evidence, and qualitative artifacts while the published report stays byte-identical to a quantitative-only run. Rendering is controlled by the `AI_COMMENTARY_ENABLED` repository variable ([§6](#6-github-actions-secrets)) plus the `ai_commentary` dispatch input; the `skip_qualitative` input disables the qualitative steps for a single run.

Cost controls: one Claude call per run (`claude-opus-4-8`, pinned in `aims.qualitative.MODEL_ID`), input bounded by the evidence caps, output capped at 8192 tokens, 300-second request timeout, one SDK-level retry for 429/5xx, and one regeneration retry. Expected order of magnitude per [§10](#10-ai-qualitative-analysis-layer-design): roughly $0.20–0.45 per run (≈$10–20/month); record measured figures here after the first shadow-mode week. Changing the model or the committed prompt (`.agents/skills/qualitative-analysis/prompts/qualitative_v1.md`, version + SHA-256 recorded in every artifact) requires the [§12](#12-stance-evaluation-accountability-and-okf-theme-curation) regression harness.

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

**Before adopting any change to `prompts/qualitative_v1.md`, `PROMPT_VERSION`, or `MODEL_ID`:** run the harness (over freshly generated candidate artifacts, or the committed fixtures when no API key is available) with `--record data/performance/prompt_regressions.json` and commit the updated file. A CI test (`tests/test_prompt_regression.py::test_committed_prompt_and_model_have_a_recorded_passing_entry`) fails when the committed prompt/model has no recorded passing entry, so an unreviewed prompt change cannot merge. There is **no automatic prompt tuning or optimization loop** — the harness measures and records; adoption stays a reviewed human decision. See the `qualitative-analysis` skill doc for the exact command.

### Citation link-rot sampling (#97)

`check_citation_links.py` (in `src/aims/link_check.py`) probes a bounded, deterministic sample of recent evidence citation URLs over HTTP (HEAD, falling back to GET) so dead sources surface in the workflow log. It is **a warning, not a gate**: it always exits 0, writes no artifact (network results are non-deterministic and stay out of committed data), and runs `continue-on-error` in the daily workflow. Persistent rot on a source means editing or removing its row in `data/mappings/evidence_sources.csv` per [§11](#11-ai-qualitative-analysis-layer-operations).

### OKF theme curation (#96)

Durable themes surfaced by the daily qualitative artifacts belong in the OKF knowledge layer, not the point-in-time reports. `curate_themes.py` (in `src/aims/okf_curation.py`, behind the `aims-okf-curator` skill) runs a **monthly** deterministic pass over `data/qualitative/*.json`: it clusters recurring theme titles by token overlap, prints promotion candidates that recur on **≥3 distinct dates spanning ≥14 days** (with dated artifact and evidence citations plus a ready-to-edit concept skeleton), lists supporting per-instrument stance streaks, and flags retirement candidates among existing `qualitative-theme`-tagged concepts (unseen for **>60 days**).

Its output is a **proposal for human review only** — it never writes to `okf/`. Promotion and retirement follow the standard OKF flow: edit a draft into `okf/concepts/theme-<slug>.md` (carry the `qualitative-theme` tag and a `theme_tokens` front-matter list so future passes assess recurrence; cite dated artifacts; numeric facts stay pointers into `data/analysis/` and are never asserted as truth in prose), record the pass — including "no promotions" — in `okf/logs/log.md`, regenerate shadow content (`tools/okf_hugo_adapter.py --clean` then `--check`), build with `hugo --gc --minify`, and open a reviewed PR. **OKF changes are never auto-merged.** Cadence and criteria are documented in `.agents/skills/aims-okf-curator/SKILL.md`.

**Current state (accumulation limitation):** shadow mode has not yet committed qualitative artifacts to `main`, so both the stance-evaluation artifact and the first curation pass are recorded empty states. The machinery, schemas, fixtures, and tests are complete; the "at least one promoted theme" and populated evaluation-summary milestones fill in once artifacts accumulate. This limitation is recorded rather than worked around.

### Go/no-go checkpoint (#98)

After roughly one quarter of enabled rendering, review this section's stance hit rates and confidence calibration, gate withhold rates, and realized API cost, then record a continue / adjust / retire decision on issue #98. A layer that measures as plausible-sounding noise is retired, not maintained.
