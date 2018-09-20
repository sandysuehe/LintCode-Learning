#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-09 19:49:44
# File Name: orderOfLargestPlusSign.py
# Description: 
#########################################################################
def orderOfLargestPlusSign(N, mines):
    res = 0
    dp = [[float("inf")]*N for i in range(N)]
    for mine in mines:
        dp[mine[0]][mine[1]] = 0
    for i in range(0, N):
        left = 0
        right = 0
        upper = 0
        down = 0
        for j,k in zip(range(0, N, 1), range(N-1, -1, -1)):

            left = left + 1 if dp[i][j] > 0 else 0
            dp[i][j] = min(dp[i][j], left)

            upper = upper + 1 if dp[j][i] > 0 else 0
            dp[j][i] = min(dp[j][i], upper)

            right = right + 1 if dp[i][k] > 0 else 0
            dp[i][k] = min(dp[i][k], right)

            down = down + 1 if dp[k][i] > 0 else 0
            dp[k][i] = min(dp[k][i], down)
    for i in range(0, N):
        for j in range(0, N):
            res = max(res, dp[i][j])
    return res

N = 5
mines = [[4, 2]]
print orderOfLargestPlusSign(N, mines)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
