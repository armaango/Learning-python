# simple program to read a file and
# calculate the sum of all the numerals
#  in the file using Regex

import re
fh = open("regex_sum_221800.txt")
data = fh.read()
total = sum(int(num) for num in (re.findall("[0-9]+", data)))
print(total)
fh.close()
