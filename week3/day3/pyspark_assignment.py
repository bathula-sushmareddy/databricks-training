--1. select()
# 1
emp_df.select("name", "salary")

# 2
emp_df.select("emp_id", "department", "city")

# 3
emp_df.select("name", "age")

# 4
emp_df.select("designation", "salary")

# 5
emp_df.select("emp_id", "name", "joining_date")

--2. filter() / where()
# 6
emp_df.filter(col("salary") > 70000)

# 7
emp_df.filter(col("department") == "IT")

# 8
emp_df.filter(col("age") < 30)

# 9
emp_df.filter(col("gender") == "Female")

# 10
emp_df.filter(col("city") == "Hyderabad")

--3. withColumn()
# 11
emp_df.withColumn("bonus", col("salary") * 0.10)

# 12
emp_df.withColumn("tax", col("salary") * 0.05)

# 13
emp_df.withColumn("salary_increment", col("salary") + 5000)

# 14
emp_df.withColumn(
    "age_group",
    when(col("age") < 30, "Young").otherwise("Senior")
)

# 15
emp_df.withColumn("yearly_salary", col("salary") * 12)

--4. withColumnRenamed()
# 16
emp_df.withColumnRenamed("emp_id", "employee_id")

# 17
emp_df.withColumnRenamed("designation", "role")

# 18
emp_df.withColumnRenamed("salary", "monthly_salary")

# 19
emp_df.withColumnRenamed("city", "work_location")

# 20
emp_df.withColumnRenamed("joining_date", "doj")

--5. drop()
# 21
emp_df.drop("age")

# 22
emp_df.drop("gender")

# 23
emp_df.drop("joining_date")

# 24
emp_df.drop("city", "age")

# 25
emp_df.drop("designation")

--6. distinct()
# 26
emp_df.select("department").distinct()

# 27
emp_df.select("city").distinct()

# 28
emp_df.select("designation").distinct()

# 29
emp_df.select("gender").distinct()

# 30
emp_df.select("department", "city").distinct()

--7. dropDuplicates()
# 31
emp_df.dropDuplicates(["emp_id"])

# 32
emp_df.dropDuplicates(["department"])

# 33
emp_df.dropDuplicates(["city"])

# 34
emp_df.dropDuplicates(["department", "city"])

# 35
emp_df.dropDuplicates(["name"])

--8. sort() / orderBy()
# 36
emp_df.orderBy("salary")

# 37
emp_df.orderBy(col("age").desc())

# 38
emp_df.orderBy("department", "salary")

# 39
emp_df.orderBy("city")

# 40
emp_df.orderBy(col("joining_date").desc())

--9. groupBy()
# 41
emp_df.groupBy("department").avg("salary")

# 42
emp_df.groupBy("department").max("salary")

# 43
emp_df.groupBy("department").min("age")

# 44
emp_df.groupBy("city").count()

# 45
emp_df.groupBy("gender").sum("salary")

--10. agg()
# 46
emp_df.agg(sum("salary"))

# 47
emp_df.agg(avg("age"))

# 48
emp_df.agg(max("salary"), min("salary"))

# 49
emp_df.agg(count("*"))

# 50
emp_df.groupBy("department").agg(
    avg("salary").alias("avg_salary"),
    avg("age").alias("avg_age")
)

--11. join()
# 51 - Inner Join
emp_df.join(dept_df, "department", "inner")

# 52 - Left Join
emp_df.join(dept_df, "department", "left")

# 53 - Right Join
emp_df.join(dept_df, "department", "right")

# 54 - Full Outer Join
emp_df.join(dept_df, "department", "outer")

# 55 - Employees with Manager Names
emp_df.join(dept_df, "department").select(
    "emp_id", "name", "department", "manager"
)

--12. union()
# 56
union_df = emp_df.union(new_emp_df)

# 57
union_df.count()

# 58
union_df.distinct()

# 59
union_df.filter(col("department") == "IT")

# 60
union_df.orderBy(col("salary").desc())

--13. unionByName()
# 61
emp_df.unionByName(shuffled_df)

# 62
emp_df.unionByName(df2, allowMissingColumns=True)

# 63
emp_df.unionByName(extra_col_df, allowMissingColumns=True)

# 64
# union() -> columns by position
# unionByName() -> columns by name

# 65
emp_df.unionByName(other_schema_df, allowMissingColumns=True)

--14. limit()
# 66
emp_df.limit(3)

# 67
emp_df.limit(5)

# 68
emp_df.orderBy(col("salary").desc()).limit(2)

# 69
emp_df.filter(col("department") == "IT").limit(4)

# 70
emp_df.limit(1)

--15. sample()
# 71
emp_df.sample(False, 0.5)

# 72
emp_df.sample(False, 0.3, seed=123)

# 73
emp_df.filter(col("department")=="IT").sample(False,0.5)

# 74
print(emp_df.count())
print(emp_df.sample(False,0.5).count())

# 75
emp_df.orderBy(rand()).limit(5)

--16. explode()
# 76
skills_df.select("emp_id", explode("skills").alias("skill"))

# 77
skills_df.select(explode("skills")).count()

# 78
skills_df.filter(array_contains("skills", "Python"))

# 79
skills_df.select(explode("skills").alias("skill")).distinct()

# 80
skills_df.select(
    explode("skills").alias("skill")
).groupBy("skill").count()

--17. split()
# 81
emp_df.withColumn("year", split("joining_date","-")[0]) \
      .withColumn("month", split("joining_date","-")[1]) \
      .withColumn("day", split("joining_date","-")[2])

# 82
emp_df.withColumn("designation_words",
                  split("designation"," "))

# 83
emp_df.withColumn("city_parts",
                  split("city"," "))

# 84
emp_df.withColumn("year",
                  split("joining_date","-")[0])

# 85
emp_df.withColumn("year", split("joining_date","-")[0]) \
      .withColumn("month", split("joining_date","-")[1]) \
      .withColumn("day", split("joining_date","-")[2])

--18. concat() / concat_ws()
# 86
emp_df.withColumn(
    "name_dept",
    concat(col("name"), col("department"))
)

# 87
emp_df.withColumn(
    "details",
    concat_ws(" | ",
              "name",
              "designation",
              "department")
)

# 88
emp_df.withColumn(
    "city_dept",
    concat_ws("-", "city", "department")
)

# 89
emp_df.withColumn(
    "emp_label",
    concat_ws("_", "emp_id", "name")
)

# 90
emp_df.withColumn(
    "name_role",
    concat_ws(" - ", "name", "designation")
)

--19. cast()
# 91
emp_df.withColumn(
    "salary_double",
    col("salary").cast("double")
)

# 92
emp_df.withColumn(
    "age_string",
    col("age").cast("string")
)

# 93
emp_df.withColumn(
    "joining_date",
    to_date("joining_date")
)

# 94
emp_df.withColumn(
    "emp_id_string",
    col("emp_id").cast("string")
)

# 95
emp_df.withColumn(
    "bonus",
    (col("salary") * 0.10).cast("double")
)

--20. alias()
# 96
emp_df.select(col("salary").alias("monthly_salary"))

# 97
emp_df.select(col("department").alias("dept_name"))

# 98
emp_df.groupBy("department").agg(
    avg("salary").alias("avg_salary")
)

# 99
emp_df.agg(
    avg("salary").alias("average_salary")
)

# 100
emp_df.alias("e").join(
    dept_df.alias("d"),
    col("e.department") == col("d.department")
).select(
    "e.name",
    "d.manager"
)
