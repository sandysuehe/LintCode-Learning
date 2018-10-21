#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-28 13:13:52
# File Name: maxAverage.py
# Description: Maximum Average Subarray
# LintCode: https://www.lintcode.com/problem/maximum-average-subarray/
#########################################################################
def maxAverage(nums, k):
    n = len(nums)
    max_val = float("-inf")

    for left in range(0, n - k + 1):
        for right in range(left + k - 1, n):
            val = 0
            for i in range(left, right+1):
                val += nums[i]
            avg = float(val) / float(right - left + 1)
            max_val = max(avg, max_val)
            right += 1
    return max_val

nums = [1, 12, -5, -6, 50, 3]
k = 3
print maxAverage(nums, k)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
