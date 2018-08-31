#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (hexue@4paradigm.com)
#########################################################################
# Created Time: 2018-08-10 10:26:07
# File Name: judgeSquareSum.py
# Description: 
#########################################################################
def judgeSquareSum(c):
    sum_set = []
    if c < 0: return False
    import math
    c_sqrt = int(math.sqrt(c))
    for i in range(0, c_sqrt+1):
        sum_set.append(i*i)
        if c - i*i in sum_set:
            return True
    return False

c = 0
print judgeSquareSum(c)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
