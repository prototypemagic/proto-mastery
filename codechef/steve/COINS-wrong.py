#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.01.04

# This is wrong because it assumes you can only go to the bank
# once. As mentioned by a commenter below the problem description, you
# can turn 13 into 12 and 1, get $13 for the 12 and $1 for the one.

# CORRECTION: That ^^^ explanation is wrong! See the comments in
# COINS-wrong2.py.

num = ''
while True:
    try:
        num = raw_input().strip()
        num = int(num)
        conversion = num/2 + num/3 + num/4
        print conversion if conversion > num else num
    except:
        break
