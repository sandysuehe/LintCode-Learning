#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-22 13:11:51
# File Name: MapSum.py
# Description: 数对统计
# LintCode: https://www.lintcode.com/problem/number-pair-statistics/
#########################################################################
# a,b,c,d为point数组中（奇数，偶数）,（奇数，奇数）,
#（偶数，偶数）,（偶数，奇数）四种情况的数量。
#（奇数，偶数）与（奇数，偶数）组合，
#（奇数，奇数）与（奇数，奇数）组合，
#（偶数，偶数）与（偶数，偶数）组合，
#（偶数，奇数）与（偶数，奇数）组合，
# 即答案为ans = (a - 1) * a + (b - 1) * b + (c - 1) * c + (d - 1) * d。
#########################################################################
def pairNumbers(p):
    n = len(p)
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if (p[i][0] + p[j][0]) % 2 == 0 and (p[i][1] + p[j][1]) % 2 == 0:
                count += 1
    return count

#p = [[1,2],[3,4],[5,6]]
p = [[0,3],[1,1],[3,4],[5,6]]
print pairNumbers(p)
