# aims

AI Market Strategist

[![CI](https://github.com/dceoy/aims/actions/workflows/ci.yml/badge.svg)](https://github.com/dceoy/aims/actions/workflows/ci.yml)

## Automated data maintenance

AIMS maintains structured research data through independent GitHub Actions workflows:

- **Daily market analysis:** `.github/workflows/daily-market-analysis.yml` runs on weekdays, creates and validates machine-readable analysis, history, and performance JSON artifacts, and merges a data-only pull request. It does not generate articles or Hugo pages.
- **Event calendars:** `.github/workflows/update-calendars.yml` refreshes the earnings and central-bank event calendars every Monday (05:30 UTC).
- **CFD instruments:** `.github/workflows/update-cfd-instruments.yml` refreshes `data/cfd_instruments.csv` every Monday (05:00 UTC).

Scheduled Markdown report generation and GitHub Pages deployment have been retired. Existing reports under `content/results/` are historical snapshots, not new scheduled publications. The Hugo source remains available for local/manual use; there is no automated website deployment.

See [OPERATIONS.md](OPERATIONS.md) for data sources, scoring methodology, and manual recovery procedures.

