#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-17 17:00:21
# File Name: longest-consecutive-sequence.py
# Description: 最长连续序列 Longest Consecutive Sequence 
# LintCode: https://www.lintcode.com/problem/longest-consecutive-sequence/
#########################################################################
# 思路: 
# 遍历所有数字，如果数字不在hashMap中，看该数字左右两个数字是否在hashMap中
# 如果在，则返回hashMap中的值
# 如果不在，则返回0
#########################################################################
def longestConsecutive(num):
    res = 0
    hash_map = {}
    for val in num:
        if val not in hash_map: 
            left = hash_map.get(val-1, 0)
            right = hash_map.get(val+1, 0)

            sums = left + right + 1
            res = max(res, sums)

            hash_map[val] = sums
            hash_map[val-left] = sums
            hash_map[val+right] = sums

    return res

num = [100, 4, 200, 1, 3, 2]
num = [1,2,0,1]
print num
print longestConsecutive(num)
