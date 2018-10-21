#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-22 13:11:51
# File Name: hammingWeight.py
# Description: Number of 1 Bits 位1的个数 
# LintCode: https://www.lintcode.com/problem/number-of-1-bits/
#########################################################################
def hammingWeight(n):
    res = 0
    if n <= 0:
        return res
    while n:
        count = n % 2
        n = n / 2
        res += count
    return res

n = 11
print hammingWeight(n)
