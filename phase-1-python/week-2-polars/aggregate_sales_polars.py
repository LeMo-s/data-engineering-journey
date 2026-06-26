from pathlib import Path
import polars as pl


BASE_DIR = Path(__file__).resolve().parent
data_file = BASE_DIR / "data" / "raw" / "sales.csv"
processed_data_folder = BASE_DIR / "data" / "processed"
processed_data_folder.mkdir(parents=True, exist_ok=True)
processed_data = processed_data_folder / "processed.csv"

df = pl.read_csv(data_file)
totals = df.group_by("product").agg(pl.col("amount").sum().alias("total_amount")).sort("product")
totals.write_csv(processed_data)
print(totals)