#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-16 11:58:32
# File Name: maximum-product-path.py
# Description: 最大乘积路径
# LintCode: https://www.lintcode.com/problem/maximum-product-path/
#########################################################################
class Solution:
    def getProduct(self, x, y, d): 
        n = len(d)
        self.ans = 0
        self.graph = [[] for i in range(n+1)]

        for i in range(len(x)):
            self.graph[x[i]].append(y[i])
            self.graph[y[i]].append(x[i])

        self.dfs(1, -1, d, 1)
        return self.ans

    def dfs(self, cur, pre, weight, multiple):
        isLeaf = True
        mod = 1000000007
        multiple = multiple * weight[cur-1] % mod

        for back in self.graph[cur]:
            if back == pre:
                continue
            isLeaf = False
            self.dfs(back, cur, weight, multiple)

        if isLeaf:
            self.ans = max(self.ans, multiple)


x = [1,2,2]
y = [2,3,4]
d = [1,1,-1,2]
obj = Solution()
print obj.getProduct(x, y, d)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
