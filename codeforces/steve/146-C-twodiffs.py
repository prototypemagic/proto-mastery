#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.01.22

a = raw_input()
b = raw_input()
n = len(a) # len(a) == len(b)

# print r'%s' % a
# print r'%s' % b

def naive_diff(x, y):
    '''Counts how many digits differ, digit by digit'''
    return sum([1 if tup[0] != tup[1] else 0 for tup in zip(x, y)])

# print naive_diff('44',  '77')
# print naive_diff('474', '777')
# print naive_diff('447', '774')
# print naive_diff('74777', '77477')

def swap(num, ndx):
    return num[:ndx] + num[ndx+1] + num[ndx] + num[ndx+2:]

def swap_diff(x, y):
    '''Falsely assumes swapping is all that is necessary, and that '''
    changes = 0
    for ndx in range(n-1):
        if x[ndx] != y[ndx] and x[ndx+1] != y[ndx+1] and x[ndx] == y[ndx+1]:
            x = swap(x, ndx)
            changes += 1
            # y = swap(y, ndx)
    return x, changes


# Naive only
naive = naive_diff(a, b)

# Swap only is equivalent to hybrid; naive_diff(a, b) will be 0

# Hybrid technique
new_a, changes = swap_diff(a, b)
hybrid = naive_diff(new_a, b) + changes

print min([naive, hybrid])
