#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-18 12:50:47
# File Name: find-peak-element.py
# LintCode: https://www.lintcode.com/problem/find-peak-element
# Description: Find Peak Element 求数组的局部峰值 
#########################################################################
# 思路:
#########################################################################
def findPeak1(A):
    # 此解法会TLE
    # 由于题目中说明了局部峰值一定存在，那么实际上可以从第二个数字开始往后遍历，如果第二个数字比第一个数字小，说明此时第一个数字就是一个局部峰值；否则就往后继续遍历，现在是个递增趋势，如果此时某个数字小于前面那个数字，说明前面数字就是一个局部峰值，返回位置即可。如果循环结束了，说明原数组是个递增数组，返回最后一个位置即可
    for i in range(1, len(A)):
        if A[i] < A[i-1]:
            return i-1
    return len(A)-1


def findPeak(A):
    # 二分法
    # 由于只是需要找到任意一个峰值，那么我们在确定二分查找折半后中间那个元素后，和紧跟的那个元素比较下大小，如果大于，则说明峰值在前面，如果小于则在后面。这样就可以找到一个峰值了
    n = len(A)
    left = 0
    right = n - 1

    while left < right:
        mid = (left + right)/2
        if A[mid] < A[mid+1]:
            left = mid +1
        else:
            right = mid
    return right

A = [1, 2, 1, 3, 4, 5, 7, 6]
print findPeak(A)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
