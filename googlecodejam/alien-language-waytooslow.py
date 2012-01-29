#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.01.05

# From http://code.google.com/codejam/contest/dashboard?c=90101#s=p0

import itertools, re

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
for case in range(len(patterns)):
    num_matches = 0
    #for word in [''.join(tup) for tup in itertools.product(*patterns[case])]:
    for tup in itertools.product(*patterns[case]):
        word = ''.join(tup)
        if word in alien_words:
            num_matches += 1
    print "Case #%d: %d" % (case+1, num_matches)


##
## Ideas
##
'''
Before beginning each successive loop (obscured by itertools.product),
throw in an if-statement to make sure any alien words begin with the
partial word we're currently iterating through.
'''
