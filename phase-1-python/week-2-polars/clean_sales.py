from pathlib import Path
import polars as pl


BASE_DIR = Path(__file__).resolve().parent
data_file = BASE_DIR / "data" / "raw" / "sales_messy.csv"
processed_data_folder = BASE_DIR / "data" / "processed"
processed_data_folder.mkdir(parents=True, exist_ok=True)
processed_data = processed_data_folder / "sales_clean.csv"

df = pl.read_csv(data_file)
print(df)

df = df.with_columns(
    pl.col("product").str.strip_chars().str.to_lowercase()
)

df = df.drop_nulls()        
df = df.unique() 

totals = df.group_by("product").agg(pl.col("amount").sum().alias("total_amount")).sort("product")
totals.write_csv(processed_data)

print(totals)