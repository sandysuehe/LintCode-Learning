#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-16 14:03:05
# File Name: findMinArrowShots.py
# Description:给定 n 个区间，求其一共有多少个相交的部分 
# 只要我们朝相交区间的任意一点射箭，就能用最少的箭刺破所有的气球。
#########################################################################
def findMinArrowShots(points):
    if not points:
        return 0
    points = sorted(points, key = lambda x:x[1])

    ans = 1
    last_end = points[0][1]
    for i in range(1, len(points)):
        # 与上一个区间不相交, ans+1,然后移动到下一个区间
        if points[i][0] > last_end: 
            ans += 1 
            last_end = points[i][1]
    return ans

points = [[10,16], [2,8], [1,6], [7,12]]
print findMinArrowShots(points)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
