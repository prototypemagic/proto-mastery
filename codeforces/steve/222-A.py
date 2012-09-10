#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2012.09.10

import os

def solve():
    n, k = [int(x) for x in raw_input().split()]
    nums = [int(x) for x in raw_input().split()]
    # assert len(nums) == n
    steps = 0
    # while len(set(nums)) != 1:
    while not all([ nums[ndx] == nums[ndx+1] for ndx in range(len(nums[:-1])) ]):
        nums.append(nums[k-1])
        nums = nums[1:]
        if len(nums) >= 2:
            if nums[k-1] != nums[k]:
                return -1
        steps += 1
    return steps


if __name__ == '__main__':
    print solve()
