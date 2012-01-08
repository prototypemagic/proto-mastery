#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.01.08

name = raw_input()
host = raw_input()
both = raw_input()

if sorted(name+host) == sorted(both):
    print "YES"
else:
    print "NO"
