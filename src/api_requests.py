###This file is responsible for collecting data from NBP API.

import requests

def request_data(currency, date):
    if currency == 'PLN': #In case someone would like to pay in PLN
        mid_value = 1.0
    elif currency == 'EUR' or 'GBP' or 'USD':
        #API requires specification of the table; for GBP, USD, and EUR it's table A.
        table = "A"
        #Collection of the exchange rate value via NBP API
        url = (f"http://api.nbp.pl/api/exchangerates/rates/{table}/{currency}/{date}/")
        response = requests.get(url)
        #Actions depending on the response
        if response.status_code == 200:
            data = response.json()
            mid_value = data['rates'][0]['mid'] #mid value is the exchange rate value (given by NBP)
        elif response.status_code == 400:
            print(f"{response}:\nLegend:\n'400 Bad Request' - incorrectly formulated enquiries\n '400 Bad Request - Limit exceeded' - an enquiry/query exceeding the returned data size limit")
        elif response.status_code == 404:
            print(f"{response} - lack of data for a correctly determined time interval")
        else:
            print("Something went wrong.")     
    else:
        print("This program only accepts currencies: PLN, EUR, USD, GBP")

    return mid_value
