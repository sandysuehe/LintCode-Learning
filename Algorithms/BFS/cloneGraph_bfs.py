#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-17 16:27:29
# File Name: cloneGraph.py
# Description: 克隆图 BFS
# LintCode: https://www.lintcode.com/problem/clone-graph/
#########################################################################
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def cloneGraph(self, node):
        if not node:
            return node

        visited = {}
        import Queue
        queue = Queue.Queue()

        newNode = UndirectedGraphNode(node.label)
        visited[node] = newNode
        queue.put(node)

        while not queue.empty():
            curNode = queue.get()
            for neighbor in curNode.neighbors:
                if neighbor not in visited:
                    queue.put(neighbor)
                    newNeighbor = UndirectedGraphNode(neighbor.label)
                    visited[neighbor] = newNeighbor

                visited[curNode].neighbors.append(visited[neighbor])
        return newNode
# vim: set noexpandtab ts=4 sts=4 sw=4 :
