#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# LintCode: https://www.lintcode.com/problem/jump-game/
# Subject: Jump Game 跳跃游戏 
#########################################################################
# 思路：
# 维护一个变量reach，表示最远能到达的位置，初始化为0.
# 遍历数组中每一个数字，如果当前坐标大于reach或者reach已经抵达最后一个位置则跳出循环，
# 否则就更新reach的值为其和i + nums[i]中的较大值，其中i + nums[i]表示当前位置能到达的最大位置
#########################################################################
def canJump(A):
    n = len(A)
    reach = 0

    for i in range(n):
        if i > reach or reach >= n - 1:
            break
        print "reach: {0}, can: {1}".format(reach, i+A[i])
        reach = max(reach, i+A[i])
    return reach >= n-1

A = [2,3,1,1,4]
print canJump(A)
A = [3,2,1,0,4]
print canJump(A)
