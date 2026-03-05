import duckdb
from pathlib import Path
import pandas as pd


def run_query(query_path: str, db_path="warehouse.db"):

    conn = duckdb.connect(db_path)

    with open(query_path, "r") as f:
        query = f.read()

    df = conn.execute(query).fetchdf()

    conn.close()

    return df


def run_all_queries(sql_folder="sql"):

    results = {}

    for query_file in Path(sql_folder).glob("*.sql"):

        df = run_query(str(query_file))

        results[query_file.stem] = df

    return results