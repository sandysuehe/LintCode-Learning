#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# LintCode: https://www.lintcode.com/problem/missing-number
# Subject:  Missing Number 丢失的数字
#########################################################################
# 思路：
# 用等差数列的求和公式求出0到n之间所有的数字之和
# 然后再遍历数组算出给定数字的累积和，然后做减法，差值就是丢失的那个数字 
#########################################################################
def findMissing(nums):
    sumval = 0
    n = len(nums)

    for i in nums:
        sumval += i

    return n*(n+1)/2 - sumval

nums = [0, 1, 3]
print findMissing(nums)
