#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-15 16:43:17
# File Name: threeSumSmaller.py
# Description: 
#########################################################################
def threeSumSmaller(nums, target):
    if len(nums) < 3:
        return 0

    res = 0
    nums = sorted(nums)

    for i in range(0, len(nums)-2):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            # 判断三个数之和小于targe
            # 如果nums[i] + nums[j] + nums[k] < target
            # 可以推出nums[i] + nums[j] + nums[j+1] < target
            # 可以推出nums[i] + nums[j] + nums[j+2] < target
            # ........
            # 可以推出nums[i] + nums[j] + nums[k-1] < target
            if nums[i] + nums[j] + nums[k] < target:
                res += k - j
                j += 1
            else:
                k -= 1
    return res

nums = [-2,0,1,3]
target = 2
print threeSumSmaller(nums, target)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
