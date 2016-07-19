# Enter your code here. Read input from STDIN. Print output to STDOUT


cases = long(raw_input())
phoneBook = dict()
for i in range(0,cases):
    x,y = raw_input().split()
    phoneBook[x]=y
while True:
    try:
        inp = raw_input()
        if inp in phoneBook:
            print(inp+"="+phoneBook[inp])
        else:
            print "Not found"
    except:
        break