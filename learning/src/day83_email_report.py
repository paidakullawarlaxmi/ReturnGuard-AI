import pandas as pd

history = pd.read_csv("../outputs/prediction_history.csv")

latest = history.iloc[-1]

email = f"""
RETURN FRAUD REPORT

Prediction:
{latest["Prediction"]}

Confidence:
{latest["Confidence"]}

Quantity:
{latest["Quantity"]}

Price:
{latest["Price"]}

Age:
{latest["Age"]}

Previous Returns:
{latest["PreviousReturns"]}

Recommendation:
"""

if "LOW" in latest["Prediction"]:
    email += "\nApprove Return"

else:
    email += "\nInvestigate Further"

print(email)
with open("../reports/email_report.txt",
          "w",
          encoding="utf-8") as file:
    file.write(email)

print("Email Report Created Successfully")