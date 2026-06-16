#!/usr/bin/env bash

set -euxo pipefail
cd "$(git rev-parse --show-toplevel)"

# Python
uv run ruff format .
uv run ruff check --fix .
uv run pyright .

if [ -d tests ] || [ -n "$(git ls-files 'tests/**' '*test*.py' 'test_*.py')" ]; then
  uv run pytest
else
  echo "No Python tests found; skipping pytest."
fi

# Validate CFD instruments CSV
if [ -f data/cfd_instruments.csv ]; then
  uv run python .agents/skills/update-cfd-instruments/scripts/validate_cfd_instruments.py \
    --input data/cfd_instruments.csv \
    --schema data/schema/cfd_instruments.schema.json
fi

# OKF knowledge shadow content
if [ -d okf ]; then
  uv run python tools/okf_hugo_adapter.py --src okf --dst content/knowledge --check
fi

# Markdown
npx -y prettier --write './**/*.md'

# Hugo
hugo --gc --minify

# GitHub Actions
case "${OSTYPE}" in
  darwin* | linux* )
    zizmor --fix=safe .github/workflows
    if [ -n "$(git ls-files '.github/workflows/*.yml' '.github/workflows/*.yaml')" ]; then
      git ls-files -z -- '.github/workflows/*.yml' '.github/workflows/*.yaml' | xargs -0 -t actionlint
      git ls-files -z -- '.github/workflows/*.yml' '.github/workflows/*.yaml' | xargs -0 -t yamllint -d '{"extends": "relaxed", "rules": {"line-length": "disable"}}'
    fi
    checkov --framework=all --output=github_failed_only --directory=.
    ;;
  * )
    echo "GitHub Actions linting is only supported on Linux and macOS."
    ;;
esac
