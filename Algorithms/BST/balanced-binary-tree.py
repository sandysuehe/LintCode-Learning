#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-26 17:46:59
# File Name: balanced-binary-tree.py
# Description: 平衡二叉树 Balanced Binary Tree 
# LintCode: https://www.lintcode.com/problem/balanced-binary-tree/
# 思路:
# 一棵高度平衡的二叉树的定义是：一棵二叉树中每个节点的两个子树的深度相差不会超过1。 
#########################################################################
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def isBalanced(self, root):
        # write your code here
        balance, index = self.validate(root)
        return balance

    def validate(self, root):
        if not root:
            return True, 0

        balance, left_height = self.validate(root.left)
        if not balance:
            return False, 0

        balance, right_height = self.validate(root.right)
        if not balance:
            return False, 0

        return abs(left_height - right_height) <= 1, max(left_height, right_height) + 1
# vim: set noexpandtab ts=4 sts=4 sw=4 :
