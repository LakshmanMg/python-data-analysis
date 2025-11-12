import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Date': pd.date_range(start='2024-01-01', periods=100, freq='D'),
    'Store': np.random.choice(['Mumbai', 'Delhi', 'Bangalore', 'Chennai'], 100),
    'Product_Category': np.random.choice(['Electronics', 'Clothing', 'Groceries'], 100),
    'Units_Sold': np.random.randint(1, 50, size=100),
    'Unit Price': np.random.randint(100, 2000, size=100)  # <— NOTE space here
}

df = pd.DataFrame(data)

# Clean columns (important!)
df.columns = df.columns.str.strip().str.replace(' ', '_')

print("Column names are:", df.columns.tolist())  # Verify cleaned names

# Compute total sales
df['Total_Sales'] = df['Units_Sold'] * df['Unit_Price']

print(df.head())
print(df.info())
print(df.describe())
print(df['Store'].value_counts())

df.loc[5:10, 'Units_Sold']=np.nan
df['Units_Sold']=df['Units_Sold'].fillna(df['Units_Sold'].mean())
print(df.isnull().sum())

store_sales=df.groupby('Store')['Total_Sales'].sum().sort_values(ascending=False)
print(store_sales)
category_sales=df.groupby('Product_Category')['Total_Sales'].mean().sort_values(ascending=False)
print(category_sales)

df['Month']=df['Date'].dt.month_name()
month_order=['January','February','March','April','May','June','July','August','September','October','November','December']
monthly_sales=df.groupby('Month')['Total_Sales'].sum().reindex(month_order)
print(monthly_sales)

store_sales.plot(kind='bar', title='Total Sales by Store', ylabel='Total Sales (Rs)', xlabel='Store')
plt.show()

category_sales.plot(kind='pie', title='Average Sales by Product Category', autopct='%1.1f%%')
plt.ylabel(' ')
plt.show()
