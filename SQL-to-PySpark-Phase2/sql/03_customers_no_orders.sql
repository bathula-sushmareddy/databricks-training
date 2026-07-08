# #3. Customers with no orders
result = spark.sql("""
SELECT c.customer_id,
       c.first_name,
       c.last_name
FROM customers c
LEFT JOIN sales s
ON c.customer_id = s.customer_id
WHERE s.customer_id IS NULL
""")

result.show()
