#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-22 13:11:51
# File Name: inorderSuccessor.py
# Description: Inorder Successor in BST 二叉搜索树中的中序后继节点 
# LintCode: https://www.lintcode.com/problem/inorder-successor-in-bst/
#########################################################################
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root, p):
        # write your code here
        if not root or not p:
            return None
        
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            left = self.inorderSuccessor(root.left, p)
            if left:
                return left
            else:
                return root
