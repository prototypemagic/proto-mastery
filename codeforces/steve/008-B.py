#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.02.07

# From http://codeforces.com/problemset/problem/8/B

# Define the starting point as [0, 0]. Return "OK" if the robot never
# crosses its path, "BUG" otherwise
def surrounding_squares(square):
    '''Returns list of [x, y] coordinates surrounding the passed-in
    square coordinates, including the point itself'''
    x, y = square
    surrounding = []
    surrounding.append([x, y])   # Original point
    surrounding.append([x, y+1]) # Up
    surrounding.append([x, y-1]) # Down
    surrounding.append([x-1, y]) # Left
    surrounding.append([x+1, y]) # Right
    return surrounding


def suboptimal_path(directions):
    visited_or_adjacent = []
    am_at               = [0, 0] # [x, y] coordinates
    for d in directions:
        # Record where the robot just was
        was_at = am_at
        # Move robot to new location
        if d == 'U':   # Up
            am_at = [am_at[0], am_at[1]+1]
        elif d == 'D': # Down
            am_at = [am_at[0], am_at[1]-1]
        elif d == 'L': # Left
            am_at = [am_at[0]-1, am_at[1]]
        elif d == 'R': # Right
            am_at = [am_at[0]+1, am_at[1]]
        # If new location has been visited, or is adjacent to a
        # previously-visited square _not including the previous one_,
        # the robot contains a bug, for its path is suboptimal
        if am_at in visited_or_adjacent:
            return "BUG"
        visited_or_adjacent += surrounding_squares(was_at)
    return "OK"

print suboptimal_path(raw_input())
