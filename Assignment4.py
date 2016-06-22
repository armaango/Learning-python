def computepay(h, r):
    if h <= 40:
        p = h * r
        return p
    elif h > 40:
        p = (r * 40) + (r * 1.5 * (h-40))
        return p

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
pay = computepay(h, r)
print("Pay", pay)
