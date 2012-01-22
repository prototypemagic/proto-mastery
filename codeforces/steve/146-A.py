#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.01.21

import sys

n   = int(raw_input())
num = raw_input()

if num.count('4') + num.count('7') != n:
    print "NO"
    sys.exit(0)

first_half  = sum([int(x) for x in num[:n/2]])
second_half = sum([int(x) for x in num[n/2:]])

print "YES" if first_half == second_half else "NO"
