#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (hexue@4paradigm.com)
#########################################################################
# Created Time: 2018-08-08 11:31:24
# File Name: pourWater.py
# Description: 
#########################################################################
def pourWater(heights, V, K):
    for i in range(0, V):
        left = K
        right = K
        length = len(heights)

        # 找到左边的局部最低点
        while left > 0 and heights[left] >= heights[left-1]:
            left -= 1

        # 回滚操作：找到左边最靠近雨滴下降点的局部最低点
        while left < K and heights[left] == heights[left+1]:
            left += 1

        # 找到右边的局部最低点
        while right < length - 1 and heights[right] >= heights[right + 1]:
            right += 1

        # 回滚操作：找到右边最靠近雨滴下降点的局部最低点
        while right > K and heights[right] == heights[right - 1]:
            right -= 1

        if heights[left] < heights[K]:
            heights[left] += 1
        else:
            heights[right] += 1
    return heights

heights = [2,1,1,2,1,2,2]
V = 4
K = 3
print pourWater(heights, V, K)

heights = [1,2,3,4]
V = 2
K = 2
print pourWater(heights, V, K)

heights = [3, 1, 3]
V = 5
K = 1
print pourWater(heights, V, K)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
