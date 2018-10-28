#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-25 11:51:38
# File Name: moving-average-from-data-stream.py
# Description: moving-average-from-data-stream 
# LintCode: https://www.lintcode.com/problem/moving-average-from-data-stream/ 
#########################################################################
class MovingAverage:
    def __init__(self, size):
        # do intialization if necessary
        self.size = size
        self.sum = 0
        import Queue
        self.queue = Queue.Queue()

    def next(self, val):
        # write your code here
        if self.queue.qsize() >= self.size:
            self.sum -= self.queue.get()

        self.queue.put(val)
        self.sum += val
        return float(self.sum)/ float(self.queue.qsize())


obj = MovingAverage(3)
print obj.next(1)
print obj.next(10)
print obj.next(3)
print obj.next(5)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
