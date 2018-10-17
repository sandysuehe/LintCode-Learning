#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-28 13:13:52
# File Name: maxAverage.py
# Description: 
#########################################################################
def maxAverage(nums, k):
    csum = [0]
    n = len(nums)

    for i in range(0, n):
        csum.append(csum[i]+nums[i])

    ans = float(csum[k])/k

    check = 0
    for i in range(k+1, len(csum)):
        left = float(csum[i]-csum[check])/float(i-check)
        right = float(csum[i]-csum[i-k])/float(k)
        if left >= right:
            if left > ans:
                ans = left
        else:
            if right > ans:
                ans = right
            check = i - k
    return ans

nums = [1, 12, -5, -6, 50, 3]
k = 3
nums = [-2147483648,-2147483648,-2147483648,-2147483648]
k = 2
print maxAverage(nums, k)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
