# aims

Maintains three financial reference datasets without a static website.

## Datasets

- CFD instrument listings: `data/cfd_instruments.csv` (Monday 05:00 UTC).
- Earnings and central-bank calendars: `data/calendars/*.json` (Monday
  05:30 UTC).
- Broker/provider symbol mappings: `data/mappings/*.csv` (reviewed PRs).

The scheduled workflows create PRs for changed data. Automatic PR merging is
disabled. The dataset schemas, validation, and CI remain in place.

## Manual updates

```bash
uv sync --locked
uv run python -m aims.update_cfd_instruments \
  --output data/cfd_instruments.csv \
  --mappings data/mappings/cfd_ticker_mappings.csv
uv run python -m aims.validate_cfd_instruments \
  --input data/cfd_instruments.csv \
  --schema data/schema/cfd_instruments.schema.json
uv run python -m aims.mappings \
  --input data/mappings/canonical_instrument_mappings.csv \
  --cfd-instruments data/cfd_instruments.csv
uv run python -m aims.calendars \
  --mapping data/mappings/canonical_instrument_mappings.csv \
  --output data/calendars/earnings.json
uv run python -m aims.macro_calendar \
  --output data/calendars/macro_events.json
uv run python -m aims.validate_calendar \
  --input data/calendars/earnings.json
uv run python -m aims.validate_calendar \
  --input data/calendars/macro_events.json
uv run pytest
```

The calendar updaters protect previously committed data when external sources
fail or return anomalous schedules. The CFD updater ignores timestamp-only
changes.
