#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-16 10:23:51
# File Name: longest-path-on-the-tree.py
# Description: 
#########################################################################
class Solution:
    def longestPath(self, n, starts, ends, lens):
        self.graph = [[] for i in range(n)]
        self.dp = [0 for i in range(n)]

        # build graph
        for i in range(n-1):
            self.graph[starts[i]].append([ends[i], lens[i]])
            self.graph[ends[i]].append([starts[i], lens[i]])

        # from 0 points, max weight
        self.dfs(0, 0)

        max_weight = max(self.dp)
        pos = self.dp.index(max_weight)

        self.dp[pos] = 0
        self.dfs(pos, pos)

        return max(self.dp)

    def dfs(self, cur, pre):
        for back, weight in self.graph[cur]: 
            if back != pre:
                self.dp[back] = self.dp[cur] + weight
                self.dfs(back, cur)
    

n=5
starts=[0,0,2,2]
ends=[1,2,3,4]
lens=[1,2,5,6]
n=5
starts=[0,0,2,2]
ends=[1,2,3,4]
lens=[5,2,5,6]
obj = Solution()
print obj.longestPath(n, starts, ends, lens)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
