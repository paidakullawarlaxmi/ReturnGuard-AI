from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Read CSV
df = pd.read_csv("../data/online_retail.csv")

# Keep only first 30 rows
df = df.head(30)

# Replace missing values
df = df.fillna("N/A")

@app.route("/")
def home():

    records = df.to_dict(orient="records")

    return render_template(
        "history.html",
        records=records
    )

if __name__ == "__main__":
    print("ReturnGuard AI Running...")
    print("http://127.0.0.1:5000")
    app.run(debug=True)