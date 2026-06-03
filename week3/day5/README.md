# PySpark Transformations Practice Questions

## Overview

This file contains practice questions and solutions for advanced PySpark DataFrame, RDD, optimization, aggregation, and performance-related transformations.

---

## Covered Topics

36. na.drop()
37. na.fill()
38. map() (RDD)
39. flatMap() (RDD)
40. reduceByKey() (RDD)
41. mapPartitions()
42. zipWithIndex()
43. crossJoin()
44. except()
45. intersect()
46. cube()
47. rollup()
48. broadcast()
49. explode_outer()
50. array_contains()

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

employee_data = [
(101, "Sravan", "Data Engineer", "IT", 75000, "Hyderabad", 28,
"2021-05-10", "Male"),
(102, "Ravi", "Software Engineer", "IT", 68000, "Bangalore", 30,
"2020-03-15", "Male"),
(103, "Priya", "Data Analyst", "Analytics", 62000, "Chennai", 26,
"2022-01-12", "Female"),
(104, "Kiran", "Manager", "HR", 90000, "Mumbai", 35,
"2018-07-19", "Male"),
(105, "Anjali", "HR Executive", "HR", 45000, "Pune", 24,
"2023-02-20", "Female"),
(106, "Vikram", "Data Scientist", "Analytics", 98000, "Delhi", 32,
"2019-11-25", "Male"),
(107, "Sneha", "Developer", "IT", 71000, "Hyderabad", 27,
"2021-08-17", "Female"),
(108, "Rahul", "Tester", "QA", 55000, "Chennai", 29,
"2020-06-10", "Male"),
(109, "Meena", "QA Lead", "QA", 83000, "Bangalore", 33,
"2017-09-14", "Female"),
(110, "Arjun", "Support Engineer", "Support", 50000, "Pune", 31,
"2022-04-11", "Male")
]

columns = [
    "emp_id", "name", "designation", "department",
    "salary", "city", "age", "joining_date", "gender"
]

emp_df = spark.createDataFrame(employee_data, columns)

emp_df.show()
```

---

## 36. na.drop()

Remove rows containing null values.

### Key Methods

```python
na.drop()
na.drop(how="all")
na.drop(thresh=5)
na.drop(subset=["column"])
```

---

## 37. na.fill()

Replace null values with specified values.

### Key Methods

```python
na.fill()
fillna()
```

---

## 38. map() (RDD)

Transform each RDD record.

### Example

```python
emp_df.rdd.map(
    lambda x: x.name.upper()
)
```

---

## 39. flatMap() (RDD)

Transform and flatten records.

### Example

```python
sentence_rdd.flatMap(
    lambda x: x.split(" ")
)
```

---

## 40. reduceByKey() (RDD)

Aggregate values having the same key.

### Example

```python
rdd.reduceByKey(
    lambda a, b: a + b
)
```

---

## 41. mapPartitions()

Process records partition-wise.

### Example

```python
emp_df.rdd.mapPartitions(
    lambda rows: [
        (r.emp_id, r.name.upper())
        for r in rows
    ]
)
```

---

## 42. zipWithIndex()

Generate index values for records.

### Example

```python
emp_df.rdd.zipWithIndex()
```

---

## 43. crossJoin()

Generate Cartesian product.

### Example

```python
emp_df.crossJoin(dept_df)
```

---

## 44. except()

Find records present in one DataFrame but not another.

### Example

```python
emp_df.exceptAll(new_emp_df)
```

---

## 45. intersect()

Find common records between DataFrames.

### Example

```python
emp_df.intersect(new_emp_df)
```

---

## 46. cube()

Perform multidimensional aggregations.

### Example

```python
emp_df.cube(
    "department",
    "city"
).sum("salary")
```

---

## 47. rollup()

Generate hierarchical aggregations.

### Example

```python
emp_df.rollup(
    "department",
    "city"
).sum("salary")
```

---

## 48. broadcast()

Optimize joins using small lookup tables.

### Example

```python
from pyspark.sql.functions import broadcast

emp_df.join(
    broadcast(dept_df),
    "department"
)
```

---

## 49. explode_outer()

Explode arrays while preserving null values.

### Example

```python
skills_df.select(
    explode_outer("skills")
)
```

---

## 50. array_contains()

Search values inside arrays.

### Example

```python
skills_df.filter(
    array_contains(
        "skills",
        "Python"
    )
)
```
