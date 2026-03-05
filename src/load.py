import duckdb
from pandas import DataFrame


def load(dataframes: dict, db_path: str = "warehouse.db"):

    conn = duckdb.connect(db_path)

    for table_name, df in dataframes.items():

        conn.execute(f"""
        CREATE OR REPLACE TABLE {table_name} AS
        SELECT * FROM df
        """)

    conn.close()