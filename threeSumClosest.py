#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-15 17:08:31
# File Name: threeSumClosest.py
# Description: 
#########################################################################
def threeSumClosest(nums, target):
    nums = sorted(nums)
    closest = nums[0] + nums[1] + nums[2]
    diff = abs(closest - target)

    for i in range(0, len(nums)-2):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            three_sum = nums[i] + nums[j] + nums[k]
            new_diff = abs(three_sum - target)
            if diff > new_diff:
                diff = new_diff
                closest =  three_sum
            if three_sum < target:
                j += 1
            else:
                k -= 1
    return closest

nums = [-1, 2, 1, -4]
target = 1
print threeSumClosest(nums, target)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
