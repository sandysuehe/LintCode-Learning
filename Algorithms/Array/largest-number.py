#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-07 16:48:48
# File Name: largest-number.py
# Description: 最大数 
# LintCode: https://www.lintcode.com/problem/largest-number/ 
#########################################################################
def largestNumber(nums):
    res = ""
    nums = sorted(nums, cmp=lambda x, y: 1 if str(x) + str(y) < str(y) + str(x) else -1)
    print nums
    for i in range(len(nums)):
        res += str(nums[i])
    if res[0] == "0":
        return "0"
    return res

nums = [1, 20, 23, 4, 8]
nums = [5,13]
print largestNumber(nums)
