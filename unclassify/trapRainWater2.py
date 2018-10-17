#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-15 12:47:55
# File Name: trapRainWater2.py
# Description: 
#########################################################################
def trapRainWater(heightMap):
    if len(heightMap) == 0:
        return 0
    m = len(heightMap)
    n = len(heightMap[0])
    res = 0
    max_height = float("-inf")
    
    import Queue
    queue = Queue.PriorityQueue()
    visited = [[False]*n for i in range(m)]

    dirs = [[0, -1], [-1, 0], [0, 1], [1, 0]]

    # 将边界元素放入queue中，并标记已访问放入visited[i][j]=True
    for i in range(0, m):
        for j in range(0, n):
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                visited[i][j] = True
                queue.put((heightMap[i][j], i*n+j))

    # 遍历queue
    while not queue.empty():
        element = queue.get()
        height = element[0]
        row = element[1] / n
        col = element[1] % n
        # 寻找最大高度
        max_height = max(max_height, height)

        for i in range(0, len(dirs)):
            # 遍历该元素的周边元素（上下左右）
            x = row + dirs[i][0]
            y = col + dirs[i][1]
            # BFS搜索的条件：1.不能越界；2.未访问过的元素
            if x >= 0 and x < m and y >= 0 and y < n and visited[x][y] == False:
                visited[x][y] = True
                # 如果获得的周边元素比最大高度低，说明可以蓄水，故用最大高度-周边元素高度
                if heightMap[x][y] < max_height:
                    res += max_height - heightMap[x][y]
                queue.put((heightMap[x][y], x*n+y))
    return res

heightMap = [
  [12,13,0,12],
  [13,4,13,12],
  [13,8,10,12],
  [12,13,12,12],
  [13,13,13,13]
]
heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
print trapRainWater(heightMap)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
