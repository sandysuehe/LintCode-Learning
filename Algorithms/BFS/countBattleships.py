#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-16 18:33:47
# File Name: countBattleships.py
# Description: https://www.lintcode.com/problem/battleships-in-a-board 
#########################################################################
import Queue

def countBattleships(board):
    if len(board) == 0 or len(board[0]) == 0:
        return 0

    res = 0
    m = len(board)
    n = len(board[0])
    visited = [[False for i in range(n)] for j in range(m)]
    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    for i in range(m):
        for j in range(n):
            if board[i][j] == 'X' and visited[i][j] == False:
                res += 1
                queue = Queue.Queue()
                queue.put((i, j))

                while not queue.empty():
                    x, y = queue.get()
                    visited[x][y] = True

                    for dx, dy in directions:
                        new_x = x + dx
                        new_y = y + dy
                        if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and not visited[new_x][new_y] and board[new_x][new_y] == "X":
                            queue.put((new_x, new_y))

    return res

board = ["X..X","...X","...X"]
print countBattleships(board)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
