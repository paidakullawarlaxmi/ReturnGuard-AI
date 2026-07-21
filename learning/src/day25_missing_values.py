import pandas as pd

df = pd.read_csv("../data/online_retail.csv")

# Check missing values
print(df.isnull().sum())