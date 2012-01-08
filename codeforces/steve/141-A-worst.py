#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.01.08

name = raw_input()
host = raw_input()
both = raw_input()

name_host = list(name+host)
name_host.sort()

both = list(both)
both.sort()

if name_host == both:
    print "YES"
else:
    print "NO"
