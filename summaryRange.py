#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (hexue@4paradigm.com)
#########################################################################
# Created Time: 2018-08-29 15:25:03
# File Name: summaryRange.py
# Description: 
#########################################################################
def summaryRange(intervals):
    n = len(intervals)
    i = 0
    j = 0
    ans = []
    if n == 1:
        return [str(intervals[0])]
    while j < n - 1:
        if intervals[j+1] - intervals[j] == 1:
            j += 1
            if j == n - 1:
                ans.append("{0}->{1}".format(intervals[i], intervals[j]))
        else:
            if i != j:
                ans.append("{0}->{1}".format(intervals[i], intervals[j]))
            else:
                ans.append(intervals[i])
            j += 1
            i = j
            if j == n - 1:
                ans.append(intervals[i])
    return ans

intervals = [0,1,2,4,5,7]
intervals = [0,2,3,4,6,8,9]
print summaryRange(intervals)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
