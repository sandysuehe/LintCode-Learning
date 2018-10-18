#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-18 16:39:57
# File Name: search-in-rotated-sorted-array.py
# Description: 
# 思路:
# 如果中间的数小于最右边的数，则右半段是有序的;
# 若中间数大于最右边数，则左半段是有序的;
# 我们只要在有序的半段里用首尾两个数组来判断目标值是否在这一区域内，这样就可以确定保留哪半边了
#########################################################################
def search(A, target):
    # write your code here
    left = 0
    right = len(A) - 1

    while left <= right:
        mid = (left + right)/2
        if A[mid] == target:
            return mid
        elif A[mid] < A[right]:
            # 右边部分(mid->right)有序
            if A[mid] < target and A[right] >= target:
                left = mid + 1
            else:
                right = mid - 1
        else:
            # 左边部分(left->mid)有序, 对左边部分做判断
            if A[left] <= target and A[mid] > target: 
                right = mid - 1
            else:
                left = mid + 1
    return -1

A = [4, 5, 1, 2, 3]
target = 1
print search(A, target)
target = 0
print search(A, target)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
