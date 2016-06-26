import urllib
import xml.etree.ElementTree as ET

address = raw_input('Enter url: ')
if len(address) < 1 : exit(0)
print 'Retrieving', address
uh = urllib.urlopen(address)
data = uh.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)
results = tree.findall('.//count')
tot = 0
for result in results:
    tot += int(result.text)

print tot