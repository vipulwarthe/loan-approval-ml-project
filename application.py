from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def loan_approval():
    if request.method == 'POST':
        applicant_income = float(request.form['applicant_income'])
        credit_history = int(request.form['credit_history'])
        loan_amount = float(request.form['loan_amount'])
        
        if applicant_income >= 50000 and credit_history == 1 and loan_amount <= 200000:
            result = "Congratulations! Your loan is approved."
        else:
            result = "Sorry, your loan application is not approved."
        
        return render_template('home.html', result=result)
    
    return render_template('home.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)