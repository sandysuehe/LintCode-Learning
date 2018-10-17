#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-28 12:53:23
# File Name: findMaxAverage.py
# Description: 
#########################################################################
def findMaxAverage(nums, k):
    n = len(nums)
    max_val = float("-inf")

    for i in range(0, n - k + 1):
        val = 0
        for j in range(i, i + k):
            val += nums[j]
        max_val = max(val, max_val)
    return float(max_val)/float(k)


nums = [1,12,-5,-6,50,3]
k = 4
nums = [5]
k = 1
print findMaxAverage(nums, k)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
