import pandas as pd
history = pd.read_csv("../outputs/prediction_history.csv")
print(history)
total = len(history)
high = (history["Prediction"] == "🚨 HIGH FRAUD").sum()
low = (history["Prediction"] == "✅ LOW FRAUD").sum()
average = history["Price"].mean()

maximum = history["Price"].max()

minimum = history["Price"].min()

fraud_percentage = (high / total) * 100

print("Total Predictions :", total)

print("High Fraud :", high)

print("Low Fraud :", low)

print("Average Price :", average)

print("Highest Price :", maximum)

print("Lowest Price :", minimum)

print("Fraud Percentage :", fraud_percentage)