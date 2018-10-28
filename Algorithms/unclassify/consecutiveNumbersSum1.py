#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-14 11:29:53
# File Name: consecutiveNumbersSum.py
# Description: 
#########################################################################
def consecutiveNumbersSum(N):
    res = 1
    n = 2
    while 1:
        divisor = N - (n-1)*n/2
        # 因为a至少为1，所以一旦小于就可以直接返回结果
        if divisor < n: return res
        res += divisor%n==0
        n += 1
print "result::::::"
print consecutiveNumbersSum(43156417)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
