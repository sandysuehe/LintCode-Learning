#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-18 18:23:00
# File Name: permutations.py
# Description: 
#########################################################################
class Solution:
    def permute(self, nums):
        # write your code here
        if len(nums) == 0:
            return [[]]

        self.ans = []
        nums = sorted(nums)
        visited = [False for i in range(len(nums))]

        self.dfs(nums, [], visited)
        return self.ans
    
    def dfs(self, nums, subset, visited):
        if len(nums) == len(subset):
            self.ans.append(subset[:])
        for i in range(len(nums)):
            if visited[i] == True:
                # 如果该数字已经被访问过
                continue
            visited[i] = True
            subset.append(nums[i])
            self.dfs(nums, subset, visited)
            visited[i] = False
            subset.pop()


nums = [1,2,3] 
obj = Solution()
print obj.permute(nums)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
