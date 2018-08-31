#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (hexue@4paradigm.com)
#########################################################################
# Created Time: 2018-08-09 16:14:11
# File Name: maxVacationDays.py
# Description: 
#########################################################################
def maxVacationDays(flights, days):
    city_nums = len(flights)
    week_nums = len(days[0])
    dp = [float('-inf')] * city_nums
    dp[0] = 0
    from copy import deepcopy

    for j in range(0, week_nums):
        #temp = [float('-inf')] * city_nums
        temp = deepcopy(dp)
        for i in range(0, city_nums):
            for p in range(0, city_nums):
                if flights[p][i] == 1 or i == p:
                    temp[i] = max(temp[i], dp[p] + days[i][j])
        print temp, dp
        dp = temp
    return max(dp)


#flights = [[0,0,0],[0,0,0],[0,0,0]]
#days = [[1,1,1],[7,7,7],[7,7,7]]
#flights = [[0,1,1],[1,0,1],[1,1,0]]
#days = [[1,3,1],[6,0,3],[3,3,3]]
# flights = [[0,1,1],[1,0,1],[1,1,0]]
# days = [[7,0,0],[0,7,0],[0,0,7]]
# flights = [[0,1,0],[0,0,0],[0,0,0]]
# days = [[0,0,7],[2,7,7],[7,7,7]]
flights = [[0,1,1],[1,0,1],[1,1,0]]
days = [[1,3,1],[6,0,3],[3,3,3]]
print maxVacationDays(flights, days)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
