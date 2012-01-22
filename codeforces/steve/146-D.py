#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.01.21

import sys

a, b, c, d = [int(x) for x in raw_input().split()]

# concat = ''.join([str(x) for x in [a, b, c, d]])
# if concat.count('4') + concat.count('7') != len(concat):
#     print -1
#     sys.exit(0)

def lucky_gen():
    num = '4'
    while True:
        if len(num) >= 10 and num[-10] not in '47':
            num = str( int(num)+10**9 )
            continue
        if len(num) >= 9 and num[-9] not in '47':
            num = str( int(num)+10**8 )
            continue
        if len(num) >= 8 and num[-8] not in '47':
            num = str( int(num)+10**7 )
            continue
        if len(num) >= 7 and num[-7] not in '47':
            num = str( int(num)+10**6 )
            continue
        if len(num) >= 6 and num[-6] not in '47':
            num = str( int(num)+10**5 )
            continue
        if num[-1] not in '47':
            num = str( int(num)+1 )
            continue            
        if num.count('4') + num.count('7') != len(num):
            num = str( int(num)+1 )
            continue
        yield num
        num = str( int(num)+1 )            


lucky = lucky_gen()

num = '4'
while not (num.count('4')  == a and
           num.count('7')  == b and
           num.count('47') == c and
           num.count('74') == d):
    num = lucky.next()
    if int(num) > 10**6:
        print -1
        sys.exit(0)

print num
