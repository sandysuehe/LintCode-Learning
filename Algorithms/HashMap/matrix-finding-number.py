#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-16 11:16:30
# File Name: matrix-finding-number.py
# Description: 矩阵找数
# LintCode: https://www.lintcode.com/problem/matrix-finding-number/
#########################################################################
def findingNumber(mat):
    hashSet = [0 for i in range(100000 + 1)]
    n = len(mat)

    for row in mat:
        visited = {}
        for x in row:
            visited[x] = 1
        for key in visited:
            hashSet[key] += 1

    ans = -1
    for i in range(1, 100000 + 1):
        if hashSet[i] == n:
            ans = i
            break
    return ans

mat = [[1,2,3],[3,4,1],[2,1,3]]
#mat =[[1,2,3],[3,4,2],[2,1,8]]
print findingNumber(mat)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
