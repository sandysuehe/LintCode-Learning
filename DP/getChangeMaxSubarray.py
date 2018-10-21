#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-15 16:55:53
# File Name: getChangeMaxSubarray.py
# Description: 可交换的最大子数组
# LintCode: https://www.lintcode.com/problem/maximum-can-exchanged-subarray/
#########################################################################
def getAnswer(a):
    if len(a) == 0:
        return 0
    
    n = len(a)
    prev_maxsum = [0 for i in range(n)]
    back_maxsum = [0 for i in range(n)]

    cur_max = a[0]
    prev_maxsum[0] = a[0]
    
    # prev_maxsum[i-1]表示i前某一元素交换到i上是i前的元素可达到最大值
    for i in range(1, n):
        cur_max = max(cur_max, a[i])
        prev_maxsum[i] = max(cur_max, prev_maxsum[i-1] + a[i])
            
    back_maxsum[n-1] = a[n-1]
    result = a[n-1]

    # back_maxsum[i]表示从i到len-1的元素所能达到的最大值
    for i in range(n-2, -1, -1): 
        back_maxsum[i] = max(back_maxsum[i+1], 0) + a[i]
        result = max(back_maxsum[i], result)

    for i in range(1, n):
        result = max(back_maxsum[i] - a[i] + prev_maxsum[i-1], result)   

    return result 

#nums = [-3,1,2,3,-10,1]
#print getAnswer(nums)
nums = [1,1,-100,1,1,-100,-100,-100,1,2,-100]
print getAnswer(nums)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
