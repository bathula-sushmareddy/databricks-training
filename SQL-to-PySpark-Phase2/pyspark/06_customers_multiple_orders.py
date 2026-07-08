# #6. Customers with more than one order
result = sales.groupBy("customer_id") \
              .agg(count("*").alias("orders")) \
              .filter(col("orders") > 1)

result.show()
