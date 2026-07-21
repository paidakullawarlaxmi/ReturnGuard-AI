import pandas as pd

df = pd.read_csv("../data/online_retail.csv")

print("Total Transactions:")
print(df["InvoiceNo"].count())
import pandas as pd

df = pd.read_csv("../data/online_retail.csv")

result = df.groupby("Country")["InvoiceNo"].count()

print(result)
