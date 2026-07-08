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
