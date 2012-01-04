#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2011.06.08

import sys

lines = open(sys.argv[1], 'r').readlines()

for line in lines:
    a, b = [x for x in line.split(';')]
    
