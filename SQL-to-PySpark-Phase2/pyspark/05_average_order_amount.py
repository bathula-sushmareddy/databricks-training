# #5. Average order amount per customer
result = sales.groupBy("customer_id") \
              .agg(avg("total_amount").alias("avg_order"))

result.show()
