# SQL Window Functions Practice

This file contains the SQL Window Function concepts and practice queries using Employees and Orders tables.

## Topics Covered

- ROW_NUMBER()
- RANK()
- DENSE_RANK()
- PARTITION BY
- ORDER BY with Window Functions

---

# Tables Used

## Employees Table

```sql
CREATE TABLE employees (
    emp_id INT,
    emp_name VARCHAR(50),
    department VARCHAR(50),
    salary INT,
    join_date DATE
);
```

## Orders Table

```sql
CREATE TABLE orders (
    order_id INT,
    customer_name VARCHAR(50),
    city VARCHAR(50),
    amount INT,
    order_date DATE
);
```

---

# Concepts

## ROW_NUMBER()

Assigns a unique number to each row.

---

## RANK()

Assigns ranks to rows. Duplicate values get the same rank and rank numbers are skipped.


---

## DENSE_RANK()

Assigns ranks without skipping numbers.

---

# Difference Between Functions

| Function | Duplicate Rank | Skips Numbers |
|-----------|----------------|----------------|
| ROW_NUMBER() | No | No |
| RANK() | Yes | Yes |
| DENSE_RANK() | Yes | No |

