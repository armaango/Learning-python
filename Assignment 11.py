import urllib.request

fh = urllib.request.urlopen("http://www.pythonlearn.com/code/intro-short.txt")

for line in fh:
    line.strip()
    print(line)
