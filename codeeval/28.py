#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2011.06.08

import sys

lines = open(sys.argv[1], 'r').readlines()

for line in lines:
    string, sub = [x for x in line.strip().split(',')]
    if sub in string: # Leaves out regex
        print 'true'
    else:
        print 'false'
