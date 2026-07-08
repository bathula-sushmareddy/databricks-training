# ==========================================
# # ETL Pipeline
# # ==========================================
print("===== Final ETL Pipeline =====")
customers = spark.read.option("header", "true").csv("/samples/customers.csv")
sales = spark.read.option("header", "true").csv("/samples/sales.csv")
customers = customers.dropna(subset=["customer_id"])
sales = sales.dropna(subset=["customer_id"])
sales = sales.withColumn(
    "total_amount",
    col("total_amount").cast("double")
)
sales = sales.filter(col("total_amount") > 0)
report = customers.join(sales, "customer_id") \
                  .groupBy("customer_id", "city") \
                  .agg(
                      sum("total_amount").alias("total_spend"),
                      count("*").alias("order_count")
                  )
print("===== Final Report =====")
report.show()
