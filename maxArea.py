#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-15 14:52:21
# File Name: maxArea.py
# Description: 
#########################################################################
def maxArea(height):
    res = 0
    left = 0
    right = len(height) - 1

    while left < right:
        min_height = min(height[left], height[right])
        res = max(res, min_height * (right - left))

        while left < right and min_height == height[left]:
            left += 1
        while left < right and min_height == height[right]:
            right -= 1

    return res

height = [1,3,2]
print maxArea(height)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
