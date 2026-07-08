# ==========================================
# 3. Repeat Customers (>2 Orders)
# ==========================================
print("===== Repeat Customers (PySpark) =====")
result = sales.groupBy("customer_id") \
              .agg(count("*").alias("orders")) \
              .filter(col("orders") > 2)
result.show()
