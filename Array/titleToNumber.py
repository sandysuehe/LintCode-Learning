#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-08-22 13:11:51
# File Name: titleToNumber.py
# Description: Excel Sheet Column Title 求Excel表列名称
# LintCode: https://www.lintcode.com/problem/excel-sheet-column-number/ 
#########################################################################
def titleToNumber(s):
    n = len(s) 
    ans = 0

    for i in range(n):
        ans = ans*26 + (ord(s[i])-ord('A')) + 1
    return ans


print 'A', titleToNumber('A')
print 'Z', titleToNumber('Z')
print 'AB', titleToNumber('AB')
