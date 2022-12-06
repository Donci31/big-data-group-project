import pandas as pd
import os


os.makedirs('2019', exist_ok=True)
os.makedirs('2020', exist_ok=True)
os.makedirs('ossz', exist_ok=True)

for year in (2019, 2020):
    for month in range(1, 13):
        (
            pd
            .read_parquet(f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month:02d}.parquet')
            .to_parquet(f'{year}/{year}-{month:02d}.parquet')
        )
        