#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-26 13:12:31
# File Name: search-in-a-big-sorted-array.py
# Description: 在大数组中查找 Search in a Big Sorted Array 
# LintCode: https://www.lintcode.com/problem/search-in-a-big-sorted-array/
#########################################################################
def searchBigSortedArray(reader, target):
    index = 0
    while reader.get(index) < target:
        index = index*2 + 1

    left = 0
    right = index

    while left + 1 < right:
        mid = (left+right)/2

        if reader.get(index) > target:
            right = mid
        elif reader.get(index) < target:
            left = mid
        else:
            right = mid

    if reader.get(left) == target:
        return left
    if reader.get(right) == target:
        return right

    return -1
# vim: set noexpandtab ts=4 sts=4 sw=4 :
