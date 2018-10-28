#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-22 16:09:54
# File Name: dungeon-game.py
# Description: Dungeon Game 地牢游戏 
# LintCode: https://www.lintcode.com/problem/dungeon-game/
#########################################################################
# 思路: 动态规划+逆向推理
# 建立一个二维数组dp，其中dp[i][j]用来表示当前位置 (i, j) 出发的起始血量，
# 最先处理的是公主所在的房间的起始生命值，然后慢慢向第一个房间扩散，不断的得到各个位置的最优的生命值
#########################################################################
def calculateMinimumHP(dungeon):
    m = len(dungeon)
    n = len(dungeon[0])

    dp = [[float("inf") for i in range(n+1)] for j in range(m+1)] 
    dp[m][n-1] = 1
    dp[m-1][n] = 1

    # Rule: dp[i+1][j] + dp[i][j] >= 1 && dp[i][j+1] + dp[i][j] >= 1
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
    return dp[0][0]

dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
print calculateMinimumHP(dungeon)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
