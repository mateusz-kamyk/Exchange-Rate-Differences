#Checking the data from input_data.py

from datetime import datetime

###Functions for verifying the correctness of the data (formats)
def check_invoice_amount(invoice_amount):
    try:
        float(invoice_amount)
    except (ValueError, TypeError):
        print("You've provided wrong value! - Invoice amount")

def check_invoice_currency(invoice_currency):
    if invoice_currency.isalpha():
        return
    else:
        print("You've provided wrong value! - Invoice currency")

def check_invoice_date(invoice_date):
    date_format = "%Y-%m-%d"
    try:
        datetime.strptime(invoice_date, date_format)
    except (ValueError, TypeError):
        print("You've provided wrong value! - Invoice date")
    if len(invoice_date) >= 10:
        pass
    else:
        print("You've provided wrong value! - Invoice date")

def check_user_amount(user_amount):
    try:
        float(user_amount)
    except (ValueError, TypeError):
        print("You've provided wrong value! - Paid amount")

def check_user_currency(user_currency):
    if user_currency.isalpha():
        return
    else:
        print("You've provided wrong value! - Payment currency")

def check_user_date(user_date):
    date_format = "%Y-%m-%d"
    try:
        datetime.strptime(user_date, date_format)
    except (ValueError, TypeError):
        print("You've provided wrong value! - Payment date")
    if len(user_date) >= 10:
        pass
    else:
        print("You've provided wrong value! - Payment date")

#Activation of the user data collection and checking functions
def check_data(invoice_amount, invoice_currency, invoice_date, user_amount, user_currency, user_date):
    check_invoice_amount(invoice_amount)
    check_invoice_currency(invoice_currency)
    check_invoice_date(invoice_date)
    check_user_amount(user_amount)
    check_user_currency(user_currency)
    check_user_date(user_date)