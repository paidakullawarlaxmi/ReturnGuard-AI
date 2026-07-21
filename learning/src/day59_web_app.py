from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # prediction code
        return render_template('index.html', prediction_text="Fraudulent Return")

    return render_template('index.html')

    quantity = float(request.form["Quantity"])

    price = float(request.form["UnitPrice"])

    sample = pd.DataFrame({

        "Quantity":[quantity],

        "UnitPrice":[price]

    })

    prediction = model.predict(sample)

    if prediction[0]==1:

        result="Fraudulent Return"

    else:

        result="Genuine Return"

    return f"<h1>{result}</h1>"

if __name__=="__main__":

    app.run(debug=True)


print("Root Path:", app.root_path)
print("Template Folder:", app.template_folder)