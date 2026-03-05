from src.extract import extract
from src.config import CSV_FOLDER, CSV_TABLE_MAPPING, WEATHER_URL


def test_extract():

    dfs = extract(CSV_FOLDER, CSV_TABLE_MAPPING, WEATHER_URL)

    assert "flights" in dfs
    assert "airlines" in dfs
    assert "airports" in dfs