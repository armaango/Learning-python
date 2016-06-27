# Enter your code here. Read input from STDIN. Print output to STDOUT
# VAlidating a Regex pattern
import re
cases = int(raw_input())
for x in range(0, cases):
    regPattern = raw_input().strip()
    try :
        re.compile(regPattern)
        print "True"
    except re.error:
        print "False"