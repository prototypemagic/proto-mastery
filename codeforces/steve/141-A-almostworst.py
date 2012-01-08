#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.01.08

name = list(raw_input())
host = list(raw_input())
both = list(raw_input())

name_host = name+host
name_host.sort()
both.sort()

if name_host == both:
    print "YES"
else:
    print "NO"
