#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-22 13:11:51
# File Name: convertToTitle.py
# Description: Excel表列标题
# LintCode: https://www.lintcode.com/problem/excel-sheet-column-title/
#########################################################################
def convertToTitle(n):
    charlist = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    if n <= 0:
        return res
    while n:
        res = charlist[(n-1)%26] + res 
        n = (n-1)/26
    return res



print 1, convertToTitle(1)
print 26, convertToTitle(26)
print 27, convertToTitle(27)
print 53, convertToTitle(53)
print 54, convertToTitle(54)
