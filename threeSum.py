#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-15 15:59:49
# File Name: threeSum.py
# Description: 
#########################################################################
def threeSum(nums):
    res = []
    nums = sorted(nums)

    for i in range(0, len(nums)):
        if nums[i] > 0:
            break
        if i > 0 and nums[i-1] == nums[i]:
            continue
        target = -nums[i]
        j = i + 1
        k = len(nums) - 1

        while j < k:
            if nums[j] + nums[k] == target:
                res.append((nums[i], nums[j], nums[k]))
                while j < k and nums[j] == nums[j+1]:
                    j += 1
                while j < k and nums[k] == nums[k-1]:
                    k -= 1
                j += 1
                k -= 1
            elif nums[j] + nums[k] < target:
                j += 1
            else:
                k -= 1
    return res

nums = [-1, 0, 1, 2, -1, -4]
nums = [-1,1,0]
print threeSum(nums)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
