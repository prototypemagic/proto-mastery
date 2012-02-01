#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.02.01

num_tests = int(raw_input())
answers = []

for _ in range(num_tests):
    len_next_line = int(raw_input()) # Not used
    numbers = [int(x) for x in raw_input().split()]
    maybe_answers = []

    # For each test case, output two space separated integers V & C. V
    # is the value which occurs maximum number of times and C is its
    # count.
    most_frequent, occurrences = 10001, -1
    number_set = set(numbers)
    for this_num in number_set:
        count = numbers.count(this_num)
        # print "count ==", count
        # Save smallest number that occurs the most number of times
        if count >= occurrences:
            maybe_answers.append([this_num, count])

    correct_answer = sorted(maybe_answers, key=lambda x: x[0])[-1]
    answers.append(correct_answer)


print
for v, c in answers:
    print v, c
