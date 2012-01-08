#!/usr/bin/env python

num_words = int(raw_input())

for _ in range(num_words):
    word = raw_input()
    if len(word) > 10:
        print word[0] + str(len(word)-2) + word[-1]
    else:
        print word
