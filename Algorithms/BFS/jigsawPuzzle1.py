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
    # 使用最普通的BFS遍历方式，检查上下左右四个方向
    import Queue
    queue = Queue.Queue()
    visited = []

    m = len(board)
    n = len(board[0])
    target = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    dirs = [[0, -1], [-1, 0], [0, 1], [1, 0]]

    # 寻找board中元素0的位置，将其put到queue中
    for i in range(0, m):
        for j in range(0, n):
            if board[i][j] == 0:
                queue.put((board, (i, j)))

    while not queue.empty():
        for i in range(queue.qsize()-1, -1, -1):
            cur = queue.get()
            cur_board = cur[0]
            zero_index = cur[1]

            if cur_board == target:
                return "YES"

            visited.append(cur_board)

            for direct in dirs:
                x = zero_index[0] + direct[0]
                y = zero_index[1] + direct[1]

                from copy import deepcopy
                cand = deepcopy(cur_board)
                if x >= 0 and x < m and y >= 0 and y < n:
                    cand[zero_index[0]][zero_index[1]], cand[x][y] = cand[x][y], cand[zero_index[0]][zero_index[1]]
                    if cand not in visited:
                        visited.append(cand)
                        queue.put((cand, (x, y)))
    return "NO" 

board = [[1,2,3],[4,0,6],[7,5,8]]
board = [[1,2,3],[4,5,6],[7,0,8]]
board = [[4,0,2],[5,3,8],[6,1,7]]
print jigsawPuzzle(board)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
