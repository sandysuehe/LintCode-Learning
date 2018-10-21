#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-22 13:11:51
# File Name: flatten-binary-tree-to-linked-list.py
# Description: 将二叉树拆成链表
# LintCode: https://www.lintcode.com/problem/flatten-binary-tree-to-linked-list/ 
#########################################################################
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def flatten(self, root):
        # write your code here
        self.dfs(root)
        
    def dfs(self, root):
        if not root:
            return None

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if left:
            left.right = root.right
            root.right = root.left
            root.left = None

        if right :
            return right
        
        if left:
            return left

        return root
