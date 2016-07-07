# Enter your code here. Read input from STDIN. Print output to STDOUT
inp = raw_input()
c = [0,0,0,0,0]
for char in inp:
    if char.isalnum():
        c[0]+=1
    if char.isalpha():
        c[1] +=1
    if char.isdigit():
        c[2]+=1
    if char.islower():
        c[3]+=1
    if char.isupper():
        c[4]+=1
for i in range (0,5):
    if c[i] > 0:
        print 'True'
    else:
        print 'False'Read Phone State -Phone
Access Fine location - Location
Write External Storage- Storage