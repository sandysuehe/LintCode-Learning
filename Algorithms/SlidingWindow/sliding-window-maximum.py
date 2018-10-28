#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-25 17:24:24
# File Name: sliding-window-maximum.py
# Description: Sliding window maximum
# LintCode: https://www.lintcode.com/problem/sliding-window-maximum/
#########################################################################
def maxSlidingWindow(nums, k):
    ans = []
    n = len(nums)

    from collections import deque
    queue = deque()

    for i in range(n):
        # 队列的首元素是i - k的话，表示此时窗口向右移了一步，则移除队首元素。
        if len(queue) > 0 and queue[0] == i-k:
            queue.popleft()

        # 比较队尾元素和将要进来的值，如果小的话就都移除，然后此时我们把队首元素加入结果中即可
        while len(queue) > 0 and nums[queue[-1]] < nums[i]:
            queue.pop()

        queue.append(i)

        if i >= k-1: 
            ans.append(nums[queue[0]])

    return ans

nums = [1,2,7,7,8]
k = 3
print maxSlidingWindow(nums, k)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
