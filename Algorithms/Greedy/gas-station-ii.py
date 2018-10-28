#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-22 12:14:23
# File Name: gas-station-ii.py
# Description: Gas Station II 加油站II 
# LintCode: https://www.lintcode.com/problem/gas-station-ii/
#########################################################################
# 思路: 考虑贪心，每次都用[能到达]并且[能加最多油的]加油站加油。
# 使用优先队列贪心地选择加油量最大的加油站
#########################################################################
def getTimes(target, original, distance, apply):
    import Queue
    queue = Queue.PriorityQueue()
    ans = 0
    pre = 0
    n = len(distance)

    if target > distance[n-1]: 
        distance.append(target)
        apply.append(0)

    capability = original 

    for i in range(n):
        if distance[i] >= target:
            distance[i] = target

        gas_distance = distance[i] - pre # 当前加油站距上个加油站的距离

        while capability < gas_distance and not queue.empty():
            # 当汽车汽油量capability不足以行驶至下一个加油站 && 队列里有汽油可以加 
            new_cap = queue.get()
            capability += new_cap
            ans += 1

        if gas_distance <= capability:  # 如果汽车汽油量capability足以支撑其行驶到下一个汽车加油站
            capability -= gas_distance  # 汽车汽油量capability更新，capability = capability - gas_distance
        else:
            ans = -1                    # 如果汽车汽油量capability不足以支撑其行驶到下一个汽车加油站,退出
            break

        queue.put(apply[i])             # 将当前加油站的所加油量放在到queue里 
        pre = distance[i]               # 更新上一个加油站为：当前加油站

        if pre == target:               # 如果当前加油站距离起点位置等于target，即到达终点，退出
            break

    return ans

target = 25
original = 10
distance = [10,14,20,21]
apply = [10,5,2,4]
print "Result: ", getTimes(target, original, distance, apply)

target = 25
original = 10
distance = [10,14,20,21]
apply = [1,1,1,1]
print "Result: ", getTimes(target, original, distance, apply)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
