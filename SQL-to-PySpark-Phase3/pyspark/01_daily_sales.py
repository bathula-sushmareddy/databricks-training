# ==========================================
# 1. Daily Sales
# ==========================================
print("===== Daily Sales (PySpark) =====")
result = sales.groupBy("sale_date") \
              .agg(sum("total_amount").alias("daily_sales"))
result.show()
