#!/bin/python
from __future__ import print_function
import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
for i in reversed(arr):
    print (i,sep=" ",end =' ')