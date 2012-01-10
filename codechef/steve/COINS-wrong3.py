#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.01.04

# Q: Why does clever_max(num) work when num < 26, but not after?

answers = {}

def clever_max(n):
    if n < 12:
        return n
    if n == 12:
        return 13
    elif n in answers:
        return answers[n]
    else:
        answers[num/2] = clever_max(num/2)
        answers[num/3] = clever_max(num/3)
        answers[num/4] = clever_max(num/4)
        return answers[num/2] + answers[num/3] + answers[num/4]


while True:
    try:
        num = int( raw_input().strip() )
        print clever_max(num)
    except EOFError:
        break
