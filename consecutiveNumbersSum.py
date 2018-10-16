#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-14 11:29:53
# File Name: consecutiveNumbersSum.py
# Description: 
#########################################################################
def consecutiveNumbersSum(num):
    result = 0
    for i in range(0, num):
        if i*(i+1)/2 > num:
            break
        temp = num - i*(i+1)/2
        if temp % (i+1) == 0:
            if temp / (i+1) > 0:
                print temp / (i+1), i
                result += 1
    return result
print "result::::::"
print consecutiveNumbersSum(43156417)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
