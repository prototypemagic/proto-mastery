#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.01.04

# The following is wrong, to say the least, because input == 13 should
# produce output == 13, not 14. As the problem states, you cannot
# exchange Bytelandian coins for other Bytelandian coins.

def naive_max(num):
    # Given in problem description
    return num/2 + num/3 + num/4

def clever_max(num):
    '''Turns every 12 bytelandian coins into 13, plus remainder'''
    # NOT given in problem description
    naive = naive_max(num)
    maybe_bigger = (num/12) * 13 + (num % 12) # WRONG!
    return maybe_bigger if maybe_bigger > naive else naive


n = 0
while True:
    try:
        n = int( raw_input().strip() )
        print max([n, clever_max(n),
                   clever_max(n/2) + clever_max(n/3) + clever_max(n/4)])
    except:
        break
