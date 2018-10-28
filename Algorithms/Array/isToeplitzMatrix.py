#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-28 11:38:28
# File Name: isToeplitzMatrix.py
# Description: Toeplitz Matrix 托普利兹矩阵
# LintCode: https://www.lintcode.com/problem/toeplitz-matrix/ 
#########################################################################
def isToeplitzMatrix(matrix):
    m = len(matrix)
    n = len(matrix[0])

    for delta in range(1-m, n):
        temp = set()
        for i in range(0, m):
            j = i + delta
            if j >= 0 and j < n:
                temp.add(matrix[i][j])
        if len(temp) > 1:
            return False

    return True

matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
matrix = [[1,2],[2,2]]
print isToeplitzMatrix(matrix)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
