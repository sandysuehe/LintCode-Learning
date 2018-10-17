#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# LintCode: https://www.lintcode.com/problem/sort-colors
# Subject:  Sort Colors 颜色分类 
#########################################################################
# 思路：快速排序
#########################################################################
def sortColors(nums):
    pos = sort(nums, 0, 0)
    sort(nums, 1, pos)
    return nums

def sort(nums, target, index):
    left = index
    right = len(nums) - 1

    while left <= right:
        while left <= right and nums[left] == target:
            left += 1
        while left <= right and nums[right] != target:
            right -= 1

        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    return left


nums = [1, 0, 1, 2]
print sortColors(nums)
