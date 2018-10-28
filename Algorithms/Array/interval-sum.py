#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-25 14:36:18
# File Name: interval-sum.py
# Description: 区间求和 I
# LintCode: https://www.lintcode.com/problem/interval-sum/
#########################################################################
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def intervalSum(self, A, queries):
        # write your code here
        result = []
        n = len(A)

        if not A or n == 0:
            return result

        sums = [0] * n
        sums[0] = A[0]

        for i in range(1,n):
            sums[i] = sums[i-1] + A[i]

        for interval in queries:
            start = interval.start
            end = interval.end
            result.append(sums[end]-sums[start]+A[start])

        return result
# vim: set noexpandtab ts=4 sts=4 sw=4 :
