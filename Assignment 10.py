name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
ndict = dict()
for line in handle:
    if not line.startswith("From "):
        continue
    line = line.strip()
    lst = line.split()
    time = lst[5]
    tList = time.split(":")
    tHour = tList[0]
    ndict[tHour] = ndict.get(tHour, 0) + 1
tmp = ndict.items()
for tItem in sorted(tmp):
    print(tItem)