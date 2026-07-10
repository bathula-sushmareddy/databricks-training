# SQL-to-PySpark-Phase4A - Bucketing & Segmentation in PySpark

## Overview

This project demonstrates customer bucketing and segmentation techniques using PySpark. It classifies customers based on their total spending and compares different segmentation approaches for business analysis.

## Features

- Calculate total customer spend
- Gold, Silver, and Bronze segmentation using conditional logic
- Customer count by segment
- Quantile-based segmentation
- Bucketizer using PySpark MLlib
- Customer ranking using `percent_rank()`
- Export segmented customer data

## Technologies

- Python
- PySpark
- Spark SQL
- PySpark MLlib

  ## Project Structure

```text
SQL-to-PySpark-Phase4A/
│
├── README.md
├── phase4A_bucketing_segmentation.py
│
└── outputs/
    ├── README.md
    ├── segmented_customers.csv
    ├── conditional_segmentation.png
    ├── customer_count_by_segment.png
    ├── quantile_segmentation.png
    ├── bucketizer_output.png
    ├── window_percent_rank.png
    └── comparison.png
```

---

## Output

The generated results, screenshots, and CSV files are available in the `outputs/` folder.
