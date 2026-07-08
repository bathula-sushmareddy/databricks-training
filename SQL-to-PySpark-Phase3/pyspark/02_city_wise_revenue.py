# ==========================================
# 2. City-wise Revenue
# ==========================================
print("===== City-wise Revenue (PySpark) =====")
result = customers.join(sales, "customer_id") \
                  .groupBy("city") \
                  .agg(sum("total_amount").alias("revenue"))
result.show()
