#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# LintCode: https://www.lintcode.com/problem/find-minimum-in-rotated-sorted-array
# Subject:  Find Minimum in Rotated Sorted Array 寻找旋转排序数组中的最小值
#########################################################################
# 思路：二分查找
#########################################################################
def findMin(self, nums):
    # write your code here
    n = len(nums)
    if n == 0:
        return -1

    left = 0
    right = n - 1

    while left + 1 < right:
        mid = (left + right) / 2
        if nums[mid]> nums[right]:
            left = mid
        else:
            right = mid

    return min(nums[left], nums[right])
