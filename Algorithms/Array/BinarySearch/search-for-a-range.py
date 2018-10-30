#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-26 10:26:37
# File Name: search-for-a-range.py
# Description: 搜索区间 
# LintCode: https://www.lintcode.com/problem/search-for-a-range/
#########################################################################
def searchRange(A, target):
    left = 0
    right = len(A) - 1
    index = search(A, left, right, target)

    if index == -1:
        return (-1, -1)

    left = index
    right = index

    while left > 0 and A[left-1] == A[index]:
        left -= 1
    while right < len(A)-1 and A[right+1] == A[index]:
        right += 1
    return (left, right)

def search(nums, left, right, target):
    while left <= right:
        mid = (left+right)/2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid -1
    return -1

A = [5, 7, 7, 8, 8, 10]
target = 8
A = [1]
target = 1
print searchRange(A, target)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
