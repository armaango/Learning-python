# Enter your code here. Read input from STDIN. Print output to STDOUT
#Find the second highest number in a list
nums = int(raw_input())
lst = set(int(i) for i in (raw_input().split()))
lst = sorted(lst)
print lst[len(lst)-2]