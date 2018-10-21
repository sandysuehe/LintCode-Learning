#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-29 17:40:53
# File Name: myCalendar.py
# Description: 我的日程安排表 I
# LintCode: https://www.lintcode.com/problem/my-calendar-i/
#########################################################################
class MyCalendar(object):

    def __init__(self):
        self.intervals = []

    def book(self, start, end):

        for interval in self.intervals:
            if start >= interval[0] and start < interval[1]:
                return False
            elif start <= interval[0] and end > interval[1]:
                return False
        self.intervals.append([start, end])
        return True


obj = MyCalendar()
print obj.book(10, 20)
print obj.book(15, 25)
print obj.book(20, 30)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
