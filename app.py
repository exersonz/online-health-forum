from flask import Flask, redirect, url_for, render_template, request
from fileinput import filename

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/about.html')
def loadabout():
    return render_template('about.html')

@app.route('/index.html')
def loadindex():
    return render_template('index.html')

@app.route('/services.html')
def loadservices():
    # return render_template('services.html')
    return render_template('services2.html')

@app.route('/portfolio.html')
def loadportfolio():
    return render_template('portfolio.html')

@app.route('/pricing.html')
def loadpricing():
    return render_template('pricing.html')

@app.route('/contact.html')
def loadcontact():
    return render_template('contact.html')

if __name__=='__main__':
    app.run(debug=True)