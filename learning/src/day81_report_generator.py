
import pandas as pd

history = pd.read_csv("../outputs/prediction_history.csv")

latest = history.iloc[-1]

print("="*50)
print("RETURN FRAUD INVESTIGATION REPORT")
print("="*50)

print()

print("Prediction :", latest["Prediction"])

print("Confidence :", latest["Confidence"])

print()

print("Reasons")

if latest["PreviousReturns"] < 5:
    print("✔ Customer has very few previous returns")
else:
    print("⚠ Customer has many previous returns")

if latest["Quantity"] < 30:
    print("✔ Quantity looks normal")
else:
    print("⚠ Quantity is unusually high")

if latest["Price"] < 500:
    print("✔ Product price is normal")
else:
    print("⚠ Product price is expensive")

if latest["Age"] > 18:
    print("✔ Adult customer")
else:
    print("⚠ Very young customer")

print()

print("Recommendation")

if "LOW" in latest["Prediction"]:
    print("Approve Return")
else:
    print("Investigate Before Approval")