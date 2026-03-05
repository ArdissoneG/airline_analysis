from src.extract import extract
from src.load import load
from src.transform import run_all_queries
from src.config import CSV_FOLDER, CSV_TABLE_MAPPING, WEATHER_URL


def main():

    dataframes = extract(
        CSV_FOLDER,
        CSV_TABLE_MAPPING,
        WEATHER_URL
    )

    load(dataframes)

    results = run_all_queries()

    print(results["delays_by_airline"].head())


if __name__ == "__main__":
    main()