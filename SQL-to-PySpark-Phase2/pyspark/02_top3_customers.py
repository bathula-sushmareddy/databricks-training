# #2. Top 3 customers by total spend
result = sales.groupBy("customer_id") \
              .agg(sum("total_amount").alias("total_spent")) \
              .orderBy(col("total_spent").desc()) \
              .limit(3)

result.show()
