#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-16 19:16:09
# File Name: 2-keys-keyboard.py
# Description: 
#########################################################################
def minSteps(n):
    if n == 1:
        return 0
    res = n
    for i in range(n-1, 1, -1):
        if n % i == 0:
            res = min(res, minSteps(n/i)+i)
    return res

print minSteps(6)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
