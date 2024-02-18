# Exchange Rate Differences Program
This program calculates exchange rate differences resulting from invoices. Based on the invoice and payment data entered it calculates the currency difference to be settled.

## Functions
This Program:
- Accepts invoice data (amount, currency, date of issue).
- Accepts payment information (amount, currency, date of payment).
- Receives current exchange rates from the API of the National Bank of Poland (NBP) and calculates exchange rate differences based on them.
- Provides an option to save entered data and calculation results to files with .txt and .csv extensions.
- Operates in an interactive mode.
- Accepts currencies: USD, EUR, GBP, PLN.

## Manual
The Exchange Rate Differences Program can be started by executing the command: 
`./main.py`

#### Arguments:

- `-f FILENAME`, `--filename FILENAME`;    Save a summary of the calculation. Available formats: .txt, .csv.
- `-h`, `--help`;    Show the help message and exit.

