#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (hexue@4paradigm.com)
#########################################################################
# Created Time: 2018-08-16 16:27:51
# File Name: canFinish.py
# Description: 
#########################################################################
def canFinish(numCourses, prerequisites):
    graph = {i:[] for i in range(numCourses)}
    inDegree = {i:0 for i in range(numCourses)}
    build(graph, inDegree, numCourses, prerequisites)
    return topoSort(graph, inDegree)


def build(graph, inDegree, numCourses, prerequisites):
    for interval in prerequisites:
        pre_course = interval[1]
        post_course = interval[0]
        graph[pre_course].append(post_course)
        inDegree[post_course] += 1

def topoSort(graph, inDegree):
    import Queue
    queue = Queue.Queue()

    for c in inDegree:
        if inDegree[c] == 0:
            queue.put(c)

    while not queue.empty():
        course = queue.get()
        for p_course in graph[course]:
            inDegree[p_course] -= 1
            if inDegree[p_course] == 0:
                queue.put(p_course)

    for i in inDegree:
        if inDegree[i] != 0:
            return False

    return True

numCourses = 4
prerequisites =[[1,0],[2,0],[3,1],[3,2]]
print canFinish(numCourses, prerequisites)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
