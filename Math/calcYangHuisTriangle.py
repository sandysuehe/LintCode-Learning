#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-27 17:05:21
# File Name: calcYangHuisTriangle.py
# Description: 杨辉三角
# LintCode: https://www.lintcode.com/problem/yang-hui-triangle/
#########################################################################
def calcYangHuisTriangle(n):
    res = []
    for i in range(n):
        row = [1 for _ in range(i+1)]
        if i > 1:
            prev_row = res[-1]
            for j in range(1, len(row) - 1):
                row[j] = prev_row[j-1] + prev_row[j]
        res.append(row)
    return res
print calcYangHuisTriangle(4)
# vim: set noexpandtab ts=4 sts=4 sw=4 :
