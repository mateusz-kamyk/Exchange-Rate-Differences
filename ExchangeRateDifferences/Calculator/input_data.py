#Invoice data input functions

#Questions for the user
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



