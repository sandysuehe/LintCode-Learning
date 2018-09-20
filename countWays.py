#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-27 19:11:32
# File Name: countWays.py
# Description: 
#########################################################################
def countWays(n):
    res = [1] * (n + 1)

    for i in range(2, len(res)):
        res[i] = res[i-1] + res[i-2]
    return res[-1]

print countWays(4)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
