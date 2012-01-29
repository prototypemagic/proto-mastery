#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.01.29

import re

# "The first line of input contains 3 integers, L, D and N separated
# by a space."
L, D, N = [int(x) for x in raw_input().split()]

# "D lines follow, each containing one word of length L. These are the
# words that are known to exist in the alien language."
alien_words = []
for _ in range(D):
    s = raw_input()
    alien_words.append(s)

# "N test cases then follow, each on its own line and each consisting
# of a pattern as described above."
patterns = []
for _ in range(N):
    letter_groups = []
    line = raw_input()
    seqs = re.findall(r'(\(\w+\))', line) # find paren-wrapped digit seqs
    for seq in seqs:
        cleaned_seq = seq.replace('(', '').replace(')', '')
        letter_groups.append(cleaned_seq)
        line = line.replace(seq, '', 1) # do a maximum of 1 replacement
    # Only individual letters remain
    for letter in line:
        letter_groups.append(letter)
    patterns.append(letter_groups) # `patterns` is a list of lists

# At this point, if we started out with the lines '(abc)xy(za)' and
# 'c(yz)', patterns == [['abc', 'x', 'y', 'za'], ['c', 'yz']]
#for word in alien_words:
for p_ndx in range(len(patterns)):
    matches = 0
    for word in alien_words:
        if all([w in p for (w, p) in zip(word, patterns[p_ndx])]):
            matches += 1
    print "Case #%d: %d" % (p_ndx+1, matches)
