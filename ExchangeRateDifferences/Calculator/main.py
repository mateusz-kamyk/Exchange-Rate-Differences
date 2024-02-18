#!/usr/bin/env python3

import input_data
import input_data_check
import api_requests
import calculator
import save_file

def main():
    #input data (regarding the invoice and user payment), collect information
    invoice_amount, invoice_currency, invoice_date, user_amount, user_currency, user_date = input_data.input_data()
    input_data_check.check_data(invoice_amount, invoice_currency, invoice_date, user_amount, user_currency, user_date)

    #Collect mid values (exchange rate values) for invoice and user data.
    invoice_mid_value = api_requests.request_data(invoice_currency, invoice_date)
    user_mid_value = api_requests.request_data(user_currency, user_date)

    #Calculate if a refund or additional payment is required
    calculator.calculate_difference(invoice_amount, user_amount, invoice_mid_value, user_mid_value)

    return invoice_amount, invoice_currency, invoice_date, user_amount, user_currency, user_date, invoice_mid_value, user_mid_value, difference

def parse_arguments():
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)
    parser.add_argument('-f', '--filename', help='It is possible to enter a file name in order to save a summary of the calculation.\nAvailable formats: .txt, .csv.')
    parser.epilog = """
    Example of use:

    ./main.py -f invoice-status-summary.txt
    ./main.py --filename invoice-status-summary.txt
    
    If you do not need a file with summary:
    ./main.py

    """
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    if args.filename:
        invoice_amount, invoice_currency, invoice_date, user_amount, user_currency, user_date, invoice_mid_value, user_mid_value, difference = main()
        save_file.save_to_file(invoice_amount, invoice_currency, invoice_date, user_amount, user_currency, user_date, invoice_mid_value, user_mid_value, difference, args.filename)
    else:
        main()
        
