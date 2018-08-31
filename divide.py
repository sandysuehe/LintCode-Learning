#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (hexue@4paradigm.com)
#########################################################################
# Created Time: 2018-08-28 16:01:15
# File Name: divide.py
# Description: 
#########################################################################
def divide(dividend, divisor):
    ans = 0
    m = abs(dividend)
    n = abs(divisor)
    if m < n:
        return 0
    temp = n
    p = 1
    while m > (temp << 1):
        temp <<= 1
        p <<= 1
    ans += p + divide(m-temp, n) 
    if (dividend < 0) ^ (divisor < 0):
        ans = -ans
    return ans

dividend = 100
divisor = 9
print divide(dividend, divisor)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
