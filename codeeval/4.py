#!/usr/bin/env python
# 2011.02.07
# Prime generator from http://code.activestate.com/recipes/366178-a-fast-prime-number-list-generator/#c13

from math import sqrt

def primes_below(high):
    "Returns list of primes below high, inclusive"
    sqrt_high = int(sqrt(high))
    sieve = range(high+1)
    sieve[1] = 0

    for i in xrange(2, sqrt_high+1):
        if sieve[i] != 0:
            sieve[i*i: high+1 : i] = [0] * len(sieve[i*i: high+1 : i])

    return [x for x in sieve if x]

# My one-liner :-)
print sum(primes_below(1000)),
