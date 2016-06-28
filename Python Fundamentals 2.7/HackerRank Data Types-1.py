# Enter your code here. Read input from STDIN. Print output to STDOUT
cases = int(raw_input())
lst = []
for x in range (0,cases):
    inp = raw_input().strip().split()
    if inp[0] == "insert":
        lst.insert(int(inp[1]),int(inp[2]))
    elif inp [0] == "remove":
        lst.remove(int(inp[1]))
    elif inp [0] =="print":
        print lst
    elif inp[0] == "append":
        lst.append(int(inp[1]))
    elif inp[0] == "pop":
        lst.pop()
    elif inp[0] == "sort":
        lst.sort()
    elif inp[0] == "reverse":
        lst.reverse()
    