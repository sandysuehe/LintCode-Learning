#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# LintCode: https://www.lintcode.com/problem/rotate-image
# Subject:  Rotate Image 旋转图像 
#########################################################################
# 思路：
# 对原数组取其转置矩阵，然后把每行的数字翻转
#########################################################################
def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
    return matrix

matrix = [[1,2],[3,4]]
print rotate(matrix)
