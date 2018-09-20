#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-15 19:30:24
# File Name: alienOrder.py
# Description: 
#########################################################################
def alienOrder(words):

    if not words or len(words) == 0:
        return ""

    graph = {}
    inDegree = {}

    # 建立图
    build(graph, inDegree, words)

    # 使用BFS进行拓扑排序
    return topoSort(graph, inDegree)


def build(graph, inDegree, words):

    # 初始化graph和inDegree
    for word in words:
        for char in list(word):
            graph[char] = []
            inDegree[char] = 0

    # 遍历words集，对上下两行word做对比，给graph和inDegree赋值
    for i in range(0, len(words)-1):
        index = 0
        while index < len(words[i]) and index < len(words[i+1]):
            char1 = words[i][index]
            char2 = words[i+1][index]
            if char1 != char2:
                graph[char1].append(char2)
                inDegree[char2] += 1
                break
            index += 1


def topoSort(graph, inDegree):
    res = ""

    import Queue
    queue = Queue.PriorityQueue()

    for char in inDegree:
        if inDegree[char] == 0:
            queue.put(char)

    while not queue.empty():
        q_char = queue.get() 
        res += q_char
        for edge_node  in graph[q_char]:
            inDegree[edge_node] -= 1
            if inDegree[edge_node] == 0:
                queue.put(edge_node)
    if len(res) != len(graph):
        return ""
    return res



# words = ["zy","zx"]
# words = ["kef", "krt", "kr", "kft", "rftt"]
words = ["wrt","wrf","er","ett","rftt"]
# words = ["ab", "adc"]
print alienOrder(words)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
