from typing import Dict
import pandas as pd
import requests
from pandas import DataFrame, read_csv, to_datetime


def get_weather_data(weather_url: str) -> DataFrame:
    """Get weather forecast data from API"""

    try:
        response = requests.get(weather_url)
        response.raise_for_status()

        data = response.json()

        # los datos útiles están aquí
        periods = data["properties"]["periods"]

        df = pd.DataFrame(periods)

    except requests.exceptions.RequestException as err:
        raise SystemExit(f"Request failed: {err}")

    return df


def extract(
    csv_folder: str,
    csv_table_mapping: Dict[str, str],
    weather_url: str
) -> Dict[str, DataFrame]:

    dataframes = {
        table_name: read_csv(f"{csv_folder}/{csv_file}")
        for csv_file, table_name in csv_table_mapping.items()
    }

    weather = get_weather_data(weather_url)

    dataframes["weather"] = weather

    return dataframes