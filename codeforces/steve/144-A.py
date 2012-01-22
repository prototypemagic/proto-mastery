#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.01.18

soldiers = int(raw_input())
heights  = [int(x) for x in raw_input().split()]

shortest = min(heights)
tallest  = max(heights)

# Move tallest to front first
tall_ndx = heights.index(tallest)

new_heights = []
new_heights.append(tallest)
new_heights += heights[:tall_ndx] + heights[tall_ndx+1:]

print tall_ndx + [x for x in reversed(new_heights)].index(shortest)
