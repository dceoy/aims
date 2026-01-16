# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Financial Market Analysis system that uses Google's Gemini CLI to analyze macroeconomic and financial news. The system is designed to run automated market analysis and send results to Slack channels.

## Architecture

### Core Components

1. **Gemini CLI Commands** (`.gemini/commands/`)
   - `analyze_market.toml`: Defines the market analysis prompt that fetches and analyzes economic news for indices, commodities, and macro indicators

2. **GitHub Actions Workflows** (`.github/workflows/`)
   - `gemini-cli-to-slack.yml`: Core workflow that runs Gemini CLI and sends results to Slack
   - `scheduler.yml`: Scheduled job that runs analysis every 8 hours
   - `ci.yml`: CI/CD pipeline for linting and release management

### Workflow Architecture

The system operates through GitHub Actions:

- **Scheduled Analysis**: Runs every 8 hours via cron schedule
- **Manual Trigger**: Can be triggered manually with custom prompts
- **Slack Integration**: Automatically posts analysis results to configured Slack channel
- **Translation**: Default configuration translates analysis to Japanese

## Development Commands

### Running Analysis Manually

Trigger the analysis workflow via GitHub Actions UI:

1. Go to Actions → "Scheduled jobs" workflow
2. Click "Run workflow"
3. Optional: Provide custom prompt (default analyzes market and translates to Japanese)

### Testing Workflows Locally

For workflow validation:

```bash
# Lint GitHub Actions workflows
actionlint .github/workflows/*.yml

# Validate TOML configuration
taplo fmt --check .gemini/commands/*.toml
```

### Required Secrets

The following GitHub secrets must be configured:

- `GEMINI_API_KEY`: Google Gemini API key
- `SLACK_API_TOKEN`: Slack bot token with chat:write permissions
- `SLACK_CHANNEL_ID`: Target Slack channel ID

## Key Files

- `.gemini/commands/analyze_market.toml`: Market analysis prompt configuration
- `.github/workflows/scheduler.yml`: Scheduled job configuration (cron: `0 */8 * * *`)
- `.github/workflows/gemini-cli-to-slack.yml`: Core workflow implementation

## Analysis Scope

The `/analyze_market` command analyzes:

- **Stock Indices**: S&P 500, NASDAQ 100, Dow Jones, Russell 2000, Nikkei 225, and major global indices
- **Commodities**: Oil (WTI/Brent), precious metals (gold, silver, platinum), copper, natural gas
- **Macro/FX**: US Treasury yields, DXY, VIX, USD/JPY, EUR/USD

Output includes:

- Key short-term drivers for each category
- Why these drivers matter for price movements
- 24-hour outlook with trend bias (bullish/bearish/sideways)
- Critical levels or events to watch

## Code Design Principles

Follow Robert C. Martin's SOLID and Clean Code principles:

### SOLID Principles

1. **SRP (Single Responsibility)**: One reason to change per class; separate concerns (e.g., storage vs formatting vs calculation)
2. **OCP (Open/Closed)**: Open for extension, closed for modification; use polymorphism over if/else chains
3. **LSP (Liskov Substitution)**: Subtypes must be substitutable for base types without breaking expectations
4. **ISP (Interface Segregation)**: Many specific interfaces over one general; no forced unused dependencies
5. **DIP (Dependency Inversion)**: Depend on abstractions, not concretions; inject dependencies

### Clean Code Practices

- **Naming**: Intention-revealing, pronounceable, searchable names (`daysSinceLastUpdate` not `d`)
- **Functions**: Small, single-task, verb names, 0-3 args, extract complex logic
- **Classes**: Follow SRP, high cohesion, descriptive names
- **Error Handling**: Exceptions over error codes, no null returns, provide context, try-catch-finally first
- **Testing**: TDD, one assertion/test, FIRST principles (Fast, Independent, Repeatable, Self-validating, Timely), Arrange-Act-Assert pattern
- **Code Organization**: Variables near usage, instance vars at top, public then private functions, conceptual affinity
- **Comments**: Self-documenting code preferred, explain "why" not "what", delete commented code
- **Formatting**: Consistent, vertical separation, 88-char limit, team rules override preferences
- **General**: DRY, KISS, YAGNI, Boy Scout Rule, fail fast

## Development Methodology

Follow Martin Fowler's Refactoring, Kent Beck's Tidy Code, and t_wada's TDD principles:

### Core Philosophy

- **Small, safe changes**: Tiny, reversible, testable modifications
- **Separate concerns**: Never mix features with refactoring
- **Test-driven**: Tests provide safety and drive design
- **Economic**: Only refactor when it aids immediate work

### TDD Cycle

1. **Red** → Write failing test
2. **Green** → Minimum code to pass
3. **Refactor** → Clean without changing behavior
4. **Commit** → Separate commits for features vs refactoring

### Practices

- **Before**: Create TODOs, ensure coverage, identify code smells
- **During**: Test-first, small steps, frequent tests, two hats rule
- **Refactoring**: Extract function/variable, rename, guard clauses, remove dead code, normalize symmetries
- **TDD Strategies**: Fake it, obvious implementation, triangulation

### When to Apply

- Rule of Three (3rd duplication)
- Preparatory (before features)
- Comprehension (as understanding grows)
- Opportunistic (daily improvements)

### Key Rules

- One assertion per test
- Separate refactoring commits
- Delete redundant tests
- Human-readable code first

> "Make the change easy, then make the easy change." - Kent Beck
