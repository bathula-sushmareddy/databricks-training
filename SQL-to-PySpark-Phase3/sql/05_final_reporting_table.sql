# ==========================================
# 5. Final Reporting Table
# ==========================================

print("===== Final Reporting Table (SQL) =====")

result = spark.sql("""
SELECT
    c.customer_id,
    c.city,
    SUM(s.total_amount) AS total_spend,
    COUNT(*) AS order_count
FROM customers c
JOIN sales s
ON c.customer_id = s.customer_id
GROUP BY c.customer_id, c.city
""")

result.show()
