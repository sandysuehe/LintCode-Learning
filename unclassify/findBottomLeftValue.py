#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-16 14:14:17
# File Name: findBottomLeftValue.py
# Description: 
#########################################################################
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def findBottomLeftValue(self, root):
        # write your code here
        if not root:
            return None

        return self.dfs(root, 1, [0, 0])

    def dfs(self, node, depth, res):
        if res[1] < depth:
            res[0] = node.val
            res[1] = depth

        if node.left:
            self.dfs(root.left, depth+1, res)
        if node.right:
            self.dfs(root.right, depth+1, res)
        return res[0] 

# vim: set noexpandtab ts=4 sts=4 sw=4 :
