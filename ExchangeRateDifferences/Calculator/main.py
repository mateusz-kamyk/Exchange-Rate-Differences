#!/usr/bin/env python3

import input_data
import api_requests
import calculator

def main():
    #input data (regarding the invoice and user payment), collect information
    invoice_amount, invoice_currency, invoice_date, user_amount, user_currency, user_date = input_data.run_input_data()

    #Collect mid values (exchange rate values) for invoice and user data.
    invoice_mid_value = api_requests.request_data(invoice_currency, invoice_date)
    user_mid_value = api_requests.request_data(user_currency, user_date)

    #Calculate if a refund or additional payment is required
    calculator.calculate_difference(invoice_amount, user_amount, invoice_mid_value, user_mid_value)

if __name__ == "__main__":
    main()    