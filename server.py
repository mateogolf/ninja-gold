from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = "countThis"


@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'output' not in session:
        session['output'] = ""
    return render_template('index.html', gold=session['gold'], log=session['output'])


@app.route('/process_money', methods=['POST'])
def process_money():
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
            session['output'] += "\nEarned {} gold from the {}!(Date Time)".format(
                earnings, request.form['building'])
        else:
            session['output'] += "\nEntered a {}  and lost {} gold.. Ouch..(Date Time)".format(
                request.form['building'], earnings)
        #Increase Gold by Earnings
        session['gold'] += earnings
    else:
        if session['gold'] <= 0:
            session['output'] += "\nYou're broke, you can't go to the casino...(Date Time)"
        else:
            earnings = random.randint(-50, 50)
            print earnings
            #Set Output in Activities
            if earnings >= 0:
                session['output'] += "\nEarned {} gold from the {}!(Date Time)".format(
                    earnings, request.form['building'])
            else:
                session['output'] += "\nEntered a {}  and lost {} gold.. Ouch..(Date Time)".format(
                    request.form['building'],earnings)
            #Increase Gold by Earnings
            session['gold'] += earnings
    return redirect('/')

@app.route('/reset')
def reset():
    session['gold'] = 0
    session['output'] = ""
    return redirect('/')

app.run(debug=True)
