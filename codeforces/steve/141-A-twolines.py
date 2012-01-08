#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.01.08

name, host, both = [raw_input() for _ in range(3)]
print "YES" if sorted(name+host) == sorted(both) else "NO"
