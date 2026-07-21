import pandas as pd

import matplotlib.pyplot as plt

import os
file="../outputs/prediction_history.csv"

if os.path.exists(file):

    history=pd.read_csv(file)

else:

    print("History File Not Found")

    exit()
    print("Prediction History")

print(history)
counts=history["Prediction"].value_counts()

print(counts)
plt.figure(figsize=(6,5))
counts.plot(kind="bar")
plt.title("ReturnGuard AI Prediction Dashboard")
plt.xlabel("Prediction")
plt.ylabel("Number of Customers")
plt.savefig("../static/dashboard.png")
plt.show()
print("Dashboard Created Successfully")

