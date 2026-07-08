from pyspark.sql import SparkSession
from pyspark.sql.functions import *
# ==========================================
# Create Spark Session
# ==========================================
spark = SparkSession.builder.appName("Spark Playground").getOrCreate()
# ==========================================
# Extract - Read CSV Files
# ==========================================
customers = spark.read.option("header", "true").csv("/samples/customers.csv")
sales = spark.read.option("header", "true").csv("/samples/sales.csv")
print("===== Customers =====")
customers.show()
customers.printSchema()
print("===== Sales =====")
sales.show()
sales.printSchema()
# ==========================================
# Transform - Clean Data
# ==========================================
customers = customers.dropna(subset=["customer_id"])
sales = sales.dropna(subset=["customer_id"])
sales = sales.withColumn(
    "total_amount",
    col("total_amount").cast("double")
)
sales = sales.filter(col("total_amount") > 0)
# Create SQL Views
customers.createOrReplaceTempView("customers")
sales.createOrReplaceTempView("sales")
# ==========================================
# 1. Daily Sales
# ==========================================
print("===== Daily Sales (SQL) =====")
result = spark.sql("""
SELECT sale_date,
       SUM(total_amount) AS daily_sales
FROM sales
GROUP BY sale_date
""")
result.show()
print("===== Daily Sales (PySpark) =====")

result = sales.groupBy("sale_date") \
              .agg(sum("total_amount").alias("daily_sales"))
result.show()
