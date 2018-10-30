#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-26 12:55:20
# File Name: last-position-of-target.py
# Description: 
#########################################################################
def lastPosition(nums, target):
    if not nums or not target:
        return -1

    left = 0
    right = len(nums)-1

    while left+1 < right:
        mid = (left+right)/2

        if nums[mid] < target:
            left = mid
        elif nums[mid] > target:
            right = mid
        else:
            left = mid

    if nums[right] == target:
        return right
    elif nums[left] == target:
        return left
    else:
        return -1


nums = [1, 2, 2, 4, 5, 5]
target = 2
print lastPosition(nums, target)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
