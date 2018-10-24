#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-15 15:59:49
# File Name: find-median-from-data-stream.py
# Description: 数据流中位数
# LintCode: https://www.lintcode.com/problem/find-median-from-data-stream/
#########################################################################
def medianII(nums): 
    ans = []
    if len(nums) == 0:
        return ans 

    median = nums[0]
    ans.append(median)

    import Queue
    max_heap = Queue.PriorityQueue()
    min_heap = Queue.PriorityQueue()

    for i in range(1, len(nums)):
        if nums[i] < median:
            max_heap.put(-nums[i]) 
        else:
            min_heap.put(nums[i])

        if max_heap.qsize() > min_heap.qsize(): 
            min_heap.put(median)
            median = -max_heap.get()
        elif max_heap.qsize() + 1 < min_heap.qsize():
            max_heap.put(-median)
            median = min_heap.get()

        ans.append(median)
    return ans 

nums = [1, 2, 3, 4, 5]
print nums
print medianII(nums)
nums = [4, 5, 1, 3, 2, 6, 0]
print nums, medianII(nums)
nums = [2, 20, 100]
print nums, medianII(nums)
nums = [1,0,1]
print nums, medianII(nums)
