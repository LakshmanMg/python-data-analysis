#Basic Data Exploration with NumPy
#Goal: Practice working with numerical data arrays, summary statistics, and filtering.
import numpy as np
import matplotlib.pyplot as plt
sales=np.array([23, 25, 31, 29, 33, 30, 35, 40, 38, 36, 21, 28])
print("Monthly sales:", sales)
print("Average sales:", np.mean(sales))
print("Median sales:", np.median(sales))
print("Highest month sales:", np.max(sales))
print("Lowest month sales:", np.min(sales))
print("Standard deviation:", np.std(sales))
avg_sales=np.mean(sales)
months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
high_months=np.where(sales>avg_sales)
print("Months above average:", high_months)
print("Sales in those months:", sales[high_months])
plt.plot(months, sales, marker='o', label='Sales')
plt.axhline(y=avg_sales, color='r', linestyle='--', label='Average')
plt.title("Monthly Sales Data (2025)")
plt.xlabel("Month")
plt.ylabel("Sales (in thousands)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
