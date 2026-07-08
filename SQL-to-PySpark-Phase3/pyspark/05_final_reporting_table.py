# ==========================================
# 5. Final Reporting Table
# ==========================================
print("===== Final Reporting Table (PySpark) =====")
result = customers.join(sales, "customer_id") \
                  .groupBy("customer_id", "city") \
                  .agg(
                      sum("total_amount").alias("total_spend"),
                      count("*").alias("order_count")
                  )
result.show()
# ==========================================
# Read JSON File
# ==========================================
print("===== Products JSON =====")
products_json = spark.read.option("multiLine", "true") \
                          .json("/samples/products.json")
products_json.show()
products_json.printSchema()
# ==========================================
# Read Parquet File
# ==========================================
print("===== Titanic Parquet =====")
titanic = spark.read.parquet("/samples/titanic.parquet")

titanic.show()
titanic.printSchema()
