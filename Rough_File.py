import pandas as pd

df=pd.read_csv(r'C:\Users\Administrator\Desktop\New folder\data (2).csv')

df['Date']=pd.to_datetime(df['Date'], format='mixed')

print(df.to_string())
