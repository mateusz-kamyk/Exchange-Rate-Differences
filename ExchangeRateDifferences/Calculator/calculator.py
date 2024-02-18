#This code is rosponsible for calculating values between invoice and payment.

def calculate_difference(invoice_amount, user_amount, invoice_mid_value, user_mid_value):

    #Multiplying the amount with the exchange rate
    total_invoice_amount = float(invoice_amount) * float(invoice_mid_value)
    total_user_amount = float(user_amount) * float(user_mid_value)
    difference = total_invoice_amount - total_user_amount     #Difference in PLN
    
    if difference <= -0.01:
        print(f"You will receive a refund: {'{:.2f}'.format(abs(difference))} PLN")
    elif difference >= 0.01:
        print(f"An additional amount must be paid: {'{:.2f}'.format(difference)} PLN")
    else:
        print("Paid the full amount of the invoice.")

    return difference