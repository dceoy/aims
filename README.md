# aims

Maintains three financial reference datasets. Static website sources and deployment
workflows have been removed; the existing Pages site must be disabled separately.

## Datasets

- CFD instrument listings: `data/cfd_instruments.csv` (Monday 05:00 UTC).
- Earnings and central-bank calendars: `data/calendars/*.json` (Monday
  05:30 UTC).
- Broker/provider symbol mappings: `data/mappings/*.csv` (reviewed PRs).

The scheduled workflows create PRs for changed data. Automatic PR merging is
disabled. The dataset schemas, validation, and CI remain in place.


## Retire the published GitHub Pages site

Removing site source files and deployment workflows does not unpublish an
existing GitHub Pages deployment. An administrator must visit the
[repository Pages settings](https://github.com/dceoy/aims/settings/pages),
choose `Deploy from a branch` as the Source, set the publishing branch to
`None`, and save. Confirm the site is no longer published. Also remove the
old `https://dceoy.github.io/aims/` repository homepage URL if present.

This administrative task cannot be completed by this code-only pull request.

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
