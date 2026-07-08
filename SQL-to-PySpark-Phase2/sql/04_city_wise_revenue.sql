# #4. City-wise total revenue
result = spark.sql("""
SELECT c.city,
       SUM(s.total_amount) AS revenue
FROM customers c
JOIN sales s
ON c.customer_id = s.customer_id
GROUP BY c.city
""")
