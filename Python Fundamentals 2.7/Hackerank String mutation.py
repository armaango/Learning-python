# Enter your code here. Read input from STDIN. Print output to STDOUT
inp = list(raw_input())
x,y = raw_input().split()
x = int(x)
inp[x] = y
inp = "".join(inp)
print inp