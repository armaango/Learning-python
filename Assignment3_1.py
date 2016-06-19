#Assignment 3.1

hrs = input("Enter hours:")
h = float(hrs)
rate = input("Enter rate:")
rate = float(rate)
if hrs <= 40:
    grossPay = rate * hrs
    print(grossPay)
elif hrs > 40:
    grossPay = (rate *40)+(rate*1.5*(hrs-40))
    print(grossPay)
quit()
