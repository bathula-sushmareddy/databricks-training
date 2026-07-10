from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, when, percent_rank
from pyspark.sql.window import Window
from pyspark.ml.feature import Bucketizer

# ------------------------------------
# Create Spark Session
# ------------------------------------
spark = SparkSession.builder \
    .appName("Phase4A - Bucketing & Segmentation") \
    .getOrCreate()

# ------------------------------------
# Load Data
# ------------------------------------
customers = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("/samples/customers.csv")

sales = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("/samples/sales.csv")

# ------------------------------------
# Display Schema
# ------------------------------------
print("Customers Schema")
customers.printSchema()

print("Sales Schema")
sales.printSchema()

# ------------------------------------
# Calculate Total Spend
# ------------------------------------
customer_spend = sales.groupBy("customer_id") \
    .agg(
        sum("total_amount").alias("total_spend")
    )

customer_data = customers.join(
    customer_spend,
    on="customer_id",
    how="left"
).fillna(
    0,
    subset=["total_spend"]
)

print("\n============================")
print("Customer Total Spend")
print("============================")
customer_data.show()

# ==================================================
# Task 1 - Gold / Silver / Bronze
# ==================================================
segmented_df = customer_data.withColumn(
    "segment",
    when(customer_data.total_spend > 10000, "Gold")
    .when(
        (customer_data.total_spend >= 5000) &
        (customer_data.total_spend <= 10000),
        "Silver"
    )
    .otherwise("Bronze")
)

print("\n============================")
print("Conditional Segmentation")
print("============================")
segmented_df.show()

# ==================================================
# Task 2 - Count Customers by Segment
# ==================================================
print("\n============================")
print("Customer Count")
print("============================")

segmented_df.groupBy("segment").count().show()

# ==================================================
# Task 3 - Quantile Segmentation
# ==================================================
q1, q2 = segmented_df.approxQuantile(
    "total_spend",
    [0.33, 0.66],
    0
)

print("33% Quantile :", q1)
print("66% Quantile :", q2)

quantile_df = segmented_df.withColumn(
    "quantile_segment",
    when(segmented_df.total_spend <= q1, "Bronze")
    .when(segmented_df.total_spend <= q2, "Silver")
    .otherwise("Gold")
)

print("\n============================")
print("Quantile Segmentation")
print("============================")
quantile_df.show()

# ==================================================
# Task 4 - Bucketizer
# ==================================================
splits = [
    float("-inf"),
    5000,
    10000,
    float("inf")
]

bucketizer = Bucketizer(
    splits=splits,
    inputCol="total_spend",
    outputCol="bucket"
)

bucket_df = bucketizer.transform(customer_data)

print("\n============================")
print("Bucketizer")
print("============================")
bucket_df.show()

# ==================================================
# Task 5 - Window Percent Rank
# ==================================================
window = Window.orderBy("total_spend")

rank_df = customer_data.withColumn(
    "percent_rank",
    percent_rank().over(window)
)

print("\n============================")
print("Percent Rank")
print("============================")
rank_df.show()

# ==================================================
# Compare Methods
# ==================================================
comparison = quantile_df.select(
    "customer_id",
    "total_spend",
    "segment",
    "quantile_segment"
)

print("\n============================")
print("Comparison")
print("============================")
comparison.show()

# ==================================================
# Save Output
# ==================================================
segmented_df.coalesce(1) \
    .write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv("/tmp/segmented_customers")

print("\nOutput saved successfully to /tmp/segmented_customers")

spark.stop()
