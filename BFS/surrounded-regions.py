#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-17 16:27:29
# File Name: surrounded-regions.py
# Description: 被围绕的区域 Surrounded Regions 
# LintCode: https://www.lintcode.com/problem/surrounded-regions/
#########################################################################
def surroundedRegions(board):
    # write your code here
    if len(board) == 0 or len(board[0]) == 0:
        return board

    m = len(board)
    n = len(board[0])

    import Queue
    queue = Queue.Queue()

    for i in range(m):
        for j in range(n):
            print board[i][j]
            if i != 0 and i != m-1 and j != 0 and j != n-1:
                continue
            if board[i][j] != "O":
                continue

            board[i][j] = "W"
            queue.put(i, j)

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while not queue.empty():
                x, y = queue.get()
                for dx, dy in directions: 
                    new_x = x + dx
                    new_y = y + dy

                    if new_x >= 0 and new_x < m and new_y >=0 and new_y < n and board[new_x][new_y] == "O":
                        board[new_x][new_y] = "W"
                        queue.put(new_x, new_y)

    for i in range(m):
        for j in range(n):
            if board[i][j] == "O":
                board[i][j] = "X"
            if board[i][j] == "W":
                board[i][j] = "O"

    return board


board = ["XXXX","XOOX","XXOX","XOXX"]
print surroundedRegions(board)
