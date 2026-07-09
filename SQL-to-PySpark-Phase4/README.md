# Phase 4 – Business Pipeline & Analytics

## Objective

Build an end-to-end ETL pipeline using PySpark to clean customer and sales data, generate business insights, and prepare a final reporting table.

## Dataset

- `customers.csv`
- `sales.csv`

## ETL Pipeline

### Extract

- Loaded customer and sales datasets from the `/samples` directory using PySpark.

### Transform

- Removed rows with null `customer_id`.
- Removed duplicate records.
- Converted the `total_amount` column to the `double` data type.
- Filtered out negative transaction amounts.
- Joined customer and sales datasets using `customer_id`.
- Generated business insights through aggregation and analysis.

### Load

- Created the final reporting DataFrame.
- Displayed the final report using `show()` in Spark Playground.
- Attempted to save the report as a CSV file. However, Spark Playground provides read-only access to the `/samples` directory, so the report could not be written to `/samples/output/report`.

## Tasks Completed

- Daily Sales
- City-wise Revenue
- Top 5 Customers
- Repeat Customers
- Customer Segmentation
- Final Reporting Table

## Technologies Used

- Python
- PySpark
- Spark SQL
- DataFrames
- ETL Pipeline
- CSV Files
