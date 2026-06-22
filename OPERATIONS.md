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

---

## 1. Data sources

### Stooq (primary market data)

AIMS fetches daily OHLCV (open/high/low/close/volume) price history from [Stooq](https://stooq.com) using its free CSV download API.

**Symbol format:** Stooq uses its own symbol convention.
Examples: `^SPX` (S&P 500), `^DJI` (Dow Jones), `^NDX` (NASDAQ 100), `^NKX` (Nikkei 225), `^DAX` (DAX).

**Limitations:**

- Daily, weekly, and monthly bars only — no intraday data.
- Symbol availability and history depth vary; some symbols return no data.
- No authentication required, but subject to undocumented rate limits.
- Network access is required; fetches that fail are logged as `WARNING` and skipped.

**Terms of use:** Data obtained from Stooq is subject to Stooq's own terms. AIMS does not redistribute raw Stooq data — it stores derived analysis artifacts only. Verify Stooq's terms before commercial or redistribution use.

**Configured symbols:** `data/stooq_symbols.txt` — one Stooq symbol per line; lines starting with `#` are comments. Edit this file to add or remove instruments from the daily run when using `--symbols` mode.

### Provider registry

AIMS routes market-data fetches through a provider registry defined in `src/aims/market_analysis.py`. Registered providers:

| Provider | Supported intervals | Notes                                   |
| -------- | ------------------- | --------------------------------------- |
| `stooq`  | `d`, `w`, `m`       | Free CSV download; default provider     |
| `csv`    | `d`, `w`, `m`       | Reads pre-downloaded CSVs from data dir |

Pass `--provider <name>` to `init-fetch-status`, `fetch`, or `generate`. The default is `stooq`.

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
| `asset_class`            | Yes      | `equity_index`, `commodity`, etc.                            |
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

1. Add one or more rows to `canonical_instrument_mappings.csv` — one per provider/interval combination to analyze, plus one per broker CFD pairing.
2. Run the validator above to confirm no errors.
3. Run `uv run pytest` to confirm 100% coverage still holds.
4. Optionally add the provider symbol to `data/stooq_symbols.txt` to include it in `--symbols` mode.

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

The market regime label is derived from the median composite score of reliable instruments:

| Label       | Median score            |
| ----------- | ----------------------- |
| Bullish     | ≥ 65                    |
| Neutral     | 40 – 64                 |
| Bearish     | ≤ 40                    |
| Unavailable | No reliable instruments |

### Scoring version

`SCORING_VERSION = "1.0.0"` in `src/aims/market_analysis.py`. Increment this when the feature set or scoring logic changes in a way that makes old and new scores incomparable.

### Assumptions and limitations

- Scores are cross-sectional: they reflect relative, not absolute, performance. A score of 80 in a falling market still means that instrument fell less than most others.
- Volatility and drawdown are historical. They do not predict future risk.
- Missing or stale data can distort percentile ranks when the universe is small.
- Short history (< 60 bars) triggers the `insufficient_history` gate and excludes an instrument from reliable rankings.

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
3. Load symbols from `data/stooq_symbols.txt`
4. Initialize `data/prices/fetch_status_<interval>.json` and fetch market data from Stooq (1-year lookback), recording per-symbol outcomes in fetch status
5. Generate JSON analysis artifact (`data/analysis/YYYY-MM-DD.json`) using `--fetch-status`; fail if coverage gates are violated
6. Validate artifact
7. Generate score history (`data/history/YYYY-MM-DD.json`)
8. Generate Hugo Markdown report (`content/results/YYYY-MM-DD-market-analysis.md`)
9. Build Hugo site (validation only — catches template or content errors before commit)
10. Create a pull-request branch `generated/analysis-YYYY-MM-DD` with both artifacts and the report
11. A Slack notification summarizes new/persistent signals and risk-gate changes and links to the analysis PR.

### Manual dispatch

The workflow supports `workflow_dispatch` with optional inputs:

| Input                 | Default   | Description                                                   |
| --------------------- | --------- | ------------------------------------------------------------- |
| `analysis_date`       | Today UTC | Override the analysis date (YYYY-MM-DD)                       |
| `interval`            | `d`       | Price bar interval: `d` (daily), `w` (weekly), `m` (monthly)  |
| `dry_run`             | `false`   | When `true`, skips PR creation and Slack success notification |
| `min_success_ratio`   | `0.8`     | Minimum symbol fetch success ratio for coverage gate          |
| `max_missing_symbols` | `1`       | Maximum allowed missing symbols for coverage gate             |
| `provider`            | `stooq`   | Market data provider: `stooq`                                 |

### Deployment gate

GitHub Pages deployment is handled by `ci.yml` (`hugo-deploy-to-gh-pages` job), which runs only after Python linting, type checking, and tests all pass. The daily analysis workflow commits only content files (JSON and Markdown), not Python source, so existing tests remain stable.

---

## 6. GitHub Actions secrets

| Secret              | Required | Description                                                                                                                                      |
| ------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `SLACK_WEBHOOK_URL` | Optional | Slack incoming webhook URL for success and failure notifications. If not set, the workflow skips Slack notification steps.                       |
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
| Permission | Scope | Reason |
| ---------- | ----- | ------ |
| `id-token: write` | `hugo-deploy-to-gh-pages` job | OIDC token for Pages deployment |
| `pages: write` | `hugo-deploy-to-gh-pages` job | Deploy to GitHub Pages |

---

## 8. Troubleshooting

### Fetch failed for symbol

```
ERROR: fetch failed for ^SPX
```

Stooq may be temporarily unavailable or the symbol may be invalid. Per-symbol fetch failures are non-fatal — a `WARNING` is logged and the fetch loop continues. The symbol is passed to the `generate` step which marks it as `missing_data` in the artifact and report when coverage policy still passes. The workflow fails before publishing when coverage gates detect a systemic data-source failure (too many missing symbols or success ratio below threshold). It also fails when no symbols at all can be fetched.

**Fix:** Check `data/stooq_symbols.txt` for typos. Verify the symbol at https://stooq.com. Remove permanently unavailable symbols to keep the analysis clean. Re-run the workflow after the data source recovers.

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
2. Verify Stooq availability and symbol validity in `data/stooq_symbols.txt`.
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
