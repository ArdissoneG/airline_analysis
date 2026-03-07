import logging

from extract import extract
from load import load
from transform import run_all_queries
from visualize import plot_delays_by_airline, plot_monthly_delay
from config import CSV_FOLDER, CSV_TABLE_MAPPING, WEATHER_URL

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():

    logging.info("Starting pipeline")

    logging.info("Extracting data")
    dataframes = extract(CSV_FOLDER, CSV_TABLE_MAPPING, WEATHER_URL)

    logging.info("Loading data into warehouse")
    load(dataframes)

    logging.info("Running transformations")
    results = run_all_queries()

    logging.info("Generating visualizations")
    plot_delays_by_airline(results["delays_by_airline"])
    plot_monthly_delay(results["monthly_delay_trend"])

    logging.info("Pipeline finished successfully")


if __name__ == "__main__":
    main()