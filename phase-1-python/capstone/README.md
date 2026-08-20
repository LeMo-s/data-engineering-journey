## What the Pipeline Does

* **`load(path)`**: Reads the raw `products_messy.json` file safely into memory using `try-except` error handling for missing files, converting it into a list of Python dictionaries.
* **`clean(records)`**: Loads data into a Polars DataFrame, standardizes strings (trimming whitespace and standardizing casing), safely parses numeric types (`strict=False`), removes duplicate entries, and drops any incomplete records containing null values.
* **`transform(clean_records)`**: Flattens the nested `category` struct into top-level columns (`type` and `origin`) and aggregates sales amounts grouped by product.
* **`save(df, path)`**: Writes the final cleaned and unnested dataset to `data/processed/products_clean_flat.csv`.

---

### Pipeline Architecture

```mermaid
flowchart TD
    A["<b>RAW DATA (JSON)</b><br/><code>data/raw/products_messy.json</code>"] 
    -->|"1. load(path)"| B["<b>CLEAN DATA (Polars)</b><br/>• Trim & lowercase 'product'<br/>• Safely cast 'amount' to Int64<br/>• Standardize nested 'category' struct<br/>• Deduplicate & drop all null rows"]
    
    B -->|"2. clean(records)"| C["<b>AGGREGATE / TRANSFORM</b><br/>• Unnest 'category' (extracts 'type' & 'origin')<br/>• Compute totals grouped by 'product'"]
    
    C -->|"3. transform(cleaned_records)"| D["<b>OUTPUT FILE (CSV)</b><br/><code>data/processed/products_clean_flat.csv</code>"]