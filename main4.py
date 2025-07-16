import numpy as np

# Products data
product_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
prices = np.array([10.99, 20.99, 15.49, 25.49, 5.99, 12.99, 7.99, 30.99, 18.99, 9.99])
quantities = np.array([100, 50, 75, 30, 200, 120, 150, 20, 80, 110])
dates = np.array([
    '2023-07-01', '2023-07-02', '2023-07-03', '2023-07-04', '2023-07-05',
    '2023-07-06', '2023-07-07', '2023-07-08', '2023-07-09', '2023-07-10',
])

# Total sales per product
total_sales = prices * quantities
print(f"Total sales: {total_sales}")

# Total revenue
total_revenue = np.sum(total_sales)
print(f"Total revenue: {total_revenue:.2f}")

# Average check
average_check = np.mean(total_sales)
print(f"Average check: {average_check:.2f}")

# Best and worst products
best_product_index = np.argmax(total_sales)
worst_product_index = np.argmin(total_sales)

print(f"Best product (ID: {product_ids[best_product_index]}) sales amount: {total_sales[best_product_index]:.2f}")
print(f"Worst product (ID: {product_ids[worst_product_index]}) sales amount: {total_sales[worst_product_index]:.2f}")
