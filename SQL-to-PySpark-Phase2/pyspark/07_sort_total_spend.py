# #7. Sort customers by total spend descending
result = sales.groupBy("customer_id") \
              .agg(sum("total_amount").alias("total_spent")) \
              .orderBy(col("total_spent").desc())

result.show()
