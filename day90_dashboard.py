from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("../data/online_retail.csv")

df.fillna("N/A", inplace=True)

total_transactions = len(df)

total_revenue = (df["Quantity"] * df["UnitPrice"]).sum()

total_products = df["StockCode"].nunique()

total_countries = df["Country"].nunique()

fraud_cases = len(df[df["Quantity"] > 20])

safe_cases = total_transactions - fraud_cases

@app.route("/")
def dashboard():

    return render_template(

        "dashboard.html",

        total_transactions=total_transactions,

        total_revenue=round(total_revenue,2),

        total_products=total_products,

        total_countries=total_countries,

        fraud_cases=fraud_cases,

        safe_cases=safe_cases

    )

if __name__=="__main__":
    app.run(debug=True)