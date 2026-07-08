# #5. Average order amount per customer
result = spark.sql("""
SELECT customer_id,
       AVG(total_amount) AS avg_order
FROM sales
GROUP BY customer_id
""")
result.show()
