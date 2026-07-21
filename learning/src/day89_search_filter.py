from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("../data/online_retail.csv")

df.fillna("N/A", inplace=True)

@app.route("/", methods=["GET"])

def home():

    search = request.args.get("search")

    filtered = df.copy()

    if search:

        filtered = filtered[
            filtered["StockCode"]
            .astype(str)
            .str.contains(search, case=False)
        ]

    filtered = filtered.head(50)

    records = filtered.to_dict(orient="records")

    return render_template(
        "search.html",
        records=records,
        search=search
    )

if __name__=="__main__":
    app.run(debug=True)