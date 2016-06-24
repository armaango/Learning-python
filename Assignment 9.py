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
    mailId = lst[1]
    ndict[mailId] = ndict.get(mailId,0) + 1
largest = 0
for key in ndict:
    if ndict[key] > largest:
        largest = ndict[key]
        mId = key
print(key, largest)
