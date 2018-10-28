#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# LintCode: https://www.lintcode.com/problem/validate-binary-search-tree
# Subject: Validate Binary Search Tree 验证二叉查找树
# 思路：中序遍历二叉树
#########################################################################
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        self.last_val = None
        self.ans = True
        self.valid(root)
        return self.ans

    def valid(self, root):
        if not root:
            return
        self.valid(root.left)
        if self.last_val and self.last_val >= root.val:
            self.ans = False
            return
        self.last_val = root.val
        self.valid(root.right)
