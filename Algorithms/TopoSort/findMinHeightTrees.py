#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-17 14:38:13
# File Name: findMinHeightTrees.py
# Description: Minimum Height Trees 最小高度树 
# LintCode: https://www.lintcode.com/problem/minimum-height-trees/
#########################################################################
def findMinHeightTrees(n, edges):
    if n == 1:
        return [0]

    import Queue
    leaves = Queue.Queue()
    graph = {i:[] for i in range(n)}
    build(graph, leaves, n, edges)
    return topoSort(graph, leaves, n)


def build(graph, leaves, n, edges):
    # 构建graph
    for edge in edges:
        node1 = edge[0]
        node2 = edge[1]
        graph[node1].append(node2)
        graph[node2].append(node1)

    # 找出所有的叶子结点
    for i in range(n):
        if len(graph[i]) == 1:
            leaves.put(i)

def topoSort(graph, leaves, n):
    while n > 2:
        n -= leaves.qsize()
        for i in range(leaves.qsize()): 
            leaf = leaves.get()
            # 叶子结点的parent一定是唯一的,否则就不是叶子结点
            leaf_parent = graph[leaf][0]
            graph[leaf_parent].remove(leaf)

            # 叶子结点的parent也变成了叶子结点, 放入leaves中
            if len(graph[leaf_parent]) == 1:
                leaves.put(leaf_parent)
    res = []
    for i in range(leaves.qsize()):
        res.append(leaves.get())
    return res


# n = 4
# edges = [[1, 0], [1, 2], [1, 3]]
n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
print findMinHeightTrees(n, edges)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
