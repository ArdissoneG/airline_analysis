from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from src.extract import extract
from src.transform import transform
from src.load import load


with DAG(
    dag_id="airline_delay_pipeline",
    start_date=datetime(2024,1,1),
    schedule="@daily",
    catchup=False
) as dag:

    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract
    )

    transform_task = PythonOperator(
        task_id="transform",
        python_callable=transform
    )

    load_task = PythonOperator(
        task_id="load",
        python_callable=load
    )

    extract_task >> transform_task >> load_task