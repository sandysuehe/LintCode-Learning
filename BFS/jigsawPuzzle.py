#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-14 14:05:08
# File Name: slidingPuzzle.py
# Description: Jigsaw Puzzle 拼图游戏 
# Lint: http://www.cnblogs.com/grandyang/p/4794251.html
#########################################################################
def jigsawPuzzle(board):
    import Queue
    m = len(board)
    n = len(board[0])
    target = "123456780"
    start = ""
    dirs = [[1, 3], [0, 2, 4], [1, 5], [0, 4, 6], [1, 3, 5, 7], [2,4,8], [3,7], [4,6,8], [5,7]]

    # 把board化为一维字符串
    for i in range(0, m):
        for j in range(0, n):
            start += str(board[i][j])
    visited = []
    visited.append(start)

    queue = Queue.Queue() 
    queue.put(start)

    while not queue.empty():
        for i in range(queue.qsize()-1, -1, -1):
            cur = queue.get()
            if cur == target:
                return "YES" 
            zero_index = cur.find("0")
            for direct in dirs[zero_index]:
                cand = list(cur)
                cand[zero_index],cand[direct] = cand[direct],cand[zero_index]
                cand = ''.join(cand)
                if cand not in visited:
                    visited.append(cand)
                    queue.put(cand)

    return "NO" 

board = [[1,2,3],[4,0,6],[7,5,8]]
board = [[1,2,3],[4,5,6],[7,0,8]]
print jigsawPuzzle(board)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
