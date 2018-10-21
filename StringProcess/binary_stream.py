#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-22 13:11:51
# File Name: MapSum.py
# Description: 二进制流
# LintCode: https://www.lintcode.com/problem/binary-stream/
#########################################################################
def getOutput1(s):
    cur = 0
    n = len(s)
    mlist = []
    for i in xrange(n):
        cur = (cur*2 + int(s[i])) % 3
        if cur % 3 == 0:
            mlist.append(i+1)
    return mlist

s = "11011"
#s = "0000"
print getOutput1(s)
