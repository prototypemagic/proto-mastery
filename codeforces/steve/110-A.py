#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.02.05

n = raw_input()

lucky_digits = str(n.count('4') + n.count('7'))

if lucky_digits.count('4') + lucky_digits.count('7') == len(lucky_digits):
    print "YES"
else:
    print "NO"
