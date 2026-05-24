SELECT
# 1. Select only emp_name and salary
df.select("emp_name", "salary").display()

# 2. Select emp_id, emp_name, and department
df.select("emp_id", "emp_name", "department").display()

# 3. Select city, designation, and salary
df.select("city", "designation", "salary").display()

# 4. Select all employees from only IT department with selected columns
df.filter(col("department") == "IT") \
  .select("emp_name", "designation", "salary").display()

# 5. Select emp_name, joining_date, and salary
df.select("emp_name", "joining_date", "salary").display()

# 6. Select first 5 columns from dataframe
df.select(df.columns[:5]).display()

# 7. Select employees whose salary column only
df.select("salary").display()

# 8. Select emp_name and city for employees from Hyderabad
df.filter(col("city") == "Hyderabad") \
  .select("emp_name", "city").display()

# 9. Select designation and department
df.select("designation", "department").display()

# 10. Select all columns except joining_date
df.drop("joining_date").display()

ALIAS
# 1. Display emp_name as employee_name
df.select(col("emp_name").alias("employee_name")).display()

# 2. Display salary as monthly_salary
df.select(col("salary").alias("monthly_salary")).display()

# 3. Display department as dept
df.select(col("department").alias("dept")).display()

# 4. Display joining_date as doj
df.select(col("joining_date").alias("doj")).display()

# 5. Select emp_name as name and city as location
df.select(
    col("emp_name").alias("name"),
    col("city").alias("location")
).display()

# 6. Display designation as job_role
df.select(col("designation").alias("job_role")).display()

# 7. Display age as employee_age
df.select(col("age").alias("employee_age")).display()

# 8. Select multiple columns using aliases
df.select(
    col("emp_id").alias("id"),
    col("emp_name").alias("name"),
    col("salary").alias("income")
).display()

# 9. Display salary as emp_salary and department as emp_dept
df.select(
    col("salary").alias("emp_salary"),
    col("department").alias("emp_dept")
).display()

# 10. Display city as work_location
df.select(col("city").alias("work_location")).display()

FILTER / WHERE
# 1. Salary greater than 70000
df.filter(col("salary") > 70000).display()

# 2. Employees from Hyderabad
df.filter(col("city") == "Hyderabad").display()

# 3. Age less than 25
df.filter(col("age") < 25).display()

# 4. Employees from IT department
df.filter(col("department") == "IT").display()

# 5. Designation is Developer
df.filter(col("designation") == "Developer").display()

# 6. Salary between 50000 and 80000
df.filter(col("salary").between(50000, 80000)).display()

# 7. Employees from Bangalore
df.filter(col("city") == "Bangalore").display()

# 8. Joined after 2022-01-01
df.filter(col("joining_date") > "2022-01-01").display()

# 9. Age greater than 30
df.filter(col("age") > 30).display()

# 10. Salary less than 50000
df.filter(col("salary") < 50000).display()

# 11. Chennai employees with salary > 60000
df.filter((col("city") == "Chennai") & (col("salary") > 60000)).display()

# 12. Employees from Mumbai or Pune
df.filter((col("city") == "Mumbai") | (col("city") == "Pune")).display()

# 13. Name starts with 'S'
df.filter(col("emp_name").startswith("S")).display()

# 14. Name ends with 'a'
df.filter(col("emp_name").endswith("a")).display()

# 15. Department is HR
df.filter(col("department") == "HR").display()

# 16. Designation contains 'Engineer'
df.filter(col("designation").contains("Engineer")).display()

# 17. City is not Hyderabad
df.filter(col("city") != "Hyderabad").display()

# 18. Age between 25 and 30
df.filter(col("age").between(25, 30)).display()

# 19. Salary greater than 90000
df.filter(col("salary") > 90000).display()

# 20. Employees from Support department
df.filter(col("department") == "Support").display()

WITHCOLUMNRENAMED
# 1. Rename emp_name to employee_name
df.withColumnRenamed("emp_name", "employee_name").display()

# 2. Rename department to dept
df.withColumnRenamed("department", "dept").display()

# 3. Rename joining_date to doj
df.withColumnRenamed("joining_date", "doj").display()

# 4. Rename salary to monthly_salary
df.withColumnRenamed("salary", "monthly_salary").display()

# 5. Rename designation to job_role
df.withColumnRenamed("designation", "job_role").display()

# 6. Rename city to work_location
df.withColumnRenamed("city", "work_location").display()

# 7. Rename age to employee_age
df.withColumnRenamed("age", "employee_age").display()

# 8. Rename multiple columns one by one
df.withColumnRenamed("emp_name", "employee_name") \
  .withColumnRenamed("salary", "monthly_salary").display()

# 9. Rename emp_id to employee_id
df.withColumnRenamed("emp_id", "employee_id").display()

# 10. Rename department to business_unit
df.withColumnRenamed("department", "business_unit").display()

