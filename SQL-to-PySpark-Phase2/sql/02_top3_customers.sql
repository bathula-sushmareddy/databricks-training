# #2. Top 3 customers by total spend
result = spark.sql("""
SELECT customer_id,
       SUM(total_amount) AS total_spent
FROM sales
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 3
""")
