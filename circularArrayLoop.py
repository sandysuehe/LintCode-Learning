#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-15 14:54:25
# File Name: circularArrayLoop.py
# Description: 
#########################################################################
def circularArrayLoop(nums):
    if not nums or len(nums) < 2:
        return False

    step = nums[0]
    i = 0
    tmp = []
    while i < len(nums):
        if i+step < len(nums):
            tmp.append(nums[i])
            if nums[i+step] in tmp:
                return True
            step = nums[i+step]
            i += step
        else:
            return False
    return False

nums =  [2, -1, 1, 2, 2]
nums = [-1, 2]
print circularArrayLoop(nums)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
