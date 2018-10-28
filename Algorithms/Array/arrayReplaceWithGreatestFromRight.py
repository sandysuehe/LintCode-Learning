#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-27 18:33:21
# File Name: arrayReplaceWithGreatestFromRight.py
# Description: 替换为右侧最大值
# LintCode: https://www.lintcode.com/problem/replace-with-greatest-from-right/
#########################################################################
def arrayReplaceWithGreatestFromRight(nums):
    max_val = nums[len(nums)-1]
    len_nums = len(nums)

    for i in range(len_nums-1, -1, -1):
        init = nums[i]
        nums[i] = max_val
        max_val = max(max_val, init)

    nums[-1] = -1
    return nums


n = [-1,-1,-1,-1,-1,-1]
print arrayReplaceWithGreatestFromRight(n)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
