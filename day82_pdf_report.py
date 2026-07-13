from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import pandas as pd

history = pd.read_csv("../outputs/prediction_history.csv")

latest = history.iloc[-1]

doc = SimpleDocTemplate("../reports/Fraud_Report.pdf")

styles = getSampleStyleSheet()

story = []

story.append(
    Paragraph(
        "RETURN FRAUD INVESTIGATION REPORT",
        styles["Title"]
    )
)

story.append(
    Paragraph(
        f"Prediction : {latest['Prediction']}",
        styles["BodyText"]
    )
)

story.append(
    Paragraph(
        f"Confidence : {latest['Confidence']}",
        styles["BodyText"]
    )
)

story.append(
    Paragraph(
        f"Quantity : {latest['Quantity']}",
        styles["BodyText"]
    )
)

story.append(
    Paragraph(
        f"Price : {latest['Price']}",
        styles["BodyText"]
    )
)

story.append(
    Paragraph(
        f"Age : {latest['Age']}",
        styles["BodyText"]
    )
)

story.append(
    Paragraph(
        f"Previous Returns : {latest['PreviousReturns']}",
        styles["BodyText"]
    )
)

if "LOW" in latest["Prediction"]:
    recommendation = "Approve Return"
else:
    recommendation = "Investigate Further"

story.append(
    Paragraph(
        recommendation,
        styles["Heading2"]
    )
)

doc.build(story)

print("Fraud Report Generated Successfully!")