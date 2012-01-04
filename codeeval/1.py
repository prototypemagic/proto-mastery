#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2011.06.08

import sys

lines = open(sys.argv[1], 'r').readlines()

for line in lines:
    answer = []
    a, b, max_num = [int(x) for x in line.split()]
    for num in range(1, max_num+1):
        if num % a == 0 and num % b == 0:
            answer.append("FB")
        elif num % a == 0:
            answer.append("F")
        elif num % b == 0:
            answer.append("B")
        else:
            answer.append(str(num))
    print " ".join(answer)
