# #4. City-wise total revenue
result = customers.join(sales, "customer_id") \
                  .groupBy("city") \
                  .agg(sum("total_amount").alias("revenue"))

result.show()
