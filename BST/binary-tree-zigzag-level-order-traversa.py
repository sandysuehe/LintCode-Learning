#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-18 15:09:26
# File Name: binary-tree-zigzag-level-order-traversa.py
# Description: 
# LintCode: https://www.lintcode.com/problem/binary-tree-zigzag-level-order-traversal/
#########################################################################
# 思路:
# 这道二叉树的之字形层序遍历是之前那道[LeetCode] Binary Tree Level Order Traversal 二叉树层序遍历的变形，不同之处在于一行是从左到右遍历，下一行是从右往左遍历，交叉往返的之字形的层序遍历。根据其特点我们用到栈的后进先出的特点，这道题我们维护两个栈，相邻两行分别存到两个栈中，进栈的顺序也不相同，一个栈是先进左子结点然后右子节点，另一个栈是先进右子节点然后左子结点，这样出栈的顺序就是我们想要的之字形了
#########################################################################
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        if not root:
            return []

        ans = []

        import Queue
        queue = Queue.Queue()
        queue.put(root)
        level = 1

        while not queue.empty():
            visited = []
            for _ in range(queue.qsize()):
                node = queue.get()
                visited.append(node.val)
                if node.left:
                    queue.put(node.left)
                if node.right:
                    queue.put(node.right)
            if level % 2 == 0:
                ans.append(visited[::-1])
            else:
                ans.append(visited)
            level += 1
        return ans
# vim: set noexpandtab ts=4 sts=4 sw=4 :
