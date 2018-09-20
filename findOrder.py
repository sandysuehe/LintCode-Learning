#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-16 15:55:52
# File Name: findOrder.py
# Description: 
#########################################################################
def findOrder(n, prerequisites):

    graph = {}
    inDegree = {}

    # 建立图
    build(graph, inDegree, n, prerequisites)
    print graph
    print inDegree

    # 使用BFS进行拓扑排序
    return topoSort(graph, inDegree)

def build(graph, inDegree, n, prerequisites):

    # 初始化graph和inDegree
    for i in range(0, n):
        graph[i] = []
        inDegree[i] = 0

    # 遍历prerequisites, 给graph和inDegree赋值
    for interval in prerequisites:
        pre_course = interval[1]
        post_course = interval[0]
        graph[pre_course].append(post_course)
        inDegree[post_course] += 1

def topoSort(graph, inDegree):
    res = []

    import Queue
    queue = Queue.Queue()
    
    for i in range(0, n):
        if inDegree[i] == 0:
            queue.put(i)

    while not queue.empty():
        course = queue.get()
        res.append(course)
        
        for p_course in graph[course]:
            inDegree[p_course] -= 1
            if inDegree[p_course] == 0:
                queue.put(p_course)
    if len(res) != n:
        return []
    return res

n = 4
prerequisites =[[1,0],[2,0],[3,1],[3,2]]
print findOrder(n, prerequisites)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
