# Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(raw_input())
stamps = set()
for n in range(0,num):
    stamps.add(raw_input().strip())
print len(stamps)