#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-08 18:48:52
# File Name: findCheapestPrice.py
# Description: 
#########################################################################
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        dp = [[float('inf')]*n for i in range(K+2)]
        dp[0][src] = 0

        for i in range(1, K+2):
            dp[i][src] = 0
            for flight in flights:
                start_city = flight[0]
                end_city = flight[1]
                price = flight[2]
                dp[i][end_city] = min(dp[i][end_city], dp[i-1][start_city]+price)
        return dp[K+1][dst] if dp[K+1][dst] < float('inf') else -1

n = 10
edges = [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]
src = 6
dst = 0
k = 7
#n = 3
#edges = [[0,1,100],[1,2,100],[0,2,500]]
#src = 0
#dst = 2
#k = 0
obj = Solution()
print obj.findCheapestPrice(n, edges, src, dst, k)
#vim: set noexpandtab ts=4 sts=4 sw=4 :
