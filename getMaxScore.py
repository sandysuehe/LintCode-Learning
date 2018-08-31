#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (hexue@4paradigm.com)
#########################################################################
# Created Time: 2018-08-08 12:08:49
# File Name: getMaxScore.py
# Description: 
#########################################################################
class Solution(object):
    def dfs(self, x_point, edges, scores, visited, temp_score):
        # 标志结点是否被遍历过
        visited[x_point] = 1
    
        if x_point not in edges:
            self.result = max(self.result, temp_score)
            return
        for y_point in edges[x_point]:
            if not visited[y_point]:
                self.dfs(y_point, edges, scores, visited, temp_score + scores[x_point, y_point])
        return
    
    def getMaxScore(self, x, y, cost, profit):
        self.result = 0
        point_nums = len(profit)
        edges = {}
        scores = {}
    
        #构建字典，存放树的父子关系，结点的得分和花费
        for i in range(0, len(x)):
            if x[i] not in edges:
                edges[x[i]] = [y[i]]
            else:
                edges[x[i]].append(y[i])
            if x[i] == 0:
                scores[x[i], y[i]] = profit[y[i]] + profit[x[i]] - cost[i]
            else:
                scores[x[i], y[i]] = profit[y[i]] - cost[i]

    
        # DFS，得到每个结点得分，得到最大值
        visited = [0]*point_nums
        self.dfs(0, edges, scores, visited, 0)
        return self.result

x = [0,0,0]
y = [1,2,3]
cost = [1,1,1]
profit = [1,1,2,3]
obj = Solution()
print obj.getMaxScore(x, y, cost, profit)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
