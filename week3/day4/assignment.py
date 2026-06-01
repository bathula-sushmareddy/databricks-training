--21. lit()
# 101
emp_df.withColumn("company_name", lit("ABC Technologies"))

# 102
emp_df.withColumn("country", lit("India"))

# 103
emp_df.withColumn("bonus", lit(5000))

# 104
emp_df.withColumn("status", lit("Active"))

# 105
emp_df.withColumn("training", lit("Yes"))

--22. when() / otherwise()
# 106
emp_df.withColumn(
    "salary_category",
    when(col("salary") > 70000, "High")
    .otherwise("Low")
)

# 107
emp_df.withColumn(
    "age_category",
    when(col("age") < 30, "Young")
    .otherwise("Senior")
)

# 108
emp_df.withColumn(
    "experience_level",
    when(col("age") < 28, "Junior")
    .otherwise("Experienced")
)

# 109
emp_df.withColumn(
    "bonus_eligible",
    when(col("salary") > 60000, "Yes")
    .otherwise("No")
)

# 110
emp_df.withColumn(
    "dept_category",
    when(col("department") == "IT", "Technical")
    .otherwise("Non-Technical")
)

--23. substring()
# 111
emp_df.withColumn("name_prefix",
                  substring("name", 1, 3))

# 112
emp_df.withColumn("join_year",
                  substring("joining_date", 1, 4))

# 113
emp_df.withColumn("dept_code",
                  substring("department", 1, 2))

# 114
emp_df.withColumn(
    "designation_suffix",
    expr("substring(designation, length(designation)-2, 3)")
)

# 115
emp_df.withColumn(
    "emp_code",
    concat(substring("name",1,3), col("emp_id"))
)


--24. regexp_replace()
  # 116
emp_df.withColumn(
    "designation",
    regexp_replace("designation", " ", "_")
)

# 117
emp_df.withColumn(
    "name",
    regexp_replace("name", "[AEIOUaeiou]", "")
)

# 118
emp_df.withColumn(
    "city",
    regexp_replace("city", "Hyderabad", "HYD")
)

# 119
emp_df.withColumn(
    "designation",
    regexp_replace("designation", "[^A-Za-z ]", "")
)

# 120
emp_df.withColumn(
    "department",
    regexp_replace("department", "IT", "Information Technology")
)

--25. like()
# 121
emp_df.filter(col("name").like("S%"))

# 122
emp_df.filter(col("designation").like("%Engineer"))

# 123
emp_df.filter(col("city").like("%a%"))

# 124
emp_df.filter(col("department").like("A%"))

# 125
emp_df.filter(col("name").like("%ra%"))

--26. isin()
# 126
emp_df.filter(
    col("city").isin("Hyderabad", "Bangalore")
)

# 127
emp_df.filter(
    col("department").isin("IT", "QA")
)

# 128
emp_df.filter(
    col("age").isin(28, 30, 35)
)

# 129
emp_df.filter(
    (col("gender") == "Female") &
    (col("city").isin("Pune", "Chennai"))
)

# 130
emp_df.filter(
    col("emp_id").isin(101, 105, 110)
)

--27. between()
# 131
emp_df.filter(
    col("salary").between(50000, 80000)
)

# 132
emp_df.filter(
    col("age").between(25, 30)
)

# 133
emp_df.filter(
    col("salary").between(60000, 90000)
)

# 134
emp_df.filter(
    year("joining_date").between(2020, 2022)
)

# 135
emp_df.filter(
    col("emp_id").between(102, 108)
)

--28. pivot()
# 136
emp_df.groupBy().pivot("department") \
      .avg("salary")

# 137
emp_df.groupBy().pivot("city") \
      .count()

# 138
emp_df.groupBy().pivot("gender") \
      .sum("salary")

# 139
emp_df.groupBy().pivot("department") \
      .max("age")

# 140
emp_df.groupBy().pivot("department") \
      .agg(avg("salary"))

--29. unpivot / stack()
# 141
pivot_df.selectExpr(
    "stack(3,'IT',IT,'HR',HR,'QA',QA) as (Department,Salary)"
)

# 142
city_df.selectExpr(
    "stack(3,'Hyd',Hyd,'Pune',Pune,'Chennai',Chennai) as (City,Count)"
)

# 143
dept_df.selectExpr(
    "stack(3,'IT',IT,'HR',HR,'QA',QA) as (Department,Value)"
)

# 144
pivot_df.selectExpr(
    "stack(3,'A',A,'B',B,'C',C) as (Key,Value)"
)

# 145
pivot_df.selectExpr(
    "stack(3,'IT',IT,'HR',HR,'QA',QA) as (Department,Metric)"
)

--30. Window Functions
from pyspark.sql.window import Window
from pyspark.sql.functions import *

window_spec = Window.orderBy(col("salary").desc())

# 146
emp_df.withColumn(
    "rank",
    rank().over(window_spec)
)

# 147
emp_df.withColumn(
    "dense_rank",
    dense_rank().over(
        Window.partitionBy("department")
              .orderBy(col("salary").desc())
    )
)

# 148
emp_df.withColumn(
    "row_num",
    row_number().over(window_spec)
)

# 149
emp_df.withColumn(
    "lead_salary",
    lead("salary").over(window_spec)
)

# 150
emp_df.withColumn(
    "lag_salary",
    lag("salary").over(window_spec)
)

--31. repartition()
# 151
emp_df.repartition(4)

# 152
emp_df.repartition("department")

# 153
emp_df.rdd.getNumPartitions()

# 154
emp_df.repartition(4)
emp_df.coalesce(2)

# 155
large_df.repartition(8)

--32. coalesce()
# 156
emp_df.coalesce(2)

# 157
emp_df.coalesce(2).rdd.getNumPartitions()

# 158
emp_df.coalesce(1).write.csv("/output")

# 159
# coalesce avoids full shuffle
emp_df.coalesce(2)

# 160
emp_df.coalesce(1)

--33. cache()
# 161
emp_df.cache()

# 162
emp_df.cache()
emp_df.count()
emp_df.show()

# 163
import time
emp_df.cache()
emp_df.count()

# 164
emp_df.cache()
emp_df.groupBy("department").avg("salary").show()

# 165
emp_df.unpersist()

--34. fillna()
# 166
emp_df.fillna({"salary": 0})

# 167
emp_df.fillna({"city": "Unknown"})

# 168
emp_df.fillna({
    "salary": 0,
    "city": "Unknown"
})

# 169
avg_age = emp_df.select(avg("age")).first()[0]
emp_df.fillna({"age": avg_age})

# 170
emp_df.fillna("N/A")

--35. replace()
# 171
emp_df.replace("Hyderabad", "HYD", "city")

# 172
emp_df.replace("IT",
               "Information Technology",
               "department")

# 173
emp_df.replace(
    {"Male": "M", "Female": "F"},
    subset=["gender"]
)

# 174
emp_df.replace("QA",
               "Testing",
               "department")

# 175
emp_df.replace(
    {
        "Hyderabad": "HYD",
        "Bangalore": "BLR"
    },
    subset=["city"]
)

  
