cases = int(raw_input())
dic = dict()
for x in range (0, cases):
    lst = raw_input().split()
    tot = 0
    for y in range (1,len(lst)):
        tot += float(lst[y])
    avg = tot/float((len(lst)-1))
    dic[lst[0]] = avg
name = raw_input()
print("%.2f" % dic[name])