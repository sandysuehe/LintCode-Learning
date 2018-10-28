#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-22 19:19:20
# File Name: binary-tree-maximum-path-sum-ii.py 
# Description: 二叉树的最大路径和 II Binary Tree Maximum Path Sum II 
# LintCode: https://www.lintcode.com/problem/binary-tree-maximum-path-sum-ii/
#########################################################################
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root of binary tree.
    @return: An integer
    """
    def maxPathSum2(self, root):
        # write your code here
        vals = []
        self.dfs(root, 0, vals)
        return max(vals) 

    def dfs(self, node, length, vals):
        length += node.val
        vals.append(length)

        if node.left:
            self.dfs(node.left, length, vals)
        if node.right:
            self.dfs(node.right, length, vals)

