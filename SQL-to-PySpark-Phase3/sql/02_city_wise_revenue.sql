
# ==========================================
# 2. City-wise Revenue
# ==========================================
print("===== City-wise Revenue (SQL) =====")
result = spark.sql("""
SELECT c.city,
       SUM(s.total_amount) AS revenue
FROM customers c
JOIN sales s
ON c.customer_id = s.customer_id
GROUP BY c.city
""")
result.show()
print("===== City-wise Revenue (PySpark) =====")

result = customers.join(sales, "customer_id") \
                  .groupBy("city") \
                  .agg(sum("total_amount").alias("revenue"))
result.show()
