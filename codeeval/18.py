#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2011.06.08

import sys

lines = open(sys.argv[1], 'r').readlines()

for line in lines:
    x, n = [int(a) for a in line.split(',')]
    
