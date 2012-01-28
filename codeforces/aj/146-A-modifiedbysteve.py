#!/usr/bin/env python
# AJ Bahnken / avb_wkyhu
# 2012.01.21

half = int(raw_input()) / 2
t    = ticket_digits = [int(x) for x in raw_input()]

if t.count(4) + t.count(7) == len(t) and sum(t[half:]) == sum(t[:half]):
    print "YES"
else:
    print "NO"

