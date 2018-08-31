#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (hexue@4paradigm.com)
#########################################################################
# Created Time: 2018-08-28 16:51:20
# File Name: merge.py
# Description: 
#########################################################################
class Interval(object):
 def __init__(self, start, end):
     self.start = start
     self.end = end

class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x:x.start)
        ans = []
        for interval in intervals:
            if len(ans) == 0 or ans[-1].end < interval.start:
                ans.append(interval)
            else:
                ans[-1].end = max(ans[-1].end, interval.end)
        for item in ans:
            print item.start, item.end
        return ans

intervals = []
inter = Interval(2, 3)
intervals.append(inter)
inter = Interval(4, 5)
intervals.append(inter)
inter = Interval(6, 7)
intervals.append(inter)
inter = Interval(1, 10)
intervals.append(inter)

obj = Solution()
print obj.merge(intervals)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
