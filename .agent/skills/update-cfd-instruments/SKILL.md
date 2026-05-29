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

## Procedure

1. Run the updater from the repository root:

   ```bash
   python3 .agent/skills/update-cfd-instruments/scripts/update_cfd_instruments.py --output data/cfd_instruments.csv
   ```

2. If the script reports missing ticker mappings, update the symbol maps in `scripts/update_cfd_instruments.py` and rerun it. Do not leave blank ticker symbols.

3. Confirm the generated CSV has rows and no blank required fields:

   ```bash
   python3 - <<'PY'
   import csv
   from collections import Counter

   with open('data/cfd_instruments.csv', encoding='utf-8', newline='') as fh:
       rows = list(csv.DictReader(fh))

   assert rows
   assert all(r['broker'] and r['category'] and r['instrument_name'] and r['ticker_symbol'] for r in rows)
   print('rows', len(rows))
   print(Counter((r['broker'], r['category']) for r in rows))
   PY
   ```

## Notes

- The updater fetches the official public lineup pages:
  - `https://www.click-sec.com/corp/guide/cfd/lineup/`
  - `https://www.rakuten-sec.co.jp/web/rcfd/lineup/`
- The updater uses only Python's standard library.
- Ticker symbols are exchange/product root symbols. If a CFD source references multiple venues for one instrument, symbols are semicolon-separated.
