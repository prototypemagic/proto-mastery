#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.02.01

# From http://www.codechef.com/FEB12/problems/MAXCOUNT

num_tests = int(raw_input())
answers = []

for _ in range(num_tests):
    len_next_line = int(raw_input()) # Not used
    numbers = sorted([int(x) for x in raw_input().split()])[::-1]

    # For each test case, output two space separated integers V & C. V
    # is the value which occurs maximum number of times and C is its
    # count.
    value, occurrences = 10001, -1
    for this_num in sorted(list(set(numbers)))[::-1]:
        count = numbers.count(this_num)
        # Save smallest number that occurs the most number of times
        if count >= occurrences:
            value, occurrences = this_num, count

    print value, occurrences
