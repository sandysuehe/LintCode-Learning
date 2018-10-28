#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-23 15:09:12
# File Name: the-skyline-problem.py
# Description: The Skyline Problem
# LintCode: https://www.lintcode.com/problem/the-skyline-problem/
#########################################################################
# 基本思路:
# 将buildings中的每个线段的左边节点和右边节点保存到height_list, 根据x坐标值排序，遍历求拐点
# 求拐点的方法:
# 1. 用heap来保存当前的楼顶高度
# 2. 遇到左边节点，就在heap中插入高度信息, 这栋楼的index
# 3. 遇到右边节点，就从heap中删除高度信息, 并将这栋楼的index加入removed set 
#########################################################################
def buildingOutline(buildings):
    # write your code here
    if not buildings:
        return []

    building_edges = []  #[(position, height, left/right, index)]
    for index, building in enumerate(buildings):
        start, end, height = building
        building_edges.append((start, height, "L", index))
        building_edges.append((end, height, "R", index))

    building_edges = sorted(building_edges)

    current_buildings = []
    removed_list = set()
    outline = []
    import heapq

    for edge in building_edges:
        position, height, direct, index = edge
        if direct == "L":
            heapq.heappush(current_buildings, (-height, height, index))
        else:
            removed_list.add(index)

        while current_buildings and top_index(current_buildings) in removed_list:
            heapq.heappop(current_buildings)

        if current_buildings:
            tallest = top_height(current_buildings) 
        else:
            tallest = 0

        if not outline:
            outline.append([position, tallest])
        elif outline_latest_position(outline) == position: 
            outline[-1][1] = max(tallest, outline[-1][1])
        elif outline_latest_tallest(outline) != tallest: 
            outline.append([position, tallest])

    ans = []
    for i in range(len(outline)-1):
        if outline[i][1] == 0:
            continue
        ans.append([outline[i][0], outline[i+1][0], outline[i][1]])
    return ans 

def top_index(current_buildings):
    _, height, index = current_buildings[0]
    return index 

def top_height(current_buildings):
    _, height, index = current_buildings[0]
    return height

def outline_latest_position(outline):
    position, tallest = outline[-1]
    return position 

def outline_latest_tallest(outline):
    position, tallest = outline[-1]
    return tallest 


buildings = [
  [1, 3, 3],
  [2, 4, 4],
  [5, 6, 1]
]
print buildingOutline(buildings)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
