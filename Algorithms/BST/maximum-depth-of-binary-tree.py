#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-26 17:40:25
# File Name: maximum-depth-of-binary-tree.py
# Description: 二叉树的最大深度 Maximum Depth of Binary Tree
# LintCode: https://www.lintcode.com/problem/maximum-depth-of-binary-tree/
#########################################################################
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
# vim: set noexpandtab ts=4 sts=4 sw=4 :
