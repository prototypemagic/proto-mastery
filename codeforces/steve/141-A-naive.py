#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.01.08

name, host, both = [raw_input() for _ in range(3)]

if sorted(name+host) == sorted(both):
    print "YES"
else:
    print "NO"
