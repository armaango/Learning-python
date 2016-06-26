import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
count = int(raw_input('Enter count -'))
pos = int(raw_input('Enter Position'))
i = 0
while i < count :

    soup = BeautifulSoup(html)
    # Retrieve all of the anchor tags
    tags = soup('a')
    url = tags[pos-1].get('href', None)
    name = tags[pos-1].contents[0]
    print name
    html = urllib.urlopen(url).read()
    i += 1

    # Look at the parts of a tag

