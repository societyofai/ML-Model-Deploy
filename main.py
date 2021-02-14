from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load('bank_model.sav')

@app.route("/user")
def user_details():
    return render_template('index.html')

@app.route("/predictions", methods=['GET', 'POST'])
def details():
    if request.method == 'POST': ## post method
        data = request.form
        job = int(data['job']) # string
        marital = int(data['marital'])
        default = int(data['default'])
        balance = int(data['balance'])
        housing = int(data['housing'])
        loan = int(data['loan'])
        month = int(data['month'])
        age_category = int(data['age_category'])
        
        parameters = [[job, marital, default, balance, housing, loan, month, age_category]]

        result = model.predict(parameters)[0] #
        print("result is=========", result)

        if result == 0:
            return "Dont give loan"
        else:
            return "Give loan"

if __name__ == "__main__":
    app.run()



