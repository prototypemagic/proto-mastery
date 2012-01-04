#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2011.06.08

import sys

lines = open(sys.argv[1], 'r').readlines()

for line in lines:
    chars = [x for x in line.split()]
    nums, ops, stack = '0123456789', '+-*/%', []
    while len(chars) > 1:
        while chars[0] in ops and chars[1] in ops:
            stack.append(chars.pop(0))
        op, num1, num2 = chars.pop(0), chars.pop(0), chars.pop(0)
        chars.insert(0, str(eval(num1+op+num2)))
        if stack:
            chars.insert(0, stack.pop(-1))
        else:
            print chars[0]
            break
