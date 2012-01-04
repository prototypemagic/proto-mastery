#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2011.06.08

import sys

lines = open(sys.argv[1], 'r').readlines()

for line in lines:
    chars = [x for x in line.split()]
    nums = '0123456789'
    while len(chars) > 1:        
        ndx = 0
        if chars[ndx] not in nums and chars[ndx+1] in nums and chars[ndx+2] in nums:
            op, num1, num2 = chars.pop(ndx), chars.pop(ndx), chars.pop(ndx)
            chars.insert(ndx, str(eval(num1+op+num2)))
            ndx = 0
        ndx += 1
    print chars[0]

