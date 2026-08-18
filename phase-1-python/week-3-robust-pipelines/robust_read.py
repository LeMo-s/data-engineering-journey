from pathlib import Path
import polars as pl


BASE_DIR = Path(__file__).resolve().parent
data_file = BASE_DIR / "data" / "raw" / "doesnt_exist.csv"
processed_data_folder = BASE_DIR / "data" / "processed"
processed_data_folder.mkdir(parents=True, exist_ok=True)
processed_data = processed_data_folder / "cannot.csv"

try:
    df = pl.read_csv("C:\dev\data-engineering-journey\phase-1-python\week-2-polars\data\processed\sales_clean.csv")
except FileNotFoundError:
    print(f'Could not find: {data_file}. Check the path')
    raise SystemExit(1)
else:
    print("File loaded successfully")
    print(df)