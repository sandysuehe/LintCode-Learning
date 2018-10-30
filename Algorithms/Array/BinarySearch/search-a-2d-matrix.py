#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-26 10:48:10
# File Name: search-a-2d-matrix.py
# Description: Search a 2D Matrix 搜索一个二维矩阵 
# LintCode: https://www.lintcode.com/problem/search-a-2d-matrix/
#########################################################################
def searchMatrix(matrix, target):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False

    m = len(matrix)
    n = len(matrix[0])

    if target < matrix[0][0] or target > matrix[m-1][n-1]:
        return False

    # 通过二分查找发确定行
    left = 0
    right = m - 1
    while left <= right:
        mid = (left+right)/2
        if matrix[mid][0] == target:
            return True
        elif matrix[mid][0] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # 通过二分查找发确定列
    row = right
    left = 0
    right = len(matrix[row]) - 1
    while left <= right:
        mid = (left+right)/2
        if matrix[row][mid] == target:
            return True
        elif matrix[row][mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


matrix = [
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
print searchMatrix(matrix, target)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
