#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# LintCode: https://www.lintcode.com/problem/set-matrix-zeroes
# Subject:  Set Matrix Zeroes 矩阵归零 
#########################################################################
# 思路：
#- 先扫描第一行第一列，如果有0，则将各自的flag设置为true
#- 然后扫描除去第一行第一列的整个数组，如果有0，则将对应的第一行和第一列的数字赋0
#- 再次遍历除去第一行第一列的整个数组，如果对应的第一行和第一列的数字有一个为0，则将当前值赋0
#- 最后根据第一行第一列的flag来更新第一行第一列
#########################################################################
def setZeroes(matrix):
    if len(matrix) == 0:
        return
    m = len(matrix)
    n = len(matrix[0])
    row_visited = [False for i in range(m)]
    col_visited = [False for i in range(n)]

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row_visited[i] = True
                col_visited[i] = True 
    for i in range(m):
        for j in range(n):
            if row_visited[i] or col_visited[j]:
                matrix[i][j] = 0
    return matrix

matrix = [
  [1, 2],
  [0, 3]
]
print setZeroes(matrix)
