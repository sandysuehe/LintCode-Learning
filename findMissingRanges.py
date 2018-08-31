#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (hexue@4paradigm.com)
#########################################################################
# Created Time: 2018-08-29 15:46:22
# File Name: findMissingRanges.py
# Description: 
#########################################################################
def findMissingRanges(nums, lower, upper):
    n = len(nums)
    ans = []

    left = lower
    for i in range(0, n+1):
        if i < n and nums[i] <= upper:
            right = nums[i]
        else:
            right = upper + 1

        if left == right:
            left += 1
        elif right > left:
            if right - left == 1:
                ans.append(str(left))
            else:
                ans.append("{0}->{1}".format(left, right-1))

            left = right + 1
    return ans


nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print findMissingRanges(nums, lower, upper)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
