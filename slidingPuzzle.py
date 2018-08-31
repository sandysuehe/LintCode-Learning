#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (hexue@4paradigm.com)
#########################################################################
# Created Time: 2018-08-14 14:05:08
# File Name: slidingPuzzle.py
# Description: 
#########################################################################
def slidingPuzzle(board):
    import Queue
    res = 0
    m = len(board)
    n = len(board[0])
    target = "123450"
    start = ""
    dirs = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2,4]]

    # 把board化为一维字符串
    for i in range(0, m):
        for j in range(0, n):
            start += str(board[i][j])
    print start
    visited = []
    visited.append(start)

    queue = Queue.Queue() 
    queue.put(start)

    while not queue.empty():
        #for i in range(queue.qsize()-1, -1, -1):
        cur = queue.get()
        if cur == target:
            print cur
            return res
        zero_index = cur.find("0")
        for direct in dirs[zero_index]:
            cand = list(cur)
            cand[zero_index],cand[direct] = cand[direct],cand[zero_index]
            cand = ''.join(cand)
            if cand not in visited:
                visited.append(cand)
                queue.put(cand)
        res += 1

    return -1 

board = [[1,2,3],[4,0,5]]
board = [[1,2,3],[5,4,0]]
board = [[4,1,2],[5,0,3]]
board = [[3,2,4],[1,5,0]]
print slidingPuzzle(board)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
