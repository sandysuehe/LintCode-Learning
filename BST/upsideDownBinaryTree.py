#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-22 13:11:51
# File Name: upsideDownBinaryTree.py
# Description: Binary Tree Upside Down 二叉树的上下颠倒 
# LintCode: https://www.lintcode.com/problem/binary-tree-upside-down/ 
#########################################################################
# 思路: 递归
#########################################################################
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def upsideDownBinaryTree(self, root):
        # write your code here
        if not root or not root.left:
            return root

        new_root = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.right = None
        root.left = None
        return new_root
