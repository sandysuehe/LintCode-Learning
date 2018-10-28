#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-29 15:46:22
# File Name: findMissingRanges.py
# Description: Missing Ranges 缺失区间
# LintCode: https://www.lintcode.com/problem/missing-ranges/ 
#########################################################################
def findMissingRanges(nums, lower, upper):
    ans = []
    nums.insert(0, lower-1)
    nums.append(upper+1)
    n = len(nums)

    for i in range(0, n-1):
        if nums[i+1] - nums[i] > 2:
            ans.append("{0}->{1}".format(nums[i]+1, nums[i+1]-1))
        elif nums[i+1] - nums[i] == 2:
            ans.append(str(nums[i]+1))
    return ans


nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print findMissingRanges(nums, lower, upper)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
