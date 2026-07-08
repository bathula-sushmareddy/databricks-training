from pyspark.sql.functions import *
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Spark Playground").getOrCreate()

customers = spark.read.option("header", "true").csv("/samples/customers.csv")
sales = spark.read.option("header", "true").csv("/samples/sales.csv")

customers = customers.dropna(subset=["customer_id"])
sales = sales.dropna(subset=["customer_id"])

sales = sales.withColumn(
    "total_amount",
    col("total_amount").cast("double")
)
# # Total order amount for each customer
result = sales.groupBy("customer_id") \
              .agg(sum("total_amount").alias("total_spent"))

result.show()
