# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

numShoes = int(raw_input())
sizeList = list(int (i) for i in raw_input().split())
sizeCounter = Counter(sizeList)
numCust = int(raw_input())
earning = 0
for x in range(0,numCust):
    size , price = (int (i) for i in raw_input().split())
    if size in Counter(sizeList).keys():
        earning += price
        print Counter(sizeList).values()
        