#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: (sandysuehe@gmail.com)
#########################################################################
# Created Time: 2018-10-25 13:50:33
# File Name: atoi.py
# Description: atoi
# LintCode: https://www.lintcode.com/problem/string-to-integer-atoi/
# 注意: sys.maxint = 9223372036854775807
#########################################################################
def atoi(strs):
    import sys
    maxint = sys.maxint
    minint = -sys.maxint-1 
    if not strs:
        return 0

    flag = 1
    num = 0
    i = 0
    n = len(strs)

    while i < n and strs[i] == " ":
        i += 1

    if strs[i] in ("+", "-"):
        if strs[i] == "-":
            flag = -1
        else:
            flag = 1

    while i < n and strs[i].isdigit():
        if num > maxint/10 or (num == maxint/10 and int(strs[i])>7):
            if flag == 1:
                return maxint
            else:
                return minint
        num = 10 * num + int(strs[i])
        i += 1

    return num * flag
# vim: set noexpandtab ts=4 sts=4 sw=4 :
