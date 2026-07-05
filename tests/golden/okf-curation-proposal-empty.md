# OKF qualitative theme curation proposal — n/a

Deterministic pass over 0 qualitative artifacts — none have accumulated yet; this is a recorded empty pass. Promotion is a human-reviewed pull request only — never auto-merged.

## Promotion candidates

_No recurring themes meet the promotion criteria (≥3 distinct dates spanning ≥14 days). Record a "no promotions" pass in `okf/logs/log.md`._

## Per-instrument stance streaks (supporting context)

_No instrument held a single stance on ≥3 dates spanning ≥14 days._

## Retirement candidates

_No qualitative artifacts available — recurrence of existing theme concepts cannot be assessed; skipping._

## Warnings

- tests/fixtures/okf_concepts_missing: concepts directory not found

## Curation checklist

- [ ] Review candidates; edit a draft into `okf/concepts/theme-<slug>.md` (cite dated artifacts; numeric facts stay pointers into `data/analysis/`)
- [ ] Record this pass — including "no promotions" — in `okf/logs/log.md`
- [ ] `uv run python tools/okf_hugo_adapter.py --src okf --dst content/knowledge --clean`
- [ ] `uv run python tools/okf_hugo_adapter.py --src okf --dst content/knowledge --check`
- [ ] `hugo --gc --minify`
- [ ] Open a human-reviewed PR — never auto-merge OKF changes
