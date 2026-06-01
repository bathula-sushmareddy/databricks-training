# PySpark Transformations Practice Questions Master

## Overview
This file contains practice questions and solutions for 20 commonly used PySpark transformations and operations.

## Covered Topics

1. select()
2. filter() / where()
3. withColumn()
4. withColumnRenamed()
5. drop()
6. distinct()
7. dropDuplicates()
8. sort() / orderBy()
9. groupBy()
10. agg()
11. join()
12. union()
13. unionByName()
14. limit()
15. sample()
16. explode()
17. split()
18. concat() / concat_ws()
19. cast()
20. alias()

---

## Installation

```bash
pip install pyspark
```

## Create Spark Session

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("PySparkPractice") \
    .getOrCreate()
```

---

## Example Dataset

```python
from pyspark.sql.functions import *
# Employee Dataset
employee_data = [
(101, "Sravan", "Data Engineer", "IT", 75000, "Hyderabad", 28,
"2021-05-10", "Male"),
(102, "Ravi", "Software Engineer", "IT", 68000, "Bangalore", 30,
"2020-03-15", "Male"),
(103, "Priya", "Data Analyst", "Analytics", 62000, "Chennai", 26,
"2022-01-12", "Female"),
(104, "Kiran", "Manager", "HR", 90000, "Mumbai", 35, "2018-07-19",
"Male"),
(105, "Anjali", "HR Executive", "HR", 45000, "Pune", 24, "2023-02-20",
"Female"),
(106, "Vikram", "Data Scientist", "Analytics", 98000, "Delhi", 32,
"2019-11-25", "Male"),
(107, "Sneha", "Developer", "IT", 71000, "Hyderabad", 27, "2021-08-17",
"Female"),
(108, "Rahul", "Tester", "QA", 55000, "Chennai", 29, "2020-06-10",
"Male"),
(109, "Meena", "QA Lead", "QA", 83000, "Bangalore", 33, "2017-09-14",
"Female"),
(110, "Arjun", "Support Engineer", "Support", 50000, "Pune", 31,
"2022-04-11", "Male")
]
columns = ["emp_id", "name", "designation", "department", "salary", "city",
"age", "joining_date", "gender"]
emp_df = spark.createDataFrame(employee_data, columns)
emp_df.show()
```

---
