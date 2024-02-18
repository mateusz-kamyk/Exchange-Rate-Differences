#This code allows saving data to file
import pandas as pd

def save_to_file(invoice_amount, invoice_currency, invoice_date, user_amount, user_currency, user_date, invoice_mid_value, user_mid_value, difference, filename):
    #Define the format
    format = filename.split('.')[-1]
    #Saving to .txt file
    if format == 'txt':
        data = [
            f"Invoice Amount: {invoice_amount}",
            f"Invoice Currency: {invoice_currency}",
            f"Invoice Date: {invoice_date}",
            f"User Amount: {user_amount}",
            f"User Currency: {user_currency}",
            f"User Date: {user_date}",
            f"Invoice Mid Value: {invoice_mid_value}",
            f"User Mid Value: {user_mid_value}",
            f"Difference: {'{:.2f}'.format(difference)+' PLN'}"
        ]
        with open(filename, "w") as file:
            for element in data:
                file.write(element + "\n")
    #Saving to .csv file            
    elif format =='csv':
        data = {'Data' : ['Invoice Amount', 'Invoice Currency', 'Invoice Date',
                        'User Amount', 'User Currency', 'User Date',
                        'Invoice Mid Value', 'User Mid Value', 'Difference'],
                'Values' : [invoice_amount, invoice_currency, invoice_date,
                            user_amount, user_currency, user_date,
                            invoice_mid_value, user_mid_value, '{:.2f}'.format(difference)+' PLN']}
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
    else:
        print(f"Unknown file format: {filename}")
        