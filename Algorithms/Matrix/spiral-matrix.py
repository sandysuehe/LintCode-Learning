#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# LintCode: https://www.lintcode.com/problem/piral-matrix
# Subject:  Spiral Matrix 螺旋矩阵
#########################################################################
def spiralOrder(matrix):
    if len(matrix) == 0:
        return []

    ans = []
    up = 0
    down = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    direct = 0  #0: go right   1: go down  2: go left  3: go up

    while True:
        if direct == 0:
            for i in range(left, right+1):
                ans.append(matrix[up][i])
            up += 1
        if direct == 1: 
            for i in range(up, down+1):
                ans.append(matrix[i][right])
            right -= 1
        if direct == 2:
            for i in range(right, left-1, -1):
                ans.append(matrix[down][i])
            down -= 1
        if direct == 3:
            for i in range(down, up-1, -1):
                ans.append(matrix[i][left])
            left += 1

        if up > down or left > right:
            return ans
        direct = (direct + 1) % 4

matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print spiralOrder(matrix)
