#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-06 16:54:28
# File Name:  k-closest-points.py
# Description: K个最近的点
# LintCode: https://www.lintcode.com/problem/k-closest-points/
#########################################################################
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    def kClosest(self, points, origin, k):
        if not points:
            return

        import heapq 
        heap = []
        for point in points:
            distance = self.getDistance(origin, point)
            heapq.heappush(heap, (-distance, point))

            if len(heap) > k:
                heapq.heappop(heap)

        heap = sorted(heap, key=lambda item: (-item[0], item[1].x, item[1].y))
        return [p for d, p in heap]

    def getDistance(self, a_point, b_point):
        if not a_point or not b_point:
            return float("inf")

        x = a_point.x - b_point.x
        y = a_point.y - b_point.y

        return x**2 + y**2

points = [Point(4,6), Point(4,7), Point(4,4), Point(2,5), Point(1,1)]
origin = Point(0, 0)
k = 3
obj = Solution()
print obj.kClosest(points, origin, k)
