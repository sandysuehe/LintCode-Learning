#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-27 17:39:35
# File Name: getRow.py
# Description: 
#########################################################################
def getRow(n):
    res = []
    n = n + 1
    for i in range(n):
        row = [1 for _ in range(i+1)]
        if i > 1:
            pre_row = res[-1]
            for j in range(1, len(row)-1):
                row[j] = pre_row[j-1] + pre_row[j]
        res.append(row)
    return res[-1]

print getRow(3)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
