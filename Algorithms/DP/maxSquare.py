#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-07 14:17:14
# File Name: maxSquare.py
# Description: Maximal Square 最大正方形 
# LintCode: https://www.lintcode.com/problem/maximal-square/
#########################################################################
def maxSquare(matrix):
    m = len(matrix)
    n = len(matrix[0])
    ans = 0
    
    if m == 0:
        return ans

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] != 0:
                matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]) + 1
                if matrix[i][j] > ans:
                    ans = matrix[i][j]
    if ans == 0:
        ans = 1
    return ans ** 2

a=[[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]]
print maxSquare(a)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
