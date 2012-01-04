#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.01.03

withdraw, balance = [x for x in raw_input().split()]
withdraw = int(withdraw)
balance  = float(balance)

if withdraw + 0.5 <= balance and withdraw % 5 == 0:
    balance -= withdraw + 0.5

print "%.2f" % balance
