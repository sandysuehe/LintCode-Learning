#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (hexue@4paradigm.com)
#########################################################################
# Created Time: 2018-08-23 14:36:57
# File Name: containsNearbyAlmostDuplicate.py
# Description: 
#########################################################################
def containsNearbyAlmostDuplicate(nums, k, t):
    if k < 1 or t < 0:
        return False

    num_dict = {}
    for i in range(0, len(nums)):
        key = nums[i] / max(1, t)
        for j in (key, key-1, key+1):
            if j in num_dict and abs(nums[i]-num_dict[j]) <= t:
                return True
            num_dict[key] = nums[i]
            if i >= k:
                num_dict.pop()
    return False
# vim: set noexpandtab ts=4 sts=4 sw=4 :
