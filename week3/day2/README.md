# PySpark DataFrame Operations Practice

This file contains basic and important PySpark DataFrame operations used in Databricks.

---

# Import Required Functions

```python
from pyspark.sql.functions import *
```

---

# Create Employee Dataset

```python
data = [
    (1, "Sravan", 25, "Hyderabad", "Data Engineer", 55000, "2023-01-15", "IT"),
    (2, "Ravi", 28, "Bangalore", "Software Engineer", 72000, "2022-11-10", "IT"),
    (3, "Priya", 24, "Chennai", "Analyst", 48000, "2023-03-12", "Analytics"),
    (4, "Kiran", 30, "Pune", "Manager", 85000, "2021-09-20", "Management"),
    (5, "Sneha", 27, "Mumbai", "HR", 45000, "2020-05-18", "HR")
]
```

---

# Define Column Names

```python
columns = [
    "emp_id",
    "emp_name",
    "age",
    "city",
    "designation",
    "salary",
    "joining_date",
    "department"
]
```

---

# Create DataFrame

```python
df = spark.createDataFrame(data, columns)
```

---

# Display DataFrame

```python
df.display()
```

---

# Dataset Columns

The dataset contains:

- emp_id
- emp_name
- age
- city
- designation
- salary
- joining_date
- department

---
