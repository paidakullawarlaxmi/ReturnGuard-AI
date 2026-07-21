import pandas as pd
import matplotlib.pyplot as plt

history = pd.read_csv("../outputs/prediction_history.csv")

fraud_counts = history["Prediction"].value_counts()

print(fraud_counts)

plt.bar(
    fraud_counts.index,
    fraud_counts.values
)

plt.title("Fraud Prediction Count")

plt.xlabel("Prediction")

plt.ylabel("Count")

plt.savefig("../charts/fraud_bar.png")

plt.show()