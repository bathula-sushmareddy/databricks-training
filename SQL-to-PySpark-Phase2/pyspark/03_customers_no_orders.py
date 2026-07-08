# #3. Customers with no orders
result = customers.join(
    sales,
    "customer_id",
    "left_anti"
)
