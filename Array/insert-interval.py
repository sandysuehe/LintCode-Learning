#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-28 16:51:20
# File Name: insert-interval.py
# Description: Insert Interval 插入区间 
# LintCode: https://www.lintcode.com/problem/insert-interval/
#########################################################################
class Interval(object):
 def __init__(self, start, end):
     self.start = start
     self.end = end

class Solution:
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
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
inter = Interval(1, 2)
intervals.append(inter)
inter = Interval(5, 9)
intervals.append(inter)

newInterval = Interval(3, 4)

obj = Solution()
print obj.insert(intervals, newInterval)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
