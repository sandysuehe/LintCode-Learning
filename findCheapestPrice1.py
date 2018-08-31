#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (hexue@4paradigm.com)
#########################################################################
# Created Time: 2018-08-08 18:48:52
# File Name: findCheapestPrice.py
# Description: 
#########################################################################
class Solution(object):
    def dfs(self, start_city, dest, K, edges, temp_price):
        if start_city == dest:
            self.result = temp_price
            return
        if K < 0:
            return
        for city_info in edges[start_city]:
            end_city = city_info[0]
            price = city_info[1]
            if temp_price + price < self.result: #or not visited[end_city]:
                self.dfs(end_city, dest, K-1, edges, temp_price + price)
        return

    def findCheapestPrice(self, n, flights, src, dest, K):
        self.result = float('inf') 
        edges = {}

        for flight in flights:

            start_city = flight[0]
            end_city = flight[1]
            cost = flight[2]

            if start_city not in edges:
                edges[start_city] = [(end_city, cost)]
            else:
                edges[start_city].append((end_city, cost))

        self.dfs(src, dest, K, edges, 0)
        return self.result if self.result != float('inf') else -1

n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
obj = Solution()
print obj.findCheapestPrice(n, edges, src, dst, k)
#vim: set noexpandtab ts=4 sts=4 sw=4 :
