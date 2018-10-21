#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-07 18:36:52
# File Name: sequenceReconstruction.py
# Description: Sequence Reconstruction 序列重建 
# LintCode: https://www.lintcode.com/problem/sequence-reconstruction/
#########################################################################
def sequenceReconstruction(org, seqs):
    if not seqs:
        return False

    n = len(org)
    graph = {i:[] for i in range(1,n+1)}
    inDegree = {}
    build(graph, inDegree, seqs)
    return topoSort(graph, inDegree, n, org)

def build(graph, inDegree, seqs):
    for seq in seqs:
        for i in range(0, len(seq)):
            if i == 0:
                if seq[i] in inDegree:
                    inDegree[seq[i]] += 0
                else:
                    inDegree[seq[i]] = 0
            if i < len(seq)-1:
                if seq[i] in graph:
                    graph[seq[i]].append(seq[i+1])
                if seq[i+1] in inDegree:
                    inDegree[seq[i+1]] += 1
                else:
                    inDegree[seq[i+1]] = 1

def topoSort(graph, inDegree, n, org):
    import Queue
    queue = Queue.Queue()
    res = []

    for i in inDegree:
        if inDegree[i] == 0:
            queue.put(i)

    while queue.qsize() == 1:
        node = queue.get()
        res.append(node)
        if node not in graph:
            return False
        for p_node in graph[node]:
            inDegree[p_node] -= 1
            if inDegree[p_node] == 0:
                queue.put(p_node)
    if queue.qsize() > 1:
        return False
    return len(res) == n and res == org

org = [4,1,5,2,6,3]
seqs = [[5,2,6,3],[4,1,5,2]]
# org = [1]
# seqs = [[],[]]
org = [5,3,2,4,1]
seqs = [[5,3,2,4],[4,1],[1],[3],[2,4],[1,1000000000]]
org = [5,4,8,9,1,6,3,2,7,10]
seqs = [[233665123,2145174067],[783368690,1102520059,2044897763,1967513926,1365180540,1540383426,304089172],[1059961393,2089018456,628175011,1656478042,1131176229],[1101513929,1801979802,1315634022,635723058,1369133069],[],[184803526],[1025202362],[859484421,1914544919,608413784],[1734575198,1973594324,149798315],[35005211,521595368,294702567,1726956429,336465782,861021530]]
org = [1]
seqs = [[1],[1],[1]]
print sequenceReconstruction(org, seqs)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
