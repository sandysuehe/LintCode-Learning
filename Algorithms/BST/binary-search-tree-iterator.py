#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-22 19:19:20
# File Name: binary-search-tree-iterator.py
# Description: 二叉查找树迭代器
# LintCode: https://www.lintcode.com/problem/binary-search-tree-iterator/
#########################################################################
# 思路:
# 二叉树的中序遍历的非递归形式，需要额外定义一个栈来辅助;
# 二叉搜索树的建树规则就是左<根<右，用中序遍历即可从小到大取出所有节点
#########################################################################
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

"""
Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    """
    @return: True if there has next node, or false
    """
    def hasNext(self, ):
        # write your code here
        return len(self.stack) != 0

    """
    @return: return next node
    """
    def next(self, ):
        # write your code here
        node = self.stack.pop()
        ans = node
        if node.right:
            node = node.right
            while node:
                self.stack.append(node)
                node = node.left
        return ans 
# vim: set noexpandtab ts=4 sts=4 sw=4 :
