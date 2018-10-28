#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-18 13:51:29
# File Name: construct-binary-tree-from-inorder-and-postorder-traversal.py
# LintCode: https://www.lintcode.com/problem/construct-binary-tree-from-inorder-and-postorder-traversal
# Description: Construct Binary Tree from Inorder and Postorder Traversal 
#########################################################################
# 思路:
# 由于后序的顺序的最后一个肯定是根，所以原二叉树的根节点可以知道，题目中给了一个很关键的条件就是树中没有相同元素，有了这个条件我们就可以在中序遍历中也定位出根节点的位置，并以根节点的位置将中序遍历拆分为左右两个部分，分别对其递归调用原函数。
#########################################################################
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param inorder: A list of integers that inorder traversal of a tree
    @param postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """
    def buildTree(self, inorder, postorder):
        # write your code here
        inorder_len = len(inorder)
        postorder_len = len(postorder)
        return self.build(inorder, 0, inorder_len-1, postorder, 0, postorder_len-1)

    def build(self, inorder, inorder_left, inorder_right, postorder, postorder_left, postorder_right):
        if inorder_left > inorder_right or postorder_left > postorder_right:
            return None
        # 后序遍历的最后一个元素是根节点
        cur = TreeNode(postorder[postorder_right])
        # 根据根节点，中序遍历，确定根节点的左子树和右子树
        for i in range(inorder_left, len(inorder)):
            if inorder[i] == cur.val:
                break
        # (i-inorder_left)是inorder根节点位置和左边起始点的距离
        cur.left = self.build(inorder, inorder_left, i-1, postorder, postorder_left, postorder_left+(i-inorder_left)-1)
        cur.right = self.build(inorder, i+1, inorder_right, postorder, postorder_left+(i-inorder_left), postorder_right-1)
        return cur
# vim: set noexpandtab ts=4 sts=4 sw=4 :
