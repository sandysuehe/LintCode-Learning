#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-25 15:56:57
# File Name: sliding-window-median.py
# Description: Sliding window median 
# LintCode: https://www.lintcode.com/problem/sliding-window-median/
#########################################################################
# 思路:
# 维护了min_heap和max_heap两个堆，分别保存有序数组的左半段和右半段的数字，
# min_heap存放+较大的数字(4,5,6), max_heap存放-较小的数字(-3,-2,-1)
# 保持min_heap的长度>=max_heap的长度
#########################################################################
def medianSlidingWindow1(nums, k):
    # write your code here
    if not nums or k == 1 or k == 0:
        return nums
        
    import heapq
    max_heap, min_heap = [], []
    res = []
    
    for index, num in enumerate(nums[:k]):
        heapq.heappush(min_heap, (num, index))
    
    for _ in xrange((k+1)/2):
        num, index = heappop(min_heap)
        heapq.heappush(max_heap, (-num, index))
    
    for i,n in enumerate(nums[k:]):
        res.append(-max_heap[0][0])
        if n >= min_heap[0][0]:
            heappush(min_heap, (n,i+k))
            if nums[i] <= min_heap[0][0]:
                m, j = heappop(min_heap)
                heappush(max_heap, (-m, j))
        else:
            heappush(max_heap, (-n, i+k))
            if nums[i] >= min_heap[0][0]:
                m,j = heappop(max_heap)
                heappush(min_heap, (-m, j))
                
        while min_heap and min_heap[0][1] <= i: heappop(min_heap)
        while max_heap and max_heap[0][1] <= i: heappop(max_heap)
    res.append(-max_heap[0][0])
    
    return res

nums = [1,2,7,8,5]
k = 3
nums = [1,2,7,7,2,10,3,4,5]
k = 2
print medianSlidingWindow1(nums, k)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
