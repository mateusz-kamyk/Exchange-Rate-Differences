###This file is responsible for downloading data from NBP API.

import requests

def request_data(currency, date):
    #API requires specification of the table; for GBP, USD, and EUR it's table A.
    table = "A"

    url = (f"http://api.nbp.pl/api/exchangerates/rates/{table}/{currency}/{date}/")

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        mid_value = data['rates'][0]['mid'] #mid value is the exchange rate value
        print(mid_value)
        return mid_value
    elif response.status_code == 400:
        print(f"{response}:\nLegend:\n'400 Bad Request' - incorrectly formulated enquiries\n '400 Bad Request - Limit exceeded' - an enquiry/query exceeding the returned data size limit")
    elif response.status_code == 404:
        print(f"{response} - lack of data for a correctly determined time interval")
    else:
        print("Something went wrong.")     

