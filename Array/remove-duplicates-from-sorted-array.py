#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-22 13:11:51
# File Name: remove-duplicates-from-sorted-array.py
# Description: 删除排序数组中的重复数字 
# LintCode: https://www.lintcode.com/problem/remove-duplicates-from-sorted-array/
#########################################################################
def removeDuplicates(nums):
    if len(nums) in (0, 1):
        return len(nums)

    i = 1
    j = 1

    while j < len(nums):
        if nums[j] != nums[j-1]:
            nums[i] = nums[j]
            i += 1
        j += 1
    return i

nums = [1,1,2]
print removeDuplicates(nums)
