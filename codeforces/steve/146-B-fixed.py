#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.01.21

import sys

a, b = raw_input().split()

def mask(n):
    if n.count('4') + n.count('7') == len(n):
        return n
    new_str = ''
    for d in n:
        if d in '47':
            new_str += d

    return new_str

test_num = str( int(a)+1 )
while mask(test_num) != b:
    test_num = str( int(test_num)+1 )

print test_num
