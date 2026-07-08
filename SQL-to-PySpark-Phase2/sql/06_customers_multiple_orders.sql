# #6. Customers with more than one order
result = spark.sql("""
SELECT customer_id,
       COUNT(*) AS orders
FROM sales
GROUP BY customer_id
HAVING COUNT(*) > 1
""")
result.show()
