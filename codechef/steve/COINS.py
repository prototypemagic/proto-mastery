#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.01.04

answers = {}

def clever_max(n):
    if n < 12:
        return n
    if n == 12:
        return 13
    elif n in answers:
        return answers[n]
    else:
        answers[n/2] = clever_max(n/2)
        answers[n/3] = clever_max(n/3)
        answers[n/4] = clever_max(n/4)
        return answers[n/2] + answers[n/3] + answers[n/4]


def main():
    while True:
        try:
            # Wrapping everything in main so n isn't global
            n = int(raw_input())
            print clever_max(n)
        except EOFError:
            break


main()
