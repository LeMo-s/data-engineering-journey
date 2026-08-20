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
data_file = BASE_DIR / "data" / "raw" / "products_messy.json"
processed_data_folder = BASE_DIR / "data" / "processed"
processed_data = processed_data_folder / "products_clean_flat.csv"


def load(path):
    try:
        with open(path, 'r', encoding='utf-8') as raw_data:
            records = json.load(raw_data)
    except FileNotFoundError:
        logger.error("Could not find %s", path)
        raise SystemExit(1)
    else:
        logger.info("Loaded %d records from %s", len(records), path)
        return records

def clean(records):
    df = pl.DataFrame(records)

    clean_df = (
        df
        .with_columns([
            pl.col("product").str.strip_chars().str.to_lowercase(),
            pl.col("amount").cast(pl.Int64, strict=False),
            pl.struct([
                pl.col("category").struct.field("type").str.strip_chars().str.to_lowercase().alias("type"),
                pl.col("category").struct.field("origin").str.strip_chars().str.to_titlecase().alias("origin")
            ]).alias("category")
        ])
    )

    clean_df = clean_df.unique().drop_nulls()

    logger.info("Data cleaned")
    
    return clean_df

def transform(clean_records):

    df = clean_records.unnest("category")
    
    totals = (
        df.group_by("product")
        .agg(
            pl.col("amount").sum().alias("total_amount"),
            pl.col("type").first(),
            pl.col("origin").first() 
        )
        .sort("product")
    )
    
    logger.info("The table has %d rows and %d columns", len(totals), len(totals.columns))
    return totals

def save(df, path):
    df.write_csv(path)
    logger.info("A %d by %d table has been written in %s", len(df), len(df.columns), path)


def main():
    records = load(data_file)
    cleaned_records = clean(records)
    df = transform(cleaned_records)
    save(df, processed_data)

if __name__ == '__main__':
    main()