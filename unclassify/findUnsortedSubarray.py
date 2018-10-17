#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-28 10:56:17
# File Name: findUnsortedSubarray.py
# Description: 
#########################################################################
def findUnsortedSubarray(nums):
    left = 0
    right = len(nums) - 1
    temp = sorted(nums)
    while left < len(nums) and nums[left] == temp[left]:
        left += 1
    while right > left and nums[right] == temp[right]:
        right -= 1
    return right - left + 1

nums = [2, 6, 4, 8, 10, 9, 15]
print findUnsortedSubarray(nums)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
