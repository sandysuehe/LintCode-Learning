#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (hexue@4paradigm.com)
#########################################################################
# Created Time: 2018-08-28 15:10:11
# File Name: plusOne.py
# Description: 
#########################################################################
def plusOne(nums):
    n = len(nums)
    flag = 0
    for i in range(n-1, -1, -1):
        if i == n - 1:
            val = (nums[i] + 1 + flag) % 10
            flag = (nums[i] + 1 + flag) / 10
        else:
            val = (nums[i] + flag) % 10
            flag = (nums[i] + flag) / 10

        nums[i] = val

        if flag == 0:
            break 

    if flag == 1:
        nums.insert(0, 1)
    return nums


#nums = [1, 2, 3]
nums = [9, 9, 9]
print plusOne(nums)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
