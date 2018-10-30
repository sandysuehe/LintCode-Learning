#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-26 12:53:01
# File Name: find-peak-element.py
# Description: find-peak-element 
# https://www.lintcode.com/problem/find-peak-element/
#########################################################################
def findPeak(self, A):
    # write your code here
    n = len(A)
    left = 0
    right = n-1

    while left < right:
        mid = (left+right)/2
        if A[mid] < A[mid+1]:
            left = mid + 1
        else:
            right = mid
    return right
# vim: set noexpandtab ts=4 sts=4 sw=4 :
