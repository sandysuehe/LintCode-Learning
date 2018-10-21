#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-22 13:11:51
# File Name: findLeaves.py
# Description: Find Leaves of Binary Tree 找二叉树的叶节点 
# LintCode: https://www.lintcode.com/problem/find-leaves-of-binary-tree/
#########################################################################
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def findLeaves(self, root):
        # write your code here
        self.results = []
        self.dfs(root)
        retturn self.results
        
    def dfs(self, root):
        if not root:
            return 0

        level = max(self.dfs(root.left), self.dfs(root.right)) + 1

        size = len(self.results)
        if level > size:
            self.results.append([])

        self.results[level-1].append(root.val)

        print level, root.val, self.results[level-1]

        return level
