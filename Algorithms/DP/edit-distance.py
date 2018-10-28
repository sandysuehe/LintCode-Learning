#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-22 15:56:53
# File Name: minDistance.py
# Description: Edit Distance 编辑距离 
# LintCode: https://www.lintcode.com/problem/edit-distance/ 
#########################################################################
def minDistance(word1, word2):
    n1 = len(word1)
    n2 = len(word2)

    dp = [[float('inf')] * (n2+1) for _ in range(n1+1)]
    print dp

    for i in range(0, n1+1):
        dp[i][0] = i
    for j in range(0, n2+1):
        dp[0][j] = j

    print dp
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

    return dp[n1][n2]

word1="sea"
word2="ate"
#word1="b"
#word2=""
print minDistance(word1, word2)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
