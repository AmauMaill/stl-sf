import polars as pl
from src.aggregate import simple_agg
from src.process import clean

df_path = "./rent.csv"
df = pl.read_csv(df_path)

print(df.head())

print(
    df.select(
        [
            pl.col("county").n_unique(),
            pl.col("city").n_unique(),
            pl.col("nhood").n_unique()
        ]
    )
)

print(
    df.select(
        [
            pl.col("date").min().alias("min_date"),
            pl.col("date").max().alias("max_date")
        ]
    )
)

print(df.columns)

print(df.with_column(pl.col("date").cast(pl.Utf8, strict=False).str.strptime(pl.Date, "%Y%m%d")))

smr_prices = (
            df
            .groupby(["year", "county"])
            .agg(
                [
                    pl.count("price").alias("n_prices"),
                    pl.mean("price").alias("meab_prices"),
                    pl.median("price").alias("median_prices"),
                    pl.std("price").alias("str_prices"),
                    pl.min("price").alias("min_prices"),
                    pl.max("price").alias("max_prices")
                ]
            )
        )

print(smr_prices)

df_clean = clean(df=df)
print(simple_agg(df=df_clean))