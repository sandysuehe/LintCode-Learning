#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-26 15:48:27
# File Name: binary-tree-preorder-traversal.py
# Description: Binary Tree Preorder Traversal 二叉树的先序遍历 
# LintCode: https://www.lintcode.com/problem/binary-tree-preorder-traversal/
#########################################################################
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def preorderTraversal(self, root):
        # write your code here
        self.ans = []
        self.traverse(root)
        return self.ans

    def traverse(self, node):
        if not node:
            return

        self.ans.append(node.val)
        self.traverse(node.left)
        self.traverse(node.right)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
