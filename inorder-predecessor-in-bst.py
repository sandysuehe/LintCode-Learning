#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-16 19:23:02
# File Name: inorder-predecessor-in-bst.py
# Description:https://www.lintcode.com/problem/inorder-predecessor-in-bst/ 
#########################################################################
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def inorderSuccessor(self, root, p):
        # write your code here
        pre = None

        while root:
            if root.val >= p.val:
                root = root.left
            else:
                pre = root
                root = root.right
        return pre
# vim: set noexpandtab ts=4 sts=4 sw=4 :
