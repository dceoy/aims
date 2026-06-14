# market-analysis

Fetch OHLCV market data, score instruments, and generate structured analysis artifacts.

> **Disclaimer:** All output is informational only and does not constitute investment advice.

## Scripts

All scripts are in `.agents/skills/market-analysis/scripts/`.

### `market_analysis.py`

Four sub-commands:

| Command    | Purpose                                                   |
| ---------- | --------------------------------------------------------- |
| `fetch`    | Download OHLCV data from Stooq and save to `data/prices/` |
| `check`    | Run data-quality checks on saved data                     |
| `score`    | Score and rank instruments cross-sectionally              |
| `generate` | Generate a versioned JSON analysis artifact               |

### `validate_analysis.py`

Validate a generated JSON artifact against the expected schema.

### `generate_report.py`

Generate a Hugo Markdown report from a JSON analysis artifact and write it to `content/results/`.

### `notify_slack.py`

Send a Slack notification (success or failure) via an incoming webhook. Reads `SLACK_WEBHOOK_URL` from the environment; exits silently if the variable is not set.

## Usage

```sh
# Fetch daily OHLCV data for two symbols
uv run .agents/skills/market-analysis/scripts/market_analysis.py \
    fetch --symbol AAPL.US --start 2023-01-01 --end 2024-12-31

uv run .agents/skills/market-analysis/scripts/market_analysis.py \
    fetch --symbol MSFT.US --start 2023-01-01 --end 2024-12-31

# Check data quality
uv run .agents/skills/market-analysis/scripts/market_analysis.py \
    check --symbol AAPL.US

# Score instruments and print ranking
uv run .agents/skills/market-analysis/scripts/market_analysis.py \
    score --symbols AAPL.US,MSFT.US

# Generate a dated JSON artifact in data/analysis/
uv run .agents/skills/market-analysis/scripts/market_analysis.py \
    generate --symbols AAPL.US,MSFT.US --output data/analysis/

# Validate the generated artifact
uv run .agents/skills/market-analysis/scripts/validate_analysis.py \
    --input data/analysis/$(date +%Y-%m-%d).json

# Generate a Hugo Markdown report from the artifact
uv run .agents/skills/market-analysis/scripts/generate_report.py \
    --input data/analysis/$(date +%Y-%m-%d).json \
    --output content/results/

# Send a Slack success notification
SLACK_WEBHOOK_URL="https://hooks.slack.com/services/..." \
uv run .agents/skills/market-analysis/scripts/notify_slack.py \
    --artifact data/analysis/$(date +%Y-%m-%d).json \
    --report-url https://dceoy.github.io/aims/results/$(date +%Y-%m-%d)-market-analysis/

# Send a Slack failure notification
SLACK_WEBHOOK_URL="https://hooks.slack.com/services/..." \
uv run .agents/skills/market-analysis/scripts/notify_slack.py \
    --failure \
    --run-url https://github.com/dceoy/aims/actions/runs/12345 \
    --message "Analysis failed"
```

## Data layout

```
data/
├── prices/
│   ├── AAPL.US_d.csv        # Daily OHLCV for AAPL.US
│   └── MSFT.US_d.csv
└── analysis/
    └── YYYY-MM-DD.json      # Analysis artifact
```

Each `data/prices/<SYMBOL>_<INTERVAL>.csv` has columns:
`symbol, timestamp, open, high, low, close, volume, source, interval`

Timestamps are UTC ISO 8601.

## Artifact format

`data/analysis/YYYY-MM-DD.json` — see `data/schema/analysis.schema.json` for the
schema reference. Key structure:

```json
{
  "version": "1.0.0",
  "metadata": {
    "generated_at": "...",
    "git_commit": "...",
    "data_source": "stooq",
    "data_freshness": {"AAPL.US": "2024-12-31"},
    "scoring_version": "1.0.0",
    "config": {"stale_days": 5, "min_history": 60, "interval": "d"}
  },
  "instruments": [
    {
      "symbol": "AAPL.US",
      "rank": 1,
      "score": 72.5,
      "is_reliable": true,
      "risk_gates": [],
      "explanation": "20d up +5.3%; above MA20 by 2.1%; RSI14=62",
      "features": { "ret_1d": 0.012, "ret_5d": 0.031, ... }
    }
  ]
}
```

## Provider limitations (StooqProvider)

- Daily, weekly, and monthly bars only — no intraday data.
- Symbol format is Stooq-specific: `AAPL.US`, `^SPX`, `7203.JP`.
- Data availability varies by symbol; some return empty results.
- No authentication required, but subject to Stooq rate limits.
- Requires outbound network access. Use `CsvFileProvider` for tests.

## Risk gates

Instruments failing quality checks are included in output but marked
`is_reliable: false` and excluded from top rankings:

| Gate                   | Trigger                                                       |
| ---------------------- | ------------------------------------------------------------- |
| `stale_data`           | Latest bar older than `stale_days` calendar days              |
| `insufficient_history` | Fewer than `min_history` bars                                 |
| `missing_bars`         | Gap > 7 calendar days between consecutive bars                |
| `malformed_input`      | Non-positive prices, high < low, or price outside [low, high] |
| `high_volatility`      | 20-day annualized volatility > 100%                           |
