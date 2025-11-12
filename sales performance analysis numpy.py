import numpy as np
import matplotlib.pyplot as plt
months=np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
sales=np.array([
[23, 25, 31, 29, 33, 30, 35, 40, 38, 36, 31, 28],
[18, 20, 22, 25, 27, 29, 30, 33, 31, 28, 24, 22],
[12, 15, 19, 20, 24, 21, 25, 27, 29, 26, 22, 20]
    ])
print("Shape of data:", sales.shape)
print("Overall average sales: ", np.mean(sales))
print("Average per product: ", np.mean(sales, axis=1))
print("Total sales per product: ", np.sum(sales, axis=1))
print("Total sales per month: ", np.sum(sales, axis=0))

best_month_index=np.argmax(np.sum(sales, axis=0))
print("Best month:", months[best_month_index])

best_product_index=np.argmax(np.sum(sales, axis=1))
products=['Product A', 'Products B', 'Products C']
print("Best performing product:", products[best_product_index])

overall_avg=np.mean(sales)
above_avg_months=np.where(np.sum(sales, axis=0)>overall_avg*3)
print("Months above avg total sales:", months[above_avg_months])

for i in range(3):
    plt.plot(months, sales[i], marker='o', label=products[i])

plt.title("Product-wise Monthly Sales (in thousands)")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
