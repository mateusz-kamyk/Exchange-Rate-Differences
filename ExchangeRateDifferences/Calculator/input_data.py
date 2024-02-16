#Invoice data input functions
import sys
from datetime import datetime

def input_data():
    print("Exchange Rate Differences program")
    print("Please provide:")
    invoice_amount = input("The amount to be paid:\n")
    invoice_currency = input("The currency (on the invoice):\n")
    invoice_date = input("The invoice date (YYYY-MM-DD):\n")
    user_amount = input("Paid amount:\n")
    user_currency = input("Payment currency:\n")
    user_date = input("Payment date (YYYY-MM-DD):\n")

    return invoice_amount, invoice_currency, invoice_date, user_amount, user_currency, user_date


def check_invoice_amount(invoice_amount):
    try:
        float(invoice_amount)
    except (ValueError, TypeError):
        print("You've provided wrong value! - Invoice amount")
        sys.exit()

def check_invoice_currency(invoice_currency):
    if invoice_currency.isalpha():
        return
    else:
        print("You've provided wrong value! - Invoice currency")
        sys.exit()

def check_invoice_date(invoice_date):
    date_format = "%Y-%M-%D"
    try:
        datetime.strptime(invoice_date, date_format)
    except (ValueError, TypeError):
        print("You've provided wrong value! - Invoice date")
        sys.exit()

def check_user_amount(user_amount):
    try:
        float(user_amount)
    except (ValueError, TypeError):
        print("You've provided wrong value! - Paid amount")
        sys.exit()

def check_user_currency(user_currency):
    if user_currency.isalpha():
        return
    else:
        print("You've provided wrong value! - Payment currency")
        sys.exit()

def check_user_date(user_date):
    date_format = "%Y-%M-%D"
    try:
        datetime.strptime(user_date, date_format)
    except (ValueError, TypeError):
        print("You've provided wrong value! - Payment date")
        sys.exit()


def run_input_data():
    invoice_amount, invoice_currency, invoice_date, user_amount, user_currency, user_date = input_data()
    check_invoice_amount(invoice_amount)
    check_invoice_currency(invoice_currency)
    check_invoice_date(invoice_date)
    check_user_amount(user_amount)
    check_user_currency(user_currency)
    check_user_date(user_date)

