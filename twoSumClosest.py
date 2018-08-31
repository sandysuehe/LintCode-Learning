#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (hexue@4paradigm.com)
#########################################################################
# Created Time: 2018-08-15 17:28:46
# File Name: twoSumClosest.py
# Description: 
#########################################################################
def twoSumClosest(nums, target):
    nums = sorted(nums)
    closest = nums[0] + nums[1]
    diff = abs(closest-target)

    for i in range(0, len(nums)-1):
        j = i + 1
        while i < j:
            two_sum = nums[i] + nums[j]
            new_diff = abs(two_sum-target)

            if new_diff < diff:
                diff = new_diff
                closest = two_sum

            if two_sum < target:
                i += 1
            else:
                j -= 1
    return closest

nums = [-1, 2, 1, -4]
target = 4
print twoSumClosest(nums, target)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
