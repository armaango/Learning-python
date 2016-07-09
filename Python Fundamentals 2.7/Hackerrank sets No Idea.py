# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = (int(i) for i in raw_input().split())
arr = list(int(i) for i in raw_input().split())
A = set(int(i) for i in raw_input().split())
B = set(int(i) for i in raw_input().split())
happiness = 0
for num in arr:
    if num in A:
        happiness +=1
    elif num in B:
        happiness -=1
print happiness