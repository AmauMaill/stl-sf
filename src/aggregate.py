import polars as pl

def simple_agg(df: pl.DataFrame) -> pl.DataFrame:
    #
    return df.select(
        [
            pl.count().alias("Total Number of Sales"),
            pl.col("county").n_unique().alias("Number of Counties"),
            pl.col("city").n_unique().alias("Number of Cities"),
            pl.col("nhood").n_unique().alias("Number of Neighborhoods"),
            pl.col("date").min().alias("Oldest Sale"),
            pl.col("date").max().alias("Newest Sale")
        ]
    )