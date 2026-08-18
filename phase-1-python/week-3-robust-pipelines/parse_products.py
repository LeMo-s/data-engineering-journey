from pathlib import Path
import polars as pl
import json
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
data_file = BASE_DIR / "data" / "raw" / "products.json"
processed_data_folder = BASE_DIR / "data" / "processed"
processed_data_folder.mkdir(parents=True, exist_ok=True)
processed_data = processed_data_folder / "products_flat.csv"


def load(path):
    try:
        with open(path, 'r', encoding='utf-8') as raw_data:
            records = json.load(raw_data)
    except FileNotFoundError:
        logger.error("Could not find %s", data_file)
        raise SystemExit(1)
    else:
        logger.info("Loaded %d records from %s", len(records), data_file)
        return records

def transform(records):
    df = pl.DataFrame(records)
    df = df.unnest("category")
    logger.info("The table has %d rows and %d columns", len(df), len(df.columns))
    return df

def save(df, path):
    df.write_csv(processed_data)
    logger.info("A %d by %d table has been written in %s", len(df), len(df.columns), path)


def main():
    records = load(data_file)
    df = transform(records)
    save(df, processed_data)

if __name__ == '__main__':
    main()