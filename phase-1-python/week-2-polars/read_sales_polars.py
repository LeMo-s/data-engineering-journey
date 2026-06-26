from pathlib import Path
import polars as pl

BASE_DIR = Path(__file__).resolve().parent
data_file = BASE_DIR / "data" / "raw" / "sales.csv"

df = pl.read_csv(data_file)
print(df)
print(df.shape)
print(df.schema)