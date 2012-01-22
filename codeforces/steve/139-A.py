#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.01.21

num_book_pages = int(raw_input())
pages_per_day  = [int(x) for x in raw_input().split()]
DAYS_PER_WEEK  = 7

def day_yielder():
    '''
    Generator function. Returns tuple of the form (ndx from 0 to 6,
    pages read that day). Loops infinitely (0 1 2 3 4 5 6 0 1 2 3...)
    '''
    ndx = 0
    while True:
        yield (ndx % DAYS_PER_WEEK, pages_per_day[ndx % DAYS_PER_WEEK])
        ndx += 1

days = day_yielder()

total_pages_read = 0

# Loop stops when book is finished
while total_pages_read < num_book_pages:
    ndx, pages_read_today = days.next()
    total_pages_read += pages_read_today

# Compensate for our day numbering (0-6) v. their numbering (1-7)
print ndx + 1
