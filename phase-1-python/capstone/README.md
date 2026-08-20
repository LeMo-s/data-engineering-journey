What the Pipeline Does

    load(path): Reads the raw products_messy.json file safely into memory using try-except error handling for missing files, converting it into a list of Python dictionaries.

    clean(records): Loads data into a Polars DataFrame, standardizes strings (trimming whitespace and standardizing casing), safely parses numeric types (strict=False), removes duplicate entries, and drops any incomplete records containing null values.

    transform(clean_records): Flattens the nested category struct into top-level columns (type and origin) and aggregates sales amounts grouped by product.

    save(df, path): Writes the final cleaned and unnested dataset to data/processed/products_clean_flat.csv.


  ┌────────────────────────┐
  │   RAW DATA (JSON)      │  data/raw/products_messy.json
  └───────────┬────────────┘
              │ 1. load(path)
              ▼
  ┌────────────────────────┐
  │  CLEAN DATA (Polars)   │  • Trim & lowercase 'product'
  │                        │  • Safely cast 'amount' to Int64
  │                        │  • Standardize nested 'category' struct
  │                        │  • Deduplicate & drop all null rows
  └───────────┬────────────┘
              │ 2. clean(records)
              ▼
  ┌────────────────────────┐
  │ AGGREGATE / TRANSFORM  │  • Unnest 'category' (extracts 'type' & 'origin')
  │                        │  • Compute totals grouped by 'product'
  └───────────┬────────────┘
              │ 3. transform(cleaned_records)
              ▼
  ┌────────────────────────┐
  │  OUTPUT FILE (CSV)     │  data/processed/products_clean_flat.csv
  └────────────────────────┘

Incomplete records containing null values are removed to prevent mathematical skew and ensure accurate calculations. Additionally, duplicate rows from ingestion overlaps or retries are eliminated to prevent double-counting.