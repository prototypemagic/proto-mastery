#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2011.06.08

import sys

lines = open(sys.argv[1], 'r').readlines()

for line in lines:
    nums = [int(x) if x.strip() != '' else 0 for x in line.split(',')]
    indices = range(len(nums))
    print max([ sum(nums[x:y+1]) for x in indices for y in indices if x < y ])
