# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n,m = (int(i) for i in raw_input().split())
d = defaultdict(list)
for j in range (1,n+1):
    d[raw_input()].append(j)
for k in range(0,m):
    wordB = raw_input()
    if wordB in d.keys():
        print " ".join([str(x) for x in d[wordB]] )
    else:
        print "-1"