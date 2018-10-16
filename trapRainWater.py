#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-15 11:43:51
# File Name: trapRainWater.py
# Description: 
#########################################################################
def trapRainWater(heights):
    max_left = 0
    max_right = 0
    ans = 0
    if not heights or len(heights) == 0:
        return 0

    left = 0
    right = len(heights) - 1

    while left < right:
        if heights[left] <= heights[right]:
            max_left = max(max_left, heights[left])
            ans += max_left - heights[left]
            left += 1
        else:
            max_right = max(max_right, heights[right])
            ans += max_right - heights[right]
            right -= 1
    return ans
# vim: set noexpandtab ts=4 sts=4 sw=4 :
