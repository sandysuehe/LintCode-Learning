#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-07 16:48:48
# File Name: kth-largest-in-n-arrays.py
# Description: N数组第K大元素 
# LintCode: https://www.lintcode.com/problem/kth-largest-in-n-arrays/
#########################################################################
def KthInArrays(arrays, k):
    merge_array = []
    for array in arrays:
        merge_array.extend(array)
    return quick_select(0, len(merge_array)-1, merge_array, k)

def quick_select(start, end, nums, k):
    if start == end:
        return nums[start]
    left = start
    right = end
    p = nums[(start+end)/2]

    while left <= right:
        while left <= right and nums[left] > p:
            left += 1
        while left <= right and nums[right] < p:
            right -= 1

        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    if start <= right and right >= k:
        quick_select(start, right, nums, k)
    if left <= end and left <= k:
        quick_select(left, end, nums, k)

    return nums[k]

arrays = [[9,3,2,4,7],[1,2,3,4,8]]
k = 2
print KthInArrays(arrays, k)

arrays = [[9,3,2,4,8],[1,2,3,4,2]]
k = 2
print KthInArrays(arrays, k)
