from pathlib import Path
import polars as pl

def load_from_path(path: Path) -> pl.DataFrame:
    #
    return pl.read_csv(path)

def load_from_url(url: str) -> pl.DataFrame:
    #
    return pl.read_csv(url)

def clean(df: pl.DataFrame) -> pl.DataFrame:
    #
    return (
        df
        .with_column(pl.col("date")
        .cast(pl.Utf8, strict=False)
        .str
        .strptime(pl.Date, "%Y%m%d"))
    )