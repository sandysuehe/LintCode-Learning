#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-26 11:48:42
# File Name: maximum-number-in-mountain-sequence.py
# Description: 山脉序列中的最大值 Maximum Number in Mountain Sequence
# LintCode: https://www.lintcode.com/problem/maximum-number-in-mountain-sequence/
#########################################################################
def mountainSequence(nums):
    left = 0
    right = len(nums) - 1

    while left + 1 < right:
        mid = (left+right)/2

        if nums[mid] < nums[mid+1]:
            left = mid
        else:
            right = mid

    if nums[right] > nums[left]:
        return nums[right]
    else:
        return nums[left]


nums = [1, 2, 4, 8, 6, 3]
print mountainSequence(nums)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
