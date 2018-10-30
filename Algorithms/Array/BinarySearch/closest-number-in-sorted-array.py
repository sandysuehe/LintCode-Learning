#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-26 13:03:58
# File Name: closest-number-in-sorted-array.py
# Description: closest-number-in-sorted-array 
# LintCode: https://www.lintcode.com/problem/closest-number-in-sorted-array/ 
#########################################################################
def closestNumber(A, target):
    if not A:
        return -1

    left = 0
    right = len(A)-1

    while left + 1 < right:
        mid = (left+right)/2
        if A[mid] == target:
            return mid
        elif A[mid] > target:
            right = mid 
        else:
            left = mid

    if A[right] - target > target - A[left]:
        return left
    else:
        return right


A = [1, 2, 3]
target = 2
print closestNumber(A, target)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
