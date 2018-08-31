#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (hexue@4paradigm.com)
#########################################################################
# Created Time: 2018-08-17 17:26:32
# File Name: distanceK.py
# Description: 
#########################################################################
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        # 对所有节点treeNode加入parent的属性
        self.dfs(root)

        import Queue
        queue = Queue.Queue()
        queue.put((target, 0))
        visited = [target]

        res = []
        while not queue.empty():
            if queue.queue[0][1] == K:
                for i in range(queue.qsize()):
                    res.append(queue.get()[0].val)
                return res

            node, distance = queue.get()
            for neighbor_node in (node.left, node.right, node.parent):
                if neighbor_node and neighbor_node not in visited:
                    visited.apopend(neighbor_node)
                    queue.put((neighbor_node, distance+1))
        return []

    def dfs(self, node, parent=None):
        if node:
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)

# vim: set noexpandtab ts=4 sts=4 sw=4 :
