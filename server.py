from flask import Flask, render_template, redirect, request, session
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = "countThis"


@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    # if 'output' not in session:
    #     session['output'] = ""
    return render_template('index.html', gold=session['gold'], log=session['activities']  )# , log=session['output'])


@app.route('/process_money', methods=['POST'])
def process_money():
    now = str(datetime.today().strftime("%Y/%m/%d %I:%M %p"))
    if request.form['building'] != 'casino':
        #Set earnings
        if request.form['building'] == 'farm':
            earnings = random.randint(10,20)
        elif request.form['building'] == 'cave':
            earnings = random.randint(5,10)
        elif request.form['building'] == 'house':
            earnings = random.randint(2,5)
        #Set Output in Activities
        if earnings >= 0:
            # session['output'] += "\nEarned {} gold from the {}!({})".format(
            #     earnings, request.form['building'], now)
            session['activities'].append("<p style='color:green'>" + 
                    "Earned {} gold from the {}!({})".format(earnings, request.form['building'], now)+ "</p>")
                #     earnings, request.form['building'], now) + )
        else:
            # session['output'] += "\nEntered a {}  and lost {} gold.. Ouch..({})".format(
            #     request.form['building'], earnings, now)
            session['activities'].append("<p style='color:red'>" + 
                    "Entered a {}  and lost {} gold.. Ouch..({})".format(request.form['building'], earnings, now)+ "</p>")
        #Increase Gold by Earnings
        session['gold'] += earnings
    else:
        if session['gold'] <= 0:
            # session['output'] += "\nYou're broke, you can't go to the casino...({})".format(now)
            session['activities'].append("<p style='color:red'>You're broke, you can't go to the casino...({})".format(now)+ "</p>")
        else:
            earnings = random.randint(-50, 50)
            print earnings
            #Set Output in Activities
            if earnings >= 0:
                # session['output'] += "\nEarned {} gold from the {}!({})".format(
                #     earnings, request.form['building'], now)
                session['activities'].append("<p style='color:green'>" + 
                    "Earned {} gold from the {}!({})".format(earnings, request.form['building'], now)+ "</p>")
            else:
                # session['output'] += "\nEntered a {}  and lost {} gold.. Ouch..({})".format(
                #     request.form['building'], earnings, now)
                session['activities'].append("<p style='color:red'>" + 
                    "Entered a {}  and lost {} gold.. Ouch..({})".format(request.form['building'], earnings, now)+ "</p>")
            #Increase Gold by Earnings
            session['gold'] += earnings
    return redirect('/')

@app.route('/reset')
def reset():
    session['gold'] = 0
    # session['output'] = ""
    session['activities'] = []
    return redirect('/')

app.run(debug=True)
