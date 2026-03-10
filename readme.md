# Airline Delay ETL Pipeline

## Project Overview

This project implements a simple **ETL data pipeline** to analyze airline delay data.
The pipeline extracts flight data, performs transformations to compute metrics such as delays and cancellation rates, and generates visualizations to explore patterns in airline performance.

The goal of the project is to demonstrate a basic **data engineering workflow**, including modular pipeline components and workflow orchestration.

---

## Project Structure

```
project/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── dags/
│   └── airline_delay_pipeline.py
│
├── graficos/
│   ├── hist_sales.png
│   ├── cancellation_rate.png
│   └── delay_heatmap.png
│
├── visualizaciones.py
└── README.md
```

* **extract.py** → loads the raw dataset
* **transform.py** → cleans and aggregates the data
* **load.py** → saves the processed data
* **visualizaciones.py** → generates plots to analyze delay patterns
* **dags/** → Airflow DAG used to orchestrate the pipeline

---

## ETL Pipeline

The project follows the standard **ETL architecture**:

1. **Extract**

   * Load airline delay dataset.

2. **Transform**

   * Clean missing values
   * Compute delay statistics
   * Aggregate delays by airline, month, and day.

3. **Load**

   * Store processed results and generate visualizations.

---

## Visualizations

The analysis generates several plots to explore flight performance.

### Cancellation Rate by Airline

This visualization shows the cancellation rate for different airlines.

**Insight**

Cancellation rates vary across airlines. Some carriers show noticeably higher cancellation rates, suggesting differences in operational reliability.

---

### Distribution of Arrival Delays

This histogram shows the distribution of flight arrival delays.

**Insight**

Most flights experience small delays or arrive close to schedule. However, the distribution is right-skewed, meaning that large delays occur less frequently but still significantly affect overall performance.

---

### Average Flight Delay Heatmap

The heatmap shows average delays by **month** and **day of the week**.

**Insight**

Average delays vary across both months and days of the week, suggesting potential seasonal or operational patterns that influence airline performance.

---

## Key Findings

* Cancellation rates differ significantly between airlines.
* Most flights experience small delays, but extreme delays still occur.
* Delay patterns vary across months and days of the week.
* These patterns may be influenced by operational efficiency, travel demand, or seasonal factors.

---

## Technologies Used

* Python
* Pandas
* DuckDB
* Matplotlib
* Apache Airflow

---

## Future Improvements

Possible extensions for the project:

* Add automated scheduling with Airflow.
* Include more advanced delay analysis.
* Store processed data in a data warehouse.
* Build a dashboard for interactive exploration.

---