## 36. na.drop()

# 176
emp_df.na.drop(subset=["salary"])

# 177
emp_df.na.drop()

# 178
emp_df.na.drop(how="all")

# 179
emp_df.na.drop(thresh=5)

# 180
emp_df.na.drop(subset=["city"])


## 37. na.fill()

# 181
emp_df.na.fill({"age": 25})

# 182
emp_df.na.fill({"department": "Unknown"})

# 183
avg_salary = emp_df.select(avg("salary")).first()[0]
emp_df.na.fill({"salary": avg_salary})

# 184
emp_df.na.fill({
    "age": 25,
    "city": "Unknown"
})

# 185
emp_df.na.fill("N/A")


## 38. map() (RDD)

# 186
emp_df.rdd.map(
    lambda x: x.name.upper()
)

# 187
emp_df.rdd.map(
    lambda x: (x.name, x.salary * 1.10)
)

# 188
emp_df.rdd.map(
    lambda x: x.name
)

# 189
emp_df.rdd.map(
    lambda x: x.department.lower()
)

# 190
emp_df.rdd.map(
    lambda x: f"{x.name}-{x.department}-{x.salary}"
)


## 39. flatMap() (RDD)

# 191
emp_df.select("name").rdd.flatMap(
    lambda x: list(x[0])
)

# 192
emp_df.select("designation").rdd.flatMap(
    lambda x: x[0].split(" ")
)

# 193
skills_df.rdd.flatMap(
    lambda x: x.skills
)

# 194
nested_rdd.flatMap(lambda x: x)

# 195
sentence_rdd.flatMap(
    lambda x: x.split(" ")
)


## 40. reduceByKey() (RDD)

# 196
emp_df.rdd.map(
    lambda x: (x.department, 1)
).reduceByKey(lambda a, b: a + b)

# 197
emp_df.rdd.map(
    lambda x: (x.department, x.salary)
).reduceByKey(lambda a, b: a + b)

# 198
emp_df.rdd.map(
    lambda x: (x.city, 1)
).reduceByKey(lambda a, b: a + b)

# 199
emp_df.rdd.map(
    lambda x: (x.department, x.age)
).reduceByKey(lambda a, b: a + b)

# 200
emp_df.rdd.map(
    lambda x: (x.city, x.salary)
).reduceByKey(max)


## 41. mapPartitions()

# 201
emp_df.rdd.mapPartitions(lambda x: x)

# 202
emp_df.rdd.mapPartitions(
    lambda x: [sum(1 for _ in x)]
)

# 203
emp_df.rdd.mapPartitions(
    lambda rows: [
        (r.emp_id, r.name.upper())
        for r in rows
    ]
)

# 204
emp_df.rdd.mapPartitions(process_partition)

# 205
emp_df.rdd.mapPartitions(custom_function)


## 42. zipWithIndex()

# 206
emp_df.rdd.zipWithIndex()

# 207
emp_df.rdd.zipWithIndex().map(
    lambda x: (x[1] + 1, x[0])
)

# 208
emp_df.rdd.zipWithIndex()

# 209
emp_df.rdd.zipWithIndex()

# 210
emp_df.rdd.zipWithIndex().collect()


## 43. crossJoin()

# 211
emp_df.crossJoin(dept_df)

# 212
emp_df.crossJoin(dept_df)

# 213
emp_df.crossJoin(dept_df).count()

# 214
city_df.crossJoin(dept_df)

# 215
emp_df.crossJoin(dept_df)


## 44. except()

# 216
emp_df.exceptAll(new_emp_df)

# 217
df1.exceptAll(df2)

# 218
emp_df.exceptAll(new_emp_df)

# 219
df1.exceptAll(df2)

# 220
emp_df.exceptAll(new_emp_df).show()


## 45. intersect()

# 221
emp_df.intersect(new_emp_df)

# 222
df1.intersect(df2)

# 223
emp_df.select("department").intersect(
    new_emp_df.select("department")
)

# 224
emp_df.select("city").intersect(
    new_emp_df.select("city")
)

# 225
emp_df.intersect(new_emp_df).show()


## 46. cube()

# 226
emp_df.cube(
    "department",
    "city"
).sum("salary")

# 227
emp_df.cube(
    "department",
    "city"
).count()

# 228
emp_df.cube(
    "department",
    "city"
).avg("salary")

# 229
emp_df.cube(
    "department",
    "city"
).agg(sum("salary"))

# 230
emp_df.cube(
    "department",
    "city"
).show()


## 47. rollup()

# 231
emp_df.rollup(
    "department",
    "city"
).sum("salary")

# 232
emp_df.rollup(
    "department",
    "city"
).count()

# 233
emp_df.rollup(
    "department",
    "city"
).agg(sum("salary"))

# 234
emp_df.rollup(
    "department",
    "city"
).show()

# 235
emp_df.rollup(
    "department",
    "city"
).count()


## 48. broadcast()

# 236
from pyspark.sql.functions import broadcast

emp_df.join(
    broadcast(dept_df),
    "department"
)

# 237
emp_df.join(
    broadcast(dept_df),
    "department"
).explain()

# 238
emp_df.join(
    broadcast(dept_df),
    "department"
)

# 239
emp_df.join(
    broadcast(dept_df),
    "department"
)

# 240
emp_df.join(
    broadcast(dept_df),
    "department"
).explain(True)


## 49. explode_outer()

# 241
skills_df.select(
    explode_outer("skills")
)

# 242
skills_df.select(
    explode_outer("skills")
)

# 243
skills_df.select(
    "emp_id",
    explode_outer("skills")
)

# 244
skills_df.select(
    explode_outer("skills")
).show()

# 245
skills_df.select(
    "emp_id",
    explode_outer("skills").alias("skill")
)


## 50. array_contains()

# 246
skills_df.filter(
    array_contains("skills", "Spark")
)

# 247
skills_df.filter(
    array_contains("skills", "Python")
)

# 248
skills_df.filter(
    array_contains("skills", "SQL")
)

# 249
skills_df.filter(
    array_contains("skills", "Azure")
)

# 250
skills_df.select(
    "emp_id",
    array_contains("skills", "Azure")
    .alias("has_azure")
)
