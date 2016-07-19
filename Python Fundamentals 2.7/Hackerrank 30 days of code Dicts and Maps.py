# Enter your code here. Read input from STDIN. Print output to STDOUT

cases = int(raw_input())
phoneBook = dict()
for i in range(0,cases):
    x,y = raw_input().split()
    phoneBook[x]=y
t = raw_input()
while(t != ""):
    if t in phoneBook.keys():
        print(t+"="+phoneBook[t])
    else:
        print "Not found"
    t = raw_input()