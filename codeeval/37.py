#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2011.08.12

import sys

alphabet = list('abcdefghijklmnopqrstuvwxyz')
#alphabet = [chr(x) for x in range( ord('a'), ord('z')+1 )]

lines = open(sys.argv[1], 'r').readlines()
lines = [x.strip() for x in lines]
#lines = [x.strip() for x in open(sys.argv[1], 'r').readlines()]

for line in lines:
    letter_list = alphabet[:]
    for letter in line:
        if letter in letter_list:
            letter_list.remove(letter)
    if letter_list:
        print ''.join(letter_list)
    else:
        print 'NULL'
