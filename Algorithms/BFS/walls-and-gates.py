#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-17 16:27:29
# File Name: walls-and-gates.py
# Description: Walls and Gates
# LintCode: https://www.lintcode.com/problem/walls-and-gates/
#########################################################################
def wallsAndGates(rooms):
    if len(rooms) == 0 or len(rooms[0]) == 0:
        return rooms

    m = len(rooms)
    n = len(rooms[0])

    import Queue
    queue = Queue.Queue()

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for i in range(m):
        for j in range(n):
            if rooms[i][j] == 0:
                queue.put((i, j))

    while not queue.empty():
        x, y = queue.get()

        for dx, dy in directions: 
            new_x = x + dx
            new_y = y + dy

            if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or rooms[new_x][new_y] < rooms[x][y]+1:
                continue
            rooms[new_x][new_y] = rooms[x][y] + 1
            queue.put((new_x, new_y))

    return rooms

rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
print wallsAndGates(rooms)
