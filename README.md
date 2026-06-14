# aims

AI Market Strategist

[![CI](https://github.com/dceoy/aims/actions/workflows/ci.yml/badge.svg)](https://github.com/dceoy/aims/actions/workflows/ci.yml)

## Static analysis site

Analysis results are saved as Hugo content under `content/results/` and rendered to the ignored `site/` directory.
The site uses the Congo Hugo theme via Hugo Modules.

Create a new result:

```bash
hugo new results/YYYY-MM-DD-market-analysis.md
```

Set `draft = false` in the generated front matter when the result is ready to publish, then build the static site:

```bash
hugo --gc --minify
```

Preview drafts locally with:

```bash
hugo server --buildDrafts
```

## Automated analysis pipeline

Daily market analysis runs automatically via `.github/workflows/daily-market-analysis.yml`. It fetches market data, scores instruments, generates JSON artifacts and Hugo Markdown reports, builds the site, and commits the results.

See [OPERATIONS.md](OPERATIONS.md) for data sources, scoring methodology, required secrets, and operational runbooks.
