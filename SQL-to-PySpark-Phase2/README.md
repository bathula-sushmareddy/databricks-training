# SQL to PySpark – Phase 2: SQL to PySpark Bridge Pack

## Overview

This repository contains solutions for the SQL to PySpark Bridge Pack (Phase 2). The exercises demonstrate how common SQL operations can be implemented using PySpark DataFrame APIs on sample datasets from Spark Playground.

## Datasets

- customers.csv
- sales.csv

## Data Preparation

The following preprocessing steps were performed before solving the exercises:

- Loaded CSV datasets with headers
- Removed records with missing `customer_id`
- Verified dataset schema
- Inspected sample records for validation

## Exercises

1. Total order amount for each customer
2. Top 3 customers by total spend
3. Customers with no orders
4. City-wise total revenue
5. Average order amount per customer
6. Customers with multiple orders
7. Sort customers by total spend

## Technologies Used

- Python
- PySpark
- Apache Spark
- Spark Playground

## Repository Structure

```text
SQL-to-PySpark-Phase2/
│
├── sql/
│   ├── 01_total_order_amount.sql
│   ├── 02_top3_customers.sql
│   ├── 03_customers_no_orders.sql
│   ├── 04_city_wise_revenue.sql
│   ├── 05_average_order_amount.sql
│   ├── 06_customers_multiple_orders.sql
│   └── 07_sort_total_spend.sql
│
├── pyspark/
│   ├── 01_total_order_amount.py
│   ├── 02_top3_customers.py
│   ├── 03_customers_no_orders.py
│   ├── 04_city_wise_revenue.py
│   ├── 05_average_order_amount.py
│   ├── 06_customers_multiple_orders.py
│   └── 07_sort_total_spend.py
│
├── outputs/
│   ├── exercise1.png
│   ├── exercise2.png
│   ├── exercise3.png
│   ├── exercise4.png
│   ├── exercise5.png
│   ├── exercise6.png
│   └── exercise7.png
│
└── README.md
```

## Project Contents

- SQL solutions for all Phase 2 exercises
- Equivalent PySpark DataFrame implementations
- Output screenshots for each exercise
- Project documentation with repository structure and execution details
