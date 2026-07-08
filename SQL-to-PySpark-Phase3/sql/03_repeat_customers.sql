# ==========================================
# 3. Repeat Customers (>2 Orders)
# ==========================================
print("===== Repeat Customers (SQL) =====")
result = spark.sql("""
SELECT customer_id,
       COUNT(*) AS orders
FROM sales
GROUP BY customer_id
HAVING COUNT(*) > 2
""")
result.show()
print("===== Repeat Customers (PySpark) =====")
result = sales.groupBy("customer_id") \
              .agg(count("*").alias("orders")) \
              .filter(col("orders") > 2)
result.show()
