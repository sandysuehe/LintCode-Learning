#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-17 16:27:29
# File Name: cloneGraph.py
# Description: 克隆图
# LintCode: https://www.lintcode.com/problem/clone-graph/
#########################################################################
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def cloneGraph(self, node):
        hash_set = {}
        return self.clone(node, hash_set)

    def clone(self, hash_set):
        if not node:
            return node
        if node.label in hash_set:
            return hash_set[node.label]

        newNode = UndirectedGraphNode(node.label)
        hash_set[node.label] = newNode

        for i in range(0, len(node.neighbors)):
            newNode.neighbors.append(self.clone(node.neighbors[i], hash_set))

        return newNode
# vim: set noexpandtab ts=4 sts=4 sw=4 :