WITHCOLUMN
# 1. Bonus column as 10% of salary
df.withColumn("bonus", col("salary") * 0.10).display()

# 2. Annual salary column
df.withColumn("annual_salary", col("salary") * 12).display()

# 3. Tax column as 5% of salary
df.withColumn("tax", col("salary") * 0.05).display()

# 4. Updated salary by adding 5000
df.withColumn("updated_salary", col("salary") + 5000).display()

# 5. Salary category column
df.withColumn(
    "salary_category",
    when(col("salary") >= 80000, "High")
    .when(col("salary") >= 50000, "Medium")
    .otherwise("Low")
).display()

# 6. Age group column
df.withColumn(
    "age_group",
    when(col("age") < 25, "Young")
    .otherwise("Adult")
).display()

# 7. Location column by combining city and department
df.withColumn(
    "location",
    concat_ws("-", col("city"), col("department"))
).display()

# 8. Increment salary with 15% hike
df.withColumn(
    "increment_salary",
    col("salary") * 1.15
).display()

# 9. Experience status based on joining year
df.withColumn(
    "experience_status",
    when(year(col("joining_date")) < 2021, "Experienced")
    .otherwise("New")
).display()

# 10. Name length column
df.withColumn(
    "name_length",
    length(col("emp_name"))
).display()

# 11. High salary condition column
df.withColumn(
    "is_high_salary",
    when(col("salary") > 80000, True).otherwise(False)
).display()

# 12. Joining year column
df.withColumn(
    "joining_year",
    year(col("joining_date"))
).display()

# 13. Salary after tax
df.withColumn(
    "salary_after_tax",
    col("salary") - (col("salary") * 0.05)
).display()

# 14. Department code column
df.withColumn(
    "department_code",
    upper(substring(col("department"), 1, 3))
).display()

# 15. Double salary column
df.withColumn(
    "double_salary",
    col("salary") * 2
).display()

TYPECASTING
# 1. Salary to string
df.withColumn("salary", col("salary").cast("string")).display()

# 2. Age to double
df.withColumn("age", col("age").cast("double")).display()

# 3. Joining_date to date
df.withColumn("joining_date", col("joining_date").cast("date")).display()

# 4. emp_id to string
df.withColumn("emp_id", col("emp_id").cast("string")).display()

# 5. Salary to integer
df.withColumn("salary", col("salary").cast("int")).display()

# 6. Age to string
df.withColumn("age", col("age").cast("string")).display()

# 7. Joining_date to timestamp
df.withColumn("joining_date", col("joining_date").cast("timestamp")).display()

# 8. Salary to float
df.withColumn("salary", col("salary").cast("float")).display()

# 9. emp_id to long
df.withColumn("emp_id", col("emp_id").cast("long")).display()

# 10. Multiple columns casting
df.withColumn("salary", col("salary").cast("double")) \
  .withColumn("age", col("age").cast("string")) \
  .withColumn("joining_date", col("joining_date").cast("date")).display()

SORT / ORDERBY
# 1. Salary ascending
df.orderBy("salary").display()

# 2. Salary descending
df.orderBy(col("salary").desc()).display()

# 3. Age descending
df.orderBy(col("age").desc()).display()

# 4. emp_name ascending
df.orderBy("emp_name").display()

# 5. City and salary descending
df.orderBy("city", col("salary").desc()).display()

# 6. Joining date
df.orderBy("joining_date").display()

# 7. Department
df.orderBy("department").display()

# 8. Designation descending
df.orderBy(col("designation").desc()).display()

# 9. First city then age
df.orderBy("city", "age").display()

# 10. Salary and limit top 10
df.orderBy(col("salary").desc()).limit(10).display()

# 11. emp_id descending
df.orderBy(col("emp_id").desc()).display()

# 12. IT employees salary descending
df.filter(col("department") == "IT") \
  .orderBy(col("salary").desc()).display()

# 13. Joining date descending
df.orderBy(col("joining_date").desc()).display()

# 14. Alphabetically by emp_name
df.orderBy("emp_name").display()

# 15. Multiple columns sorting
df.orderBy("department", col("salary").desc()).display()

LIMIT
# 1. First 5 records
df.limit(5).display()

# 2. Top 10 employees
df.limit(10).display()

# 3. First 3 employees from IT department
df.filter(col("department") == "IT").limit(3).display()

# 4. Top 5 highest salary employees
df.orderBy(col("salary").desc()).limit(5).display()

# 5. Lowest 5 salary employees
df.orderBy("salary").limit(5).display()

# 6. First 7 rows after sorting by age
df.orderBy("age").limit(7).display()

# 7. First 2 employees from Hyderabad
df.filter(col("city") == "Hyderabad").limit(2).display()

# 8. First 15 records from dataframe
df.limit(15).display()

# 9. Top 5 youngest employees
df.orderBy("age").limit(5).display()

# 10. First 8 employees after filtering salary > 60000
df.filter(col("salary") > 60000).limit(8).display()
