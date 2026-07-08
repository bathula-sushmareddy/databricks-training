# ==========================================
# 4. Highest Spending Customer in Each City
# ==========================================
print("===== Highest Spending Customer in Each City (SQL) =====")
result = spark.sql("""
SELECT
    c.city,
    s.customer_id,
    SUM(s.total_amount) AS total_spent
FROM customers c
JOIN sales s
ON c.customer_id = s.customer_id
GROUP BY c.city, s.customer_id
ORDER BY c.city, total_spent DESC
""")
result.show()
print("===== Highest Spending Customer in Each City (PySpark) =====")
result = customers.join(sales, "customer_id") \
                  .groupBy("city", "customer_id") \
                  .agg(sum("total_amount").alias("total_spent")) \
                  .orderBy("city", col("total_spent").desc())
result.show()
