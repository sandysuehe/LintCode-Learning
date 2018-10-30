#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-26 14:37:10
# File Name: word-break-ii.py
# Description: word-break-ii 
# LintCode: https://www.lintcode.com/problem/word-break-ii/
#########################################################################
class Solution:
    def wordBreak(self, s, wordDict):
        return self.dfs(s, wordDict, {})

    def dfs(self, s, wordDict, visited):
        if s in visited:
            return visited[s]

        if len(s) == 0:
            return []

        ans = []

        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix not in wordDict:
                continue

            post_list = self.dfs(s[i:], wordDict, visited)
            for post in post_list:
                ans.append(prefix + " " + post)

        if s in wordDict:
            ans.append(s)

        visited[s] = ans 
        return ans 

s = "lintcode"
wordDict = ["de", "ding", "co", "code", "lint"]
obj = Solution()
print obj.wordBreak(s, wordDict)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
