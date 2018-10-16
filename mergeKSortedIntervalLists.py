#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-07 14:36:17
# File Name: mergeKSortedIntervalLists.py
# Description: 
#########################################################################
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class IntervalNode(object):
    def __init__(self, interval, item, index):
        self.interval = interval
        self.item = item
        self.index = index

    def cmp_start(self, other):
        return self.interval.start - other.interval.start

class Solution:
    def mergeKSortedIntervalLists(self, intervals):
        from heapq import heappop, heappush, heapify
        heap = []
        ans = [Interval(0, 0)]

        for interval_item in intervals:
            if not interval_item:
                continue
            first_interval = interval_item[0]
            heappush(heap, IntervalNode(first_interval, interval_item, 0))
        for item in heap:
            print item.first_interval.start, item.first_interval.end, len(item.interval_item)

        while heap:
            next_interval = heappop(heap)
            interval = next_interval.interval
            last = ans[-1]

            if interval.start <= last.end:
                ans[-1] = Interval(last.start, max(last.end, interval.end))
            else:
                ans.append(interval)

            if next_interval.index + 1 >= len(next_interval.item):
                push_interval = next_interval.item[next_interval.index + 1]
                heappush(heap, IntervalNode(push_interval, next_interval.item, next_interval.index + 1))


obj = Solution()
interval1 = []
interval1.append(Interval(1,3))
interval1.append(Interval(4,7))
interval1.append(Interval(6,8))

interval2 = []
interval2.append(Interval(1,2))
interval2.append(Interval(9,10))

intervals = []
intervals.append(interval1)
intervals.append(interval2)

obj.mergeKSortedIntervalLists(intervals)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
