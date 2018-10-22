#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-22 19:40:30
# File Name: median-of-two-sorted-arrays.py
# Description: Median of Two Sorted Arrays 两个有序数组的中位数 
# LintCode: https://www.lintcode.com/problem/median-of-two-sorted-arrays/
#########################################################################
def findMedianSortedArrays(A, B):
    # write your code here
    n = len(A) + len(B)
    if n % 2 == 1:
        return findKth(A, B, n/2+1)
    else:
        smaller = findKth(A, B, n / 2)
        bigger = findKth(A, B, n / 2 + 1)
        return (smaller + bigger) / 2.0

def findKth(A, B, k):
    if len(A) == 0:
        return B[k-1]
    if len(B) == 0:
        return A[k-1]
    if k == 1:
        return min(A[0], B[0])

    if len(A) >= k/2:
        a = A[k/2-1]
    else:
        a = None

    if len(B) >= k/2:
        b = B[k/2-1]
    else:
        b = None

    if not b or (a and a<b):
        return findKth(A[k/2:], B, k-k/2)
    return findKth(A, B[k/2:], k-k/2)

A = [1,2,3,4,5,6]
B = [2,3,4,5]
print findMedianSortedArrays(A, B)
A = [1,2,3]
B = [4,5]
print findMedianSortedArrays(A, B)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
