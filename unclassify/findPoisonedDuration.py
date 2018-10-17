#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-28 17:46:31
# File Name: findPoisonedDuration.py
# Description: 
#########################################################################
def findPoisonedDuration(timeSeries, duration):
    if len(timeSeries) == 0:
        return 0
    ans = 0
    n = len(timeSeries)

    for i in range(1, n):
        diff = timeSeries[i] - timeSeries[i-1]
        if diff < duration:
            ans += diff
        else:
            ans += duration
    return ans + duration

timeSeries = [1,2,3,4,5,6,7,8,9]
duration = 1
print findPoisonedDuration(timeSeries, duration)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
