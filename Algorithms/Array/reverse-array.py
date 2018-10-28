#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-15 15:59:49
# File Name: reverse-array.py
# Description: 翻转数组
# LintCode: https://www.lintcode.com/problem/reverse-array/
#########################################################################
def reverseArray(nums):
    i = 0
    j = len(nums) - 1

    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    return nums

nums = [1,2,5]
print reverseArray(nums)
