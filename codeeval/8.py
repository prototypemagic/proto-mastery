#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2011.06.08

import sys

lines = open(sys.argv[1], 'r').readlines()

for line in lines:
    words = line.split()
    print ' '.join(words[-x-1] for x in range(len(words)))
