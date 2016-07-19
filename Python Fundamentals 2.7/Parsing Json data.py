import urllib
import json

link = raw_input("Enter url : ")
data = urllib.urlopen(link)
content = data.read()
info = json.loads(content)
countData = info["comments"]
tot = 0
for item in countData:
    tot += int(item['count'])
print tot