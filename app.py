import os, re
from flask import Flask, render_template, session, request, redirect
from flask_material import Material


app = Flask(__name__)
app.secret_key = os.urandom(24)
Material(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact-us')
def contactUs():
    return render_template('contact_us.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        invalid_email = None
        invalid_password=None
        email = request.form.get('email')
        password = request.form.get('password')
        print (email, password)
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not(re.search(regex, email)):
            invalid_email = "Invalid email format. Email should be in format abc@xyz.com"
        if (len(password)) < 6:
            invalid_password = "Invalid password. Password length should be greater than 6"
        if not invalid_email and not invalid_password:
            return render_template('login.html', logged_in="Success")
        return render_template('login.html', invalid_email=invalid_email, invalid_password=invalid_password)
    return render_template('login.html')


@app.route('/payment', methods=['POST', 'GET'])
def payment():
    if request.method == 'POST':
        invalid_expiry = None
        invalid_card_number = None
        invalid_cvv = None
        expiry = request.form.get('expiry')
        card_number = request.form.get('card_number')
        cvv = request.form.get('cvv')

        if not cvv or not expiry or not card_number:
            return render_template('payment.html', missing_details="Missing Card Details")

        if not (len(str(card_number)) == 16):
            invalid_card_number = "Invalid Card Number"

        if not len(str(cvv)) == 3:
            invalid_cvv = "Invalid CVV"

        if (int(expiry[:2]) > 12):
            invalid_expiry = "Invalid Exipry Month"

        if (int(expiry[2:]) < 20):
            invalid_expiry = "Invalid Exipry Year"

        if not invalid_expiry and not invalid_card_number and not invalid_cvv:
            return render_template('payment.html', payment_success="Payment Successful")
        return render_template('payment.html', invalid_card_number=invalid_card_number, invalid_cvv=invalid_cvv, invalid_expiry=invalid_expiry)

    return render_template('payment.html')


