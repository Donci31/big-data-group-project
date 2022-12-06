import pandas as pd
import os
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile


def main() -> None:
    os.makedirs('2019', exist_ok=True)
    os.makedirs('2020', exist_ok=True)
    os.makedirs('sum', exist_ok=True)
    os.makedirs('taxi_zones', exist_ok=True)

    with urlopen('https://data.cityofnewyork.us/api/geospatial/d3c5-ddgc?method=export&format=Original') as zip_resp:
        with ZipFile(BytesIO(zip_resp.read())) as file:
            file.extractall('taxi_zones')

    for year in (2019, 2020):
        for month in range(1, 13):
            (
                pd
                .read_parquet(f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month:02d}.parquet')
                .to_parquet(f'{year}/{year}-{month:02d}.parquet')
            )


if __name__ == '__main__':
    main()