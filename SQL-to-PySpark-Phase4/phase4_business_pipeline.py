from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# -----------------------------
# Create Spark Session
# -----------------------------
spark = SparkSession.builder.appName("BusinessPipeline").getOrCreate()

# -----------------------------
# Load Datasets
# -----------------------------
customers = spark.read.option("header", "true").csv("/samples/customers.csv")
sales = spark.read.option("header", "true").csv("/samples/sales.csv")

# -----------------------------
# Create customer_name column
# -----------------------------
customers = customers.withColumn(
    "customer_name",
    concat_ws(" ", col("first_name"), col("last_name"))
)

# -----------------------------
# Data Cleaning
# -----------------------------

# Remove rows with null customer_id
customers = customers.dropna(subset=["customer_id"])
sales = sales.dropna(subset=["customer_id"])

# Remove duplicate rows
customers = customers.dropDuplicates()
sales = sales.dropDuplicates()

# Convert total_amount to numeric
sales = sales.withColumn(
    "total_amount",
    col("total_amount").cast("double")
)

# Remove invalid values
sales = sales.filter(col("total_amount") >= 0)

# -----------------------------
# Task 1: Daily Sales
# Output: sale_date, total_sales
# -----------------------------
daily_sales = sales.groupBy("sale_date") \
    .agg(sum("total_amount").alias("total_sales")) \
    .orderBy("sale_date")

print("========== Task 1: Daily Sales ==========")
daily_sales.show()

# -----------------------------
# Task 2: City-wise Revenue
# Output: city, total_revenue
# -----------------------------
city_revenue = customers.join(sales, "customer_id") \
    .groupBy("city") \
    .agg(sum("total_amount").alias("total_revenue")) \
    .orderBy(desc("total_revenue"))

print("========== Task 2: City-wise Revenue ==========")
city_revenue.show()

# -----------------------------
# Task 3: Top 5 Customers
# Output: customer_name, total_spend
# -----------------------------
top_customers = customers.join(sales, "customer_id") \
    .groupBy("customer_name") \
    .agg(sum("total_amount").alias("total_spend")) \
    .orderBy(desc("total_spend")) \
    .limit(5)

print("========== Task 3: Top 5 Customers ==========")
top_customers.show()

# -----------------------------
# Task 4: Repeat Customers
# Output: customer_id, order_count
# -----------------------------
repeat_customers = sales.groupBy("customer_id") \
    .agg(count("sale_id").alias("order_count")) \
    .filter(col("order_count") > 1)

print("========== Task 4: Repeat Customers ==========")
repeat_customers.show()

# -----------------------------
# Task 5: Customer Segmentation
# Output: customer_name, total_spend, segment
# -----------------------------
customer_spend = customers.join(sales, "customer_id") \
    .groupBy("customer_id", "customer_name") \
    .agg(sum("total_amount").alias("total_spend"))

segmentation = customer_spend.withColumn(
    "segment",
    when(col("total_spend") > 10000, "Gold")
    .when(
        (col("total_spend") >= 5000) &
        (col("total_spend") <= 10000),
        "Silver"
    )
    .otherwise("Bronze")
)

print("========== Task 5: Customer Segmentation ==========")
segmentation.show()

# -----------------------------
# Task 6: Final Reporting Table
# Output:
# customer_name, city,
# total_spend, order_count, segment
# -----------------------------
order_counts = sales.groupBy("customer_id") \
    .agg(count("sale_id").alias("order_count"))

final_df = segmentation \
    .join(
        customers.select("customer_id", "city"),
        "customer_id"
    ) \
    .join(
        order_counts,
        "customer_id"
    ) \
    .select(
        "customer_name",
        "city",
        "total_spend",
        "order_count",
        "segment"
    ) \
    .orderBy(desc("total_spend"))

print("========== Task 6: Final Reporting Table ==========")
final_df.show()

# -----------------------------
# Task 7: Save Output
# -----------------------------
final_df.write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv("/samples/output/report")

print("========== Task 7 Completed ==========")
print("Report saved successfully!")

-----------------------------
Display schema (Optional)
-----------------------------
print("Customers Schema")
customers.printSchema()

print("Sales Schema")
sales.printSchema()
