#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-18 18:23:00
# File Name: window-sum.py
# Description:  滑动窗口内数的和
# LintCode: https://www.lintcode.com/problem/window-sum/
#########################################################################
def winSum(nums, k):
    n = len(nums)
    if n < k or k <= 0:
        return []
    sums = [0] * (n-k+1)

    for i in range(k):
        sums[0] += nums[i]

    for i in range(1, n-k+1):
        sums[i] = sums[i-1] - nums[i-1] + nums[i-1+k]

    return sums

nums = [1,2,7,8,5]
k = 3
print winSum(nums, k)
