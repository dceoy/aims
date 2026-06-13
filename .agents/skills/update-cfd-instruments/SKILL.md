---
name: update-cfd-instruments
description: Create or update data/cfd_instruments.csv from GMO Click Securities and Rakuten Securities CFD lineup pages, including ticker symbols.
---

# Update CFD instruments

Use this skill when the user asks to create, refresh, update, or repair the CFD master table for tradable CFDs at GMO Click Securities (`クリック証券`, `Click sec.`) and Rakuten Securities (`楽天証券`, `Rakuten sec.`).

## Output

The canonical output file is:

```text
data/cfd_instruments.csv
```

The CSV contains one row per broker CFD listing and includes:

- broker, source URL, category, section, and sector
- instrument name and `ticker_symbol`
- underlying asset / exchange, currency, tick size, price display example, trade unit, trading hours, leverage/margin, quantity limits, and adjustment notes

## Ticker mappings

Ticker symbol mappings are stored in:

```text
data/mappings/cfd_ticker_mappings.csv
```

The file uses the following columns:

| Column | Description |
|---|---|
| `mapping_type` | `broker_instrument`, `instrument`, or `gmo_stock_base` |
| `broker` | Broker name (for `broker_instrument` and `gmo_stock_base`) |
| `category` | CFD category (informational; used to label `gmo_stock_base` rows) |
| `instrument_name` | Instrument name key (for `broker_instrument` and `instrument`) |
| `base_name` | Base name after stripping exchange suffix (for `gmo_stock_base`) |
| `ticker_symbol` | Resulting ticker symbol |

Lookup precedence in the updater:

1. Parse the `underlying_asset_exchange` field for a leading uppercase exchange code.
2. Look up `(broker, instrument_name)` in `broker_instrument` rows.
3. Look up `instrument_name` in `instrument` rows.
4. For GMO 株式CFD, strip the `（NASDAQ）`/`（NYSE）` suffix and look up the base name in `gmo_stock_base` rows.

To add or update a mapping, edit `data/mappings/cfd_ticker_mappings.csv` directly and re-run the updater.

## Schema and validation

The CSV schema is defined in:

```text
data/schema/cfd_instruments.schema.json
```

The schema specifies required columns, required non-empty fields, allowed broker values, the ticker symbol pattern, and the uniqueness key `(broker, instrument_name, source_url)`.

Validate the CSV at any time:

```bash
python3 .agents/skills/update-cfd-instruments/scripts/validate_cfd_instruments.py \
  --input data/cfd_instruments.csv \
  --schema data/schema/cfd_instruments.schema.json
```

The validator prints actionable errors with row numbers and exits non-zero on failure.

## Procedure

1. Run the updater from the repository root:

   ```bash
   python3 .agents/skills/update-cfd-instruments/scripts/update_cfd_instruments.py \
     --output data/cfd_instruments.csv
   ```

2. If the script reports missing ticker mappings, add the missing entries to
   `data/mappings/cfd_ticker_mappings.csv` and rerun. Do not leave blank ticker symbols.

3. Run the validator to confirm the output is well-formed:

   ```bash
   python3 .agents/skills/update-cfd-instruments/scripts/validate_cfd_instruments.py
   ```

## Notes

- The updater fetches the official public lineup pages:
  - `https://www.click-sec.com/corp/guide/cfd/lineup/`
  - `https://www.rakuten-sec.co.jp/web/rcfd/lineup/`
- Both the updater and the validator use only Python's standard library.
- Ticker symbols are exchange/product root symbols. If a CFD source references multiple venues for one instrument, symbols are semicolon-separated.
- The scheduled refresh workflow (`.github/workflows/update-cfd-instruments.yml`) runs every Monday, opens a PR only when instrument data changes, and applies the labels `agent:chatgpt`, `model:gpt-5.5`, and `priority:p1` when they exist in the repository.
