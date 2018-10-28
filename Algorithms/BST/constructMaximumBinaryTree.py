#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-16 15:14:38
# File Name: constructMaximumBinaryTree.py
# Description: Maximum Binary Tree 最大二叉树 
# LintCode: https://www.lintcode.com/problem/maximum-binary-tree/
#########################################################################
def constructMaximumBinaryTree(nums):
    if len(nums) == 0 or not nums:
        return None

    return dfs(nums, 0, len(nums)-1)

def dfs(nums, left, right):
    if left > right:
        return None

    mid = left
    # 找到当前nums[left+1, right]中最大的元素
    for i in range(left+1, right+1):
        if nums[i] > nums[mid]:
            mid = i

    node = TreeNode(nums[mid])
    node.left = dfs(nums, left, mid-1)
    node.right = dfs(nums, mid+1, right)
    return node
# vim: set noexpandtab ts=4 sts=4 sw=4 :
