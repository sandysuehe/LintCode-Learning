#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-07 16:48:48
# File Name: search-a-2d-matrix-ii.py
# Description: 搜索二维矩阵 II Search a 2D Matrix II 
# LintCode: https://www.lintcode.com/problem/search-a-2d-matrix-ii/
#########################################################################
def searchMatrix(matrix, target):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0

    m = len(matrix)
    n = len(matrix[0])
    i = m - 1
    j = 0
    count = 0

    while i >= 0 and j < n:
        if matrix[i][j] == target:
            count += 1
            i -= 1
            j += 1
        elif matrix[i][j] < target:
            j += 1
        elif matrix[i][j] > target: 
            i -= 1

    return count

matrix = [
[1, 3, 5, 7],
[2, 4, 7, 8],
[3, 5, 9, 10]
]
target = 3
print searchMatrix(matrix, target)
