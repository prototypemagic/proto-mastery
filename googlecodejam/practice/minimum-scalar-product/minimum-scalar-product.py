#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2011.05.06

import sys

lines = open(sys.argv[1], 'r').readlines()
#print "\n".join([line.strip() for line in lines])
output_file = open(sys.argv[2], 'w')
answer = []

gen = (x.strip() for x in lines)
for it in range(int(gen.next())):
    

output_file.write("\n".join(answer))
