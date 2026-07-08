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

