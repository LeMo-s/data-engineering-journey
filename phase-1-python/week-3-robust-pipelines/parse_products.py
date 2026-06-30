from pathlib import Path
import polars as pl
import json


BASE_DIR = Path(__file__).resolve().parent
data_file = BASE_DIR / "data" / "raw" / "products.json"
processed_data_folder = BASE_DIR / "data" / "processed"
processed_data_folder.mkdir(parents=True, exist_ok=True)
processed_data = processed_data_folder / "products_flat.csv"

try:
    with open(data_file, 'r', encoding='utf-8') as raw_data:
        records = json.load(raw_data)
except FileNotFoundError:
    print(f'Could not find: {data_file}. Check the path')
    raise SystemExit(1)
else:
    print("File loaded successfully")

df = pl.DataFrame(records)
print(df)
df = df.unnest("category")
print(df)
df.write_csv(processed_data)
