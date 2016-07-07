# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function
inp = raw_input()
for char in inp:
    if char.isupper():
        print (char.lower(),sep="",end="")
    else:
        print (char.upper(),sep="",end="")