#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-26 15:54:22
# File Name: binary-tree-inorder-traversal.py
# Description: binary-tree-inorder-traversal 
# LintCode: https://www.lintcode.com/problem/binary-tree-inorder-traversal/
#########################################################################
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        self.ans = []
        self.traverse(root)
        return self.ans

    def traverse(self, node):
        if not node:
            return

        self.traverse(node.left)
        self.ans.append(node.val)
        self.traverse(node.right)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
