#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-22 13:11:51
# File Name: minimum-subtree.py
# Description: 最小子树 
# LintCode: https://www.lintcode.com/problem/minimum-subtree/
#########################################################################
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def findSubtree(self, root):
        # write your code here
        minsum, subtree, sumval = self.dfs(root)
        return subtree 

    def dfs(self, root):
        if not root:
            return float("inf"), None, 0

        left_minsum, left_subtree, left_sumval = self.dfs(root.left)
        right_minsum, right_subtree, right_sumval = self.dfs(root.right)

        sumval = left_sumval + right_sumval + root.val

        minsum = min(left_minsum, right_minsum, sumval)

        if minsum == left_minsum:
            return left_minsum, left_subtree, sumval
        elif minsum == right_minsum:
            return right_minsum, right_subtree, sumval
        else:
            return sumval, root, sumval
