#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.02.17

times = int(raw_input())
for _ in range(times):
    s = raw_input()
    left, right = s[:len(s)/2], s[len(s)/2:]
    print left[::-1] + right[::-1]
