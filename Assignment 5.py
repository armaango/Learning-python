largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
        try:
            num = int(num)
            if largest is None:
                largest = num
            elif largest < num:
                largest = num
            if smallest is None:
                smallest = num
            elif smallest > num:
                smallest = num
        except:
            print("Invalid Input")
            continue

print ("Maximum", largest)
print ("Minimum", smallest)