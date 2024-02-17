###This file is responsible for collecting data from NBP API.

import requests

def request_data(currency, date):
    #API requires specification of the table; for GBP, USD, and EUR it's table A.
    table = "A"
    #Collection of the exchange rate value via NBP API
    url = (f"http://api.nbp.pl/api/exchangerates/rates/{table}/{currency}/{date}/")
    response = requests.get(url)
    
    if currency == 'EUR' or 'GBP' or "USD":
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
    elif currency == 'PLN': #In case someone would like to pay in PLN
        mid_value = 1.0
    else:
        print("This program accepts currencies: PLN, EUR, USD, GBP")

    return mid_value
