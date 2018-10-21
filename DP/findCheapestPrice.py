#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-08 18:48:52
# File Name: findCheapestPrice.py
# Description: Cheapest Flights Within K Stops K次转机内的最便宜的航班 
# LintCode: https://www.lintcode.com/problem/cheapest-flights-within-k-stops/
#########################################################################
class Solution(object):
    def dfs(self, start_city, dest, K, edges, prices, visited, temp_price):
        visited[start_city] = 1
        if start_city == dest:
            self.result = temp_price
            return
        if K < 0:
            return
        for end_city in edges[start_city]:
            if temp_price + prices[start_city, end_city] < self.result:
                self.dfs(end_city, dest, K-1, edges, prices, visited, temp_price + prices[start_city, end_city])
        return

    def findCheapestPrice(self, n, flights, src, dest, K):
        self.result = float('inf') 
        edges = {}
        prices = {}
        visited = [0] * n

        for flight in flights:

            start_city = flight[0]
            end_city = flight[1]
            cost = flight[2]

            if start_city not in edges:
                edges[start_city] = [end_city]
            else:
                edges[start_city].append(end_city)

            prices[start_city, end_city] = cost
        self.dfs(src, dest, K, edges, prices, visited, 0)
        return self.result if self.result != float('inf') else -1

n = 10
edges = [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]
src = 6
dst = 0
k = 7
obj = Solution()
print obj.findCheapestPrice(n, edges, src, dst, k)
#vim: set noexpandtab ts=4 sts=4 sw=4 :
