#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.01.29

def swapcase(letter):
    return letter.upper() if letter.islower() else letter.lower()

word = raw_input()

if all([x.isupper() for x in word]) or word[0].islower() and all([x.isupper() for x in word[1:]]):
    print ''.join([swapcase(x) for x in word])
else:
    print word
