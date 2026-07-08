# ==========================================
# 4. Highest Spending Customer in Each City
# ==========================================
print("===== Highest Spending Customer in Each City (PySpark) =====")
result = customers.join(sales, "customer_id") \
                  .groupBy("city", "customer_id") \
                  .agg(sum("total_amount").alias("total_spent")) \
                  .orderBy("city", col("total_spent").desc())
result.show()
