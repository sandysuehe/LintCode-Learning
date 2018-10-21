#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-08 18:48:52
# File Name: findCheapestPrice.py
# Description: Cheapest Flights Within K Stops K次转机内的最便宜的航班 
# LintCode: https://www.lintcode.com/problem/cheapest-flights-within-k-stops/
#########################################################################
from copy import deepcopy

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):

        dp = [float('inf')]*n
        dp[src] = 0

        for i in range(0, K+1):
            temp = deepcopy(dp)
            for flight in flights:
                start_city = flight[0]
                end_city = flight[1]
                price = flight[2]

                temp[end_city] = min(temp[end_city], dp[start_city]+price)
            dp = temp

        return dp[dst] if dp[dst] < float('inf') else -1

n = 4
edges = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
src = 0
dst = 3
k = 1
#k = 0
obj = Solution()
print obj.findCheapestPrice(n, edges, src, dst, k)
#vim: set noexpandtab ts=4 sts=4 sw=4 :
