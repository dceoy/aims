# aims

Automated maintenance of three versioned financial reference datasets. No static site, articles, market scoring, or AI analysis.

## Maintained datasets

| Dataset | Path | Schedule (UTC) |
| --- | --- | --- |
| GMO Click and Rakuten CFD listings | `data/cfd_instruments.csv` | Monday 05:00 |
| Earnings and Fed/ECB/BOJ event calendars | `data/calendars/*.json` | Monday 05:30 |
| Canonical broker/provider symbol mappings | `data/mappings/*.csv` | Versioned reference; edited by PR and validated in CI |

The workflows create pull requests for material changes; production data is updated when the PR is merged. Neither GitHub Pages nor a web frontend is required.

## Run manually

```bash
uv sync --locked
uv run python -m aims.update_cfd_instruments --output data/cfd_instruments.csv --mappings data/mappings/cfd_ticker_mappings.csv
uv run python -m aims.validate_cfd_instruments --input data/cfd_instruments.csv --schema data/schema/cfd_instruments.schema.json
uv run python -m aims.mappings --input data/mappings/canonical_instrument_mappings.csv --cfd-instruments data/cfd_instruments.csv
uv run python -m aims.calendars --mapping data/mappings/canonical_instrument_mappings.csv --output data/calendars/earnings.json
uv run python -m aims.macro_calendar --output data/calendars/macro_events.json
uv run python -m aims.validate_calendar --input data/calendars/earnings.json
uv run python -m aims.validate_calendar --input data/calendars/macro_events.json
uv run pytest
```

The calendar updater keeps existing data when all earnings providers fail, and the macro calendar updater validates official-source schedules. The CFD update workflow ignores timestamp-only changes. All three datasets are independent of the retired daily analysis pipeline.
